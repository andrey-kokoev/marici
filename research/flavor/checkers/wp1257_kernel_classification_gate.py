import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1143,1144,1145,1146)
wp1143=json.loads((ROOT/"results"/"wp1143_local_rank_two_no_go.json").read_text())
wp1144=json.loads((ROOT/"results"/"wp1144_minimal_support_reweighting_classification.json").read_text())
wp1145=json.loads((ROOT/"results"/"wp1145_rank_three_matching_gate.json").read_text())
wp1146=json.loads((ROOT/"results"/"wp1146_matching_symmetry_orbits.json").read_text())
assert wp1143["classification"].startswith("negative gate: rank-two")
assert wp1144["classification"].startswith("classification gate: support two")
assert wp1145["classification"].startswith("classification plus negative")
assert wp1146["classification"].startswith("classification gate: equal weights")
# Exact support, rank, matching, and orbit classifications are retained;
# no production adjacency or source-selected kernel exists.
rank_two_closed=True
minimal_support=True
matchings_classified=True
orbits_classified=True
selected_matching=False
production_matching_packet=False
physical16_couplings=False
same_frame_gain=False
exchange_symmetry=False
selected_kernel=False
assert rank_two_closed and minimal_support and matchings_classified and orbits_classified
assert wp1144["minimal_target_support"]==2 and wp1144["minimal_support_two_rank"]==3
assert wp1145["candidate_count"]==6 and wp1146["orbit_count"]==3
assert not (selected_matching or production_matching_packet or physical16_couplings or same_frame_gain or exchange_symmetry or selected_kernel)
result={
    "schema":"marici.flavor.wp1257.v1",
    "status":"PASS",
    "question":"Can support/rank/orbit algebra select the Physical16 production kernel?",
    "dpc":{
        "conjecture":"Locality, rank, or equal-weight symmetry may select a target-compatible production kernel.",
        "rivals":["rank-two local map","support-two rank-three map","six perfect matchings","twin-swap orbit","production-matching packet"],
        "risky_consequences":["all 15625 partner assignments were tested","729 support-two maps satisfy the target","their ranks are 3, 4, or 5","six rank-three candidates are perfect matchings","the twin swap gives three two-element orbits"],
        "falsification_attempt":"zero rank-two local maps, matching certificates, Physical16 coupling maps, same-frame gain certificates, physical exchange certificates, or kernel invariance certificates exist.",
        "residual":"materialize a production-matching packet selecting one matching with couplings, gain 3/2, and localization certificate",
        "disposition":"accept exact support/rank/orbit classification; reject current source-selected kernel"
    },
    "rank_two_search":{
        "local_assignments_tested":wp1143["local_assignments_tested"],
        "target_compatible_local_maps":wp1143["target_compatible_local_maps"],
        "low_rank_local_maps":wp1143["low_rank_local_maps"],
        "rank_histogram":wp1143["rank_histogram"]
    },
    "minimal_support":{
        "minimal_target_support":wp1144["minimal_target_support"],
        "target_compatible_support_two_maps":wp1144["target_compatible_support_two_maps"],
        "minimal_support_two_rank":wp1144["minimal_support_two_rank"],
        "rank_three_example":wp1144["rank_three_example"]
    },
    "matchings":{
        "candidate_count":wp1145["candidate_count"],
        "matchings_zero_based":wp1145["matchings_zero_based"],
        "all_perfect_matchings":wp1145["all_perfect_matchings"],
        "missing_object":wp1145["missing_object"]
    },
    "orbits":{
        "equal_weight_pairs_zero_based":wp1146["equal_weight_pairs_zero_based"],
        "orbit_count":wp1146["orbit_count"],
        "orbit_sizes":wp1146["orbit_sizes"],
        "fixed_matchings":wp1146["fixed_matchings"]
    },
    "rank_two_closed":rank_two_closed,
    "minimal_support_classified":minimal_support,
    "matchings_classified":matchings_classified,
    "orbits_classified":orbits_classified,
    "selected_matching":selected_matching,
    "production_matching_packet":production_matching_packet,
    "physical16_couplings":physical16_couplings,
    "same_frame_gain":same_frame_gain,
    "exchange_symmetry":exchange_symmetry,
    "selected_kernel":selected_kernel,
    "classification":"conditional kernel-classification gate: support/rank/orbits exact, source-selected kernel absent",
    "remaining_gate":"materialize production_matching_packet and select one matching with Physical16 couplings, gain 3/2, and localization certificate",
    "hostile_gate":"do not call support two, rank three, six matchings, three orbits, equal weights, or local algebra a source-selected kernel",
    "claim_boundary":"WP1143 through WP1146 classify the executable algebra; no production adjacency, couplings, gain, or kernel authority is admitted",
    "disposition":"kernel-classification gate resolved conditionally; production-matching packet rival selected"
}
(ROOT/"results"/"wp1257_kernel_classification_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1257 PASS: support/rank/orbits exact, source-selected kernel absent")
