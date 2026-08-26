"""Exact WP452 census of source coefficient representations."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp451 = json.loads((root / "results" / "wp451_triplet_symmetry_selector_obstruction.json").read_text(encoding="utf-8"))
I = sp.I
identity = sp.eye(3)
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]

def anti(left, right):
    return (left*right+right*left)/2


Q = [
    J[0]**2-sp.Rational(2, 3)*identity,
    J[1]**2-sp.Rational(2, 3)*identity,
    anti(J[0], J[1]),
    anti(J[0], J[2]),
    anti(J[1], J[2]),
]
singlet = [identity]
vector = J
full_basis = singlet+vector+Q
vectorized = sp.Matrix.hstack(*[matrix.reshape(9, 1) for matrix in full_basis])

# Hilbert-Schmidt block orthogonality.
singlet_vector_gram = sp.Matrix([[sp.trace(a.conjugate().T*b) for b in vector] for a in singlet])
singlet_quintet_gram = sp.Matrix([[sp.trace(a.conjugate().T*b) for b in Q] for a in singlet])
vector_quintet_gram = sp.Matrix([[sp.trace(a.conjugate().T*b) for b in Q] for a in vector])

# A triplet-only order parameter has the spin-one characteristic polynomial.
n1, n2, n3, x = sp.symbols("n1 n2 n3 x", real=True)
triplet_matrix = n1*J[0]+n2*J[1]+n3*J[2]
characteristic_polynomial = triplet_matrix.charpoly(x)
characteristic = sp.factor(characteristic_polynomial.as_expr())

# After an SO(3) rotation, two real triplet vectors lie in the x-z plane;
# both corresponding matrices are real and admit real eigenframes.
a, b, c = sp.symbols("a b c", real=True)
up_plane = a*J[2]
down_plane = b*J[0]+c*J[2]

checks = {
    "wp451_dependency_passed": wp451["passed"],
    "singlet_rank_is_one": sp.Matrix.hstack(*[m.reshape(9, 1) for m in singlet]).rank() == 1,
    "vector_rank_is_three": sp.Matrix.hstack(*[m.reshape(9, 1) for m in vector]).rank() == 3,
    "quadrupole_rank_is_five": sp.Matrix.hstack(*[m.reshape(9, 1) for m in Q]).rank() == 5,
    "one_plus_three_plus_five_spans_End_C3": vectorized.rank() == 9,
    "irreducible_blocks_are_pairwise_orthogonal": singlet_vector_gram == sp.zeros(1, 3) and singlet_quintet_gram == sp.zeros(1, 5) and vector_quintet_gram == sp.zeros(3, 5),
    "triplet_only_characteristic_is_equally_spaced": characteristic_polynomial.all_coeffs() == [1, 0, -(n1**2+n2**2+n3**2), 0],
    "two_triplet_order_parameters_have_real_plane_representatives": all(entry.is_real is not False for entry in up_plane) and all(entry.is_real is not False for entry in down_plane),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP452",
    "decomposition": "End(C^3)=1 direct-sum 3 direct-sum 5 under the WP447 source SO(3)",
    "dimensions": {"singlet": 1, "vector": 3, "quadrupole": 5, "total": 9},
    "triplet_only_characteristic": str(characteristic),
    "triplet_only_limit": "Equally spaced eigenvalues and CP-real relative frames; insufficient for observed generic flavor.",
    "minimal_dynamic_coefficient_content": "For each generic complex Yukawa: a complex singlet, complex triplet, and complex symmetric-traceless quintet, or a source mechanism imposing a smaller predictive subfamily.",
    "selector_classification": "Representation census only; it types the minimal carrier fields but selects no vacuum values.",
    "instrument": None,
    "smallest_exact_falsifier": "Failure of the 1+3+5 basis to have rank nine, or a generic triplet-only matrix with non-equally-spaced eigenvalues.",
    "remaining_gate": "Freeze a positive source action for the coefficient triplet/quintet and preregister which invariants may select their relative magnitudes, orientation, and complex phase.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp452_coefficient_representation_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
