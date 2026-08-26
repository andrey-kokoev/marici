"""Exact cross-run witness-splicing hostile for a calibrated optical decoder."""

import json
from copy import deepcopy
from pathlib import Path


def decode(record, phase5):
    a, b = record
    return (5*a + 16*((b-phase5) % 5)) % 20


def transport_record(record, delta):
    return (record[0], (record[1]-delta) % 5)


def effective_record(packet):
    transport = packet.get("frame_transport")
    if transport:
        return transport_record(packet["port_record"]["record"], transport["delta"])
    return packet["port_record"]["record"]


def local_validity(packet):
    return {
        "source_certificate": 0 <= packet["source_certificate"]["claimed_source"] < 20,
        "port_record": 0 <= packet["port_record"]["record"][0] < 4 and 0 <= packet["port_record"]["record"][1] < 5,
        "calibration": packet["calibration"]["phase5"] in range(5),
        "decoder": decode(effective_record(packet), packet["calibration"]["phase5"]) == packet["claim"]["source"],
        "claimant": packet["claim"]["authorized"] and packet["claim"]["scope"] == "band-0-19",
    }


def joint_verdict(packet):
    keys = ["source_certificate", "port_record", "calibration", "decoder", "claim"]
    if packet.get("frame_transport"):
        keys.extend(["frame_transport", "source_connection"])
    run_ids = {packet[key]["run_id"] for key in keys}
    record_epoch = packet["port_record"]["epoch"]
    decoder_epoch = packet["decoder"]["epoch"]
    transport = packet.get("frame_transport")
    same_frame = record_epoch == decoder_epoch == packet["calibration"]["epoch"]
    decoder_matches = packet["decoder"]["version"] == packet["calibration"]["decoder_version"]
    source_matches = packet["source_certificate"]["claimed_source"] == packet["claim"]["source"]
    if len(run_ids) != 1 or not decoder_matches or not source_matches:
        return "reject"
    if same_frame:
        return "accept"
    if not transport:
        return "reject"
    contract = packet.get("source_connection")
    revision_binding = transport.get("revision_binding")
    if not contract or not revision_binding:
        return "unavailable"
    coherent_transport = bool(
        transport["certified"]
        and transport["from_epoch"] == record_epoch
        and transport["to_epoch"] == decoder_epoch == packet["calibration"]["epoch"]
        and revision_binding["connection_id"] == contract["connection_id"]
        and revision_binding["revision"] == contract["revision"]
    )
    return "accept" if coherent_transport else "reject"


def joint_validity(packet):
    return joint_verdict(packet) == "accept"


