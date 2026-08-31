import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1060 pole/soft clock and WP771 vector KK ports share the same radius.
# M^2=1/(4R^2), while p_N^2=M_V,N^2=N^2/R^2.
def ratio_for_vector_level(N):
    return Fraction(4 * N * N, 1)


def normalized_response(ratio):
    return Fraction(1, 1 + ratio)

vector_ports = []
for N in (1, 2):
    ratio = ratio_for_vector_level(N)
    vector_ports.append({
        "port": f"vector_KK_N{N}",
        "p2_over_M2": ratio,
        "normalized_response": normalized_response(ratio),
    })
assert vector_ports[0]["p2_over_M2"] == 4
assert vector_ports[0]["normalized_response"] == Fraction(1, 5)
assert vector_ports[1]["p2_over_M2"] == 16
assert vector_ports[1]["normalized_response"] == Fraction(1, 17)

# The WP1042 granted ratio-1 port is a separate soft/pole-scale momentum
# channel.  The vector KK law alone does not supply it.
soft_scale_port = {
    "port": "soft_or_pole_scale",
    "p2_over_M2": Fraction(1),
    "normalized_response": Fraction(1, 2),
    "source_channel_derived": False,
}
assert soft_scale_port["normalized_response"] == Fraction(1, 2)

# The two vector ports are independent standards, but neither gives the ratio
# used by WP1042.  Promoting the N=1 vector port to p^2=M^2 changes 1/5 to 1/2.
assert vector_ports[0]["normalized_response"] != soft_scale_port["normalized_response"]
assert soft_scale_port["normalized_response"] - vector_ports[0]["normalized_response"] == Fraction(3, 10)

# Radius rescaling cancels from every ratio, so the cofiber is same-frame even
# before WP1061's absolute clock is fixed.
for R in (1, 2, 3):
    M2 = Fraction(1, 4 * R * R)
    p2 = Fraction(1, R * R)
    assert p2 / M2 == 4

result = {
    "schema": "marici.flavor.wp1062.v1",
    "status": "PASS",
    "question": "What same-frame momentum ratios does the common-twist/KK source supply?",
    "same_frame_law": "M^2=1/(4R^2), p_N^2=N^2/R^2, hence p_N^2/M^2=4N^2",
    "vector_ports": [
        {k: (str(v) if isinstance(v, Fraction) else v) for k, v in port.items()}
        for port in vector_ports
    ],
    "soft_scale_port": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in soft_scale_port.items()},
    "response_gap_between_N1_and_soft_port": str(Fraction(3, 10)),
    "radius_cancellation_verified": True,
    "classification": "conditional same-frame momentum cofiber: the source-derived vector KK ports have ratios 4 and 16, while the WP1042 ratio-1 readout requires a distinct soft/pole-scale channel",
    "remaining_gate": "derive an actual physical16 production/decay momentum channel at the soft/pole scale, or revise the integer-pole readout to a source-derived vector-KK ratio and carry that response through the gain chain",
    "claim_boundary": "uses the common radius frame of WP771 and WP1060; it does not select the absolute radius or prove that the vector KK port is the flavor detector port",
    "disposition": "productive: the momentum blocker is sharpened to a missing soft-scale channel, with an exact N=1 vector-port hostile",
}

(ROOT / "results" / "wp1062_same_frame_kk_momentum_ratio_cofiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1062 PASS:", vector_ports[0]["p2_over_M2"], vector_ports[0]["normalized_response"], soft_scale_port["normalized_response"])
