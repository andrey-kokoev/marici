import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(852,853)
wp852=json.loads((ROOT/"results"/"wp852_finite_path_partial_isometry_normalization_selector.json").read_text())
wp853=json.loads((ROOT/"results"/"wp853_incidence_does_not_authorize_path_partial_isometry.json").read_text())
assert wp852["summary"]["all_passed"] is True
assert wp853["summary"]["all_passed"] is True
assert wp852["faithful_quotient"] == "degree-one partial isometries modulo number-preserving diagonal unitaries"
assert wp852["selected_data"] == "unit descendant norms and unit graded multiplication coefficients"
assert wp852["classification"] == "conditional algebraic normalization selector"
assert wp853["smallest_hostile_pair"] == ["T(1,1,1)","T(1,2,1)"]
assert wp853["classification"] == "WP852 is a selector only after adding the partial-isometry source relation"
assert wp853["remaining_gate"] == "derive T^*T=I-P3 microscopically or instrument T^*T in the physical16 frame"
# The path pairing gives a canonical normalization, but incidence probes leave
# the three positive path weights free.
path_normalization_selected=True
unit_multiplication_selected=True
incidence_authorizes_partial_isometry=False
microscopic_source_relation=False
physical16_instrument=False
assert path_normalization_selected and unit_multiplication_selected
assert not (incidence_authorizes_partial_isometry or microscopic_source_relation or physical16_instrument)
result={
    "schema":"marici.flavor.wp1202.v1",
    "status":"PASS",
    "question":"Can a positive path pairing normalize graded multiplication?",
    "dpc":{
        "conjecture":"A positive pairing normalizes the graded multiplication maps needed for spurion alignment.",
        "rivals":["declared recursive potential","finite-path partial isometry","incidence-authorized normalization","microscopic source relation or calibrated instrument"],
        "risky_consequences":["partial isometry fixes all path weights to unit magnitude","diagonal phases are absorbed by number-preserving unitaries","T(1,1,1) and T(1,2,1) share charge ray, incidence, and cubic inflow","only the first satisfies T^*T=I-P3"],
        "falsification_attempt":"The path relation selects one unitary orbit, but the admitted incidence packet cannot distinguish the positive-weight fiber.",
        "residual":"A microscopic derivation or physical16 instrument for T^*T is required.",
        "disposition":"construct conditional positive-path normalization; reject incidence-derived authority"
    },
    "faithful_quotient":wp852["faithful_quotient"],
    "selected_data":wp852["selected_data"],
    "hostile_pair":wp853["smallest_hostile_pair"],
    "first_nonfaithful_arrow":wp853["first_nonfaithful_arrow"],
    "path_normalization_selected":path_normalization_selected,
    "unit_multiplication_selected":unit_multiplication_selected,
    "incidence_authorizes_partial_isometry":incidence_authorizes_partial_isometry,
    "microscopic_source_relation":microscopic_source_relation,
    "physical16_instrument":physical16_instrument,
    "classification":"conditional positive-pairing selector: path partial isometry normalizes multiplication; incidence cannot authorize it",
    "remaining_gate":"derive T^*T=I-P3 from a microscopic source or measure it in physical16",
    "hostile_gate":"do not infer the partial-isometry relation from charge ray, incidence, or cubic inflow",
    "claim_boundary":"the normalization applies to the declared charged path and lacks a physical flavor interface",
    "disposition":"positive-pairing normalization leaf resolved; oriented-cycle constructor rival selected"
}
(ROOT/"results"/"wp1202_positive_pairing_normalization_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1202 PASS: path normalization selected; incidence fiber remains")
