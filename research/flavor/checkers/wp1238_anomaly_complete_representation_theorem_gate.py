import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1040,1041,1042)
wp1040=json.loads((ROOT/"results"/"wp1040_degenerate_pole_clock_fiber.json").read_text())
wp1041=json.loads((ROOT/"results"/"wp1041_momentum_port_calibration_fiber.json").read_text())
wp1042=json.loads((ROOT/"results"/"wp1042_ratio_to_physical16_gain_fiber.json").read_text())
assert wp1040["classification"] == "exchange-enforced degeneracy is a threshold rigidifier, not a mass-clock selector"
assert wp1041["classification"] == "finite response is faithful to p2/M2 on the degenerate one-pole domain; it is not an absolute mass or source selector"
assert wp1042["classification"] == "source-locked threshold ratio would be a shape selector, not an absolute physical16 normalization selector"
# Even after granting integer selection and degenerate-pole typing, the
# threshold clock, calibrated port, ratio, and detector gain remain separate
# missing source arrows.
degeneracy_rigidifies=True
mass_clock_unfixed=True
momentum_port_unfixed=True
threshold_shape_locked=True
physical16_gain_unfixed=True
representation_theorem=False
calibrated_port=False
source_ratio=False
gain_law=False
interference_monitor=False
assert degeneracy_rigidifies and mass_clock_unfixed and momentum_port_unfixed
assert threshold_shape_locked and physical16_gain_unfixed
assert not (representation_theorem or calibrated_port or source_ratio or gain_law or interference_monitor)
result={
    "schema":"marici.flavor.wp1238.v1",
    "status":"PASS",
    "question":"Would an anomaly-complete representation theorem complete the integer-pole source packet?",
    "dpc":{
        "conjecture":"Selecting k=2,C=23 and the degenerate pole operator completes the source packet.",
        "rivals":["exchange-enforced pole degeneracy","finite threshold response","calibrated momentum port","source-locked p squared over M squared ratio","source-to-detector gain law"],
        "risky_consequences":["M squared=1 and M squared=2 packets share all zero-momentum data","response depends only on p squared over M squared","the ratio p squared over M squared=1 fixes shape 1/2","interface gains g=1 and g=2 produce different Physical16 rows","normalized fractions collide at one"],
        "falsification_attempt":"granting the representation theorem and pole type leaves three independent fibers: mass clock, momentum calibration, and detector gain.",
        "residual":"source-derived physical pole mass or locked ratio, common-frame calibrated momentum port, and source-to-Yukawa/detector gain or interference monitor",
        "disposition":"reject representation-theorem sufficiency; select source-detector gain-law rival"
    },
    "zero_momentum_data":wp1040["fixed_zero_momentum_data"],
    "hostile_degenerate_packets":wp1040["hostile_degenerate_packets"],
    "response_law":wp1041["response_law"],
    "common_scale_hostile":wp1041["common_scale_hostile"],
    "threshold_shape":wp1042["threshold_shape"],
    "hostile_interface_gains":wp1042["hostile_interface_gains"],
    "normalized_fraction_collision":wp1042["normalized_fraction_collision"],
    "degeneracy_rigidifies":degeneracy_rigidifies,
    "mass_clock_unfixed":mass_clock_unfixed,
    "momentum_port_unfixed":momentum_port_unfixed,
    "threshold_shape_locked":threshold_shape_locked,
    "physical16_gain_unfixed":physical16_gain_unfixed,
    "representation_theorem":representation_theorem,
    "calibrated_port":calibrated_port,
    "source_ratio":source_ratio,
    "gain_law":gain_law,
    "interference_monitor":interference_monitor,
    "classification":"conditional representation gate: even granted integer and pole selection, absolute Physical16 gain remains absent",
    "remaining_gate":"derive the source-to-Yukawa or source-to-detector gain in the threshold frame, with absolute or interference-calibrated Physical16 readout",
    "hostile_gate":"do not call degeneracy, threshold shape, calibrated momentum ratio, or normalized fractions an absolute Physical16 prediction",
    "claim_boundary":"the theorem would select labels and pole type but not detector normalization; all downstream fibers remain explicit",
    "disposition":"anomaly-complete-representation-theorem leaf resolved conditionally; source-detector gain-law rival selected"
}
(ROOT/"results"/"wp1238_anomaly_complete_representation_theorem_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1238 PASS: representation theorem insufficient; source-detector gain law required")
