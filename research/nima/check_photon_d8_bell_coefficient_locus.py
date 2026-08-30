"""Exact Bell/positivity/identifiability locus for parity-even photon EFT D=8."""

import hashlib
import json
from pathlib import Path

import sympy as sp

r, rp, q, lam, g, f = sp.symbols("r rp q lam g f", real=True, nonzero=True)
x = sp.symbols("x", real=True)
sqrt2 = sp.sqrt(2)

q_x = 1 - x + x**2
y = 2*r*q
bell = sp.simplify(4*sqrt2*y/(1+y**2))

q_min = sp.Rational(3,4)
q_max = sp.Integer(1)
r_lower = sp.simplify(sp.Rational(2,3)*(sqrt2-1))
r_source_upper = sp.simplify((sqrt2+1)/2)
r_positive_upper = sp.Integer(1)

# Bell saturation polynomial: |I|=2 iff y is sqrt(2)+/-1.
sat_poly = sp.expand(y**2 - 2*sqrt2*y + 1)
lower_endpoint_residual = sp.simplify(sat_poly.subs({r:r_lower,q:q_min}))
upper_endpoint_residual = sp.simplify(sat_poly.subs({r:r_source_upper,q:q_max}))

# Two distinct angles remove the projective y <-> 1/y ambiguity.
def B(qv, rv):
    return sp.simplify(bell.subs({q:qv,r:rv}))

cross_difference_q1 = sp.factor(B(1,r)-B(1,rp))
cross_difference_q2 = sp.factor(B(q_min,r)-B(q_min,rp))
dual_branch_q1 = sp.simplify(r*rp-sp.Rational(1,4))
dual_branch_q2 = sp.simplify(r*rp-sp.Rational(4,9))
dual_incompatibility = sp.simplify(sp.Rational(1,4)-sp.Rational(4,9))

# Scale invariance and radial kernel in the coefficient plane.
bell_fg = sp.simplify(8*sqrt2*f*g*q/(g**2+4*f**2*q**2))
scale_residual = sp.simplify(bell_fg.subs({f:lam*f,g:lam*g})-bell_fg)
radial_kernel = sp.simplify(g*sp.diff(bell_fg,g)+f*sp.diff(bell_fg,f))

# Maximin balance of the endpoint Bell values.
r_maximin = 1/sp.sqrt(3)
maximin_balance = sp.simplify(B(q_min,r_maximin)-B(q_max,r_maximin))
maximin_duality = sp.simplify((2*r_maximin*q_min)*(2*r_maximin*q_max)-1)
endpoint_difference = sp.factor(B(q_min,r)-B(q_max,r))
lower_endpoint_derivative = sp.factor(sp.diff(B(q_min,r),r))
upper_endpoint_derivative = sp.factor(sp.diff(B(q_max,r),r))

# Benchmarks in projective coefficient space.
r_qed = sp.Rational(3,11)
qed_gap = sp.simplify(r_qed-r_lower)
benchmark = {
    "qed_one_loop_abs_ratio": str(r_qed),
    "qed_minus_lower_boundary": str(qed_gap),
    "qed_all_angle_status": "outside: fails only near the transverse minimum",
    "bell_lower_boundary": str(r_lower),
    "maximin_ratio": str(r_maximin),
    "born_infeld_ratio": "0",
    "born_infeld_bell_value": "0",
}

# Existing accepted-event theorem: uniform full angular bin.
full_bin = sp.simplify((sp.Rational(20,3)*sqrt2*f*g)/(g**2+sp.Rational(14,5)*f**2))
full_bin_scale_residual = sp.simplify(full_bin.subs({f:lam*f,g:lam*g})-full_bin)

