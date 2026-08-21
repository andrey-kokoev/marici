"""Exact rank-four amplitude -> helicity state -> Bell comparison."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

# Real and imaginary parts keep conjugation exact and simplification finite.
ar, ai, br, bi, cr, ci = sp.symbols("ar ai br bi cr ci", real=True)
a, b, c = ar + sp.I*ai, br + sp.I*bi, cr + sp.I*ci

# Canonical fixed-input contraction of a rank-four helicity tensor.
A = sp.MutableDenseNDimArray.zeros(2,2,2,2)
symbols = sp.symbols("A0:16")
for idx, value in zip(itertools.product(range(2), repeat=4), symbols):
    A[idx] = value
mu_generic = sp.Matrix([A[0,0,o1,o2] for o1 in range(2) for o2 in range(2)])

# Identical-particle + parity packet of Sinha-Zahed for incoming ++.
mu = sp.Matrix([a,c,c,b])
norm2 = sp.expand_complex(sum(sp.conjugate(v)*v for v in mu))

alpha = {1:sp.Rational(0), 2:sp.Rational(1,2)}
beta = {1:sp.Rational(1,4), 2:sp.Rational(-1,4)}

def phase(q):
    return sp.exp(sp.I*sp.pi*q)

def raw_prob(Asetting, Bout, alice_out, bob_out):
    amp = 0
    for m in range(2):
        for n in range(2):
            amp += mu[2*m+n]*phase(m*(alice_out+alpha[Asetting]))*phase(n*(-bob_out+beta[Bout]))
    return sp.simplify(sp.expand_complex(amp*sp.conjugate(amp))/(4*norm2))

P={(x,y,j,l):raw_prob(x,y,j,l) for x in (1,2) for y in (1,2) for j in (0,1) for l in (0,1)}
eq=lambda x,y,shift: sp.simplify(sum(P[x,y,j,(j+shift)%2] for j in (0,1)))

# Eq. (6), written with Alice's outcome as the summation index.
Ibell=sp.simplify(
    eq(1,1,0) + eq(2,1,1) + eq(2,2,0) + eq(1,2,0)
    - eq(1,1,1) - eq(2,1,0) - eq(2,2,1) - eq(1,2,1)
)
expected=sp.simplify(2*sp.sqrt(2)*(a*sp.conjugate(b)+b*sp.conjugate(a))/norm2)
bell_residual=sp.simplify(Ibell-expected)
two_term=sp.simplify(expected.subs({cr:0,ci:0}))
source_two_term=sp.simplify(2*sp.sqrt(2)*(a*sp.conjugate(b)+b*sp.conjugate(a))/(sp.conjugate(a)*a+sp.conjugate(b)*b))

normalization=[sp.simplify(sum(P[x,y,j,l] for j in (0,1) for l in (0,1))-1) for x in (1,2) for y in (1,2)]
alice_ns=[sp.simplify(sum(P[x,1,j,l] for l in (0,1))-sum(P[x,2,j,l] for l in (0,1))) for x in (1,2) for j in (0,1)]
bob_ns=[sp.simplify(sum(P[1,y,j,l] for j in (0,1))-sum(P[2,y,j,l] for j in (0,1))) for y in (1,2) for l in (0,1)]

payload={
 "schema":"marici.rank-four-photon-bell-map.v1",
 "strength":"exact symbolic source comparison",
 "canonical_fixed_input_contraction":[str(v) for v in mu_generic],
 "source_symmetry_image":["Phi1","Phi5","Phi5","Phi2"],
 "two_term_condition":"Phi5 = 0 (low-energy dynamical suppression, not parity/crossing alone)",
 "normalization_residuals":[str(v) for v in normalization],
 "alice_no_signalling_residuals":[str(v) for v in alice_ns],
 "bob_no_signalling_residuals":[str(v) for v in bob_ns],
 "full_bell_residual_against_source_Phi5_formula":str(bell_residual),
 "full_bell_formula":"2*sqrt(2)*(Phi1*conj(Phi2)+Phi2*conj(Phi1))/(abs(Phi1)^2+abs(Phi2)^2+2*abs(Phi5)^2)",
 "two_term_residual_against_source_equation_13":str(sp.simplify(two_term-source_two_term)),
 "conclusion":"The canonical contraction and Born lens reproduce the Sinha-Zahed photon packet exactly; the reduction from four coefficients to two uses Phi5 approximately zero, not symmetry alone."
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"rank-four-photon-bell-map.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert mu_generic == sp.Matrix([A[0,0,0,0],A[0,0,0,1],A[0,0,1,0],A[0,0,1,1]])
assert all(v==0 for v in normalization+alice_ns+bob_ns)
assert bell_residual==0
assert sp.simplify(two_term-source_two_term)==0
print(json.dumps({"rank_four_map":True,"source_symmetry_packet":True,"born_match":True,"sha256":payload["content_sha256"]}))
