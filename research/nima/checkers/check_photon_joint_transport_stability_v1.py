"""Joint-data cut recovery: unbounded-image discontinuity and conditional quartic-bound continuity."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_joint_transport_v1 as joint
equal=joint.equal;t=joint.t;p=joint.p
CONTRACT=HOME/'contracts/photon-joint-transport-stability-v1.json';PROOF=HOME/'photon-joint-transport-stability-v1.md'
TEST=HOME/'checkers/test_photon_joint_transport_stability_v1.py';MANIFEST=HOME/'scc-models/photon-joint-transport-stability-v1.json'
RESULT=HOME/'results/photon-joint-transport-stability-v1.json'
Z=(Q(),)*6
EXPONENTS=(1,1,0,0,0,-1,-1,-1)


def estimate_m3(B):
    B=tuple(map(Q,B))
    return -(B[2]+(B[4]-12*B[3])/9)/60

def surrogate(B):return joint.response_from_transport(B,estimate_m3(B))
def norm(v):return max(map(abs,v),default=Q())
def difference(a,b):return tuple(x-y for x,y in zip(a,b))
def flat_cut(R):return joint.nonzero.flatten(joint.cut_from_response(R))

def bias_bound(x,Kmax,Lmax):
    assert Kmax>=0 and Lmax>=0 and abs(x[5])<=Kmax and abs(x[6])<=Lmax
    return abs(x[0])*Kmax/1680+abs(x[0])*Lmax/7200+abs(x[1])*Lmax/43200


def degenerating_source(eps):
    eps=Q(eps);assert eps>0
    x=equal.source(Q(1))
    return tuple(v*eps**e for v,e in zip(x,EXPONENTS))


def matrices():
    units=tuple(tuple(Q(int(i==j)) for j in range(6)) for i in range(6))
    R=tuple(zip(*(surrogate(v) for v in units)))
    C=tuple(zip(*(flat_cut(surrogate(v)) for v in units)))
    return R,C,max(sum(map(abs,row),Q()) for row in R),max(sum(map(abs,row),Q()) for row in C)


def certificate():
    assert all(EXPONENTS[i]+EXPONENTS[j]==0 for i,j in t.cut.PAIRS)
    row=t.add(t.FLOW[2],t.scale(Q(1,9),t.add(t.FLOW[4],t.scale(-12,t.FLOW[3]))))
    estimate=t.scale(-Q(1,60),row);bias=t.add(t.M3,t.scale(-1,estimate))
    target=tuple(-Q(1,1680) if i==0 else Q(1,7200) if i==1 else -Q(1,43200) if i==4 else Q() for i in range(12))
    assert bias==target
    line=joint.response_from_transport(Z,Q(1));assert line==equal.LINE
    assert norm(line)==5 and norm(flat_cut(line))==18
    R,C,KR,KC=matrices()
    return {'source_rescaling_exponents':list(EXPONENTS),'degree6_rescaling_product_identities':12,
            'missing_coordinate_bias_coefficients':list(map(str,bias)),
            'response_bias_line':list(map(str,line)),'response_line_norm':'5','cut_polynomial_line_norm':'18',
            'response_surrogate_matrix':[[str(v) for v in row] for row in R],
            'cut_surrogate_matrix':[[str(v) for v in row] for row in C],
            'response_operator_norm':str(KR),'cut_polynomial_operator_norm':str(KC)}


def validate(c):
    assert c['schema']=='marici.photon-joint-transport-stability.v1' and c['owner']=='marici.Nima'
    for k in ('unbounded_real_image_discontinuity_constructed','quartic_source_growth_tracked',
              'exact_missing_coordinate_bias_identity','conditional_zero_leading_boundary_bound_derived'):
        assert c[k] is True,k
    for k in ('physical_quartic_bound_derived','bounded_source_continuity_refuted',
              'uniform_EFT_window_for_diverging_sources_derived','global_compact_source_noise_modulus_derived',
              'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=joint.build();cert=certificate()
    _,_,KR,KC=matrices()
    x0=(Q(),Q(),Q(),Q(1),Q(),Q(),Q(),Q());B0=equal.previous.transport(x0)
    J0=joint.five.observe(x0[:5]);R0=equal.previous.cut_coordinates(x0)
    assert B0==equal.TARGET and J0==(Q(),)*7 and surrogate(B0)==R0
    assert joint.classify(J0,B0)['response']==R0
    sequence=[]
    for n in (10,100,1000,10000):
        eps=Q(1,n);x=degenerating_source(eps);B=equal.previous.transport(x);J=joint.five.observe(x[:5])
        R=joint.classify(J,B)['response'];gap=norm(difference(J+B,J0+B0));cutgap=norm(difference(flat_cut(R),flat_cut(R0)))
        assert B==B0 and R==equal.previous.cut_coordinates(equal.source(Q(1)))
        assert gap==Q(23,37)*eps and cutgap==Q(7,10952)
        growth=norm(x[5:]);assert growth==Q(343,5476)/eps
        assert cutgap/gap==Q(7,6808)/eps
        sequence.append({'epsilon':str(eps),'joint_data_gap':str(gap),'cut_coefficient_gap':str(cutgap),
                         'inverse_amplification':str(cutgap/gap),'quartic_max_norm':str(growth)})
    # The limit identity is exact for every eps>0, not established only by this sequence:
    # all degree-six monomials are constant, J=(eps²,0,0,eps*p,0,eps*q,0).
    x=equal.source(Q(1));assert all(x[i]!=0 for i in (5,6,7))
    # Conditional estimate on the entire source domain follows from the coefficientwise bias identity.
    controls=0
    for leading in product((Q(-1),Q(),Q(1)),repeat=2):
        for cubic in product((Q(-1),Q(1)),repeat=3):
            for quartic in product((Q(-1),Q(1)),repeat=3):
                x=leading+cubic+quartic;B=equal.previous.transport(x);R=equal.previous.cut_coordinates(x)
                b=-x[0]*x[5]/1680+x[0]*x[6]/7200-x[1]*x[6]/43200
                assert difference(R,surrogate(B))==tuple(b*v for v in equal.LINE)
                cap=bias_bound(x,Q(1),Q(1));assert abs(b)<=cap
                assert norm(difference(R,R0))<=KR*norm(difference(B,B0))+5*cap
                assert norm(difference(flat_cut(R),flat_cut(R0)))<=KC*norm(difference(B,B0))+18*cap
                controls+=1
    # The unobserved coefficient f4 need not be bounded for this missing-coordinate estimate.
    for M in (Q(-10000),Q(10000)):
        x=(Q(1,10),Q(-1,7),Q(1),Q(2),Q(3),Q(1),Q(-1),M)
        B=equal.previous.transport(x);R=equal.previous.cut_coordinates(x);cap=bias_bound(x,Q(1),Q(1))
        assert norm(difference(R,surrogate(B)))<=5*cap
    refused=['omit_diverging_quartic_contacts_from_counterexample','apply_unbounded_witness_to_a_fixed_source_box',
             'declare_surrogate_always_a_realizable_cut','claim_forward_polynomial_source_map_discontinuous']
    for key in ('physical_quartic_bound_derived','bounded_source_continuity_refuted',
                'uniform_EFT_window_for_diverging_sources_derived','global_compact_source_noise_modulus_derived',
                'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned reconstruction-stability promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-joint-transport-stability-receipt.v1','status':'pass',
        'scope':'unbounded_joint_image_discontinuity_and_conditional_quartic_bounded_zero_leading_continuity_not_physical_prior',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'exact_degenerating_controls':sequence,'bounded_identity_controls':controls,
        'unbounded_f4_controls':2,'constant_cut_gap':'7/10952','limit_data_realizable':True,
        'all_source_maps_remain_polynomial_continuous':True,'general_stability_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale joint-transport stability receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','constant_cut_gap','bounded_identity_controls','unbounded_real_image_discontinuity_constructed','physical_quartic_bound_derived')}))

if __name__=='__main__':main()
