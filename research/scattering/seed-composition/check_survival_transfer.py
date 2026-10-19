"""Exact decay and Perron reweighting of the conditional counting survival transfer."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, eye, encode
from check_conditioned_history_weights import audit as weights_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/survival-transfer.v1.json'


def characteristic(A):
    n=len(A);B=eye(n);coefficients=[F(1)]
    for k in range(1,n+1):
        AB=mm(A,B);c=-sum(AB[i][i] for i in range(n))/k
        coefficients.append(c)
        B=[[AB[i][j]+c*F(i==j) for j in range(n)] for i in range(n)]
    assert all(not v for row in B for v in row)
    return coefficients


def ring(p):
    p=list(p)+[F(0)]*max(0,5-len(p))
    for k in range(len(p)-1,4,-1):
        v=p[k];p[k]=F(0);p[k-4]+=v/32;p[k-5]+=v/16
    return tuple(p[:5])
def plus(a,b):return ring([a[i]+b[i] for i in range(5)])
def times(a,b):
    p=[F(0)]*9
    for i,x in enumerate(a):
        for j,y in enumerate(b):p[i+j]+=x*y
    return ring(p)
def scale(a,c):return tuple(x*c for x in a)
def polynomial(x):return 32*x**5-x-2


def audit():
    previous=weights_audit();K=previous['survival_recurrence']['backward_matrix_K']
    n=len(K);reach=[[bool(K[i][j]) or i==j for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):reach[i][j]=reach[i][j] or (reach[i][k] and reach[k][j])
    groups=[];unused=set(range(n))
    while unused:
        i=min(unused);group=[j for j in sorted(unused) if reach[i][j] and reach[j][i]]
        groups.append(group);unused.difference_update(group)
    assert groups==[[0,1,2,3,4,5,12,13,14],[6,7,8,9,10,11,15,16,17]]
    assert all(not K[i][j] for group in groups for i in group for j in range(n) if j not in group)
    block=[[K[i][j] for j in groups[0]] for i in groups[0]]
    coeff=characteristic(block)
    assert coeff==[1,0,0,0,-F(1,32),-F(1,16),0,0,0,0]
    # Graph positivity, independent of a floating-point spectrum.
    adjacency=[[int(v>0) for v in row] for row in block];power=eye(9);exponent=None
    for k in range(1,31):
        power=mm(power,adjacency)
        if all(v>0 for row in power for v in row):exponent=k;break
    assert exponent==19
    K3=mm(K,mm(K,K));row_sums=[sum(row) for row in K3]
    assert max(row_sums)==F(1,2) and min(row_sums)==F(1,8)
    assert all(0<sum(row)<=1 for row in K)
    lo=F(3,5);hi=F(5,8)
    assert polynomial(lo)<0<polynomial(hi)
    # f decreases until its unique positive derivative zero, then increases;
    # f(0)<0 guarantees exactly one positive root. A positive block's PF root
    # is therefore the root in this exact rational bracket.
    one=ring([F(1)]);rho=ring([F(0),F(1)])
    inverse=ring([-F(1,2),0,0,0,F(16)])
    assert times(rho,inverse)==one
    inv2=times(inverse,inverse);inv3=times(inv2,inverse)
    h=[None]*18
    values=[one,scale(rho,2),scale(inv2,F(1,4)),scale(inv3,F(1,2)),inverse,one,
            scale(inverse,F(1,2)),inv2,scale(rho,2)]
    for s,v in zip(groups[0],values):h[s]=v
    reflection=[9,10,11,6,7,8,3,4,5,0,1,2,17,15,16,13,14,12]
    assert all(reflection[reflection[s]]==s for s in range(18))
    assert all(K[reflection[i]][reflection[j]]==K[i][j] for i in range(18) for j in range(18))
    for s in groups[0]:h[reflection[s]]=h[s]
    for i in range(18):
        Kh=ring([F(0)])
        for j in range(18):Kh=plus(Kh,scale(h[j],K[i][j]))
        assert Kh==times(rho,h[i])
    assert h[0]!=h[4]
    # Explicit Doob row for a branching context: unlike the controller-only
    # equal target weights, the limiting conditioned choice depends on h.
    # Row 1 targets 2 and 3. h3/h2=2/rho>1; hence unequal choices.
    assert times(h[3],rho)==scale(h[2],2)

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_survival_transfer.py']
    return {
        'schema':'marici.scattering.survival-transfer.v1',
        'status':'uniform_decay_certified_two_primitive_classes_have_nonconstant_algebraic_conditioning_profile',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'classes':{'closed_strongly_connected_components':groups,'reflection_exchanges_classes':True,
                   'positive_power_per_block':exponent,'period_per_block':1,
                   'global_unique_stationary_or_conditioned_class':False},
        'decay':{'max_row_sum_K3':max(row_sums),'bound':'0<q_n(s)<=2^(-floor(n/3))',
                 'all_states_survival_tends_to_zero':True,'first_reject_total_weight_tends_to_one':True},
        'perron_certificate':{'block_characteristic_descending':coeff,
                              'nonzero_factor':'lambda^5-lambda/32-1/16',
                              'rho_equation':'32*rho^5-rho-2=0',
                              'unique_positive_root_bracket':[lo,hi],
                              'rho_below_one':True,'other_block_eigenvalues_strictly_smaller_in_modulus':True,
                              'reason':'positive nineteenth power and Perron-Frobenius; exact characteristic and positive h'},
        'backward_profile':{'normalization':'h(0)=h(9)=1',
                            'first_class_order':groups[0],
                            'first_class_h':['1','2*rho','1/(4*rho^2)','1/(2*rho^3)','1/rho','1','1/(2*rho)','1/rho^2','2*rho'],
                            'second_class':'reflection of first class',
                            'Kh_equals_rho_h_verified_modulo_equation':True,
                            'q_n_over_rho_n':'tends to c*h for q0=1; same positive c on reflected classes',
                            'q_n_s_over_q_n_0':'tends to h(s) for the reflection-symmetric all-ones terminal seed',
                            'nonconstant':True,
                            'general_terminal_seed':'different positive Perron coefficients may survive in the two closed classes'},
        'conditioned_control':{'finite_horizon':'K(s,t)*q_(N-1)(t)/q_N(s)',
                               'limit':'Khat(s,t)=K(s,t)*h(t)/(rho*h(s))',
                               'row_sum_one':'follows exactly from Kh=rho*h',
                               'same_as_controller_equal_target_split':False,
                               'branching_context_1':'Khat(1,3)/Khat(1,2)=h(3)/h(2)=2/rho, not 1',
                               'physical_control_or_probabilities_derived':False},
        'boundary':{'decay_is_physical_clock_or_emission_rate':False,'conditioned_reweighting_source_authorized':False,
                    'history_or_first_reject_records_erased':False,'formal_outcome_admitted':False},
        'next_gate':'Pull the nonconstant Perron profile back to the selected initial two-plane and test whether any scalar or reference-mode-invariant normalization can realize the limiting conditioning; distinguish algebraic state filtering from the native controller.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale survival-transfer receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: K^3 row sums at most 1/2 certify uniform survival decay; two reflected primitive classes identified.')
    print('PASS: exact quintic Perron root and nonconstant positive profile determine conditioned reweighting.')
    print('Boundary: algebraic counting-control limit, not a physical clock, probability law or authorized preparation.')


if __name__=='__main__':main()
