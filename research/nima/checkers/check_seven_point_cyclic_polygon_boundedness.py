"""Universal telescoping boundedness certificate for cyclic-positive n=7 fibres."""
import json
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
k=(1,-6,15,-20,15,-6,1)
x=s.symbols('x1:8');y=s.symbols('y1:8');a,b=s.symbols('a b')
def minor(i,j):
 X=lambda l:x[l]+a*k[l];Y=lambda l:y[l]+b*k[l]
 return s.expand(X(i)*Y(j)-X(j)*Y(i))
edges=[(i,i+1) for i in range(6)]+[(0,6)]
weights=[Q(1,-k[i]*k[j]) for i,j in edges[:-1]]+[Q(1,k[0]*k[6])]
assert all(t>0 for t in weights)
L=s.expand(sum(s.Rational(z.numerator,z.denominator)*minor(i,j) for z,(i,j) in zip(weights,edges)))
assert not L.has(a) and not L.has(b)
K=s.expand(sum(s.Rational(z.numerator,z.denominator)*(x[i]*y[j]-x[j]*y[i]) for z,(i,j) in zip(weights,edges)))
assert s.expand(L-K)==0
# Normals are the coefficient vectors in (a,b). A positive cyclic source
# with rank-one normal span is impossible: dividing C_i by alternating k_i
# makes consecutive q_i differences collinear and all six det(q_i,q_i+1)
# negative, while det(q1,q7) must be positive. See accompanying proof.
example={'cyclic_weight_vector':list(map(str,weights)),'weight_sum_identity':'sum lambda_ij Delta_ij(C+[a,b]^T k) = sum lambda_ij Delta_ij(C)',
 'all_variable_coefficients_symbolically_zero':True}
# Deliberate mutation: omitting ANY one positive coefficient destroys
# the universal cancellation, so a sparse false relation is rejected.
for index in range(7):
 changed=s.expand(L-s.Rational(weights[index].numerator,weights[index].denominator)*minor(*edges[index]))
 assert changed.has(a) or changed.has(b)
result={'schema':'marici.nima.seven-point-cyclic-polygon-boundedness.v1','passed':True,
 'edges':[[i+1,j+1] for i,j in edges],'positive_weights':list(map(str,weights)),
 'identity':example,'single-weight-deletion_rejections':7,
 'theorem':'For every source C with all seven ordered cyclic minors strictly positive, its cyclic-only fibre { (a,b): each cyclic minor(C+[a,b]^T k)>=0 } is nonempty and bounded. Positivity of the weighted constant and noncollinearity of cyclic normals follow from strict cyclic positivity and alternating k; compactness is universal on this scope.',
 'scope':'This proves boundedness only, NOT that the fourteen noncyclic inequalities are redundant or that the six repaired image cells cover the positive target.'}
(N/'results/seven-point-cyclic-polygon-boundedness.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'weights':result['positive_weights'],'mutations_rejected':7},indent=2))