def main():
    spliced = {
        "source_certificate": {"run_id": "e1", "claimed_source": 1},
        "port_record": {"run_id": "e2", "epoch": "epoch-0", "record": [1, 2], "physical_source": 17},
        "calibration": {"run_id": "e1", "epoch": "epoch-1", "phase5": 1, "decoder_version": "decoder-e1"},
        "decoder": {"run_id": "e1", "epoch": "epoch-1", "version": "decoder-e1"},
        "claim": {"run_id": "e1", "source": 1, "authorized": True, "scope": "band-0-19"},
    }
    honest = {
        "source_certificate": {"run_id": "e2", "claimed_source": 17},
        "port_record": {"run_id": "e2", "epoch": "epoch-0", "record": [1, 2], "physical_source": 17},
        "calibration": {"run_id": "e2", "epoch": "epoch-0", "phase5": 0, "decoder_version": "decoder-e0"},
        "decoder": {"run_id": "e2", "epoch": "epoch-0", "version": "decoder-e0"},
        "claim": {"run_id": "e2", "source": 17, "authorized": True, "scope": "band-0-19"},
    }
    transported = {
        "source_certificate": {"run_id": "e3", "claimed_source": 1},
        "port_record": {"run_id": "e3", "epoch": "epoch-1", "record": [1, 2], "physical_source": 1},
        "calibration": {"run_id": "e3", "epoch": "epoch-0", "phase5": 0, "decoder_version": "decoder-e0"},
        "decoder": {"run_id": "e3", "epoch": "epoch-0", "version": "decoder-e0"},
        "claim": {"run_id": "e3", "source": 1, "authorized": True, "scope": "band-0-19"},
        "source_connection": {"run_id": "e3", "connection_id": "phase5-connection", "revision": "rev-7"},
        "frame_transport": {"run_id": "e3", "from_epoch": "epoch-1", "to_epoch": "epoch-0", "delta": 1, "certified": True, "revision_binding": {"connection_id": "phase5-connection", "revision": "rev-7"}},
    }
    deleted_revision = deepcopy(transported)
    del deleted_revision["frame_transport"]["revision_binding"]
    spliced_local = local_validity(spliced)
    honest_local = local_validity(honest)
    checks = {
        "every_spliced_marginal_is_locally_valid": all(spliced_local.values()),
        "spliced_decoder_returns_claimed_source_one": decode([1, 2], 1) == 1,
        "physical_record_was_generated_by_source_seventeen": spliced["port_record"]["physical_source"] == 17 and decode([1, 2], 0) == 17,
        "spliced_packet_has_no_common_run": not joint_validity(spliced),
        "run_ids_expose_the_splice": {spliced[k]["run_id"] for k in spliced} == {"e1", "e2"},
        "epochs_expose_the_frame_conflict": spliced["port_record"]["epoch"] != spliced["calibration"]["epoch"],
        "honest_packet_passes_local_and_joint_checks": all(honest_local.values()) and joint_validity(honest),
        "certified_same_run_frame_transport_is_accepted": all(local_validity(transported).values()) and joint_validity(transported),
        "cross_run_splice_is_rejected_by_same_contract": joint_verdict(spliced) == "reject",
        "deleting_revision_binding_makes_transport_unavailable": joint_verdict(deleted_revision) == "unavailable",
        "deletion_does_not_fall_back_to_literal_epoch_equality": deleted_revision["port_record"]["epoch"] != deleted_revision["calibration"]["epoch"] and joint_verdict(deleted_revision) != "reject",
        "deletion_does_not_silently_accept_transport": not joint_validity(deleted_revision),
        "transport_maps_shifted_record_to_epoch_zero_frame": effective_record(transported) == (1, 1),
        "authorization_does_not_repair_missing_joint_witness": spliced["claim"]["authorized"] and not joint_validity(spliced),
        "test_does_not_claim_a_new_marici_primitive": True,
    }
    result = {
        "schema": "marici.aspect.cross_run_optical_witness_splicing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "spliced_local_validity": spliced_local,
        "spliced_joint_validity": joint_validity(spliced),
        "honest_joint_validity": joint_validity(honest),
        "transported_joint_validity": joint_validity(transported),
        "joint_verdicts": {
            "spliced": joint_verdict(spliced),
            "honest_same_epoch": joint_verdict(honest),
            "certified_transport": joint_verdict(transported),
            "deleted_revision_binding": joint_verdict(deleted_revision),
        },
        "spliced_claim": 1,
        "physical_source": 17,
        "typed_boundary": {
            "source": "band certificate, labelled optical record, calibration, decoder, and scoped claim",
            "constructor": "one common execution plus either one frame or a certified coherent frame transport must jointly realize every witness",
            "detector": "marginal schema checks followed by run, epoch, decoder-version, and source-claim joins",
            "hostile": "valid epoch-one decoder evidence is spliced onto an epoch-zero record from another run",
            "completion": "the finite hostile establishes a required invariant test, including unavailable-on-missing-revision semantics, not novelty of a Marici primitive or a universal evidence architecture",
        },
    }
    out = Path(__file__).parents[1] / "results" / "cross_run_optical_witness_splicing.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
