"""Exact Cayley-Hamilton completion of the adjoint quartic census for WP496."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp447 = load("wp447_irreducible_adjoint_triplet.json")
wp495 = load("wp495_adjoint_gram_rg_closure.json")

a = sp.symbols("a0:8", real=True)
b = sp.symbols("b0:8", real=True)
A = sp.Matrix([[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], -a[0] - a[4]]])
B = sp.Matrix([[b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], -b[0] - b[4]]])

polarized_identity = sp.expand(
    4 * sp.trace(A**2 * B**2)
    + 2 * sp.trace(A * B * A * B)
    - sp.trace(A**2) * sp.trace(B**2)
    - 2 * sp.trace(A * B) ** 2
)

I_rad, I_gram, I_comm = sp.symbols("I_rad I_gram I_comm")
C_reduced = sp.factor((I_rad + 2 * I_gram + 2 * I_comm) / 6)
D_reduced = sp.factor((I_rad + 2 * I_gram - 4 * I_comm) / 6)

mu = sp.symbols("mu", positive=True)
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -sp.I, 0], [sp.I, 0, -sp.I], [0, sp.I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
X = [mu * matrix for matrix in J]
gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.trace(X[i] * X[j])))
vacuum_radial = sp.factor(sp.trace(gram) ** 2)
vacuum_gram = sp.factor(sp.trace(gram * gram))
vacuum_comm = sp.factor(
    sum(
        sp.trace(
            (X[i] * X[j] - X[j] * X[i]).conjugate().T
            * (X[i] * X[j] - X[j] * X[i])
        )
        for i in range(3)
        for j in range(i + 1, 3)
    )
)
vacuum_c = sp.factor(sum(sp.trace(X[i] ** 2 * X[j] ** 2) for i in range(3) for j in range(3)))
vacuum_d = sp.factor(sum(sp.trace(X[i] * X[j] * X[i] * X[j]) for i in range(3) for j in range(3)))
vacuum_substitution = {I_rad: vacuum_radial, I_gram: vacuum_gram, I_comm: vacuum_comm}

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "wp495_dependency_passed": wp495["passed"],
    "generic_traceless_matrices_are_traceless": sp.trace(A) == 0 and sp.trace(B) == 0,
    "polarized_cayley_hamilton_identity_is_exact": polarized_identity == 0,
    "C_minus_D_reconstructs_commutator_basis": sp.simplify(C_reduced - D_reduced - I_comm) == 0,
    "four_C_plus_two_D_reconstructs_double_traces": sp.simplify(4 * C_reduced + 2 * D_reduced - I_rad - 2 * I_gram) == 0,
    "spin_one_C_matches_reduction": sp.simplify(vacuum_c - C_reduced.subs(vacuum_substitution)) == 0,
    "spin_one_D_matches_reduction": sp.simplify(vacuum_d - D_reduced.subs(vacuum_substitution)) == 0,
    "spin_one_commutator_is_six": vacuum_comm == 6 * mu**4,
    "three_invariant_basis_has_full_reduction_rank": sp.Matrix([[1, -1], [4, 2]]).rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP496",
    "domain": "parity-even quartics of three traceless 3x3 adjoints with SO(3)_P indices contracted by Kronecker deltas",
    "polarized_identity": "4 Tr(A^2 B^2)+2 Tr(ABAB)=Tr(A^2)Tr(B^2)+2 Tr(AB)^2",
    "basis": {
        "I_rad": "(Tr G_X)^2",
        "I_gram": "Tr(G_X^2)",
        "I_comm": "sum_{i<j} ||[X_i,X_j]||_F^2",
    },
    "single_trace_reduction": {
        "C=sum_ij Tr(X_i^2 X_j^2)": str(C_reduced),
        "D=sum_ij Tr(X_i X_j X_i X_j)": str(D_reduced),
    },
    "spin_one_vacuum": {
        "I_rad": str(vacuum_radial),
        "I_gram": str(vacuum_gram),
        "I_comm": str(vacuum_comm),
        "C": str(vacuum_c),
        "D": str(vacuum_d),
    },
    "classification": "After WP495 adds I_gram, the delta-contracted parity-even pure-adjoint quartic sector is algebraically closed; no further single-trace coordinate is independent.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "The polarized Cayley-Hamilton identity reduces both apparent single-trace words uniquely to I_rad, I_gram, and I_comm.",
    "remaining_gate": "Complete the cyclic-row connector invariant census and mixed tensor portals, then form the full scalar Hessian with independent running coefficients.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp496_adjoint_quartic_cayley_hamilton.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
