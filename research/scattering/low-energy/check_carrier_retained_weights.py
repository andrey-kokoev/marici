"""Full-tail carrier-difference point weights via exact residue enclosures."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_enriched_bound_sector as bound

e=bound.enrichment;p=e.p;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/carrier-retained-weights.v1.json'
PROOF=HOME/'CARRIER-RETAINED-WEIGHTS.md'
RESULT=HOME/'results/carrier-retained-weights.v1.json'
F,pa,ps,pm,peval=e.F,e.pa,e.ps,e.pm,e.peval


def derivative(a):return e.trim([F(i)*a[i] for i in range(1,len(a))] or [F()])
def lift(poly,degree):
    # s^degree poly((1+s)^2/s), with no negative powers.
    assert len(poly)-1<=degree
    r=[F()];power=[F(1)];step=[F(1),F(2),F(1)]
    for k,c in enumerate(poly):
        r=pa(r,[F()]*(degree-k)+ps(c,power));power=pm(power,step)
    return e.trim(r)
def secular_polynomials(num,den):
    d=len(den)-1;N=lift(num,d-1);D=lift(den,d)
    secular=pa(D,pm([F(),F(1),F(1)],N))
    assert secular[0]==F(1)
    return N,secular

def sign(x):return 0 if x==F() else (1 if x.positive() else -1)
def refine_root(poly,a,b,steps):
    assert 0<a<b<1
    sa,sb=sign(peval(poly,F(a))),sign(peval(poly,F(b)))
    assert sa*sb==-1,'no strict root sign change'
    for _ in range(steps):
        mid=(a+b)/2;sm=sign(peval(poly,F(mid)))
        assert sm!=0,'exact rational root requires a separate certificate'
        if sm==sa:a=mid
        else:b=mid
    return a,b

def less(a,b):return (b-a).positive()
def ordered(values):
    lo=hi=values[0]
    for v in values[1:]:
        if less(v,lo):lo=v
        if less(hi,v):hi=v
    return lo,hi

def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def ineg(a):return -a[1],-a[0]
def imul(a,b):return ordered([x*y for x in a for y in b])
def idiv(a,b):
    assert sign(b[0])*sign(b[1])==1,'interval denominator contains zero'
    return imul(a,(F(1)/b[1],F(1)/b[0]))
def ipoly(poly,x):
    value=(F(),F())
    for c in reversed(poly):value=iadd(imul(value,x),(c,c))
    return value

def weight_interval(N,secular,a,b):
    s=(F(a),F(b));s2=imul(s,s)
    numerator=imul(iadd((F(1),F(1)),ineg(s2)),ipoly(N,s))
    denominator=imul(s,ipoly(derivative(secular),s))
    return idiv(numerator,denominator)


def floor_unit(x,grid):
    assert sign(x)>=0 and less(x,F(1)),'weight enclosure outside [0,1)'
    a,b=0,grid
    while b-a>1:
        mid=(a+b)//2
        if less(x,F(Q(mid,grid))):b=mid
        else:a=mid
    return a

def outward(weight,grid):
    assert not less(weight[1],weight[0])
    return Q(floor_unit(weight[0],grid),grid),Q(floor_unit(weight[1],grid)+1,grid)

def encode_interval(interval):return [x.encoded() for x in interval]

def audit_weights(num,den,brackets,count,steps,grid):
    assert den[-1]==F(1) and num[-1]==F(-1),'unit-normalized port compliance required'
    N,secular=secular_polynomials(num,den)
    assert len(brackets)==count
    assert all(0<a<b<1 for a,b in brackets)
    assert all(b<c for (a,b),(c,d) in zip(brackets,brackets[1:])),'overlapping root witnesses'
    # Disjoint strict sign changes give >=count distinct roots. The parent
    # proves exactly count simple point roots, so these exhaust them.
    modes=[];total=(F(),F())
    for a,b in brackets:
        coarse=(a,b);a,b=refine_root(secular,a,b,steps)
        weight=weight_interval(N,secular,a,b);assert less(F(),weight[0])
        rational=outward(weight,grid);total=iadd(total,weight)
        modes.append({'coarse_decay_bracket':[str(x) for x in coarse],
            'decay_bracket':[str(a),str(b)],'energy_bracket':[str(bound.energy(b)),str(bound.energy(a))],
            'secular_endpoint_signs':[sign(peval(secular,F(a))),sign(peval(secular,F(b)))],
            'full_tail_weight_field_enclosure':encode_interval(weight),
            'full_tail_weight_rational_enclosure':[str(x) for x in rational]})
    rational=outward(total,grid)
    return {'scaled_core_numerator':N,'secular':secular,'modes':modes,
            'total_field':total,'total_rational':rational}


def validate_contract(c):
    assert c['schema']=='marici.scattering.carrier-retained-weights.v1'
    assert ROOT/c['point_sector_certificate']==bound.RESULT
    assert c['root_refinement_steps']==50 and c['rational_weight_grid']==10**12
    assert len(c['native_root_brackets'])==3 and len(c['enriched_root_brackets'])==1
    for key in ('absolute_single_carrier_weights_evaluated','arbitrary_preparation_error_bound_claimed',
                'complement_declared_escaped','physical_capture_or_branching_ratio_claimed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=bound.build();assert parent==json.loads(bound.RESULT.read_text(encoding='utf-8')),'stale point-sector input'
    enrichment=json.loads(e.RESULT.read_text(encoding='utf-8'))
    pol={key:[F(*v) for v in values] for key,values in enrichment['scalar_polynomials'].items()}
    counts={label:parent[label]['antisymmetric']['point_dimension'] for label in ('native','enriched')}
    assert counts=={'native':3,'enriched':1}
    grid=c['rational_weight_grid'];steps=c['root_refinement_steps'];audits={};brackets={}
    for label,prefix in (('native','native'),('enriched','reduced')):
        brackets[label]=[(Q(a),Q(b)) for a,b in c[label+'_root_brackets']]
        audits[label]=audit_weights(pol[prefix+'_numerator'],pol[prefix+'_denominator'],
                                    brackets[label],counts[label],steps,grid)
        expected=tuple(Q(x) for x in c[label+'_weight_enclosure'])
        assert audits[label]['total_rational']==expected,'unexpected total weight enclosure'
    n=audits['native']['total_rational'];r=audits['enriched']['total_rational']
    gap=(n[0]-r[1],n[1]-r[0]);single=(gap[0]/2,gap[1]/2)
    assert gap[0]>0 and single==tuple(Q(x) for x in c['single_carrier_native_minus_enriched_enclosure'])
    assert parent['symmetric_preparation_bound_weights_exactly_preserved'] is True
    a,b=[Q(x) for x in audits['enriched']['modes'][0]['decay_bracket']]
    weight=audits['enriched']['total_field']
    tail=(F(bound.tail_factor(a)),F(bound.tail_factor(b)))
    core_only=idiv(weight,iadd((F(1),F(1)),ineg(imul(tail,weight))))
    excess=iadd(core_only,ineg(weight));assert less(F(Q(1,2500)),excess[0])
    controls=[]
    for name in ('omit-weak-native-mode','normalize-core-only','claim-identical-weights',
                 'promote-to-all-preparations','declare-complement-escaped','admit-physical-branching'):
        try:
            if name=='omit-weak-native-mode':
                audit_weights(pol['native_numerator'],pol['native_denominator'],brackets['native'][1:],3,steps,grid)
            elif name=='normalize-core-only':assert not less(F(),excess[0])
            elif name=='claim-identical-weights':assert gap[0]<=0
            else:
                bad=copy.deepcopy(c)
                key={'promote-to-all-preparations':'arbitrary_preparation_error_bound_claimed',
                     'declare-complement-escaped':'complement_declared_escaped',
                     'admit-physical-branching':'physical_capture_or_branching_ratio_claimed'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile retained-weight control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((bound.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_carrier_retained_weights.py'))
    def payload(data):
        return {'mode_count':len(data['modes']),'modes':data['modes'],
                'scaled_core_numerator':[v.encoded() for v in data['scaled_core_numerator']],
                'secular_polynomial':[v.encoded() for v in data['secular']],
                'total_field_enclosure':encode_interval(data['total_field']),
                'total_rational_enclosure':[str(x) for x in data['total_rational']]}
    return {'schema':'marici.scattering.carrier-retained-weights-receipt.v1','status':'pass',
        'scope_verdict':'full_tail_named_carrier_retained_weight_comparison',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'preparation':'unit_normalized_initially_central_carrier_difference_with_zero_leads',
        'native':payload(audits['native']),'enriched':payload(audits['enriched']),
        'native_minus_enriched_enclosure':[str(x) for x in gap],
        'single_carrier_native_minus_enriched_enclosure':[str(x) for x in single],
        'root_refinement_steps':steps,'rational_outward_grid':grid,'all_antisymmetric_point_modes_accounted':True,
        'symmetric_preparation_weights_still_exact':True,
        'enriched_core_only_normalization_excess_enclosure':encode_interval(excess),
        'enriched_core_only_normalization_excess_strict_lower_bound':'1/2500',
        'absolute_single_carrier_weights_evaluated':False,'arbitrary_preparation_error_bound_claimed':False,
        'complement_declared_escaped':False,'physical_capture_or_branching_ratio_claimed':False,
        'numerical_search_used_as_proof':False,'analytic_argument_machine_formalized':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale carrier retained weights'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':r['status'],'native_weight_enclosure':r['native']['total_rational_enclosure'],
        'enriched_weight_enclosure':r['enriched']['total_rational_enclosure'],
        'single_carrier_difference_enclosure':r['single_carrier_native_minus_enriched_enclosure'],
        'all_antisymmetric_point_modes_accounted':True,'hostile_controls_refused':r['hostile_controls_refused']}))


if __name__=='__main__':main()
