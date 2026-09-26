"""Normalized source coefficient recursion and contact-grade/score traps."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'normalized-contact-jet-map.md',ROOT/'src/ledger/20260824-2158 The First Contact Null Syndrome Is Pointwise but Not Source-Constant.md',ROOT/'temp/triangle-measure-primary-2401.05207-source/GeomCosmoCorr.tex']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();l,nu,X=s.symbols('lambda nu X');g=s.symbols('g',positive=True)
V,U,a,b=s.symbols('V U a b')
R=1+l*(V-a)+l*l*(U-a*V+a*a-b)
assert s.series(R*(1+l*a+l*l*b)-(1+l*V+l*l*U),l,0,3).removeO().expand()==0
V0,V1,U0,U1,a0,a1,b0,b1=s.symbols('V0 V1 U0 U1 a0 a1 b0 b1')
jet=s.expand((U-a*V+a*a-b).subs({V:V0+nu*V1,U:U0+nu*U1,a:a0+nu*a1,b:b0+nu*b1})).coeff(nu,1)
assert s.expand(jet-(U1-b1-a0*V1-a1*V0+2*a0*a1))==0
def E(expr,var=1):
 total=0
 for (n,),coef in s.Poly(s.expand(expr),X).terms():
  if not n%2:total+=coef*(s.factorial2(n-1) if n else 1)*var**(n//2)
 return s.simplify(total)
v=X**2+nu*X**4;av=E(v);r1=v-av;r2=-av*v+av**2
assert E(r1)==0 and E(r2)==0
actual=s.expand(E(X**2*r2)).coeff(nu,1)
naive=E(X**2*(-E(X**4)*X**4+E(X**4)**2))
assert actual==-18 and naive==-36
exact=(1+l*E(X**2*v))/(1+l*av)
assert s.expand(s.series(exact,l,0,3).removeO()).coeff(l,2).coeff(nu,1)==actual
S=(X**2/g-1)/2;rg=X**2-g
fixed_term=E(X**2*rg*S,g);correction=E(X**2*(-g),g)
assert fixed_term==5*g*g and correction==-g*g
assert s.simplify(fixed_term+correction-g*s.diff(E(X**2*rg,g),g))==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'normalization_order_checked':2,'correct_lambda2_nu_coefficient':int(actual),'discarded_lower_grade_result':int(naive),'fixed_effective_insertion_score_term':'5*g**2','normalization_derivative_correction':'-g**2','correct_log_covariance_response':'4*g**2','scope':'Universal normalized perturbative interface and exact Gaussian controls. Actual source contact coefficients and uniform physical norm bounds remain to be instantiated.'}
(HERE/'normalized-contact-jet-map.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
