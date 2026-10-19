"""Explicit conditional box-cut Holder modulus and a bounded-source obstruction above exponent 1/2."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_joint_transport_stability_v1 as prior
joint=prior.joint;equal=prior.equal;t=prior.t;p=prior.p
CONTRACT=HOME/'contracts/photon-box-cut-modulus-v1.json';PROOF=HOME/'photon-box-cut-modulus-v1.md'
TEST=HOME/'checkers/test_photon_box_cut_modulus_v1.py';MANIFEST=HOME/'scc-models/photon-box-cut-modulus-v1.json'
RESULT=HOME/'results/photon-box-cut-modulus-v1.json'


def data(x):return joint.five.observe(x[:5])+equal.previous.transport(x)
def cut_vector(x):return prior.flat_cut(equal.previous.cut_coordinates(x))
def gap(a,b):return prior.norm(prior.difference(a,b))
CUT_ROWS=tuple(tuple(t.get(case[r],n) for case in t.CASES) for r,count in enumerate((3,3,4,3)) for n in range(count))
CUT_NORM=max(sum(map(abs,row),Q()) for row in CUT_ROWS)

def holder_constant(M):
    M=Q(M);assert M>=1
    return Q(13,3)+Q(45,7)*M*M


def diameter(M):return 2*CUT_NORM*Q(M)**2


def cube_root_upper(x,bits=64):
    x=Q(x);assert 0<=x<=1 and type(bits) is int and bits>=1
    if x==0:return Q()
    hi=Q(1)
    while (hi/2)**3>=x:hi/=2
    lo=hi/2
    for _ in range(bits):
        mid=(lo+hi)/2
        if mid**3<x:lo=mid
        else:hi=mid
    assert lo**3<=x<=hi**3
    return hi


def modulus(delta,M,bits=64):
    delta=Q(delta);M=Q(M);assert delta>=0 and M>=1
    if delta==0:return Q()
    if delta>=1:return diameter(M)
    rho=cube_root_upper(delta,bits)
    return min(diameter(M),holder_constant(M)*rho)


def bounded_pair(r):
    r=Q(r);assert 0<r<=1
    u=equal.source(Q(1));v=equal.source(1+r)
    dp=v[2]**2-u[2]**2;dq=v[2]*v[3]-u[2]*u[3]
    x=(r,Q(),u[2],u[3],Q(),Q(),Q(),Q())
    y=(r,Q(),v[2],v[3],Q(),-Q(7,16)*dp/r,-Q(5,56)*dp/r,-Q(5,84)*dq/r)
    return x,y


def certificate():
    # Gram alignment: F^2-r^2*d^2/4 is concave in the nonnegative alignment cosine.
    # Its endpoint at cosine=1 has this nonnegative factorization; the other is >=1/2 on [0,1].
    endpoint=(Q(3,4),Q(1,2),-Q(9,4),Q(),Q(1))
    assert endpoint==p.mul((Q(1),Q(-2),Q(1)),(Q(3,4),Q(2),Q(1)))
    # Cubic sensing A^T A: det=g^4+g²f²+100f^4 >=(g²+f²)^2/2; trace<=101*(g²+f²).
    det=(Q(1),Q(1),Q(100));r4=(Q(1),Q(2),Q(1))
    assert tuple(a-b/2 for a,b in zip(det,r4))==(Q(1,2),Q(),Q(199,2))
    assert 15**2>202 and 11**2>102
    assert Q(1440,4032)==Q(5,14) and 18*Q(5,14)==Q(45,7)
    assert 36*(Q(37,50400)+Q(1,43200))==Q(229,8400)<Q(45,7)
    # Fixed-M3 transport-to-cut map has the same 13/3 ambient max-norm gain.
    columns=tuple(prior.flat_cut(joint.response_from_transport(tuple(Q(int(i==j)) for j in range(6)),Q())) for i in range(6))
    assert max(sum(map(abs,row),Q()) for row in zip(*columns))==Q(13,3)
    # Exact source-difference directions for the bounded sharpness family.
    V=( -Q(7,16),-Q(5,56),Q(),Q(),Q(),Q(),Q(1),Q(),Q(),-Q(30,7),Q(),Q())
    W=(Q(),Q(),-Q(5,84),Q(),Q(),Q(),Q(),Q(1),Q(),Q(),Q(),Q())
    assert all(t.dot(row,V)==t.dot(row,W)==0 for row in t.FLOW)
    assert tuple(t.dot(row,V) for row in equal.previous.RESP)==tuple(x/4032 for x in equal.LINE)
    assert all(t.dot(row,W)==0 for row in equal.previous.RESP)
    # Derivative bounds on v in [1,2], sufficient for every source coordinate in the pair to stay in [-1,1].
    pprime=Q(14,37);qprime=Q(1680,1369)
    assert Q(7,16)*2*pprime<1 and Q(5,56)*2*pprime<1 and Q(5,84)*(pprime+qprime)<1
    # Exact first-order Taylor coefficients at v=1 from the rational source parameterization.
    D=(Q(37),Q(60),Q(30));P=(Q(14),Q(14));Qn=(Q(-23),Q(-60),Q(-30))
    derivative=lambda N:(N[1]*D[0]-N[0]*D[1])/D[0]**2
    dp=derivative(P);dq=derivative(Qn)
    assert (dp,dq)==(-Q(322,1369),-Q(840,1369))
    cut_limit=abs(2*Q(14,37)*dp)/224;data_limit=max(abs(dp),abs(dq))
    assert (cut_limit,data_limit)==(Q(161,202612),Q(840,1369))
    return {'gram_cosine_endpoint_factorization':list(map(str,endpoint)),
            'sensing_det_minus_half_r4':['1/2','0','199/2'],
            'gram_alignment_gain':'4','cubic_sensing_inverse_gain':'15',
            'away_square_gain':'1440','away_cut_gain':'45/7','near_cut_gain':'229/8400',
            'fixed_M3_cut_gain':'13/3','cut_diameter_coefficient':str(2*CUT_NORM),
            'bounded_family_data_gap_over_r_squared_limit':str(data_limit),
            'bounded_family_cut_gap_over_r_limit':str(cut_limit),
            'bounded_family_exponent_upper_limit':'1/2'}


def validate(c):
    assert c['schema']=='marici.photon-box-cut-modulus.v1' and c['owner']=='marici.Nima'
    for k in ('explicit_conditional_two_data_holder_modulus','all_leading_strata_included',
              'bounded_source_exponents_above_half_excluded','deterministic_compatible_cut_diameter_bound'):
        assert c[k] is True,k
    for k in ('one_third_exponent_proved_optimal','one_half_upper_modulus_derived','physical_source_box_licensed',
              'unique_Born_source_or_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=prior.build();cert=certificate()
    points=[tuple(map(Q,x)) for x in product((-1,0,1),repeat=8)]
    # Deterministic subset of two-point controls; these do not substitute for the universal proof.
    controls=0
    for i in range(0,len(points),37):
        x=points[i];y=points[(113*i+19)%len(points)]
        delta=gap(data(x),data(y));observed=gap(cut_vector(x),cut_vector(y))
        assert observed<=modulus(delta,Q(1));controls+=1
    for x in (points[0],points[-1],(Q(),)*8):
        assert gap(data(x),data(tuple(-v for v in x)))==0
        assert gap(cut_vector(x),cut_vector(tuple(-v for v in x)))==modulus(Q(),Q(1))==0
    witnesses=[]
    for n in (10,100,1000,10000):
        r=Q(1,n);x,y=bounded_pair(r)
        assert max(map(abs,x+y))<=1
        assert equal.previous.transport(x)==equal.previous.transport(y) and any(equal.previous.transport(x))
        delta=gap(data(x),data(y));observed=gap(cut_vector(x),cut_vector(y))
        assert delta>0 and observed>0 and observed<=modulus(delta,Q(1))
        assert delta==r*max(abs(x[2]-y[2]),abs(x[3]-y[3]))
        assert observed==abs(y[2]**2-x[2]**2)/224
        witnesses.append({'r':str(r),'joint_data_gap':str(delta),'cut_gap':str(observed),
                          'Lipschitz_amplification':str(observed/delta),'quartic_max_norm':str(max(map(abs,y[5:])))})
    # Scaled boxes and a conservative noise-radius consequence: pair gap <=2*epsilon.
    for M in (Q(1),Q(2),Q(3)):
        x,y=bounded_pair(Q(1,10));x=tuple(M*v for v in x);y=tuple(M*v for v in y)
        delta=gap(data(x),data(y));assert gap(cut_vector(x),cut_vector(y))<=modulus(delta,M)
        epsilon=delta/2;assert gap(cut_vector(x),cut_vector(y))<=modulus(2*epsilon,M)
    assert cube_root_upper(Q(1,1000))**3>=Q(1,1000)
    refused=['use_compactness_without_quantitative_constants','reuse_unbounded_quartic_counterexample_on_unit_box',
             'promote_Holder_modulus_to_Lipschitz','declare_computed_exponent_optimal','treat_deterministic_noise_radius_as_probability']
    for key in ('one_third_exponent_proved_optimal','one_half_upper_modulus_derived','physical_source_box_licensed',
                'unique_Born_source_or_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned box-modulus promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-box-cut-modulus-receipt.v1','status':'pass',
        'scope':'conditional_source_box_explicit_one_third_cut_modulus_and_bounded_exponent_obstruction_not_native_prior',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'modulus_for_delta_le_one':'min(diameter,(13/3+45*M^2/7)*delta^(1/3))',
        'upper_exponent':'1/3','excluded_exponents':'alpha>1/2','two_point_controls':controls,
        'bounded_sharpness_controls':witnesses,'compatible_noise_cut_diameter':'omega_M(2*epsilon)',
        'norms':'max normalized joint13 and independent-cut-coefficient13 coordinates',
        'general_quantitative_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale source-box cut modulus receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','upper_exponent','excluded_exponents','two_point_controls','physical_source_box_licensed')}))

if __name__=='__main__':main()
