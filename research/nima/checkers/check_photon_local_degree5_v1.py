"""Twelve regular local photon tensor generators through degree five (exact Q)."""
import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_local_ward_basis_v1 as base
NAMES=base.NAMES+('g5','g5prime','f5','h5');DEGREES=base.DEGREES+(5,5,5,5)
CONTRACT=HOME/'contracts/photon-local-degree5-v1.json';PROOF=HOME/'photon-local-degree5-v1.md'
TEST=HOME/'checkers/test_photon_local_degree5_v1.py';MANIFEST=HOME/'scc-models/photon-local-degree5-v1.json'
RESULT=HOME/'results/photon-local-degree5-v1.json'


def covariants(q,e):
    old=base.covariants(q,e);F,T=zip(*(base.fields(p,v) for p,v in zip(q,e)))
    s={(i,j):base.determinant(base.ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    S2=sum((s[i,j]**2 for i,j in combinations(range(4),2)),Q())/2;G5=Gp=Q()
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j))
        x=(s[i,j]+s[k,l])/2
        w=(s[i,k]*s[i,l]+s[j,k]*s[j,l]+s[k,i]*s[k,j]+s[l,i]*s[l,j])/4
        P=base.contract(F[i],F[j])*base.contract(T[k],T[l])
        G5+=P*x**3;Gp+=P*x*w
    return old+(G5,Gp,S2*old[3],S2*old[4])


def oracle(a,b,h):
    old=base.spinor_oracle(a,b,h);inv=lambda i,j:base.bracket(a[i],a[j])*base.bracket(b[i],b[j])
    S2=sum((inv(i,j)**2 for i,j in combinations(range(4),2)),Q())/2
    plus=[i for i in range(4) if h[i]==1];g5=gp=Q()
    if len(plus)==2:
        i,j=plus;k,l=tuple(n for n in range(4) if n not in plus);x=inv(i,j)
        g5=old[0]*x**3;gp=old[0]*x*inv(i,k)*inv(i,l)
    return old+(g5,gp,S2*old[3],S2*old[4])


def rows(c=Q(3,5),s=Q(4,5),scale=Q(1)):
    a,b,q=base.cm(c,s,scale)
    return tuple(covariants(q,base.polarizations(a,b,h)) for h in base.PHI)


def forward_map():
    phi=rows(Q(1),Q())
    return tuple(tuple(x if DEGREES[j]==n else Q() for j,x in enumerate(phi[i]))
                 for i,n in ((0,2),(0,3),(0,4),(1,2),(1,4),(0,5)))


