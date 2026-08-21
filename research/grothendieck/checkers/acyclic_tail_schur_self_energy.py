"""Exact scalar and small-matrix audit of acyclic-tail Schur cancellation."""

from fractions import Fraction as F


# One physical mode, one even auxiliary mode, and its odd cancelling copy.
h_p = F(2)
h_a = F(5)
c = F(3)
even_block_det = h_p * h_a - c * c
graded_det = even_block_det / h_a
schur_det = h_p - c * c / h_a

assert even_block_det == 1
assert graded_det == F(1, 5)
assert graded_det == schur_det

result = {
    "even_block_determinant": "1",
    "odd_auxiliary_determinant": "5",
    "graded_determinant": "1/5",
    "schur_self_energy_identity": True,
    "auxiliary_net_weyl_multiplicity": "zero by even/odd pairing",
    "auxiliary_effect_survives": "-C(H_A-z)^(-1)C*",
    "physical_realization_still_required": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "acyclic-tail-schur-self-energy.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

