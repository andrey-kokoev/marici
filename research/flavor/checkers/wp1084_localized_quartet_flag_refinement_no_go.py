import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Align the localized SU(4)xSU(2) decomposition with WP1080's
# SU(3)_A x SU(3)_B carrier through the common subgroup
# SU(3)_A x SU(2)_B x U(1):
#   6=(3,1)+(1,2)+(1,1).
# The localized quartet is the full A triplet plus the B singlet; the
# remaining B doublet is the SU(2) factor.
common_branching = [
    {"sector": "localized_4", "rep": "(3_A,1_B)", "dim": 3},
    {"sector": "localized_4", "rep": "(1_A,1_B)", "dim": 1},
    {"sector": "su2_complement", "rep": "(1_A,2_B)", "dim": 2},
]
assert sum(x["dim"] for x in common_branching) == 6

# Natural endomorphisms on each triplet under the common subgroup:
# A side remains irreducible: one eigenvalue.
# B side splits 2+1: at most two eigenvalues.
a = Fraction(2)
b = Fraction(5)
A_side_spectrum = [a, a, a]
B_side_spectrum = [a, a, b]
assert len(set(A_side_spectrum)) == 1
assert len(set(B_side_spectrum)) == 2

# The 2+1 B-side operator cannot generate a three-dimensional Krylov space.
def det3(cols):
    (p,q,r),(s,t,u),(v,w,x) = cols
    return p*(t*x-u*w)-q*(s*x-u*v)+r*(s*w-t*v)
x = [Fraction(1), Fraction(2), Fraction(3)]
A_B = [a, a, b]
Ax = [ai*xi for ai,xi in zip(A_B,x)]
A2x = [ai*xi for ai,xi in zip(A_B,Ax)]
assert det3([x,Ax,A2x]) == 0

supply = {
    "localized_4_aligned_with_common_subgroup": True,
    "b_side_two_plus_one_flag": True,
    "a_side_simple_spectrum": False,
    "b_side_simple_spectrum": False,
    "ordered_three_line_eigenflag": False,
    "canonical_cyclic_ray": False,
    "history_dilation": False,
}
assert list(supply.values()).count(False) == 5

result = {
    "schema": "marici.flavor.wp1084.v1",
    "status": "PASS",
    "question": "Does the localized SU(4)xSU(2) cell refine either WP1080 SU(3) triplet to a simple-spectrum ordered flag?",
    "common_branching": common_branching,
    "spectra": {
        "A_side": [str(v) for v in A_side_spectrum],
        "A_side_distinct_count": len(set(A_side_spectrum)),
        "B_side": [str(v) for v in B_side_spectrum],
        "B_side_distinct_count": len(set(B_side_spectrum)),
    },
    "krylov_witness": {
        "A_B": [str(v) for v in A_B],
        "x": [str(v) for v in x],
        "determinant": str(det3([x,Ax,A2x])),
    },
    "current_localization_supply": supply,
    "classification": "localized-quartet flag no-go: the common subgroup gives an A-side unbroken triplet and only a B-side 2+1 flag; neither yields a simple-spectrum Krylov evolution",
    "remaining_gate": "derive a second-stage source breaking of the SU(2) doublet into two ordered lines, or a different localization producing a 1+1+1 flag, together with cyclic-ray preparation and history dilation",
    "claim_boundary": "uses one natural alignment of SU(3)xSU(3) with SU(4)xSU(2); a different alignment would need its own source derivation and still requires three distinguished lines",
    "disposition": "productive: the obvious existing localization refinement is closed and the successor breaking is sharpened",
}

(ROOT / "results" / "wp1084_localized_quartet_flag_refinement_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1084 PASS:", len(set(A_side_spectrum)), len(set(B_side_spectrum)), det3([x,Ax,A2x]))
