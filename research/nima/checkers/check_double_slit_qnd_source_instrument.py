"""Exact source-derived QND realization of double-slit complementarity."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/double-slit-qnd-source-instrument.json"

c = sp.Rational(3, 5)
s = sp.Rational(4, 5)

# Path-controlled pointer rotation in basis L0,L1,R0,R1.
rotation = sp.Matrix([[c, -s], [s, c]])
unitary = sp.diag(1, 1, 1, 1)
unitary[2:4, 2:4] = rotation

e_left = sp.Matrix([1, 0])
e_right = sp.Matrix([c, s])
overlap = (e_left.T * e_right)[0]
record_gram = sp.Matrix([[1, overlap], [overlap, 1]])

# The optimal binary separator is the difference of record projectors.
delta = e_left * e_left.T - e_right * e_right.T
delta_eigenvalues = sorted(delta.eigenvals().keys(), key=lambda value: float(value))
distinguishability = max(abs(value) for value in delta_eigenvalues)
visibility = abs(overlap)

# The source-generated eraser basis is the normalized sum/difference of the
# two record vectors. It produces full-visibility path subensembles with
# opposite phases; their weighted coherence recombines to the unconditioned
# overlap c/2.
e_plus = sp.simplify((e_left + e_right) / sp.sqrt(2 * (1 + c)))
e_minus = sp.simplify((e_left - e_right) / sp.sqrt(2 * (1 - c)))
plus_amplitudes = sp.Matrix([(e_plus.T * e_left)[0], (e_plus.T * e_right)[0]])
minus_amplitudes = sp.Matrix([(e_minus.T * e_left)[0], (e_minus.T * e_right)[0]])
plus_probability = sp.simplify((plus_amplitudes.dot(plus_amplitudes)) / 2)
minus_probability = sp.simplify((minus_amplitudes.dot(minus_amplitudes)) / 2)
plus_normalized_coherence = sp.simplify(
    plus_amplitudes[0] * plus_amplitudes[1] / (2 * plus_probability)
)
minus_normalized_coherence = sp.simplify(
    minus_amplitudes[0] * minus_amplitudes[1] / (2 * minus_probability)
)
recombined_coherence = sp.simplify(
    plus_probability * plus_normalized_coherence
    + minus_probability * minus_normalized_coherence
)

gates = {
    "source_pointer_coupling_is_unitary": sp.simplify(unitary.T * unitary) == sp.eye(4),
    "pointer_overlap_is_c": overlap == c,
    "visibility_is_three_fifths": visibility == c,
    "optimal_distinguishability_is_four_fifths": distinguishability == s,
    "complementarity_is_exact": sp.simplify(visibility**2 + distinguishability**2) == 1,
    "eraser_basis_is_orthonormal": sp.simplify(
        sp.Matrix.hstack(e_plus, e_minus).T * sp.Matrix.hstack(e_plus, e_minus)
    ) == sp.eye(2),
    "eraser_subensembles_have_opposite_full_coherence": (
        plus_normalized_coherence == sp.Rational(1, 2)
        and minus_normalized_coherence == sp.Rational(-1, 2)
    ),
    "forgetting_eraser_outcome_recovers_unconditioned_coherence": (
        recombined_coherence == c / 2
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.double-slit-qnd-source-instrument.v1",
    "source_coupling": {"c": str(c), "s": str(s)},
    "record_overlap": str(overlap),
    "visibility": str(visibility),
    "separator_eigenvalues": [str(value) for value in delta_eigenvalues],
    "distinguishability": str(distinguishability),
    "eraser": {
        "plus_probability": str(plus_probability),
        "minus_probability": str(minus_probability),
        "plus_normalized_coherence": str(plus_normalized_coherence),
        "minus_normalized_coherence": str(minus_normalized_coherence),
        "recombined_coherence": str(recombined_coherence),
    },
    "gates": gates,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

