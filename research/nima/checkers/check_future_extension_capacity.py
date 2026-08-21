"""Finite falsifier and surviving recursion for future-extension capacity."""

import json
from pathlib import Path
import sympy as sp


def H(ps):
    return sp.simplify(-sum(p*sp.log(p) for p in ps if p != 0))


# A two-level typed future tree.
root = [sp.Rational(1, 3), sp.Rational(2, 3)]
conditional_second = [sp.Rational(1, 4), sp.Rational(3, 4)]
leaves = [root[0], root[1]*conditional_second[0], root[1]*conditional_second[1]]
chain_residual = sp.simplify(H(leaves) - H(root) - root[1]*H(conditional_second))
assert chain_residual == 0

# Null/presentation refinement changes raw cardinality but not physical entropy.
with_null = root + [sp.Rational(0)]
assert len(with_null) != len(root)
assert sp.simplify(H(with_null) - H(root)) == 0

# Independent composition is additive in H and multiplicative in exp(H).
q = [sp.Rational(1, 4), sp.Rational(3, 4)]
product = [p*r for p in root for r in q]
tensor_residual = sp.simplify(H(product) - H(root) - H(q))
assert tensor_residual == 0

# Raw support count would assign equal weights, contradicting a nonuniform
# source-derived Born state.
born = [sp.Rational(9, 10), sp.Rational(1, 10)]
count_weights = [sp.Rational(1, 2), sp.Rational(1, 2)]
assert born != count_weights

result = {
    "status": "PASS",
    "raw_count_falsifier": {
        "original_count": len(root),
        "null_refined_count": len(with_null),
        "entropy_change": "0",
    },
    "born_vs_count": {
        "born_weights": [str(v) for v in born],
        "count_weights": [str(v) for v in count_weights],
        "equal": False,
    },
    "shannon_chain_residual": str(chain_residual),
    "independent_product_residual": str(tensor_residual),
    "surviving_capacity": "C(h)=H(p_next)+sum_i p_i C(h_i)",
    "selection_law_status": "not derived",
}
out = Path(__file__).parents[1] / "results" / "future_extension_capacity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
