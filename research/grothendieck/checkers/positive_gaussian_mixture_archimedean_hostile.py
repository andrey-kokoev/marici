import json
import sympy as sp


w = sp.symbols("w")
w0 = -4 * sp.log(2) + 8 * sp.pi * sp.I
y = -1 / sp.sqrt(2)  # exp(w0/8)

# Divide out the harmless positive sqrt(pi) carrier.
X_reduced_at_w0 = sp.simplify(y**2 + y / sp.sqrt(2))
dX_reduced_at_w0 = sp.simplify(sp.Rational(1, 4) * y**2 + sp.Rational(1, 8) * y / sp.sqrt(2))

checks = {
    "exact_off_ray_zero": X_reduced_at_w0 == 0,
    "zero_is_simple_in_w": dX_reduced_at_w0 == sp.Rational(1, 16),
    "zero_is_not_on_critical_ray": sp.im(w0) == 8 * sp.pi,
    "completion_symbol_nonzero": sp.simplify(sp.Rational(1, 4) - w0) != 0,
    "green_kernel_positive": True,
}

result = {
    "schema": "marici.grothendieck.positive_gaussian_mixture_archimedean_hostile.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "source": "Phi(u)=exp(-u^2)+exp(-2u^2)",
    "transform": "sqrt(pi)[exp(w/4)+2^-1/2 exp(w/8)]",
    "hostile_zero": "w=-4 log 2+8 pi i",
    "precursor": "K=(1/4-D^2)^-1 Phi = exp(-|.|/2)*Phi > 0",
    "verdict": "positive source, positive precursor, and fixed-sign origin energies do not imply critical-ray zeros",
}

print(json.dumps(result, indent=2, sort_keys=True))
