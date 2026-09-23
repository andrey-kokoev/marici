"""Match sourced four-mass auxiliary alpha,beta equations to exact n=9 cell roots."""
import json
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=json.loads((OUT/'nine-point-four-mass-source-match.json').read_text());assert source['passed']
tex=(ROOT/source['primary_source']).read_text(encoding='utf-8');src=tex.index(r'\label{four_mass_explicit_solution}')
source_equation=tex[src-650:src]
assert r'A=z_7+\alpha z_8' in source_equation and r'B=z_3+\beta z_4' in source_equation
assert r'\ab{5\,6\,3\,7}+\beta\ab{5\,6\,4\,7}' in source_equation
assert r'\ab{8\,5\,6\,3}+\beta\ab{8\,5\,6\,4}' in source_equation
assert r'\ab{1\,2\,7\,3}+\alpha\ab{1\,2\,8\,3}' in source_equation
assert r'\ab{4\,1\,2\,7}+\alpha\ab{4\,1\,2\,8}' in source_equation
prior=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text());assert prior['passed']
raw=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
weights=list(map(Q,raw['weights']));slopes=list(map(Q,raw['slopes']));negative=raw['negative_initial_columns']
X=[-weights[i] if i<negative else weights[i] for i in range(9)];V=[X[i]*slopes[i] for i in range(9)]
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
Y=s.Matrix([[sum(X[j]*Z[j,d] for j in range(9)) for d in range(6)],
            [sum(V[j]*Z[j,d] for j in range(9)) for d in range(6)]])
labels=[1,2,4,5,6,7,8,9]
def bracket(i,j,k,l):return s.Matrix.vstack(Y,*[Z[labels[h-1]-1,:] for h in (i,j,k,l)]).det(method='domain-ge')
# Source arXiv:1212.5605, equation four_mass_explicit_solution:
# alpha=(<5637>+beta<5647>)/(<8563>+beta<8564>)
# beta=(<1273>+alpha<1283>)/(<4127>+alpha<4128>).
f0,f1=bracket(5,6,3,7),bracket(5,6,4,7)
e0,e1=bracket(8,5,6,3),bracket(8,5,6,4)
n0,n1=bracket(1,2,7,3),bracket(1,2,8,3)
d0,d1=bracket(4,1,2,7),bracket(4,1,2,8)
alpha,beta,q=s.symbols('alpha beta q')
source_alpha=s.expand(alpha*(e0+beta*e1)-f0-beta*f1)
source_beta=s.expand(beta*(d0+alpha*d1)-n0-alpha*n1)
Palpha=s.Poly(s.factor((d0+alpha*d1)*source_alpha.subs(beta,(n0+alpha*n1)/(d0+alpha*d1))),alpha)
assert Palpha.degree()==2 and s.discriminant(Palpha.as_expr(),alpha)!=0
# Construct exact paired-cell source over original Y, using the frozen
# rational eight-label source as a section of the same target fibre.
base=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
C=s.Matrix([[s.Rational(v) for v in row] for row in base['source_rows']])[:,[j-1 for j in labels]]
Z8=Z[[j-1 for j in labels],:];K=s.Matrix([list(-Z8[6,:]*Z8[:6,:].inv())+[1,0],list(-Z8[7,:]*Z8[:6,:].inv())+[0,1]])
a,b,c,d=s.symbols('a b c d');T=s.Matrix([[a,b],[c,d]])
def affine(i,j):
 Cq=C+T*K;f=s.Poly(s.expand(Cq[0,i]*Cq[1,j]-Cq[0,j]*Cq[1,i]),a,b,c,d)
 assert f.coeff_monomial(a*d)==-f.coeff_monomial(b*c)
 return f.coeff_monomial(1)+sum(f.coeff_monomial(v)*v for v in (a,b,c,d))+f.coeff_monomial(a*d)*q
pairs=((0,1),(2,3),(4,5),(6,7));M,rhs=s.linear_eq_to_matrix([affine(*p) for p in pairs],(a,b,c,d))
solution=M.inv()*rhs;Pq=s.Poly(s.factor(q-solution[0]*solution[3]+solution[1]*solution[2]),q)
assert s.expand(Pq.as_expr()-s.sympify(prior['quadratic_graph_polynomial'],locals={'q':q}))==0
Cq=C+T.subs(dict(zip((a,b,c,d),solution)))*K
D=s.cancel(Cq[:,[0,2]].inv()*Cq)
alpha_q=s.cancel(D[0,7]/D[0,6]);beta_q=s.cancel(D[1,3]);assert alpha_q.has(q) and beta_q.has(q)
def remainder(expr):
 num=s.fraction(s.cancel(expr))[0];return s.rem(s.Poly(num,q),Pq)
assert remainder(source_alpha.subs({alpha:alpha_q,beta:beta_q})).is_zero
assert remainder(source_beta.subs({alpha:alpha_q,beta:beta_q})).is_zero
assert remainder(Palpha.as_expr().subs(alpha,alpha_q)).is_zero
assert not remainder((source_alpha+1).subs({alpha:alpha_q,beta:beta_q})).is_zero
assert not remainder((source_beta+1).subs({alpha:alpha_q,beta:beta_q})).is_zero
# The two independent exact quadratic presentations generate the SAME
# nonsplit field over the rational target. Test their discriminant classes.
disc_ratio=s.factor(s.discriminant(Palpha.as_expr(),alpha)/s.discriminant(Pq.as_expr(),q))
num,den=map(int,s.fraction(disc_ratio));assert num>0 and den>0 and isqrt(num)**2==num and isqrt(den)**2==den
result={'schema':'marici.nima.nine-point-four-mass-auxiliary-match.v1','passed':True,
 'source_equation':'arXiv:1212.5605 four_mass_explicit_solution, with eight-point labels (1,2,3,4,5,6,7,8) mapped to physical (1,2,4,5,6,7,8,9)',
 'source_auxiliary_alpha_quadratic':str(Palpha.as_expr()),
 'source_auxiliary_alpha_in_paired_kernel_q':str(alpha_q),
 'source_auxiliary_beta_in_paired_kernel_q':str(beta_q),
 'alpha_and_beta_source_equations_vanish_mod_graph_quadratic':True,
 'two_perturbed_source_equations_refused':True,
 'auxiliary_and_graph_quadratic_discriminant_ratio_square':True,
 'discriminant_square_root_of_ratio':str(s.Rational(isqrt(num),isqrt(den))),
 'claim_boundary':'Source-identified eight-point four-mass psi cell and exact identification of BOTH kinematic solution branches for the embedded n=9 target. Does not match complete psi superfunction/canonical form or show a sourced nine-point generalized-R history includes this cell.'}
(OUT/'nine-point-four-mass-auxiliary-match.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'source_alpha_beta_match_both_branches':True,
 'same_quadratic_field':True,'nine_point_history_matched':False},indent=2))
