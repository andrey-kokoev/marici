"""Exact retained-history retry effects and reduced-channel disturbance."""
from fractions import Fraction as F
import argparse
import json

from check_retained_selector_controls import audit as controls_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,BASE

DEST=BASE/'results/retained-selector-retries.v1.json'


def zero():return tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
def trace(M):return sum((M[i][i] for i in range(4)),ZERO)
def unit(a,b):return tuple(tuple(ONE if i==a and j==b else ZERO for j in range(4)) for i in range(4))
def sandwich(R,X):return mm(mm(R,X),adj(R))
def diagonal(X):return tuple(tuple(X[i][j] if i==j else ZERO for j in range(4)) for i in range(4))


def audit():
    previous=controls_audit()
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    raw=previous['coherent_selector']['retained_reject_map']
    reject=tuple(tuple(decode(x) for x in row) for row in raw)
    branches=[reject[4*i:4*i+4] for i in range(18)]
    images=[]
    for a in range(4):
        row=[]
        for b in range(4):
            Y=zero()
            for R in branches:Y=add(Y,sandwich(R,unit(a,b)))
            row.append(Y)
        images.append(row)
    def apply(X):
        Y=zero()
        for a in range(4):
            for b in range(4):Y=add(Y,scale(X[a][b],images[a][b]))
        return Y
    def dual(X):
        return tuple(tuple(sum((X[i][j]*images[b][a][j][i] for i in range(4) for j in range(4)),ZERO) for b in range(4)) for a in range(4))
    assert dual(eye(4))==add(Pm,scale(A(F(16,25)),P))
    assert dual(P)==scale(A(F(16,25)),P) and dual(Pm)==Pm
    for a in range(4):
        for b in range(4):
            X=sandwich(P,unit(a,b));Y=sandwich(Pm,unit(a,b))
            assert apply(X)==add(scale(A(F(-4,25)),X),scale(A(F(2,5))*trace(X),P))
            assert apply(Y)==add(scale(A(F(1,5)),Y),scale(A(F(2,5))*trace(Y),Pm))
            # Lead readout is its own retained instrument. Reduction over the
            # readout record is dephasing, not erasure of the physical record.
            assert sandwich(P,diagonal(X))==add(scale(A(F(1,6)),X),scale(A(F(1,6))*trace(X),P))
    assert dual(P)!=P  # failure decreases plus weight, never minus weight
    n_effect=eye(4);cumulative=zero();first=scale(A(F(9,25)),P);checks=[]
    for n in range(9):
        assert n_effect==add(Pm,scale(A(F(16,25)**n),P))
        assert cumulative==scale(A(1-F(16,25)**n),P)
        assert add(cumulative,n_effect)==eye(4)
        checks.append({'attempts':n,'all_failure_effect_plus':str(F(16,25)**n),
                       'all_failure_effect_minus':'1','cumulative_success_effect_plus':str(1-F(16,25)**n),
                       'failure_history_slots':str(18**n)})
        cumulative=add(cumulative,first);first=dual(first);n_effect=dual(n_effect)
    # Every restricted branch is proportional to a plus-sector unitary, even
    # though ignoring its history produces a depolarizing reduced channel.
    branch_records=[]
    for item,R in zip(previous['coherent_selector']['controller_preparation'],branches):
        q=tuple(F(x) for x in item['quaternion']);kappa=F(2,125) if abs(q[0])==1 else F(19,500)
        assert sandwich(P,mm(adj(R),R))==scale(A(kappa),P)
        assert mm(R,P)==mm(P,R)
        branch_records.append({'quaternion':item['quaternion'],'plus_failure_effect':str(kappa),
                               'normalized_plus_branch_is_unitary':True})
    # A pure plus witness separates the actual reduced failure map from the
    # positive-square-root-effect substitute, which would leave it unchanged.
    rho=scale(A(2),sandwich(P,unit(0,0)));assert mm(rho,rho)==rho and trace(rho)==ONE
    state=rho;retry_witness=[]
    for n in range(7):
        expected=add(scale(A(F(16,25)**n/2),P),scale(A(F(-4,25)**n),add(rho,scale(A(F(-1,2)),P))))
        assert state==expected
        normalized=scale(A(F(25,16)**n),state)
        purity=trace(mm(normalized,normalized));assert purity==A((1+F(1,16)**n)/2)
        retry_witness.append({'failures':n,'conditional_plus_Bloch_factor':str(F(-1,4)**n),
                              'conditional_plus_purity':str((1+F(1,16)**n)/2)})
        state=apply(state)
    assert apply(rho)!=scale(A(F(16,25)),rho)
    pooled=add(scale(A(F(1,2)),P),scale(A(F(9,29)),add(rho,scale(A(F(-1,2)),P))))
    assert trace(pooled)==ONE and trace(mm(pooled,pooled))==A(F(461,841))
    # General input after lead readout has plus and minus weights one half.
    for a in range(4):
        for b in range(4):
            X=unit(a,b)
            assert trace(mm(P,diagonal(X)))==trace(X)/2
            assert trace(mm(Pm,diagonal(X)))==trace(X)/2
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_retained_selector_retries.py'}
    return {
        'schema':'marici.scattering.retained-selector-retries.v1',
        'status':'retries_select_only_initial_plus_weight_reduced_failure_depolarizes_history_retains_information',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'failure_channel':{'definition':'Phi(X)=sum_g R_g X R_g*; eighteen actual retained controller components',
                           'plus_block':'Phi(X_plus)=(-4/25)*X_plus+(2/5)*tr(X_plus)*P_plus',
                           'minus_block':'Phi(X_minus)=(1/5)*X_minus+(2/5)*tr(X_minus)*P_minus',
                           'operator_basis_tests':16,'sector_transfer':False,
                           'positive_square_root_effect_substitute_is_same_channel':False,
                           'plus_branch_records':branch_records},
        'retained_retry_tree':{'history':'each failure appends a fresh controller slot; first success time is retained',
                               'coherent_history_map':'sum_history |history> tensor R_last...R_first',
                               'all_failure_effect':'P_minus+(16/25)^n*P_plus',
                               'cumulative_success_effect':'[1-(16/25)^n]*P_plus',
                               'first_success_effect_at_attempt_k':'(9/25)*(16/25)^(k-1)*P_plus',
                               'finite_depth_checks':checks,'all_depth_argument':'dual(P_plus)=(16/25)P_plus and dual(P_minus)=P_minus',
                               'ever_success_probability':'tr(P_plus*rho)',
                               'all_failure_limit_effect':'P_minus',
                               'deterministic_preparation_from_general_input':False},
        'logical_state_gate':{'reduced_plus_state_after_n_failures':'Bloch vector multiplied by (-1/4)^n',
                               'first_success_logical_state_depends_on_failure_history':True,
                               'success_time_pooled_infinite_retry_Bloch_factor':'9/29',
                               'pure_plus_input_pooled_success_purity':'461/841',
                               'pure_plus_witness':retry_witness,'pooled_success_witness':record(pooled),
                               'joint_controller_information_destroyed':False,
                               'depolarization_scope':'system reduction after ignoring failure history; branchwise plus unitary correction is a further control gate'},
        'lead_readout_gate':{'reduced_map':'Delta(X)=diag(X) on ground-label coordinates',
                             'plus_weight_after_readout':'tr(X)/2','minus_weight_after_readout':'tr(X)/2',
                             'plus_to_plus_map':'P_plus Delta(X_plus) P_plus=(X_plus+tr(X_plus)P_plus)/6',
                             'conditional_plus_Bloch_factor_after_readout':'1/3',
                             'fixed_lead_readout_preserves_original_sector':False,
                             'record_retained_in_readout_instrument':True,
                             'not_part_of_retry_formula_above':True},
        'boundary':{'new_controls_from_predecessor_still_required':True,
                    'history_traced_for_statistics_means_records_erased':False,
                    'retry_success_is_physical_spin_admission':False,'formal_outcome_admitted':False},
        'next_gate':'Test history-conditioned polar correction of the failure branches: can it restore the plus logical state with a gauge-compatible extension on the minus sector, and is that correction in the admitted native control library? Keep feedback/work/history requirements explicit.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale retry receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: actual failure channel gives exact all-history retry effects; eventual success equals initial plus weight.')
    print('PASS: reduced logical state depolarizes while controller history remains available; lead readout mixes sectors.')


if __name__=='__main__':main()
