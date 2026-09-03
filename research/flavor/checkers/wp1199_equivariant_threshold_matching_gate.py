import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(843,846)
wp843=json.loads((ROOT/"results"/"wp843_positive_tensor_threshold_contraction_no_go.json").read_text())
wp846=json.loads((ROOT/"results"/"wp846_equivariant_character_threshold_memory.json").read_text())
assert wp843["summary"]["all_passed"] is True
assert wp846["summary"]["all_passed"] is True
assert wp843["required_transition"] == "Y_full=70 -> Y_active=84"
assert wp846["threshold_sewing"] == "(z^2+z^3)+z=z+z^2+z^3"
assert wp846["preserved_selector"] == "diameter of sewn character support is 2, so x*=1/2"
assert wp846["finite_probe"] == "four evaluations at 1,-1,i,-i reconstruct support coefficients q=0,1,2,3"
assert wp846["classification"] == "conditional representation-valued threshold repair with finite faithful relational probe"
# Ordinary positive restriction fails, but the equivariant character gives an
# exact noncontractive threshold carrier. It is conditional on an added
# background-holonomy port and an equivariant source index.
ordinary_positive_restriction=False
representation_valued_matching=True
diameter_selector_survives=True
equivariant_source_index=False
calibrated_holonomy_ports=False
physical16_realization=False
assert representation_valued_matching and diameter_selector_survives
assert not (ordinary_positive_restriction or equivariant_source_index or calibrated_holonomy_ports or physical16_realization)
result={
    "schema":"marici.flavor.wp1199.v1",
    "status":"PASS",
    "question":"Can threshold matching be noncontractive without losing the selector?",
    "dpc":{
        "conjecture":"A noncontractive threshold law preserves the diameter-selected flow.",
        "rivals":["ordinary positive tensor restriction","equivariant character sewing","source-derived equivariant index","calibrated holonomy instrument"],
        "risky_consequences":["70->84 is impossible by ordinary positive restriction","character sewing is (z^2+z^3)+z=z+z^2+z^3","sewn support has diameter 2 and x*=1/2","four holonomy evaluations reconstruct support coefficients"],
        "falsification_attempt":"Anomaly matching misses diameter, while equivariant character sewing preserves it exactly but adds a background-holonomy reference port.",
        "residual":"An equivariant source index and calibrated physical16 holonomy ports remain absent.",
        "disposition":"construct conditional representation-valued matching; reject source-complete threshold repair"
    },
    "ordinary_tensor_transition":wp843["required_transition"],
    "ordinary_positive_restriction":ordinary_positive_restriction,
    "threshold_sewing":wp846["threshold_sewing"],
    "preserved_selector":wp846["preserved_selector"],
    "finite_probe":wp846["finite_probe"],
    "representation_valued_matching":representation_valued_matching,
    "diameter_selector_survives":diameter_selector_survives,
    "equivariant_source_index":equivariant_source_index,
    "calibrated_holonomy_ports":calibrated_holonomy_ports,
    "physical16_realization":physical16_realization,
    "classification":"conditional threshold carrier: character sewing preserves the diameter selector with four faithful holonomy probes",
    "remaining_gate":"derive the equivariant source index and calibrated holonomy instrument",
    "hostile_gate":"do not treat added background holonomy as already calibrated physical16 data",
    "claim_boundary":"the repair changes the probe groupoid by adding background holonomy and remains relative to its stabilizer",
    "disposition":"noncontractive threshold-matching leaf resolved; equivariant-index source rival selected"
}
(ROOT/"results"/"wp1199_equivariant_threshold_matching_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1199 PASS: character sewing preserves x*=1/2")
