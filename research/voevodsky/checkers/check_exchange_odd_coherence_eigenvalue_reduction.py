#!/usr/bin/env python3
"""Exact parity reversal of the exchange-odd shape derivative."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
S = sp.Matrix([[0, 1], [1, 0]])
N = sp.diag(1, -1)
even = sp.Matrix([1, 1])
odd = sp.Matrix([1, -1])

checks = {
    "shape_derivative_matrix": N == sp.Matrix([[1, 0], [0, -1]]),
    "twisted_exchange": N * S == -S * N,
    "even_simple_to_odd_doubled": N * even == odd,
    "odd_simple_to_even_doubled": N * odd == even,
    "involution_on_coordinates": N * N == sp.eye(2),
    "primitive_vectors_retained": sp.gcd(*map(abs, N * even)) == 1 and sp.gcd(*map(abs, N * odd)) == 1,
}
assert all(checks.values()), checks

out = {
    "schema": "marici.voevodsky.exchange-odd-coherence-parity-reversal.v2",
    "passed": True,
    "correction": "the shape derivative is anti-equivariant, not exchange-equivariant",
    "shape_derivative_matrix": [[1, 0], [0, -1]],
    "twisted_intertwining": "N_D S = - S N_D",
    "simple_even_to_doubled_odd": True,
    "simple_odd_to_doubled_even": True,
    "constructed_response_preimage": "the sourced doubled odd vector (1,-1) comes from the canonical simple even vector (1,1)",
    "v_alg_consequence": "inverse differentiation sends the constructed doubled odd response back to the simple even class, whose v_alg projection cancels",
    "required_for_v_alg": "source the simple odd mixed class; its shape derivative lies in the doubled even line",
    "checks": checks,
}
p = R / "research/voevodsky/results/exchange_odd_coherence_eigenvalue_reduction.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "twisted_exchange": True, "constructed_preimage": "simple-even", "v_alg_from_constructed_response": False}))
