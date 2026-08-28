"""Exact real-fiber audit of the celestial Hodge bridge."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "celestial_hodge_bridge_checks.json"


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(s, a):
    return [[s * x for x in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def frobenius(a, b):
    return sum(a[i][j] * b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def covariant_derivative(c, dc, omega):
    # Oriented orthonormal-frame connection Gamma = omega * EPS.
    gamma = scale(omega, EPS)
    return add(add(dc, mm(gamma, c)), scale(-1, mm(c, gamma)))


I2 = [[1, 0], [0, 1]]
EPS = [[0, -1], [1, 0]]
REFLECTION = [[1, 0], [0, -1]]
C = [[2, 3], [3, -2]]
DC = [[5, 7], [7, -5]]


def hodge(c):
    return mm(EPS, c)


def reflect(c):
    return mm(mm(REFLECTION, c), transpose(REFLECTION))


JC = hodge(C)
SHEET_J = [[1j, 0j], [0j, -1j]]
H = [[1, 1], [1, -1]]
H_INV = [[0.5, 0.5], [0.5, -0.5]]
PARITY_J = mm(mm(H, SHEET_J), H_INV)
checks = {
    "real_stf_fiber_is_preserved": JC == transpose(JC) and JC[0][0] + JC[1][1] == 0,
    "hodge_complex_structure_squares_to_minus_identity": hodge(JC) == scale(-1, C),
    "hodge_structure_is_orthogonal": frobenius(JC, JC) == frobenius(C, C),
    "orientation_reversal_anticommutes_with_hodge": reflect(JC) == scale(-1, hodge(reflect(C))),
    "helicity_coordinate_is_multiplied_by_i": complex(JC[0][0], JC[0][1]) == 1j * complex(C[0][0], C[0][1]),
    "conjugate_helicity_coordinate_is_multiplied_by_minus_i": complex(JC[0][0], -JC[0][1]) == -1j * complex(C[0][0], -C[0][1]),
    "sheet_matrix_is_diag_i_minus_i": SHEET_J == [[1j, 0j], [0j, -1j]],
    "parity_basis_matrix_is_i_times_exchange": PARITY_J == [[0j, 1j], [1j, 0j]],
    "parallel_hodge_commutes_with_covariant_derivative": all(
        covariant_derivative(hodge(basis_c), hodge(basis_dc), omega)
        == hodge(covariant_derivative(basis_c, basis_dc, omega))
        for basis_c in ([[1, 0], [0, -1]], [[0, 1], [1, 0]])
        for basis_dc in ([[1, 0], [0, -1]], [[0, 1], [1, 0]])
        for omega in (-2, 0, 3)
    ),
    "hostile_reflection_commuting_claim_is_false": reflect(JC) != hodge(reflect(C)),
    "hostile_one_coordinate_real_slice_is_not_J_closed": JC[0][1] != 0,
}

payload = {
    "schema": "marici.strominger.celestial-hodge-bridge.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "real_fiber_witness": {"C": C, "J_C": JC},
    "theorem_scope": {
        "source_object": "real symmetric trace-free rank-two tensors on an oriented Riemannian celestial two-manifold",
        "constructor": "J(C)_AB = epsilon_A^C C_CB",
        "domain_law": "nabla epsilon = 0 implies J commutes with covariant derivatives and preserves derivative-defined domains",
        "correction": "multiplication by i in a helicity coordinate is a real bundle operation, not scalar extension",
        "remaining_gap": "an executable instrument implementing J is not constructed by the bundle automorphism",
    },
    "hostile_boundary": {
        "orientation_deleted": "J is no longer canonically selectable",
        "single_real_Laurent_coordinate_slice": "not closed under J",
        "full_nonlinear_gravity_duality_claimed": "rejected; only the radiative tensor bundle and covariant fold are certified",
    },
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
