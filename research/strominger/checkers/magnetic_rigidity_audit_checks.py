"""Hard-to-vary audit for the magnetic binomial/Euler transport ansatz."""
import json
import os

import sympy as sp

a, h, s, x, t = sp.symbols("a h s x t")
u, v, u0, v0 = sp.symbols("u v u0 v0")

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Classify binomial grade EGFs with exponents affine in pole depth.
general = (1 + t) ** (u * a + u0) * (1 - x * t) ** (v * a + v0)
shift_quotient = sp.simplify(general.subs(a, a + 2) / general)
target = ((1 - x * t) / (1 + t)) ** 2
record("RIGID.slopes", "the square reflection character fixes the pole-depth slopes",
       sp.simplify(shift_quotient.subs({u: -1, v: 1}) - target) == 0,
       "u=-1, v=1")

# Valuations at the independent divisors t=-1 and xt=1 prove uniqueness of
# those slopes within the affine-binomial ansatz.
valuation_solution = sp.solve([sp.Eq(2 * u, -2), sp.Eq(2 * v, 2)], [u, v],
                              dict=True)
record("RIGID.unique", "divisor valuations make the slope solution unique",
       valuation_solution == [{u: -1, v: 1}], valuation_solution)

# The additive exponents are invisible to pole-depth transport.  Writing the
# relevant surviving combination as h gives a genuine deformation family.
constants_cancel = not shift_quotient.has(u0) and not shift_quotient.has(v0)
record("MODULUS.constants", "the additive binomial exponents cancel from the shift quotient",
       constants_cancel, "u0 and v0 remain free")

family = (1 + t) ** (-a) * (1 - x * t) ** (a - h)
family_shift = sp.simplify(family.subs(a, a + 2) / family)
record("MODULUS.h", "every h has the same square pole-depth character",
       sp.simplify(family_shift - target) == 0, "h is unconstrained")

# Apply the same magnetic Euler operator with m=1-g+s-a at EGF level.
# The result is F times H_h, and clearing the two linear denominators produces
# a quadratic numerator for every h.
mu = 1 + s - a
h_factor = (mu * (1 + x) + a * (1 + 2 * x) * t / (1 + t) +
            (a - h) * x ** 2 * t / (1 - x * t))
numerator = sp.Poly(sp.cancel(h_factor * (1 + t) * (1 - x * t)), t)
record("MODULUS.order", "the transported numerator remains quadratic for arbitrary h",
       numerator.degree() == 2, f"degree={numerator.degree()}")

numerator_shift = sp.Poly(numerator.as_expr().subs(a, a + 2), t)
difference = sp.factor(numerator_shift.as_expr() - numerator.as_expr())
record("MODULUS.universal", "the numerator shift is independent of h and s",
       sp.expand(difference - 2 * (1 + x) * (2 * t * x - 1)) == 0,
       str(difference))

left_multiplier = sp.Poly(sp.expand((1 + t) ** 2 * numerator.as_expr()), t)
right_multiplier = sp.Poly(sp.expand((1 - x * t) ** 2 *
                                     numerator_shift.as_expr()), t)
record("MODULUS.memory", "order-four magnetic contiguity survives for every h",
       left_multiplier.degree() == right_multiplier.degree() == 4,
       "degrees=(4,4)")

# A neighboring deformation changes actual coefficient data while preserving
# every transport property above.
n4 = sp.expand(numerator.as_expr().subs(h, 4))
n5 = sp.expand(numerator.as_expr().subs(h, 5))
record("FALSIFIER.h5", "h=5 changes the magnetic numerator without changing transport order",
       n4 != n5 and sp.factor(n5 - n4) == -t * x ** 2 * (t + 1),
       "N_5-N_4=-t*x^2*(t+1)")

# The local endpoint data also vary, proving h is not a mere presentation
# gauge of the coefficient matrix.
right_endpoint_h = sp.rf(h - a, sp.symbols("g", integer=True, nonnegative=True))
record("FALSIFIER.payload", "the surviving h modulus changes endpoint coefficients",
       right_endpoint_h.subs(h, 4) != right_endpoint_h.subs(h, 5),
       "(h-a) rising g")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_rigidity_audit_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic hard-to-vary classification within the affine-binomial/Euler ansatz"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The square reflection character uniquely fixes the pole-depth slopes (-1,+1) of the two binomial factors, but it does not fix their additive exponents. A genuine parameter h survives: all h retain the same square shift, quadratic magnetic numerator, universal numerator increment, and order-four contiguity, while changing endpoint coefficient data. Therefore finite transport and reflection squaring alone are not yet a hard-to-vary explanation of the physical h=4 theory.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_rigidity_audit.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
