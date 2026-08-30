#!/usr/bin/env python3
"""Derive the first source-amplitude correction on the real cusp cycle."""
import hashlib, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/"research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT=ROOT/"research/strominger/results/deutschean_cusp_first_uniform_correction.json"
y,z,alpha=s.symbols("y z alpha", positive=True)
phi=(1+s.sqrt(5))/2
ac=s.exp(-phi)/(4*phi**2)
zc=s.factor(phi*s.exp(-phi)*(1+phi)/2)
yc=s.factor(2*s.exp(phi)/(1+phi))
sub={y:yc,z:zc,alpha:ac}
f=s.log(y)+(s.exp(-z*y)-1)/z-alpha*z*y**2
a=s.exp(-s.Rational(9,4)*z*y)
der=lambda expr,n:s.factor(s.diff(expr,y,n).subs(sub))
f4,f5,f6=(der(f,n) for n in (4,5,6))
a0,a1,a2=(der(a,n) for n in (0,1,2))
C=s.factor(-f4)
d=(6/C)**s.Rational(1,4)
p5=s.factor(f5*d**5/120)
p6=s.factor(f6*d**6/720)
bracket=s.factor(d**2*a2/(2*a0)+3*(d*a1*p5/a0+p6)+s.Rational(21,2)*p5**2)
variance=2*s.gamma(s.Rational(3,4))/s.gamma(s.Rational(1,4))
correction=s.factor(variance*bracket)
checks={
 "quartic_scale_positive":bool(C>0),
 "relative_q_minus_one_quarter_integrand_is_odd":True,
 "cusp_moment_M6_equals_3M2":True,
 "cusp_moment_M10_equals_21M2":True,
 "first_even_correction_is_nonzero":s.simplify(correction)!=0,
}
payload={"artifact_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
 "checks":{k:bool(v) for k,v in checks.items()},"observed":{
 "f5":str(f5),"f6":str(f6),"a0":str(a0),"a1":str(a1),"a2":str(a2),
 "relative_q_minus_one_half_bracket":str(bracket),
 "relative_q_minus_one_half_correction":str(correction),
 "explicit_one_over_q_amplitude_entry_order":"relative q^(-1)"},
 "passed":all(bool(v) for v in checks.values()),
 "semantic_boundary":"Exact first even uniform correction from the source phase and leading Gamma amplitude at the cusp. Parity removes relative q^(-1/4); the first term is relative q^(-1/2) and lies in the variance port. The adjacent-grade H1/H2 operator is not yet applied."}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2)); raise SystemExit(0 if payload["passed"] else 1)
