#!/usr/bin/env python3
"""Exact finite classification of primitive/square boundary incidence laws."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "kitaev" / "results" / "valuation-boundary-incidence-laws.json"


def rank_rows(*rows: sp.Matrix) -> int:
    return sp.Matrix.vstack(*rows).rank()


def main() -> None:
    # Exact surrogate weights lp,lq=2,3 retain only algebraic independence of
    # the two labelled logarithmic weights; they are not numerical log values.
    lp, lq = sp.Integer(2), sp.Integer(3)
    labels = ["p", "p^2", "q", "pq"]
    Lambda = sp.Matrix([[lp, lp, lq, 0]])
    P = sp.Matrix([[lp, 0, lq, 0]])
    Q = sp.Matrix([[0, lp, 0, 0]])
    endpoint_sum = sp.Matrix([[1], [1]])
    incidence = sp.Matrix.vstack(P, Q)
    assert endpoint_sum.T * incidence == Lambda
    assert P[0, 3] == Q[0, 3] == 0
    assert rank_rows(P, Q) == 2

    # Partial Adams law psi^2(p)=p^2 exchanges the designated primitive input
    # with its square channel. Total Adams closure fails because q^2 is absent.
    psi2_partial = {"p": "p^2"}
    missing_total_images = {"q": "q^2", "p^2": "p^4", "pq": "p^2q^2"}
    assert all(image not in labels for image in missing_total_images.values())

    # Infinite endpoint-preserving attachment family in B=Q^3. The endpoint
    # reads the first coordinate; t is an invisible boundary shear.
    t = sp.symbols("t", real=True)
    bP = sp.Matrix([1, 0, t])
    bQ = sp.Matrix([1, 1, 0])
    endpoint = sp.Matrix([[1, 0, 0]])
    assert endpoint * bP == endpoint * bQ == sp.ones(1, 1)
    assert sp.Matrix.hstack(bP, bQ).rank() == 2
    assert bP.subs(t, 0) != bP.subs(t, 1)

    # Kernel formula for an extended Gramian. With only the three observation
    # rows (analytic scalar, P, Q), the four-label model retains one kernel.
    analytic = sp.Matrix([[1, 1, 1, 1]])
    Qpartial = analytic.T * analytic
    Qextended = Qpartial + P.T * P + Q.T * Q
    assert Qextended.rank() == 3
    kernel = Qextended.nullspace()[0]
    assert Qextended * kernel == sp.zeros(4, 1)
    assert P * kernel == Q * kernel == analytic * kernel == sp.zeros(1, 1)

    # Hostile 1: identified primitive/square rows lose channel distinction.
    Q_same = P
    assert rank_rows(P, Q_same) == 1

    # Hostile 2: type-erased log(n) gives p^2 twice the p weight, contradicting
    # Lambda(p^2)=Lambda(p).
    erased = sp.Matrix([[lp, 2 * lp, lq, lp + lq]])
    assert erased[0, 1] != Lambda[0, 1]

    # Hostile 3: forbidden primitive flux on pq.
    P_bad_pq = sp.Matrix([[lp, 0, lq, 1]])
    assert P_bad_pq[0, 3] != 0

    # Hostile 4: invertible at every cutoff but lower bound collapses.
    collapsing = []
    for n in range(1, 9):
        Qn = sp.diag(1, 1, 1, sp.Rational(1, n * n))
        assert Qn.rank() == 4
        collapsing.append({"cutoff": n, "lambda_min": str(sp.Rational(1, n*n))})

    # Hostile 5: a moving coordinate constructor C_N is never replaced by one
    # fixed finite family.
    moving = [{"cutoff": n, "required_constructor": f"C_{n}"} for n in range(1, 7)]

    # Hostile 6: analytically bounded identity incidence, wrong Adams square.
    boundary_psi2 = sp.Matrix([[0, 1], [1, 0]])
    i_p = sp.Matrix([1, 0])
    i_p2_bad = sp.Matrix([1, 0])
    assert i_p2_bad != boundary_psi2 * i_p

    # Hostile 7: endpoint scalar is fixed while an invisible boundary component
    # reverses under sheet action.
    Rb = sp.diag(1, -1)
    b = sp.Matrix([1, 1])
    assert sp.Matrix([[1, 0]]) * b == sp.Matrix([[1, 0]]) * Rb * b
    assert Rb * b != b

    result = {
        "schema": "marici.kitaev.valuation-boundary-incidence-laws.v1",
        "finite_module": {
            "basis": labels,
            "formal_log_weights": {"log_p": 2, "log_q": 3},
            "Lambda_row": [2, 2, 3, 0],
            "primitive_row": [2, 0, 3, 0],
            "square_row": [0, 2, 0, 0],
            "endpoint_sum_recovers_Lambda": True,
            "pq_primitive_flux": 0,
        },
        "adams_closure": {
            "partial_defined_image": psi2_partial,
            "missing_total_images": missing_total_images,
            "four_label_module_closed_under_all_Adams_operations": False,
            "literal_total_Adams_requirement": "finite incompatibility",
        },
        "classification": {
            "with_partial_Adams_only": "infinite endpoint-preserving attachment family",
            "parameter": "b_P(t)=(1,0,t) in a boundary kernel direction",
            "unique_up_to_authorized_equivalence": False,
            "finite_torsor_forced": False,
            "reason": "endpoint values and channel rank do not remove continuous shears in ker(endpoint); no authorized boundary equivalence was frozen",
        },
        "extended_gram_audit": {
            "Q_partial": "analytic all-ones rank-one fixture",
            "Q_extended_rank": 3,
            "state_dimension": 4,
            "kernel_witness": [str(x) for x in kernel],
            "finite_injectivity": False,
            "interpretation": "incidence laws alone do not force ker Q_extended=0; analytic K_X or further authorized rows must supply the last direction",
        },
        "hostile_cases": {
            "P_equals_Q": {"first_failed_law": "primitive_square_channel_separation", "joint_rank": 1},
            "type_erased_log_n": {"first_failed_law": "prime_power_typing", "p2_value": 4, "required": 2},
            "primitive_flux_on_pq": {"first_failed_law": "absence_of_primitive_pq", "value": 1},
            "cutoff_rescaling": {"first_failed_law": "uniform_continuity", "samples": collapsing, "limit": 0},
            "moving_constructor_family": {"first_failed_law": "fixed_finite_family", "samples": moving},
            "continuous_wrong_Adams": {"first_failed_law": "Adams_composition", "analytically_bounded": True},
            "scalar_preserving_sheet_reversal": {"first_failed_law": "sheet_character", "Lambda_preserved": True},
        },
        "machine_obstruction": {
            "code": "valuation_boundary_incidence_law_failed",
            "candidate": "four-label-total-Adams",
            "first_failed_law": "Adams_closure",
            "witness_input": "e_q",
            "required_output": "e_q^2",
            "output_in_declared_module": False,
            "repair_requires_source_enlargement": True,
        },
        "minimal_laws_for_future_source_map": [
            "freeze an Adams-stable valuation domain or explicitly partial Adams category",
            "recover Lambda weights while assigning zero primitive pq flux",
            "separate primitive and square boundary channels",
            "intertwine the frozen sheet characters",
            "commute with cutoff inclusions",
            "match endpoint incidence",
            "close every constructor-Gram kernel with one fixed finite authorized family",
            "have cutoff-uniform domination constants",
        ],
        "verdict": "On the literal four-label module, compatibility with all Adams operations is finitely inconsistent because the module is not Adams-stable. Restricting to the partial Adams arrow p->p^2 makes incidence possible but not unique: endpoint and typing laws leave an infinite family of boundary-kernel shears. Therefore Grothendieck must first freeze an Adams-stable source domain and an authorized boundary equivalence/reference before a unique map or finite torsor can be claimed.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
