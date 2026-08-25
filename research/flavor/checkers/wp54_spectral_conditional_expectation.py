#!/usr/bin/env python3
"""WP54: exact descent and fitted-domain falsifier for spectral pinching."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/flavor/results/wp54_spectral_conditional_expectation.json"


def dagger(a: sp.Matrix) -> sp.Matrix:
    return a.conjugate().T


def pinching(projectors: list[sp.Matrix], x: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sum((p * x * p for p in projectors), sp.zeros(x.rows)))


def hs_norm2(x: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(dagger(x) * x))


def main() -> None:
    hu = sp.diag(1, 4, 9)
    projectors = [sp.diag(1, 0, 0), sp.diag(0, 1, 0), sp.diag(0, 0, 1)]
    hd = sp.Matrix([[2, 1 + sp.I, 0], [1 - sp.I, 5, 2], [0, 2, 7]])
    q = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                   [-sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    transformed_projectors = [q * p * dagger(q) for p in projectors]

    e_hd = pinching(projectors, hd)
    covariance_residual = sp.simplify(
        pinching(transformed_projectors, q * hd * dagger(q)) - q * e_hd * dagger(q)
    )
    idempotence_residual = sp.simplify(pinching(projectors, e_hd) - e_hd)
    unital_residual = sp.simplify(pinching(projectors, sp.eye(3)) - sp.eye(3))
    fixed_commutator = sp.simplify(hu * e_hd - e_hd * hu)
    discarded = sp.simplify(hd - e_hd)

    # Exact two-generation mixing witness: nonzero mixing is erased by pinching.
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    v = sp.Matrix([[c, s, 0], [-s, c, 0], [0, 0, 1]])
    down_eigenvalues = sp.diag(1, 4, 16)
    hd_mixed = sp.simplify(v * down_eigenvalues * dagger(v))
    hd_pinched = pinching(projectors, hd_mixed)
    commutator_before = sp.simplify(hu * hd_mixed - hd_mixed * hu)
    commutator_after = sp.simplify(hu * hd_pinched - hd_pinched * hu)

    gates = {
        "conditional_expectation_is_full_weak_basis_covariant": covariance_residual == sp.zeros(3),
        "conditional_expectation_is_idempotent": idempotence_residual == sp.zeros(3),
        "conditional_expectation_is_unital": unital_residual == sp.zeros(3),
        "image_is_proper_commutant_subspace": fixed_commutator == sp.zeros(3) and discarded != sp.zeros(3),
        "discarded_hilbert_schmidt_norm_is_positive": bool(hs_norm2(discarded) > 0),
        "nonzero_mixing_is_exact_fixed_locus_falsifier": commutator_before != sp.zeros(3) and commutator_after == sp.zeros(3),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.flavor.spectral-conditional-expectation.v1",
        "arithmetic": "exact SymPy rational and Gaussian-rational matrix algebra",
        "domain": "nondegenerate Hermitian Yukawa Gram pairs (H_u,H_d)",
        "quotient": "simultaneous conjugation by full U(3)_Q; right-handed basis already removed by Gram formation",
        "operation": "E_u(H_d) = sum_i P_i^u H_d P_i^u",
        "descent": "yes: E_{QH_uQ^dag}(QH_dQ^dag) = Q E_{H_u}(H_d) Q^dag",
        "proper_image": "the commutant of H_u (diagonal down Gram in the up spectral frame)",
        "contextual_partition": {
            "before": "generic physical16 points with mixing",
            "fixed_locus": "commuting H_u,H_d; generically permutation/phase CKM with J=0",
        },
        "classification": {
            "mathematical_selector": True,
            "physical_selector": False,
            "rigidifier": False,
            "reason_physical_selector_fails": "the source defines the spectral data but no flavor dynamics or instrument applies the pinching; its fixed locus also excludes observed nonzero mixing",
            "physical_instrument": "none admitted for the projection; CKM measurements instrument its failure",
        },
        "smallest_exact_falsifier": "one nonzero off-diagonal matrix element of H_d in the H_u eigenbasis (equivalently a nontrivial CKM mixing modulus); CP violation J != 0 is a stronger experimental falsifier",
        "gates": gates,
        "conclusion": "A canonical positive conditional expectation descends and has a proper image, but it is not an admissible physical flavor selector and its fixed locus is empirically false.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": sum(gates.values()), "total": len(gates), "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
