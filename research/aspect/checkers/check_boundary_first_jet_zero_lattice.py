import json
from pathlib import Path

import mpmath as mp
import sympy as sp


u, L, z, tau, f = sp.symbols("u L z tau f", positive=True, real=True)
J = 2 * f * sp.Integral(sp.exp(-u / 2) * sp.sinh(z * u), (u, 0, L))
Q = 2 * f * sp.exp(-L / 2) * sp.sinh(z * L)
seam_Q = sp.simplify(Q.subs(z, sp.I * tau))
n = sp.symbols("n", integer=True, positive=True)

primes = [2, 3, 5, 7, 11]
zero_residuals = []
simple_derivatives = []
for p in primes:
    length = mp.log(p)
    for k in range(1, 9):
        frequency = k * mp.pi / length
        zero_residuals.append(abs(mp.exp(-length / 2) * mp.sin(frequency * length)))
        simple_derivatives.append(abs(length * mp.exp(-length / 2) * mp.cos(frequency * length)))

checks = {
    "endpoint_current_is_cutoff_derivative": sp.simplify(sp.diff(J, L) - Q) == 0,
    "seam_first_jet_is_sine_quadrature": sp.simplify(
        seam_Q - 2 * sp.I * f * sp.exp(-L / 2) * sp.sin(tau * L)
    ) == 0,
    "exact_symbolic_zero_lattice": sp.simplify(seam_Q.subs(tau, n * sp.pi / L)) == 0,
    "prime_resolved_zero_residuals": max(zero_residuals) < mp.mpf("1e-12"),
    "prime_resolved_zeros_are_simple": min(simple_derivatives) > mp.mpf("1e-6"),
    "first_jet_is_reciprocal_odd": sp.simplify(Q.subs(z, -z) + Q) == 0,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "primes": primes,
    "zeros_checked_per_prime": 8,
    "maximum_zero_residual": float(max(zero_residuals)),
    "minimum_zero_slope": float(min(simple_derivatives)),
    "predicted_spacing": "pi/log(p)",
}
out = Path(__file__).resolve().parents[1] / "results" / "boundary_first_jet_zero_lattice.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
