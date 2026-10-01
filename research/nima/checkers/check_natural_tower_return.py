"""Test which parts of the proposed six-packet tower return are intrinsic.

Retained regrouping, spectral reconstruction, raw incidence evolution and
spectral phase extraction are kept as distinct operations. No rung clock fit.
"""
from fractions import Fraction as F
from pathlib import Path
import json

LABELS='ABCD'
PACKETS=(('AB','A','B'),('BC','B','C'),('CA','C','A'),
         ('BA','B','A'),('AD','A','D'),('DB','D','B'))
N=4
I=tuple(tuple(F(i==j) for j in range(N)) for i in range(N))
Z=tuple(tuple(F(0) for _ in range(N)) for _ in range(N))

def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in r) for r in a)
def sub(a,b): return add(a,scale(b,-1))
def transpose(a): return tuple(zip(*a))
def mm(a,b): return tuple(tuple(sum((x*y for x,y in zip(r,c)),F(0)) for c in transpose(b)) for r in a)
def power(a,n):
    out=I
    for _ in range(n): out=mm(a,out)
    return out

def incidence(packets):
    result=[[F(0)]*4 for _ in range(4)]
    for occurrence,source,target in packets:
        result[LABELS.index(target)][LABELS.index(source)]+=1
    return tuple(tuple(r) for r in result)

def group(packets,index):
    return tuple((key,tuple(p for p in packets if p[index]==key)) for key in LABELS)
def unpack(groups): return tuple(p for _,members in groups for p in members)

def rmul(x,y,d):
    # Matrices in Q(sqrt(d)): x=x0+sqrt(d)*x1; also handles d=-3.
    return (add(mm(x[0],y[0]),scale(mm(x[1],y[1]),d)),
            add(mm(x[0],y[1]),mm(x[1],y[0])))
def radd(x,y): return (add(x[0],y[0]),add(x[1],y[1]))
def rscale(x,a,b,d): return (add(scale(x[0],a),scale(x[1],d*b)),add(scale(x[0],b),scale(x[1],a)))
def rtranspose(x): return tuple(transpose(a) for a in x)

