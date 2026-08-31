"""Protocol gate for the reopened rank-26 p-normal relation-module test.

Repeat iteration 5 re-reads the mutable frontier: the minimal tau_p source routes
are exhausted, but Nima's rank-26 prior-art audit opens a different source-derived
algorithm.  This checker verifies that the rank-26 route is genuinely distinct
from the failed local tau_p routes and records the exact admissible protocol.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_rank26_p_normal_protocol_gate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dot(a: list[int], b: list[int]) -> int:
    return sum(x * y for x, y in zip(a, b))


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


def main() -> None:
    c_mismatch = load(VOEVODSKY_RESULTS / "cosmology_c_kernel_p_normal_mismatch.json")
    trichotomy = load(VOEVODSKY_RESULTS / "cosmology_tau_source_domain_trichotomy.json")
    rank26 = load(NIMA_RESULTS / "cosmology_p_normal_rank26_relation_bockstein_prior_art.json")
    frontier = load(NIMA_RESULTS / "cosmology_current_activation_frontier_exhaustion.json")
    source = load(NIMA_RESULTS / "cosmology_source_principal_wall_cell.json")

    assert c_mismatch["passed"] is True
    assert trichotomy["passed"] is True
    assert rank26["passed"] is True
    assert frontier["passed"] is True
    assert source["passed"] is True

    p_covector = source["induced_base_first_jet"]
    nx = rank26["integral_unit_normals"]["nx"]
    ny = rank26["integral_unit_normals"]["ny"]
    tangent = rank26["integral_unit_normals"]["difference_tangent_to_p"]
    point = rank26["generic_p_normal_test_point"]["xyz"]
    assert p_covector == [1, 1, 3]
    assert dot(p_covector, nx) == 1
    assert dot(p_covector, ny) == 1
    assert dot(p_covector, tangent) == 0
    assert dot(p_covector, point) == 0
    assert sum(point) == rank26["generic_p_normal_test_point"]["total_energy"] == 6

    normal_matrix = [nx, ny, tangent]
    witnesses = {}
    for prime in (101, 103):
        normal_rank = rank_mod_prime(normal_matrix, prime)
        p_and_tangent_rank = rank_mod_prime([p_covector, tangent], prime)
        assert normal_rank == 2
        assert p_and_tangent_rank == 2
        witnesses[str(prime)] = {
            "rank_of_nx_ny_tangent": normal_rank,
            "rank_of_p_covector_and_tangent": p_and_tangent_rank,
            "dp_nx": dot(p_covector, nx) % prime,
            "dp_ny": dot(p_covector, ny) % prime,
            "dp_tangent": dot(p_covector, tangent) % prime,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-protocol-gate.v1",
        "status": "minimal_tau_routes_exhausted_rank26_relation_module_protocol_open",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_c_kernel_p_normal_mismatch.json",
            "research/voevodsky/results/cosmology_tau_source_domain_trichotomy.json",
            "research/nima/results/cosmology_p_normal_rank26_relation_bockstein_prior_art.json",
            "research/nima/results/cosmology_current_activation_frontier_exhaustion.json",
            "research/nima/results/cosmology_source_principal_wall_cell.json",
        ],
        "minimal_tau_route_status": "exhausted at source-derived unit map to tau_p",
        "rank26_route_status": "open source-derived algorithm, not a transferable class",
        "p_normal_covector": p_covector,
        "test_point_xyz": point,
        "integral_unit_normals": {"nx": nx, "ny": ny, "p_tangent_difference": tangent},
        "normal_checks": {
            "dp(nx)": dot(p_covector, nx),
            "dp(ny)": dot(p_covector, ny),
            "dp(nx-ny)": dot(p_covector, tangent),
            "p(test_point)": dot(p_covector, point),
            "total_energy_at_test_point": sum(point),
        },
        "finite_field_witnesses": witnesses,
        "admissible_protocol": rank26["proposed_test"],
        "hard_restrictions": rank26["typing_restrictions"] + [
            "do not use the c pivot as the p-normal; c and p covectors have rank two",
            "do not treat the abstract tau_p classifier as source data",
            "do not use residue equality to invert the residue functor",
        ],
        "success_criterion": "a surviving full-rank26 p-normal derivative line maps to the formal horn as primitive column (1,1) up to sign, with normal-choice independence modulo the p-tangent derived-relation span",
        "current_computation_status": "protocol verified; full labelled rank-26 relation derivative matrix not computed in this Voevodsky locus",
        "next_nonrepeat_task": "obtain or construct the full labelled rank-26 relation matrix and implement the nx/ny derivative-reduction protocol over two primes",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
