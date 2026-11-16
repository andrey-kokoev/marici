#!/usr/bin/env python3
"""Exact source-symmetry and conditional green criterion audit.
Inputs: six directed occurrence labels from ActualSeedEndpointTable.agda.
No new primitive relations or operational effects are inferred from the source.
"""
from itertools import permutations
from fractions import Fraction as Q
from collections import Counter

VERTICES=('A','B','C','D')
EDGES={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),
       'AD':('A','D'),'DB':('D','B'),'BA':('B','A')}
INV={pair:k for k,pair in EDGES.items()}
R=('AB','BC','CA')
B=('AD','DB','BA')
p=('AB',)
q=('AD','DB')


def classify(contravariant):
    out=[]
    for tup in permutations(VERTICES):
        f=dict(zip(VERTICES,tup))
        m={}
        for edge,(s,t) in EDGES.items():
            pair=(f[t],f[s]) if contravariant else (f[s],f[t])
            if pair not in INV: break
            m[edge]=INV[pair]
        if len(m)==len(EDGES):
            assert len(set(m.values()))==len(EDGES)
            out.append((f,m))
    return out

def trans(word,m,contra):
    word=word[::-1] if contra else word
    return tuple(m[e] for e in word)

cov=classify(False)
anti=classify(True)
assert len(cov)==len(anti)==2
# The full 4-element symmetry set has parity covariant/contravariant;
# composition of two contravariant maps is covariant. Verify closure.
for fc,mc in cov+anti:
    for fd,md in cov+anti:
        fg={v:fc[fd[v]] for v in VERTICES}
        mg={e:mc[md[e]] for e in EDGES}
        assert any(fg==f and mg==m for f,m in cov+anti)

assert all(all(f[f[x]]==x for x in f) and all(m[m[e]]==e for e in m) for f,m in cov+anti)
assert set(tuple(sorted(f.items())) for f,m in anti)=={
    (('A','A'),('B','B'),('C','D'),('D','C')),
    (('A','B'),('B','A'),('C','C'),('D','D'))}

# The A,B-fixed anti-involution exchanges red and blue, and the green questions.
tau_f,tau=next((f,m) for f,m in anti if f['A']=='A')
assert tau=={'AB':'BA','BA':'AB','BC':'DB','DB':'BC','CA':'AD','AD':'CA'}
assert trans(R,tau,True)==B
assert trans(B,tau,True)==R
assert trans(p,tau,True)==('BA',)
assert trans(q,tau,True)==('BC','CA')

# Directed path category has no identity-object anti-involution.
assert not any(all(f[v]==v for v in VERTICES) for f,m in anti)

# In a groupoid with anti-involution *, assume p *q =1 and q *p=1.
# Then q=(*p)^-1 and green equality p=q iff p *p=1.
# Verify with exact 2x2 rational matrices and transpose adjoint.
I=((Q(1),Q(0)),(Q(0),Q(1)))
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a):return ((a[0][0],a[1][0]),(a[0][1],a[1][1]))
def inv(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det!=0
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))
def norm(a):return mul(a,tr(a))
def effects(a):
    qb=inv(tr(a))
    # f(e)^T=f(tau(e)), ensuring contravariant naturality.
    F={'AB':a,'BA':tr(a),'AD':I,'CA':I,'DB':qb,'BC':tr(qb)}
    assert all(tr(F[e])==F[tau[e]] for e in EDGES)
    def ev(word):
        res=I
        for e in word:res=mul(res,F[e])
        return res
    assert ev(R)==I and ev(B)==I
    assert ev(p)==a and ev(q)==qb
    assert (ev(p)==ev(q))==(norm(a)==I)
    assert (ev(('AB','BA'))==I)==(norm(a)==I)
    return {'a':a,'q':qb,'norm':norm(a),'green':ev(p)==ev(q)}

# Exact examples: shear, diagonal scaling, 90-degree rotation, 120-degree lattice rotation.
cases={
    'nonunitary_shear':((Q(1),Q(1)),(Q(0),Q(1))),
    'nonunitary_scale':((Q(2),Q(0)),(Q(0),Q(1))),
    'orthogonal_quarterturn':((Q(0),Q(-1)),(Q(1),Q(0))),
    'reflection':((Q(1),Q(0)),(Q(0),Q(-1))),
}
results={k:effects(a) for k,a in cases.items()}
assert [results[x]['green'] for x in cases]==[False,False,True,True]

# Unitariy under an anti-involution is stable under arbitrary products.
unitary=[a for a in [cases['orthogonal_quarterturn'],cases['reflection'],I] if norm(a)==I]
assert len(unitary)==3

# Enumerate every invertible 2x2 integer matrix with entries -2..2.
all_small=[]
for v in __import__('itertools').product(range(-2,3), repeat=4):
    a=((Q(v[0]),Q(v[1])),(Q(v[2]),Q(v[3])))
    if v[0]*v[3]-v[1]*v[2]==0:continue
    all_small.append(effects(a))
assert len(all_small)>300
strict_count=sum(z['green'] for z in all_small)
assert strict_count==sum(z['norm']==I for z in all_small)
# Canonical dual (contragredient) action always preserves evaluation,
# including for nonunitary matrices. It cannot select green coherence.
for row in all_small:
    a=row['a']
    dual=tr(inv(a))
    assert mul(tr(dual),a)==I
# A pairing invariant under ALL invertible scalar changes cannot be nonzero:
scale=((Q(2),Q(0)),(Q(0),Q(2)))
assert mul(tr(scale),mul(I,scale))!=I


# The dagger norm is covariant under composition, not a commutator test.
for a in unitary:
    for b in unitary:
        assert norm(mul(a,b))==I

# Norm transport law: N(pq)=p N(q) p^T (rather than the covariant-automorphism
# commutator rule used in Stage 8).
for a in cases.values():
    for b in cases.values():
        assert norm(mul(a,b))==mul(mul(a,norm(b)),tr(a))

# Counting source-derived symmetries/paths.
print('covariant_symmetries',len(cov),'contravariant_symmetries',len(anti))
for i,(f,m) in enumerate(anti):
    print('anti',i,'vertex_map',f,'edge_map',m)
print('tau_red',trans(R,tau,True),'tau_blue',trans(B,tau,True))
for k,x in results.items():print(k,'green',x['green'],'norm',x['norm'],'q',x['q'])
print('exhaustive_integer_matrices',len(all_small),'green_strict',strict_count)
print('PASS: all exact checks')
