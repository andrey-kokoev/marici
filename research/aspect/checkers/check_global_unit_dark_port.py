import json

import sympy as sp


r, phi = sp.symbols("r phi", positive=True, real=True)
U = r * sp.exp(sp.I * phi)
dark_intensity = sp.simplify(sp.expand_complex((1 - U) * (1 - sp.conjugate(U))))
bright_max = (1 + r) ** 2
minimum = sp.simplify(dark_intensity.subs(phi, 0))
extinction = sp.simplify(minimum / bright_max)

u1 = sp.exp(sp.I * sp.Rational(2, 7))
u2 = sp.exp(-sp.I * sp.Rational(2, 7))

checks = {
    "local_units_are_nonzero": sp.simplify(u1 * u2) == 1,
    "global_dark_port_can_vanish": sp.simplify(1 - u1 * u2) == 0,
    "intensity_formula": sp.simplify(
        dark_intensity - (1 + r**2 - 2 * r * sp.cos(phi))
    )
    == 0,
    "phase_optimized_minimum": sp.simplify(minimum - (1 - r) ** 2) == 0,
    "normalized_extinction_bound": sp.simplify(
        extinction - ((1 - r) / (1 + r)) ** 2
    )
    == 0,
    "perfect_extinction_requires_unit_modulus": sp.solve(
        sp.Eq(minimum, 0), r
    )
    == [1],
}

result = {
    "schema": "marici.aspect.global-unit-dark-port.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "dark_intensity": str(dark_intensity),
    "minimum_extinction_ratio": str(extinction),
    "interpretation": (
        "A global section can vanish by coherent phase closure while every "
        "local comparison remains invertible."
    ),
}

print(json.dumps(result, indent=2))
