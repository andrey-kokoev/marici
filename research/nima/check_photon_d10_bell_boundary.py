"""Exact dimension-ten deformation of the transverse photon Bell boundary."""

import hashlib
import json
from pathlib import Path

import sympy as sp

s, a, b, h, r, p = sp.symbols("s a b h r p", real=True)
sqrt2 = sp.sqrt(2)

# Ratios are a=g3/g2, b=f3/g2, h=h3/g2, r=f2/g2.  At theta=pi/2,
# t=u=-s/2, hence (s^2+t^2+u^2)/s^2=3/2 and stu/s^3=1/4.
z = sp.simplify((sp.Rational(3, 2) * r + sp.Rational(1, 4) * b * s) / (1 + a * s))
c = sp.simplify(sp.Rational(1, 4) * h * s / (1 + a * s))
bell = sp.simplify(4 * sqrt2 * z / (1 + z**2 + 2 * c**2))

# The lower positive Bell boundary solves z=sqrt(2)-sqrt(1-2c^2).
z_lower = sp.simplify(sqrt2 - sp.sqrt(1 - 2 * c**2))
r_lower = sp.simplify(sp.Rational(2, 3) * ((1 + a * s) * z_lower - sp.Rational(1, 4) * b * s))
r0 = sp.Rational(2, 3) * (sqrt2 - 1)
linear = sp.simplify(sp.diff(r_lower, s).subs(s, 0))
quadratic = sp.simplify(sp.diff(r_lower, s, 2).subs(s, 0) / 2)

# Direct substitution certifies that this is the exact Bell-saturation branch.
saturation_residual = sp.simplify(
    bell.subs(r, r_lower) - 2
)

# Full angular audit.  Put p=x(1-x), so 0<=p<=1/4 and
# (s^2+t^2+u^2)/s^2=2(1-p), stu/s^3=p.
A = 1 + a * s
k = h * s / A
D = 1 - 2 * k**2 * p**2
L = sqrt2 - sp.sqrt(D)
r_angular = sp.simplify((A * L - b * s * p) / (2 * (1 - p)))
angular_derivative_numerator = sp.simplify(2 * (1 - p) ** 2 * sp.diff(r_angular, p))
angular_derivative_certificate = sp.simplify(
    A * (L + 2 * k**2 * p * (1 - p) / sp.sqrt(D)) - b * s
)
certificate_residual = sp.simplify(angular_derivative_numerator - angular_derivative_certificate)
# The bracket B=L+(1-p)L' is increasing because B'=(1-p)L''.
bracket = sp.simplify(L + 2 * k**2 * p * (1 - p) / sp.sqrt(D))
bracket_derivative = sp.simplify(sp.diff(bracket, p))
bracket_derivative_expected = sp.simplify(2 * k**2 * (1 - p) / D ** sp.Rational(3, 2))

payload = {
    "schema": "marici.photon-d10-bell-boundary.v1",
    "strength": "exact transverse dimension-ten Bell-boundary theorem",
    "source_basis": {
        "Phi1": "g2*s^2+g3*s^3",
        "Phi2": "f2*(s^2+t^2+u^2)+f3*s*t*u",
        "Phi5": "h3*s*t*u",
        "ratios": "a=g3/g2, b=f3/g2, h=h3/g2, r=f2/g2",
    },
    "transverse": {
        "Phi2_over_Phi1": str(z),
        "Phi5_over_Phi1": str(c),
        "bell": str(bell),
        "exact_lower_boundary": str(r_lower),
        "saturation_residual": str(saturation_residual),
    },
    "small_s_expansion": {
        "dimension_eight_boundary": str(r0),
        "linear_coefficient": str(linear),
        "quadratic_coefficient": str(quadratic),
        "linear_controlling_combination": "(2/3)*(sqrt(2)-1)*(g3/g2)-(1/6)*(f3/g2)",
        "h3_linear_coefficient": "0",
        "h3_first_contribution": "(h3/g2)^2/24 at order s^2",
    },
    "all_angle_audit": {
        "angular_coordinate": "p=x*(1-x) in [0,1/4]",
        "exact_lower_threshold": str(r_angular),
        "derivative_numerator": str(angular_derivative_certificate),
        "bracket_derivative": str(bracket_derivative),
        "sufficient_domain": "1+a*s>0; 1-2*(h*s*p/(1+a*s))^2>0 on [0,1/4]; b*s<(1+a*s)*(sqrt(2)-1)",
        "verdict": "On this explicit EFT-validity domain the angular threshold is strictly increasing in p, so its maximum is transverse and the displayed transverse boundary is the all-angle lower boundary.",
    },
    "typing_verdict": "The first finite-energy motion of the Bell boundary is an off-diagonal comparison of the g3 and f3 helicity sectors. The mixed-helicity h3 sector enters only quadratically and cannot control the infinitesimal direction.",
    "scope": "The exact all-angle promotion holds on the explicit regularity and monotonicity domain stated in all_angle_audit.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "photon-d10-bell-boundary.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

assert saturation_residual == 0
assert sp.simplify(linear - (sp.Rational(2, 3) * (sqrt2 - 1) * a - b / 6)) == 0
assert sp.simplify(quadratic - h**2 / 24) == 0
assert sp.diff(linear, h) == 0
assert certificate_residual == 0
assert sp.simplify(bracket_derivative - bracket_derivative_expected) == 0
print(json.dumps({"saturation": True, "linear_typing": True, "mixed_helicity_quadratic": True, "all_angle_certificate": True, "sha256": payload["content_sha256"]}))
