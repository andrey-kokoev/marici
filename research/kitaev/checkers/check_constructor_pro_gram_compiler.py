#!/usr/bin/env python3
"""Exact rational compiler for current continuity in constructor pro-Gram topologies."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "kitaev" / "results" / "constructor-pro-gram-compiler.json"


def kernel_contained(Q: sp.Matrix, H: sp.Matrix) -> bool:
    return all(H * v == sp.zeros(H.rows, 1) for v in Q.nullspace())


def sharp_abs_constant(Q: sp.Matrix, H: sp.Matrix) -> sp.Expr | None:
    """Sharp |x*Hx| <= C x*Qx for symmetric rational matrices."""
    if not kernel_contained(Q, H):
        return None
    vals = (Q.pinv() * H).eigenvals().keys()
    return max((abs(sp.simplify(v)) for v in vals), default=sp.Integer(0))


def aggregate(constructor_Q: dict[str, sp.Matrix], subset: tuple[str, ...], dim: int) -> sp.Matrix:
    total = sp.zeros(dim)
    for name in subset:
        total += constructor_Q[name]
    return total


def json_matrix(matrix: sp.Matrix) -> list[list[int | str]]:
    return [[int(x) if x.is_Integer else str(x) for x in row] for row in matrix.tolist()]


def minimal_subsets(constructor_Q: dict[str, sp.Matrix], H: sp.Matrix) -> list[dict[str, object]]:
    names = list(constructor_Q)
    dim = H.rows
    for size in range(len(names) + 1):
        found = []
        for subset in itertools.combinations(names, size):
            Q = aggregate(constructor_Q, subset, dim)
            constant = sharp_abs_constant(Q, H)
            if constant is not None:
                found.append({"subset": list(subset), "sharp_constant": str(constant), "Q_rank": Q.rank()})
        if found:
            return found
    return []


def main() -> None:
    # Synthetic authorized finite registry, K=I and Q_C=D_C^T D_C.
    e1, e2, e3 = [sp.eye(3).row(i) for i in range(3)]
    constructor_Q = {
        "tail_coordinate": sp.diag(1, 0, 0),
        "square_coordinate": sp.diag(0, 1, 0),
        "seam_coordinate": sp.diag(0, 0, 1),
    }
    targets = {
        "primitive": e1.T * e1,
        "square": e2.T * e2,
        "seam": e3.T * e3,
        "archimedean": (e1 + e2).T * (e1 + e2),
        "green": sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        "defect": sp.diag(1, -1, 0),
    }
    compiled = {name: minimal_subsets(constructor_Q, H) for name, H in targets.items()}
    assert compiled["primitive"][0]["subset"] == ["tail_coordinate"]
    assert compiled["square"][0]["subset"] == ["square_coordinate"]
    assert compiled["seam"][0]["subset"] == ["seam_coordinate"]
    assert len(compiled["archimedean"][0]["subset"]) == 2
    assert len(compiled["green"][0]["subset"]) == 2
    assert len(compiled["defect"][0]["subset"]) == 2

    # Mandatory hostile fixtures.
    Q_kernel = sp.diag(1, 0)
    L_hidden = sp.Matrix([[0, 1]])
    H_hidden = L_hidden.T * L_hidden
    v_hidden = sp.Matrix([0, 1])
    assert Q_kernel * v_hidden == sp.zeros(2, 1)
    assert L_hidden * v_hidden == sp.ones(1, 1)
    assert sharp_abs_constant(Q_kernel, H_hidden) is None

    divergent = []
    for n in range(1, 9):
        Qn = sp.diag(1, sp.Rational(1, n * n))
        cn = sharp_abs_constant(Qn, H_hidden)
        assert cn == n * n  # M_N^2; hence M_N=N.
        divergent.append({"cutoff": n, "M_N_squared": str(cn), "M_N": str(n), "lambda_min_Q": str(sp.Rational(1, n*n))})

    # No fixed finite F: at cutoff N the target observes coordinate N, while
    # constructor C_j observes only coordinate j. C_N works cutoffwise, but
    # every fixed finite subset misses all later target coordinates.
    moving_witnesses = []
    for n in range(1, 7):
        Qn = sp.zeros(n)
        Qn[n - 1, n - 1] = 1  # constructor C_N
        Ln = sp.zeros(1, n)
        Ln[0, n - 1] = 1
        assert sharp_abs_constant(Qn, Ln.T * Ln) == 1
        moving_witnesses.append({"cutoff": n, "controlling_constructor": f"C_{n}", "constant": 1})

    # Scalar cancellation hides nonzero typed residual matrices.
    Bp = sp.diag(1, -1)
    Bs = -Bp
    assert Bp + Bs == sp.zeros(2)
    assert Bp != sp.zeros(2) and Bs != sp.zeros(2)

    # Unauthorized repair.
    Q_admitted = sp.diag(1, 0)
    Q_unauthorized = sp.diag(0, 1)
    assert sharp_abs_constant(Q_admitted, H_hidden) is None
    assert sharp_abs_constant(Q_admitted + Q_unauthorized, H_hidden) == 1

    # Mixed-sheet block certificate with a controlled and a kernel-failing case.
    Qleft = sp.diag(1, 0)
    Qright = sp.diag(1, 0)
    Bgood = sp.Matrix([[1, 0], [0, 0]])
    Bbad = sp.Matrix([[0, 1], [0, 0]])
    Qblock = sp.diag(Qleft, Qright)
    Hgood = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(2), Bgood), sp.Matrix.hstack(Bgood.T, sp.zeros(2)))
    Hbad = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(2), Bbad), sp.Matrix.hstack(Bbad.T, sp.zeros(2)))
    assert sharp_abs_constant(Qblock, Hgood) == 1
    assert sharp_abs_constant(Qblock, Hbad) is None

    result = {
        "schema": "marici.kitaev.constructor-pro-gram-compiler.v1",
        "compiler": {
            "linear_kernel_gate": "ker Q_F,N subset ker L_N",
            "linear_sharp_M_squared": "lambda_max(Q_F,N^dagger/2 L_N^*L_N Q_F,N^dagger/2)",
            "quadratic_gate": "-C Q_F,N <= B_N <= C Q_F,N",
            "mixed_gate": "apply quadratic gate to [[0,B],[B*,0]] against diag(Q_left,Q_right)",
            "extension": "one fixed finite authorized F and one cutoff-independent constant",
        },
        "synthetic_authorized_registry": {
            "warning": "compiler fixture only; not theta/Tate source data",
            "minimal_controls": compiled,
        },
        "hostile_fixtures": {
            "kernel_failure": {"Q": [[1, 0], [0, 0]], "L": [[0, 1]], "witness": [0, 1]},
            "divergent_constants": {"Q_N": "diag(1,1/N^2)", "L": [[0, 1]], "samples": divergent, "sup_M_N_finite": False},
            "rank_complete_nonuniform": {"Q_N_rank": 2, "lambda_min": "1/N^2 -> 0"},
            "no_fixed_finite_F": {"target": "coordinate N at cutoff N", "cutoffwise_controls": moving_witnesses, "fixed_finite_subset_exists": False},
            "scalar_cancellation": {"B_primitive": [[1, 0], [0, -1]], "B_square": [[-1, 0], [0, 1]], "sum": [[0, 0], [0, 0]], "typed_matrices_individually_zero": False},
            "unauthorized_repair": {"admitted_Q": [[1, 0], [0, 0]], "unauthorized_Q": [[0, 0], [0, 1]], "repair_constant": 1, "authorized": False},
            "mixed_kernel_failure": {"controlled_B": json_matrix(Bgood), "uncontrolled_B": json_matrix(Bbad), "controlled_constant": 1},
        },
        "machine_rejection": {
            "code": "current_not_continuous_in_constructor_completion",
            "current": "primitive",
            "cutoff": "kernel-fixture",
            "constructor_subset": ["admitted_coordinate_1"],
            "kernel_witness": [0, 1],
            "sharp_domination_constant": None,
            "uniform_bound_failed": True,
            "unauthorized_constructor_required": True,
        },
        "distinctions": {
            "continuity": "target form is uniformly dominated by a fixed finite authorized constructor Gramian",
            "faithfulness": "selected observations separate admissible states",
            "uniform_observability": "observation energy has a cutoff-independent lower bound on state norm",
        },
        "source_authority_boundary": {
            "optimized_over": "frozen authorized constructor list only",
            "theta_matrices_supplied": False,
            "required": ["K_N", "D_C,N", "L_k1,N", "L_k2,N", "L_seam,N", "L_infinity,N", "B_Green,N", "defect residual matrices"],
        },
        "verdict": "A current extends to the constructor pro-Gram completion exactly when one fixed finite authorized constructor subset closes every kernel and supplies a cutoff-uniform domination constant. Rank, cutoffwise choice of moving constructors, scalar cancellation, and repair by an unauthorized row are each insufficient.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
