import json
from math import gcd, lcm
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def record(frequency, rates=(4, 5), phases=(0, 0)):
    return tuple((frequency + phase) % rate for rate, phase in zip(rates, phases))


def decode(pair):
    a, b = pair
    return (5 * a + 16 * b) % 20


band = range(20)
records = [record(f) for f in band]
check("rates_are_coprime", gcd(4, 5) == 1)
check("joint_period_is_twenty", lcm(4, 5) == 20)
check("joint_observer_is_injective_on_band", len(set(records)) == 20)
check("decoder_is_left_inverse_on_band", all(decode(record(f)) == f for f in band))

check("deleting_second_clock_restores_alias", 1 % 4 == 5 % 4)
noncoprime_records = [record(f, rates=(4, 6)) for f in band]
check("noncoprime_replacement_fails_twenty_band",
      lcm(4, 6) == 12 and len(set(noncoprime_records)) < 20)
check("deleting_band_restores_period_hostile", record(1) == record(21))

unlabelled = {}
unlabelled_witness = None
for f in band:
    value = tuple(sorted(record(f)))
    if value in unlabelled:
        unlabelled_witness = (unlabelled[value], f, value)
        break
    unlabelled[value] = f
check("erasing_port_labels_creates_in_band_collision", unlabelled_witness is not None)

shifted_record = record(1, phases=(0, 1))
check("stale_phase_decoder_returns_wrong_class", decode(shifted_record) != 1)

# Same decoder package, different live calibration epochs.
decoder_package = {
    "rates": [4, 5],
    "phases": [0, 0],
    "ordered_ports": ["clock-4", "clock-5"],
    "band": [0, 20],
    "calibration_epoch": 7,
}


def invoke_decoder(package, pair, live_epoch, trust_capture=False):
    observed = package["calibration_epoch"] if trust_capture else live_epoch
    admitted = observed == package["calibration_epoch"]
    return {
        "status": "decoded" if admitted else "rejected",
        "value": decode(pair) if admitted else None,
    }


live = invoke_decoder(decoder_package, record(9), live_epoch=7)
stale = invoke_decoder(decoder_package, record(9), live_epoch=8)
hostile = invoke_decoder(decoder_package, record(9), live_epoch=8, trust_capture=True)
check("live_calibration_decodes", live == {"status": "decoded", "value": 9})
check("stale_calibration_rejects", stale == {"status": "rejected", "value": None})
check("trusting_captured_epoch_admits_stale_decoder",
      hostile == {"status": "decoded", "value": 9})

# Residue evidence alone cannot certify the chosen integer representative.
preimages = [f for f in range(-40, 61) if record(f) == record(1)]
check("record_has_multiple_unrestricted_preimages", len(preimages) > 1 and 1 in preimages and 21 in preimages)

# Static readout theorem deliberately contains no controlled transition.
model_fields = {"state_domain", "observation_ports", "decoder"}
check("packet_is_static_observer_not_feedback_system",
      "control_input" not in model_fields and "state_transition" not in model_fields)

result = {
    "schema": "marici.sontag.dual_clock_packet_control_marici_attack.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "unlabelled_port_collision": unlabelled_witness,
    "stale_phase_example": {
        "source": 1,
        "shifted_record": shifted_record,
        "stale_decoder_output": decode(shifted_record),
    },
    "unrestricted_preimages_of_record_for_one": preimages,
    "claim_boundary": (
        "Exact finite static-observer and Marici procedure-boundary audit; no "
        "continuum, jitter, physical band, or clock-availability theorem."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "dual_clock_packet_control_marici_attack.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)

