"""Exact helicity-blind angular-bin pushforward for the photon Bell packet."""

import hashlib
import json
from pathlib import Path

import sympy as sp

x = sp.symbols("x", real=True)
L, U = sp.symbols("L U", real=True)
g, f = sp.symbols("g f", real=True)
q = 1-x+x**2
mu = sp.Matrix([g,0,0,2*f*q])
norm_density = sp.expand(sum(sp.conjugate(v)*v for v in mu))

alpha={1:sp.Rational(0),2:sp.Rational(1,2)}
beta={1:sp.Rational(1,4),2:sp.Rational(-1,4)}
phase=lambda z: sp.exp(sp.I*sp.pi*z)

def raw_density(a_setting,b_setting,j,l):
    amp=sum(mu[2*m+n]*phase(m*(j+alpha[a_setting]))*phase(n*(-l+beta[b_setting])) for m in range(2) for n in range(2))
    return sp.simplify(sp.expand_complex(amp*sp.conjugate(amp))/4)

total=sp.integrate(norm_density,(x,L,U))
P={(a,b,j,l):sp.simplify(sp.integrate(raw_density(a,b,j,l),(x,L,U))/total) for a in (1,2) for b in (1,2) for j in (0,1) for l in (0,1)}
eq=lambda a,b,shift:sp.simplify(sum(P[a,b,j,(j+shift)%2] for j in (0,1)))
Ibell=sp.simplify(eq(1,1,0)+eq(2,1,1)+eq(2,2,0)+eq(1,2,0)-eq(1,1,1)-eq(2,1,0)-eq(2,2,1)-eq(1,2,1))

W0=sp.integrate(1,(x,L,U))
W1=sp.integrate(q,(x,L,U))
W2=sp.integrate(q**2,(x,L,U))
expected=sp.simplify(8*sp.sqrt(2)*g*f*W1/(g**2*W0+4*f**2*W2))
full_interval=sp.simplify(expected.subs({L:0,U:1}))
full_expected=sp.simplify((sp.Rational(20,3)*sp.sqrt(2)*g*f)/(g**2+sp.Rational(14,5)*f**2))

normalization=[sp.simplify(sum(P[a,b,j,l] for j in (0,1) for l in (0,1))-1) for a in (1,2) for b in (1,2)]
alice_ns=[sp.simplify(sum(P[a,1,j,l] for l in (0,1))-sum(P[a,2,j,l] for l in (0,1))) for a in (1,2) for j in (0,1)]
bob_ns=[sp.simplify(sum(P[1,b,j,l] for j in (0,1))-sum(P[2,b,j,l] for j in (0,1))) for b in (1,2) for l in (0,1)]

payload={
 "schema":"marici.angular-bin-bell-pushforward.v1",
 "strength":"exact symbolic interval pushforward",
 "coordinate":"x=sin(theta/2)^2; two-body angular measure is constant times dx",
 "support_condition":"0 <= L < U <= 1 and one scalar nonnegative acceptance weight for all helicity outcomes",
 "W0":str(W0),"W1":str(W1),"W2":str(W2),
 "normalization_residuals":[str(v) for v in normalization],
 "alice_no_signalling_residuals":[str(v) for v in alice_ns],
 "bob_no_signalling_residuals":[str(v) for v in bob_ns],
 "interval_bell_residual":str(sp.simplify(Ibell-expected)),
 "full_interval_bell":str(full_interval),
 "full_interval_residual":str(sp.simplify(full_interval-full_expected)),
 "pushforward_rule":"integrate the unnormalized density |psi(x)><psi(x)|, then normalize once",
 "conclusion":"Helicity-blind angular acceptance defines a positive relative pushforward preserving normalization and no-signalling; its Bell value is the ratio of integrated interference to integrated intensity."
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"angular-bin-bell-pushforward.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert all(v==0 for v in normalization+alice_ns+bob_ns)
assert sp.simplify(Ibell-expected)==0
assert sp.simplify(full_interval-full_expected)==0
print(json.dumps({"interval_pushforward":True,"no_signalling":True,"full_bin_formula":True,"sha256":payload["content_sha256"]}))
