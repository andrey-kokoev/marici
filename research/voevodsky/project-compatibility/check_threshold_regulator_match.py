"""Same-density singular-coefficient and finite-part bookkeeping controls."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'threshold-regulator-consolidation.md',HERE/'restored-period-threshold-continuation.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();e=s.symbols('epsilon');d,V,M,mu,P=s.symbols('delta V M mu P',positive=True)
b0,b1,c,sigma=s.symbols('b0 b1 c sigma',real=True)
area=2*s.pi**(1+e)/s.gamma(1+e)
assert area.subs(e,0)==2*s.pi
assert s.simplify(s.diff(area,e).subs(e,0)/(2*s.pi)-s.log(s.pi)-s.EulerGamma)==0
# Local profile beta_e(v)=b0+e*b1+c*v on [0,V].
regulated=(b0/e+b1)*(V/M)**e+c*V*(V/M)**e/(1+e)
assert s.limit(e*regulated,e,0)==b0
finite=s.simplify(s.limit(regulated-b0/e,e,0))
threshold=b0*(s.log(V+d)-s.log(d))+c*(V-d*(s.log(V+d)-s.log(d)))
C_M=s.simplify(s.limit(threshold+b0*s.log(d/M),d,0,dir='+'))
assert s.simplify(finite-C_M-b1)==0
assert s.limit(d*s.diff(threshold,d),d,0,dir='+')==-b0
# Constant f0 endpoint fixture: all endpoint weights included, not a physical f0 replacement.
endpoint=2*s.pi*(2*s.pi*P*M/mu**2)**e*s.gamma(1+e)/s.gamma(2+2*e)
B1=s.simplify(s.diff(endpoint,e).subs(e,0))
expected=2*s.pi*(s.EulerGamma+s.log(2*s.pi*P*M/mu**2)-2)
assert s.simplify(B1-expected)==0
assert s.simplify(s.diff(B1,mu)*mu+4*s.pi)==0
# Scale transformation acts on the whole regulated period.
shifted=s.exp(-2*sigma*e)*regulated
assert s.simplify(s.limit(shifted-b0/e,e,0)-finite+2*sigma*b0)==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'singular_coefficient_match':'regulator residue = negative-log coefficient = B0','finite_part_relation':'FP_dim=C_M+B1','angular_log_derivative':'log(pi)+EulerGamma','endpoint_fixture_B1':str(expected),'mu_scale_finite_shift':'-2 sigma B0','scope':'Exact Mellin/angle/endpoint fixtures. Same-density theorem is written analysis for the declared rotational Lebesgue continuation; no physical subtraction prescription selected.'}
(HERE/'threshold-regulator-consolidation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
