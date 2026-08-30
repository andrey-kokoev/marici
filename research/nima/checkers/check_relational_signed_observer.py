import json
from pathlib import Path


def signed_port(beam, phase_sign):
    return beam * phase_sign


def paired_port(tag, beam, phase_sign):
    return tag * beam * phase_sign


beam = 1
tag = 1
phase = 1

unpaired = signed_port(beam, phase)
beam_reversed_unpaired = signed_port(-beam, phase)
orbit_average = (unpaired + beam_reversed_unpaired) // 2
assert unpaired == 1
assert beam_reversed_unpaired == -1
assert orbit_average == 0

squared = unpaired * unpaired
phase_reversed_squared = signed_port(beam, -phase) ** 2
assert squared == phase_reversed_squared

paired = paired_port(tag, beam, phase)
beam_reversed_paired = paired_port(-tag, -beam, phase)
phase_reversed_paired = paired_port(tag, beam, -phase)
assert beam_reversed_paired == paired
assert phase_reversed_paired == -paired

# Optical sign model: global sign reverses signal and reference, but their
# relative product survives.
signal = 1
reference = -1
relative = signal * reference
global_sign_relative = (-signal) * (-reference)
assert global_sign_relative == relative

# A trivial tag does not cancel the quotient action.
trivial_tag_beam_reversal = paired_port(tag, -beam, phase)
assert trivial_tag_beam_reversal == -paired

result = {
    "schema": "marici.relational-signed-observer.v1",
    "unpaired_orbit_average": orbit_average,
    "squared_port_phase_odd": False,
    "paired_port_quotient_invariant": True,
    "paired_port_target_phase_odd": True,
    "optical_relative_sign_invariant": True,
    "trivial_tag_cancels_quotient": False,
    "claim_boundary": "signed information descends through a source-derived dual-character reference",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "relational-signed-observer.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
