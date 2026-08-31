"""Formal lifting-problem package for the cosmology tau_p obstruction.

This checker replaces route-by-route residue probing with a small typed problem:
a chain-complex horn whose universal filler is tau_p.  Existing candidates are
tested by their signatures against that universal property.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path
from functools import reduce

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_tau_lift_formal_problem.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
    for col in range(col_count):
        pivot = next((r for r in range(rank, row_count) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(row_count):
            if r == rank:
                continue
            factor = rows[r][col] % prime
            if factor:
                rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def primitive(vector: list[int]) -> bool:
    return reduce(gcd, (abs(v) for v in vector)) == 1


def main() -> None:
    trichotomy = load(VOEVODSKY_RESULTS / "cosmology_tau_source_domain_trichotomy.json")
    nonfaithful = load(VOEVODSKY_RESULTS / "cosmology_residue_functor_nonfaithfulness_gate.json")
    universal = load(VOEVODSKY_RESULTS / "cosmology_universal_total_lift_cell.json")
    prior = load(NIMA_RESULTS / "cosmology_tau_lift_prior_art_audit.json")
    pivot = load(NIMA_RESULTS / "cosmology_tau_gradient_pivot_type_gate.json")

    assert trichotomy["passed"] is True
    assert nonfaithful["passed"] is True
    assert universal["passed"] is True
    assert prior["passed"] is True
    assert pivot["passed"] is True

    d_residue = universal["residue_differential_rows_pair_faces_cols_Xi_minusSigma"]
    tau = universal["primitive_kernel_generator"]
    assert d_residue == [[1, -1], [-1, 1], [1, -1]]
    assert tau == [1, 1]
    assert mat_vec(d_residue, tau) == [0, 0, 0]
    assert primitive(tau)

    # Formal horn: degree 1 filler -> degree 2 pair -> degree 3 residues.
    horn = {
        "degree_1_required_filler": "tau_p_source",
        "degree_2_pair_basis": ["Xi_log", "minus_sigma123"],
        "degree_3_residue_basis": ["q1q2", "q1q3", "q2q3"],
        "d2_rows_degree3_cols_degree2": d_residue,
        "required_d1_column": tau,
        "d2_d1_zero": mat_vec(d_residue, tau) == [0, 0, 0],
        "primitive_integral_filler": primitive(tau),
    }

    candidates = {
        "abstract_tau_p": {
            "column": [1, 1],
            "sourced": False,
            "chain_condition": True,
            "reason_not_admissible": "classifier only; no source map",
        },
        "ordered_blowup_exceptional_face": {
            "column": [0, 1],
            "sourced": True,
            "chain_condition": mat_vec(d_residue, [0, 1]) == [0, 0, 0],
            "reason_not_admissible": "misses Xi_log unit leg",
        },
        "residue_monic_comparison": {
            "column": [1, 1],
            "sourced": False,
            "chain_condition": True,
            "reason_not_admissible": "exists only after residue; residue functor has kernel rank one",
        },
        "gradient_pivot_normal_adapter": {
            "column": None,
            "sourced": True,
            "chain_condition": False,
            "reason_not_admissible": "fixed-fiber restriction leaves no sigma123 triple face",
        },
    }

    assert candidates["ordered_blowup_exceptional_face"]["chain_condition"] is False
    assert pivot["restricted_cover"]["triple_face_count"] == 0
    assert prior["tau_p_source_map_constructed"] is False

    witnesses = {}
    for prime in (101, 103):
        d_rank = rank_mod_prime(d_residue, prime)
        tau_rank = rank_mod_prime([[tau[0]], [tau[1]]], prime)
        exceptional_augmented_rank = rank_mod_prime([[0, 1], [1, 1]], prime)
        assert (d_rank, tau_rank, exceptional_augmented_rank) == (1, 1, 2)
        witnesses[str(prime)] = {
            "residue_differential_rank": d_rank,
            "tau_column_rank": tau_rank,
            "exceptional_column_plus_tau_rank": exceptional_augmented_rank,
            "formal_horn_has_universal_filler": True,
            "current_sourced_candidate_fills_horn": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-tau-lift-formal-problem.v1",
        "status": "formal_lifting_problem_defined_no_sourced_filler",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_tau_source_domain_trichotomy.json",
            "research/voevodsky/results/cosmology_residue_functor_nonfaithfulness_gate.json",
            "research/voevodsky/results/cosmology_universal_total_lift_cell.json",
            "research/nima/results/cosmology_tau_lift_prior_art_audit.json",
            "research/nima/results/cosmology_tau_gradient_pivot_type_gate.json",
        ],
        "formal_horn": horn,
        "candidate_signatures": candidates,
        "finite_field_witnesses": witnesses,
        "theorem": "A source route advances the p-normal line iff it supplies a sourced degree-one filler whose differential is the primitive column (1,1) in (Xi_log,minus_sigma123). The abstract tau_p and residue comparison satisfy the formal column but are unsourced; the blow-up exceptional face is sourced but has column (0,1); the gradient-pivot prior art is sourced but lacks the required triple face on the fixed fiber.",
        "next_task": "construct a new source object with a map into this formal horn; the checker for any proposed object is now only its differential column, source provenance, and d^2 compatibility",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
