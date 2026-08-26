import json
from pathlib import Path

from sympy import Matrix, Rational


def positive_diagonal(matrix: Matrix) -> bool:
    return matrix.is_diagonal() and all(value > 0 for value in matrix.diagonal())


checks = {}

# Observability witness and deliberate hostile.
A_obs = Matrix([[0, 1], [-2, -3]])
C_obs = Matrix([[1, 0]])
O_obs = C_obs.col_join(C_obs * A_obs)
checks["observability_witness_rank_two"] = O_obs.rank() == 2

A_hidden = Matrix.diag(1, 2)
O_hidden = C_obs.col_join(C_obs * A_hidden)
hidden = Matrix([0, 1])
checks["observability_hostile_rank_one"] = O_hidden.rank() == 1
checks["observability_hostile_nonzero_kernel"] = hidden != Matrix.zeros(2, 1) and O_hidden * hidden == Matrix.zeros(2, 1)

# Ordered feedback witness and singular direct-feedthrough hostile.
A = Matrix([[0]])
B = C = F = Matrix([[0]])
B = Matrix([[1]])
C = Matrix([[1]])
G = H = Matrix([[1]])
K = Matrix([[0]])
closed_loop = (A + B * K * C).row_join(B * H).col_join((G * C).row_join(F))
checks["feedback_witness_exact_block"] = closed_loop == Matrix([[0, 1], [1, 0]])

D_bad = Matrix([[1]])
K_bad = Matrix([[1]])
solve_operator = Matrix.eye(1) - K_bad * D_bad
hostile_rhs = Matrix([[1]])
checks["feedback_hostile_singular_loop"] = solve_operator.det() == 0
checks["feedback_hostile_inconsistent_signal"] = solve_operator.rank() < solve_operator.row_join(hostile_rhs).rank()

# Strict storage witness and semidefinite hostile.
A_stable = Matrix.diag(Rational(1, 2), Rational(1, 3))
P = Matrix.eye(2)
Q = P - A_stable.T * P * A_stable
checks["stability_witness_exact_lyapunov_identity"] = A_stable.T * P * A_stable - P == -Q
checks["stability_witness_strict_dissipation"] = positive_diagonal(P) and positive_diagonal(Q)

A_marginal = Matrix.diag(1, Rational(1, 2))
Q_marginal = P - A_marginal.T * P * A_marginal
marginal_mode = Matrix([1, 0])
checks["stability_hostile_semidefinite_not_strict"] = Q_marginal.det() == 0 and Q_marginal != Matrix.zeros(2)
checks["stability_hostile_persistent_mode"] = A_marginal * marginal_mode == marginal_mode and (marginal_mode.T * Q_marginal * marginal_mode)[0] == 0

result = {
    "schema": "marici.sontag.control-factorization-milestone.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "arithmetic": "exact_sympy_rationals",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "residuals": {
        "observability_hostile_kernel_vector": [str(value) for value in hidden],
        "feedback_hostile_solve_operator": [[str(value) for value in row] for row in solve_operator.tolist()],
        "feedback_hostile_rhs": [[str(value) for value in row] for row in hostile_rhs.tolist()],
        "stability_hostile_Q": [[str(v) for v in row] for row in Q_marginal.tolist()],
    },
    "scope": "finite-dimensional discrete-time linear systems only",
}

output = Path(__file__).resolve().parents[1] / "results" / "control_factorization_milestone.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "passed" else 1)
