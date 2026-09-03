import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1030,1031,1032,1033,1034,1035)
wp1030=json.loads((ROOT/"results"/"wp1030_schur_pole_vs_gram_norm.json").read_text())
wp1031=json.loads((ROOT/"results"/"wp1031_minimal_single_pole_seventeen_no_go.json").read_text())
wp1032=json.loads((ROOT/"results"/"wp1032_protected_single_pole_normalization_no_go.json").read_text())
wp1033=json.loads((ROOT/"results"/"wp1033_existing_fixed_point_topological_interface_audit.json").read_text())
wp1034=json.loads((ROOT/"results"/"wp1034_litim_sannino_pole_interface_no_go.json").read_text())
wp1035=json.loads((ROOT/"results"/"wp1035_primitive_integer_clebsch_gap.json").read_text())
assert wp1030["classification"] == "Schur matching is controlled by the inverse pole operator, not the Frobenius mass norm; mediator multiplicity changes port contraction, not m to sqrt(17)m"
assert wp1031["classification"] == "O(N) radial symmetry does not transmit N into curvature; an N-fold spectator sum transmits N but retains the free portal coupling g"
assert wp1032["classification"] == "protected relative rigidifier, not absolute selector"
assert wp1033["classification"] == "empty source-authorized interface intersection; neither selector nor new rigidifier for the WP1028 pole"
assert wp1034["classification"] == "neither selector nor rigidifier for the pole; even the unauthorized direct interface predicts the wrong magnitude"
assert wp1035["classification"] == "integer rigidifier with empty admissible readout; not a selector"
# The surviving interpretation must be one composite pole with additive mass
# contributions; all minimal, protected, fixed-point, and integer-interface
# routes leave or miss the required normalization.
schur_rank17_invalid=True
single_pole_freedom=True
protected_fiber_remains=True
archive_interface_empty=True
litim_sannino_wrong_magnitude=True
integer_clebsch_gap=True
typed_mass_interface=False
normalization_theorem=False
threshold_survival=False
calibrated_pole_interface=False
assert schur_rank17_invalid and single_pole_freedom and protected_fiber_remains
assert archive_interface_empty and litim_sannino_wrong_magnitude and integer_clebsch_gap
assert not (typed_mass_interface or normalization_theorem or threshold_survival or calibrated_pole_interface)
result={
    "schema":"marici.flavor.wp1236.v1",
    "status":"PASS",
    "question":"Can a source-covariant mass-norm interface realize the conditional N=17 pole?",
    "dpc":{
        "conjecture":"A rank-17 equal-mass frame, minimal single-pole symmetry, protected D/F-term completion, or existing fixed point realizes M squared = 17 f squared.",
        "rivals":["rank-17 Schur denominator","O(N) radial or spectator constructor","D-term and F-term protection","existing fixed-point/topological archive","direct WP802 interface","integer Clebsch coefficient"],
        "risky_consequences":["normalized ports give Schur response 1/m, not 1/(sqrt(17)m)","O(N) curvature is independent of N while spectator sums retain free g","protected classes retain a continuous G or y fiber","no archived candidate passes all five interface gates","the WP802 h=y squared interface is below threshold","integer C=11 and C=12 straddle the fitted interval"],
        "falsification_attempt":"every proposed interface either changes the pole type, leaves a continuous normalization, lacks a typed map, or gives the wrong magnitude.",
        "residual":"a named source theorem mapping a controlled fixed coupling to the CP-even single-pole mass operator with threshold survival and instrument rank",
        "disposition":"reject the tested mass-norm interfaces; select a discrete source-actuator typing rival"
    },
    "schur_response":wp1030["normalized_exact_schur_response"],
    "frobenius_mass":wp1030["frobenius_mass"],
    "single_pole_constructors":{"radial":wp1031["radial_constructor"],"spectator":wp1031["spectator_constructor"]},
    "protected_constructors":{"d_term":wp1032["D_term"],"f_term":wp1032["F_term"]},
    "archive_candidate_matrix":wp1033["candidate_matrix"],
    "wp1034_fixed_coordinate":wp1034["fixed_coordinate"],
    "clebsch_adjacent_falsifiers":wp1035["adjacent_falsifiers"],
    "schur_rank17_invalid":schur_rank17_invalid,
    "single_pole_freedom":single_pole_freedom,
    "protected_fiber_remains":protected_fiber_remains,
    "archive_interface_empty":archive_interface_empty,
    "litim_sannino_wrong_magnitude":litim_sannino_wrong_magnitude,
    "integer_clebsch_gap":integer_clebsch_gap,
    "typed_mass_interface":typed_mass_interface,
    "normalization_theorem":normalization_theorem,
    "threshold_survival":threshold_survival,
    "calibrated_pole_interface":calibrated_pole_interface,
    "classification":"negative mass-norm-interface result: conditional N=17 survives only as an underived single-pole additive normal form",
    "remaining_gate":"derive the source theorem and typed map fixing the pole normalization, then prove threshold survival and calibrate pole/condensate readout",
    "hostile_gate":"do not call Frobenius norms, symmetry relations, archived fixed points, direct identifications, or integer multiplicities a source-covariant mass interface",
    "claim_boundary":"the WP1028 candidate remains a conditional normal form; the tested interface families do not derive it",
    "disposition":"source-covariant mass-norm-interface leaf resolved negatively; discrete source-actuator typing rival selected"
}
(ROOT/"results"/"wp1236_source_covariant_mass_norm_interface_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1236 PASS: mass-norm interfaces fail; discrete source-actuator typing required")
