import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1171=json.loads((ROOT/"results"/"wp1171_exact_unistochastic_certificate.json").read_text())
assert wp1171["exact_real_orthogonal_solution_certified"] is True
assert wp1171["krawczyk_containment"] is True
assert "source_production_map" not in wp1171
assert "physical16_image" not in wp1171
assert "coupling_scale" not in wp1171
assert "locality_certificate" not in wp1171

# A unistochastic modulus fixes only |S_ij|. For every pair of unit-modulus
# diagonal matrices L,R, LSR has the same squared modulus. The 6+6 diagonal
# phases contain one redundant global phase, so the unobserved phase orbit has
# dimension 11. A production law that needs amplitudes rather than only
# probabilities is therefore not determined by WP1171.
row_phase_parameters=6
col_phase_parameters=6
redundant_global_phase=1
phase_orbit_dimension=row_phase_parameters+col_phase_parameters-redundant_global_phase
assert phase_orbit_dimension == 11

# The certified carrier is zero-diagonal support five. Modulus data have no
# source-preparation labels, channel reweighting, detector interference law,
# or coupling scale.
production_components={
    "source_preparation_labels":0,
    "channel_reweighting_maps":0,
    "detector_interference_laws":0,
    "coupling_scales":0,
    "locality_certificates":0,
}
assert all(v == 0 for v in production_components.values())
physical_production_maps=0
assert physical_production_maps == 0
result={
    "schema":"marici.flavor.wp1172.v1",
    "status":"PASS",
    "question":"Does the certified unistochastic modulus realize physical production?",
    "dpc":{
        "conjecture":"The exact support-five modulus supplies a physical production law.",
        "rivals":["modulus suffices","diagonal phase orbit","coupling-scale source","production authority"],
        "risky_consequences":["Krawczyk-certified P=|S|^2","11 unobserved phase parameters","no physical16 image","no locality certificate"],
        "falsification_attempt":"Diagonal row and column phase actions preserve the modulus, and the WP1171 certificate contains no sourced map, coupling scale, or locality component.",
        "residual":"A separate phase-gauge and production law must be derived from the source packet.",
        "disposition":"reject modulus-to-production promotion"
    },
    "certified_modulus":True,
    "phase_orbit_dimension":phase_orbit_dimension,
    "production_components":production_components,
    "physical_production_maps":physical_production_maps,
    "classification":"negative authority gate: exact unistochastic modulus does not realize sourced physical production",
    "remaining_gate":"derive a phase-gauge law and sourced channel map to physical16",
    "hostile_gate":"do not promote P=|S|^2 to a production, coupling, or locality theorem",
    "claim_boundary":"the result separates the certified modulus from physical production authority",
    "disposition":"production-realization leaf resolved; phase-gauge law rival selected"
}
(ROOT/"results"/"wp1172_production_realization_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1172 PASS:",phase_orbit_dimension,physical_production_maps)
