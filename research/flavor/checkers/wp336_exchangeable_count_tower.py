"""WP336: exact binomial-zeta faithfulness of the exchangeable count tower."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def zeta_matrix(size):
    return sp.Matrix([
        [sp.binomial(k, j) if k >= j else 0 for k in range(size + 1)]
        for j in range(size + 1)
    ])


def mobius_matrix(size):
    return sp.Matrix([
        [(-1) ** (j - k) * sp.binomial(j, k) if j >= k else 0 for j in range(size + 1)]
        for k in range(size + 1)
    ])


def main():
    size = 6
    zeta = zeta_matrix(size)
    mobius = mobius_matrix(size)
    identity = sp.eye(size + 1)
    q = sp.Matrix(sp.symbols("q0:7"))
    moments = zeta * q
    reconstructed = sp.simplify(mobius * moments)
    labelled_left = {(1, 0, 0): sp.Integer(1)}
    labelled_right = {(0, 1, 0): sp.Integer(1)}
    count_law_left = [sum(weight for word, weight in labelled_left.items() if sum(word) == k) for k in range(4)]
    count_law_right = [sum(weight for word, weight in labelled_right.items() if sum(word) == k) for k in range(4)]
    checks = {
        "binomial_zeta_matrix_is_unimodular": zeta.det() == 1,
        "declared_mobius_matrix_is_exact_inverse": mobius * zeta == identity and zeta * mobius == identity,
        "complete_factorial_tower_reconstructs_count_law": reconstructed == q,
        "zeroth_moment_is_normalization": moments[0] == sum(q),
        "highest_moment_is_top_count_probability": moments[size] == q[size],
        "hostile_labelled_laws_are_distinct": labelled_left != labelled_right,
        "hostile_labelled_laws_have_identical_count_law": count_law_left == count_law_right,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP336",
        "admitted_state_domain": "exchangeable N=6 binary CP-domain indicators represented by their count law q_0 through q_6",
        "faithful_quotient_coordinate": "the complete exchangeable count distribution, not a labelled spatial joint law",
        "candidate_probe_family": "factorial-count moments m_j=E[binomial(K,j)] for j=0 through 6",
        "source_authorization": "conditional only; physical executability of the complete tower and exchangeability of the admitted domain remain unproved",
        "zeta_matrix": [[int(value) for value in row] for row in zeta.tolist()],
        "mobius_matrix": [[int(value) for value in row] for row in mobius.tolist()],
        "determinant": int(zeta.det()),
        "forward_transform": [str(value) for value in moments],
        "inverse_rule": "q_k=sum_{j>=k} (-1)^(j-k) binomial(j,k) m_j",
        "contextual_partition": "the complete tower has singleton fibers on exchangeable count laws; labelled laws remain grouped by their common count distribution",
        "classification": "jointly faithful on the finite exchangeable count packet, but neither faithful to labelled spatial routes nor a selector of the domain probability",
        "smallest_exact_falsifier": "the labelled laws concentrated on 100 and 010 have identical complete count towers but are distinct spatial source stories",
        "remaining_physical_instrument_gate": "derive executable coincidence measurements through order six with efficiency and correlation calibration, and justify exchangeability or add source-derived labelled ports",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp336_exchangeable_count_tower.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
