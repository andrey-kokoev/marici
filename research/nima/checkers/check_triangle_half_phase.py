"""Three composable two-endpoint packets -> cyclic plane -> half-phase lift.

Exact rational matrices and Q(i*sqrt(3)) eigenpairs. No fourth identity packet,
physical angle fitting, spatial normal, mass value or external dependency.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

@dataclass(frozen=True)
class TwoPacket:
    label: str
    source: str
    target: str


def transpose(a): return tuple(zip(*a))
def mm(a,b):
    return tuple(tuple(sum((x*y for x,y in zip(row,col)),F(0)) for col in transpose(b)) for row in a)
def mv(a,v): return tuple(sum((x*y for x,y in zip(row,v)),F(0)) for row in a)
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in row) for row in a)
def sub(a,b): return add(a,scale(b,-1))
def power(a,n):
    out=I
    for _ in range(n): out=mm(a,out)
    return out

def norm2(v): return sum(x*x for x in v)
def trace(a): return sum(a[i][i] for i in range(3))
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
ZERO=scale(I,F(0))

def cycle_from_packets(packets):
    if len(packets)!=3 or len({p.label for p in packets})!=3:
        raise ValueError('Three distinct packet occurrences required')
    if len({p.source for p in packets})!=3 or any(p.source==p.target for p in packets):
        raise ValueError('Three distinct triangle vertices required')
    if any(packets[i].target!=packets[(i+1)%3].source for i in range(3)):
        raise ValueError('Consecutive packets must compose and close')
    return tuple(tuple(F(a.target==b.source) for b in packets) for a in packets)

# z=a+i*sqrt(3)*b, represented by two rationals.
def zadd(x,y): return (x[0]+y[0],x[1]+y[1])
def zmul(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zscale(x,a): return (a*x[0],a*x[1])
def zconj(x): return (x[0],-x[1])
def znorm(x): return x[0]**2+3*x[1]**2

def zmm(a,b):
    out=[]
    for row in a:
        values=[]
        for col in transpose(b):
            value=(F(0),F(0))
            for x,y in zip(row,col): value=zadd(value,zmul(x,y))
            values.append(value)
        out.append(tuple(values))
    return tuple(out)

def zmscale(a,c): return tuple(tuple(zmul(x,c) for x in row) for row in a)
def zreal(a): return tuple(tuple((x,F(0)) for x in row) for row in a)

def zmv(a,v):
    out=[]
    for row in a:
        value=(F(0),F(0))
        for weight,z in zip(row,v): value=zadd(value,zscale(z,weight))
        out.append(value)
    return tuple(out)

def rejects(fn):
    try: fn()
    except ValueError: return
    raise AssertionError('Malformed primitive admitted')

def main():
    packets=(TwoPacket('p01','0','1'),TwoPacket('p12','1','2'),TwoPacket('p20','2','0'))
    C=cycle_from_packets(packets);Ct=transpose(C)
    assert mm(Ct,C)==I and power(C,3)==I
    Q=scale(add(add(I,C),mm(C,C)),F(1,3))
    P=sub(I,Q);A=sub(C,Ct)
    assert Q==tuple(tuple(F(1,3) for _ in range(3)) for _ in range(3))
    assert mm(Q,Q)==Q and mm(P,P)==P and mm(Q,P)==ZERO
    assert trace(Q)==1 and trace(P)==2
    assert mm(C,Q)==Q and mv(Q,(F(1),F(1),F(1)))==(1,1,1)
    assert transpose(A)==scale(A,-1) and mm(A,A)==scale(P,-3)
    assert mm(A,Q)==ZERO and mm(transpose(A),A)==scale(P,3)
    # J=A/sqrt(3): J²=-P, the intrinsic contrast-plane identity is -J².
    S=add(add(Q,scale(P,F(1,2))),scale(A,F(1,2)))
    alternative=mm(C,C)
    assert mm(S,S)==C and mm(transpose(S),S)==I and mm(S,Q)==Q
    assert mm(alternative,alternative)==C
    assert add(S,transpose(S))==add(scale(Q,2),P)
    assert add(alternative,transpose(alternative))==sub(scale(Q,2),P)
    assert power(S,3)==sub(Q,P) and power(S,6)==I
    assert all(power(S,k)!=I for k in range(1,6))
    assert power(alternative,3)==I
    # Both C and its half-lift have the same complex eigendirections.
    one=(F(1),F(0));omega=(F(-1,2),F(1,2));half=(F(1,2),F(1,2))
    v=(one,omega,zmul(omega,omega))
    assert zmul(omega,zmul(omega,omega))==one and zmul(half,half)==omega
    for eigenvector,eigenvalue,liftvalue in [(v,omega,half),(tuple(map(zconj,v)),zconj(omega),zconj(half))]:
        assert zmv(C,eigenvector)==tuple(zmul(eigenvalue,z) for z in eigenvector)
        assert zmv(S,eigenvector)==tuple(zmul(liftvalue,z) for z in eigenvector)
        half_vector=tuple(zscale(z,F(1,2)) for z in eigenvector)
        assert zmv(C,half_vector)==tuple(zmul(eigenvalue,z) for z in half_vector)
        assert sum(znorm(z) for z in half_vector)==F(1,4)*sum(znorm(z) for z in eigenvector)
    # The literal factor 1/2 also occurs in spectral identity projectors,
    # not in an arbitrarily rescaled eigenvector: E+ = (P-iJ)/2.
    Eplus=tuple(tuple((P[i][j]/2,-A[i][j]/6) for j in range(3)) for i in range(3))
    Eminus=tuple(tuple(zconj(z) for z in row) for row in Eplus)
    for E,lam,h in ((Eplus,omega,half),(Eminus,zconj(omega),zconj(half))):
        assert zmm(E,E)==E
        assert tuple(tuple(zconj(z) for z in row) for row in transpose(E))==E
        assert zmm(zreal(C),E)==zmscale(E,lam)
        assert zmm(zreal(S),E)==zmscale(E,h)
        assert sum(E[i][i][0] for i in range(3))==1
        assert sum(E[i][i][1] for i in range(3))==0
    assert zmm(Eplus,Eminus)==zreal(ZERO)
    assert tuple(tuple(zadd(a,b) for a,b in zip(r,s)) for r,s in zip(Eplus,Eminus))==zreal(P)
    # No distinguished starting vertex: cyclic relabellings commute; reversals conjugate.
    for perm in permutations(range(3)):
        B=tuple(tuple(F(j==perm[i]) for j in range(3)) for i in range(3))
        Cp=mm(mm(B,C),transpose(B));Sp=mm(mm(B,S),transpose(B))
        assert Cp in (C,Ct)
        assert Sp==(S if Cp==C else transpose(S))
    renamed=tuple(TwoPacket(p.label,'v'+p.source,'v'+p.target) for p in packets)
    assert cycle_from_packets(renamed)==C
    rejects(lambda:cycle_from_packets(packets[:2]))
    rejects(lambda:cycle_from_packets((packets[0],packets[0],packets[2])))
    rejects(lambda:cycle_from_packets((packets[0],packets[2],packets[1])))
    rejects(lambda:cycle_from_packets((packets[0],packets[1],TwoPacket('bad','2','x'))))
    # Important correction: arity doubling is NOT six-step traversal.
    squaring=[]
    for depth in range(9):
        arity=2**depth
        residual=arity%6
        value=power(S,residual)
        assert value!=I
        squaring.append({'depth':depth,'arity':arity,'lift_exponent_mod_6':residual})
    assert power(S,4)==mm(C,C) and power(S,8)==C
    # The +/- ambiguity cannot be eliminated by the equation S²=C alone.
    assert alternative!=S and mm(alternative,alternative)==mm(S,S)
    # Rank-one common mode is derived, but no absolute amplitude is selected.
    for amplitude in (F(0),F(1,2),F(1),F(7)):
        common=(amplitude,)*3
        assert mv(C,common)==common and mv(S,common)==common
    report={'status':'passed','primitive':[p.__dict__ for p in packets],
            'cycle_matrix':[[str(v) for v in row] for row in C],
            'common_projector':[[str(v) for v in row] for row in Q],
            'plane_projector':[[str(v) for v in row] for row in P],
            'half_phase_matrix':[[str(v) for v in row] for row in S],
            'complex_structure':'J=(C-C^T)/sqrt(3); J²=-P',
            'complex_eigenline_identities':'E±=(P∓iJ)/2; E±²=E±; E+E-=0; E++E-=P',
            'eigenvalues':['1','-1/2+i*sqrt(3)/2','-1/2-i*sqrt(3)/2'],
            'half_phase_eigenvalues':['1','1/2+i*sqrt(3)/2','1/2-i*sqrt(3)/2'],
            'root_selection':'fix common mode; choose root with positive symmetric part (short half-angle)',
            'other_orthogonal_root':'C², fixing common mode but taking the long branch',
            'cycle_and_lift_return':'C³=I, S³=Q-P, S⁶=I',
            'doubling':squaring,
            'scope':'Triangle coefficient-plane structure; no fourth identity packet, physical spatial axis, proton, or native promotion bridge derived.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'triangle-half-phase.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: triangle-derived common/complex plane, eigenpairs and half-weight eigenprojectors, 60-degree short root, three/six-step returns, and no arity-four squaring closure.')

if __name__=='__main__': main()
