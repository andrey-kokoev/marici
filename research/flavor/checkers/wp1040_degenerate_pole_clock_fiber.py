import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

C = 23
k = 2
h_coeff = Fraction(12 * C, 1367 * k)
q2 = Fraction(1, 1)

# Degenerate S_C-symmetric pole packet, with residues scaled so R(0)=C for
# every common pole mass M2.  The normalized finite response is M2/(M2+q2).
def normalized_degenerate_response(M2):
    residues = [Fraction(M2, 1)] * C
    masses = [Fraction(M2, 1)] * C
    R0 = sum(r / m for r, m in zip(residues, masses))
    Rq = sum(r / (m + q2) for r, m in zip(residues, masses))
    assert R0 == C
    return Rq / R0

r1 = normalized_degenerate_response(1)
r2 = normalized_degenerate_response(2)
assert r1 == Fraction(1, 2)
assert r2 == Fraction(2, 3)
assert r2 - r1 == Fraction(1, 6)

result = {
    "schema": "marici.flavor.wp1040.v1",
    "status": "PASS",
    "question": "Does exact degeneracy of the C=23 pole packet select the threshold clock?",
    "granted_structure": [
        "k=2",
        "C=23",
        "S23 exchange symmetry among the unit operator copies",
        "one exactly degenerate pole mass within each packet",
        "residues scaled so the zero-momentum coefficient is fixed"
    ],
    "fixed_zero_momentum_data": {
        "h": "138*pi^2/1367",
        "R0": C
    },
    "hostile_degenerate_packets": {
        "M2=1": {"normalized_R_at_q2_1": str(r1)},
        "M2=2": {"normalized_R_at_q2_1": str(r2)}
    },
    "finite_response_difference": "1/6 at q2=1 after zero-momentum normalization",
    "shared_readouts": ["same k", "same C", "same h at q2=0", "same S23 degeneracy", "same positive pole type"],
    "first_nonfaithful_arrow": "degenerate integer pole packet to physical threshold clock M2/q2",
    "classification": "exchange-enforced degeneracy is a threshold rigidifier, not a mass-clock selector",
    "remaining_gate": "derive the common pole mass in physical units, or a source-locked ratio q2/M2 for the physical16 instrument, from the same source selecting k,C and the pole operator",
    "claim_boundary": "degenerate positive pole packets with fixed zero-momentum coefficient; does not exclude a topological or fixed-point mass-clock theorem",
    "disposition": "negative for degeneracy-only repair of WP1039"
}

(ROOT / "results" / "wp1040_degenerate_pole_clock_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1040 PASS:", r1, r2, r2 - r1)
