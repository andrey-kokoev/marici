"""Exact algebraic eight-support paired-cell lift and local CZ image-rank gate."""
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sympy as s
from check_nine_point_no_seven_support_packet import replay
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
lower=json.loads((OUT/'nine-point-no-seven-support-verification.json').read_text());assert replay(frozen,lower)==36
upper=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
labels=upper['retained_labels'];assert labels==[1,2,4,5,6,7,8,9]
Z=s.Matrix([[j**d for d in range(6)] for j in labels]);full=s.Matrix([[s.Rational(t) for t in row] for row in upper['source_rows']]);C=full[:,[i-1 for i in labels]]
K=s.Matrix.vstack(s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0]]),s.Matrix([list(-Z[7,:]*Z[:6,:].inv())+[0,1]]))
assert K*Z==s.zeros(2,6)
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(M,i,j):return s.expand(M[0,i]*M[1,j]-M[0,j]*M[1,i])
def lifted(i,j):
 base=minor(C,i,j)
 linear=sum(T[0,p]*(K[p,i]*C[1,j]-K[p,j]*C[1,i])+T[1,p]*(C[0,i]*K[p,j]-C[0,j]*K[p,i]) for p in range(2))
 return s.expand(base+linear+q*(K[0,i]*K[1,j]-K[0,j]*K[1,i]))
matching=[(0,1),(2,3),(4,5),(6,7)];equations=[lifted(*p) for p in matching]
M,rhs=s.linear_eq_to_matrix(equations,(a,b,c,d));assert M.det()!=0
solution=[s.factor(v) for v in M.inv()*rhs];sub=dict(zip((a,b,c,d),solution))
assert all(s.expand(f.subs(sub))==0 for f in equations)
P=s.Poly(s.factor(q-(solution[0]*solution[3]-solution[1]*solution[2])),q);assert P.degree()==2
left,right=s.Rational(-19199558,10**12),s.Rational(-19199557,10**12)
assert left<right and P.eval(left)*P.eval(right)<0
# A quadratic with opposite signs at endpoints has exactly one simple root
# in this interval. All nonactive minors are AFFINE in q on the lifted line.
other=[]
for pair in combinations(range(8),2):
 if pair in matching:continue
 F=s.Poly(s.expand(lifted(*pair).subs(sub)),q);assert F.degree()<=1
 assert F.eval(left)>0 and F.eval(right)>0
 other.extend([F.eval(left),F.eval(right)])
# The graph/linear intersection is transverse. It follows that the four
# paired constraints have full rank ON THE FOUR-DIMENSIONAL SOURCE FIBRE.
actual=[s.expand(f.subs(q,a*d-b*c)) for f in equations]
J=s.factor(s.Matrix(actual).jacobian((a,b,c,d)).det().subs(sub))
Jpoly=s.Poly(J,q);assert s.gcd(Jpoly,P).degree()==0
# Source-cell dimension: G(2,8) is 12-dimensional; four independent paired
# adjacent minors impose four conditions. The transverse fibre intersection
# makes its differential to the eight-dimensional target invertible here.
report={'schema':'marici.nima.nine-point-paired-cell-exact.v1','passed':True,
 'retained_source_labels':labels,'deleted_label':3,
 'paired_source_edges':[[labels[i],labels[j]] for i,j in matching],
 'cell_source_dimension':8,'target_dimension':8,
 'quadratic_graph_polynomial':str(P.as_expr()),'unique_root_interval':[str(left),str(right)],
 'other_ordered_minors_certified_strict':24,
 'minimum_rational_endpoint_minor_bound':str(min(other)),
 'four_fibre_constraint_matrix_determinant':str(s.factor(M.det())),
 'jacobian_graph_polynomial_coprime_to_root_polynomial':True,
 'all_seven_or_fewer_label_supports_excluded':36,
 'scope':'One exact algebraic positive eight-label paired source cell over a fixed nine-point target, with local full image rank. No sourced generalized-R history/canonical-form identification, global nine-point cell coverage, or analytic n^-2 result.'}
(OUT/'nine-point-paired-cell-exact.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'pairs':report['paired_source_edges'],'positive_remaining_minors':24,
 'root_interval':report['unique_root_interval'],'image_rank':8,'min_other_endpoint_bound':report['minimum_rational_endpoint_minor_bound']},indent=2))
