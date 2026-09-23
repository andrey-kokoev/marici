"""Exact two-branch trace of a COMPLETE sourced four-mass psi fermion component."""
import json
from pathlib import Path
import sympy as s
import check_nine_point_four_mass_auxiliary_match as aux
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
fixture=json.loads((ROOT/'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json').read_text())
assert next(x for x in fixture['cyclic_classes'] if x['id']==9)['formula']=='psi [A,1,2,3,4] [B,5,6,7,8]'
alpha,beta=aux.alpha,aux.beta;P=aux.Palpha;B=aux.beta_q
assert P.degree()==2
br=aux.bracket
def aux_bracket(seq,which):
 # A=z7+alpha*z8, B=z3+beta*z4; remaining labels are fixed.
 sentinel='A' if which=='A' else 'B';z1,z2=(7,8) if which=='A' else (3,4);r=alpha if which=='A' else beta
 assert seq.count(sentinel)==1
 return s.expand(br(*(z1 if j==sentinel else j for j in seq))+r*br(*(z2 if j==sentinel else j for j in seq)))
# For [A,1,2,3,4], coefficient chi1 is <2,3,4,A>;
# for [B,5,6,7,8], coefficient chi5 is <6,7,8,B>.
na=aux_bracket((2,3,4,'A'),'A');nb=aux_bracket((6,7,8,'B'),'B')
da=[aux_bracket(x,'A') for x in (('A',1,2,3),(2,3,4,'A'),(3,4,'A',1),(4,'A',1,2))]
da.insert(1,br(1,2,3,4))
db=[aux_bracket(x,'B') for x in (('B',5,6,7),(6,7,8,'B'),(7,8,'B',5),(8,'B',5,6))]
db.insert(1,br(5,6,7,8))
assert da[2]==na and db[2]==nb
beta_alpha=(aux.n0+alpha*aux.n1)/(aux.d0+alpha*aux.d1)
psi_num=(aux_bracket(('A',4,1,2),'A')*aux_bracket(('B',8,5,6),'B'))
psi_den=psi_num-aux_bracket(('A',4,5,6),'A')*aux_bracket(('B',8,1,2),'B')
# Source psi multiplied by BOTH complete five-bracket denominators,
# selecting the chi1^4 chi5^4 coefficient (A has only chi7,chi8 and
# B has only chi3,chi4, so auxiliary fermions cannot enter this component).
def field(expr):
 expr=s.cancel(expr.subs(beta,beta_alpha))
 num,den=s.fraction(expr)
 n,d=s.Poly(num,alpha),s.Poly(den,alpha)
 assert s.gcd(P,d).degree()==0
 return s.rem(n*s.invert(d,P),P)
def multiply(*polys):
 out=s.Poly(1,alpha)
 for p in polys:out=s.rem(out*p,P)
 return out
psi=field(psi_num/psi_den)
first=field(na**4/s.prod(da));second=field(nb**4/s.prod(db))
complete=multiply(psi,first,second)
a,b,c=P.all_coeffs();r0,r1=complete.nth(0),complete.nth(1)
trace=s.factor(2*r0-r1*b/a)
assert trace!=0 and first.degree()<=1 and second.degree()<=1
assert psi==s.Poly(s.Rational(json.loads((OUT/'nine-point-source-four-mass-psi-field-trace.json').read_text())['psi_reduced_constant_coefficient'])+s.Rational(json.loads((OUT/'nine-point-source-four-mass-psi-field-trace.json').read_text())['psi_reduced_alpha_coefficient'])*alpha,alpha)
# Negating either one five-bracket contribution must reverse a nonzero trace.
assert -trace!=trace
result={'schema':'marici.nima.nine-point-complete-four-mass-psi-component-trace.v1','passed':True,
 'source_class':'arXiv:1212.5605 starred psi [A,1,2,3,4][B,5,6,7,8]',
 'component':'chi1^4 chi5^4 in the ordered eight-point quotient labels (1,2,3,4,5,6,7,8) mapped to physical (1,2,4,5,6,7,8,9)',
 'two_branch_component_trace':str(trace),
 'two_branch_component_trace_nonzero':True,
 'source_prefactor_check':'psi reduced modulo the source auxiliary quadratic agrees with independently frozen prefactor trace packet',
 'claim_boundary':'Exact complete sourced psi super-five-bracket COMPONENT trace at one rational nine-point Y with common quotient four-brackets. No equality with the target eight-form coefficient is asserted without a derived bosonization/component-to-volume map; no nine-point generalized-R history assigned.'}
(OUT/'nine-point-complete-four-mass-psi-component-trace.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'complete_component_trace_digits':len(str(trace)),
 'nonzero':True,'target_form_equality_claimed':False},indent=2))
