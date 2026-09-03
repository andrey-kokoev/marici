import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1147,1148,1149)
wp1147=json.loads((ROOT/"results"/"wp1147_twin_exchange_no_go.json").read_text())
wp1148=json.loads((ROOT/"results"/"wp1148_quartet_quotient_gate.json").read_text())
wp1149=json.loads((ROOT/"results"/"wp1149_quotient_anomaly_invariance.json").read_text())
assert wp1147["classification"].startswith("negative gate: formal pre-localization")
assert wp1148["classification"].startswith("conditional quotient")
assert wp1149["classification"].startswith("negative gate: anomaly")
# The exchange relation and quotient algebra are exact, but neither selects
# a post-localization symmetry, production quotient, or matching class.
exchange_relation=True
quotient_algebra=True
anomaly_invariance=True
unbroken_exchange=False
production_quotient=False
selected_matching_class=False
physical16_couplings=False
same_frame_gain=False
selected_kernel=False
assert exchange_relation and quotient_algebra and anomaly_invariance
assert wp1148["matching_classes_after_quotient"]==3 and wp1149["selected_classes"]==0
assert not (unbroken_exchange or production_quotient or selected_matching_class or physical16_couplings or same_frame_gain or selected_kernel)
result={
    "schema":"marici.flavor.wp1258.v1",
    "status":"PASS",
    "question":"Can exchange, quotient, or anomaly data select a production matching?",
    "dpc":{
        "conjecture":"Twin exchange, quartet quotient, or anomaly invariance may select one of the three quotient matching classes.",
        "rivals":["post-localization twin exchange","quartet-choice quotient","anomaly-selected matching class","boundary S-matrix phase data"],
        "risky_consequences":["exchange relates two one-quartet cells","the quotient has shared C=23,k=2,q and three matching classes","all five-channel and seven-channel anomaly differences vanish","a selected class needs production couplings and same-frame gain"],
        "falsification_attempt":"exchange fixes no selected cell, the quotient supplies no production map, and anomaly data are class-independent with zero selected classes.",
        "residual":"test boundary S-matrix phase data against the three quotient matching classes",
        "disposition":"accept exchange/quotient/anomaly classifications; reject current matching selection"
    },
    "twin_exchange":{
        "quartet_choices":wp1147["quartet_choices"],
        "selected_cells":wp1147["selected_cells"],
        "prelocalization_formal_exchange":wp1147["prelocalization_formal_exchange"],
        "exchange_fixed_selected_cells":wp1147["exchange_fixed_selected_cells"],
        "missing_object":wp1147["missing_object"]
    },
    "quotient":{
        "shared_invariants":wp1148["shared_invariants"],
        "algebraic_quotient_well_defined":wp1148["algebraic_quotient_well_defined"],
        "matching_classes_after_quotient":wp1148["matching_classes_after_quotient"],
        "production_quotient_maps":wp1148["production_quotient_maps"]
    },
    "anomaly_invariance":{
        "quotient_classes":wp1149["quotient_classes"],
        "five_channel_vector":wp1149["five_channel_vector"],
        "seven_channel_vector":wp1149["seven_channel_vector"],
        "shifted_coset":wp1149["shifted_coset"],
        "pairwise_differences_zero":wp1149["pairwise_differences_zero"]
    },
    "exchange_relation_exact":exchange_relation,
    "quotient_algebra_exact":quotient_algebra,
    "anomaly_invariance_exact":anomaly_invariance,
    "unbroken_exchange":unbroken_exchange,
    "production_quotient":production_quotient,
    "selected_matching_class":selected_matching_class,
    "physical16_couplings":physical16_couplings,
    "same_frame_gain":same_frame_gain,
    "selected_kernel":selected_kernel,
    "classification":"conditional matching-selection gate: exchange, quotient, and anomaly facts exact, selected class absent",
    "remaining_gate":"test boundary S-matrix phase data against the three quotient matching classes or materialize a production quotient",
    "hostile_gate":"do not call pre-localization exchange, label quotient, shared anomaly vectors, or class invariance a selected production matching",
    "claim_boundary":"WP1147 through WP1149 classify symmetry and anomaly data; no post-localization symmetry, quotient production map, couplings, gain, or kernel is sourced",
    "disposition":"matching-selection gate resolved conditionally; S-matrix phase rival selected"
}
(ROOT/"results"/"wp1258_matching_selection_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1258 PASS: exchange, quotient, and anomaly facts exact, selected class absent")
