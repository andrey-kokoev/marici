import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Branch data under SU(4)xSU(2)xU(1).  T values are total Dynkin indices with
# T(fund)=1/2 and include the dimension of the other factor.
branches = [
    {"id": "15_to_6", "dim": 6, "q": Fraction(2), "A4": Fraction(0), "T4": Fraction(1), "T2": Fraction(0)},
    {"id": "15_to_8", "dim": 8, "q": Fraction(-1), "A4": Fraction(2), "T4": Fraction(1), "T2": Fraction(2)},
    {"id": "15_to_1", "dim": 1, "q": Fraction(-4), "A4": Fraction(0), "T4": Fraction(0), "T2": Fraction(0)},
    {"id": "bar6a_to_4", "dim": 4, "q": Fraction(-1), "A4": Fraction(-1), "T4": Fraction(1, 2), "T2": Fraction(0)},
    {"id": "bar6a_to_2", "dim": 2, "q": Fraction(2), "A4": Fraction(0), "T4": Fraction(0), "T2": Fraction(1, 2)},
    {"id": "bar6b_to_4", "dim": 4, "q": Fraction(-1), "A4": Fraction(-1), "T4": Fraction(1, 2), "T2": Fraction(0)},
    {"id": "bar6b_to_2", "dim": 2, "q": Fraction(2), "A4": Fraction(0), "T4": Fraction(0), "T2": Fraction(1, 2)},
]

CHANNELS = ["SU4^3", "SU4^2 U1", "SU2^2 U1", "U1^3", "U1 grav"]


def coeff(b, channel):
    if channel == "SU4^3":
        return b["A4"]
    if channel == "SU4^2 U1":
        return b["q"] * b["T4"]
    if channel == "SU2^2 U1":
        return b["q"] * b["T2"]
    if channel == "U1^3":
        return b["dim"] * b["q"] ** 3
    if channel == "U1 grav":
        return b["dim"] * b["q"]
    raise AssertionError(channel)

# All admitted channels have vanishing full-family anomaly.  Gauge-gravity
# SU4/SU2 channels are not admitted here because the subgroup truncation has
# nonzero total coefficients and needs an external completion.
for channel in CHANNELS:
    assert sum(coeff(b, channel) for b in branches) == 0
assert sum(b["T4"] for b in branches) == 3
assert sum(b["T2"] for b in branches) == 3

by_id = {b["id"]: b for b in branches}


def inflow_vector(boundary_ids, endpoint=0):
    boundary = [by_id[i] for i in boundary_ids]
    bvec = [sum(coeff(b, channel) for b in boundary) for channel in CHANNELS]
    Bvec = [-x for x in bvec]
    if endpoint == 0:
        kvec = [-b - B / 2 for b, B in zip(bvec, Bvec)]
    else:
        kvec = [-(Fraction(0)) - B / 2 for B in Bvec]
        # Local cancellation at endpoint pi gives A_pi=b+B/2-k=0.
        kvec = [b + B / 2 for b, B in zip(bvec, Bvec)]
    # Verify the displayed fixed-point equations.
    if endpoint == 0:
        assert all(b + B / 2 + k == 0 for b, B, k in zip(bvec, Bvec, kvec))
        assert all(B / 2 - k == 0 for B, k in zip(Bvec, kvec))
    else:
        assert all(B / 2 + k == 0 for B, k in zip(Bvec, kvec))
        assert all(b + B / 2 - k == 0 for b, B, k in zip(bvec, Bvec, kvec))
    return kvec

quartet = inflow_vector(["bar6a_to_4"])
quartet_reflected = inflow_vector(["bar6a_to_4"], endpoint=1)
doublet_pair = inflow_vector(["bar6a_to_2", "bar6b_to_2"])
bifundamental8 = inflow_vector(["15_to_8"])
singlet = inflow_vector(["15_to_1"])

assert quartet == [Fraction(1, 2), Fraction(1, 4), 0, 2, 2]
assert quartet_reflected == [-x for x in quartet]
assert doublet_pair == [0, 0, -1, -16, -4]
assert bifundamental8 == [-1, Fraction(1, 2), 1, 4, 4]
assert singlet == [0, 0, 0, 32, 2]

def all_integral(vec):
    return all(x.denominator == 1 for x in vec)
assert not all_integral(quartet)
assert all_integral(doublet_pair)
assert not all_integral(bifundamental8)
assert all_integral(singlet)

result = {
    "schema": "marici.flavor.wp1067.v1",
    "status": "PASS",
    "question": "What complete globally vanishing anomaly vector does the one-quartet localization require?",
    "normalization": "A(4)=1 and T(fund)=1/2; T values include the dimension of the other product factor",
    "channels": CHANNELS,
    "inflow_vectors": {
        "one_quartet": [str(x) for x in quartet],
        "one_quartet_reflected": [str(x) for x in quartet_reflected],
        "doublet_pair_C23_k0": [str(x) for x in doublet_pair],
        "bifundamental8_C19": [str(x) for x in bifundamental8],
        "singlet_C26": [str(x) for x in singlet],
    },
    "integral_lattice": {
        "one_quartet": all_integral(quartet),
        "doublet_pair_C23_k0": all_integral(doublet_pair),
        "bifundamental8_C19": all_integral(bifundamental8),
        "singlet_C26": all_integral(singlet),
    },
    "excluded_completion_channels": {
        "SU4_gravity_total_index": "3",
        "SU2_gravity_total_index": "3",
        "reason": "nonzero full-family gauge-gravity coefficients require an external Green-Schwarz or UV completion before local inflow can be tested",
    },
    "classification": "complete vanishing-channel anomaly-vector gate: the one-quartet cell requires the half/quarter level vector (1/2,1/4,0,2,2), while the port-destroying C=23 doublet-pair cell is integral on these channels",
    "remaining_gate": "derive a multicomponent shifted Chern-Simons quantization law and complete the nonzero SU4/SU2 gauge-gravity channels from the UV theory",
    "claim_boundary": "covers exactly the five globally vanishing perturbative channels listed; it does not prove or reject a future shifted lattice",
    "disposition": "productive: the shifted-quantization requirement is now an exact vector rather than a single SU(4) cubic level",
}

(ROOT / "results" / "wp1067_localized_quartet_anomaly_vector_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1067 PASS:", quartet, doublet_pair, all_integral(quartet), all_integral(doublet_pair))
