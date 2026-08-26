from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


def canonical_state(state):
    g_phi, g_psi, kappa, visibility, background = state
    pair = (g_phi, g_psi)
    flipped = (-g_phi, -g_psi)
    chosen = min(pair, flipped)
    return chosen + (kappa, visibility, background)


def record(state):
    g_phi, g_psi, kappa, visibility, background = state
    gamma_phi = g_phi * g_phi
    gamma_psi = g_psi * g_psi
    interference = g_phi * g_psi
    portal = -kappa * interference
    common = background + gamma_phi + gamma_psi
    plus = common + 2 * visibility * interference
    minus = common - 2 * visibility * interference
    return gamma_phi, gamma_psi, portal, plus, minus


couplings = tuple(Fraction(x) for x in (-3, -2, -1, 1, 2, 3))
kappas = tuple(Fraction(x) for x in (-2, -1, 1, 2))
visibilities = (Fraction(1, 2), Fraction(1))
backgrounds = (Fraction(10), Fraction(11))

states = [
    (g_phi, g_psi, kappa, visibility, background)
    for g_phi in couplings
    for g_psi in couplings
    for kappa in kappas
    for visibility in visibilities
    for background in backgrounds
]

fibers = defaultdict(set)
for state in states:
    fibers[record(state)].add(canonical_state(state))

assert max(len(fiber) for fiber in fibers.values()) == 1

# If visibility vanishes, relative sign can be exchanged against kappa sign.
zero_left = (Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(10))
zero_right = (Fraction(1), Fraction(-1), Fraction(-1), Fraction(0), Fraction(10))
assert record(zero_left) == record(zero_right)
assert canonical_state(zero_left) != canonical_state(zero_right)

# Summing the ports erases the signed comparison even at nonzero visibility.
def summed_record(state):
    gamma_phi, gamma_psi, portal, plus, minus = record(state)
    return gamma_phi, gamma_psi, portal, plus + minus


sum_left = (Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(10))
sum_right = (Fraction(1), Fraction(-1), Fraction(-1), Fraction(1), Fraction(10))
assert summed_record(sum_left) == summed_record(sum_right)
assert canonical_state(sum_left) != canonical_state(sum_right)

# Removing the portal leaves kappa invisible.
def no_portal_record(state):
    gamma_phi, gamma_psi, _, plus, minus = record(state)
    return gamma_phi, gamma_psi, plus, minus


kappa_left = (Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(10))
kappa_right = (Fraction(1), Fraction(1), Fraction(2), Fraction(1), Fraction(10))
assert no_portal_record(kappa_left) == no_portal_record(kappa_right)

result = {
    "schema": "marici.nima.flavor-compatibility-locus.v1",
    "raw_states_checked": len(states),
    "states_mod_global_sign": len({canonical_state(s) for s in states}),
    "observable_records": len(fibers),
    "maximum_record_fiber_mod_global_sign": max(len(f) for f in fibers.values()),
    "joined_record_faithful_mod_global_sign": True,
    "zero_visibility_hostile_passed": True,
    "summed_port_hostile_passed": True,
    "missing_portal_hostile_passed": True,
    "verdict": (
        "On the declared finite reachable locus with positive visibility, the "
        "joined widths, portal, and ordered phase ports are faithful modulo "
        "simultaneous global sign. The result fails if the comparison ports "
        "are summed, visibility vanishes, or the portal channel is removed."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-compatibility-locus.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
