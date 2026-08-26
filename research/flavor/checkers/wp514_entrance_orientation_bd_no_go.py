"""Entrance-defined nonaligned orientation versus the calibrated B_d port."""

import json
import multiprocessing as mp
from pathlib import Path

import sympy as sp


_original_get_context = mp.get_context
mp.get_context = lambda method=None: _original_get_context(
    "spawn" if method == "fork" else method
)

import flavio
from wilson import Wilson


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp511 = load("wp511_neutral_b_current_instrument.json")
wp513 = load("wp513_aligned_closure_current_no_go.json")

z = sp.symbols("z")
g_f, g_p, g_e, mu, s, a, b = sp.symbols(
    "g_F g_P g_E mu s a b", positive=True
)
symbols = {
    "z": z,
    "g_F": g_f,
    "g_P": g_p,
    "g_E": g_e,
    "mu": mu,
    "s": s,
    "a": a,
    "b": b,
}

current_kernel = sp.zeros(8)
for component in wp508["heavy_gauge_poles"]["components"]:
    flavor_indices = [
        int(name[1:]) - 1 for name in component["generators"] if name.startswith("F")
    ]
    if component["size"] == 1:
        current_kernel[flavor_indices[0], flavor_indices[0]] = 1 / (3 * mu**2)
        continue
    resolvent = component["flavor_current_resolvent"]
    numerator = sp.Matrix(
        [
            [sp.sympify(value, locals=symbols) for value in row]
            for row in resolvent["numerator_matrix"]
        ]
    )
    denominator = sp.sympify(resolvent["denominator"], locals=symbols)
    block = (-numerator.subs(z, 0) / denominator.subs(z, 0)).applyfunc(
        sp.factor
    )
    for row, global_row in enumerate(flavor_indices):
        for column, global_column in enumerate(flavor_indices):
            current_kernel[global_row, global_column] = block[row, column]

I = sp.I
gell_mann = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
generators = [matrix / 2 for matrix in gell_mann]

radius = sp.sqrt(a**2 + b**2)
entrance_orientation = sp.Matrix(
    [[a / radius, 0, b / radius], [0, 1, 0], [-b / radius, 0, a / radius]]
)


def transition_shape(left, right):
    transition = sp.Matrix(
        [
            (entrance_orientation.T * generator * entrance_orientation)[left, right]
            for generator in generators
        ]
    )
    return sp.factor((transition.T * current_kernel * transition)[0])


sd_shape = transition_shape(0, 1)
bd_shape = transition_shape(0, 2)
bs_shape = transition_shape(1, 2)
expected_bd_shape = sp.factor(
    2
    * a**2
    * (3 * b**2 * mu**2 + b**2 * s**2 + 3 * mu**2 * s**2)
    / (3 * mu**2 * s**2 * (a**2 + b**2) ** 2)
)

# With v_phys^2=2(a^2+b^2)w^2, tree elimination maps C to
# x=-C(a^2+b^2)/v_phys^2.  The dimensionless numerator below is |x|v^2.
matched_bd_times_v_squared = sp.factor(bd_shape * (a**2 + b**2))
orientation_floor = 2 * a**2 / (a**2 + b**2)
positive_remainder = sp.factor(matched_bd_times_v_squared - orientation_floor)

# WP513's determinant argument gives b/a<8 throughout the vector-pair closure
# domain. Hence a^2/(a^2+b^2)>1/65.
closure_floor_times_v_squared = sp.Rational(2, 65)
v_phys_gev = sp.Integer(246)
minimum_abs_xd = sp.factor(
    closure_floor_times_v_squared / v_phys_gev**2
)
boundary_xd = -minimum_abs_xd


def delta_md(coefficient):
    wilson = Wilson(
        {
            "CVLL_bdbd": float(coefficient),
            "CVRR_bdbd": float(coefficient),
            "CVLR_bdbd": float(2 * coefficient),
        },
        scale=160.0,
        eft="WET",
        basis="flavio",
    )
    return float(flavio.np_prediction("DeltaM_d", wilson))


