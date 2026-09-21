"""Fixed-capacity failure and event-graded typed bar descent, exact arithmetic."""
from itertools import product
from pathlib import Path
import json
import sympy as s

def words(n):return [w for r in range(n+1) for w in product(range(2),repeat=r)]
N=2;vertices=(2,4,6,12)
a=(s.Integer(1),s.Integer(0));b=(s.Integer(0),s.Integer(1));c=(s.Integer(1),s.I)
def plus(u,v):return tuple(x+y for x,y in zip(u,v))
base_edges=[(2,4,a),(4,12,plus(b,c)),(2,6,plus(a,b)),(6,12,c)]
edges=[(x,y,mark,g) for x,y,g in base_edges for mark in (0,1)]

# A Rees homogeneous piece of event length n has word basis of retained length <= n.
# Forgotten event t raises event length and leaves the word unchanged.
def action(word,mark,g,left=False):
    if not mark:return {word:s.Integer(1)}
    return {(j,)+word if left else word+(j,):g[j] for j in range(2) if g[j]!=0}

B0=[(x,k,u,v) for x in vertices for k in range(N+1) for u in words(k) for v in words(N-k)]
B1=[(ei,k,u,v) for ei in range(len(edges)) for k in range(N) for u in words(k) for v in words(N-1-k)]
i0={x:i for i,x in enumerate(B0)};out=words(N);io={w:i for i,w in enumerate(out)}
d=s.zeros(len(B0),len(B1))
for j,(ei,k,u,v) in enumerate(B1):
    x,y,mark,g=edges[ei]
    for word,z in action(u,mark,g).items():d[i0[y,k+1,word,v],j]+=z
    for word,z in action(v,mark,g,left=True).items():d[i0[x,k,u,word],j]-=z
mu=s.zeros(len(out),len(B0))
for j,(x,k,u,v) in enumerate(B0):mu[io[u+v],j]=1
assert (mu*d).applyfunc(s.simplify)==s.zeros(len(out),len(B1))

# Prescribed signed record forms; t has no feature-degree weight.
tau=s.Integer(2)
weight=lambda w:tau**(2*len(w))*(-1)**sum(w)
Q0=s.diag(*[weight(u+v) for _,_,u,v in B0]);Qout=s.diag(*[weight(w) for w in out])
sharp=Q0.inv()*mu.H*Qout
assert sharp==mu.T
assert (d.H*Q0*sharp).applyfunc(s.simplify)==s.zeros(len(B1),len(out))
# Thus the mate lands in the annihilator of boundary relations, not an arbitrary
# inverse image or an assumed nondegenerate quotient metric.

# Fixed cap a=b=1 is NOT balanced for the same right/left creation.
u=(0,);v=();g=a
right_truncated={w:z for w,z in action(u,1,g).items() if len(w)<=1}
left_truncated={w:z for w,z in action(v,1,g,left=True).items() if len(w)<=1}
assert not right_truncated and {u+w:z for w,z in left_truncated.items()}=={(0,0):1}

# Polarity supplies left creation: reverse(conjugate(right_g(word))) equals
# left_conjugate(g)(reverse(conjugate(word))) on these real word bases.
for n in range(3):
    for w in words(n):
        lhs={z[::-1]:s.conjugate(k) for z,k in action(w,1,c).items()}
        rhs=action(w[::-1],1,tuple(s.conjugate(z) for z in c),left=True)
        assert lhs==rhs

# Ordinary balanced coefficient quotient for the full Rees algebra, degree two.
# Its generators are central t and two feature letters. These relations compute
# H0 only; this is NOT claimed to be a two-term projective resolution of Rees.
C0=[(k,u,v) for k in range(N+1) for u in words(k) for v in words(N-k)]
C1=[(gen,k,u,v) for gen in (-1,0,1) for k in range(N) for u in words(k) for v in words(N-1-k)]
ici={x:i for i,x in enumerate(C0)}
rel=s.zeros(len(C0),len(C1));mul=s.zeros(len(out),len(C0))
for j,(gen,k,u,v) in enumerate(C1):
    r=u if gen==-1 else u+(gen,)
    l=v if gen==-1 else (gen,)+v
    rel[ici[k+1,r,v],j]+=1;rel[ici[k,u,l],j]-=1
for j,(_,u,v) in enumerate(C0):mul[io[u+v],j]=1
assert mul*rel==s.zeros(len(out),len(C1))
assert len(C0)-rel.rank()==len(out)==mul.rank()
rank=d.rank()
result={'schema':'marici.grothendieck.typed-balanced-composition.v1','passed':True,
        'event_length':N,'source_vertices':list(vertices),'marked_arrows':len(edges),
        'typed_bar_dimensions':{'degree_minus_one':len(B1),'degree_zero':len(B0),'target':len(out)},
        'typed_bar_homology_dimensions':{'H_minus_one':len(B1)-rank,'H_zero':len(B0)-rank},
        'checks':{'fixed_capacity_balancing_fails':True,
                  'polarity_induced_left_creation':True,
                  'event_graded_typed_bar_chain_map':True,
                  'signed_mate_annihilates_bar_boundaries':True,
                  'regular_rees_balanced_quotient_H0':True},
        'scope':'Free marked quiver admits the stated two-term source resolution. Rees coefficient quotient check concerns H0 only. No nondegenerate quotient form or topological completion is inferred.'}
p=Path(__file__).resolve().parents[1]/'results/typed-balanced-composition.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
