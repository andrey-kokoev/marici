import json
import sympy as sp


F, Fp, Fpp, a, g, gp = sp.symbols("F Fp Fpp a g gp")
I = sp.I
Hplus = F + I * a * Fp
Hminus = F - I * a * Fp
C = sp.expand(Hplus - Hminus)
T = sp.expand(Hplus + Hminus)

Fnew = g * F
Fpnew = gp * F + g * Fp
Cnew = sp.expand(2 * I * a * Fpnew)
W = sp.expand(2 * I * a * (F * Fpp - Fp**2))

checks = {
    "symmetric_channel_is_value": sp.expand(T - 2 * F) == 0,
    "antisymmetric_channel_is_conormal": sp.expand(C - 2 * I * a * Fp) == 0,
    "zero_lands_on_antisymmetric_line": sp.expand(T.subs(F, 0)) == 0
    and sp.expand(C.subs(F, 0) - 2 * I * a * Fp) == 0,
    "multiplicative_covariance_at_zero": sp.expand(Cnew.subs(F, 0) - g * C.subs(F, 0)) == 0,
    "simple_zero_wronskian": sp.expand(W.subs(F, 0) + 2 * I * a * Fp**2) == 0,
    "reciprocal_conormal_is_odd": sp.expand(C.subs(Fp, -Fp) + C) == 0,
    "quadratic_current_is_reciprocal_even": sp.expand(
        C.subs(Fp, -Fp) ** 2 - C**2
    ) == 0,
}

result = {
    "schema": "marici.grothendieck.scalar_zero_conormal_adapter.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "adapter": "F=0 maps to C=H_+-H_-=2 i a F'",
    "covariance": "C(gF)|_{F=0}=g C(F)|_{F=0}",
    "orientation_loss": "C changes sign under reciprocal reflection, but C^2 and |C|^2 do not",
}

print(json.dumps(result, indent=2, sort_keys=True))
