"""Integral section of the six-point quotient, with a nonfaithful control."""
import json
from pathlib import Path
from itertools import combinations
from sympy import Matrix, Integer, prod
p=json.loads(Path('research/nima/results/local_global_torus_lattice.json').read_text())
assert p['status']=='passed' and p['combined_index_in_saturation']==1
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
qs=list(combinations(range(6),3))
boundary={tuple(sorted((i,(i+1)%6))) for i in range(6)}
B=Matrix([[int(all(e in t|boundary for e in combinations(q,2))) for q in qs] for t in T])
D=Matrix(p['complement']);M=D*B
pair=next(c for c in combinations(range(20),2) if abs(M[:,list(c)].det())==1)
E=Matrix.zeros(20,2)
inv=M[:,list(pair)].inv()
for i,c in enumerate(pair):
    for j in range(2):E[c,j]=inv[i,j]
S=B*E
assert D*S==Matrix.eye(2)
channels=sorted(set().union(*T))
A=Matrix([[int(c in t) for c in channels] for t in T])
assert D*A==Matrix.zeros(2,9)
def section(a,b):return [Integer(a)**int(S[i,0])*Integer(b)**int(S[i,1]) for i in range(14)]
def coord(w):return [prod(w[i]**int(D[j,i]) for i in range(14)) for j in range(2)]
w=section(2,3)
assert coord(w)==[2,3]
scales=list(map(Integer,range(2,11)))
shift=[w[i]*prod(scales[j]**int(A[i,j]) for j in range(9)) for i in range(14)]
assert coord(shift)==[2,3] and shift!=w
v=section(-2,3)
assert coord(v)==[-2,3]
assert [coord(w)[0]**2,coord(w)[1]]==[coord(v)[0]**2,coord(v)[1]]
result={'status':'passed','triangles':[qs[i] for i in pair],'triangle_section_exponents':[[int(x) for x in row] for row in inv.tolist()],'weight_section_exponents':[[int(x) for x in row] for row in S.tolist()],'section_coordinates':[2,3],'channel_shift_preserves_coordinates':True,'nonprimitive_collision':[[2,3],[-2,3]],'scope':'D S = identity is an integral monomial section certificate. Squaring the first character loses a mu_2 distinction.'}
Path('research/nima/results/quotient_section.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
