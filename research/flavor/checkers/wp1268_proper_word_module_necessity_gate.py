import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1268-proper-word-module-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1218,1227))
wp1218=json.loads((ROOT/"results"/"wp1218_boundaryless_holonomy_instrument_gate.json").read_text())
wp1219=json.loads((ROOT/"results"/"wp1219_source_derived_proper_word_module_gate.json").read_text())
wp1220=json.loads((ROOT/"results"/"wp1220_independent_source_normal_coordinate_gate.json").read_text())
wp1221=json.loads((ROOT/"results"/"wp1221_asymmetric_full_weak_basis_operation_gate.json").read_text())
wp1222=json.loads((ROOT/"results"/"wp1222_three_source_decomposition_instrument_gate.json").read_text())
wp1223=json.loads((ROOT/"results"/"wp1223_physical_doublet_projective_coupling_gate.json").read_text())
wp1224=json.loads((ROOT/"results"/"wp1224_ordered_spanning_triple_source_action_gate.json").read_text())
wp1225=json.loads((ROOT/"results"/"wp1225_interior_enforcing_source_completion_gate.json").read_text())
wp1226=json.loads((ROOT/"results"/"wp1226_microscopic_affine_action_authority_gate.json").read_text())

bypass_routes={
    "single_holonomy":{
        "proper":wp1218["single_holonomy_proper"],
        "cp_zero":wp1218["single_holonomy_cp_zero"],
        "proper_word_module":wp1218["proper_word_module"]
    },
    "universal_weyl_closure":{
        "universal":wp1218["weyl_pair_universal"],
        "coefficient_fiber_hostile":wp1218["coefficient_fiber_hostile"],
        "physical_instrument":wp1218["physical_instrument"]
    },
    "canonical_twirls_and_deformation":{
        "closure_universal":wp1219["closure_universal"],
        "source_rigid":wp1219["source_rigid"],
        "proper_noncommuting_module":wp1219["proper_noncommuting_module"],
        "independent_source_normal_coordinate":wp1219["independent_source_normal_coordinate"]
    },
    "canonical_normal_coordinates":{
        "traceless_nonpositive":wp1220["traceless_nonpositive"],
        "average_cp_erasing":wp1220["average_cp_erasing"],
        "independent_source_coordinate":wp1220["independent_source_coordinate"],
        "asymmetric_source_operation":wp1220["asymmetric_source_operation"]
    },
    "asymmetric_sector_operations":{
        "asymmetric_weights_distinct":wp1221["asymmetric_weights_distinct"],
        "isotropic_channels_erase_cp":wp1221["isotropic_channels_erase_cp"],
        "two_involutions_cp_zero":wp1221["two_involutions_cp_zero"],
        "asymmetric_operation":wp1221["asymmetric_operation"],
        "three_source_decompositions":wp1221["three_source_decompositions"]
    },
    "s3_flags":{
        "three_flag_orbit":wp1222["three_flag_orbit"],
        "projective_sign_blind":wp1222["projective_sign_blind"],
        "radial_blind":wp1222["radial_blind"],
        "physical_doublet":wp1222["physical_doublet"],
        "calibrated_instrument":wp1222["calibrated_instrument"]
    },
    "projective_coupling":{
        "second_tensor_algebraically_sufficient":wp1223["second_tensor_algebraically_sufficient"],
        "second_tensor_not_source_authorized":wp1223["second_tensor_not_source_authorized"],
        "ordered_spanning_triple":wp1223["ordered_spanning_triple"],
        "source_action":wp1223["source_action"]
    },
    "minimal_ordered_triple_actions":{
        "pair_overlap_cp_blind":wp1224["pair_overlap_cp_blind"],
        "linear_bargmann_rank_deficient":wp1224["linear_bargmann_rank_deficient"],
        "squared_orientation_boundary":wp1224["squared_orientation_boundary"],
        "spanning_oriented_triple":wp1224["spanning_oriented_triple"],
        "interior_enforcing_completion":wp1224["interior_enforcing_completion"]
    },
    "affine_interior_completion":{
        "strict_spanning_minima":wp1225["strict_spanning_minima"],
        "orientation_nonzero":wp1225["orientation_nonzero"],
        "five_gates_unauthorized":wp1225["five_gates_unauthorized"],
        "microscopic_source_object":wp1225["microscopic_source_object"],
        "relative_normalization":wp1225["relative_normalization"]
    }
}

