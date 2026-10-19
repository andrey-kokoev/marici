"""Local analytic continuation of the reference plane; exact polynomial certificates.

Rational arithmetic checks the characteristic/discriminant identities and a
Riccati jet. Analytic existence uses the nonsingular finite-dimensional implicit
function theorem, not an assertion that a truncated jet is an exact global frame.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, eye, encode
from check_graded_boundary_transport import audit as graded_audit, inverse, add as madd, scale as mscale
from check_retained_word_transport import poly, add, sub, mul, scale

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/moving-boundary-plane.v1.json'


def determinant(matrix):
    n=len(matrix);out={}
    for perm in permutations(range(n)):
        if any(not matrix[i][perm[i]] for i in range(n)):continue
        term=poly((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):term=mul(term,matrix[i][perm[i]])
        out=add(out,term)
    return out


def block(M,i,j):return [row[j:j+2] for row in M[i:i+2]]
def zero():return [[F(0),F(0)],[F(0),F(0)]]


def audit():
    previous=graded_audit();carrier=previous['minimal_constant_carrier']
    A=carrier['one_step_A4'];C=carrier['two_step_C4']
    z=poly(variable=0);lam=poly(variable=1)
    zp=[poly(1)]
    for i in range(22):zp.append(mul(zp[-1],z))
    pencil=[[sub(scale(lam,i==j),add(scale(z,A[i][j]),scale(zp[2],C[i][j]))) for j in range(4)] for i in range(4)]
    characteristic=determinant(pencil)
    p=scale(zp[4],-1);q=scale(add(zp[4],zp[5]),-1);r=scale(zp[5],-1)
    expected=add(add(mul(mul(lam,lam),mul(lam,lam)),mul(p,mul(lam,lam))),add(mul(q,lam),r))
    assert characteristic==expected
    # Quartic / derivative Sylvester determinant, computed independently of
    # the closed discriminant formula for a depressed quartic.
    coefficients=[poly(1),{},p,q,r]
    derivative=[poly(4),{},scale(p,2),q]
    sylvester=[]
    for shift in range(3):sylvester.append([{}]*shift+coefficients+[{}]*(2-shift))
    for shift in range(4):sylvester.append([{}]*shift+derivative+[{}]*(3-shift))
    discriminant=determinant(sylvester)
    sept={}
    for power,coefficient in enumerate([-256,-27,36,-2,36,-23,-8,4]):sept=add(sept,scale(zp[power],coefficient))
    assert discriminant==mul(zp[15],sept)
    assert sum(discriminant.values())==-240

    # M(1+epsilon)=M0+epsilon M1+epsilon^2 M2.
    Ms=[madd(A,C),madd(A,mscale(C,2)),C]
    P=[block(m,0,0) for m in Ms];Q=[block(m,0,2) for m in Ms]
    R=[block(m,2,0) for m in Ms];S=[block(m,2,2) for m in Ms]
    T=P[0]
    assert T==[[-F(1,2),F(1,2)],[-F(3,2),-F(1,2)]] and R[0]==zero()
    # Characteristic factors at z=1 are disjoint: Phi3 and lambda^2-lambda-1.
    phi=add(add(mul(lam,lam),lam),poly(1))
    other=sub(sub(mul(lam,lam),lam),poly(1))
    at_one={}
    for (_,power,_),coefficient in characteristic.items():
        at_one=add(at_one,{(0,power,0):coefficient})
    assert at_one==mul(phi,other)

    columns=[]
    for k in range(4):
        basis=[[F(2*i+j==k) for j in range(2)] for i in range(2)]
        image=madd(mm(S[0],basis),mscale(mm(basis,T),-1))
        columns.append(sum(image,[]))
    L=list(map(list,zip(*columns)))
    detL=determinant([[poly(value) for value in row] for row in L])
    assert detL==poly(4)
    Linv=inverse(L)
    assert mm(L,Linv)==eye(4)

    order=4
    def product_series(left,right):
        out=[zero() for _ in range(order+1)]
        for i,a in enumerate(left):
            for j,b in enumerate(right):
                if i+j<=order:out[i+j]=madd(out[i+j],mm(a,b))
        return out
    def riccati(X):
        sx=product_series(S,X);xp=product_series(X,P)
        xqx=product_series(product_series(X,Q),X)
        return [madd(madd(R[i] if i<len(R) else zero(),sx[i]),mscale(madd(xp[i],xqx[i]),-1)) for i in range(order+1)]
    X=[zero() for _ in range(order+1)]
    for n in range(1,order+1):
        known=riccati(X)[n]
        rhs=[[-v] for v in sum(known,[])]
        solved=mm(Linv,rhs)
        X[n]=[[solved[2*i+j][0] for j in range(2)] for i in range(2)]
        assert riccati(X)[n]==zero()
    assert all(m==zero() for m in riccati(X))
    assert X[1]==[[-F(1,8),F(5,8)],[F(1,4),-F(1,4)]]
    QX=product_series(Q,X)
    effective=[madd(P[i] if i<len(P) else zero(),QX[i]) for i in range(order+1)]
    assert effective[0]==T
    trace=[m[0][0]+m[1][1] for m in effective]
    det=[sum(effective[i][0][0]*effective[n-i][1][1]-effective[i][0][1]*effective[n-i][1][0] for i in range(n+1)) for n in range(order+1)]
    assert trace[:2]==[-1,-2] and det[:2]==[1,F(5,2)]
    phi_series=product_series(effective,effective)
    phi_series=[madd(madd(phi_series[i],effective[i]),eye(2) if i==0 else zero()) for i in range(order+1)]
    assert phi_series[0]==zero() and phi_series[1]!=zero()

    dependencies=list(previous['source_sha256'])+[
        'research/scattering/seed-composition/check_moving_boundary_plane.py',
        'research/scattering/seed-composition/check_retained_word_transport.py']
    return {
        'schema':'marici.scattering.moving-boundary-plane.v1',
        'status':'unique_local_analytic_graph_plane_exists_phase_and_modulus_deform',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'characteristic':'lambda^4-z^4*lambda^2-(z^4+z^5)*lambda-z^5',
        'at_z_one_factorization':'(lambda^2+lambda+1)*(lambda^2-lambda-1)',
        'discriminant':'z^15*(4*z^7-8*z^6-23*z^5+36*z^4-2*z^3+36*z^2-27*z-256)',
        'discriminant_at_one':-240,
        'local_graph':{'epsilon':'z-1','embedding_in_four_carrier':'[I_2; X(epsilon)]','X_at_zero':zero(),
                       'equation':'R+S X-X P-X Q X=0, with M=[[P,Q],[R,S]]',
                       'linearization':'L(Y)=S0 Y-Y T','linearization_matrix':L,'linearization_determinant':4,
                       'existence_basis':'analytic implicit-function theorem at X=0, epsilon=0',
                       'unique_scope':'analytic graph near the original plane; not uniqueness of all global invariant planes',
                       'series_coefficients_through_order_4':X,
                       'residual_zero_through_order':4,'convergence_radius_certified':False},
        'induced_step':{'formula':'T(epsilon)=P(epsilon)+Q(epsilon)X(epsilon)',
                        'series_coefficients_through_order_4':effective,
                        'trace_series':trace,'determinant_series':det,
                        'phi3_first_derivative':phi_series[1],
                        'real_local_conjugate_pair_modulus':'1+(5/4)*(z-1)+O((z-1)^2)',
                        'exact_C3_persists_under_grading':False},
        'global_boundary':{'discriminant_zeros_are_candidate_spectral_collision_locus':True,
                           'every_collision_is_a_singularity_of_selected_plane':False,
                           'rational_global_rank_two_frame_constructed':False},
        'boundary':{'physical_clock_or_normalization_derived':False,'native_parse_control_derived':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Track the selected local plane along real positive z: isolate spectral collisions and distinguish a two-eigenvalue internal collision from a loss of separation from the complementary sector; do not infer bundle singularities from the full discriminant alone.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale moving-plane receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact characteristic/discriminant; Sylvester determinant 4 gives a unique local analytic graph plane.')
    print('PASS: Riccati jet through order 4; trace derivative -2 and determinant derivative 5/2, so C3 does not persist.')
    print('Boundary: local existence, not certified global continuation, physical normalization or photon identification.')


if __name__=='__main__':main()
