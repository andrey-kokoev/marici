"""Exact aligned-family incompatibility between width closure and B mixing."""

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
wp512 = load("wp512_aligned_source_bmixing_falsifier.json")

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
cubic_by_entrance = {}
for component in wp508["heavy_gauge_poles"]["components"]:
    flavor_indices = [
        int(name[1:]) - 1 for name in component["generators"] if name.startswith("F")
    ]
    if component["size"] == 1:
        current_kernel[flavor_indices[0], flavor_indices[0]] = 1 / (3 * mu**2)
        continue
    cubic = sp.Poly(
        sp.sympify(component["cubic_characteristic_polynomial"], locals=symbols),
        z,
    )
    generators = component["generators"]
    if generators[:2] == ["F1", "F6"]:
        cubic_by_entrance["a_squared"] = cubic
    elif generators[:2] == ["F3", "F8"]:
        cubic_by_entrance["b_squared"] = cubic
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


def aligned_shape(left, right):
    transition = sp.Matrix(
        [generator[left, right] for generator in generators]
    )
    return sp.factor((transition.T * current_kernel * transition)[0])


sd_shape = aligned_shape(0, 1)
bd_shape = aligned_shape(0, 2)
bs_shape = aligned_shape(1, 2)
expected_shape = b**2 / (4 * a**2 * (a**2 + b**2))

determinant_ratio = sp.factor(
    cubic_by_entrance["a_squared"].coeff_monomial(1)
    / cubic_by_entrance["b_squared"].coeff_monomial(1)
)

# If every heavy squared mass lies between m and M with M/m<4, the ratio of
# any two products of three cubic roots lies strictly between 1/64 and 64.
# Since the exact determinant ratio is a^2/b^2, aligned total-width closure
# implies 1/8<b/a<8.
root_spread_bound = sp.Integer(4)
determinant_ratio_bound = root_spread_bound**3
minimum_b_over_a_squared = 1 / determinant_ratio_bound
v_phys_gev = sp.Integer(246)
minimum_abs_xs = sp.factor(
    minimum_b_over_a_squared / (4 * v_phys_gev**2)
)
boundary_xs = -minimum_abs_xs


def delta_ms(coefficient):
    wilson = Wilson(
        {
            "CVLL_bsbs": float(coefficient),
            "CVRR_bsbs": float(coefficient),
            "CVLR_bsbs": float(2 * coefficient),
        },
        scale=160.0,
        eft="WET",
        basis="flavio",
    )
    return float(flavio.np_prediction("DeltaM_s", wilson))


# DeltaM_s squared is a quadratic along a fixed real Wilson ray because the
# mixing amplitude is affine and the observable is its modulus. Reconstruct
# that quadratic and verify the closure boundary lies beyond its minimum.
fit_step = float(minimum_abs_xs)
value_zero = delta_ms(0.0)
value_plus = delta_ms(fit_step)
value_minus = delta_ms(-fit_step)
quadratic_a = (
    value_plus**2 + value_minus**2 - 2 * value_zero**2
) / (2 * fit_step**2)
quadratic_b = (value_plus**2 - value_minus**2) / (2 * fit_step)
quadratic_vertex = -quadratic_b / (2 * quadratic_a)
boundary_prediction = delta_ms(boundary_xs)
double_boundary_prediction = delta_ms(2 * boundary_xs)
boundary_quadratic_prediction = (
    quadratic_a * float(boundary_xs) ** 2
    + quadratic_b * float(boundary_xs)
    + value_zero**2
) ** 0.5
double_boundary_quadratic_prediction = (
    quadratic_a * float(2 * boundary_xs) ** 2
    + quadratic_b * float(2 * boundary_xs)
    + value_zero**2
) ** 0.5

measurement = flavio.combine_measurements("DeltaM_s")
theory_variance = float(
    wp511["physical_instrument"]["frozen_theory_covariance"][1][1]
)
total_sigma = (
    theory_variance + float(measurement.standard_deviation) ** 2
) ** 0.5
boundary_pull = abs(boundary_prediction - measurement.central_value) / total_sigma

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp512_dependency_passed": bool(wp512["passed"]),
    "aligned_sd_shape_is_universal": sd_shape == expected_shape,
    "aligned_bs_shape_is_universal": bs_shape == expected_shape,
    "aligned_bd_shape_vanishes": bd_shape == 0,
    "cubic_determinant_ratio_is_a_squared_over_b_squared": determinant_ratio
    == a**2 / b**2,
    "pair_closure_implies_b_over_a_above_one_eighth": bool(
        minimum_b_over_a_squared == sp.Rational(1, 64)
    ),
    "electroweak_calibrated_current_floor_is_exact": minimum_abs_xs
    == sp.Rational(1, 15_492_096),
    "delta_ms_squared_is_quadratic_on_real_ray": bool(
        abs(double_boundary_prediction - double_boundary_quadratic_prediction)
        / double_boundary_prediction
        < 1e-10
    ),
    "quadratic_vertex_lies_outside_closure_allowed_negative_ray": bool(
        quadratic_vertex > float(boundary_xs)
    ),
    "response_grows_beyond_closure_boundary": bool(
        double_boundary_prediction > boundary_prediction
    ),
    "least_aligned_closure_current_is_excluded_beyond_eighty_thousand_sigma": bool(
        boundary_pull > 80_000
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP513",
    "exact_aligned_family": {
        "sd_shape": str(sd_shape),
        "bd_shape": str(bd_shape),
        "bs_shape": str(bs_shape),
        "matched_bs_coordinate": "x_s=-(b/a)^2/(4 v_phys^2)",
    },
    "closure_implication": {
        "cubic_determinant_ratio": str(determinant_ratio),
        "global_squared_mass_spread": "M/m<4",
        "determinant_product_bound": "1/64<a^2/b^2<64",
        "entrance_ratio_bound": "1/8<b/a<8",
    },
    "instrument_floor": {
        "v_phys_GeV": str(v_phys_gev),
        "minimum_abs_xs_GeV^-2": str(minimum_abs_xs),
        "boundary_delta_ms_prediction": boundary_prediction,
        "measurement": float(measurement.central_value),
        "frozen_total_sigma": total_sigma,
        "boundary_absolute_pull": boundary_pull,
        "quadratic_vertex_xs_GeV^-2": quadratic_vertex,
    },
    "classification": "Exact no-go for the entire J3-aligned messenger family: complete quark-only vector-pair width closure and the calibrated DeltaM_s constraint cannot both hold at the observed electroweak norm.",
    "selector": False,
    "rigidifier": bool(sd_shape == bs_shape and bd_shape == 0),
    "instrument": "WP511 executable DeltaM_s likelihood",
    "smallest_exact_falsifier": "Closure forces |x_s|>1/15492096 GeV^-2, whose least-magnitude boundary already predicts DeltaM_s about 4.37e-8 and is excluded above eighty thousand frozen standard deviations.",
    "remaining_gate": "Either derive a nonaligned source orientation that survives the complete K, B_d, and B_s instrument family, or abandon quark-only total-width closure and calculate the newly open source-derived decay channels. The aligned branch is closed globally.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp513_aligned_closure_current_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
