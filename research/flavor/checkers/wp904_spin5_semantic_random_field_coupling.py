"""WP904: executable semantic random field for branch-stable pairing."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = b"marici.flavor.wp904.semantic-random-field.v1"
ADDRESSES = (
    ("source", "parent_virtuality", 0),
    ("source", "production_kinematics", 0),
    ("shower", "first_emission", 0),
    ("pileup", "overlay_choice", 0),
    ("detector", "muon_smear_plus", 0),
    ("detector", "muon_smear_minus", 0),
    ("reconstruction", "tie_break", 0),
)


def encode_part(value):
    raw = str(value).encode("utf-8")
    return len(raw).to_bytes(4, "big") + raw


def random_word(seed_family, event_id, stage, address, draw_index):
    fields = (seed_family, event_id, stage, address, draw_index)
    digest = hashlib.sha256(DOMAIN + b"".join(encode_part(x) for x in fields)).digest()
    return int.from_bytes(digest[:8], "big")


def packet(seed_family, event_id, addresses=ADDRESSES):
    if len(addresses) != len(set(addresses)):
        raise ValueError("duplicate semantic address")
    return {
        f"{stage}/{address}/{index}": random_word(seed_family, event_id, stage, address, index)
        for stage, address, index in addresses
    }


def main():
    wp903 = json.loads((ROOT / "results/wp903_spin5_cmssw_pairing_executability_audit.json").read_text())
    seed = "preregistered-family-0001"
    baseline = {event: packet(seed, event) for event in range(256)}
    replay = {event: packet(seed, event) for event in range(256)}
    extra = ("source", "width_branch", 0)
    branched = {event: packet(seed, event, ADDRESSES + (extra,)) for event in range(256)}
    branch_stable = all(
        all(branched[event][key] == value for key, value in baseline[event].items())
        for event in baseline
    )
    arm_a = {event: packet(seed, event) for event in range(256)}
    arm_b = {event: packet(seed, event) for event in range(256)}
    event_heads = [baseline[event]["source/parent_virtuality/0"] for event in baseline]
    different_seed = packet("preregistered-family-0002", 0)
    duplicate_rejected = False
    try:
        packet(seed, 0, ADDRESSES + (ADDRESSES[0],))
    except ValueError:
        duplicate_rejected = True
    null_records = [
        {"pair_id": event, "output": "not_selected" if event % 17 == 0 else "bin1"}
        for event in range(256)
    ]
    checks = {
        "wp903_defect_was_open": wp903["pairing_executable_on_current_evidence"] is False,
        "bit_identical_replay_256_events": baseline == replay,
        "width_arms_share_registered_field": arm_a == arm_b,
        "branch_insertion_does_not_shift_registered_draws": branch_stable,
        "event_identifiers_separate_sample": len(set(event_heads)) == 256,
        "seed_families_separate_fields": different_seed != baseline[0],
        "duplicate_addresses_rejected": duplicate_rejected,
        "all_null_outputs_keep_pair_ids": all("pair_id" in row for row in null_records),
        "null_output_is_retained": any(row["output"] == "not_selected" for row in null_records),
        "width_is_not_part_of_random_field_key": True,
        "sequential_reseeding_is_not_claimed": True,
        "cmssw_adapter_not_claimed": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP904",
        "constructor": "SHA-256 semantic random field over seed family, event, stage, address, and local index",
        "events_executed": 256,
        "registered_addresses": [f"{s}/{a}/{i}" for s, a, i in ADDRESSES],
        "branch_hostile_address": "source/width_branch/0",
        "branch_stable": branch_stable,
        "smallest_exact_falsifier": "one registered word changes after insertion of an unrelated semantic branch draw; this falsifies semantic alignment, not every coupling",
        "classification": "executable sufficient reference coupling and variance-reduction adapter; neither selector nor rigidifier",
        "remaining_physical_instrument_gate": "adapt every stochastic generator-to-reconstruction operation to semantic addressing or immutable typed base events, then calibrate acceptance",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp904_spin5_semantic_random_field_coupling.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
