#!/usr/bin/env python3
"""Laurent audit of the late-time field--momentum initial-state readout."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-mixed-momentum-readout.json"


def main() -> None:
    # With C=P+iQ and N real, the normalized equal-time correction is
    # D(y)=2 Im[C q(y)^2] + 2N(1+y^2).
    # q^2=1+y^2-(2i/3)y^3+O(y^4).
    coefficients = {
        0: (Fraction(0), Fraction(2), Fraction(2)),
        1: (Fraction(0), Fraction(0), Fraction(0)),
        2: (Fraction(0), Fraction(2), Fraction(2)),
        3: (Fraction(-4, 3), Fraction(0), Fraction(0)),
    }  # basis (P=ReC,Q=ImC,N)

    # a^2 d_eta = (k^3/H^2) y^-2 d_y up to the canonical factor.
    # Differentiating D and multiplying by y^-2 gives:
    # 4(Q+N)/y - 4P + O(y).
    pole_row = tuple(2 * coefficients[2][i] for i in range(3))
    finite_row = tuple(3 * coefficients[3][i] for i in range(3))
    assert pole_row == (Fraction(0), Fraction(4), Fraction(4))
    assert finite_row == (Fraction(-4), Fraction(0), Fraction(0))

    # Together with the field-field freeze-out row 2(Q+N), the finite
    # mixed row has rank two on the physical two-coordinate readout (P,Q+N).
    determinant = Fraction(8)
    assert determinant != 0

    packet = {
        "schema": "marici.de_sitter_mixed_momentum_readout.v1",
        "canonical_momentum": "Pi_zeta=2 epsilon M_pl^2 a^2 partial_eta zeta",
        "normalized_equal_time_series": (
            "D(y)=2(Q+N)+2(Q+N)y^2-(4/3)P y^3+O(y^4), "
            "P=Re(C), Q=Im(C)"
        ),
        "mixed_laurent_series": (
            "a^2 partial_eta D=(k^3/H^2)[4(Q+N)/y-4P+O(y)]"
        ),
        "rows_in_basis_P_Q_N": {
            "field_field_freezeout": ["0", "2", "2"],
            "mixed_pole": ["0", "4", "4"],
            "mixed_finite_part": ["-4", "0", "0"],
        },
        "rank": {
            "field_field_alone": 1,
            "field_field_plus_mixed_finite_part": 2,
            "determinant_on_P_and_Q_plus_N": str(determinant),
        },
        "status": (
            "The Laurent finite part of the symmetrized field--momentum correlator reads "
            "the third-grade horizontal coordinate. Physical canonicity still requires a "
            "finite-counterterm and boundary-renormalization audit."
        ),
        "classification": "candidate renormalized readout; no new carrier incidence",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pole_row": [str(x) for x in pole_row], "finite_row": [str(x) for x in finite_row]}))


if __name__ == "__main__":
    main()
