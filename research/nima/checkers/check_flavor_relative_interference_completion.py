import json
from fractions import Fraction as F
from pathlib import Path


MAGNITUDES = (1, 2, 3)
STATES = tuple((a, b) for a in range(-3, 4) if a != 0
               for b in range(-3, 4) if b != 0)


def canonical_global_sign(state):
    a, b = state
    return (a, b) if a > 0 else (-a, -b)


CLASSES = tuple(sorted({canonical_global_sign(state) for state in STATES}))
assert len(STATES) == 36
assert len(CLASSES) == 18


def rates(state):
    a, b = state
    return a * a, b * b


def interference(state):
    a, b = state
    return a * b


rate_fibers = {}
for state in CLASSES:
    rate_fibers.setdefault(rates(state), []).append(state)
assert len(rate_fibers) == 9
assert all(len(fiber) == 2 for fiber in rate_fibers.values())
assert all(len({interference(state) for state in fiber}) == 2
           for fiber in rate_fibers.values())

joint_records = {(rates(state), interference(state)): state for state in CLASSES}
assert len(joint_records) == len(CLASSES)
assert all(interference(state) ** 2 == rates(state)[0] * rates(state)[1]
           for state in CLASSES)

# A phase-flipped two-port reference isolates the interference even with an
# unknown common background B. Visibility is an independently calibrated gain.
background = F(50)
visibility = F(3, 5)


def ports(state, visibility_value=visibility):
    cross = F(interference(state))
    return background + 2 * visibility_value * cross, background - 2 * visibility_value * cross


for state in CLASSES:
    plus, minus = ports(state)
    recovered = (plus - minus) / (4 * visibility)
    assert recovered == interference(state)
    assert plus + minus == 2 * background

# Summing ports or losing visibility erases the relative channel exactly.
assert len({sum(ports(state)) for state in CLASSES}) == 1
assert len({ports(state, F(0)) for state in CLASSES}) == 1

result = {
    "schema": "marici.nima.flavor-relative-interference-completion.v1",
    "raw_signed_states": len(STATES),
    "classes_mod_simultaneous_global_sign": len(CLASSES),
    "separate_rate_fibers": len(rate_fibers),
    "gauge_classes_per_rate_fiber": 2,
    "separate_rates_jointly_faithful": False,
    "rates_plus_signed_interference_faithful_mod_global_sign": True,
    "interference_square_relation_verified": True,
    "two_port_phase_flip_recovers_interference": True,
    "summed_ports_erase_interference": True,
    "zero_visibility_erases_interference": True,
    "verdict": "Signed interference is the minimal relative completion of separate rate channels modulo simultaneous global sign; a phase-flipped two-port reference recovers it, while port summation or zero visibility quotients it out."
}

out = Path(__file__).parents[1] / "results" / "flavor-relative-interference-completion.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
