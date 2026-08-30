"""Exact full electroweak-doublet entrance Hessian attempt for WP506."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp505 = load("wp505_complex_entrance_kernel_closure.json")

a, b = sp.symbols("a b", positive=True)
couplings = sp.symbols(
    "lambda_u lambda_d kappa alpha_u alpha_d eta rho sigma_u sigma_d",
    positive=True,
)
lambda_u, lambda_d, kappa, alpha_u, alpha_d, eta, rho, sigma_u, sigma_d = couplings
variables = sp.symbols("Ur0:6 Ui0:6 Dr0:6 Di0:6", real=True)
Ur = sp.Matrix(3, 2, variables[0:6])
Ui = sp.Matrix(3, 2, variables[6:12])
Dr = sp.Matrix(3, 2, variables[12:18])
Di = sp.Matrix(3, 2, variables[18:24])
I = sp.I
U = Ur + I * Ui
D = Dr + I * Di


def inner(left, right):
    return (sp.conjugate(left).T * right)[0]


def epsilon(left, right):
    return sp.expand(left[0] * right[1] - left[1] * right[0])


def real_part(value):
    return sp.expand(sp.re(sp.expand_complex(value)))


def imaginary_part(value):
    return sp.expand(sp.im(sp.expand_complex(value)))


def absolute_square(value):
    return sp.expand(real_part(value) ** 2 + imaginary_part(value) ** 2)


norm_u = sp.expand(sum(real_part(inner(U.row(row).T, U.row(row).T)) for row in range(3)))
norm_d = sp.expand(sum(real_part(inner(D.row(row).T, D.row(row).T)) for row in range(3)))
trace_overlap = sp.expand(sum(inner(U.row(row).T, D.row(row).T) for row in range(3)))

row_imaginary_u = sum(
    imaginary_part(inner(U.row(i).T, U.row(j).T)) ** 2
    for i in range(3) for j in range(3)
)
row_imaginary_d = sum(
    imaginary_part(inner(D.row(i).T, D.row(j).T)) ** 2
    for i in range(3) for j in range(3)
)
cross_square_sum = sum(
    inner(U.row(i).T, D.row(j).T) ** 2
    for i in range(3) for j in range(3)
)
phase_gap = sp.expand(norm_u * norm_d - real_part(cross_square_sum))
weak_cross_alignment = sum(
    absolute_square(epsilon(U.row(i).T, D.row(j).T))
    for i in range(3) for j in range(3)
)
phase_gap_squares = sum(
    2 * imaginary_part(inner(U.row(i).T, D.row(j).T)) ** 2
    + absolute_square(epsilon(U.row(i).T, D.row(j).T))
    for i in range(3) for j in range(3)
)
weak_u_alignment = sum(
    absolute_square(epsilon(U.row(i).T, U.row(j).T))
    for i in range(3) for j in range(3)
)
weak_d_alignment = sum(
    absolute_square(epsilon(D.row(i).T, D.row(j).T))
    for i in range(3) for j in range(3)
)

potential = sp.expand(
    lambda_u * (norm_u - a**2) ** 2
    + lambda_d * (norm_d - b**2) ** 2
    + kappa * absolute_square(trace_overlap)
    + alpha_u * row_imaginary_u
    + alpha_d * row_imaginary_d
    + eta * phase_gap
    + rho * weak_cross_alignment
    + sigma_u * weak_u_alignment
    + sigma_d * weak_d_alignment
)

# Rows are (e1,e2,e3), weak components are (charged,neutral).
vacuum_U = sp.zeros(3, 2)
vacuum_D = sp.zeros(3, 2)
vacuum_U[2, 1] = a
vacuum_D[0, 1] = b
vacuum_vector = sp.Matrix(list(vacuum_U) + [0] * 6 + list(vacuum_D) + [0] * 6)
vacuum = {variable: vacuum_vector[index] for index, variable in enumerate(variables)}

vacuum_energy = sp.simplify(potential.subs(vacuum))
gradient = sp.Matrix([sp.diff(potential, variable) for variable in variables])
vacuum_gradient = sp.simplify(gradient.subs(vacuum))
hessian = sp.simplify(sp.hessian(potential, variables).subs(vacuum))


def flatten_variation(real_u, imaginary_u, real_d, imaginary_d):
    return sp.Matrix(list(real_u) + list(imaginary_u) + list(real_d) + list(imaginary_d))


L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
zero_u = sp.zeros(3, 2)
row_tangents = [
    flatten_variation(generator * vacuum_U, zero_u, generator * vacuum_D, zero_u)
    for generator in L
]

pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.diag(1, -1),
]
electroweak_tangents = []
for generator in pauli:
    delta_u = I * vacuum_U * generator.T / 2
    delta_d = I * vacuum_D * generator.T / 2
    electroweak_tangents.append(
        flatten_variation(sp.re(delta_u), sp.im(delta_u), sp.re(delta_d), sp.im(delta_d))
    )
hypercharge_delta_u = I * vacuum_U / 2
hypercharge_delta_d = I * vacuum_D / 2
hypercharge_tangent = flatten_variation(
    sp.re(hypercharge_delta_u),
    sp.im(hypercharge_delta_u),
    sp.re(hypercharge_delta_d),
    sp.im(hypercharge_delta_d),
)
gauge_tangents = sp.Matrix.hstack(*(row_tangents + electroweak_tangents + [hypercharge_tangent]))
kernel = sp.Matrix.hstack(*hessian.nullspace())
gauge_hessian_response = (hessian * gauge_tangents).applyfunc(sp.simplify)

checks = {
    "wp505_dependency_passed": wp505["passed"],
    "full_doublet_vacuum_has_zero_energy": vacuum_energy == 0,
    "full_doublet_vacuum_is_stationary": vacuum_gradient == sp.zeros(24, 1),
    "phase_gap_is_zero_at_vacuum": sp.simplify(phase_gap.subs(vacuum)) == 0,
    "phase_gap_has_exact_sum_of_squares_decomposition": sp.expand(phase_gap - phase_gap_squares) == 0,
    "full_hessian_rank_is_eighteen": hessian.rank() == 18,
    "full_hessian_nullity_is_six": len(hessian.nullspace()) == 6,
    "broken_row_and_electroweak_gauge_orbit_rank_is_six": gauge_tangents.rank() == 6,
    "all_broken_gauge_tangents_are_hessian_zeros": gauge_hessian_response == sp.zeros(24, 7),
    "broken_gauge_tangents_span_full_hessian_kernel": kernel.row_join(gauge_tangents).rank() == 6,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP506",
    "domain": "two complete complex SU(2)_L doublet row triplets with hypercharge one-half and gauged SO(3)_E",
    "positive_source_terms": [
        "two radial norm squares",
        "Hermitian row-trace orthogonality norm",
        "two imaginary row-Gram Frobenius norms",
        "Cauchy phase gap N_u N_d-Re sum[(U_alpha^dagger D_beta)^2]",
        "cross and self weak-antisymmetric alignment norms",
    ],
    "vacuum": "U_3=(0,a), D_1=(0,b), all other doublets zero",
    "full_hessian": {
        "real_dimension": 24,
        "rank": int(hessian.rank()),
        "nullity": len(hessian.nullspace()),
        "broken_gauge_orbit_dimension": int(gauge_tangents.rank()),
        "physical_kernel_dimension": int(len(hessian.nullspace()) - gauge_tangents.rank()),
    },
    "classification": "Exact manifestly electroweak- and row-gauge-invariant positive entrance-sector vacuum whose full scalar Hessian kernel equals the broken gauge orbit; spectrum rigidifier, not a numerical selector.",
    "selector": False,
    "rigidifier": bool(len(hessian.nullspace()) == gauge_tangents.rank()),
    "instrument": None,
    "smallest_exact_falsifier": "The full 24-real-dimensional Hessian kernel must equal the six-dimensional broken SO(3)_E and electroweak gauge orbit.",
    "remaining_gate": "Combine this entrance Hessian with connector, flavor-adjoint, Higgs-clock, and gauge sectors; compute the complete mixed poles and source-normalized residues, then derive every open width and detector response without fitting a,b or their ratio.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp506_full_doublet_hessian_attempt.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
