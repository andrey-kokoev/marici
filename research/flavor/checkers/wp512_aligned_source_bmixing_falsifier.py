"""Aligned messenger completion versus the executable neutral-B instrument."""

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


wp450 = load("wp450_messenger_word_grammar.json")
wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp510 = load("wp510_common_source_total_width_closure.json")
wp511 = load("wp511_neutral_b_current_instrument.json")

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
witness = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: 55,
    b: 54,
}

# Reassemble the complete source-normalized zero-momentum flavor-current
# kernel from the three WP508 matrix resolvents and two singleton poles.
current_kernel = sp.zeros(8)
for component in wp508["heavy_gauge_poles"]["components"]:
    flavor_indices = [
        int(name[1:]) - 1 for name in component["generators"] if name.startswith("F")
    ]
    if component["size"] == 1:
        current_kernel[flavor_indices[0], flavor_indices[0]] = sp.Rational(1, 3)
        continue
    resolvent = component["flavor_current_resolvent"]
    numerator = sp.Matrix(
        [
            [sp.sympify(value, locals=symbols) for value in row]
            for row in resolvent["numerator_matrix"]
        ]
    )
    denominator = sp.sympify(resolvent["denominator"], locals=symbols)
    contact_block = (
        -numerator.subs(z, 0) / denominator.subs(z, 0)
    ).subs(witness).applyfunc(sp.factor)
    for row, global_row in enumerate(flavor_indices):
        for column, global_column in enumerate(flavor_indices):
            current_kernel[global_row, global_column] = contact_block[row, column]

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


def delta_f_two_shape(left, right):
    transition = sp.Matrix(
        [generator[left, right] for generator in generators]
    )
    return sp.factor((transition.T * current_kernel * transition)[0])


bd_shape = delta_f_two_shape(0, 2)
bs_shape = delta_f_two_shape(1, 2)
sd_shape = delta_f_two_shape(0, 1)

# The same entrance doublets supply the measured electroweak norm.  Their
# WP510 amplitudes therefore fix the common clock rather than allowing it to be
# rescaled independently after the current constraint is read.
v_phys_gev = sp.Integer(246)
w_gev = sp.factor(v_phys_gev / sp.sqrt(2 * (55**2 + 54**2)))
tree_elimination_factor = -sp.Rational(1, 2) / w_gev**2
x_d = sp.factor(tree_elimination_factor * bd_shape)
x_s = sp.factor(tree_elimination_factor * bs_shape)

wilson = Wilson(
    {
        "CVLL_bsbs": float(x_s),
        "CVRR_bsbs": float(x_s),
        "CVLR_bsbs": float(2 * x_s),
    },
    scale=160.0,
    eft="WET",
    basis="flavio",
)
delta_ms_prediction = float(flavio.np_prediction("DeltaM_s", wilson))
delta_ms_sm = float(flavio.sm_prediction("DeltaM_s"))
delta_ms_measurement = flavio.combine_measurements("DeltaM_s")
delta_ms_experiment = float(delta_ms_measurement.central_value)
experimental_sigma = float(delta_ms_measurement.standard_deviation)
theory_variance = float(
    wp511["physical_instrument"]["frozen_theory_covariance"][1][1]
)
total_sigma = (theory_variance + experimental_sigma**2) ** 0.5
total_pull = abs(delta_ms_prediction - delta_ms_experiment) / total_sigma

checks = {
    "wp450_dependency_passed": bool(wp450["passed"]),
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp510_dependency_passed": bool(wp510["passed"]),
    "wp511_dependency_passed": bool(wp511["passed"]),
    "aligned_bd_current_coefficient_vanishes": bd_shape == 0,
    "aligned_bs_current_shape_is_exact": bs_shape
    == sp.Rational(729, 17_971_525),
    "aligned_sd_shape_matches_bs_shape": sd_shape == bs_shape,
    "electroweak_calibration_fixes_common_clock": w_gev
    == 123 * sp.sqrt(11882) / 5941,
    "matched_bs_wet_coefficient_is_exact": x_s
    == -sp.Rational(81, 20_340_100),
    "source_image_on_two_b_ports_has_rank_one": bool(x_d == 0 and x_s != 0),
    "full_executable_delta_ms_prediction_is_finite": bool(
        delta_ms_prediction > 0
    ),
    "aligned_witness_is_excluded_beyond_million_sigma": bool(
        total_pull > 1_000_000
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP512",
    "source_completion": "WP450 down Yukawa restricted to a polynomial in J3, so its mass basis is aligned with the WP447 principal-SU(2) frame; the up sector may carry CKM mixing",
    "exact_current_shapes_before_tree_factor": {
        "sd": str(sd_shape),
        "bd": str(bd_shape),
        "bs": str(bs_shape),
    },
    "common_frame_calibration": {
        "v_phys_GeV": str(v_phys_gev),
        "v_phys_squared_relation": "v_phys^2=11882 w^2",
        "w_GeV": str(w_gev),
        "clock_ratio_squared": "6/5941",
    },
    "matched_wet_coordinates_GeV^-2": {
        "x_d": str(x_d),
        "x_s": str(x_s),
        "chiral_pattern": "(CVLL,CVRR,CVLR)=x_q(1,1,2)",
    },
    "executable_delta_ms_test": {
        "sm_prediction": delta_ms_sm,
        "source_prediction": delta_ms_prediction,
        "measurement": delta_ms_experiment,
        "experimental_sigma": experimental_sigma,
        "frozen_total_sigma": total_sigma,
        "absolute_pull": total_pull,
    },
    "contextual_partition": "WP511 is rank two on abstract (x_d,x_s), but the aligned source map reaches only the x_s axis and is rank one before the detector.",
    "classification": "Exact common-frame falsification of the simplest source-aligned messenger completion of WP510. It does not falsify every possible messenger orientation because WP450 leaves that orientation unselected.",
    "selector": False,
    "rigidifier": bool(bd_shape == 0 and bs_shape != 0),
    "instrument": "WP511 pinned DeltaM_s likelihood with its frozen experimental and theory covariance",
    "smallest_exact_falsifier": "The electroweak-calibrated aligned source predicts x_s=-81/20340100 GeV^-2 and DeltaM_s about 2.69e-6, while the measured value is about 1.17e-11.",
    "remaining_gate": "A source law must select a messenger orientation and coefficient trajectory that reproduces physical16 and survives the calibrated K, B_d, and B_s current instruments. Rotating the fitted Yukawas after reading those constraints is prohibited.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp512_aligned_source_bmixing_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
