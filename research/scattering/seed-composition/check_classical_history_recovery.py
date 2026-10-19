"""Classically flagged successful-history recovery tests on both logical doublets."""
from fractions import Fraction as F
import argparse
import json

from check_recycling_information_channel import audit as information_audit,qa,qn,qm as qmul,qr,qsign,qrecord,qi
from check_selector_failure_feedback import mul,dagger
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import S2,S3,CI
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import spin

DEST=BASE/'results/classical-history-recovery.v1.json'


def zero(n=2):return tuple(tuple(ZERO for _ in range(n)) for _ in range(n))
def trace(X):return sum((X[i][i] for i in range(len(X))),ZERO)
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def pscale(c,X):return (scale(c,X[0]),scale(c,X[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def gram(X):return mul(dagger(X),X)
def scalar_effect(X):return all(add(M,scale(-trace(M)/2,eye(2)))==zero() for M in X)
def encode(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}


def audit():
    previous=information_audit();source=load('research/strominger/results/common-endpoint-charging.json')
    K=tuple(tuple(decode(x) for x in row) for row in source['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    def frame(projector):
        u=tuple((S2*projector[i][0],) for i in range(4));v=tuple((S2*projector[i][1],) for i in range(4))
        v=scale(S3/S2,add(v,scale(-mm(adj(u),v)[0][0],u)))
        out=tuple((u[i][0],v[i][0]) for i in range(4));assert mm(adj(out),out)==eye(2)
        return out
    Up,Um=frame(P),frame(Pm)
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6;anchor=tuple(face[0][i][0] for i in range(2));w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    quats={tuple(F(sign if i==k else 0) for i in range(4)) for k in range(4) for sign in (-1,1)}
    from itertools import product
    quats.update(tuple(F(sign,2) for sign in signs) for signs in product((-1,1),repeat=4))
    branches=[]
    for q in sorted(quats):
        if not q[0]:continue
        U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        p=[face.index(mm(mm(U,x),adj(U))) for x in face]
        raw=tuple(tuple(U[i%2][j%2] if i//2==p[j//2] else ZERO for j in range(8)) for i in range(8))
        T=mm(mm(D,raw),V);S=scale(A(1 if q[0]>0 else -1),T)
        Sm=mm(mm(adj(Um),S),Um);assert mm(adj(Sm),Sm)==eye(2)
        central=abs(q[0])==1
        if central:assert Sm==eye(2)
        else:
            H=add(Sm,adj(Sm));assert add(mm(H,H),H)==scale(A(2),eye(2))
            assert H!=scale(trace(H)/2,eye(2))
        branches.append({'q':q,'Sm':Sm,'k':qr(F(2,5)) if central else (F(0),F(1,5)),
                         'p':F(1,10) if central else F(1,20),'central':central})
    assert len(branches)==18
    c,s=F(99,101),F(20,101);success=F(9,25)
    stats=[{'success_attempt':1,'history_branches':1,'plus_scalar_effects':1,'minus_scalar_effects':1,'minus_branch_zero':True}]
    for g in branches:
        # First failure followed by success: both restrictions are scaled
        # unitaries (minus is carried into plus by the fixed frame swap).
        lp=qscale(qmul(qr(c),g['k']),(eye(2),zero()))
        lm=(scale(-CI*s,g['Sm']),zero())
        assert scalar_effect(gram(lp)) and scalar_effect(gram(lm))
    stats.append({'success_attempt':2,'history_branches':18,'plus_scalar_effects':18,'minus_scalar_effects':18})
    passing_plus=0;passing_minus=0;witness=None
    for g in branches:
        for h in branches:
            kh=qscale(h['k'],(eye(2),zero()))
            # Chronological failures g then h; success is at attempt three.
            lp=qscale(g['k'],padd(qscale(qr(c*c),kh),(scale(A(-s*s),h['Sm']),zero())))
            lm=pscale(-CI*c*s,mul(padd(kh,(h['Sm'],zero())),(g['Sm'],zero())))
            weight=success*g['p']*h['p'];gp=pscale(A(weight),gram(lp));gm=pscale(A(weight),gram(lm))
            okp=scalar_effect(gp);okm=scalar_effect(gm)
            assert okp==okm==h['central']
            passing_plus+=int(okp);passing_minus+=int(okm)
            if witness is None and g['central'] and not h['central']:
                H=add(h['Sm'],adj(h['Sm']));E1=scale(A(F(1,3)),add(H,scale(A(2),eye(2))))
                Em=scale(A(F(1,3)),add(eye(2),scale(A(-1),H)) )
                for E in (E1,Em):assert adj(E)==E and mm(E,E)==E and rank(E)==1
                assert add(E1,Em)==eye(2) and mm(E1,Em)==zero()
                assert mm(H,E1)==E1 and mm(H,Em)==scale(A(-2),Em)
                def eigenvalues(G):
                    out=[]
                    for E in (E1,Em):
                        parts=(trace(mm(E,G[0])),trace(mm(E,G[1])))
                        vals=[]
                        for part in parts:
                            assert all(x==0 for x in part.c[1:]);vals.append(part.c[0])
                        out.append(tuple(vals))
                    return out
                ep=eigenvalues(gp);en=eigenvalues(gm)
                assert qsign(qa(ep[1],qn(ep[0])))>0 and qsign(qa(en[0],qn(en[1])))>0
                entries=[]
                for code,G,low,high in (('plus',gp,ep[0],ep[1]),('minus',gm,en[1],en[0])):
                    assert qsign(low)>0
                    total=qa(low,high);gap=qa(high,qn(low))
                    schmidt=(qmul(low,qi(total)),qmul(high,qi(total)))
                    concurrence_squared=qmul(qmul(qr(4),qmul(low,high)),qi(qmul(total,total)))
                    assert qsign(qa(qr(1),qn(concurrence_squared)))>0
                    bound=qa(qr(1),qn(qmul(qr(F(1,2)),gap)))
                    entries.append({'code':code,'branch_effect':encode(G),
                                    'minimum_eigenstate_branch_probability':qrecord(low),
                                    'maximum_eigenstate_branch_probability':qrecord(high),
                                    'filtered_Bell_Schmidt_weights':[qrecord(x) for x in schmidt],
                                    'filtered_Bell_concurrence_squared':qrecord(concurrence_squared),
                                    'all_histories_uniform_heralded_inverse_success_upper_bound_from_this_leaf':qrecord(bound)})
                witness={'chronological_failures':[list(map(str,g['q'])),list(map(str,h['q']))],
                         'success_attempt':3,'positive_history_preparation_weight':str(weight),
                         'logical_eigenprojectors':{'H_eigenvalue_1':record(E1),'H_eigenvalue_minus_2':record(Em)},
                         'code_witnesses':entries}
    assert passing_plus==passing_minus==36 and witness is not None
    stats.append({'success_attempt':3,'history_branches':324,'plus_scalar_effects':passing_plus,
                  'minus_scalar_effects':passing_minus,'non_scalar_each_code':288})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_classical_history_recovery.py'}
    return {
        'schema':'marici.scattering.classical-history-recovery.v1',
        'status':'third_attempt_non_scalar_success_branches_obstruct_deterministic_classical_history_recovery_on_both_doublets',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'recovery_criterion':{'classical_flagged_channel':'sum_h |h><h| tensor K_h X K_h*',
                              'code_condition':'P_code K_h* K_h P_code = lambda_h P_code for every history',
                              'meaning':'required for deterministic exact code recovery; when output/code dimensions are two this also permits history-conditioned unitary inversion',
                              'scope':'known plus or known minus code; no additional logical-state prior'},
        'early_history_tests':stats,
        'third_attempt_formula':{'unscaled_plus_map':'k_g[c² k_h I-s² S_h,minus]',
                                 'unscaled_minus_map':'-i c s[k_h I+S_h,minus]S_g,minus',
                                 'branch_effect_scale':'(9/25)*p_g*p_h',
                                 'k_central':'2/5','k_half':'sqrt(19)/5',
                                 'history_order':'g failure, then h failure, then success'},
        'positive_probability_counterexample':witness,
        'conclusions':{'classical_record_conditioned_deterministic_recovery_plus':False,
                       'classical_record_conditioned_deterministic_recovery_minus':False,
                       'all_early_successes_are_uncorrectable':False,
                       'logical_state_information_in_history_probabilities':True,
                       'postselected_inverse_can_be_possible':True,
                       'coherent_full_dilation_isometry_invalidated':False,
                       'classical_record_is_same_as_coherent_apparatus_access':False},
        'bound_argument':'Kraus completeness gives sum_h tr(G_h)/2=1 on either code. Branchwise uniform exact inverse success <=sum_h lambda_min(G_h). The exhibited leaf has lambda_max>lambda_min, forcing an upper bound strictly below one by half its eigenvalue gap.',
        'boundary':{'new_control_and_recycling_inputs_still_required':True,'failure_records_erased':False,
                    'arbitrary_physical_implementation_or_spin_admitted':False,'formal_outcome_admitted':False},
        'next_gate':'Construct optimal heralded inverse filters for the exhibited successful histories, with explicit success/failure Kraus completeness and reference recovery. Compare classical branchwise inversion with coherent undoing of the retained dilation; state the additional control and probability costs.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale classical-history receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: attempts one/two have scalar code effects; 288 third-attempt histories have non-scalar effects on each doublet.')
    print('PASS: explicit state-dependent branch/Bell witnesses exclude deterministic classical-history recovery; coherent dilation is retained.')


if __name__=='__main__':main()
