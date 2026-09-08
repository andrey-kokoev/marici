"""Exact Laurent section on a four-generator boundary face."""
import json
from pathlib import Path
from itertools import combinations
from sympy import Matrix,eye,zeros
r=Path('research/nima/results');p=json.loads((r/'seven_point_fibers.json').read_text());g=json.loads((r/'seven_groebner.json').read_text())
assert p['status']=='passed' and g['status']=='complete'
Q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
T=[set(tuple(e) for e in t) for t in p['triangulations']]
B=Matrix([[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T])
for a,b in g['basis']:
    S=[i for i in range(42) if a[i] or b[i]]
    if len(S)!=4:continue
    U=[j for j in range(35) if any(B[i,j] for i in S)]
    if [i for i in range(42) if all(not B[i,j] or j in U for j in range(35))]!=S:continue
    M=B.extract(S,U)
    if M.rank()==3:break
else:raise AssertionError('No four-generator face')
rows=list(M.T.rref()[1]);A=M.extract(rows,range(len(U)))
for cols in combinations(range(len(U)),3):
    K=A.extract(range(3),cols)
    if abs(K.det())==1:break
else:raise AssertionError('No unimodular coordinate minor')
D=zeros(len(U),3)
for i,j in enumerate(cols):
    for k in range(3):D[j,k]=K.inv()[i,k]
assert A*D==eye(3)
C=M*D;assert C*A==M
assert all(v.q==1 for v in D) and all(v.q==1 for v in C)
bad=D.copy();bad[cols[0],0]+=1
assert A*bad!=eye(3)
out={'status':'passed','support_indices':S,'triangle_indices':U,'triangle_labels':[Q[j] for j in U],'independent_coefficient_indices':[S[i] for i in rows],'triangle_Laurent_exponents':[[int(v) for v in D.row(i)] for i in range(D.rows)],'coefficient_Laurent_exponents':[[int(v) for v in C.row(i)] for i in range(C.rows)],'kernel_torus_dimension':len(U)-3,'corrupted_section_rejected':True,'scope':'Coordinates outside U are zero. Independent coefficient values are nonzero; D defines section and C reconstructs supported coefficients exactly.'}
(r/'stratum_section.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
