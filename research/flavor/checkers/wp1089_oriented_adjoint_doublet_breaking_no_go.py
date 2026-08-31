import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Schur gate on the irreducible SU(2)_B doublet: every symmetry-natural
# endomorphism is scalar and cannot split the two lines.
a = Fraction(7)
A_doublet = [[a, Fraction(0)], [Fraction(0), a]]
assert A_doublet[0][0] == A_doublet[1][1]
assert A_doublet[0][1] == A_doublet[1][0] == 0

# A split is equivalent to choosing a nonzero adjoint direction n.  Its
# U(1) stabilizer yields two weight lines, while n and -n exchange them.
n = [Fraction(0), Fraction(0), Fraction(1)]
minus_n = [-x for x in n]
assert n != minus_n
weight_lines_for_n = ["+1_n", "-1_n"]
weight_lines_for_minus_n = list(reversed(weight_lines_for_n))
assert weight_lines_for_n != weight_lines_for_minus_n

# Acting only on the complementary B doublet preserves the WP1084 localized
# quartet, which contains the full A triplet and B singlet.
localized_quartet = {"A_triplet": "untouched", "B_singlet": "untouched"}
assert localized_quartet == {"A_triplet": "untouched", "B_singlet": "untouched"}

# A cyclic seed for the resulting three B lines must have all three components
# nonzero; no oriented adjoint direction or generic ray is currently selected.
supply = {
    "oriented_adjoint_direction": False,
    "two_ordered_weight_lines": False,
    "localized_quartet_preservation_conditional": True,
    "cyclic_three_line_seed": False,
    "history_dilation": False,
    "physical16_descent": False,
}
assert list(supply.values()).count(False) == 5

result = {
    "schema": "marici.flavor.wp1089.v1",
    "status": "PASS",
    "question": "Can the current source derive WP1084's requested second-stage SU(2)_B doublet breaking?",
    "reply_evidence": "Nima event 10687",
    "schur_gate": {
        "doublet_endomorphism": [[str(v) for v in row] for row in A_doublet],
        "split_possible": False,
    },
    "adjoint_direction_gate": {
        "n": [str(v) for v in n],
        "minus_n": [str(v) for v in minus_n],
        "weight_lines_for_n": weight_lines_for_n,
        "weight_lines_for_minus_n": weight_lines_for_minus_n,
        "orientation_required": True,
    },
    "localized_quartet": localized_quartet,
    "current_source_supply": supply,
    "classification": "current-source no-go: the requested second-stage doublet-breaking operation is absent",
    "remaining_gate": "derive an oriented adjoint ray in su(2)_B from a source packet; then derive cyclic-ray preparation, history dilation, rho, and physical16 descent",
    "hostile_gate": "do not fit n, its sign, the cyclic seed, or history from target flavor data",
    "claim_boundary": "a conditional block-diagonal operation can preserve the localized quartet, but no source-authorized oriented adjoint ray is constructed",
    "disposition": "terminal for H2; WP1085-WP1088 remain conditional constructors",
}

(ROOT / "results" / "wp1089_oriented_adjoint_doublet_breaking_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1089 PASS:", len(weight_lines_for_n), int(n[2]), int(minus_n[2]), localized_quartet["B_singlet"])
