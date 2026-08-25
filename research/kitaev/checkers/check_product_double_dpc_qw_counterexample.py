#!/usr/bin/env python3
"""Exact tensor-product counterexample to DPC-QW in D(S4 x D4)."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "product-double-dpc-qw-counterexample.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply_histograms(left: dict[str, int], right: dict[str, int], modulus: int) -> dict[str, int]:
    result = Counter()
    for a, count_a in left.items():
        for b, count_b in right.items():
            result[str((int(a) * int(b)) % modulus)] += count_a * count_b
    return dict(sorted(result.items(), key=lambda item: int(item[0])))


def main() -> None:
    s4_path = K / "results" / "s4-quantum-double-dpc-qw.json"
    d4_path = K / "results" / "d4-quantum-double-dimension-magic-conjecture.json"
    s4 = json.loads(s4_path.read_text(encoding="utf-8"))
    d4 = json.loads(d4_path.read_text(encoding="utf-8"))
    s4_spectra = s4["representative_spectrum_per_dimension"]
    d4_spectra = d4["representative_nonvacuum_spectrum_per_dimension"]

    # In Z(C[G x H]) = Z(C[G]) box-times Z(C[H]), simples are pairs,
    # dimensions multiply, and Wilson/fusion eigenvalues multiply pointwise.
    left = multiply_histograms(s4_spectra["3"], d4_spectra["2"], 4)
    right = multiply_histograms(s4_spectra["6"], d4_spectra["1"], 4)
    assert 3 * 2 == 6 * 1 == 6
    assert sum(left.values()) == sum(right.values()) == 21 * 22
    assert left == {"0": 282, "2": 180}
    assert right == {"0": 242, "2": 220}
    assert left != right

    result = {
        "schema": "marici.kitaev.product-double-dpc-qw-counterexample.v1",
        "inputs": {
            str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
            for path in (s4_path, d4_path)
        },
        "group": "S4 x D4",
        "quantum_double_factorization": "D(S4 x D4) equivalent to D(S4) box-times D(D4)",
        "sector_count": 21 * 22,
        "left_constructor": {"factor_dimensions": [3, 2], "total_dimension": 6,
                             "mod4_spectrum": left},
        "right_constructor": {"factor_dimensions": [6, 1], "total_dimension": 6,
                              "mod4_spectrum": right},
        "both_nonvacuum": True,
        "both_typed_real_integral": True,
        "equal_dimension": True,
        "equal_quarter_spectrum": False,
        "dpc_qw_status": "falsified",
        "replacement": "quarter spectrum depends on the multiplicative construction of the full Wilson character row, not quantum dimension alone; direct-product factorization is retained by tensor convolution even when dimensions coincide",
        "verdict": "D(S4 x D4) is an exact typed nonvacuum counterexample to DPC-QW. A dimension-6 sector constructed as 3x2 has mod-4 spectrum {0:282,2:180}, while one constructed as 6x1 has {0:242,2:220}. Quantum dimension alone therefore does not explain Wilson magic species.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
