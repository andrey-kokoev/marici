"""Metric residual norm and preparation-sensitive Duhamel-bound support."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_ground_preserving_native_projection as project

ROOT=project.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/native-projection-time-error.v1.json'
PROOF=HOME/'NATIVE-PROJECTION-TIME-ERROR.md'
RESULT=HOME/'results/native-projection-time-error.v1.json'
F,mm,eye,add,scale,invert=project.F,project.mm,project.eye,project.add,project.scale,project.invert
transpose,decode,difference,zeros=project.transpose,project.decode,project.difference,project.zeros


def trace(A):return sum((A[i][i] for i in range(len(A))),F())
def equal(A,B):assert A==B,'time-error support identity failed'
def quadratic(v,H):return mm(mm(transpose(v),H),v)[0][0]

def state_bound(t,alpha):
    assert alpha>=0,'negative preparation norm'
    return alpha*min(Q(2),Q(3)*abs(t))
def omitted_probability_bound(t,alpha_squared):
    assert 0<=alpha_squared<=1,'normalized preparation weight required'
    return alpha_squared*min(Q(1),Q(9)*t*t)
def effect_probability_bound(t,alpha):
    assert 0<=alpha<=1,'normalized preparation norm required'
    return min(Q(1),2*state_bound(t,alpha))

def certify_slope(tau,B):assert (F(B*B)-tau).positive(),'residual slope too small'

def validate_contract(c):
    assert c['schema']=='marici.scattering.native-projection-time-error.v1'
    assert ROOT/c['projection_certificate']==project.RESULT
    assert ROOT/c['native_source']==project.base.algebra.lower.SOURCE
    assert Q(c['certified_residual_norm_upper_bound'])==3
    assert c['state_error_bound']=='alpha min(2,3|t|)'
    assert c['omitted_core_probability_bound_for_normalized_input']=='alpha^2 min(1,9t^2)'
    for key in ('asymptotic_scattering_bound_claimed','uniform_in_time_small_error_claimed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=project.build();assert parent==json.loads(project.RESULT.read_text(encoding='utf-8')),'stale projection input'
    src=json.loads(project.base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    E=decode(parent['embedding']);L=decode(parent['metric_adjoint'])
    Kr=decode(parent['reduced_core']);Hr=decode(parent['full_metric']);n=len(Kr);assert n==8
    R=difference(mm(K,E),mm(E,Kr));assert project.rank(R)==1
    equal(mm(L,R),zeros(n,n))
    Rsharp=mm(mm(invert(Hr),transpose(R)),H);D=mm(Rsharp,R);tau=trace(D)
    equal(mm(Hr,D),mm(mm(transpose(R),H),R))
    assert project.inertia(mm(Hr,D))==(1,0,7)
    # Exact rank-one factorization gives the operator norm, not just a Frobenius bound.
    j=next(j for j in range(n) if any(R[i][j] for i in range(11)))
    a=[[row[j]] for row in R];i=next(i for i in range(11) if a[i][0])
    b=[[v/a[i][0] for v in R[i]]];equal(mm(a,b),R)
    a_norm=quadratic(a,H);b_dual=mm(mm(b,invert(Hr)),transpose(b))[0][0]
    assert a_norm.positive() and b_dual.positive() and tau==a_norm*b_dual
    assert (tau-F(4)).positive();certify_slope(tau,Q(c['certified_residual_norm_upper_bound']))
    sym=project.cyclic(K,[[F(int(i==0)) for i in range(11)],
                          [F(int(i in (1,2))) for i in range(11)]])
    S=mm(L,sym);GS=mm(mm(transpose(S),Hr),S)
    Ps=mm(mm(mm(S,invert(GS)),transpose(S)),Hr)
    equal(mm(Ps,Ps),Ps);equal(mm(Hr,Ps),transpose(mm(Hr,Ps)))
    equal(mm(Kr,Ps),mm(Ps,Kr));equal(mm(R,Ps),zeros(11,n))
    Vr=[[F(int(i==j)) for j in range(3)] for i in range(n)]
    Vn=[[F(int(i==j)) for j in range(3)] for i in range(11)]
    HP=[row[:3] for row in H[:3]]
    Vrsharp=mm(mm(invert(HP),transpose(Vr)),Hr)
    Vnsharp=mm(mm(invert(HP),transpose(Vn)),H)
    Pr=mm(Vr,Vrsharp);Pn=mm(Vn,Vnsharp)
    equal(mm(Pn,E),mm(E,Pr));equal(mm(E,Vr),Vn);equal(mm(Vnsharp,E),Vrsharp)
    equal(mm(Ps,Pr),mm(Pr,Ps))
    Qs=[[F(1),F(),F()],[F(),F(Q(1,2)),F(Q(1,2))],[F(),F(Q(1,2)),F(Q(1,2))]]
    equal(mm(Qs,Qs),Qs);equal(mm(HP,Qs),transpose(mm(HP,Qs)))
    equal(mm(Ps,Vr),mm(Vr,Qs));equal(mm(Vrsharp,Ps),mm(Qs,Vrsharp))
    Qcore=difference(eye(11),mm(E,L))
    equal(mm(Qcore,Qcore),Qcore);equal(mm(Qcore,E),zeros(11,n));assert project.rank(Qcore)==3
    equal(mm(H,Qcore),transpose(mm(H,Qcore)))
    anti=difference(eye(n),Ps);profiles={}
    seeds={'belt':[1,0,0],'carrier_sum':[0,1,1],'carrier_difference':[0,1,-1],
           'carrier_1':[0,1,0],'carrier_2':[0,0,1]}
    expected={'belt':Q(0),'carrier_sum':Q(0),'carrier_difference':Q(1),'carrier_1':Q(1,2),'carrier_2':Q(1,2)}
    for name,seed in seeds.items():
        v=[[F(x)] for x in seed+[0]*5];z=mm(anti,v)
        ratio=quadratic(z,Hr)/quadratic(v,Hr);assert ratio==F(expected[name])
        profiles[name]={'alpha_squared':str(expected[name])}
    controls=[]
    for name in ('erase-residual','understate-slope','omit-metric','call-carrier-difference-exact','promote-to-asymptotic-bound'):
        try:
            if name=='erase-residual':equal(R,zeros(11,n))
            elif name=='understate-slope':certify_slope(tau,Q(2))
            elif name=='omit-metric':assert trace(mm(transpose(R),R))==tau
            elif name=='call-carrier-difference-exact':assert profiles['carrier_difference']['alpha_squared']=='0'
            else:
                bad=copy.deepcopy(c);bad['asymptotic_scattering_bound_claimed']=True;validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile time-error control accepted: '+name)
    paths={ROOT/p for p in parent['source_sha256']}
    paths.update((project.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_native_projection_time_error.py'))
    return {'schema':'marici.scattering.native-projection-time-error-receipt.v1','status':'pass',
        'scope_verdict':'finite_time_preparation_sensitive_error_certificate',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'residual_rank':1,'residual_range_factor':project.base.encoded(a),'residual_row_factor':project.base.encoded(b),
        'exact_residual_norm_squared':tau.encoded(),'norm_strictly_greater_than':2,'certified_residual_norm_upper_bound':3,
        'symmetric_core_projector':project.base.encoded(Ps),'symmetric_port_projector':project.base.encoded(Qs),
        'reducing_and_contact_identities_verified':True,'conditional_chain_residual_same_as_core':True,
        'state_error_bound':c['state_error_bound'],
        'omitted_core_probability_bound':c['omitted_core_probability_bound_for_normalized_input'],
        'effect_probability_error_bound':c['effect_probability_error_bound_for_normalized_input'],
        'normalized_core_preparations':profiles,
        'example':{'time_horizon':'1/30','state_error_per_alpha':'1/10','omitted_probability_per_alpha_squared':'1/100'},
        'asymptotic_scattering_bound_claimed':False,'uniform_in_time_small_error_claimed':False,
        'physical_clock_or_detector_binding_claimed':False,'analytic_argument_machine_formalized':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale native projection time-error certificate'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','residual_rank','certified_residual_norm_upper_bound','state_error_bound',
          'omitted_core_probability_bound','asymptotic_scattering_bound_claimed','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
