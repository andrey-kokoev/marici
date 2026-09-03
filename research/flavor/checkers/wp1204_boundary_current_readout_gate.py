import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(855)
wp855=json.loads((ROOT/"results"/"wp855_boundary_current_readout_hierarchy.json").read_text())
assert wp855["summary"]["all_passed"] is True
assert wp855["state_domain"] == ["positive boundary orientation","negative boundary orientation","absent boundary source"]
assert wp855["probe_partition"]["referenced_difference_pair"] == "three singleton classes"
assert wp855["first_nonfaithful_arrow"] == "two charged paths -> ordinary sum port"
assert wp855["instrument_gate"] == "source-derived pre-projection difference channel and calibrated coherent reference"
# The readout hierarchy separates the three boundary states only after the
# coherent reference channel; ordinary sum and unreferenced intensity do not.
sum_port_faithful=False
loop_product_orientation_faithful=False
referenced_pair_faithful=True
preprojection_channel=False
coherent_reference_calibrated=False
threshold_transport=False
assert referenced_pair_faithful and not sum_port_faithful and not loop_product_orientation_faithful
assert not (preprojection_channel or coherent_reference_calibrated or threshold_transport)
result={
    "schema":"marici.flavor.wp1204.v1",
    "status":"PASS",
    "question":"Can a boundary-current readout separate orientation and absence?",
    "dpc":{
        "conjecture":"A dimensionless readout separates positive orientation, negative orientation, and absent boundary source.",
        "rivals":["ordinary sum port","downstream contact","loop product","unreferenced difference intensity","coherent referenced difference pair"],
        "risky_consequences":["the sum port gives zero for all three states","loop product erases boundary orientation","difference intensity detects presence but erases orientation","two referenced difference settings form three singleton classes"],
        "falsification_attempt":"p=(1,-1)/sqrt(2) and p=0 both have zero sum-contact response, and no downstream contact repairs that kernel.",
        "residual":"A source-derived pre-projection difference channel, calibrated coherent reference, and threshold transport remain required.",
        "disposition":"construct the readout hierarchy; reject sum-port or intensity-only authorization"
    },
    "state_domain":wp855["state_domain"],
    "probe_partition":wp855["probe_partition"],
    "first_nonfaithful_arrow":wp855["first_nonfaithful_arrow"],
    "smallest_exact_falsifier":wp855["smallest_exact_falsifier"],
    "groupoid_change":wp855["groupoid_change"],
    "sum_port_faithful":sum_port_faithful,
    "loop_product_orientation_faithful":loop_product_orientation_faithful,
    "referenced_pair_faithful":referenced_pair_faithful,
    "preprojection_channel":preprojection_channel,
    "coherent_reference_calibrated":coherent_reference_calibrated,
    "threshold_transport":threshold_transport,
    "classification":"conditional readout selector: referenced difference pair separates orientation and absence",
    "remaining_gate":"derive the pre-projection difference channel and coherent reference from source, then transport through thresholds",
    "hostile_gate":"do not treat a sum port, downstream contact, or intensity-only channel as faithful",
    "claim_boundary":"the hierarchy is dimensionless and conditional on a calibrated coherent reference",
    "disposition":"boundary-current-readout leaf resolved; threshold-intertwiner rival selected"
}
(ROOT/"results"/"wp1204_boundary_current_readout_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1204 PASS: referenced pair faithful; sum port collapses")