def main():
    M=incidence(PACKETS)
    expected=((0,1,1,0),(1,0,0,1),(0,1,0,0),(1,0,0,0))
    assert M==expected
    # All retained source/target presentations give the same operator and spectrum.
    p=PACKETS;presentations=[]
    for n in range(1,10):
        outgoing=group(p,1);incoming=group(unpack(outgoing),2)
        p=unpack(incoming)
        assert incidence(p)==M and set(p)==set(PACKETS) and len(p)==6
        presentations.append({'round':n,'incidence_unchanged':True,'primitive_occurrences':len(p)})
    assert tuple(sorted(p,key=lambda p:next(i for i,q in enumerate(PACKETS) if q[0]==p[0])))==PACKETS
    # The exchange of the two triangle roles splits real/complex spectral sectors.
    R=tuple(tuple(F(j==(1,0,3,2)[i]) for j in range(N)) for i in range(N))
    Pe=scale(add(I,R),F(1,2));Po=scale(sub(I,R),F(1,2))
    K=mm(sub(scale(M,2),I),Pe)
    L=mm(add(scale(M,2),I),Po)
    assert mm(Pe,Po)==Z and mm(K,K)==scale(Pe,5) and mm(L,L)==scale(Po,-3)
    # Real projectors P_phi/P_psi and complex projectors P_omega/P_conj.
    real_projectors=[];complex_projectors=[];retained_modes=[]
    real_sum=(Z,Z);complex_sum=(Z,Z)
    for sign in (1,-1):
        P_real=(scale(Pe,F(1,2)),scale(K,F(sign,10)))
        P_complex=(scale(Po,F(1,2)),scale(L,F(-sign,6)))
        assert rmul(P_real,P_real,5)==P_real
        assert rmul(P_complex,P_complex,-3)==P_complex
        assert sum(P_real[0][i][i] for i in range(4))==1
        assert sum(P_complex[0][i][i] for i in range(4))==1
        assert rmul((M,Z),P_real,5)==rscale(P_real,F(1,2),F(sign,2),5)
        assert rmul((M,Z),P_complex,-3)==rscale(P_complex,F(-1,2),F(sign,2),-3)
        real_sum=radd(real_sum,rscale(P_real,F(1,2),F(sign,2),5))
        complex_sum=radd(complex_sum,rscale(P_complex,F(-1,2),F(sign,2),-3))
        real_projectors.append(P_real);complex_projectors.append(P_complex)
        retained_modes.append((5,(F(1,2),F(sign,2)),P_real))
        retained_modes.append((-3,(F(-1,2),F(sign,2)),P_complex))
    assert real_sum[1]==complex_sum[1]==Z
    synthesized=add(real_sum[0],complex_sum[0]);assert synthesized==M
    assert rmul(real_projectors[0],real_projectors[1],5)==(Z,Z)
    assert rmul(complex_projectors[0],complex_projectors[1],-3)==(Z,Z)
    # Projectors commute with M, hence conjugation transports no new phase into them.
    for P,d in [(p,5) for p in real_projectors]+[(p,-3) for p in complex_projectors]:
        assert rmul((M,Z),P,d)==rmul(P,(M,Z),d)
    # Spectral phase operator: replace each eigenvalue by lambda/abs(lambda).
    # U acts as +1 on phi, -1 on psi, and omega/conj on the complex pair.
    U=(mm(M,Po),scale(K,F(1,5))) # Q(sqrt(5)) matrix.
    # Positive spectral modulus. This is a spectral split, not Euclidean polar decomposition.
    A=(Po,add(scale(Pe,F(1,2)),scale(K,F(1,10))))
    assert rmul(U,A,5)==(M,Z) and rmul(A,U,5)==(M,Z)
    assert rmul(rtranspose(U),U,5)!=(I,Z) # M is nonnormal in the counting metric.
    up=(I,Z);powers=[]
    for n in range(1,10):
        up=rmul(U,up,5)
        all_return=up==(I,Z)
        assert all_return==(n%6==0)
        if n in (3,9): assert up==(Po,scale(K,F(1,5)))
        assert power(M,n)!=I
        # Reconstruction uses retained spectral descriptors and works at every step.
        assert synthesized==incidence(PACKETS)
        powers.append({'step':n,'complex_mode_phase':f'omega^{n%3}',
                       'phi_phase':1,'psi_phase':(-1)**n,
                       'complex_pair_returns':n%3==0,'all_spectral_phases_return':all_return,
                       'raw_incidence_returns':False,'spectral_decode_available':True})
    assert power(M,3)!=I and power(M,6)!=I and power(M,9)!=I
    report={'status':'passed','primitive_packets':[p[0] for p in PACKETS],
            'eigenvalues':['(1+sqrt(5))/2','(1-sqrt(5))/2','(-1+i*sqrt(3))/2','(-1-i*sqrt(3))/2'],
            'regrouping_tests':presentations,'operator_steps':powers,
            'spectral_phase_operator':'U=(M P_odd)+(2M-I)P_even/sqrt(5)',
            'spectral_phase_period':6,'phase_only_is_counting_metric_orthogonal':False,
            'synthesis':'sum lambda P_lambda = M, available without waiting for a phase gate',
            'outcome':'Regrouping preserves the operator; spectral identities are fixed. The complex-only 3-step gate omits the negative real mode. No rung placement follows from these maps.',
            'scope':'Exact naturality audit, not an added clock or physical evolution rule.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'natural-tower-return.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: exact six-arrow reconstruction; regrouping advances no phase; raw M has no finite return; full spectral phase returns in 6 steps, complex pair in 3.')
    return {'modes':tuple(retained_modes),'packets':PACKETS,'matrix':M}

if __name__=='__main__': main()
