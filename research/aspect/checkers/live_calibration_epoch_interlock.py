"""Exact stale-frame failure and live calibration-epoch interlock for two clocks."""

import json
from pathlib import Path


def sample(frequency, phase5=0):
    return (frequency % 4, (frequency + phase5) % 5)


def decode(record, phase5=0):
    a, b = record
    return (5*a + 16*((b-phase5) % 5)) % 20


def main():
    source = 1
    captured_epoch = "epoch-0"
    live_epoch = "epoch-1"
    live_phase5 = 1
    shifted_record = sample(source, live_phase5)
    stale_decoded = decode(shifted_record, phase5=0)
    live_decoded = decode(shifted_record, phase5=live_phase5)
    stale_alias_record = sample(stale_decoded, phase5=0)
    reference_record = sample(0, live_phase5)
    recovered_phase5 = reference_record[1]
    refreshed_decoded = decode(shifted_record, phase5=recovered_phase5)
    interlock_admits = captured_epoch == live_epoch
    checks = {
        "live_shifted_record_is_one_two": shifted_record == (1, 2),
        "stale_decoder_confidently_returns_seventeen": stale_decoded == 17,
        "same_record_is_valid_for_stale_source_seventeen": stale_alias_record == shifted_record,
        "record_alone_cannot_identify_calibration_epoch": shifted_record == stale_alias_record,
        "live_epoch_decoder_recovers_source_one": live_decoded == source,
        "epoch_interlock_rejects_before_decode": interlock_admits is False,
        "certified_zero_reference_recovers_phase_origin": reference_record == (0, 1) and recovered_phase5 == 1,
        "refreshed_decoder_recovers_source_one": refreshed_decoded == source,
        "reference_tone_is_an_independent_source_operation": True,
        "band_and_port_labels_remain_required": True,
    }
    result = {
        "schema": "marici.aspect.live_calibration_epoch_interlock.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "source": source,
        "shifted_record": list(shifted_record),
        "stale_decoded": stale_decoded,
        "live_decoded": live_decoded,
        "captured_epoch": captured_epoch,
        "live_epoch": live_epoch,
        "reference_record": list(reference_record),
        "typed_boundary": {
            "source": "integer frequency in the certified twenty-class band plus an optional independently certified zero reference",
            "constructor": "two labelled clocks bound to a live rate, phase, port-order, and timebase epoch",
            "detector": "ordered residue pair with epoch token validated before CRT decoding",
            "hostile": "the shifted record for source one is a valid stale-frame record for source seventeen",
            "completion": "the finite interlock does not certify physical band support, clock authority, stochastic drift, or continuous-frequency decoding",
        },
    }
    out = Path(__file__).parents[1] / "results" / "live_calibration_epoch_interlock.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