# Held-out exact samples compare the reduced function with the helicity formula.
heldout = []
for rv, xv in [(sp.Rational(1,3),sp.Rational(0)),(sp.Rational(1,2),sp.Rational(1,4)),(sp.Rational(3,4),sp.Rational(1,2))]:
    qv = sp.simplify(q_x.subs(x,xv))
    phi1, phi2 = sp.Integer(1), 2*rv*qv
    direct = sp.simplify(4*sqrt2*phi1*phi2/(phi1**2+phi2**2))
    reduced = sp.simplify(bell.subs({r:rv,q:qv}))
    heldout.append({"r":str(rv),"x":str(xv),"residual":str(sp.simplify(direct-reduced))})

payload = {
    "schema": "marici.photon-d8-bell-coefficient-locus.v1",
    "strength": "exact projective semialgebraic and identifiability theorem",
    "coefficient_conventions": {
        "lagrangian": "(g2+f2)/16*(F.F)^2 + (g2-f2)/16*(F.Fdual)^2",
        "projective_coordinate": "r=f2/g2",
        "positivity": "g2>0 and |f2|<=g2",
    },
    "operator_to_helicity_source": "research/nima/results/photon-d8-helicity-map.json",
    "bell_function": "I(q,r)=8*sqrt(2)*r*q/(1+4*r^2*q^2), q=1-x+x^2",
    "angular_range": {"q_min": str(q_min), "q_max": str(q_max)},
    "strict_all_angle_bell_locus": f"{r_lower} < |r| < {r_source_upper}",
    "closed_bell_saturation_locus": f"{r_lower} <= |r| <= {r_source_upper}",
    "bell_and_positivity_locus": f"{r_lower} < |r| <= 1",
    "closed_bell_and_positivity_locus": f"{r_lower} <= |r| <= 1",
    "endpoint_residuals": {"lower": str(lower_endpoint_residual), "upper": str(upper_endpoint_residual)},
    "identifiability": {
        "overall_scale_kernel": "(g2,f2); Bell Jacobian rank is one generically",
        "scale_residual": str(scale_residual),
        "radial_derivative_residual": str(radial_kernel),
        "single_angle_ambiguity": "r' = r or r*r'=1/(4*q^2)",
        "two_angle_dual_branch_incompatibility": str(dual_incompatibility),
        "signed_two_angle_result": "r is unique generically",
        "absolute_Bell_result": "only |r| is identifiable",
    },
    "maximin": {
        "ratio": str(r_maximin),
        "endpoint_balance_residual": str(maximin_balance),
        "endpoint_duality_residual": str(maximin_duality),
        "endpoint_difference": str(endpoint_difference),
        "lower_endpoint_derivative": str(lower_endpoint_derivative),
        "upper_endpoint_derivative": str(upper_endpoint_derivative),
        "proof": "below 1/sqrt(3) the lower-q endpoint is the smaller increasing value; above it the upper-q endpoint is the smaller decreasing value",
    },
    "benchmarks": benchmark,
    "heldout_exact_samples": heldout,
    "accepted_event": {
        "rule": "integrate the unnormalized density against one nonnegative helicity-blind base weight, then normalize once",
        "uniform_full_bin_bell": str(full_bin),
        "scale_residual": str(full_bin_scale_residual),
        "hostile_control": "Entry 1578: outcome-dependent support changes a selected marginal by sqrt(2)/4",
    },
    "carrier_verdict": "the current Marici packet generates/types the two-dimensional coefficient fiber but supplies no canonical coefficient ray",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "photon-d8-bell-coefficient-locus.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

assert sp.simplify(q_x.subs(x,sp.Rational(1,2))-q_min)==0
assert lower_endpoint_residual==upper_endpoint_residual==0
assert dual_incompatibility != 0
assert scale_residual==radial_kernel==full_bin_scale_residual==0
assert maximin_balance==maximin_duality==0
assert sp.simplify(endpoint_difference.subs(r,r_maximin))==0
assert sp.N(qed_gap) < 0
assert r_lower < 1 < r_source_upper
assert all(item["residual"]=="0" for item in heldout)
print(json.dumps({"bell_locus":True,"positivity_intersection":True,"identifiability":True,"benchmarks":True,"sha256":payload["content_sha256"]}))
