"""Prolate threshold geometry and logarithmic continuation controls."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'restored-period-threshold-continuation.md',HERE/'positive-sheet-normal-integration.md',HERE/'contact-route-density-restoration.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();P,v,delta,V=s.symbols('P v delta V',positive=True);z=s.symbols('z',real=True)
a=(P+v+z)/2;b=(P+v-z)/2
u=P/2+(P+v)*z/(2*P)
rho2=((P+v)**2-P**2)*(P**2-z**2)/(4*P**2)
assert s.simplify(u*u+rho2-a*a)==0
assert s.simplify((u-P)**2+rho2-b*b)==0
jac=s.Matrix([u,rho2]).jacobian([v,z]).det()
assert s.simplify(-jac/2-a*b/(2*P))==0
assert s.simplify((-jac/2)/(a*b)-1/(2*P))==0
assert s.simplify(rho2.subs(v,0))==0
assert s.simplify(P*P-(-P+delta)**2-(2*P*delta-delta**2))==0
b0,b1=s.symbols('b0 b1',real=True)
J=b0*(s.log(delta+V)-s.log(delta))+b1*(V-delta*(s.log(delta+V)-s.log(delta)))
assert s.simplify(s.diff(J,V)-(b0+b1*V)/(delta+V))==0
assert s.limit(delta*s.diff(J,delta),delta,0,dir='+')==-b0
q=s.symbols('q',positive=True)
# q<V: negative-delta boundary values of the two logs.
real_log=s.log(V-q)-s.log(q)
upper=b0*(real_log-s.I*s.pi)+b1*(V+q*(real_log-s.I*s.pi))
lower=b0*(real_log+s.I*s.pi)+b1*(V+q*(real_log+s.I*s.pi))
assert s.simplify(upper-lower+2*s.pi*s.I*(b0+b1*q))==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'jacobian_after_focal_cancellation':'1/(2P)','normal_relation':'nu=2P delta-delta^2','leading_threshold_term':'-B0 Log(delta)','discontinuity_upper_minus_lower':'-2pi i B(s)','endpoint_scope':'Entire focal segment including endpoints, with third center off segment.','scope':'Exact coordinate/kernel fixtures support a written analytic continuation theorem for the restored representative, not a physical i0 selection or full graph observable.'}
(HERE/'restored-period-threshold-continuation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
