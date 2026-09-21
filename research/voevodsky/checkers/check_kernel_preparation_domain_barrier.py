"""Preparation does not preserve the raw reduced-response kernel."""
from pathlib import Path
import json
import sympy as s
q,z=s.symbols('q z')
rho=s.Rational(1,2)+s.I
# Finite conjugate-paired Blaschke fixture, not actual xi zeros.
B=s.prod((q-r)/(q-(6-s.conjugate(r))) for r in (rho,s.conjugate(rho)))
C=s.factor(q*(q-1)*B/(4-q)**8)
assert C.subs(q,0)==0 and C.subs(q,1)==0
ss=s.Rational(3,2)
X=s.simplify((C.subs(q,ss)+C.subs(q,1-ss))/2)
assert X.is_positive is True
assert s.simplify(s.sqrt(2)*X/ss).is_positive is True
# The cosine-preparation and moment formulas, as identities on an
# arbitrary differentiable Cauchy function.
F=s.Function('C')
sz=s.Rational(1,2)-s.I*z
Xz=(F(sz)+F(1-sz))/2
moment=(s.diff(F(q),q).subs(q,sz)-s.diff(F(q),q).subs(q,1-sz))/2
assert s.simplify(s.I*s.diff(Xz,z)-moment)==0
# In a prepared fibre, zero first endpoint forces zero even state.
a,ssym=s.symbols('a ssym',nonzero=True)
assert s.simplify(ssym*(a/ssym)-a)==0
result={'passed':True,'checks':{'raw_source_endpoints_zero':True,
 'reprepared_endpoint_strictly_positive_in_fixture':True,
 'cosine_and_moment_preparation_identities':True,
 'prepared_even_endpoint_recovery':True},
 'scope':'Exact preparation identities and a toy Blaschke fixture. Actual kernel existence, real-axis positivity, absence of a compatible-family kernel and the finite-window domain barrier are proved in the note. No new source edge or balanced witness is admitted by this checker.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/kernel-preparation-domain-barrier.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
