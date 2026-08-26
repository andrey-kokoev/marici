import importlib.util
import json
from pathlib import Path


actor_path = Path(__file__).with_name("check_optical_carrier_actor.py")
spec = importlib.util.spec_from_file_location("optical_actor", actor_path)
actor = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(actor)


frame = actor.frame
record = actor.record
pilot = actor.related_pilot
route = actor.route
request = actor.request

histories = {
    "base": [frame, record],
    "base_redundant_frame": [frame, frame, record],
    "valid_ready": [frame, record, pilot, route],
    "wrong_preparation_ready": [
        frame,
        record,
        actor.numerically_equal_wrong_preparation_pilot,
        route,
    ],
    "wrong_connection_ready": [frame, record, pilot, actor.wrong_connection_route],
    "reverse_route_ready": [frame, record, pilot, actor.reverse_route],
    "revisionless_ready": [frame, record, actor.revisionless_pilot, route],
}

continuations = {
    "decode_now": [request],
    "supply_valid_then_decode": [pilot, route, request],
    "supply_wrong_preparation_then_decode": [
        actor.numerically_equal_wrong_preparation_pilot,
        route,
        request,
    ],
    "supply_wrong_connection_then_decode": [pilot, actor.wrong_connection_route, request],
    "supply_reverse_route_then_decode": [pilot, actor.reverse_route, request],
}


def trace(history: list[dict], continuation: list[dict]) -> list[dict]:
    return actor.fold(history + continuation)["verdicts"]


def signature(history: list[dict]) -> str:
    traces = {
        name: trace(history, continuation)
        for name, continuation in continuations.items()
    }
    return json.dumps(traces, sort_keys=True)


signatures = {name: signature(history) for name, history in histories.items()}
classes: dict[str, list[str]] = {}
for name, value in signatures.items():
    classes.setdefault(value, []).append(name)

class_members = sorted(sorted(members) for members in classes.values())

assert signatures["base"] == signatures["base_redundant_frame"]
assert signatures["valid_ready"] != signatures["wrong_preparation_ready"]
assert signatures["valid_ready"] != signatures["wrong_connection_ready"]
assert signatures["valid_ready"] != signatures["reverse_route_ready"]
assert signatures["valid_ready"] != signatures["revisionless_ready"]
assert ["base", "base_redundant_frame"] in class_members

# All candidate histories share the same visible optical record.
visible_records = {
    tuple(actor.fold(history)["record"]["residues"])
    for history in histories.values()
}
assert visible_records == {(1, 2)}


def weakened_decode(history: list[dict], dropped: str) -> dict:
    state = actor.fold(history)
    frame_state = state["frame"]
    record_state = state["record"]
    pilot_state = state["pilot"]
    route_state = state["route"]
    assert frame_state and record_state and pilot_state and route_state

    if dropped != "preparation_id":
        if pilot_state["preparation_id"] != record_state["preparation_id"]:
            return {"status": "rejected"}
        if route_state["preparation_id"] != record_state["preparation_id"]:
            return {"status": "rejected"}
    if dropped != "connection_id":
        if route_state["connection_id"] != frame_state["connection_id"]:
            return {"status": "rejected"}
    if dropped != "route_direction":
        if (
            route_state["from_epoch"],
            route_state["to_epoch"],
        ) != (record_state["epoch"], frame_state["epoch"]):
            return {"status": "rejected"}
    if dropped != "revision":
        if pilot_state.get("revision") is None:
            return {"status": "unavailable"}
        if pilot_state["revision"] != frame_state["revision"]:
            return {"status": "rejected"}
        if route_state["revision"] != pilot_state["revision"]:
            return {"status": "rejected"}

    recovered_phase = pilot_state["residues"][1]
    return {
        "status": "decoded",
        "source": actor.decode(tuple(record_state["residues"]), recovered_phase),
    }


deletion_hostiles = {
    "preparation_id": histories["wrong_preparation_ready"],
    "connection_id": histories["wrong_connection_ready"],
    "route_direction": histories["reverse_route_ready"],
    "revision": histories["revisionless_ready"],
}
deletion_results = {
    field: weakened_decode(history, field)
    for field, history in deletion_hostiles.items()
}
assert all(value == {"status": "decoded", "source": 1} for value in deletion_results.values())

result = {
    "schema": "marici.nima.optical-carrier-nerode.v1",
    "status": "pass",
    "history_count": len(histories),
    "continuation_count": len(continuations),
    "equivalence_class_count": len(classes),
    "classes": class_members,
    "full_history_not_required": signatures["base"]
    == signatures["base_redundant_frame"],
    "visible_record_is_insufficient": len(visible_records) == 1 and len(classes) > 1,
    "equivalent_rejection_causes": ["wrong_connection_ready", "reverse_route_ready"],
    "field_deletion_results": deletion_results,
    "necessary_fields": [
        "preparation_id",
        "connection_id",
        "route_direction",
        "revision",
    ],
}

output = Path(__file__).parents[1] / "results" / "optical-carrier-nerode.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
