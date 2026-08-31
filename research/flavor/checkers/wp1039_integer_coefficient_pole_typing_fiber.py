import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Zero-momentum coefficient C is the sum of unit operator weights.
C = 23
single_pole_masses = [1] * C
split_masses = [1] * 22 + [4]
assert len(single_pole_masses) == len(split_masses) == C

# Normalized finite-momentum response for unit residues:
# R(q2)/R(0)= C^{-1} sum_i 1/(1+q2/M_i^2).  Use q2=1.
def normalized_response(masses):
    return sum(Fraction(m, m + 1) for m in masses) / len(masses)

r_single = normalized_response(single_pole_masses)
r_split = normalized_response(split_masses)
assert r_single == Fraction(1, 2)
assert r_split == Fraction(59, 115)
assert r_split - r_single == Fraction(3, 230)

# Both packets have the same zero-momentum coefficient and therefore the same
# WP1036 h coefficient once k is fixed.
h_coeff = Fraction(12 * C, 1367 * 2)
assert h_coeff == Fraction(138, 1367)

result = {
    "schema": "marici.flavor.wp1039.v1",
    "status": "PASS",
    "question": "Does selecting the integer coefficient C=23 also select a typed single-pole threshold operator?",
    "fixed_zero_momentum_data": {
        "k": 2,
        "C": 23,
        "h": "138*pi^2/1367",
        "unit_residue_count": 23
    },
    "hostile_packets": {
        "single_pole": {"masses_squared": "23 copies of 1", "normalized_R_at_q2_1": str(r_single)},
        "split_pole": {"masses_squared": "22 copies of 1 plus one copy of 4", "normalized_R_at_q2_1": str(r_split)}
    },
    "finite_response_difference": "3/230 at q2=1 after zero-momentum normalization",
    "shared_readouts": ["same k", "same C", "same h at q2=0", "same number of unit residues"],
    "first_nonfaithful_arrow": "integer coefficient and zero-momentum pole normalization to complete finite-momentum pole spectrum",
    "classification": "integer coefficient rigidifier only; not a typed single-pole threshold selector",
    "remaining_gate": "derive degeneracy, residues, pole masses, and finite-momentum matching for the C=23 operator from the same source that selects the integer labels",
    "claim_boundary": "unit-residue positive pole packets at k=2,C=23; does not exclude a source theorem enforcing exact single-pole degeneracy",
    "disposition": "negative for promoting C=23 arithmetic capacity to threshold-ready physical normalization"
}

(ROOT / "results" / "wp1039_integer_coefficient_pole_typing_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1039 PASS:", r_single, r_split, r_split - r_single)
