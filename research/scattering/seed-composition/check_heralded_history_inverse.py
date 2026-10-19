"""Optimal witnessed-history inverse filters with explicit retained failure effects."""
from fractions import Fraction as F
import argparse
import json

from check_classical_history_recovery import audit as history_audit
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qi,qsign,qrecord
from check_selector_failure_feedback import mul,dagger
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import S2,S3,CI
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import spin

DEST=BASE/'results/heralded-history-inverse.v1.json'


def zero(n=2):return tuple(tuple(ZERO for _ in range(n)) for _ in range(n))
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def pscale(c,X):return (scale(c,X[0]),scale(c,X[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def encode(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}
def scalar_record(X):return (F(X['constant']),F(X['sqrt19']))
def trace(X):return sum((X[i][i] for i in range(len(X))),ZERO)


def inverse2(X):
    def times(x,y):return (x[0]*y[0]+19*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def subtract(x,y):return (x[0]-y[0],x[1]-y[1])
    entry=lambda i,j:(X[0][i][j],X[1][i][j])
    determinant=subtract(times(entry(0,0),entry(1,1)),times(entry(0,1),entry(1,0)))
    norm=determinant[0]*determinant[0]-19*determinant[1]*determinant[1]
    inv=(determinant[0]/norm,-determinant[1]/norm)
    entries=[[times(inv,entry(1,1)),times(inv,(-X[0][0][1],-X[1][0][1]))],
             [times(inv,(-X[0][1][0],-X[1][1][0])),times(inv,entry(0,0))]]
    result=tuple(tuple(tuple(entries[i][j][part] for j in range(2)) for i in range(2)) for part in range(2))
    assert mul(result,X)==mul(X,result)==(eye(2),zero())
    return result


def audit():
    previous=history_audit();witness=previous['positive_probability_counterexample']
    g,h=[tuple(F(x) for x in q) for q in witness['chronological_failures']]
    assert abs(g[0])==1 and abs(h[0])==F(1,2)
    source=load('research/strominger/results/common-endpoint-charging.json')
    K=tuple(tuple(decode(x) for x in row) for row in source['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    u=tuple((S2*Pm[i][0],) for i in range(4));v=tuple((S2*Pm[i][1],) for i in range(4))
    v=scale(S3/S2,add(v,scale(-mm(adj(u),v)[0][0],u)))
    Um=tuple((u[i][0],v[i][0]) for i in range(4));assert mm(adj(Um),Um)==eye(2)
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6;anchor=tuple(face[0][i][0] for i in range(2));lines=[anchor]
    for i in range(1,4):lines.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(lines[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(h))
    p=[face.index(mm(mm(U,x),adj(U))) for x in face]
    raw=tuple(tuple(U[i%2][j%2] if i//2==p[j//2] else ZERO for j in range(8)) for i in range(8))
    S=scale(A(1 if h[0]>0 else -1),mm(mm(D,raw),V));Sm=mm(mm(adj(Um),S),Um)
    E1=tuple(tuple(decode(x) for x in row) for row in witness['logical_eigenprojectors']['H_eigenvalue_1'])
    Em=tuple(tuple(decode(x) for x in row) for row in witness['logical_eigenprojectors']['H_eigenvalue_minus_2'])
    assert add(Sm,adj(Sm))==add(E1,scale(A(-2),Em))
    c,s=F(99,101),F(20,101);weight=F(witness['positive_history_preparation_weight']);assert weight==F(9,5000)
    kh=(zero(),scale(A(F(1,5)),eye(2)))
    lp=qscale(qr(F(2,5)),padd(qscale(qr(c*c),kh),(scale(A(-s*s),Sm),zero())))
    lm=pscale(-CI*c*s,padd(kh,(Sm,zero())))
    ident=(eye(2),zero());rows=[]
    for item,L,Elow,Ehigh in zip(witness['code_witnesses'],(lp,lm),(E1,Em),(Em,E1)):
        low=scalar_record(item['minimum_eigenstate_branch_probability']);high=scalar_record(item['maximum_eigenstate_branch_probability'])
        assert qsign(low)>0 and qsign(qa(high,qn(low)))>0
        G=pscale(A(weight),mul(dagger(L),L))
        assert G==padd(qscale(low,(Elow,zero())),qscale(high,(Ehigh,zero())))
        inverse=inverse2(L)
        low_unscaled=qmul(low,qr(1/weight))
        # N=sqrt(low/weight)*L^{-1}, K=sqrt(weight)*L. Scalar roots
        # are kept as positive factored prefactors; their squares are exact.
        N_effect=qscale(low_unscaled,mul(dagger(inverse),inverse))
        out_low=qscale(qmul(qr(weight),qi(low)),mul(mul(L,(Elow,zero())),dagger(L)))
        out_high=qscale(qmul(qr(weight),qi(high)),mul(mul(L,(Ehigh,zero())),dagger(L)))
        for E in (out_low,out_high):
            assert dagger(E)==E and mul(E,E)==E
            assert trace(E[0])==ONE and trace(E[1])==ZERO
        assert padd(out_low,out_high)==ident and mul(out_low,out_high)==(zero(),zero())
        ratio=qmul(low,qi(high));alpha=qa(qr(1),qn(ratio));assert qsign(alpha)>0
        assert N_effect==padd(out_low,qscale(ratio,out_high))
        F_effect=qscale(alpha,out_high)
        assert padd(N_effect,F_effect)==ident
        # Whole witnessed leaf: inverse-success and inverse-failure effects
        # add back to its original effect, not to a silently selected state.
        success_original=pscale(A(weight),mul(mul(dagger(L),N_effect),L))
        failure_original=pscale(A(weight),mul(mul(dagger(L),F_effect),L))
        assert success_original==qscale(low,ident)
        gap=qa(high,qn(low));assert failure_original==qscale(gap,(Ehigh,zero()))
        assert padd(success_original,failure_original)==G
        assert mul(inverse,L)==ident  # NK=sqrt(low)I, reference recovery
        conditional_bell=qmul(qmul(qr(2),low),qi(qa(low,high)))
        failure_bell=qmul(qr(F(1,2)),gap)
        assert qsign(conditional_bell)>0 and qsign(qa(qr(1),qn(conditional_bell)))>0
        rows.append({'code':item['code'],'unscaled_history_map':encode(L),'history_scale_squared':str(weight),
                     'original_branch_effect':encode(G),
                     'inverse_success_Kraus':{'positive_prefactor_squared':qrecord(low_unscaled),'matrix':encode(inverse)},
                     'inverse_failure_Kraus':{'positive_prefactor_squared':qrecord(alpha),'matrix_projector':encode(out_high)},
                     'inverse_success_effect':encode(N_effect),'inverse_failure_effect':encode(F_effect),
                     'filter_completeness':True,'combined_leaf_success_effect':'lambda_min*I2',
                     'combined_leaf_failure_effect':encode(failure_original),
                     'optimal_uniform_original_input_success_probability':qrecord(low),
                     'conditional_inverse_success_on_Bell_branch':qrecord(conditional_bell),
                     'inverse_success_restores_Bell_exactly':True,
                     'original_Bell_input_inverse_failure_probability':qrecord(failure_bell),
                     'inverse_failure_Bell_output_Schmidt_rank':1,
                     'inverse_failure_rank_on_code':1,
                     'conditional_success_min_eigenstate':'1','conditional_success_max_eigenstate':qrecord(ratio)})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_heralded_history_inverse.py'}
    return {
        'schema':'marici.scattering.heralded-history-inverse.v1',
        'status':'optimal_heralded_inverse_restores_known_code_and_reference_with_explicit_rank_one_failure',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'witness_history':witness['chronological_failures'],'success_attempt':3,
        'filters':rows,
        'optimality':{'formula':'N=sqrt(lambda_min)K^{-1}',
                      'constraint':'N* N<=I requires uniform original-input acceptance <=lambda_min(K* K)',
                      'failure':'F=sqrt(1-lambda_min/lambda_max)*Pi_output,high',
                      'complete_instrument':'N* N+F* F=I',
                      'composed_leaf':'NK=sqrt(lambda_min)I; FK has rank one and effect (lambda_max-lambda_min)Pi_input,high',
                      'nested_scalar_roots':'positive factored prefactors; exact squares and every matrix/effect identity are verified without numerical roots'},
        'reference_scope':{'known_plus_or_minus_code_required':True,'inverse_output':'logical original code; a physical code-frame embedding is an additional control',
                           'heralded_success_restores_unknown_code_and_reference':True,
                           'failure_can_restore_arbitrary_entangled_input':False,
                           'failure_is_a_retained_output_not_erased':True,
                           'classical_failure_retry_can_undo_rank_one_collapse':False},
        'coherent_comparison':{'full_original_dilation_isometry':True,
                               'coherent_left_inverse_on_dilation_range_exists':True,
                               'requires':'joint coherent system/history/apparatus access, inverse controls and all records; finite-depth circuit undoing also retains its terminal failure',
                               'classical_record_only_is_equivalent_access':False,
                               'coherent_left_inverse_physically_implemented':False},
        'boundary':{'new_inverse_filter_and_readout_controls_required':True,
                    'heralded_success_is_deterministic_recovery':False,'shared_sources_or_receipts_changed':False,
                    'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Construct a retained two-outcome flag dilation of the optimal inverse filter, with explicit gauge-compatible controlled rotation and its failure flag. Compare coherent uncomputation with measuring that flag, specifying the additional projector/pulse and apparatus-access obligations.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale heralded inverse receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: optimal witnessed-history inverse filters restore both known codes/reference on success, with exact Kraus completeness.')
    print('PASS: rank-one failure and probability cost are retained; coherent dilation inversion is a different access/control assumption.')


if __name__=='__main__':main()
