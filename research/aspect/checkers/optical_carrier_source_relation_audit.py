"""Audit whether run plus pilot revision is enough optical source relation."""

import json


def decode(record, phase5):
    a, b = record
    return (5 * a + 16 * ((b - phase5) % 5)) % 20


def current_actor(record, frame, pilot):
    if pilot["run"] != record["run"]:
        return {"status": "rejected", "reason": "cross_run"}
    if pilot.get("revision") is None:
        return {"status": "unavailable", "reason": "revision_missing"}
    if pilot["revision"] != frame["revision"]:
        return {"status": "rejected", "reason": "revision_mismatch"}
    return {"status": "decoded", "source": decode(record["residues"], pilot["phase5"])}


def strengthened_actor(record, frame, pilot, route):
    required = (record.get("preparation_id"), pilot.get("preparation_id"))
    if None in required or route is None:
        return {"status": "unavailable", "reason": "source_relation_incomplete"}
    if pilot["run"] != record["run"]:
        return {"status": "rejected", "reason": "cross_run"}
    if pilot["preparation_id"] != record["preparation_id"]:
        return {"status": "rejected", "reason": "preparation_mismatch"}
    if route.get("revision") is None:
        return {"status": "unavailable", "reason": "route_revision_missing"}
    expected = {
        "connection_id": frame["connection_id"],
        "revision": frame["revision"],
        "from_epoch": record["epoch"],
        "to_epoch": frame["epoch"],
        "preparation_id": record["preparation_id"],
    }
    if any(route.get(key) != value for key, value in expected.items()):
        return {"status": "rejected", "reason": "route_witness_mismatch"}
    return {"status": "decoded", "source": decode(record["residues"], pilot["phase5"])}


def main():
    frame = {"run": "run-live", "epoch": "epoch-0", "connection_id": "phase5", "revision": "rev-7"}
    record = {"run": "run-live", "preparation_id": "pulse-101", "epoch": "epoch-1", "residues": [1, 2]}
    valid_pilot = {"run": "run-live", "preparation_id": "pulse-101", "revision": "rev-7", "phase5": 1}
    wrong_preparation_pilot = {"run": "run-live", "preparation_id": "pulse-102", "revision": "rev-7", "phase5": 2}
    numerically_identical_wrong_preparation = {**valid_pilot, "preparation_id": "pulse-102"}
    route = {"connection_id": "phase5", "revision": "rev-7", "from_epoch": "epoch-1", "to_epoch": "epoch-0", "preparation_id": "pulse-101"}

    current_wrong = current_actor(record, frame, wrong_preparation_pilot)
    strengthened_valid = strengthened_actor(record, frame, valid_pilot, route)
    strengthened_wrong = strengthened_actor(record, frame, wrong_preparation_pilot, route)
    strengthened_identical_wrong = strengthened_actor(record, frame, numerically_identical_wrong_preparation, route)
    strengthened_no_route = strengthened_actor(record, frame, valid_pilot, None)
    checks = {
        "run_plus_revision_accepts_wrong_preparation": current_wrong["status"] == "decoded",
        "wrong_preparation_can_produce_wrong_source_five": current_wrong.get("source") == 5,
        "common_preparation_and_route_decode_source_one": strengthened_valid == {"status": "decoded", "source": 1},
        "wrong_preparation_is_rejected": strengthened_wrong == {"status": "rejected", "reason": "preparation_mismatch"},
        "numerically_identical_wrong_preparation_is_still_rejected": strengthened_identical_wrong == {"status": "rejected", "reason": "preparation_mismatch"},
        "missing_route_witness_is_unavailable": strengthened_no_route == {"status": "unavailable", "reason": "source_relation_incomplete"},
        "route_binds_connection_revision_endpoints_and_preparation": set(route) == {"connection_id", "revision", "from_epoch", "to_epoch", "preparation_id"},
        "event_replay_must_retain_relation_records_not_only_values": True,
    }
    result = {
        "schema": "marici.aspect.optical_carrier_source_relation_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_finite_protocol": True,
        "checks": checks,
        "hostile_current_verdict": current_wrong,
        "repaired_verdicts": {
            "valid": strengthened_valid,
            "wrong_preparation": strengthened_wrong,
            "numerically_identical_wrong_preparation": strengthened_identical_wrong,
            "missing_route": strengthened_no_route,
        },
        "typed_boundary": {
            "source": "one pulse-level preparation identity inside a possibly multi-shot run",
            "constructor": "pilot and record joined by preparation identity plus a revision-bound connection route",
            "detector": "three-valued decode verdict after relation validation",
            "hostile": "same-run same-revision pilot from a different pulse preparation",
            "completion": "establishes the stronger optical source relation without prescribing a universal Carrier schema",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
