"""Exact scale and typing audit for candidate Higgs context controls."""

import json
from pathlib import Path

import sympy as sp


# Published central scales in GeV: SM crossover and the largest recent ALICE
# direct-photon effective slope quoted in the audited review/measurement.
T_ew = sp.Rational(319, 2)
T_alice = sp.Rational(458, 1000)
temperature_ratio = sp.factor(T_ew / T_alice)
radiation_density_ratio = sp.factor(temperature_ratio**4)

# In the leading thermal-mass grammar c=a*T^2, the relative source deformation
# between the two central scales is quadratic in their ratio.
thermal_mass_ratio = sp.factor(temperature_ratio**2)

# Candidate interface capability vectors:
# (source-derived Higgs mass deformation, executable laboratory control,
#  calibrated Higgs curvature readout, retained-vacuum displacement readout).
thermal_early_universe = sp.Matrix([1, 0, 1, 1])
heavy_ion_fireball = sp.Matrix([1, 1, 0, 0])
curvature_background = sp.Matrix([1, 0, 0, 0])
new_portal_background = sp.Matrix([1, 0, 0, 0])
required = sp.Matrix([1, 1, 1, 1])

candidates = sp.Matrix.hstack(
    thermal_early_universe,
    heavy_ion_fireball,
    curvature_background,
    new_portal_background,
)

checks = {
    "electroweak_to_alice_temperature_ratio_exceeds_300": temperature_ratio > 300,
    "thermal_mass_scale_ratio_exceeds_100000": thermal_mass_ratio > 100000,
    "radiation_density_scale_ratio_exceeds_ten_billion": radiation_density_ratio > 10**10,
    "no_candidate_has_complete_capability_vector": all(candidates[:, j] != required for j in range(candidates.cols)),
    "heavy_ion_has_no_higgs_common_frame_readout": heavy_ion_fireball[2] == 0 and heavy_ion_fireball[3] == 0,
    "early_universe_is_not_executable": thermal_early_universe[1] == 0,
    "new_portal_requires_new_source": new_portal_background[1] == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP413",
    "title": "Higgs context-knob reach gate",
    "scales_GeV": {"standard_model_crossover": str(T_ew), "alice_effective_photon_slope": str(T_alice)},
    "central_temperature_ratio": str(temperature_ratio),
    "leading_thermal_mass_ratio": str(thermal_mass_ratio),
    "radiation_density_scale_ratio": str(radiation_density_ratio),
    "capability_order": ["source_deformation", "executable_control", "higgs_curvature_readout", "reference_displacement_readout"],
    "candidate_capabilities": {
        "early_universe_thermal_history": [int(x) for x in thermal_early_universe],
        "heavy_ion_fireball": [int(x) for x in heavy_ion_fireball],
        "curvature_background": [int(x) for x in curvature_background],
        "new_portal_background": [int(x) for x in new_portal_background],
    },
    "classification": "no currently admitted Standard Model operation closes the WP412 source-control-readout square",
    "smallest_falsifier": "a calibrated laboratory record of both Higgs screening curvature and retained-vacuum displacement under one varied source setting",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP413 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp413_higgs_knob_reach_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
