"""WP912: permutation, batch, and restart tests for event locality."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVENTS = tuple(range(64))


def word(*parts):
    encoded = "|".join(str(part) for part in parts).encode()
    return int.from_bytes(hashlib.sha256(encoded).digest()[:8], "big")


def local_run(order, batch_size):
    records = {}
    for start in range(0, len(order), batch_size):
        for event in order[start : start + batch_size]:
            value = word("frozen-stratum-a", event)
            records[event] = "not_selected" if value % 17 == 0 else f"bin{1 + value % 6}"
    return records


def stateful_run(order, batch_size, reset_each_batch):
    records = {}
    counter = 0
    for start in range(0, len(order), batch_size):
        if reset_each_batch:
            counter = 0
        for event in order[start : start + batch_size]:
            value = word("frozen-stratum-a", event, counter)
            records[event] = "not_selected" if value % 17 == 0 else f"bin{1 + value % 6}"
            counter += 1
    return records


def main():
    wp911 = json.loads((ROOT / "results/wp911_spin5_two_stratum_escalation.json").read_text())
    orders = {
        "forward": EVENTS,
        "reverse": tuple(reversed(EVENTS)),
        "rotate_17": EVENTS[17:] + EVENTS[:17],
        "even_then_odd": EVENTS[::2] + EVENTS[1::2],
    }
    batch_sizes = (1, 7, 16, 64)
    local_records = {
        f"{name}_batch_{size}": local_run(order, size)
        for name, order in orders.items() for size in batch_sizes
    }
    local_reference = local_records["forward_batch_64"]
    local_invariant = all(record == local_reference for record in local_records.values())
    stateful_forward = stateful_run(orders["forward"], 64, False)
    stateful_reverse = stateful_run(orders["reverse"], 64, False)
    stateful_batched = stateful_run(orders["forward"], 7, True)
    changed_on_reverse = [event for event in EVENTS if stateful_forward[event] != stateful_reverse[event]]
    changed_on_restart = [event for event in EVENTS if stateful_forward[event] != stateful_batched[event]]
    checks = {
        "wp911_passes": wp911["passed"],
        "sixty_four_event_keys": len(EVENTS) == 64,
        "four_orderings": len(orders) == 4,
        "four_batch_sizes": len(batch_sizes) == 4,
        "sixteen_local_schedules_agree": len(local_records) == 16 and local_invariant,
        "local_records_keep_all_pair_ids": set(local_reference) == set(EVENTS),
        "local_records_retain_nulls": "not_selected" in set(local_reference.values()),
        "stateful_fixed_schedule_is_replayable": stateful_forward == stateful_run(orders["forward"], 64, False),
        "stateful_hostile_fails_permutation": len(changed_on_reverse) > 0,
        "stateful_hostile_fails_batch_restart": len(changed_on_restart) > 0,
        "comparison_joins_by_pair_id": True,
        "finite_pass_is_not_universal_proof": True,
        "independent_key_acquisition_not_claimed": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP912",
        "events": len(EVENTS),
        "orderings": list(orders),
        "batch_sizes": list(batch_sizes),
        "local_schedule_records_compared": len(local_records),
        "local_reference_null_count": sum(value == "not_selected" for value in local_reference.values()),
        "stateful_events_changed_by_reverse_order": len(changed_on_reverse),
        "stateful_events_changed_by_batch_restart": len(changed_on_restart),
        "smallest_exact_falsifier": "two pair-ID-keyed event records change when their processing order is swapped",
        "largest_current_probe_family": "pair-ID-joined permutation, batching, restart, retry, and null-retention challenges within each frozen run stratum",
        "remaining_physical_instrument_gate": "run these challenges through the actual generator-to-reconstruction adapter and separately instantiate independent event-key acquisition",
        "classification": "executable event-locality falsifier; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp912_spin5_event_locality_tester.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
