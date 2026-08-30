"""Exact C2^5 character support of the source five-cycle canonical function."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OFPT = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
COVER = ROOT / "research/benincasa/results/five-site-d3-marked-kummer-cover.json"
OUTPUT = ROOT / "research/benincasa/results/five-cycle-canonical-deck-support.json"

terms = json.loads(OFPT.read_text())["five_cycle"]["terms"]
facets = json.loads(COVER.read_text())["facet_forms"]
common = ["G", "g_1", "g_2", "g_3", "g_4", "g_5"]


def q_value(label, xs, ys):
    q = facets[label]
    return sum(Fraction(a) * b for a, b in zip(q["x"], xs)) + sum(
        Fraction(a) * b for a, b in zip(q["y"], ys)
    )


def omega(xs, positive_ys, sheet):
    ys = [Fraction(sign) * y for sign, y in zip(sheet, positive_ys)]
    denominator = Fraction(1)
    for label in common:
        value = q_value(label, xs, ys)
        assert value
        denominator *= value
    total = Fraction(0)
    for term in terms:
        product = Fraction(1)
        for label in term:
            value = q_value(label, xs, ys)
            assert value
            product *= value
        total += 1 / product
    return total / denominator


def sheets():
    for mask in range(32):
        yield tuple(-1 if mask & (1 << i) else 1 for i in range(5))


def character(sheet, mask):
    value = 1
    for i, sign in enumerate(sheet):
        if mask & (1 << i):
            value *= sign
    return value


def audit(xs, ys):
    values = {sheet: omega(xs, ys, sheet) for sheet in sheets()}
    fourier = {
        mask: sum(character(sheet, mask) * value for sheet, value in values.items())
        for mask in range(32)
    }
    support = [mask for mask, value in fourier.items() if value]
    return {
        "X": [str(x) for x in xs],
        "positive_y": [str(y) for y in ys],
        "sheet_value_count": len(values),
        "nonzero_character_masks": support,
        "support_size": len(support),
        "numerator_bit_lengths": {
            str(mask): abs(value.numerator).bit_length() for mask, value in fourier.items()
        },
        "denominator_bit_lengths": {
            str(mask): value.denominator.bit_length() for mask, value in fourier.items()
        },
    }


samples = [
    audit(list(map(Fraction, [2, 3, 5, 7, 11])), list(map(Fraction, [101, 103, 107, 109, 113]))),
    audit(list(map(Fraction, [31, 37, 41, 43, 47])), list(map(Fraction, [127, 131, 137, 139, 149]))),
]
assert all(sample["support_size"] == 32 for sample in samples)
assert all(sample["nonzero_character_masks"] == list(range(32)) for sample in samples)


def rotate_mask(mask):
    result = 0
    for i in range(5):
        if mask & (1 << i):
            result |= 1 << ((i + 1) % 5)
    return result


unseen = set(range(32))
character_orbits = []
while unseen:
    seed = min(unseen)
    orbit = []
    current = seed
    while current not in orbit:
        orbit.append(current)
        unseen.discard(current)
        current = rotate_mask(current)
    character_orbits.append(orbit)

assert sorted(map(len, character_orbits)) == [1, 1, 5, 5, 5, 5, 5, 5]

result = {
    "schema": "marici.benincasa.five_cycle_canonical_deck_support.v1",
    "deck_group": "C2^5",
    "transform": "exact unnormalized Walsh-Hadamard transform over all 32 sheets",
    "samples": samples,
    "generic_character_support": "all 32 characters",
    "minimal_generic_deck_stable_block_rank": 32,
    "cyclic_character_orbits": character_orbits,
    "cyclic_character_orbit_sizes": [len(orbit) for orbit in character_orbits],
    "cyclic_invariant_character_dimension": 8,
    "scope": "source canonical rational function before integration",
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"support_sizes": [x["support_size"] for x in samples], "rank": 32}))
