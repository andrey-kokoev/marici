import json
from pathlib import Path


def sample(source: int, phase5: int) -> tuple[int, int]:
    return source % 4, (source + phase5) % 5


def decode(record: tuple[int, int], phase5: int) -> int:
    a, b = record
    return (5 * a + 16 * ((b - phase5) % 5)) % 20


def fold(events: list[dict]) -> dict:
    state = {
        "logical_id": "optic-actor-1",
        "frame": None,
        "record": None,
        "pilot": None,
        "route": None,
        "pending": [],
        "verdicts": [],
    }
    for event in events:
        kind = event["kind"]
        if kind == "frame_bound":
            state["frame"] = event.copy()
        elif kind == "record_received":
            state["record"] = event.copy()
            state["pending"] = ["decode"]
        elif kind == "pilot_received":
            state["pilot"] = event.copy()
        elif kind == "route_bound":
            state["route"] = event.copy()
        elif kind == "decode_requested":
            state["verdicts"].append(decode_verdict(state))
        else:
            raise AssertionError(f"unknown event kind: {kind}")
    return state


def decode_verdict(state: dict) -> dict:
    frame = state["frame"]
    record = state["record"]
    pilot = state["pilot"]
    route = state["route"]
    if frame is None or record is None:
        return {"status": "unavailable", "reason": "missing_frame_or_record"}

    if record["epoch"] == frame["epoch"] and record["run"] == frame["run"]:
        return {
            "status": "decoded",
            "source": decode(tuple(record["residues"]), frame["phase5"]),
            "transport": "identity",
        }

    if pilot is None:
        return {"status": "transport_unavailable", "reason": "pilot_missing"}
    if pilot.get("revision") is None:
        return {"status": "transport_unavailable", "reason": "pilot_revision_missing"}
    if pilot["run"] != record["run"]:
        return {"status": "rejected", "reason": "cross_run_pilot_splice"}
    if pilot["preparation_id"] != record["preparation_id"]:
        return {"status": "rejected", "reason": "cross_preparation_pilot_splice"}
    if pilot["revision"] != frame["revision"]:
        return {"status": "rejected", "reason": "pilot_revision_mismatch"}
    if route is None:
        return {"status": "transport_unavailable", "reason": "route_missing"}
    route_signature = (
        route["connection_id"],
        route["preparation_id"],
        route["revision"],
        route["from_epoch"],
        route["to_epoch"],
    )
    required_signature = (
        frame["connection_id"],
        record["preparation_id"],
        pilot["revision"],
        record["epoch"],
        frame["epoch"],
    )
    if route_signature != required_signature:
        return {"status": "rejected", "reason": "route_witness_mismatch"}

    recovered_phase = pilot["residues"][1]
    return {
        "status": "decoded",
        "source": decode(tuple(record["residues"]), recovered_phase),
        "transport": "source_related_pilot",
    }


frame = {
    "kind": "frame_bound",
    "run": "run-live",
    "epoch": "epoch-0",
    "phase5": 0,
    "revision": "pilot-v1",
    "connection_id": "connection-7",
}
record = {
    "kind": "record_received",
    "run": "run-live",
    "epoch": "epoch-1",
    "preparation_id": "pulse-101",
    "residues": list(sample(1, 1)),
}
related_pilot = {
    "kind": "pilot_received",
    "run": "run-live",
    "epoch": "epoch-1",
    "preparation_id": "pulse-101",
    "revision": "pilot-v1",
    "residues": list(sample(0, 1)),
}
spliced_pilot = {**related_pilot, "run": "run-other"}
wrong_preparation_pilot = {
    **related_pilot,
    "preparation_id": "pulse-102",
    "residues": list(sample(0, 2)),
}
numerically_equal_wrong_preparation_pilot = {
    **related_pilot,
    "preparation_id": "pulse-102",
}
revisionless_pilot = {**related_pilot, "revision": None}
route = {
    "kind": "route_bound",
    "connection_id": "connection-7",
    "preparation_id": "pulse-101",
    "revision": "pilot-v1",
    "from_epoch": "epoch-1",
    "to_epoch": "epoch-0",
}
wrong_connection_route = {**route, "connection_id": "connection-other"}
reverse_route = {**route, "from_epoch": "epoch-0", "to_epoch": "epoch-1"}
request = {"kind": "decode_requested"}

premature = fold([frame, record, request])["verdicts"][-1]
missing_route = fold([frame, record, related_pilot, request])["verdicts"][-1]
valid = fold([frame, record, related_pilot, route, request])
spliced = fold([frame, record, spliced_pilot, route, request])["verdicts"][-1]
wrong_preparation = fold(
    [frame, record, wrong_preparation_pilot, route, request]
)["verdicts"][-1]
numerically_equal_wrong_preparation = fold(
    [frame, record, numerically_equal_wrong_preparation_pilot, route, request]
)["verdicts"][-1]
revisionless = fold([frame, record, revisionless_pilot, route, request])["verdicts"][-1]
wrong_connection = fold(
    [frame, record, related_pilot, wrong_connection_route, request]
)["verdicts"][-1]
reverse_direction = fold([frame, record, related_pilot, reverse_route, request])[
    "verdicts"
][-1]
replayed = fold([frame, record, related_pilot, route, request])

visible_record = tuple(record["residues"])
stale_alias = sample(17, 0)

assert visible_record == (1, 2) == stale_alias
assert decode(visible_record, 0) == 17
assert premature == {"status": "transport_unavailable", "reason": "pilot_missing"}
assert missing_route == {"status": "transport_unavailable", "reason": "route_missing"}
assert valid["verdicts"][-1] == {
    "status": "decoded",
    "source": 1,
    "transport": "source_related_pilot",
}
assert spliced == {"status": "rejected", "reason": "cross_run_pilot_splice"}
assert wrong_preparation == {
    "status": "rejected",
    "reason": "cross_preparation_pilot_splice",
}
assert numerically_equal_wrong_preparation == wrong_preparation
assert revisionless == {
    "status": "transport_unavailable",
    "reason": "pilot_revision_missing",
}
assert wrong_connection == {"status": "rejected", "reason": "route_witness_mismatch"}
assert reverse_direction == {"status": "rejected", "reason": "route_witness_mismatch"}
assert replayed == valid

result = {
    "schema": "marici.nima.optical-carrier-actor.v1",
    "status": "pass",
    "visible_record": list(visible_record),
    "stale_value_only_decode": 17,
    "premature_decode": premature,
    "valid_transport": valid["verdicts"][-1],
    "cross_run_splice": spliced,
    "cross_preparation_splice": wrong_preparation,
    "numerically_equal_wrong_preparation_splice": numerically_equal_wrong_preparation,
    "missing_route": missing_route,
    "revision_deletion": revisionless,
    "wrong_connection": wrong_connection,
    "reverse_route": reverse_direction,
    "event_replay_reconstructs_same_state": replayed == valid,
    "snapshot_alone_authorizes_decode": False,
}

output = Path(__file__).parents[1] / "results" / "optical-carrier-actor.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