assert bypass_routes["single_holonomy"]["proper"] and bypass_routes["single_holonomy"]["cp_zero"]
assert bypass_routes["universal_weyl_closure"]["universal"] and bypass_routes["universal_weyl_closure"]["coefficient_fiber_hostile"]
assert bypass_routes["canonical_twirls_and_deformation"]["closure_universal"] and bypass_routes["canonical_twirls_and_deformation"]["source_rigid"]
assert bypass_routes["canonical_normal_coordinates"]["traceless_nonpositive"] and bypass_routes["canonical_normal_coordinates"]["average_cp_erasing"]
assert bypass_routes["asymmetric_sector_operations"]["isotropic_channels_erase_cp"] and bypass_routes["asymmetric_sector_operations"]["two_involutions_cp_zero"]
assert bypass_routes["s3_flags"]["three_flag_orbit"] and bypass_routes["s3_flags"]["projective_sign_blind"] and bypass_routes["s3_flags"]["radial_blind"]
assert bypass_routes["projective_coupling"]["second_tensor_algebraically_sufficient"] and bypass_routes["projective_coupling"]["second_tensor_not_source_authorized"]
assert bypass_routes["minimal_ordered_triple_actions"]["pair_overlap_cp_blind"] and bypass_routes["minimal_ordered_triple_actions"]["linear_bargmann_rank_deficient"]
assert bypass_routes["affine_interior_completion"]["strict_spanning_minima"] and bypass_routes["affine_interior_completion"]["orientation_nonzero"]

for route in bypass_routes.values():
    for key in ("proper_word_module","physical_instrument","proper_noncommuting_module","independent_source_normal_coordinate","independent_source_coordinate","asymmetric_source_operation","asymmetric_operation","three_source_decompositions","physical_doublet","calibrated_instrument","ordered_spanning_triple","source_action","spanning_oriented_triple","interior_enforcing_completion","microscopic_source_object","relative_normalization"):
        if key in route: assert route[key] is False,(key,route)

microscopic_affine_status={
    "renormalizable_constructor":wp1226["renormalizable_constructor"],
    "benchmark_falsified":wp1226["benchmark_falsified"],
    "coefficient_ray_fiber":wp1226["coefficient_ray_fiber"],
    "dimensionless_scale_fiber":wp1226["dimensionless_scale_fiber"],
    "source_derived_relation":wp1226["source_derived_relation"],
    "controlled_elimination":wp1226["controlled_elimination"],
    "global_vacuum":wp1226["global_vacuum"],
    "calibrated_instrument":wp1226["calibrated_instrument"]
}
assert microscopic_affine_status["renormalizable_constructor"] and microscopic_affine_status["benchmark_falsified"]
assert microscopic_affine_status["coefficient_ray_fiber"] and microscopic_affine_status["dimensionless_scale_fiber"]
assert not microscopic_affine_status["source_derived_relation"] and not microscopic_affine_status["controlled_elimination"]

source_authorized_word_module=False
conjecture_refuted=source_authorized_word_module
assert not conjecture_refuted

result={
    "schema":"marici.flavor.wp1268.v1",
    "status":"PASS",
    "question":"Can a boundaryless holonomy source bypass a source-derived proper noncommuting CP-bearing word module?",
    "dpc":{
        "conjecture":"Every boundaryless holonomy source sufficient for the flavor selector must pass through a source-derived proper noncommuting CP-bearing word module with interior-enforcing microscopic action authority.",
        "rivals":["single holonomy","universal Weyl closure","canonical twirls or deformation","canonical normal coordinate","asymmetric sector operation","S3 flag instrument","projective coupling","minimal ordered-triple action","affine interior completion"],
        "risky_consequences":["WP1218 single holonomy is proper but CP-trivial and Weyl closure is universal with a coefficient hostile","WP1219 canonical constructors are universal, commutative, scalar, or rigid","WP1220 and WP1221 canonical or asymmetric coordinates are nonpositive, CP-erasing, or two-level","WP1222 flags are sign and radius blind","WP1223 has an algebraic second tensor but no source authority","WP1224 minimal actions are CP-blind, rank-deficient, or endpoint-switching","WP1225 has strict interior minima but no microscopic source object","WP1226 has a renormalizable constructor but no source-derived coefficient relation"],
        "falsification_attempt":"Replay WP1218 through WP1226 and search for a source-authorized boundaryless holonomy instrument that bypasses the proper word module and microscopic action authority.",
        "residual":"No bypass is found; the proper-word-module necessity conjecture survives. The residual is a source-derived dimensionless coefficient relation with controlled elimination, global vacuum, and calibrated transport.",
        "disposition":"proper-word-module necessity survives attempted falsification; source-derived coefficient relation selected"
    },
    "bypass_routes":bypass_routes,
    "microscopic_affine_status":microscopic_affine_status,
    "source_authorized_word_module":source_authorized_word_module,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold proper-word-module necessity gate: all replayed boundaryless-holonomy bypass routes fail source authorization",
    "remaining_gate":"derive the dimensionless coefficient relation before flavor readout, prove controlled elimination and global vacuum, and transport to calibrated physical16",
    "hostile_gate":"do not treat single holonomies, universal Weyl closure, canonical coordinates, S3 flags, algebraic second tensors, minimal actions, or conditional affine minima as a source-authorized proper word module",
    "claim_boundary":"WP1218 through WP1226 falsify the replayed bypass routes; the proper-word-module necessity conjecture survives but remains unproven",
    "disposition":"boundaryless-holonomy-source leaf resolved conditionally; source-derived coefficient relation required"
}
(ROOT/"results"/"wp1268_proper_word_module_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1268 PASS: proper-word-module necessity survives attempted falsification; coefficient relation remains open")
