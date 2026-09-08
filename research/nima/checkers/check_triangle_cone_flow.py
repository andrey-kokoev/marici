"""Exact interval-flow decomposition of the seven-point triangle cone."""
import json
from pathlib import Path
from itertools import combinations
from sympy import Matrix,Rational
p=json.loads(Path('research/nima/results/seven_point_fibers.json').read_text());assert p['status']=='passed'
n=7;Q=list(combinations(range(n),3));bd={tuple(sorted((i,(i+1)%n))) for i in range(n)}
T=[set(tuple(e) for e in t) for t in p['triangulations']]
B=Matrix([[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T])
D=sorted(set().union(*T))
H=Matrix([[int((i,k)==e)-int((i,j)==e)-int((j,k)==e) for i,j,k in Q] for e in D])
assert H*B.T==Matrix.zeros(14,42) and H.rank()==14 and B.rank()==21
v=B.T*Matrix([Rational(i+1,43) for i in range(42)])
original=v.copy();terms=[]
def choose(i,k):
    if k==i+1:return []
    j=next(j for j in range(i+1,k) if v[Q.index((i,j,k))]>0)
    return [(i,j,k)]+choose(i,j)+choose(j,k)
while any(v):
    assert all(x>=0 for x in v) and H*v==Matrix.zeros(14,1)
    fs=choose(0,n-1);ids=[Q.index(q) for q in fs]
    delta=min(v[i] for i in ids)
    assert delta>0 and len(ids)==n-2
    row=Matrix([int(i in ids) for i in range(35)])
    assert list(row) in [list(B[i,:]) for i in range(42)]
    for i in ids:v[i]-=delta
    terms.append((delta,row))
    assert len(terms)<=35
assert sum((a*r for a,r in terms),Matrix.zeros(35,1))==original
bad=Matrix.zeros(35,1);bad[Q.index((0,1,3))]=1
assert H*bad!=Matrix.zeros(14,1)
result={'status':'passed','balance_rank':14,'incidence_rank':21,'decomposition_terms':len(terms),'reconstruction_exact':True,'unbalanced_control_rejected':True,'scope':'Seven-point rank and rational decomposition checks; generic acyclic interval proof establishes cone equality, not positive sampling.'}
Path('research/nima/results/triangle_cone_flow.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
