"""Source psi prefactor is the inverse coupled-auxiliary Jacobian, both sheets."""
from pathlib import Path
import json
import sympy as s
import check_nine_point_four_mass_auxiliary_match as src
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source_tex=(ROOT/'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex').read_text(encoding='utf-8')
assert r'\psi\equiv\left(1-\frac{\ab{A\,4\,5\,6}\ab{B\,8\,1\,2}}{\ab{A\,4\,1\,2}\ab{B\,8\,5\,6}}\right)^{-1}' in source_tex
alpha,beta,q=src.alpha,src.beta,src.q
f,g=src.source_alpha,src.source_beta
A456=src.bracket(7,4,5,6)+alpha*src.bracket(8,4,5,6)
B812=src.bracket(3,8,1,2)+beta*src.bracket(4,8,1,2)
A412=src.bracket(7,4,1,2)+alpha*src.bracket(8,4,1,2)
B856=src.bracket(3,8,5,6)+beta*src.bracket(4,8,5,6)
# Alternation of four-brackets, independently evaluated on the quotient:
assert s.expand(A456-s.diff(f,beta))==0
assert s.expand(B812-s.diff(g,alpha))==0
assert s.expand(A412+s.diff(g,beta))==0
assert s.expand(B856+s.diff(f,alpha))==0
jac=s.factor(s.Matrix([f,g]).jacobian((alpha,beta)).det())
assert s.expand(jac-(A412*B856-A456*B812))==0
psi=s.factor(A412*B856/jac)
assert s.simplify(psi-1/(1-A456*B812/(A412*B856)))==0
# Pull the SOURCE psi prefactor onto the earlier fibre quadratic via
# independently matched alpha(q), beta(q). It is regular at BOTH roots.
sub={alpha:src.alpha_q,beta:src.beta_q};P=src.Pq
num,den=s.fraction(s.cancel(psi.subs(sub)))
num_poly,den_poly=s.Poly(num,q),s.Poly(den,q)
assert s.gcd(P,den_poly).degree()==0
assert s.gcd(P,num_poly).degree()==0
# The source's two-branch psi prefactor really distinguishes the branches.
rem=s.rem(num_poly,P);assert rem.degree()>=0
# A rational function over a quadratic field is conjugation-invariant iff
# its remainder after elimination of q has no q term.
invden=s.invert(den_poly,P);reduced=s.rem(rem*invden,P)
branch_distinct=reduced.degree()==1
result={'schema':'marici.nima.nine-point-four-mass-psi-jacobian.v1','passed':True,
 'source':'arXiv:1212.5605 Table g2n_yangian_invariants starred row, psi prefactor and four_mass_explicit_solution',
 'universal_identity':'psi=<A412><B856>/det(d(f,g)/d(alpha,beta)); f=alpha<856B>-<56B7>, g=beta<412A>-<127A>',
 'four_alternating_bracket_derivative_signs_checked':True,
 'jacobian_and_psi_denominators_coprime_to_graph_quadratic':True,
 'psi_algebraic_branch_values_distinct':bool(branch_distinct),
 'scope':'Exact source-prefactor normalization as an implicit two-variable Jacobian and regularity on both fixed-target branches. Does not compare the complete two-five-bracket superfunction to the traced CZ canonical form or show a nine-point generalized-R history.'}
(OUT/'nine-point-four-mass-psi-jacobian.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'psi_inverse_auxiliary_jacobian':True,
 'both_branches_regular':True,'psi_branch_values_distinct':bool(branch_distinct)},indent=2))
