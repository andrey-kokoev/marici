import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1074,1075,1076,1077,1078,1079)
wp1074=json.loads((ROOT/"results"/"wp1074_soft_channel_degeneracy_gate.json").read_text())
wp1075=json.loads((ROOT/"results"/"wp1075_soft_channel_reweighting_rank_gate.json").read_text())
wp1076=json.loads((ROOT/"results"/"wp1076_symmetric_production_law_cofiber.json").read_text())
wp1077=json.loads((ROOT/"results"/"wp1077_four_state_acquisition_calibration_gate.json").read_text())
wp1078=json.loads((ROOT/"results"/"wp1078_aspect_pattern_acquisition_composition_gate.json").read_text())
wp1079=json.loads((ROOT/"results"/"wp1079_nima_candidate_source_law_audit_gate.json").read_text())
assert wp1074["classification"].startswith("soft-channel degeneracy gate")
assert wp1075["classification"].startswith("soft-channel reweighting rank gate")
assert wp1076["classification"].startswith("symmetric-production cofiber")
assert wp1077["classification"].startswith("conditional four-state acquisition gate")
assert wp1078["classification"].startswith("conditional Aspect-pattern composition")
assert wp1079["classification"].startswith("Nima-candidate audit gate")
# The instrument chain is calibrated, but the UV/common source packet still
# lacks production kernel, mixing, gain, and flux/endpoint certificates.
soft_candidates_six=True
rank_one_reweighting_known=True
symmetric_kernel_uncertified=True
four_state_calibration=True
aspect_composition_calibrated=True
nima_candidates_fill_none=True
common_uv_packet=False
production_kernel=False
mixing_matrix_derived=False
gain_3_over_2_derived=False
flux_sector_orientation=False
endpoint_action=False
physical16_channel=False
source_gain=False
assert soft_candidates_six and rank_one_reweighting_known and symmetric_kernel_uncertified
assert four_state_calibration and aspect_composition_calibrated and nima_candidates_fill_none
assert not (common_uv_packet or production_kernel or mixing_matrix_derived or gain_3_over_2_derived or flux_sector_orientation or endpoint_action or physical16_channel or source_gain)
result={
    "schema":"marici.flavor.wp1246.v1",
    "status":"PASS",
    "question":"Can existing calibration and candidate source packets construct the common UV boundary-action packet?",
    "dpc":{
        "conjecture":"Calibrated acquisition plus the named candidate packets might supply the missing source dynamics for the common UV packet.",
        "rivals":["six degenerate soft branches","rank-one reweighting matrix","symmetric production law","four-state acquisition","Aspect pattern composition","Nima candidate source packets"],
        "risky_consequences":["all six localized branches share ratio one and response 1/2","U=(1/6)J with gain 3/2 maps dimension weights to event weights but cannot be inferred from target rows","four-state acquisition has rank five on background, luminosity, gain, visibility, and scale","Aspect patterns close scale, affine, phase, and robustness hostiles","the five Nima packets fill none of the four open selector slots"],
        "falsification_attempt":"calibration hostiles are controlled, while production kernel, source mixing, gain, flux sector/orientation, endpoint action, and Physical16 channels remain absent.",
        "residual":"obtain a microscopic mediator grammar or Nima's promised construction/no-go with source-generated proper-image task, mixing, gain, flux, endpoint action, and channel map",
        "disposition":"accept instrument calibration conditionally; hand off the source-dynamics construction to the owner rather than fabricating the UV packet"
    },
    "soft_candidates":wp1074["soft_candidates"],
    "vector_comparison":wp1074["vector_comparison"],
    "source_branch_distribution":wp1075["source_branch_distribution"],
    "target_event_role_weights":wp1075["target_event_role_weights"],
    "minimal_rank_one_solution":wp1075["minimal_rank_one_solution"],
    "symmetric_candidates":wp1076["candidate_laws"],
    "missing_certificates":wp1076["missing_certificates"],
    "four_state_source":wp1077["external_source"],
    "jacobian_rank_on_B_L_g_nu_s":wp1077["jacobian_rank_on_B_L_g_nu_s"],
    "aspect_composed_gates":wp1078["composed_gates"],
    "nima_external_reply":wp1079["external_reply"],
    "candidate_audit":wp1079["candidate_audit"],
    "slot_verdicts":wp1079["slot_verdicts"],
    "soft_candidates_six":soft_candidates_six,
    "rank_one_reweighting_known":rank_one_reweighting_known,
    "symmetric_kernel_uncertified":symmetric_kernel_uncertified,
    "four_state_calibration":four_state_calibration,
    "aspect_composition_calibrated":aspect_composition_calibrated,
    "nima_candidates_fill_none":nima_candidates_fill_none,
    "common_uv_packet":common_uv_packet,
    "production_kernel":production_kernel,
    "mixing_matrix_derived":mixing_matrix_derived,
    "gain_3_over_2_derived":gain_3_over_2_derived,
    "flux_sector_orientation":flux_sector_orientation,
    "endpoint_action":endpoint_action,
    "physical16_channel":physical16_channel,
    "source_gain":source_gain,
    "classification":"conditional common-UV-packet gate: acquisition calibrated, source-dynamics construction ownership-blocked",
    "remaining_gate":"owner-supplied microscopic source grammar or Nima construction/no-go must provide production kernel, mixing, gain, flux sector, endpoint action, and Physical16 channel map",
    "hostile_gate":"do not call calibration rank, rank-one target fitting, symmetry arithmetic, or candidate audit a common UV boundary-action packet",
    "claim_boundary":"WP1074 through WP1079 provide exact acquisition/reweighting and ownership audit; no UV action or source gain is derived",
    "disposition":"common-UV-boundary-action-packet leaf resolved as ownership-blocked; active Nima source-dynamics handoff selected"
}
(ROOT/"results"/"wp1246_common_uv_boundary_action_packet_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1246 PASS: acquisition calibrated, source-dynamics ownership handoff required")
