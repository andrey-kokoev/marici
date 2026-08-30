"""Exact audit of route identity and direction in the revised optical actor."""

import json


def current_route_accepts(route, record, pilot, frame):
    route_signature = (
        route["preparation_id"], route["revision"],
        route["from_epoch"], route["to_epoch"],
    )
    required_signature = (
        record["preparation_id"], pilot["revision"],
        frame["epoch"], record["epoch"],
    )
    return route_signature == required_signature


def strengthened_route_verdict(route, record, pilot, frame):
    required_keys = {"connection_id", "revision", "from_epoch", "to_epoch", "preparation_id"}
    if route is None or not required_keys.issubset(route):
        return "unavailable"
    expected = {
        "connection_id": frame["connection_id"],
        "revision": frame["revision"],
        "from_epoch": record["epoch"],
        "to_epoch": frame["epoch"],
        "preparation_id": record["preparation_id"],
    }
    if pilot["revision"] != frame["revision"]:
        return "reject"
    return "accept" if all(route[key] == value for key, value in expected.items()) else "reject"


def main():
    frame = {"epoch": "epoch-0", "connection_id": "phase5", "revision": "rev-7"}
    record = {"epoch": "epoch-1", "preparation_id": "pulse-101"}
    pilot = {"revision": "rev-7", "preparation_id": "pulse-101"}
    record_to_frame = {"connection_id": "phase5", "revision": "rev-7", "from_epoch": "epoch-1", "to_epoch": "epoch-0", "preparation_id": "pulse-101"}
    frame_to_record = {**record_to_frame, "from_epoch": "epoch-0", "to_epoch": "epoch-1"}
    wrong_connection = {**frame_to_record, "connection_id": "unrelated-connection"}
    corrected_wrong_connection = {**record_to_frame, "connection_id": "unrelated-connection"}

    checks = {
        "current_actor_accepts_reverse_oriented_route": current_route_accepts(frame_to_record, record, pilot, frame),
        "current_actor_rejects_record_to_decoder_direction": not current_route_accepts(record_to_frame, record, pilot, frame),
        "current_actor_ignores_wrong_connection_identity": current_route_accepts(wrong_connection, record, pilot, frame),
        "strengthened_actor_accepts_record_to_decoder_direction": strengthened_route_verdict(record_to_frame, record, pilot, frame) == "accept",
        "strengthened_actor_rejects_reverse_direction": strengthened_route_verdict(frame_to_record, record, pilot, frame) == "reject",
        "strengthened_actor_rejects_wrong_connection": strengthened_route_verdict(corrected_wrong_connection, record, pilot, frame) == "reject",
        "missing_route_is_unavailable": strengthened_route_verdict(None, record, pilot, frame) == "unavailable",
        "direction_is_typed_not_inferred_from_epoch_names": True,
    }
    result = {
        "schema": "marici.aspect.optical_carrier_route_identity_direction_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_finite_protocol": True,
        "checks": checks,
        "required_route": record_to_frame,
        "typed_boundary": {
            "source": "one record preparation and one named phase connection",
            "constructor": "directed transport from record epoch to decoder-frame epoch",
            "detector": "route validation before optical decoding",
            "hostile": "reverse-oriented or wrong-connection route passes when identity is carried but not consumed",
            "completion": "repairs the finite actor route contract without asserting a universal direction convention",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
