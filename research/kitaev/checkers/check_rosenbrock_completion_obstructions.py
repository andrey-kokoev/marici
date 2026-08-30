#!/usr/bin/env python3
"""Exact Rosenbrock distinctions and completion-hostile fixtures."""

import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, Symbol, diag, eye, factor, limit, oo, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/rosenbrock-completion-obstructions.json"
s = Symbol("s")


def transfer(A, B, C):
    return factor((C * (s * eye(A.rows) - A).inv() * B)[0])


def rosenbrock(A, B, C):
    n = A.rows
    return (s * eye(n) - A).row_join(-B).col_join(C.row_join(Matrix([[0]])))


def main():
    # Minimal finite realization with a genuine transfer/invariant zero.
    A = diag(0, 1)
    B = Matrix([1, 1])
    C = Matrix([[1, 1]])
    F = transfer(A, B, C)
    R = rosenbrock(A, B, C)
    assert F == (2 * s - 1) / (s * (s - 1))
    assert simplify(F.subs(s, Rational(1, 2))) == 0
    assert R.subs(s, Rational(1, 2)).rank() == 2
    zero_state = R.subs(s, Rational(1, 2)).nullspace()[0]
    assert zero_state != Matrix.zeros(3, 1)
    assert R.subs(s, Rational(1, 2)) * zero_state == Matrix.zeros(3, 1)

    # Same transfer, different hidden state object.
    A_hidden = diag(0, 2)
    B_hidden = Matrix([1, 0])
    C_hidden = Matrix([[1, 0]])
    assert transfer(Matrix([[0]]), Matrix([1]), Matrix([[1]])) == transfer(A_hidden, B_hidden, C_hidden) == 1 / s
    pbh_observe = (2 * eye(2) - A_hidden).col_join(C_hidden)
    pbh_control = (2 * eye(2) - A_hidden).row_join(B_hidden)
    assert pbh_observe.rank() == 1
    assert pbh_control.rank() == 1

    # Pointwise-minimal family with collapsing constants.
    collapse = []
    for N in (2, 3, 5, 10):
        eps = Rational(1, N)
        BN = Matrix([1, eps])
        CN = Matrix([[1, eps]])
        controllability = BN.row_join(A * BN)
        observability = CN.col_join(CN * A)
        assert controllability.det() == eps
        assert observability.det() == eps
        weak_reachability = (Matrix([[0, 1]]) * controllability * controllability.T * Matrix([0, 1]))[0]
        weak_observability = (Matrix([[0, 1]]) * observability.T * observability * Matrix([0, 1]))[0]
        assert weak_reachability == weak_observability == 2 * eps**2
        FN = transfer(A, BN, CN)
        assert simplify(FN - (1 / s + eps**2 / (s - 1))) == 0
        zero = Rational(1, 1) / (1 + eps**2)
        assert simplify(FN.subs(s, zero)) == 0
        collapse.append({
            "N": N,
            "det_controllability": str(controllability.det()),
            "det_observability": str(observability.det()),
            "weak_mode_energy": str(weak_observability),
            "transfer_zero": str(zero),
        })
    Nsym = Symbol("N", positive=True)
    eps = 1 / Nsym
    assert limit(2 * eps**2, Nsym, oo) == Rational(0)

    # Pointwise nonzero at zero, limiting zero at zero.
    created = []
    for N in (2, 3, 5, 10):
        eps = Rational(1, N)
        A_create = diag(-1, -2)
        B_create = Matrix([1, 1])
        C_create = Matrix([[eps - 1, 2 - eps]])
        F_create = transfer(A_create, B_create, C_create)
        assert simplify(F_create - (s + eps) / ((s + 1) * (s + 2))) == 0
        assert F_create.subs(s, 0) != 0
        assert B_create.row_join(A_create * B_create).det() != 0
        assert C_create.col_join(C_create * A_create).det() != 0
        created.append({"N": N, "zero": str(-eps), "value_at_zero": str(F_create.subs(s, 0))})

    # Persistent zero lost when a pole enters the point; convergence is only punctured.
    lost = []
    for N in (2, 3, 5, 10):
        eps = Rational(1, N)
        A_lost = diag(-eps, -1)
        B_lost = Matrix([1, 1])
        C_lost = Matrix([[-1 / (N - 1), Rational(N, N - 1)]])
        F_lost = transfer(A_lost, B_lost, C_lost)
        assert simplify(F_lost - s / ((s + eps) * (s + 1))) == 0
        assert simplify(F_lost.subs(s, 0)) == 0
        lost.append({"N": N, "zero": "0", "approaching_pole": str(-eps)})

    # Exact terminal-amplitude shear cocycle.
    Fab, Fbc = Symbol("F_ab"), Symbol("F_bc")
    Sab = Matrix([[1, Fab], [0, 1]])
    Sbc = Matrix([[1, Fbc], [0, 1]])
    Sac = Matrix([[1, Fab + Fbc], [0, 1]])
    assert Sab * Sbc == Sac

    payload = {
        "schema": "marici.kitaev.rosenbrock_completion_obstructions.v1",
        "status": "pass",
        "strength": "finite-cutoff theorem and hostile families",
        "minimal_transfer_zero": {
            "transfer": str(F), "zero": "1/2",
            "rosenbrock_rank_at_zero": R.subs(s, Rational(1, 2)).rank(),
            "zero_dynamics_witness": [str(v) for v in zero_state],
        },
        "same_transfer_hidden_mode": {
            "transfer": "1/s", "hidden_eigenvalue": 2,
            "observability_pbh_rank": pbh_observe.rank(),
            "controllability_pbh_rank": pbh_control.rank(),
        },
        "minimality_collapse_family": collapse,
        "limit_weak_mode_energy": "0",
        "pointwise_new_zero_family": created,
        "punctured_limit_lost_zero_family": lost,
        "terminal_shear_cocycle": "pass",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "adelic completion", "uniform graph control", "passivity",
            "conservativity", "KYP positivity", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
