import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

first_channels = ["SU4^3", "SU4^2 U1", "SU2^2 U1", "U1^3", "U1 grav"]
grav_channels = ["SU4 grav", "SU2 grav"]

# WP1067 vectors for globally vanishing channels.
def first_vector(kind, reflected=False):
    if kind == "quartet":
        v = [Fraction(1, 2), Fraction(1, 4), 0, 2, 2]
    elif kind == "doublet_pair":
        v = [0, 0, -1, -16, -4]
    else:
        raise AssertionError(kind)
    return [-x for x in v] if reflected else v

# Parent GS coefficient -3.  A symmetric endpoint split is a conditional
# completion law, not a derived one.
def gravity_vector(kind, gs0=Fraction(-3, 2), reflected=False):
    gspi = -3 - gs0
    assert gs0 + gspi == -3
    if kind == "quartet":
        b4, b2 = Fraction(1, 2), Fraction(0)
    elif kind == "doublet_pair":
        b4, b2 = Fraction(0), Fraction(1)
    else:
        raise AssertionError(kind)
    B4, B2 = 3 - b4, 3 - b2
    if not reflected:
        k4 = -b4 - B4 / 2 - gs0
        k2 = -b2 - B2 / 2 - gs0
        assert b4 + B4 / 2 + k4 + gs0 == 0
        assert B4 / 2 - k4 + gspi == 0
        assert b2 + B2 / 2 + k2 + gs0 == 0
        assert B2 / 2 - k2 + gspi == 0
    else:
        k4 = -B4 / 2 - gs0
        k2 = -B2 / 2 - gs0
        assert B4 / 2 + k4 + gs0 == 0
        assert b4 + B4 / 2 - k4 + gspi == 0
        assert B2 / 2 + k2 + gs0 == 0
        assert b2 + B2 / 2 - k2 + gspi == 0
    return [k4, k2]


def full_vector(kind, gs0=Fraction(-3, 2), reflected=False):
    return first_vector(kind, reflected) + gravity_vector(kind, gs0, reflected)

quartet = full_vector("quartet")
quartet_reflected = full_vector("quartet", reflected=True)
doublet_pair = full_vector("doublet_pair")
assert quartet == [Fraction(1, 2), Fraction(1, 4), 0, 2, 2, Fraction(-1, 4), 0]
assert quartet_reflected == [Fraction(-1, 2), Fraction(-1, 4), 0, -2, -2, Fraction(1, 4), 0]
assert doublet_pair == [0, 0, -1, -16, -4, 0, Fraction(-1, 2)]

# A different GS endpoint split changes the gauge-gravity inflow levels.
alternate_gs0 = Fraction(-2)
quartet_alt = full_vector("quartet", gs0=alternate_gs0)
assert quartet_alt[-2:] == [Fraction(1, 4), Fraction(1, 2)]
assert quartet_alt[-2:] != quartet[-2:]


def all_integral(v):
    return all(x.denominator == 1 for x in v)
assert not all_integral(quartet)
assert not all_integral(doublet_pair)

result = {
    "schema": "marici.flavor.wp1069.v1",
    "status": "PASS",
    "question": "What local anomaly vector follows from a symmetric split of WP1068's parent Green-Schwarz coefficient?",
    "conditional_law": "parent GS coefficient -3 is split as g0=gpi=-3/2",
    "channels": first_channels + grav_channels,
    "full_inflow_vectors": {
        "one_quartet": [str(x) for x in quartet],
        "one_quartet_reflected": [str(x) for x in quartet_reflected],
        "doublet_pair_C23_k0": [str(x) for x in doublet_pair],
    },
    "split_fiber": {
        "alternate_gs0": str(alternate_gs0),
        "alternate_one_quartet_gravity_levels": [str(x) for x in quartet_alt[-2:]],
        "symmetric_one_quartet_gravity_levels": [str(x) for x in quartet[-2:]],
    },
    "integral_lattice": {
        "one_quartet": all_integral(quartet),
        "doublet_pair_C23_k0": all_integral(doublet_pair),
    },
    "classification": "conditional local Green-Schwarz split: symmetric parent completion gives the seven-channel quartet vector (1/2,1/4,0,2,2,-1/4,0), but the endpoint split remains underived",
    "remaining_gate": "derive the Green-Schwarz endpoint split and a multicomponent shifted Chern-Simons quantization lattice from the UV compactification",
    "claim_boundary": "assumes a local symmetric split of the WP1068 parent coefficient; other splits change the gauge-gravity levels",
    "disposition": "productive: the shifted localization law now has a complete conditional seven-channel vector and an exact split hostile",
}

(ROOT / "results" / "wp1069_local_green_schwarz_split_cofiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1069 PASS:", quartet, doublet_pair, quartet_alt[-2:])
