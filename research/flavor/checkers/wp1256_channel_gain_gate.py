import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1139,1140,1141,1142)
wp1139=json.loads((ROOT/"results"/"wp1139_physical16_two_port_channel_no_go.json").read_text())
wp1140=json.loads((ROOT/"results"/"wp1140_vector_kk_gain_chain_uniqueness.json").read_text())
wp1141=json.loads((ROOT/"results"/"wp1141_gain_compatibility_no_go.json").read_text())
wp1142=json.loads((ROOT/"results"/"wp1142_common_gain_reweighting_map_classification.json").read_text())
assert wp1139["classification"].startswith("negative gate: conditional momentum")
assert wp1140["classification"].startswith("conditional vector-ratio")
assert wp1141["classification"].startswith("negative gate: the two exact gain")
assert wp1142["classification"].startswith("classification gate")
# Exact rows and map family are retained, but no physical16 channel packet,
# common scalar gain, or unique production kernel is sourced.
rows_exact=True
vector_carrier=True
map_family=True
physical16_channels=False
common_gain=False
unique_kernel=False
cascade_certificate=False
production_maps=False
same_frame=False
physical_ratio_law=False
assert rows_exact and vector_carrier and map_family
assert wp1139["realized_physical16_channels"]==0 and wp1141["common_gain_compatible"] is False and wp1142["solution_space"]["unique"] is False
assert not (physical16_channels or common_gain or unique_kernel or cascade_certificate or production_maps or same_frame or physical_ratio_law)
result={
    "schema":"marici.flavor.wp1256.v1",
    "status":"PASS",
    "question":"Can current rows and gains calibrate the physical16 two-port ratio law?",
    "dpc":{
        "conjecture":"The exact two-port rows, vector gain chain, or common reweighting gain may calibrate physical16 channels and production maps.",
        "rivals":["two-port physical16 channels","vector-KK gain chain","common scalar gain","rank-one complete mixing","rank-two/localized map"],
        "risky_consequences":["soft and vector rows have ratios 1 and 4 with responses 1/2 and 1/5","the vector event cell reconstructs uniquely at g=1,L=1/5","g=3/2 changes S,D to 9/20,3/5","the reweighting family M=U+A has affine dimension 24"],
        "falsification_attempt":"zero physical16 channels or production maps exist; event-cell gain 1 is incompatible with reweighting gain 3/2 as one scalar; q and r do not uniquely select complete mixing.",
        "residual":"materialize physical16_channel_packet and physical16_gain_cascade_certificate, then select a production-local map",
        "disposition":"retain exact rows and map classification conditionally; reject current channel/gain authority"
    },
    "two_port_rows":wp1139["rows"],
    "physical16_channel_packet":wp1139["missing_object"],
    "vector_gain_chain":{
        "retained_rows":wp1140["retained_rows"],
        "reconstruction":wp1140["reconstruction"],
        "target_gain_hostile":wp1140["target_gain_hostile"],
        "pure_rate_laundering_hostile":wp1140["pure_rate_laundering_hostile"]
    },
    "gain_compatibility":{
        "event_cell_gain":wp1141["event_cell_gain"],
        "reweighting_gain":wp1141["reweighting_gain"],
        "event_rows":wp1141["event_rows"],
        "reweighted_rows":wp1141["reweighted_rows"],
        "missing_object":wp1141["missing_object"]
    },
    "map_classification":{
        "source_q":wp1142["source_q"],
        "target_r":wp1142["target_r"],
        "gain":wp1142["gain"],
        "rank_one_map":wp1142["rank_one_map"],
        "rank_two_example":wp1142["rank_two_example"],
        "solution_space":wp1142["solution_space"]
    },
    "rows_exact":rows_exact,
    "vector_carrier_unique":vector_carrier,
    "map_family_classified":map_family,
    "realized_physical16_channels":wp1139["realized_physical16_channels"],
    "common_gain_compatible":wp1141["common_gain_compatible"],
    "unique_kernel":unique_kernel,
    "cascade_certificate":cascade_certificate,
    "production_maps":production_maps,
    "same_frame_certificate":same_frame,
    "physical_ratio_law":physical_ratio_law,
    "classification":"conditional channel/gain gate: exact rows and map family, physical16 packet absent",
    "remaining_gate":"materialize physical16 channel and gain-cascade packets, then select a production-local map",
    "hostile_gate":"do not call exact rows, g=1 reconstruction, common-gain labels, complete mixing, or affine map families calibrated physical16 authority",
    "claim_boundary":"WP1139 through WP1142 classify conditional data and close common-gain authority; no physical16 channel or kernel is sourced",
    "disposition":"channel/gain gate resolved conditionally; physical16 channel-cascade packet rival selected"
}
(ROOT/"results"/"wp1256_channel_gain_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1256 PASS: exact rows and map family, physical16 packet absent")