def validate(c):
    assert c['schema']=='marici.photon-local-degree5.v1' and c['owner']=='marici.Nima'
    assert c['coefficient_order']==list(NAMES) and c['degrees']==list(DEGREES)
    assert c['completeness_scope']=='regular_parity_even_on_shell_helicity_polynomial_jet_not_off_shell_operator_classification'
    for k in ('explicit_twelve_generators_constructed','rank_twelve_coefficient_witness','rank_six_forward_jet',
              'independent_single_minus_h5_retained'):
        assert c[k] is True,k
    for k in ('degree_five_log_window_tensor_constructed','general_dim10_Born_loop_inventory_derived',
              'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=base.build()
    counts={k:0 for k in ('helicity','gauge_patch','Bose','Ward','Lorentz','parity')}
    for cc,ss in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        a,b,q=base.cm(cc,ss)
        for h in product((1,-1),repeat=4):
            e=base.polarizations(a,b,h);got=covariants(q,e)
            assert got==oracle(a,b,h);counts['helicity']+=1
            assert covariants(q,base.polarizations(a,b,h,True))==got;counts['gauge_patch']+=1
    a,b,q=base.cm()
    for h in ((1,1,-1,-1),(1,1,1,1),(1,1,1,-1)):
        e=base.polarizations(a,b,h);value=covariants(q,e)
        for p in permutations(range(4)):
            assert covariants(tuple(q[i] for i in p),tuple(e[i] for i in p))==value;counts['Bose']+=1
        for leg in range(4):
            gauge=list(e);gauge[leg]=q[leg];assert covariants(q,tuple(gauge))==(Q(),)*12;counts['Ward']+=1
        assert covariants(tuple(map(base.transpose,q)),tuple(map(base.transpose,e)))==value;counts['parity']+=1
        L=((Q(1),Q(1)),(Q(),Q(1)));R=((Q(1),Q()),(Q(1),Q(1)))
        move=lambda A:base.mm(base.mm(L,A),base.transpose(R))
        assert covariants(tuple(map(move,q)),tuple(map(move,e)))==value;counts['Lorentz']+=1
    # Explicit component tensor for all four new generators, with arbitrary polarizations.
    components={ix:covariants(q,tuple(base.VECTOR_BASIS[i] for i in ix))[8:] for ix in product(range(4),repeat=4)}
    component_Ward=0
    for leg in range(4):
        for other in product(range(4),repeat=3):
            total=[Q()]*4
            for k in range(4):
                ix=list(other);ix.insert(leg,k);coefficient=q[leg][k//2][k%2]
                total=[x+coefficient*y for x,y in zip(total,components[tuple(ix)])]
            assert total==[Q()]*4;component_Ward+=4
    # Multi-energy jet rank: no claim that twelve helicity values are independent at one point.
    forward=forward_map();_,pivots=base.reduced_rows(forward);kernel=base.nullspace(forward)
    expected_free=(3,4,6,9,10,11)
    assert len(pivots)==6 and kernel==tuple(tuple(Q(int(i==j)) for i in range(12)) for j in expected_free)
    full=[]
    for E in (Q(1),Q(2),Q(3),Q(4)):full.append(rows(Q(1),Q(),E)[0])
    for E in (Q(1),Q(2)):full.append(rows(Q(1),Q(),E)[1])
    for phi in (0,1,4):
        for E in (Q(1),Q(2)):full.append(rows(scale=E)[phi])
    assert len(base.reduced_rows(full)[1])==12
    invisible=tuple(tuple(v[i] for i in expected_free) for v in full[6:])
    assert len(base.reduced_rows(invisible)[1])==6
    # h5 is independent of h3 across energies, not discarded when a chosen loop cut is zero.
    assert rows()[4][11]==Q(138528,390625)
    dropped=[tuple(Q() if j==11 else x for j,x in enumerate(v)) for v in full]
    assert len(base.reduced_rows(dropped)[1])==11 and all(v[11]==0 for v in forward)
    # New tensors have exact degree-five scaling in the physical helicity normalization.
    for r1,r2 in zip(rows(),rows(scale=Q(2))):
        assert r2==tuple(x*16**d for x,d in zip(r1,DEGREES))
    refused=['drop_h5_preserves_forward_but_loses_full_rank','mistake_fixed_energy_helicity_rank_for_jet_rank']
    for key in ('degree_five_log_window_tensor_constructed','general_dim10_Born_loop_inventory_derived',
                'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported degree-five local promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    encode=lambda A:[[str(x) for x in row] for row in A]
    return {'schema':'marici.photon-local-degree5-receipt.v1','status':'pass',
        'scope':'twelve_local_covariants_in_regular_parity_even_on_shell_jet_not_degree5_log_or_physical_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'coefficient_order':list(NAMES),'counts':counts,'new_component_Ward_constraints':component_Ward,
        'forward_rank':6,'full_coefficient_rank':12,'forward_map':encode(forward),
        'kernel_coordinate_names':[NAMES[i] for i in expected_free],'forward_kernel':encode(kernel),
        'full_rank_witness':encode(full),'invisible_rank_six_witness':encode(invisible),
        'h5_control':'138528/390625','drop_h5_full_rank':11,
        'general_identity_derivations_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale local degree-five receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','full_coefficient_rank','forward_rank','kernel_coordinate_names','new_component_Ward_constraints','degree_five_log_window_tensor_constructed')}))

if __name__=='__main__':main()
