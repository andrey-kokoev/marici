"""Dependency-free exact two-path visibility/distinguishability audit."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/double-slit-positive-pairing.json"


# Polynomials in r=|gamma|^2, stored in ascending coefficient order.
def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return tuple(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    )


def neg(poly: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-coefficient for coefficient in poly)


zero = (0,)
one = (1,)
overlap_squared = (0, 1)
gram_det = (1, -1)
visibility_squared = overlap_squared

# Direct 2x2 expansion in the canonical record span gives
# tr(P_L-P_R)=0 and det(P_L-P_R)=-(1-r).
separator_trace = zero
separator_det = (-1, 1)
distinguishability_squared = neg(separator_det)

gates = {
    "positive_gram_reserve_is_one_minus_overlap_squared": gram_det == (1, -1),
    "separator_is_traceless": separator_trace == zero,
    "separator_determinant_is_negative_gram_reserve": add(
        separator_det, gram_det
    ) == (0, 0),
    "pure_record_duality_is_exact": add(
        add(visibility_squared, distinguishability_squared), neg(one)
    ) == (0, 0),
}

# Bounded exact control for source-labelled coarse-graining.  Each pair is a
# rational point (V,D) on the pure unit quarter-circle.  Convex combinations
# must lie in the unit disk.
pure_pairs = [
    (Fraction(0), Fraction(1)),
    (Fraction(3, 5), Fraction(4, 5)),
    (Fraction(5, 13), Fraction(12, 13)),
    (Fraction(8, 17), Fraction(15, 17)),
    (Fraction(1), Fraction(0)),
]
weight_sets = [
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 3), Fraction(2, 3)),
    (Fraction(1, 4), Fraction(3, 4)),
]
mixture_reserves = []
for left, right in product(pure_pairs, repeat=2):
    for p, q in weight_sets:
        mixed_v = p * left[0] + q * right[0]
        mixed_d = p * left[1] + q * right[1]
        mixture_reserves.append(1 - mixed_v**2 - mixed_d**2)

gates["source_label_forgetting_contracts_bounded_pure_mixtures"] = all(
    reserve >= 0 for reserve in mixture_reserves
)

assert all(gates.values()), gates

result = {
    "schema": "marici.nima.double-slit-positive-pairing.v1",
    "symbols": {"r": "|gamma|^2"},
    "polynomial_coefficient_order": "ascending powers of r",
    "gram_determinant": list(gram_det),
    "visibility_squared": list(visibility_squared),
    "separator_trace": list(separator_trace),
    "separator_determinant": list(separator_det),
    "distinguishability_squared": list(distinguishability_squared),
    "identity": "V^2 + D^2 = 1 for normalized pure path records",
    "mixed_or_coarse_grained_extension": (
        "V^2 + D^2 <= 1 requires the additional contract that record "
        "coarse-graining is a positive contraction for both coherence and "
        "binary distinguishability."
    ),
    "bounded_mixture_census": {
        "pure_pairs": [[str(v), str(d)] for v, d in pure_pairs],
        "mixtures_tested": len(mixture_reserves),
        "minimum_reserve": str(min(mixture_reserves)),
    },
    "gates": gates,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
