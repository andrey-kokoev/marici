"""Universal symbolic two-solution partition-of-unity for sourced four-mass psi."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
alpha,beta=s.symbols('alpha beta')
e0,e1,f0,f1,n0,n1,d0,d1=s.symbols('e0 e1 f0 f1 n0 n1 d0 d1')
# Eight formal quotient brackets from the two sourced auxiliary equations;
# no moment-curve specialization or accidental Pluecker identity is used.
f=alpha*(e0+beta*e1)-(f0+beta*f1)
g=beta*(d0+alpha*d1)-(n0+alpha*n1)
g_beta=s.diff(g,beta);f_alpha=s.diff(f,alpha)
J=s.expand(s.det(s.Matrix([f,g]).jacobian((alpha,beta))))
# Source psi numerator <A412><B856> = (-g_beta)*(-f_alpha).
psi_num=s.expand(g_beta*f_alpha)
beta_solution=(n0+alpha*n1)/(d0+alpha*d1)
P=s.Poly(s.cancel((d0+alpha*d1)*f.subs(beta,beta_solution)),alpha)
assert P.degree()==2
A,B,C=P.all_coeffs();H0=e0*d0+e1*n0
assert s.expand(A-e0*d1-e1*n1)==0
assert s.cancel(psi_num.subs(beta,beta_solution)-(H0+A*alpha))==0
# Differentiating the eliminated equation: P'=J+d1*f along g=0.
assert s.factor(P.diff().as_expr()-J.subs(beta,beta_solution)-d1*f.subs(beta,beta_solution))==0
# On every simple root of P, sourced psi=(H0+A*alpha)/P'(alpha).
# For quadratic roots alpha+/-: P'(alpha+)=-P'(alpha-), so the
# branch-odd remainder cancels exactly and psi+ + psi- = 1.
assert s.factor((H0+A*alpha)-P.diff().as_expr()/2-(H0-B/2))==0
root_plus,root_minus=s.symbols('root_plus root_minus')
branch_sum=(H0+A*root_plus)/(A*(root_plus-root_minus))+(H0+A*root_minus)/(A*(root_minus-root_plus))
assert s.cancel(branch_sum)==1
packet=json.loads((OUT/'nine-point-source-four-mass-psi-field-trace.json').read_text())
assert packet['passed'] and s.Rational(packet['psi_two_branch_trace'])==1
assert s.Rational(packet['psi_reduced_alpha_coefficient'])!=0
result={'schema':'marici.nima.four-mass-psi-universal-partition.v1','passed':True,
 'formal_auxiliary_equations':'f=alpha*(e0+beta*e1)-f0-beta*f1; g=beta*(d0+alpha*d1)-n0-alpha*n1',
 'on_shell_psi':'(H0+A*alpha)/(2*A*alpha+B), where H0=e0*d0+e1*n0 and A,B are the alpha-quadratic coefficients',
 'two_simple_solution_prefactors_sum_to_one':True,
 'fixed_nine_point_exact_trace_replayed':'1',
 'scope':'Universal prefactor-only partition-of-unity for sourced four-mass psi under two simple auxiliary roots and nonzero denominators. Not a trace identity for the two super-five-brackets, a complete canonical-form comparison, or a nine-point generalized-R history assignment.'}
(OUT/'four-mass-psi-universal-partition.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_psi_two_branch_sum':1,'fixed_target_trace':1},indent=2))
