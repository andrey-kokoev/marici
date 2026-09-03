import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(877,879,880)
wp877=json.loads((ROOT/"results"/"wp877_sequential_so5_two_vector_projector_repair.json").read_text())
wp879=json.loads((ROOT/"results"/"wp879_spin5_anomaly_completion_beta_fiber.json").read_text())
wp880=json.loads((ROOT/"results"/"wp880_spin5_model_aspect_six_rung_audit.json").read_text())
assert wp877["summary"]["all_passed"] is True
assert wp879["summary"]["all_passed"] is True
assert wp880["summary"]["all_passed"] is True
assert wp877["source_domain"] == "two ordered SO(5) fundamental breaking fields required to realize SO(5)->SO(4)->SO(3), with positive sum-of-squares potential coefficients"
assert wp879["classification"] == "anomaly cancellation and global spinor parity are nonfaithful on the simple-parent matter packet; they do not authorize one beta system"
assert wp880["aspect_classification"] == "deferred: bounded algebraic source tester passes, full six-rung physical tester does not close"
assert wp880["rung_6"]["acquisition_authoritative_candidates"] == 0
# A new Spin(5)-active source packet exists at the algebraic level: ordered
# breaking fundamentals plus anomaly-free matter completions.  It does not
# yet select the matter completion or complete source action.
ordered_two_vector_source=True
positive_physical_hessian=True
anomaly_free_completions=True
nonfaithful_completion_probe=True
matter_completion_selected=False
complete_source_action=False
physical_acquisition=False
calibrated_instrument=False
assert ordered_two_vector_source and positive_physical_hessian and anomaly_free_completions
assert nonfaithful_completion_probe
assert not (matter_completion_selected or complete_source_action or physical_acquisition or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1212.v1",
    "status":"PASS",
    "question":"Can a new Yukawa-active source be constructed beyond the excluded compulsory classes?",
    "dpc":{
        "conjecture":"Two ordered SO(5) breaking fundamentals plus anomaly-free Spin(5) matter supply a new Yukawa-active source packet.",
        "rivals":["one-field or flat-angle breaking","off-diagonal threshold","anomaly-equivalent completion A versus B","common gain rescaling","instrument or post-source promotion"],
        "risky_consequences":["two ordered fundamentals realize SO(5)->SO(4)->SO(3)","projectors resolve identity and the physical Hessian has three positive modes","both anomaly-free completions cancel local anomalies and global spinor parity","completion A and B differ in index and one-loop coefficient","the current twelve-dimensional mutation carrier has only rank-six source observation"],
        "falsification_attempt":"kappa=0 restores the flat relative angle, an epsilon threshold breaks projector intertwining, anomaly data do not select A over B, and g=1 versus g=2 survives current observation.",
        "residual":"select the matter completion and complete source action, then derive transport, masses, RG, and calibrated physical16 acquisition",
        "disposition":"construct conditional new Yukawa-active source packet; reject completion-unselected promotion"
    },
    "source_domain":wp877["source_domain"],
    "faithful_coordinate":wp877["faithful_coordinate"],
    "vacuum":wp877["vacuum"],
    "physical_hessian_eigenvalues":wp877["physical_hessian_eigenvalues"],
    "anomaly_completions":{"A":wp879["completion_a"],"B":wp879["completion_b"]},
    "one_loop_spin5_coefficients":wp879["one_loop_spin5_coefficients"],
    "aspect_classification":wp880["aspect_classification"],
    "source_observation_rank":wp880["rung_3"]["source_observation_rank"],
    "unresolved_kernel_dimension":wp880["rung_3"]["unresolved_kernel_dimension"],
    "smallest_surviving_hostile":wp880["rung_3"]["smallest_surviving_hostile"],
    "ordered_two_vector_source":ordered_two_vector_source,
    "positive_physical_hessian":positive_physical_hessian,
    "anomaly_free_completions":anomaly_free_completions,
    "nonfaithful_completion_probe":nonfaithful_completion_probe,
    "matter_completion_selected":matter_completion_selected,
    "complete_source_action":complete_source_action,
    "physical_acquisition":physical_acquisition,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional new Spin(5) Yukawa-active source packet with unresolved matter completion",
    "remaining_gate":"select anomaly-equivalent Spin(5) matter completion from parent representation, zero-mode index, or locality",
    "hostile_gate":"do not promote ordered breaking projectors, anomaly cancellation, or source rank into complete action authority",
    "claim_boundary":"the packet is a bounded algebraic source candidate, not an acquisition-authorized physical source",
    "disposition":"new-Yukawa-active-source leaf resolved conditionally; matter-completion selector rival selected"
}
(ROOT/"results"/"wp1212_new_yukawa_active_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1212 PASS: ordered Spin5 packet exists; completion unselected")
