import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

quartet = [Fraction(1, 2), Fraction(1, 4), 0, 2, 2, Fraction(-1, 4), 0]
reflected = [-x for x in quartet]
doublet_pair = [0, 0, -1, -16, -4, 0, Fraction(-1, 2)]
alternate_split_quartet = [Fraction(1, 2), Fraction(1, 4), 0, 2, 2, Fraction(1, 4), Fraction(1, 2)]


def residue_mod_integer(v):
    return [x - (x.numerator // x.denominator) for x in v]

q_res = residue_mod_integer(quartet)
r_res = residue_mod_integer(reflected)
d_res = residue_mod_integer(doublet_pair)
a_res = residue_mod_integer(alternate_split_quartet)

expected_q = [Fraction(1, 2), Fraction(1, 4), 0, 0, 0, Fraction(3, 4), 0]
expected_r = [Fraction(1, 2), Fraction(3, 4), 0, 0, 0, Fraction(1, 4), 0]
expected_d = [0, 0, 0, 0, 0, 0, Fraction(1, 2)]
expected_a = [Fraction(1, 2), Fraction(1, 4), 0, 0, 0, Fraction(1, 4), Fraction(1, 2)]
assert q_res == expected_q
assert r_res == expected_r
assert d_res == expected_d
assert a_res == expected_a

# A single shifted lattice coset s+Z^7 admits exactly vectors with one residue
# vector.  The one-quartet coset therefore rejects the doublet-pair cell and
# the reflected-orientation cell; endpoint orientation must be selected too.
assert q_res != d_res
assert q_res != r_res
assert q_res != a_res

common_denominator = 1
for x in quartet:
    common_denominator = math.lcm(common_denominator, x.denominator)
assert common_denominator == 4

result = {
    "schema": "marici.flavor.wp1070.v1",
    "status": "PASS",
    "question": "What exact shifted Chern-Simons lattice coset is required by the conditional seven-channel one-quartet vector?",
    "channels": ["SU4^3", "SU4^2 U1", "SU2^2 U1", "U1^3", "U1 grav", "SU4 grav", "SU2 grav"],
    "residue_vectors_mod_integer_lattice": {
        "one_quartet": [str(x) for x in q_res],
        "one_quartet_reflected": [str(x) for x in r_res],
        "doublet_pair_C23_k0": [str(x) for x in d_res],
        "alternate_split_one_quartet": [str(x) for x in a_res],
    },
    "common_denominator": common_denominator,
    "single_coset_admission": {
        "one_quartet_coset_admits_one_quartet": True,
        "one_quartet_coset_admits_reflected_orientation": q_res == r_res,
        "one_quartet_coset_admits_doublet_pair": q_res == d_res,
        "one_quartet_coset_admits_alternate_split": q_res == a_res,
    },
    "classification": "shifted-coset gate: the symmetric-split one-quartet cell requires the exact residue vector (1/2,1/4,0,0,0,3/4,0) modulo the integral CS lattice",
    "remaining_gate": "derive this coset and endpoint orientation from the UV compactification rather than choosing the symmetric split",
    "claim_boundary": "computes lattice residues only; it does not prove that the UV theory realizes the required shifted coset",
    "disposition": "productive: shifted quantization is now an exact multicomponent coset test rather than a generic half-integer allowance",
}

(ROOT / "results" / "wp1070_shifted_chern_simons_coset_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1070 PASS:", q_res, d_res, common_denominator)
