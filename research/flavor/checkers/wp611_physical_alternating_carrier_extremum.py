"""Exact WP611 physical alternating carrier and coefficient-free extrema."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
ensemble = json.loads((ROOT / "results" / "wp20_valley_audit.json").read_text())
ensemble_j = [abs(float(record["J"])) for record in ensemble["records"]]

omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
fourier = sp.Matrix(
    [[omega ** (row * column) / sp.sqrt(3) for column in range(3)] for row in range(3)]
)
up_projectors = [
    sp.diag(*[1 if entry == index else 0 for entry in range(3)])
    for index in range(3)
]
down_projectors = [
    sp.simplify(fourier[:, index] * fourier[:, index].conjugate().T)
    for index in range(3)
]
projector_quartet = sp.simplify(
    sp.im(
        sp.trace(
            up_projectors[0]
            * down_projectors[0]
            * up_projectors[1]
            * down_projectors[1]
        )
    )
)

forward = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
permutation_down_projectors = [
    forward[:, index] * forward[:, index].T for index in range(3)
]
permutation_quartet = sp.simplify(
    sp.im(
        sp.trace(
            up_projectors[0]
            * permutation_down_projectors[0]
            * up_projectors[1]
            * permutation_down_projectors[1]
        )
    )
)

# Standard-parametrization maximum. The first two sine-cosine products each
# have square at most 1/4. For x=s13^2, the remaining squared factor is
# x*(1-x)^2, maximized at x=1/3 with value 4/27.
x = sp.symbols("x", real=True)
third_factor_squared = x * (1 - x) ** 2
derivative = sp.factor(sp.diff(third_factor_squared, x))
third_at_stationary = sp.simplify(third_factor_squared.subs(x, sp.Rational(1, 3)))
j_squared_maximum = sp.simplify(sp.Rational(1, 4) ** 2 * third_at_stationary)

fourier_j_squared = sp.simplify(projector_quartet**2)
observed_max = max(ensemble_j)
observed_min = min(ensemble_j)

c = sp.symbols("c", positive=True, real=True)
j_squared = sp.symbols("J2", nonnegative=True, real=True)
interior_potential = (j_squared - c) ** 2

checks = {
    "projector_quartet_equals_fourier_j": projector_quartet
    == sp.sqrt(3) / 18,
    "projector_quartet_vanishes_on_permutation_support": permutation_quartet
    == 0,
    "third_factor_stationary_polynomial_is_exact": derivative
    == (x - 1) * (3 * x - 1),
    "third_factor_maximum_is_four_over_twenty_seven": third_at_stationary
    == sp.Rational(4, 27),
    "universal_j_squared_maximum_is_one_over_108": j_squared_maximum
    == sp.Rational(1, 108),
    "fourier_point_saturates_universal_maximum": fourier_j_squared
    == j_squared_maximum,
    "complete_ensemble_is_nonzero": len(ensemble_j) == 1210
    and observed_min > 0,
    "complete_ensemble_is_strictly_nonmaximal": observed_max**2
    < float(j_squared_maximum),
    "ensemble_is_far_below_maximal_cp": observed_max < 1e-3,
    "interior_selector_location_is_inserted_scale": sp.solve(
        sp.diff(interior_potential, j_squared), j_squared
    )
    == [c],
}

if not all(checks.values()):
    raise SystemExit(f"WP611 check failed: {checks}")

result = {
    "work_package": "WP611",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "state_domain": "nondegenerate physical16 Yukawa Gram pairs with ordered spectral projectors",
    "physical_alternating_carrier": "Im Tr(P_u0 P_d0 P_u1 P_d1)=J up to the fixed ordered-index convention",
    "descent": "the projector quartet is invariant under common weak-basis conjugation and is measured through CP-sensitive charged-current amplitudes",
    "permutation_support": "J=0 on every exact permutation overlap, so the carrier cannot orient WP609's matching locus",
    "coefficient_free_extrema": ["minimize J^2 selects J=0", "maximize J^2 selects J^2=1/108"],
    "ensemble_interval": {"sheets": 1210, "min_abs_J": observed_min, "max_abs_J": observed_max},
    "classification": "faithful alternating readout and experimental probe; neither the zero nor maximal coefficient-free extremum selects observed flavor",
    "smallest_exact_falsifier": "permutation support makes the alternating quartet identically zero",
    "source_selector_gate": "an interior potential such as (J^2-c)^2 selects only after a dimensionless c is independently derived; choosing c from the fitted ensemble is target encoding",
    "instrument": "charged-current CP asymmetries measure J; any new alternating mediator channel must be separately resolved rather than inferred from the same record",
}

out = ROOT / "results" / "wp611_physical_alternating_carrier_extremum.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
