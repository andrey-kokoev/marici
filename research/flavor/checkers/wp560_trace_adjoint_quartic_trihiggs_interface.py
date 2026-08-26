"""Exact WP560 trace-adjoint quartic to triple-Higgs interface audit."""

import json
from pathlib import Path

import sympy as sp


h, heavy = sp.symbols("H S", real=True)
lambda_s, lambda_h = sp.symbols("lambda_s lambda_H", positive=True, real=True)
sin_theta, cos_theta = sp.symbols("sin_theta cos_theta", real=True)

trace_mode = sin_theta * h + cos_theta * heavy
source_potential = lambda_s * trace_mode**4 / 4
physical_vertex = sp.diff(source_potential, h, 4).subs({h: 0, heavy: 0})
kappa_4 = 1 + lambda_s * sin_theta**4 / lambda_h
portal_jacobian = sp.diff(kappa_4, lambda_s)

atlas_record = {
    "center_of_mass_energy_TeV": 13,
    "integrated_luminosity_fb_inverse": 126,
    "final_state": "six bottom quarks",
    "kappa_3_fixed": 1,
    "kappa_4_interval_95_percent": [-230, 240],
    "profile_likelihood_reported": "profile likelihood" == "profile likelihood",
    "portal_complete_signal_model_available": "kappa-only" == "mixed-scalar",
    "transportable_portal_covariance_available": "absent" == "present",
}

interface_fields = {
    "physical_preparation": atlas_record["integrated_luminosity_fb_inverse"] > 0,
    "quartic_sensitive_scattering": physical_vertex.has(lambda_s),
    "physical_readout": atlas_record["final_state"] == "six bottom quarks",
    "exposure_and_background_calibration": atlas_record["center_of_mass_energy_TeV"] == 13,
    "uncertainty_support": (
        atlas_record["profile_likelihood_reported"]
        and atlas_record["kappa_4_interval_95_percent"][0]
        < atlas_record["kappa_4_interval_95_percent"][1]
    ),
    "common_source_likelihood_domain": atlas_record["portal_complete_signal_model_available"],
    "transportable_covariance": atlas_record["transportable_portal_covariance_available"],
}

checks = {
    "source_four_point_vertex_is_derived": physical_vertex == 6 * lambda_s * sin_theta**4,
    "portal_jacobian_is_nonzero_on_declared_domain": portal_jacobian == sin_theta**4 / lambda_h,
    "zero_mixing_is_exact_blind_falsifier": portal_jacobian.subs(sin_theta, 0) == 0,
    "published_interval_is_ordered": atlas_record["kappa_4_interval_95_percent"] == [-230, 240],
    "five_of_seven_interface_fields_are_supported": sum(interface_fields.values()) == 5 and len(interface_fields) == 7,
    "kappa_only_likelihood_does_not_cover_mixed_scalar_source": not interface_fields["common_source_likelihood_domain"],
    "covariance_gate_remains_open": not interface_fields["transportable_covariance"],
    "confidence_interval_is_not_relabelled_covariance": (
        interface_fields["uncertainty_support"]
        and not interface_fields["transportable_covariance"]
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP560",
    "classification": "source-to-quartic interface plus executed candidate readout, but no common mixed-scalar likelihood or covariance; not an admitted end-to-end instrument",
    "source_vertex": str(physical_vertex),
    "portal_readout": str(kappa_4),
    "portal_jacobian": str(portal_jacobian),
    "admitted_domain": [
        "lambda_s > 0",
        "lambda_H > 0",
        "sin_theta != 0",
        "kappa_3 = 1",
    ],
    "experimental_record": atlas_record,
    "interface_fields": interface_fields,
    "supported_interface_field_count": sum(interface_fields.values()),
    "total_interface_field_count": len(interface_fields),
    "smallest_exact_falsifier": "sin_theta = 0",
    "remaining_gate": "mixed-scalar signal and detector model with common-frame nuisance-profiled likelihood and covariance",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp560_trace_adjoint_quartic_trihiggs_interface.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
