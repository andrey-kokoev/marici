"""Positive minimal two-point interpolant, with explicit zero/threshold failure."""
import argparse
import hashlib
import json
from pathlib import Path
import check_scalar_c_native_comparison as base

ROOT=base.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/three-hidden-native-interpolant.v1.json'
PROOF=HOME/'THREE-HIDDEN-NATIVE-INTERPOLANT.md'
RESULT=HOME/'results/three-hidden-native-interpolant.v1.json'
F,mm,eye,inverse,add,scale,inertia=base.F,base.mm,base.eye,base.inverse,base.add,base.scale,base.inertia


def transpose(A):return [list(row) for row in zip(*A)]
def block(A,B,C,D):return [a+b for a,b in zip(A,B)]+[c+d for c,d in zip(C,D)]
def decode(A):return [[F(*v) for v in row] for row in A]
def invert(A):
    B=inverse(A);assert mm(A,B)==mm(B,A)==eye(len(A));return B

def require_equal(A,B):assert A==B,'interpolation identity failed'


def validate_contract(c):
    assert c['schema']=='marici.scattering.three-hidden-native-interpolant.v1'
    assert (c['visible_dimension'],c['hidden_dimension'])==(3,3)
    assert c['spectral_points_in_stored_K_units']==['-1','-2']
    assert ROOT/c['native_source']==base.algebra.lower.SOURCE
    assert ROOT/c['lower_dimension_certificate']==base.RESULT
    for key in ('live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    prior=base.build();assert prior==json.loads(base.RESULT.read_text(encoding='utf-8')),'stale lower-dimension certificate'
    native_threshold=base.algebra.lower.audit()
    src=json.loads(base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    native_inertia=inertia([[h[i]*K[i][j] for j in range(11)] for i in range(11)])
    assert native_inertia==(10,0,1)
    HP=[[h[i] if i==j else F() for j in range(3)] for i in range(3)]
    PP=[r[:3] for r in K[:3]];QQ=[r[3:] for r in K[3:]]
    QP=[r[:3] for r in K[3:]];PQ=[r[3:] for r in K[:3]]
    native_eff=[decode(A) for A in prior['native_effective_operators']]
    N=[add(PP,scale(F(-1),A)) for A in native_eff]
    assert all(inertia(mm(HP,A))==(3,0,0) for A in N)
    R=[invert(A) for A in N]
    G=add(R[1],scale(F(-1),R[0]));T=add(scale(F(2),R[0]),scale(F(-1),R[1]))
    HH=mm(HP,G);HT=mm(HP,T)
    assert inertia(HH)==inertia(HT)==(3,0,0)
    Gi=invert(G);Ah=mm(Gi,T)
    require_equal(mm(HH,Gi),HP);require_equal(mm(HH,Ah),HT)
    zero=[[F()]*3 for _ in range(3)]
    reduced=block(PP,eye(3),Gi,Ah);metric=block(HP,zero,zero,HH)
    gram=mm(metric,reduced)
    assert gram==transpose(gram) and inertia(metric)==inertia(gram)==(6,0,0)
    core_inverse=invert(reduced)
    assert mm(scale(F(-1),reduced),scale(F(-1),core_inverse))==eye(6)
    span=base.algebra.lower.Span(6)
    for j in range(3):
        span.add([F(int(i==j)) for i in range(6)],{'visible_seed':j})
        span.add([row[j] for row in reduced],{'K_visible_seed':j})
    assert len(span.rows)==6
    endpoints=[]
    for j,s in enumerate((1,2)):
        fitted=invert(add(scale(F(s),G),T));require_equal(fitted,N[j])
        fitted_from_blocks=mm(invert(add(scale(F(s),eye(3)),Ah)),Gi)
        require_equal(fitted_from_blocks,fitted)
        fitted_eff=add(PP,scale(F(-1),fitted));require_equal(fitted_eff,native_eff[j])
        full_native=invert(add(scale(F(-s),eye(11)),scale(F(-1),K)))
        full_reduced=invert(add(scale(F(-s),eye(6)),scale(F(-1),reduced)))
        compressed_native=[r[:3] for r in full_native[:3]]
        compressed_reduced=[r[:3] for r in full_reduced[:3]]
        require_equal(compressed_native,compressed_reduced)
        require_equal(compressed_reduced,invert(add(scale(F(-s),eye(3)),scale(F(-1),fitted_eff))))
        endpoints.append({'z':str(-s),'effective_operator_equal':True,'full_visible_resolvent_equal':True})
    # Third-point and threshold structure are independent of the fit objective.
    native_N3=mm(mm(PQ,invert(add(QQ,scale(F(3),eye(8))))),QP)
    fitted_N3=invert(add(scale(F(3),G),T))
    third_difference=add(native_N3,scale(F(-1),fitted_N3))
    assert inertia(mm(HP,third_difference))==(2,0,1)
    S0=decode(native_threshold['coefficient_limit']);defect=add(eye(3),scale(F(-1),S0))
    assert mm(defect,defect)==scale(F(2),defect)
    assert inertia(mm(HP,defect))==(1,0,2) and sum((defect[i][i] for i in range(3)),F())==2
    assert native_threshold['kernel_dimension']==1
    controls=[]
    for name in ('wrong-hidden-metric','reverse-inverse-secant','claim-native-zero-mode','claim-global-response-identity'):
        try:
            if name=='wrong-hidden-metric':assert mm(HP,Gi)==HP
            elif name=='reverse-inverse-secant':assert inertia(scale(F(-1),HH))==(3,0,0)
            elif name=='claim-native-zero-mode':assert inertia(gram)[2]==1
            else:require_equal(native_N3,fitted_N3)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile interpolant accepted: '+name)
    paths={ROOT/p for p in prior['source_sha256']}
    paths.update((base.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_three_hidden_native_interpolant.py'))
    return {'schema':'marici.scattering.three-hidden-native-interpolant-receipt.v1','status':'pass',
        'scope_verdict':'positive_minimal_endpoint_interpolant_not_threshold_faithful',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'visible_dimension':3,'hidden_dimension':3,'full_core_dimension':6,
        'G':base.encoded(G),'T':base.encoded(T),'hidden_metric':base.encoded(HH),
        'reduced_core':base.encoded(reduced),'full_metric':base.encoded(metric),
        'metric_inertia':[6,0,0],'weighted_core_inertia':[6,0,0],
        'native_weighted_core_inertia':list(native_inertia),
        'direct_visible_block_retained':True,'exact_endpoint_fits':endpoints,
        'minimal_hidden_dimension_for_exact_two_point_fit':3,
        'native_zero_mode_preserved':False,'native_kernel_dimension':1,'reduced_kernel_dimension':0,
        'candidate_visible_cyclic_dimension':len(span.rows),'full_zero_energy_block_inverse_verified':True,
        'third_point_z':'-3','third_point_negative_self_energy_difference_inertia':[2,0,1],
        'conditional_chain_attachment_coefficient_limit':'I3',
        'native_chain_coefficient_limit':'rank-one Householder',
        'coefficient_limit_norm_gap_in_same_frame':2,
        'all_energy_response_identical':False,'physical_probability_error_bound_proved':False,
        'source_selected_model_claimed':False,'analytic_argument_machine_formalized':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale three-hidden interpolant'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','scope_verdict','minimal_hidden_dimension_for_exact_two_point_fit','weighted_core_inertia',
          'native_zero_mode_preserved','coefficient_limit_norm_gap_in_same_frame','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
