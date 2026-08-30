"""Exact C3 connector row-Gram quartic census for WP497."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp483 = load("wp483_connector_frame_architecture.json")
wp493 = load("wp493_radial_quartic_rg_closure.json")

cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
representation = sp.diag(cycle, cycle)

# q=(d0,d1,d2,o0,o1,o2), where d are diagonal row-Gram entries and
# o=(R01,R12,R20). Both triples cycle under the declared row action.
q = sp.Matrix(sp.symbols("d0:3 o0:3", real=True))
d = q[:3, :]
o = q[3:, :]

orbit_polynomials = [
    sp.expand(sum(d[i] ** 2 for i in range(3))),
    sp.expand(sum(d[i] * d[(i + 1) % 3] for i in range(3))),
    sp.expand(sum(o[i] ** 2 for i in range(3))),
    sp.expand(sum(o[i] * o[(i + 1) % 3] for i in range(3))),
    sp.expand(sum(d[i] * o[i] for i in range(3))),
    sp.expand(sum(d[i] * o[(i + 1) % 3] for i in range(3))),
    sp.expand(sum(d[i] * o[(i - 1) % 3] for i in range(3))),
]
orbit_names = ["D2", "DD", "O2", "OO", "DO0", "DOplus", "DOminus"]
orbit_matrices = [sp.hessian(polynomial, q) / 2 for polynomial in orbit_polynomials]

# Solve the full invariant symmetric-form space independently.
m_symbols = sp.symbols("m0:21", real=True)
M = sp.zeros(6)
cursor = 0
for i in range(6):
    for j in range(i, 6):
        M[i, j] = M[j, i] = m_symbols[cursor]
        cursor += 1
invariance_equations = list(representation.T * M * representation - M)
invariance_matrix, _ = sp.linear_eq_to_matrix(invariance_equations, m_symbols)
invariant_dimension = len(m_symbols) - invariance_matrix.rank()


def flatten_symmetric(matrix):
    return [matrix[i, j] for i in range(6) for j in range(i, 6)]


orbit_rank = sp.Matrix([flatten_symmetric(matrix) for matrix in orbit_matrices]).rank()
frame_matrix = orbit_matrices[0] + 2 * orbit_matrices[2]
radial_matrix = orbit_matrices[0] + 2 * orbit_matrices[1]
current_rank = sp.Matrix([flatten_symmetric(frame_matrix), flatten_symmetric(radial_matrix)]).rank()
combined_rank = sp.Matrix(
    [flatten_symmetric(frame_matrix), flatten_symmetric(radial_matrix)]
    + [flatten_symmetric(matrix) for matrix in orbit_matrices]
).rank()

r = sp.symbols("r", positive=True)
isotropic = {q[0]: r, q[1]: r, q[2]: r, q[3]: 0, q[4]: 0, q[5]: 0}
isotropic_values = [sp.factor(polynomial.subs(isotropic)) for polynomial in orbit_polynomials]

checks = {
    "wp483_dependency_passed": wp483["passed"],
    "wp493_dependency_passed": wp493["passed"],
    "full_cyclic_invariant_dimension_is_seven": invariant_dimension == 7,
    "seven_orbit_forms_are_each_invariant": all(
        representation.T * matrix * representation == matrix for matrix in orbit_matrices
    ),
    "seven_orbit_forms_are_independent": orbit_rank == 7,
    "current_frame_and_radial_basis_has_rank_two": current_rank == 2,
    "current_plus_orbit_basis_spans_full_space": combined_rank == 7,
    "missing_cyclic_quartic_codimension_is_five": invariant_dimension - current_rank == 5,
    "isotropic_values_are_exact": isotropic_values == [3 * r**2, 3 * r**2, 0, 0, 0, 0, 0],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP497",
    "domain": "quartics quadratic in the symmetric connector row Gram R=SS^T, invariant under the declared cyclic row action",
    "invariant_space_dimension": int(invariant_dimension),
    "explicit_orbit_basis": {
        name: str(polynomial) for name, polynomial in zip(orbit_names, orbit_polynomials)
    },
    "current_basis": {
        "frame_Frobenius": "D2+2 O2",
        "radial_square": "D2+2 DD",
        "rank": int(current_rank),
        "missing_codimension": int(invariant_dimension - current_rank),
    },
    "isotropic_vacuum_values": {
        name: str(value) for name, value in zip(orbit_names, isotropic_values)
    },
    "authority": "C3 permits all seven coordinates. The existing enhanced frame form occupies only a rank-two subspace; setting the other five to zero requires extra symmetry or boundary data.",
    "classification": "Exact cyclic-row quartic census; the current connector potential is not symmetry-complete and cannot yet define an RG-closed scalar truncation.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "The C3-invariant symmetric quadratic-form space on the six row-Gram entries has dimension seven, while the frame-plus-radial action spans only rank two.",
    "remaining_gate": "Choose an independently justified enhanced row symmetry or promote all seven cyclic invariants to running couplings, then combine them with WP493-WP496 and recompute the full vacuum Hessian.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp497_cyclic_row_quartic_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
