"""Exact Hamiltonian realization of the actual finite Bool square.
Continuous interpolation, complex coefficients and metric are declared inputs.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
from check_triangle_half_phase import zadd,zmul,zconj,zscale,znorm
ROOT=Path(__file__).resolve().parents[1]
ONE=(F(1),F(0));ZERO=(F(0),F(0))

def eye(n):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def transpose(a):return tuple(zip(*a))
def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(c,a):return tuple(tuple(c*x for x in r) for r in a)
def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(r,c)) for c in transpose(b)) for r in a)
def block(a,b,c,d):return tuple(r+s for r,s in zip(a,b))+tuple(r+s for r,s in zip(c,d))
def cm(a):return tuple(tuple((x,F(0)) for x in r) for r in a)
def zsum(v):
    s=ZERO
    for x in v:s=zadd(s,x)
    return s
def cmm(a,b):return tuple(tuple(zsum(zmul(x,y) for x,y in zip(r,c)) for c in transpose(b)) for r in a)
def adj(a):return tuple(tuple(zconj(x) for x in r) for r in transpose(a))
def mv(a,v):return tuple(zsum(zmul(x,y) for x,y in zip(r,v)) for r in a)
def minus(a,b):return tuple(zadd(x,zscale(y,-1)) for x,y in zip(a,b))
def norm(v):return sum(znorm(x) for x in v)
def power(z,k):
    out=ONE
    for _ in range(k):out=zmul(out,z)
    return out

def main():
    proof=json.loads((ROOT/'results/agda-NativeSquareHamiltonianSkeleton.json').read_text(encoding='utf-8-sig'))
    assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
    for name in ('NativeSquareHamiltonianSkeleton.agda','ObserverCoherenceCube.agda'):
        assert proof['owner_source_inventory_sha256'][name]==hashlib.sha256((ROOT/'agda'/name).read_bytes()).hexdigest()
    I=eye(4);Z=scale(0,I)
    # Source basis order is 00,01,10,11; columns contain images of basis states.
    L=tuple(tuple(F(i==(j^2)) for j in range(4)) for i in range(4))
    R=tuple(tuple(F(i==(j^1)) for j in range(4)) for i in range(4))
    assert mm(L,L)==I and mm(R,R)==I and mm(L,R)==mm(R,L)
    PL=scale(F(1,2),add(I,scale(-1,L)));PR=scale(F(1,2),add(I,scale(-1,R)))
    for P in (PL,PR):assert transpose(P)==P and mm(P,P)==P
    assert mm(PL,PR)==mm(PR,PL)
    H=add(PL,PR);H3=add(scale(3,PL),PR);Hsym=scale(3,H)
    joints={}
    for a,b in product((0,1),repeat=2):
        J=mm(PL if a else add(I,scale(-1,PL)),PR if b else add(I,scale(-1,PR)))
        assert mm(J,J)==J and sum(J[i][i] for i in range(4))==1
        assert mm(H,J)==scale(a+b,J) and mm(H3,J)==scale(3*a+b,J)
        assert mm(Hsym,J)==scale(3*(a+b),J)
        joints[a,b]=J
    assert add(add(joints[0,0],joints[0,1]),add(joints[1,0],joints[1,1]))==I
    for a,b in product(joints,repeat=2):
        if a!=b:assert mm(joints[a],joints[b])==Z
    def sector(P,z):
        delta=zadd(z,zscale(ONE,-1))
        return tuple(tuple(zadd((I[i][j],F(0)),zscale(delta,P[i][j])) for j in range(4)) for i in range(4))
    def E(z,w,branch=1,right_branch=1):return cmm(sector(PL,power(z,branch)),sector(PR,power(w,right_branch)))
    roots=[power((F(1,2),F(-1,2)),k) for k in range(6)]
    ci=cm(I);CH=cm(H);seed=(ONE,ZERO,ZERO,ZERO)
    unitary_controls=0
    for z,w in product(roots,repeat=2):
        U=E(z,w)
        assert cmm(adj(U),U)==ci
        assert cmm(sector(PL,z),sector(PR,w))==cmm(sector(PR,w),sector(PL,z))
        assert E(zconj(z),zconj(w))==adj(U)
        assert cmm(CH,U)==cmm(U,CH)
        state=mv(U,seed)
        assert zsum(zmul(zconj(x),y) for x,y in zip(state,mv(CH,state)))==ONE
        for P in (PL,PR):
            assert cmm(sector(P,z),sector(P,w))==sector(P,zmul(z,w))
        unitary_controls+=1
    minus_one=zscale(ONE,-1)
    assert E(minus_one,ONE)==cm(L) and E(ONE,minus_one)==cm(R)
    assert E(minus_one,minus_one)==cm(mm(R,L))
    # Positive self-adjoint alternative logarithm: same source corners,
    # different intermediate probability. Endpoint data do not select H.
    for z,w in product((ONE,minus_one),repeat=2):
        assert E(z,w,3)==E(z,w) and E(z,w,3,3)==E(z,w)
    # Stronger rival also respects interchange of the identical source axes.
    swap=tuple(tuple(F(i==((j%2)*2+j//2)) for j in range(4)) for i in range(4))
    assert mm(swap,H)==mm(H,swap) and mm(swap,Hsym)==mm(Hsym,swap)
    z=roots[1]
    prob1=znorm(mv(E(z,ONE),seed)[0]);prob3=znorm(mv(E(z,ONE,3,3),seed)[0])
    assert prob1==F(3,4) and prob3==0
    # Standard real canonical form on Re(psi), Im(psi).
    Omega=block(Z,I,scale(-1,I),Z)
    Hessian=block(H,Z,Z,H)
    K=block(Z,H,scale(-1,H),Z)
    assert scale(-1,mm(Omega,K))==Hessian
    assert add(mm(transpose(K),Omega),mm(Omega,K))==scale(0,eye(8))
    # The source reflects BOTH square coordinates. Starting at its forward
    # corner, reflection and positive continuation share endpoints, not paths.
    reflected=mv(E(zscale(zconj(z),-1),zscale(zconj(z),-1)),seed)
    continued=mv(E(zscale(z,-1),zscale(z,-1)),seed)
    path_residual=norm(minus(reflected,continued))
    assert path_residual==F(9,4)
    state=mv(E(z,z),seed)
    # i*velocity is H psi forward and -H psi on the reflected leg. A bare
    # autonomous vector field cannot assign both to the same visited state.
    tangent_residual=norm(tuple(zscale(v,2) for v in mv(CH,state)))
    assert tangent_residual==6
    uniform=(ONE,)*4
    assert mv(CH,uniform)==(ZERO,)*4
    result=dict(schema='marici.nima.native-square-controlled-hamiltonian.v1',status='pass',
        classification='conditional controlled Hamiltonian realization of a checked finite WG square',
        H0=[[str(x) for x in r] for r in H],spectrum=[0,1,1,2],
        gates='L and R are the actual source bit flips; P_L=(I-L)/2, P_R=(I-R)/2',
        forward_generator='H0=P_L+P_R; i dpsi/dtheta=H0 psi',
        arbitrary_path_generator='H(s)=a_prime(s)*P_L+b_prime(s)*P_R',
        real_Hamiltonian='E(q,p)=(q^T H0 q+p^T H0 p)/2 with standard canonical symplectic form',
        exact_phase_grid_controls=unitary_controls,
        source_corners_verified=True,self_adjoint=True,canonical_symplectic_identity=True,
        stronger_logarithm_rival='3*H0 is positive, axis-interchange symmetric and has the same source corners, but spectrum 0,3,3,6.',
        hostile_residuals={'wrong_positive_continuation_squared_distance':str(path_residual),
                          'same_state_opposite_leg_i_velocity_squared_difference':str(tangent_residual),
                          'same_corners_alternative_logarithm_probabilities':[str(prob1),str(prob3)]},
        disposition='Hamiltonian realization exists after complex linearization and exponential enlargement. IF reflected return is executed as a second positive-parameter leg, it needs leg-aware control: an autonomous vector field on bare psi cannot trace both legs. An inverse comparison with reversed parameter needs no such claim. Source endpoints do not select a unique logarithm.',
        scope='Dimensionless finite-source realization, not a physical energy, autonomous tick generator, 12-mode excitation or derived charge/mass law.')
    (ROOT/'results/native-square-controlled-hamiltonian.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    # Reuse the checked source algebra without reconstructing a weaker model.
    return dict(I=I, L=L, R=R, PL=PL, PR=PR, joints=joints,
                E=E, roots=tuple(roots), swap=swap, result=result)

if __name__=='__main__':main()
