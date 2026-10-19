"""Miscalibrated partial-pointer erasure and the independent calibration-resource gate."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_partial_pointer_eraser import audit as partial_audit
from check_inverse_flag_dilation import Radicals
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qrecord
from check_selector_failure_feedback import mul
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,eye,record,digest,BASE
from check_diagonal_spin_networks import S2,CI

DEST=BASE/'results/pointer-calibration-information.v1.json'


def zero():return ((ZERO,ZERO),(ZERO,ZERO))
def pair(X):return (X,zero())
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def scalar(X):return (F(X['constant']),F(X['sqrt19']))
def scalarpair(X):return {'constant':X[0].record(),'sqrt19':X[1].record()}


def audit():
    previous=partial_audit();I=pair(eye(2));H=pair(((ZERO,ZERO),(ZERO,ONE)));Low=pair(((ONE,ZERO),(ZERO,ZERO)))
    pointers=[(A(F(x['gamma'])),A(F(x['v']))) for x in previous['pointer_fixtures']]
    estimates=pointers+[(S2/2,S2/2)];rows=[]
    for case in previous['retained_tests']:
        ratio=scalar(case['ratio']);alpha=qa(qr(1),qn(ratio));R=Radicals((ratio,alpha));tests=[]
        for gamma,v in pointers:
            for hatgamma,hatv in estimates:
                assert gamma*gamma+v*v==hatgamma*hatgamma+hatv*hatv==ONE
                d=gamma*hatgamma+v*hatv
                residuals=((gamma-CI*v)*(hatgamma+CI*hatv),(gamma+CI*v)*(hatgamma-CI*hatv))
                assert residuals[0].flip(8)==residuals[1]
                assert (residuals[0]+residuals[1])/2==d
                maps=[];effects=[]
                for e in residuals:
                    assert e.flip(8)*e==ONE
                    a0=padd(Low,padd(qscale(ratio,H),qscale(alpha,pair(scale(e,H[0])))))
                    a0=(scale(S2/2,a0[0]),scale(S2/2,a0[1]))
                    a1=pair(scale(S2*(e-ONE)/2,H[0]))
                    branch=(R.clean({0:a0}),R.clean({3:a1}))
                    effect=R.add(R.mul(R.adj(branch[0]),branch[0]),R.mul(R.adj(branch[1]),branch[1]))
                    assert effect=={0:qscale(qr(F(1,2)),I)}
                    maps.extend(branch);effects.append(effect)
                assert R.add(*effects)=={0:I}
                coherence=padd(qscale(ratio,I),qscale(alpha,pair(scale(d,eye(2)))))
                for a in range(2):
                    for b in range(2):
                        X=pair(tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2)));actual={}
                        for M in maps:actual=R.add(actual,R.mul(R.mul(M,{0:X}),R.adj(M)))
                        base=padd(mul(mul(Low,X),Low),mul(mul(H,X),H))
                        cross=padd(mul(mul(Low,X),H),mul(mul(H,X),Low))
                        expected=padd(base,padd(qscale(ratio,cross),qscale(alpha,(scale(d,cross[0]),scale(d,cross[1])))))
                        assert actual==R.clean({0:expected})
                terminal=qscale(qmul(qr(2),qmul(ratio,alpha)),pair(scale(ONE-d,H[0])))
                actual_terminal=R.add(R.mul(R.adj(maps[1]),maps[1]),R.mul(R.adj(maps[3]),maps[3]))
                assert actual_terminal==R.clean({0:terminal})
                infidelity=qscale(alpha,pair(scale((ONE-d)/2,eye(2))))
                fidelity=(ONE-infidelity[0][0][0],-infidelity[1][0][0])
                matched=(gamma,v)==(hatgamma,hatv)
                assert (d==ONE)==matched
                assert (fidelity==(ONE,ZERO))==matched
                tests.append({'actual_pointer':{'gamma':gamma.record(),'v':v.record()},
                              'feedback_pointer':{'gamma':hatgamma.record(),'v':hatv.record()},
                              'dot_product':d.record(),'matched':matched,'Y_labels':['1/2','1/2'],
                              'residual_phases':[x.record() for x in residuals],
                              'coherence':scalarpair((coherence[0][0][0],coherence[1][0][0])),
                              'Bell_undo_fidelity':scalarpair(fidelity),
                              'terminal_flag_maps':[R.record(M) for M in maps],
                              'outcomes_and_terminal_flags_retained':True})
        rows.append({'code':case['code'],'ratio':qrecord(ratio),'tests':tests})
    # Independent known-flag probes are not the unknown data being erased.
    # Z pointer readout distinguishes the real nonnegative pair in its
    # population law, but finite product-probe histories remain ambiguous.
    gamma0,v0=F(3,5),F(4,5);gamma1,v1=F(4,5),F(3,5);dot=gamma0*gamma1+v0*v1
    assert dot==F(24,25)
    probes=[]
    for n in (1,2,4,6):
        histories=[];totals=[F(0),F(0)]
        for label in product((0,1),repeat=n):
            counts=sum(label);likelihood0=(v0*v0)**counts*(gamma0*gamma0)**(n-counts)
            likelihood1=(v1*v1)**counts*(gamma1*gamma1)**(n-counts)
            assert likelihood0>0 and likelihood1>0
            totals[0]+=likelihood0;totals[1]+=likelihood1
            histories.append({'Z_probe_record':list(label),'likelihood_gamma_3_5':str(likelihood0),'likelihood_gamma_4_5':str(likelihood1)})
        assert totals==[F(1),F(1)] and dot**(2*n)>0
        probes.append({'independent_probes':n,'product_pointer_overlap_squared':str(dot**(2*n)),
                       'equal_prior_optimal_quantum_guess':'(1+sqrt(1-(24/25)^(2n)))/2 < 1',
                       'retained_Z_records':histories,'finite_product_probes_exactly_discriminate':False})
    # Exact minimax midpoint for the two illustrated angular hypotheses.
    midpoint=S2/2;d0=A(gamma0)*midpoint+A(v0)*midpoint;d1=A(gamma1)*midpoint+A(v1)*midpoint
    assert d0==d1==7*S2/10 and d0*d0==A(F(49,50))
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_pointer_calibration_information.py'}
    return {
        'schema':'marici.scattering.pointer-calibration-information.v1',
        'status':'mismatched_feedback_disturbs_undo_without_any_Y_label_calibration_signal_independent_probe_resources_remain_required',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'actual_error_channel':{'parameterization':'gamma=cos(beta), v=sin(beta), beta in [0,pi/2]; estimated beta_hat sets feedback',
                                'residual_label_phases':'exp(+/- i*(beta_hat-beta))',
                                'visibility':'d=gamma*gamma_hat+v*v_hat=cos(beta-beta_hat)',
                                'reduced_undo_coherence':'r²+(1-r²)d',
                                'Bell_undo_fidelity':'1-(1-r²)(1-d)/2',
                                'small_angular_error_infidelity':'(1-r²)(beta-beta_hat)²/4+O((beta-beta_hat)^4)',
                                'terminal_flag_one_effect':'2r²(1-r²)(1-d)Pi_high',
                                'label_law':'both labels remain exactly 1/2 for every actual and estimated pointer pair',
                                'all_tests':rows},
        'identifiability_gate':{'retained_Y_labels_identify_gamma':False,
                                'Y_label_Fisher_information_for_beta':0,
                                'argument':'the entire repeated label likelihood is 2^(-n), parameter independent; estimating feedback parameters changes phases, not this law',
                                'terminal_flag_can_signal_mismatch':True,
                                'terminal_flag_is_input_independent_calibration_data':False,
                                'confound':'its rate also depends on unknown tr(Pi_high*rho); low-eigenstate input gives zero signal for every mismatch'},
        'independent_probe_resource':{'probe':'prepare known flag one and supplied apparatus zero, then apply the actual copy and measure pointer Z',
                                      'pointer_Z_one_probability':'v²=1-gamma²',
                                      'parameter_identifiable_from_ideal_population_law':True,
                                      'actual_physical_probe_supply_and_reset_derived':False,
                                      'two_hypothesis_tests':probes,
                                      'scope':'independent product pointer-state probes; not every possible coherent gate-oracle interrogation'},
        'robust_feedback':{'angular_interval_rule':'choose beta_hat=(beta_min+beta_max)/2 to minimize worst angular mismatch',
                            'fidelity_guarantee':'F>=1-(1-r²)[1-cos((beta_max-beta_min)/2)]/2',
                            'two_hypothesis_midpoint':{'gamma_hat':midpoint.record(),'v_hat':midpoint.record(),'worst_visibility':d0.record(),'visibility_squared':'49/50'},
                            'zero_error_without_pointer_knowledge_from_Y_labels':False},
        'inverse_copy_comparison':{'actual_controlled_copy_adjoint_then_W_adjoint_can_restore_input':True,
                                    'explicit_parameter_estimate_needed_if_actual_gate_adjoint_is_supplied':False,
                                    'forward_unknown_gate_automatically_supplies_adjoint':False,
                                    'new_access_obligation':'reversible actual copy control and access to every environmental outcome copy, rather than classical Y-label inference'},
        'boundary':{'new_calibration_data_controls_and_work_inputs':True,'physical_noise_or_platform_derived':False,
                    'prior_history_measurements_undone':False,'records_erased':False,'formal_outcome_admitted':False},
        'next_gate':'Build a retained finite-probe calibration acceptance test with an explicit confidence/error budget, and propagate its pointer-angle interval to eraser fidelity. Keep calibration failure probability, probe records and control resources separate from exact unknown-state recovery.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale pointer-calibration receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact mismatched-feedback channel; Y-label likelihood is parameter independent despite residual disturbance.')
    print('PASS: retained independent probe histories and robust midpoint bound; parameter knowledge and inverse-copy access remain inputs.')


if __name__=='__main__':main()
