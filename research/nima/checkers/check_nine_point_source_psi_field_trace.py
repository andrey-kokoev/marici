"""Exact quadratic-field trace of the sourced four-mass psi PREFactor at fixed Y."""
import json
from pathlib import Path
import sympy as s
import check_nine_point_four_mass_auxiliary_match as aux
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-four-mass-psi-jacobian.json').read_text());assert prior['passed']
alpha,beta=aux.alpha,aux.beta
P=s.Poly(aux.Palpha,alpha);a,b,c=[P.nth(k) for k in (2,1,0)]
assert a>0 and b>0 and c<0 and s.discriminant(P.as_expr(),alpha)>0
# Opposite signs of the two sourced alpha roots: exactly one is positive.
A456=aux.bracket(7,4,5,6)+alpha*aux.bracket(8,4,5,6)
B812=aux.bracket(3,8,1,2)+beta*aux.bracket(4,8,1,2)
A412=aux.bracket(7,4,1,2)+alpha*aux.bracket(8,4,1,2)
B856=aux.bracket(3,8,5,6)+beta*aux.bracket(4,8,5,6)
psi=s.cancel(A412*B856/(A412*B856-A456*B812))
beta_alpha=(aux.n0+alpha*aux.n1)/(aux.d0+alpha*aux.d1)
num,den=s.fraction(s.cancel(psi.subs(beta,beta_alpha)))
N,D=s.Poly(num,alpha),s.Poly(den,alpha);assert s.gcd(P,D).degree()==0
reduced=s.rem(N*s.invert(D,P),P);r0,r1=map(s.factor,(reduced.nth(0),reduced.nth(1)))
assert r1!=0
trace=s.factor(2*r0-r1*b/a)
norm=s.factor(r0*r0-r0*r1*b/a+r1*r1*c/a)
assert trace!=0 and norm!=0
# If alpha+ and alpha- are the two solutions then
# psi(alpha+)+psi(alpha-)=trace, psi(alpha+)*psi(alpha-)=norm.
packet={'schema':'marici.nima.nine-point-source-four-mass-psi-field-trace.v1','passed':True,
 'alpha_polynomial':str(P.as_expr()),'alpha_roots_have_opposite_signs':True,
 'psi_reduced_constant_coefficient':str(r0),'psi_reduced_alpha_coefficient':str(r1),
 'psi_two_branch_trace':str(trace),'psi_two_branch_norm':str(norm),
 'psi_branch_values_distinct':True,
 'scope':'Exact field trace of the sourced psi PREFACTOR only, at one fixed rational Y. The complete psi times two super-five-brackets and nine-point history coefficient are NOT compared with the traced CZ cell form.'}
(OUT/'nine-point-source-four-mass-psi-field-trace.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'passed':True,'opposite_sign_alpha_roots':True,
 'psi_branches_distinct':True,'prefactor_trace_digits':len(str(trace))},indent=2))