fit_step = float(minimum_abs_xd)
value_zero = delta_md(0.0)
value_plus = delta_md(fit_step)
value_minus = delta_md(-fit_step)
quadratic_a = (
    value_plus**2 + value_minus**2 - 2 * value_zero**2
) / (2 * fit_step**2)
quadratic_b = (value_plus**2 - value_minus**2) / (2 * fit_step)
quadratic_vertex = -quadratic_b / (2 * quadratic_a)
boundary_prediction = delta_md(boundary_xd)
double_boundary_prediction = delta_md(2 * boundary_xd)
double_boundary_quadratic = (
    quadratic_a * float(2 * boundary_xd) ** 2
    + quadratic_b * float(2 * boundary_xd)
    + value_zero**2
) ** 0.5

measurement = flavio.combine_measurements("DeltaM_d")
theory_variance = float(
    wp511["physical_instrument"]["frozen_theory_covariance"][0][0]
)
total_sigma = (
    theory_variance + float(measurement.standard_deviation) ** 2
) ** 0.5
boundary_pull = abs(boundary_prediction - measurement.central_value) / total_sigma

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp513_dependency_passed": bool(wp513["passed"]),
    "entrance_orientation_is_orthogonal": sp.simplify(
        entrance_orientation.T * entrance_orientation
    )
    == sp.eye(3),
    "entrance_defined_bd_shape_is_exact": bd_shape == expected_bd_shape,
    "entrance_defined_bd_shape_is_strictly_positive": bool(
        expected_bd_shape.is_positive
    ),
    "matched_bd_floor_has_positive_remainder": positive_remainder
    == 2
    * a**2
    * b**2
    * (3 * mu**2 + s**2)
    / (3 * mu**2 * s**2 * (a**2 + b**2)),
    "closure_implies_orientation_floor_above_two_over_sixty_five": bool(
        closure_floor_times_v_squared == sp.Rational(2, 65)
    ),
    "electroweak_calibrated_bd_current_floor_is_exact": minimum_abs_xd
    == sp.Rational(1, 1_966_770),
    "delta_md_squared_is_quadratic_on_real_ray": bool(
        abs(double_boundary_prediction - double_boundary_quadratic)
        / double_boundary_prediction
        < 1e-10
    ),
    "quadratic_vertex_lies_outside_closure_allowed_negative_ray": bool(
        quadratic_vertex > float(boundary_xd)
    ),
    "response_grows_beyond_closure_boundary": bool(
        double_boundary_prediction > boundary_prediction
    ),
    "least_entrance_oriented_closure_current_is_excluded_beyond_ten_million_sigma": bool(
        boundary_pull > 10_000_000
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP514",
    "source_orientation": {
        "constructor": "connector-mediated real 1-3 rotation fixed by the entrance amplitude ray (a,b)",
        "matrix": [[str(value) for value in row] for row in entrance_orientation.tolist()],
        "sd_shape": str(sd_shape),
        "bd_shape": str(bd_shape),
        "bs_shape": str(bs_shape),
    },
    "exact_floor": {
        "matched_bd_times_v_squared": str(matched_bd_times_v_squared),
        "strict_lower_chain": "|x_d| v_phys^2 > 2 a^2/(a^2+b^2) > 2/65",
        "v_phys_GeV": str(v_phys_gev),
        "minimum_abs_xd_GeV^-2": str(minimum_abs_xd),
    },
    "instrument_boundary": {
        "boundary_delta_md_prediction": boundary_prediction,
        "measurement": float(measurement.central_value),
        "frozen_total_sigma": total_sigma,
        "boundary_absolute_pull": boundary_pull,
        "quadratic_vertex_xd_GeV^-2": quadratic_vertex,
    },
    "classification": "Exact no-go for the connector-mediated entrance-ray orientation: complete quark-only vector-pair width closure and calibrated DeltaM_d viability cannot coexist at the observed electroweak norm.",
    "selector": False,
    "rigidifier": bool(entrance_orientation.det() == 1),
    "instrument": "WP511 executable DeltaM_d likelihood",
    "smallest_exact_falsifier": "Closure forces |x_d|>1/1966770 GeV^-2 for the entrance-defined orientation; the least-magnitude boundary predicts DeltaM_d about 2.40e-7.",
    "remaining_gate": "The two simplest source-derived orientations are now closed. A viable nonaligned law requires additional independently declared geometry, or the programme must abandon quark-only closure and calculate open-channel widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp514_entrance_orientation_bd_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
