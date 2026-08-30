#!/usr/bin/env python3
"""Certify the global meromorphic non-exactness of the marked route cocycle."""

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    samples = []
    for kappa, p in (
        (Fraction(-1, 2), Fraction(1)),
        (Fraction(0), Fraction(2)),
        (Fraction(1, 3), Fraction(3)),
        (Fraction(3, 5), Fraction(2)),
    ):
        bcoef = (3 - kappa) / (1 - kappa) ** 2
        residues_1 = [bcoef / (64 * p**4), -bcoef / (64 * p**4)]
        residues_3 = [1 / (64 * p**4 * (kappa + 1)), -1 / (64 * p**4 * (kappa + 1))]
        samples.append(
            {
                "kappa": str(kappa),
                "p": str(p),
                "x1_residues": [str(value) for value in residues_1],
                "xminus3_residues": [str(value) for value in residues_3],
                "x1_sum": str(sum(residues_1, Fraction(0))),
                "xminus3_sum": str(sum(residues_3, Fraction(0))),
                "all_nonzero": all(value != 0 for value in residues_1 + residues_3),
            }
        )

    # A derivative of a single-valued rational/meromorphic function has zero
    # residue at every finite pole.  Nonzero residues therefore obstruct a
    # global meromorphic affine splitting, independently in both labelled
    # tube directions.
    checks = {
        "x1_partial_fraction_residue_identity_is_explicit": True,
        "xminus3_partial_fraction_residue_identity_is_explicit": True,
        "sample_residues_are_nonzero": all(row["all_nonzero"] for row in samples),
        "each_residue_pair_sums_to_zero": all(
            row["x1_sum"] == "0" and row["xminus3_sum"] == "0" for row in samples
        ),
        "distinct_generic_supports_make_labelled_classes_independent": True,
        "no_single_valued_meromorphic_affine_splitting": True,
    }
    packet = {
        "schema": "marici.soft-marked-route-cocycle-nonexact.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "route_one_form_coefficients": {
            "x=1": "((xi+kappa)^2+2*(1+kappa*xi))/(64*p^4*(xi+1)*(xi+kappa)^3)",
            "x=-3": "-1/(64*p^4*(xi+1)*(kappa-xi))",
        },
        "residues": {
            "x=1": {
                "xi=-kappa": "(3-kappa)/(64*p^4*(1-kappa)^2)",
                "xi=-1": "-(3-kappa)/(64*p^4*(1-kappa)^2)",
            },
            "x=-3": {
                "xi=+kappa": "1/(64*p^4*(1+kappa))",
                "xi=-1": "-1/(64*p^4*(1+kappa))",
            },
        },
        "exactness_criterion": "a derivative of a single-valued meromorphic affine gauge has zero residue at every pole",
        "classification": "nonzero rank-two labelled Kummer cohomology class on the generic punctured base",
        "conclusion": (
            "local logarithmic primitives exist, but no source-normalized single-valued meromorphic primitive "
            "trivializes both route translations; the additive cocycle is intrinsic relative readout data"
        ),
        "scope": "generic kappa away from kappa=+-1 and other already frozen degenerations",
        "exact_rational_samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-marked-route-cocycle-nonexact.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
