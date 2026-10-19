"""One native hidden enrichment and a denominator-cleared full-band bound."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import check_native_projection_full_band_obstruction as old

p=old.p;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/resonant-native-enrichment.v1.json'
PROOF=HOME/'RESONANT-NATIVE-ENRICHMENT.md'
RESULT=HOME/'results/resonant-native-enrichment.v1.json'
F,mm,eye,scale,invert=p.F,p.mm,p.eye,p.scale,p.invert
transpose,decode,difference,zeros=p.transpose,p.decode,p.difference,p.zeros


def equal(A,B):assert A==B,'enrichment identity failed'
def trim(a):
    a=a[:]
    while len(a)>1 and a[-1]==F():a.pop()
    return a

def pa(*arrays):
    r=[F()]*max(map(len,arrays))
    for a in arrays:
        for i,v in enumerate(a):r[i]=r[i]+v
    return trim(r)
def ps(c,a):return trim([c*x for x in a])
def pm(a,b):
    r=[F()]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]=r[i+j]+x*y
    return trim(r)
def peval(a,x):
    v=F()
    for c in reversed(a):v=v*x+c
    return v

def pdivmod(a,b):
    assert b!=[F()],'zero polynomial divisor'
    remainder=trim(a);quotient=[F()]*max(1,len(a)-len(b)+1)
    while remainder!=[F()] and len(remainder)>=len(b):
        k=len(remainder)-len(b);c=remainder[-1]/b[-1];quotient[k]=quotient[k]+c
        remainder=pa(remainder,ps(-c,[F()]*k+b))
    return trim(quotient),remainder

def certify_coprime(a,b):
    while b!=[F()]:a,b=b,pdivmod(a,b)[1]
    assert len(a)==1 and a[0]!=F(),'non-coprime compliance representation'
    return True

def compliance_polynomials(model):
    A,G,u=model['A'],model['G'],model['u'];norm=model['norm'];n=len(A)
    B=eye(n);coefficients=[F(1)];adjoint_moments=[]
    for k in range(1,n+1):
        adjoint_moments.append(mm(mm(mm(transpose(u),G),B),u)[0][0]/norm)
        AB=mm(A,B);c=-sum((AB[i][i] for i in range(n)),F())/k
        coefficients.append(c);B=p.add(AB,scale(c,eye(n)))
    equal(B,zeros(n,n))  # Exact Cayley-Hamilton / adjugate recurrence.
    q=list(reversed(coefficients));num=list(reversed([-x for x in adjoint_moments]))
    return trim(num),trim(q)

def scattering_polynomials(native,reduced):
    nn,qn=compliance_polynomials(native);nr,qr=compliance_polynomials(reduced)
    e=[F(),F(1)];gamma2=[F(),F(4),F(-1)]
    dn=pa(pm(qn,qn),pm(e,pm(qn,nn)),pm(e,pm(nn,nn)))
    dr=pa(pm(qr,qr),pm(e,pm(qr,nr)),pm(e,pm(nr,nr)))
    cross=pa(pm(nn,qr),ps(F(-1),pm(nr,qn)))
    numerator=pm(gamma2,pm(cross,cross));denominator=pm(dn,dr)
    return {'native_numerator':nn,'native_denominator':qn,'reduced_numerator':nr,
            'reduced_denominator':qr,'cross':cross,'error_numerator':numerator,'error_denominator':denominator}

def bernstein_coefficients(poly):
    n=len(poly)-1
    return [sum((poly[k]*F(Q(comb(i,k)*4**k,comb(n,k))) for k in range(i+1)),F()) for i in range(n+1)]
def split_bernstein(coeff):
    rows=[coeff]
    while len(rows[-1])>1:rows.append([(a+b)/2 for a,b in zip(rows[-1],rows[-1][1:])])
    return [row[0] for row in rows],[row[-1] for row in reversed(rows)]
def certify_nonnegative(poly,max_depth=16):
    leaves=[]
    def visit(coeff,a,b,depth):
        if all(v==F() or v.positive() for v in coeff):
            minimum=coeff[0]
            for v in coeff[1:]:
                if (minimum-v).positive():minimum=v
            leaves.append({'interval':[str(a),str(b)],'depth':depth,'minimum_coefficient':minimum.encoded()});return
        assert depth<max_depth,'uncertified Bernstein cell: '+str((a,b))
        left,right=split_bernstein(coeff);mid=(a+b)/2
        visit(left,a,mid,depth+1);visit(right,mid,b,depth+1)
    visit(bernstein_coefficients(poly),Q(0),Q(4),0)
    return leaves


def construct():
    parent=old.build();assert parent==json.loads(old.RESULT.read_text(encoding='utf-8')),'stale full-band parent'
    prior=json.loads(p.RESULT.read_text(encoding='utf-8'))
    source=json.loads(p.base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(source['joint_generator']);h=[F(*v) for v in source['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    Eold=decode(prior['embedding']);Wold=[row[3:] for row in Eold[3:]]
    HQ=[row[3:] for row in H[3:]];QQ=[row[3:] for row in K[3:]];QP=[row[:3] for row in K[3:]]
    X=mm(invert(difference(QQ,scale(F(Q(2,5)),eye(8)))),QP)
    span=p.Span(8)
    for col in transpose(Wold):span.add(col,{})
    assert len(span.rows)==5
    for col in transpose(X):span.add(col,{})
    assert len(span.rows)==6
    W=transpose(p.canonical_rows(span));HW=mm(mm(transpose(W),HQ),W)
    LW=mm(mm(invert(HW),transpose(W)),HQ)
    E=p.block(eye(3),zeros(3,6),zeros(8,3),W)
    L=p.block(eye(3),zeros(3,8),zeros(6,3),LW)
    Kr=mm(mm(L,K),E);Hr=mm(mm(transpose(E),H),E)
    equal(mm(L,E),eye(9));assert p.inertia(Hr)==(9,0,0)
    assert p.inertia(mm(Hr,Kr))==(8,0,1)
    nested=mm(L,Eold);equal(mm(E,nested),Eold)
    equal(mm(mm(transpose(nested),Hr),nested),decode(prior['full_metric']))
    ground=mm(Eold,decode(prior['reduced_ground_vector']));vr=mm(L,ground)
    equal(mm(E,vr),ground);equal(mm(Kr,vr),zeros(9,1));equal(vr[:3],ground[:3])
    equal(mm(mm(transpose(vr),Hr),vr),mm(mm(transpose(ground),H),ground))
    R=difference(mm(K,E),mm(E,Kr));assert p.rank(R)==1
    sym=p.cyclic(K,[[F(int(i==0)) for i in range(11)],[F(int(i in (1,2))) for i in range(11)]])
    symr=mm(L,sym);equal(mm(E,symr),sym);equal(mm(R,symr),zeros(11,5))
    Pn=[[F(int(i==j and i<3)) for j in range(11)] for i in range(11)]
    Pr=[[F(int(i==j and i<3)) for j in range(9)] for i in range(9)]
    equal(mm(Pn,E),mm(E,Pr))
    # The same hidden transfer is now matched at a positive-band witness too.
    Ar=[row[3:] for row in Kr[3:]];Br=[row[:3] for row in Kr[3:]];Cr=[row[3:] for row in Kr[:3]]
    PQ=[row[3:] for row in K[:3]]
    for z in (Q(-1),Q(-2),Q(2,5)):
        xn=mm(invert(difference(QQ,scale(F(z),eye(8)))),QP)
        yr=mm(invert(difference(Ar,scale(F(z),eye(6)))),Br)
        equal(mm(W,yr),xn);equal(mm(PQ,xn),mm(Cr,yr))
    native=old.preceding.sector(K,H,6,Q(1,8))
    enriched=old.preceding.sector(Kr,Hr,4,Q(1,8))
    qa9=mm(enriched['B'],enriched['L']);qa_native=mm(native['B'],native['L'])
    equal(mm(qa_native,E),mm(E,qa9))
    old_time=json.loads(old.preceding.time_error.RESULT.read_text(encoding='utf-8'))
    qa8=difference(eye(8),decode(old_time['symmetric_core_projector']))
    equal(mm(qa9,nested),mm(nested,qa8))
    old_anti=old.model(json.loads(old.preceding.RESULT.read_text(encoding='utf-8'))['reduced_antisymmetric'])
    counts={}
    for name,m in (('native',native),('old_eight_state',old_anti),('enriched',enriched)):
        shifted=difference(m['A'],scale(F(4),eye(len(m['A']))))
        counts[name]=list(p.inertia(mm(m['G'],shifted)))
    assert counts=={'native':[3,3,0],'old_eight_state':[1,2,0],'enriched':[1,3,0]}
    return parent,prior,E,L,Kr,Hr,native,enriched,counts


def validate_contract(c):
    assert c['schema']=='marici.scattering.resonant-native-enrichment.v1'
    assert ROOT/c['preceding_obstruction']==old.RESULT and ROOT/c['old_projection']==p.RESULT
    assert Q(c['added_hidden_snapshot_energy'])==Q(2,5)
    assert c['hidden_dimension']==6 and c['full_core_dimension']==9
    assert Q(c['full_band_scattering_norm_error_upper_bound'])==Q(1,4)
    assert c['minimum_core_dimension_in_declared_class']==9
    for key in ('global_minimum_among_arbitrary_fitted_models_claimed','all_energy_identity_claimed',
                'native_bound_counts_inherited','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent,prior,E,L,Kr,Hr,native,enriched,counts=construct()
    pol=scattering_polynomials(native,enriched)
    for label,model in (('native',native),('reduced',enriched)):
        certify_coprime(pol[label+'_numerator'],pol[label+'_denominator'])
        for z in (Q(-1),Q(-2),Q(2,5),Q(39,10)):
            n=peval(pol[label+'_numerator'],F(z));q=peval(pol[label+'_denominator'],F(z))
            assert q!=F() and n/q==old.compliance(model,z)
    multiplicities={}
    assert pol['cross']!=[F()]
    for z in (Q(-1),Q(-2),Q(2,5)):
        rem=pol['cross'];multiplicity=0
        while len(rem)>1 and peval(rem,F(z))==F():
            rem,r=pdivmod(rem,[-F(z),F(1)]);assert r==[F()];multiplicity+=1
        assert multiplicity==2;multiplicities[str(z)]=multiplicity
    equal(old.evaluate(native,enriched,Q(2,5))['d2'],F())
    B=pa(pol['error_denominator'],ps(F(-16),pol['error_numerator']))
    cells=certify_nonnegative(B)
    assert len(B)==19 and len(cells)==5
    z=Q(39,10);d2=peval(pol['error_numerator'],F(z))/peval(pol['error_denominator'],F(z))
    assert d2==old.evaluate(native,enriched,z)['d2']
    assert (d2-F(Q(9,50)**2)).positive()
    controls=[]
    for name in ('keep-the-old-five-hidden-space','claim-full-identity','understate-full-band-error',
                 'cancel-denominator-without-checking','promote-global-fit-minimality','admit-physical-outcomes'):
        try:
            if name=='keep-the-old-five-hidden-space':assert len(Kr)==8
            elif name=='claim-full-identity':assert pol['cross']==[F()]
            elif name=='understate-full-band-error':assert (F(Q(1,10)**2)-d2).positive()
            elif name=='cancel-denominator-without-checking':
                factor=[F(-1),F(1)];certify_coprime(pm(factor,pol['native_numerator']),pm(factor,pol['native_denominator']))
            else:
                bad=copy.deepcopy(c)
                bad['global_minimum_among_arbitrary_fitted_models_claimed' if name=='promote-global-fit-minimality' else 'physical_outcomes_admitted']=True
                validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile enrichment control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((old.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_resonant_native_enrichment.py'))
    return {'schema':'marici.scattering.resonant-native-enrichment-receipt.v1','status':'pass',
        'scope_verdict':'nine_state_endpoint_ground_and_full_band_controlled_native_projection',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'full_core_dimension':9,'hidden_dimension':6,'old_hidden_dimension':5,'added_hidden_dimension':1,
        'weighted_core_inertia':[8,0,1],'embedding':p.base.encoded(E),'metric_adjoint':p.base.encoded(L),
        'reduced_core':p.base.encoded(Kr),'full_metric':p.base.encoded(Hr),
        'ground_direction_and_norm_preserved':True,'symmetric_sector_still_exact':True,
        'conditional_householder_limit_preserved':True,'old_low_window_bound_retained_by_ordering':True,
        'interpolation_points':['-1','-2','2/5'],'cross_polynomial_zero_multiplicities':multiplicities,
        'global_intertwining_residual_rank':1,
        'antisymmetric_closed_core_inertias_at_4':counts,
        'antisymmetric_in_band_closed_core_pole_counts':{'native':3,'old_eight_state':2,'enriched':3},
        'scalar_polynomials':{key:[v.encoded() for v in values] for key,values in pol.items()},
        'cleared_bound_polynomial':[v.encoded() for v in B],
        'compliance_pairs_coprime_verified':True,'bernstein_degree':18,'bernstein_cells':cells,
        'full_band_scattering_norm_error_upper_bound':'1/4','outgoing_packet_norm_error_bound':'alpha_in/4',
        'common_effect_probability_error_bound':'alpha_in/2',
        'lower_witness':{'energy':'39/10','norm_error_squared':d2.encoded(),'norm_error_strict_lower_bound':'9/50'},
        'minimum_core_dimension_in_native_endpoint_projection_class_for_error_below_2':9,
        'global_minimum_among_arbitrary_fitted_models_claimed':False,'all_energy_identity_claimed':False,
        'native_bound_counts_inherited':False,'analytic_argument_machine_formalized':False,
        'physical_energy_or_detector_binding_claimed':False,'native_owner_solver_replayed':False,
        'historical_ancestor_freshness_claimed':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale resonant native enrichment'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','full_core_dimension','added_hidden_dimension','full_band_scattering_norm_error_upper_bound',
          'antisymmetric_in_band_closed_core_pole_counts','bernstein_degree','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
