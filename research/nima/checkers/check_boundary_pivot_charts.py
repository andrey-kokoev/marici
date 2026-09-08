import json
from pathlib import Path
from itertools import combinations,product
from sympy import symbols,Matrix,simplify
R=Path('research/nima/results');p=json.loads((R/'seven_point_fibers.json').read_text());s=json.loads((R/'stratum_section.json').read_text())
assert p['status']=='passed' and s['status']=='passed'
Q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
T=[set(tuple(e) for e in t) for t in p['triangulations']]
B=Matrix([[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T]);S=s['support_indices'];U=s['triangle_indices'];M=B.extract(S,U)
patterns=[(1,1,0,0),(0,0,1,1),(1,0,1,0),(0,1,0,1)]
cols=[next(j for j in range(len(U)) if tuple(M[:,j])==pat) for pat in patterns]
u0,u1,v0,v1=symbols('u0 u1 v0 v1');W=Matrix([u0,u1])*Matrix([[v0,v1]])
charts={}
for a,b in product(range(2),repeat=2):
    rr=W[:,b];cc=W[a,:]/W[a,b]
    assert (rr*cc-W).applyfunc(simplify)==Matrix.zeros(2)
    charts[a,b]=(rr,cc)
for (a,b),(c,d) in combinations(charts,2):
    rr,cc=charts[a,b];ss,tt=charts[c,d];lam=W[a,d]/W[a,b]
    assert (ss-lam*rr).applyfunc(simplify)==Matrix.zeros(2,1)
    assert (tt-cc/lam).applyfunc(simplify)==Matrix.zeros(1,2)
# At the zero matrix, h*r*c has derivative rank <=2 by cases in the packet.
# Deliberate failure: unit row and column factors do not map to the vertex.
assert W.subs({u0:1,u1:1,v0:1,v1:1})!=Matrix.zeros(2)
result={'status':'passed','support':S,'row_factor_triangles':[Q[U[j]] for j in cols[:2]],'column_factor_triangles':[Q[U[j]] for j in cols[2:]],'charts':4,'pairwise_transitions':6,'scope':'Exact rank-one pivot identities; packet supplies zero-fiber derivative case proof. Other used triangles set to one, unused to zero.'}
(R/'boundary_pivot_charts.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
