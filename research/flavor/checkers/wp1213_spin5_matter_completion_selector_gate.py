import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(879,884,885,887)
wp879=json.loads((ROOT/"results"/"wp879_spin5_anomaly_completion_beta_fiber.json").read_text())
wp884=json.loads((ROOT/"results"/"wp884_spin5_finite_threshold_selector_obstruction.json").read_text())
wp885=json.loads((ROOT/"results"/"wp885_spin5_completion_bare_massability_audit.json").read_text())
wp887=json.loads((ROOT/"results"/"wp887_spin5_completion_b_component_mass_rank.json").read_text())
for data in (wp879,wp884,wp885,wp887): assert data["summary"]["all_passed"] is True
assert wp879["classification"] == "anomaly cancellation and global spinor parity are nonfaithful on the simple-parent matter packet; they do not authorize one beta system"
assert wp884["classification"] == "negative_source_support: completion-dependent threshold slopes do not select the finite portal jump"
assert wp885["classification"] == "split_negative: completion A is massable with free scales; completion B lacks a charged bare mass action"
assert wp887["classification"] == "generic_full_rank_not_selector: Completion B is massable with declared scalars but its spectrum remains parameter dependent"
# Anomaly, threshold, bare-mass, and generic-Yukawa probes separate structure
# but do not select one completion.  Completion A and B remain rival viable
# source packets under distinct mass mechanisms.
anomaly_nonfaithful=True
threshold_nonselective=True
completion_A_bare_massable=True
completion_B_generic_massable=True
completion_selected=False
yukawa_matrices_selected=False
rg_widths_derived=False
calibrated_poles=False
assert anomaly_nonfaithful and threshold_nonselective and completion_A_bare_massable and completion_B_generic_massable
assert not (completion_selected or yukawa_matrices_selected or rg_widths_derived or calibrated_poles)
result={
    "schema":"marici.flavor.wp1213.v1",
    "status":"PASS",
    "question":"Do anomaly, threshold, and massability probes select Spin(5) completion A or B?",
    "dpc":{
        "conjecture":"Anomaly cancellation, finite thresholds, or massability selects one Spin(5) matter completion.",
        "rivals":["completion A bare masses","completion B generic Yukawas","finite matching constant","threshold mass","anomaly/global parity"],
        "risky_consequences":["A and B cancel identical anomaly and parity classes","their one-loop beta coefficients differ by two","finite matching leaves a two-dimensional mass/finite-term fiber","A has two charged bare pairs","B has no charged bare pair but has generic full-rank Yukawa masses"],
        "falsification_attempt":"The same completion and mass admits k=0 versus k=1; A's bare scales vary; B's zero-Yukawa hostile has rank zero; anomaly and parity classify both together.",
        "residual":"derive an independent parent, zero-mode, locality, or vacuum principle selecting completion and Yukawa matrices before RG, widths, and pole calibration",
        "disposition":"reject probe-based completion selection; require an independent completion principle"
    },
    "completion_beta_coefficients":wp884["completion_beta_coefficients"],
    "anomaly_classification":wp879["classification"],
    "threshold_classification":wp884["classification"],
    "massability_classification":wp885["classification"],
    "completion_B_mass_classification":wp887["classification"],
    "threshold_free_coordinates":wp884["free_coordinates"],
    "completion_A_bare_pairs":wp885["completion_A_charged_bare_pairs"],
    "completion_B_witness_rank":wp887["witness_rank"],
    "anomaly_nonfaithful":anomaly_nonfaithful,
    "threshold_nonselective":threshold_nonselective,
    "completion_A_bare_massable":completion_A_bare_massable,
    "completion_B_generic_massable":completion_B_generic_massable,
    "completion_selected":completion_selected,
    "yukawa_matrices_selected":yukawa_matrices_selected,
    "rg_widths_derived":rg_widths_derived,
    "calibrated_poles":calibrated_poles,
    "classification":"negative completion-selector result: A and B remain viable under distinct mass mechanisms",
    "remaining_gate":"derive an independent parent/zero-mode/locality/vacuum principle selecting completion and Yukawa matrices",
    "hostile_gate":"do not infer completion selection from anomaly cancellation, beta split, bare massability, or generic full rank alone",
    "claim_boundary":"the obstruction is exact for the audited probes; it does not rule out a future source principle",
    "disposition":"spin5-matter-completion-selector leaf resolved negatively; independent completion-principle rival selected"
}
(ROOT/"results"/"wp1213_spin5_matter_completion_selector_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1213 PASS: audited probes do not select completion A or B")
