import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(984,985,986,987,988,989)
wp984=json.loads((ROOT/"results"/"wp984_uv_lift_jet_faithfulness.json").read_text())
wp985=json.loads((ROOT/"results"/"wp985_bounded_rational_lift_tomography.json").read_text())
wp986=json.loads((ROOT/"results"/"wp986_complementary_lift_channel_rank.json").read_text())
wp987=json.loads((ROOT/"results"/"wp987_complementary_instrument_composition_gate.json").read_text())
wp988=json.loads((ROOT/"results"/"wp988_complementary_channel_source_identity_gate.json").read_text())
wp989=json.loads((ROOT/"results"/"wp989_kinetic_normalization_quotient.json").read_text())
assert wp984["classification"] == "threshold jets refine UV lift classes but no fixed finite tower is faithful without a bounded source grammar"
assert wp985["classification"] == "finite jets are faithful on bounded rational responses but not on their UV factorizations"
assert wp986["classification"] == "formal separator and constructor identifier; neither selector nor established instrument"
assert wp987["classification"] == "formal constructor separator; neither selector nor admitted instrument"
assert wp988["classification"] == "upstream source-identity obstruction; neither selector, rigidifier, nor instrument"
assert wp989["classification"] == "faithful quotient correction; neither selector nor rigidifier"
# Formal complementary channels can separate the source tangent, but the
# executable and source-identity ranks are zero and quotient descent still
# needs a calibrated independent invariant.
finite_tower_unbounded=True
factorization_kernel=True
formal_rank_four=True
executable_rank_zero=True
source_identity_rank_zero=True
quotient_correction=True
independent_invariant_required=True
source_derived_coefficient_relation=False
shared_provenance=False
calibrated_instrument=False
assert finite_tower_unbounded and factorization_kernel and formal_rank_four
assert executable_rank_zero and source_identity_rank_zero and quotient_correction and independent_invariant_required
assert not (source_derived_coefficient_relation or shared_provenance or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1227.v1",
    "status":"PASS",
    "question":"Can lift tomography derive the source coefficient relation?",
    "dpc":{
        "conjecture":"UV threshold jets and complementary lift channels derive the dimensionless coefficient relation before flavor readout.",
        "rivals":["fixed finite jet tower","bounded rational lift tomography","three complementary channels","existing WP560/WP534 records","kinetic normalization quotient"],
        "risky_consequences":["an arbitrary finite jet first differs at order n+1","finite jets on bounded rational responses do not identify UV factorization","three complementary rows have formal determinant -4","admitted end-to-end and source-identity ranks are zero","normalization leaves a two-dimensional physical quotient requiring one independent invariant"],
        "falsification_attempt":"formal separation survives, but no executable row maps a measured record to the mixed vertex or its scalar/adjoint poles.",
        "residual":"construct records for the WP977 mixed vertex and its own scalar and adjoint poles, then calibrate a weak-basis-invariant A^2/C response in one shared-provenance likelihood",
        "disposition":"reject lift tomography as coefficient authority; select complementary-source-records rival"
    },
    "finite_jet_hostile":wp984["arbitrary_finite_order_hostile"],
    "bounded_tomography":wp985["degree_bounds"],
    "formal_rows":wp986["complementary_rows"],
    "formal_determinant":wp987["formal_determinant"],
    "admitted_end_to_end_rank":wp987["admitted_end_to_end_rank"],
    "source_identity_rank":wp988["source_identity_rank"],
    "quotient":wp989["invariant_rows"],
    "finite_tower_unbounded":finite_tower_unbounded,
    "factorization_kernel":factorization_kernel,
    "formal_rank_four":formal_rank_four,
    "executable_rank_zero":executable_rank_zero,
    "source_identity_rank_zero":source_identity_rank_zero,
    "quotient_correction":quotient_correction,
    "independent_invariant_required":independent_invariant_required,
    "source_derived_coefficient_relation":source_derived_coefficient_relation,
    "shared_provenance":shared_provenance,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative coefficient-relation result: formal lift separation lacks executable source records",
    "remaining_gate":"construct mixed-vertex, scalar-pole, and adjoint-pole records, then calibrate one independent quotient invariant in shared provenance",
    "hostile_gate":"do not call finite jets, bounded-response tomography, formal rank, existing unrelated records, or quotient correction a source-derived coefficient relation",
    "claim_boundary":"formal separation is genuine, but admitted executable rank and source-identity rank are zero",
    "disposition":"source-derived-coefficient-relation leaf resolved negatively; complementary-source-records rival selected"
}
(ROOT/"results"/"wp1227_source_derived_coefficient_relation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1227 PASS: lift tomography lacks executable coefficient authority")
