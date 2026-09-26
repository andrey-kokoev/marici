"""Finite-set countermodel to unrestricted PS(SP(Q)) = SP(PS(Q)),
and a bijection test for the correctly dependent Pi-Sigma distributivity law.
No higher-type or universal HoTT proof is claimed by this finite enumeration.
"""
from itertools import product
from pathlib import Path
import json
I=(0,1)
def Sigma(X):return tuple((i,x) for i in I for x in X)
def Pi(X):return tuple(product(X,repeat=len(I)))
Q=('q',)
# Preserve the full staged constructions, not just endpoint cardinalities.
left=[Q]
for operation in (Pi,Sigma,Sigma,Pi):left.append(operation(left[-1]))
right=[Q]
for operation in (Sigma,Pi,Pi,Sigma):right.append(operation(right[-1]))
assert [len(x) for x in left]==[1,1,2,4,16]
assert [len(x) for x in right]==[1,2,4,16,32]
assert len(left[-1])!=len(right[-1])
# Dependent choice/distributivity: product_i sum_j B(i,j)
# versus sum_f product_i B(i,f(i)). Vary fibre size with both indices.
def B(i,j):return tuple(range(1+i+j))
source=tuple(product(*(tuple((j,b) for j in I for b in B(i,j)) for i in I)))
target=tuple((f,bs) for f in product(I,repeat=2)
             for bs in product(*(B(i,f[i]) for i in I)))
def forward(g):return tuple(j for j,b in g),tuple(b for j,b in g)
def backward(pair):return tuple(zip(*pair))
assert set(map(forward,source))==set(target)
assert all(backward(forward(g))==g for g in source)
assert all(forward(backward(t))==t for t in target)
report={'passed':True,
 'fixed_index_interpretation':'Sigma_I(X)=sum_(i:I) X; Pi_I(X)=product_(i:I) X',
 'left_staged_cardinalities':[len(x) for x in left],
 'right_staged_cardinalities':[len(x) for x in right],
 'unrestricted_interchange_refuted_in_finite_sets':True,
 'dependent_distributivity_bijection_cases':len(source),
 'scope':'Specific finite countermodel and finite bijection regression; neither refutes all intended meanings of productization nor constructs a higher coherence tower.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/sigma-pi-interchange-typing.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
