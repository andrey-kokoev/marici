"""Executable pinned-likelihood audit for the WP453 real kaon-current ray."""

import json
import multiprocessing as mp
from pathlib import Path


# flavio 2.7.0 requests the POSIX-only `fork` context at import time. Mapping it
# to Windows `spawn` changes only worker creation; this checker uses no workers.
_original_get_context = mp.get_context
mp.get_context = lambda method=None: _original_get_context(
    "spawn" if method == "fork" else method
)

import flavio
from wilson import Wilson


root = Path(__file__).resolve().parents[1]
wp453 = json.loads(
    (root / "results" / "wp453_current_orientation_fiber.json").read_text(
        encoding="utf-8"
    )
)
wp455 = json.loads(
    (root / "results" / "wp455_correlated_kaon_response_constructor.json").read_text(
        encoding="utf-8"
    )
)
wp458 = json.loads(
    (root / "results" / "wp458_two_axis_scale_selector_audit.json").read_text(
        encoding="utf-8"
    )
)

registered_kaon_mixing = sorted(
    name
    for name in flavio.Observable.instances
    if "eps_K" in name or "DeltaM_K" in name
)
matching_measurements = sorted(
    name
    for name, measurement in flavio.Measurement.instances.items()
    if any(
        "eps_K" in str(parameter) or "DeltaM_K" in str(parameter)
        for parameter in measurement.all_parameters
    )
)
measurement = flavio.combine_measurements("eps_K")

probe = 1e-15
scale_gev = 160.0
real_wc = Wilson(
    {
        "CVLL_sdsd": probe,
        "CVRR_sdsd": probe,
        "CVLR_sdsd": 2 * probe,
    },
    scale=scale_gev,
    eft="WET",
    basis="flavio",
)
imaginary_wc = Wilson(
    {
        "CVLL_sdsd": 1j * probe,
        "CVRR_sdsd": 1j * probe,
        "CVLR_sdsd": 2j * probe,
    },
    scale=scale_gev,
    eft="WET",
    basis="flavio",
)

sm_prediction = flavio.sm_prediction("eps_K")
real_prediction = flavio.np_prediction("eps_K", real_wc)
imaginary_prediction = flavio.np_prediction("eps_K", imaginary_wc)

checks = {
    "wp453_dependency_passed": wp453["passed"],
    "wp455_dependency_passed": wp455["passed"],
    "wp458_dependency_passed": wp458["passed"],
    "flavio_version_is_pinned": flavio.__version__ == "2.7.0",
    "only_eps_K_is_registered_for_kaon_mixing": registered_kaon_mixing
    == ["eps_K"],
    "bundled_measurement_is_pdg_kaon_cpv": matching_measurements
    == ["PDG kaon CPV"],
    "measurement_central_value_exact": measurement.central_value
    == 0.0022280000000000004,
    "measurement_standard_deviation_exact": measurement.standard_deviation
    == 1.1e-05,
    "wp453_hostile_coefficient_is_real": "I"
    not in wp453["deltaF2_current_coefficients_before_common_factor"]["rotated_12"],
    "real_correlated_ray_is_in_eps_K_kernel": real_prediction == sm_prediction,
    "imaginary_correlated_ray_is_detected": imaginary_prediction != sm_prediction,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP459",
    "runtime": {
        "python": "3.12",
        "flavio": flavio.__version__,
        "particle": "0.25.4",
        "windows_process_context_shim": "fork request mapped to spawn; no worker is used",
    },
    "registered_kaon_mixing_observables": registered_kaon_mixing,
    "matching_measurements": matching_measurements,
    "eps_K_measurement": {
        "central_value": measurement.central_value,
        "standard_deviation": measurement.standard_deviation,
    },
    "probe": {
        "scale_GeV": scale_gev,
        "coefficient_GeV^-2": probe,
        "real_pattern": [1, 1, 2],
        "imaginary_pattern": ["I", "I", "2 I"],
    },
    "predictions": {
        "SM": sm_prediction,
        "real_correlated_ray": real_prediction,
        "imaginary_correlated_ray": imaginary_prediction,
    },
    "contextual_partition": "The executable eps_K likelihood collapses the real correlated source ray but separates its CP-odd counterpart.",
    "classification": "Executable physical likelihood with a kernel containing the WP453 real source direction; neither selector nor rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "smallest_exact_falsifier": "A nonzero change of eps_K under the declared real correlated probe.",
    "remaining_gate": "An executable DeltaM_K likelihood with an independently frozen SM long-distance nuisance model, or another source-derived CP-even observable on the same real current direction.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp459_executable_kaon_likelihood_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
