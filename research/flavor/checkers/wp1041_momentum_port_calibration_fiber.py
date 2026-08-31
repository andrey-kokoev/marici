import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

C = 23
k = 2
h_coeff = Fraction(12 * C, 1367 * k)

# Degenerate normalized response depends only on the dimensionless ratio p2/M2.
def response(M2, p2):
    return Fraction(M2, M2 + p2)

same_ratio_a = {"M2": 1, "p2": 1, "response": response(1, 1)}
same_ratio_b = {"M2": 2, "p2": 2, "response": response(2, 2)}
assert same_ratio_a["response"] == same_ratio_b["response"] == Fraction(1, 2)

# A calibrated momentum port separates the masses; an uncalibrated common scale does not.
calibrated_a = response(1, 1)
calibrated_b = response(2, 1)
assert calibrated_a == Fraction(1, 2)
assert calibrated_b == Fraction(2, 3)
assert calibrated_b - calibrated_a == Fraction(1, 6)

# The zero-momentum coefficient is unchanged throughout.
assert h_coeff == Fraction(138, 1367)

result = {
    "schema": "marici.flavor.wp1041.v1",
    "status": "PASS",
    "question": "Can finite-response readout close WP1040 without an independently calibrated momentum port?",
    "fixed_source_data": {
        "k": k,
        "C": C,
        "h": "138*pi^2/1367",
        "degenerate_pole_type": True
    },
    "response_law": "R(p2)/R(0)=M2/(M2+p2)",
    "common_scale_hostile": {
        "packet_A": {"M2": 1, "p2": 1, "normalized_response": str(same_ratio_a["response"])},
        "packet_B": {"M2": 2, "p2": 2, "normalized_response": str(same_ratio_b["response"])},
        "shared_ratio": "p2/M2=1"
    },
    "calibrated_port_separation": {
        "same_p2_1_M2_1": str(calibrated_a),
        "same_p2_1_M2_2": str(calibrated_b),
        "difference": "1/6"
    },
    "first_nonfaithful_arrow": "finite threshold response to absolute pole mass without a momentum standard",
    "classification": "finite response is faithful to p2/M2 on the degenerate one-pole domain; it is not an absolute mass or source selector",
    "remaining_gate": "derive or calibrate the physical momentum port in the same frame as the pole mass and physical16 detector, then separately derive the source value of the ratio",
    "claim_boundary": "degenerate one-pole normalized response; does not address split spectra already rejected by WP1039",
    "disposition": "negative for readout-only repair of the WP1040 mass-clock fiber"
}

(ROOT / "results" / "wp1041_momentum_port_calibration_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1041 PASS:", same_ratio_a["response"], same_ratio_b["response"], calibrated_b - calibrated_a)
