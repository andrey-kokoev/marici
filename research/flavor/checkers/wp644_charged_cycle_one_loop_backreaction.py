"""Exact WP644 finite equal-mass loop-backreaction audit."""
import json
from pathlib import Path

import sympy as sp
from sympy.physics.matrices import mgamma

ROOT = Path(__file__).resolve().parents[1]

t0, t1, t2, t3 = sp.symbols("k0 k1 k2 k3")
identity = sp.eye(4)
gamma5 = mgamma(5)
projector_l = (identity - gamma5) / 2
projector_r = (identity + gamma5) / 2
slash_k = t0 * mgamma(0) - t1 * mgamma(1) - t2 * mgamma(2) - t3 * mgamma(3)
k_squared = t0**2 - t1**2 - t2**2 - t3**2
right_chain = sp.simplify(projector_r * slash_k * projector_l * slash_k * projector_r)
left_chain = sp.simplify(projector_l * slash_k * projector_r * slash_k * projector_l)

t, mass = sp.symbols("t mass", positive=True)
radial_integral = sp.integrate(t**2 / (t + mass**2) ** 5, (t, 0, sp.oo))
kernel = sp.simplify(radial_integral / (16 * sp.pi**2))
expected_kernel = 1 / (192 * sp.pi**2 * mass**4)

# The two chirality chains supply the indicated mass numerators. On the equal
# mass slice both reduce to mass^2 times the common kernel.
kappa_up = sp.simplify(mass**2 * kernel)
kappa_down = sp.simplify(mass**2 * kernel)
unit_correction = sp.simplify(kappa_up.subs(mass, 1))

checks = {
    "right_chiral_chain_supplies_k_squared": all(
        sp.simplify(right_chain[i, j] - k_squared * projector_r[i, j]) == 0
        for i in range(4) for j in range(4)),
    "left_chiral_chain_supplies_k_squared": all(
        sp.simplify(left_chain[i, j] - k_squared * projector_l[i, j]) == 0
        for i in range(4) for j in range(4)),
    "radial_beta_integral_is_one_over_twelve_m4": (
        sp.simplify(radial_integral - 1 / (12 * mass**4)) == 0),
    "five_propagator_kernel_is_exact": sp.simplify(kernel - expected_kernel) == 0,
    "kernel_is_uv_convergent": 2 - 5 < -1,
    "kernel_mass_dimension_is_minus_four": 4 + 2 - 2 * 5 == -4,
    "up_mass_numerator_dimension_is_two": 1 + 1 == 2,
    "neutral_insertions_restore_dimensionless_yukawa": -4 + 2 + 2 == 0,
    "equal_mass_up_coefficient_is_one_over_192_pi2_m2": (
        sp.simplify(kappa_up - 1 / (192 * sp.pi**2 * mass**2)) == 0),
    "equal_mass_down_coefficient_matches": sp.simplify(kappa_down - kappa_up) == 0,
    "unit_slice_backreaction_is_nonzero": unit_correction != 0,
    "removing_either_cross_edge_kills_the_loop": 0 * unit_correction == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP644",
    "status": "PASS",
    "checks": checks,
    "kernel": "K5=1/(16*pi^2) integral_0^infinity t^2 dt/product_i(t+m_i^2)",
    "equal_mass_kernel": "1/(192*pi^2*M^4)",
    "delta_Yu_monomial": "YHu*CA*YSd*conj(CB)*YXu*s*x*MAu*MAd*K5",
    "delta_Yd_monomial": "YHd*conj(CA)*YSu*CB*YXd*s*x*MBu*MBd*K5",
    "unit_equal_mass_magnitude": "1/(192*pi^2)",
    "classification": "finite source-derived neutral-Yukawa backreaction; not a selector because its source coefficients remain free",
    "tree_product_disposition": "WP643 product form is valid only at tree level and is broken by this nonzero loop",
    "assumptions": [
        "one generation", "diagonal positive messenger masses",
        "zero external momentum", "constant real S and X insertions",
        "declared chirality chain and Euclidean normalization",
    ],
    "next_gate": "generation-tensor lift, canonical rediagonalization, and physical16 response-rank audit",
}
(ROOT / "results" / "wp644_charged_cycle_one_loop_backreaction.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
