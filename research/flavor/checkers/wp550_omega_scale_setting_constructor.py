"""Exact same-ensemble Omega scale-setting constructor for six flavor ports."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp542 = load("wp542_continuum_volume_design_rank.json")
wp548 = load("wp548_cross_locus_scale_reference_gate.json")
wp549 = load("wp549_temporal_scale_calibration_contract.json")

# Input log coordinates are six dimensionless lattice pole scales, the
# same-ensemble dimensionless Omega mass, and the external physical Omega mass.
J = sp.zeros(6, 8)
for i in range(6):
    J[i, i] = 1
    J[i, 6] = -1
    J[i, 7] = 1

lattice_unit_reparametrization = sp.Matrix([1, 1, 1, 1, 1, 1, 1, 0])
external_mass_shift = sp.Matrix([0, 0, 0, 0, 0, 0, 0, 1])

pole_variances = sp.symbols("s1:7", positive=True)
omega_lattice_variance, omega_physical_variance = sp.symbols(
    "s_omega_lattice s_omega_physical", positive=True
)
input_covariance = sp.diag(
    *[x**2 for x in pole_variances],
    omega_lattice_variance**2,
    omega_physical_variance**2,
)
output_covariance = sp.simplify(J * input_covariance * J.T)
shared_scale_variance = omega_lattice_variance**2 + omega_physical_variance**2

expected_covariance = sp.diag(*[x**2 for x in pole_variances]) + shared_scale_variance * sp.ones(6)

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp542, wp548, wp549)),
    "six_physical_poles_have_rank_six": J.rank() == 6,
    "lattice_unit_reparametrization_cancels": J * lattice_unit_reparametrization
    == sp.zeros(6, 1),
    "external_physical_mass_sets_common_scale": J * external_mass_shift == sp.ones(6, 1),
    "covariance_propagation_is_exact": output_covariance == expected_covariance,
    "shared_scale_uncertainty_is_off_diagonal": all(
        output_covariance[i, j] == shared_scale_variance
        for i in range(6)
        for j in range(6)
        if i != j
    ),
    "continuum_design_requires_scale_covariance": "scale-systematic covariance"
    in wp542["remaining_gate"],
    "wp548_interface_row_is_recovered": wp548["required_interface_row"] == ["0", "1", "-1"],
    "wp549_requires_successful_calibration_event": wp549["state_establishing_event"]["event"]
    == "calibration_success",
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP550",
    "domain": "A same-ensemble lattice scale-setting architecture for the six WP535 flavor ports, using the dimensionless Omega-baryon mass and an external pure-QCD physical Omega mass.",
    "source_literature": [
        {
            "title": "Scale setting the Mobius domain wall fermion on gradient-flowed HISQ action using the omega baryon mass and the gradient-flow scales t0 and w0",
            "locator": "https://arxiv.org/abs/2011.12166",
            "authority": "Primary lattice calculation measuring a m_Omega, t0/a^2, and w0/a on each of 22 ensembles with continuum, volume, and uncertainty control.",
        },
        {
            "title": "High-Precision Scale Setting with the Omega-Baryon Mass and Gradient Flow",
            "locator": "https://arxiv.org/abs/2509.14367",
            "authority": "Primary updated calculation defining electromagnetic corrections to obtain a pure-QCD Omega input and reporting a 0.40 percent w0 determination.",
        },
    ],
    "constructor": {
        "same_ensemble_inputs": ["a*m_Omega", "a*mu_1", "a*mu_2", "a*mu_3", "a*mu_4", "a*mu_5", "a*mu_6"],
        "external_input": "m_Omega in the declared pure-QCD convention",
        "lattice_spacing": "a=(a*m_Omega)/m_Omega_physical",
        "physical_poles": "mu_i=(a*mu_i)*m_Omega_physical/(a*m_Omega)",
        "log_jacobian": [[str(x) for x in row] for row in J.tolist()],
        "rank": J.rank(),
    },
    "covariance": {
        "exact_rule": "C_physical=J C_joint J^T",
        "diagonal_input_witness": [[str(x) for x in row] for row in input_covariance.tolist()],
        "output_witness": [[str(x) for x in row] for row in output_covariance.tolist()],
        "shared_scale_term": str(shared_scale_variance),
        "same_ensemble_requirement": "C_joint must include cross-covariances between every flavor estimator, a*m_Omega, gradient-flow observables, tuning coordinates, and continuum/volume nuisance parameters.",
    },
    "temporal_event": {
        "precondition": "The Omega and gradient-flow estimators are generated on the same ensemble stream as the flavor ports under one frozen action and tuning prescription.",
        "outcome": "A successful joint scale fit with pure-QCD convention, readback, and covariance.",
        "post_state": "WP549 valid calibration state for that ensemble and fit revision.",
        "deletion_replay": "Removing a*m_Omega, the physical Omega input, or their covariance invalidates physical-unit pole, width, and residue readouts.",
    },
    "theorem": "The Omega constructor supplies a physically standard candidate P_scale map: each physical flavor pole is the dimensionless pole times m_Omega_physical divided by the same-ensemble dimensionless Omega mass. The exact six-output Jacobian has rank six, cancels lattice-unit reparameterization, and propagates scale uncertainty as a common correlated term. It is not executable for WP535 until the Omega and flavor correlators are generated jointly on the declared ensembles.",
    "classification": "Source-authorized physical scale-setting architecture and exact covariance map; not yet an executed flavor dataset or source selector.",
    "selector": bool(wp548["selector"]),
    "instrument": "Concrete P_scale architecture. Execution still requires same-ensemble Omega, gradient-flow, and six-port measurements with joint continuum, volume, tuning, electromagnetic-convention, and covariance analysis.",
    "smallest_exact_falsifier": "Import a published w0 or Omega scale without measuring the corresponding dimensionless scale observable on the WP542 ensembles. Then the common unit coordinate is not shared and WP548's kernel is not removed.",
    "remaining_gate": "Preregister the exact ensembles and pure-QCD Omega convention, generate a*m_Omega and gradient-flow estimators on every WP542 ensemble together with the 48 flavor estimators, and publish the full joint covariance and deletion replay.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp550_omega_scale_setting_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
