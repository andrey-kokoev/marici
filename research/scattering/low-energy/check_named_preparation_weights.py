"""Absolute named central point weights from symmetric matrix residues."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_carrier_retained_weights as carrier

e=carrier.e;p=e.p;bound=carrier.bound;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/named-preparation-weights.v1.json'
PROOF=HOME/'NAMED-PREPARATION-WEIGHTS.md'
RESULT=HOME/'results/named-preparation-weights.v1.json'
F,pa,ps,pm,peval=carrier.F,carrier.pa,carrier.ps,carrier.pm,carrier.peval


def poly_matrix_product(A,B):
    return [[pa(*(pm(A[i][k],B[k][j]) for k in range(len(B))))
             for j in range(len(B[0]))] for i in range(len(A))]

def determinant_and_adjugate(A):
    n=len(A);cache={}
    def det(rows,cols):
        key=(rows,cols)
        if key not in cache:
            if not rows:value=[F(1)]
            else:
                terms=[]
                for k,j in enumerate(cols):
                    if A[rows[0]][j]!=[F()]:
                        term=pm(A[rows[0]][j],det(rows[1:],cols[:k]+cols[k+1:]))
                        terms.append(ps(F((-1)**k),term))
                value=pa(*terms) if terms else [F()]
            cache[key]=value
        return cache[key]
    indices=tuple(range(n));D=det(indices,indices)
    adj=[[ps(F((-1)**(i+j)),det(indices[:j]+indices[j+1:],indices[:i]+indices[i+1:]))
          for j in range(n)] for i in range(n)]
    product=poly_matrix_product(A,adj)
    assert product==[[D if i==j else [F()] for j in range(n)] for i in range(n)]
    return D,adj

def quadratic_numerator(adj,G,v):
    row=p.mm(p.transpose(v),G)[0];norm=p.mm([row],v)[0][0]
    assert norm.positive();n=len(v)
    J=pa(*(ps(row[i]*v[j][0]/norm,adj[i][j]) for i in range(n) for j in range(n)))
    return J,norm

def symmetric_data():
    src=json.loads(p.base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=p.decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    data=bound.audit_core(K,H)['symmetric'];assert data['point_dimension']==2
    A,C,G,L=data['A'],data['C'],data['G'],data['L'];n=len(A);assert n==5
    assert p.rank(C)==2 and p.inertia(p.mm(G,C))==(2,0,3)
    assert p.mm(C,C)==C
    # B(s)=s M(s)=(1+s)^2 I-s A-s(1+s)C.
    B=[[pa([F(int(i==j)),2*F(int(i==j))-A[i][j]-C[i][j],F(int(i==j))-C[i][j]])
        for j in range(n)] for i in range(n)]
    D,adj=determinant_and_adjugate(B);assert D[0]==F(1)
    numerators={};vectors={}
    for name,seed in (('belt',[int(i==0) for i in range(11)]),
                      ('carrier_sum',[int(i in (1,2)) for i in range(11)])):
        v=p.mm(L,[[F(x)] for x in seed]);J,norm=quadratic_numerator(adj,G,v)
        assert J[0]==F(1)
        assert norm==F(Q(1196,15) if name=='belt' else 40)
        numerators[name]=J;vectors[name]={'coordinates':v,'norm':norm}
    data['initial_norm_squared']={name:entry['norm'] for name,entry in vectors.items()}
    # Direct rational probes bind weighted adjugate numerators to M(s)^(-1).
    for s in (Q(1,3),Q(1,2)):
        M=bound.boundary_matrix(A,C,s);inv=p.invert(M)
        for name,entry in vectors.items():
            v=entry['coordinates'];direct=p.mm(p.mm(p.mm(p.transpose(v),G),inv),v)[0][0]/entry['norm']
            assert direct==F(s)*peval(numerators[name],F(s))/peval(D,F(s))
    return data,D,numerators

def symmetric_weight_interval(J,D,a,b):
    s=(F(a),F(b));s2=carrier.imul(s,s)
    numerator=carrier.imul(carrier.iadd(s2,(-F(1),-F(1))),carrier.ipoly(J,s))
    denominator=carrier.imul(s,carrier.ipoly(carrier.derivative(D),s))
    return carrier.idiv(numerator,denominator)


def assemble_named(common,antisymmetric):
    tables={}
    for label,a in antisymmetric.items():
        single=tuple((x+y)/2 for x,y in zip(common['carrier_sum'],a))
        tables[label]={'belt':common['belt'],'carrier_sum':common['carrier_sum'],
                       'carrier_difference':a,'carrier_1':single,'carrier_2':single}
        assert all(0<=lo<=hi<=1 for lo,hi in tables[label].values())
    return tables

def certify_energy_separation(modes):
    intervals=sorted(tuple(Q(x) for x in m['energy_bracket']) for m in modes)
    assert all(a[1]<b[0] for a,b in zip(intervals,intervals[1:])),'unresolved cross-sector energy coincidence'
    return [[str(x) for x in interval] for interval in intervals]

def validate_contract(c):
    assert c['schema']=='marici.scattering.named-preparation-weights.v1'
    assert ROOT/c['carrier_weight_certificate']==carrier.RESULT
    assert len(c['symmetric_root_brackets'])==2
    assert c['root_refinement_steps']==50 and c['rational_weight_grid']==10**12
    assert c['absolute_named_weights_evaluated'] is True
    for key in ('coherent_mixture_weights_from_diagonals_claimed','full_visible_retained_quadratic_form_certified',
                'complement_declared_escaped','physical_capture_or_branching_ratio_claimed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=carrier.build();assert parent==json.loads(carrier.RESULT.read_text(encoding='utf-8')),'stale carrier-weight input'
    assert parent['symmetric_preparation_weights_still_exact'] is True
    data,D,Js=symmetric_data();assert len(D)==9 and all(len(J)==8 for J in Js.values())
    brackets=[(Q(a),Q(b)) for a,b in c['symmetric_root_brackets']]
    assert all(0<a<b<1 and b-a==Q(1,1024) for a,b in brackets)
    assert brackets[0][1]<brackets[1][0] and len(brackets)==data['point_dimension']
    totals={name:(F(),F()) for name in Js};modes=[]
    for a,b in brackets:
        coarse=(a,b);a,b=carrier.refine_root(D,a,b,c['root_refinement_steps'])
        mode={'coarse_decay_bracket':[str(x) for x in coarse],'decay_bracket':[str(a),str(b)],
              'energy_bracket':[str(bound.energy(b)),str(bound.energy(a))],
              'secular_endpoint_signs':[carrier.sign(peval(D,F(a))),carrier.sign(peval(D,F(b)))],
              'weight_enclosures':{}}
        for name,J in Js.items():
            weight=symmetric_weight_interval(J,D,a,b);assert carrier.less(F(),weight[0])
            totals[name]=carrier.iadd(totals[name],weight)
            rational=carrier.outward(weight,c['rational_weight_grid'])
            mode['weight_enclosures'][name]={'field':carrier.encode_interval(weight),'rational':[str(x) for x in rational]}
        modes.append(mode)
    common={name:carrier.outward(weight,c['rational_weight_grid']) for name,weight in totals.items()}
    assert common['belt']==tuple(Q(x) for x in c['common_belt_weight_enclosure'])
    assert common['carrier_sum']==tuple(Q(x) for x in c['common_carrier_sum_weight_enclosure'])
    anti={label:tuple(Q(x) for x in parent[label]['total_rational_enclosure']) for label in ('native','enriched')}
    tables=assemble_named(common,anti)
    for label in ('native','enriched'):
        assert tables[label]['carrier_1']==tuple(Q(x) for x in c[label+'_single_carrier_weight_enclosure'])
    separation={label:certify_energy_separation(modes+parent[label]['modes']) for label in ('native','enriched')}
    assert len(separation['native'])==5 and len(separation['enriched'])==3
    # The reduced preparations are exactly embedded, not independently fitted.
    enriched=json.loads(e.RESULT.read_text(encoding='utf-8'));E=p.decode(enriched['embedding'])
    for seed in ([1,0,0],[0,1,1],[0,1,-1],[0,1,0],[0,0,1]):
        p.require_equal(p.mm(E,[[F(x)] for x in seed+[0]*6]),[[F(x)] for x in seed+[0]*8])
    controls=[]
    for name in ('force-rank-one-contact','forget-initial-metric-norm','omit-weak-symmetric-mode',
                 'inherit-native-antisymmetric-weight','coherent-mixture-by-diagonal-averaging',
                 'declare-complement-escaped','admit-physical-branching'):
        try:
            if name=='force-rank-one-contact':assert p.rank(data['C'])==1
            elif name=='forget-initial-metric-norm':assert F(Q(1196,15))*Js['belt'][0]==F(1)
            elif name=='omit-weak-symmetric-mode':assert len(modes)==1
            elif name=='inherit-native-antisymmetric-weight':assert anti['native']==anti['enriched']
            else:
                bad=copy.deepcopy(c)
                key={'coherent-mixture-by-diagonal-averaging':'coherent_mixture_weights_from_diagonals_claimed',
                     'declare-complement-escaped':'complement_declared_escaped',
                     'admit-physical-branching':'physical_capture_or_branching_ratio_claimed'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile named-weight control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((carrier.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_named_preparation_weights.py'))
    return {'schema':'marici.scattering.named-preparation-weights-receipt.v1','status':'pass',
        'scope_verdict':'absolute_named_central_full_tail_point_weights',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'symmetric_core_dimension':5,'symmetric_contact_rank':2,'symmetric_point_dimension':2,
        'symmetric_operator':p.base.encoded(data['A']),'symmetric_metric':p.base.encoded(data['G']),
        'symmetric_contact':p.base.encoded(data['C']),
        'initial_raw_norm_squared':{name:v.encoded() for name,v in data['initial_norm_squared'].items()},
        'secular_polynomial':[v.encoded() for v in D],
        'weighted_adjugate_numerators':{name:[v.encoded() for v in J] for name,J in Js.items()},
        'polynomial_adjugate_identity_verified':True,'symmetric_modes':modes,
        'common_symmetric_total_field_enclosures':{name:carrier.encode_interval(weight) for name,weight in totals.items()},
        'common_symmetric_total_rational_enclosures':{name:[str(x) for x in interval] for name,interval in common.items()},
        'absolute_named_weight_enclosures':{label:{name:[str(x) for x in interval] for name,interval in table.items()}
                                           for label,table in tables.items()},
        'single_carrier_native_minus_enriched_enclosure':parent['single_carrier_native_minus_enriched_enclosure'],
        'cross_sector_point_energy_intervals':separation,
        'exact_equality_for_symmetric_preparations':True,'all_named_point_contributions_accounted':True,
        'absolute_named_weights_evaluated':True,'coherent_mixture_weights_from_diagonals_claimed':False,
        'full_visible_retained_quadratic_form_certified':False,'complement_declared_escaped':False,
        'physical_capture_or_branching_ratio_claimed':False,'numerical_search_used_as_proof':False,
        'analytic_argument_machine_formalized':False,'native_owner_solver_replayed':False,
        'historical_ancestor_freshness_claimed':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale absolute named weights'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':r['status'],'absolute_named_weight_enclosures':r['absolute_named_weight_enclosures'],
        'all_named_point_contributions_accounted':True,'hostile_controls_refused':r['hostile_controls_refused']}))


if __name__=='__main__':main()
