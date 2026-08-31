import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def response(ratio):
    return Fraction(1, 1 + ratio)

# WP770's instrument uses two calibrated momentum ports p=1,2 in units of its
# mass standard m=1.  Conditionally lock that standard to WP1060's common pole
# mass M.  Then the instrument ratios are 1 and 4.
instrument_pair = {
    "soft_port": {"ratio": Fraction(1), "response": response(1), "authority": "WP770 reference momentum standard"},
    "vector_check_port": {"ratio": Fraction(4), "response": response(4), "authority": "WP771/WP1062 same-radius vector KK standard"},
}
assert instrument_pair["soft_port"]["response"] == Fraction(1, 2)
assert instrument_pair["vector_check_port"]["response"] == Fraction(1, 5)

# The pair is a genuine two-port readout: the response rows are independent.
def det_for_pair(r1, r2):
    return response(r2) - response(r1)

instrument_det = det_for_pair(1, 4)
vector_only_det = det_for_pair(4, 16)
assert instrument_det == Fraction(-3, 10)
assert vector_only_det == Fraction(-12, 85)
assert instrument_det != 0 and vector_only_det != 0

# Exact hostile: replacing the soft reference by the N=1 vector port gives two
# independent vector ports, ratios 4 and 16, but loses WP1042's ratio-one row.
vector_only_pair = {
    "ratios": [Fraction(4), Fraction(16)],
    "responses": [response(4), response(16)],
    "contains_ratio_one": False,
}
assert vector_only_pair["responses"] == [Fraction(1, 5), Fraction(1, 17)]
assert Fraction(1) not in vector_only_pair["ratios"]

# The soft port closes WP1042's granted shape only conditionally.  It is not a
# derived physical16 production/decay channel.
wp1042_shape = instrument_pair["soft_port"]["response"]
assert wp1042_shape == Fraction(1, 2)

result = {
    "schema": "marici.flavor.wp1063.v1",
    "status": "PASS",
    "question": "Can WP770's two-port instrument be locked to WP1060's common pole clock?",
    "conditional_identification": "set WP770's instrument mass unit m equal to the WP1060 common pole mass M",
    "instrument_pair": {
        name: {k: (str(v) if isinstance(v, Fraction) else v) for k, v in value.items()}
        for name, value in instrument_pair.items()
    },
    "response_determinant": str(instrument_det),
    "vector_only_hostile": {
        **{k: ([str(x) for x in v] if isinstance(v, list) else v) for k, v in vector_only_pair.items()},
        "response_determinant": str(vector_only_det),
    },
    "wp1042_shape": str(wp1042_shape),
    "classification": "conditional soft-scale two-port instrument: locking WP770's mass standard to the common pole clock gives ratios 1 and 4 and restores the 1/2 shape, but the soft port remains an instrument reference rather than a derived physical16 channel",
    "remaining_gate": "realize the soft and vector momentum ports in actual physical16 production/decay channels and derive the source-to-detector gain law in the same frame",
    "claim_boundary": "combines WP770's calibrated instrument with WP1060-WP1062's common clock and vector ratios; it does not fix the absolute radius or physical16 gain",
    "disposition": "productive: the momentum blocker is reduced from an abstract ratio-one gap to a concrete physical16 channel-realization gate",
}

(ROOT / "results" / "wp1063_soft_scale_two_port_instrument_lock.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1063 PASS:", wp1042_shape, instrument_det, vector_only_pair["responses"])
