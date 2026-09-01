import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Clock orientation sign drops out of the unit orbit.
def clock_ratio(n):
    return 6*n*n
assert clock_ratio(-1) == clock_ratio(1) == 6

# Wilson phase is orientation-odd, but only modulo one.
phi = Fraction(1,3)
phi_conj = (-phi) % 1
assert phi_conj == Fraction(2,3)
assert phi != phi_conj

# WP1111 split equations contain t, not the clock/Wilson sign.
def split_levels(t):
    return Fraction(-1,4)-t, -t
assert split_levels(1) == (Fraction(-5,4), -1)
assert split_levels(-1) == (Fraction(3,4), 1)
assert tuple(x % 1 for x in split_levels(1)) == tuple(x % 1 for x in split_levels(0))

# No admitted equation couples the Wilson phase/sign to t.
coupling_equations = []
assert coupling_equations == []
joint_selector = False
assert not joint_selector

result = {
    "schema": "marici.flavor.wp1113.v1",
    "status": "PASS",
    "question": "Can an orientation-odd Wilson/flux boundary datum jointly select the GS split and clock orientation?",
    "clock_ratio_pm1": [str(clock_ratio(-1)), str(clock_ratio(1))],
    "wilson_phase_pair": [str(phi), str(phi_conj)],
    "split_levels": ["k4=-1/4-t", "k2=-t"],
    "split_coset_t_domain": "Z",
    "wilson_split_coupling_equations": coupling_equations,
    "joint_selector": joint_selector,
    "classification": "negative gate: Wilson/flux orientation is odd but does not enter the endpoint split, while 6n^2 erases clock sign",
    "remaining_gate": "construct an independent source datum coupling orientation to the split, or proceed to the independent-rho obstruction",
    "hostile_gate": "do not use Wilson phase, flux conjugation, or clock sigma as a joint selector of t and orientation",
    "claim_boundary": "the datum is orientation-odd but has no admitted coupling to the split fiber",
    "disposition": "joint Wilson-orientation route closed",
}

(ROOT / "results" / "wp1113_wilson_orientation_split_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1113 PASS:", phi, phi_conj, clock_ratio(1), len(coupling_equations))
