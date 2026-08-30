#!/usr/bin/env python3
"""Finite local boundary-counterterm quotient for the mixed readout."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-mixed-readout-counterterms.json"


def determinant(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def main() -> None:
    # Reduced physical readout coordinates are (P, S=Q+N).
    field = (Fraction(0), Fraction(2))
    mixed = (Fraction(-4), Fraction(0))
    base_det = determinant(field, mixed)
    assert base_det == 8

    # A general local Dirichlet counterterm has kernel F(k^2) and shifts
    # Pi -> Pi + F zeta. At fixed k this sends mixed -> mixed+lambda*field.
    # Test several hostile rational values; invariance is the alternating
    # identity field wedge (mixed+lambda field)=field wedge mixed.
    for lam in [Fraction(-17, 5), Fraction(0), Fraction(9, 7), Fraction(101)]:
        shifted = (mixed[0] + lam * field[0], mixed[1] + lam * field[1])
        assert determinant(field, shifted) == base_det

    packet = {
        "schema": "marici.de_sitter_mixed_readout_counterterms.v1",
        "admissible_counterterm": (
            "S_ct=1/2 integral zeta F(-nabla^2) zeta on the regulated future boundary, "
            "with F a real local derivative polynomial/series"
        ),
        "canonical_shift": "Pi_ren -> Pi_ren + F(-nabla^2) zeta",
        "readout_rows_in_basis_P_S": {
            "field": ["0", "2"],
            "mixed_finite": ["-4", "0"],
            "counterterm_shifted_mixed": ["-4", "2 lambda"],
        },
        "invariant": {
            "wedge_determinant": "8",
            "identity": "field wedge (mixed+lambda field)=field wedge mixed",
            "quotient_class": "[mixed] in Readout/Span(field) is nonzero and counterterm-independent",
        },
        "excluded_without_extra_source": [
            "counterterms depending on canonical momentum rather than the fixed Dirichlet boundary field",
            "state-dependent future counterterms fitted to cancel Re(C)",
            "nonlocal kernels with poles or branch support",
        ],
        "conclusion": (
            "The absolute mixed finite representative is scheme-dependent by addition of the field row, "
            "but its quotient class and rank-two separation are invariant under all admitted local "
            "quadratic Dirichlet counterterms."
        ),
        "classification": "scheme-independent readout quotient; unchanged carrier",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"wedge_determinant": str(base_det), "counterterm_tests": 4}))


if __name__ == "__main__":
    main()
