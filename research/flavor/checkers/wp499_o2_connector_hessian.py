"""Exact complete O(2)-connector isotropic Hessian for WP499."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp484 = load("wp484_gauged_connector_frame_lift.json")
wp498 = load("wp498_entrance_stabilizer_quartic_obstruction.json")

s = sp.symbols("s", positive=True)
r = s**2
u, v = sp.symbols("u v", real=True)
l1, l2, l3, l4, l5 = sp.symbols("lambda_1:6", real=True)

entries = sp.symbols("S0:9", real=True)
S = sp.Matrix(3, 3, entries)
R = S * S.T
a = R[0, 0]
b = R[1, 1]
c = R[2, 2]
d = R[0, 1]
e = R[0, 2]
f = R[1, 2]
t = b + c

potential = sp.expand(
    u * a
    + v * t
    + l1 * a**2
    + l2 * a * t
    + l3 * t**2
    + l4 * (d**2 + e**2)
    + l5 * ((b - c) ** 2 + 4 * f**2)
)

vacuum = {
    entries[0]: s, entries[1]: 0, entries[2]: 0,
    entries[3]: 0, entries[4]: s, entries[5]: 0,
    entries[6]: 0, entries[7]: 0, entries[8]: s,
}
stationary_parameters = {
    u: -2 * r * (l1 + l2),
    v: -r * (l2 + 4 * l3),
}

gradient = sp.Matrix([sp.diff(potential, entry) for entry in entries])
stationary_gradient = sp.simplify(gradient.subs(vacuum).subs(stationary_parameters))
hessian = sp.simplify(sp.hessian(potential, entries).subs(vacuum).subs(stationary_parameters))

sqrt2 = sp.sqrt(2)


def mode(*components):
    return sp.Matrix(components)


modes = [
    mode(1, 0, 0, 0, 0, 0, 0, 0, 0),
    mode(0, 0, 0, 0, 1 / sqrt2, 0, 0, 0, 1 / sqrt2),
    mode(0, 1 / sqrt2, 0, 1 / sqrt2, 0, 0, 0, 0, 0),
    mode(0, 0, 1 / sqrt2, 0, 0, 0, 1 / sqrt2, 0, 0),
    mode(0, 0, 0, 0, 1 / sqrt2, 0, 0, 0, -1 / sqrt2),
    mode(0, 0, 0, 0, 0, 1 / sqrt2, 0, 1 / sqrt2, 0),
    mode(0, 1 / sqrt2, 0, -1 / sqrt2, 0, 0, 0, 0, 0),
    mode(0, 0, 1 / sqrt2, 0, 0, 0, -1 / sqrt2, 0, 0),
    mode(0, 0, 0, 0, 0, 1 / sqrt2, 0, -1 / sqrt2, 0),
]
basis = sp.Matrix.hstack(*modes)
projected = sp.simplify(basis.T * hessian * basis)

scalar_block = sp.Matrix(
    [[8 * r * l1, 4 * sqrt2 * r * l2],
     [4 * sqrt2 * r * l2, 16 * r * l3]]
)
expected = sp.zeros(9)
expected[:2, :2] = scalar_block
expected[2, 2] = expected[3, 3] = 4 * r * l4
expected[4, 4] = expected[5, 5] = 16 * r * l5

scalar_trace = sp.factor(sp.trace(scalar_block))
scalar_determinant = sp.factor(scalar_block.det())
scalar_discriminant = sp.factor(
    (scalar_block[0, 0] - scalar_block[1, 1]) ** 2
    + 4 * scalar_block[0, 1] ** 2
)
scalar_eigenvalues = [
    sp.factor((scalar_trace - sp.sqrt(scalar_discriminant)) / 2),
    sp.factor((scalar_trace + sp.sqrt(scalar_discriminant)) / 2),
]

lam = sp.symbols("lambda", positive=True)
full_so3_slice = {l1: lam, l2: 0, l3: lam / 2, l4: 2 * lam, l5: lam / 2}
full_so3_projected = sp.simplify(projected.subs(full_so3_slice))

checks = {
    "wp484_dependency_passed": wp484["passed"],
    "wp498_dependency_passed": wp498["passed"],
    "isotropic_vacuum_is_stationary_after_two_mass_relations": stationary_gradient == sp.zeros(9, 1),
    "mode_basis_is_orthonormal": basis.T * basis == sp.eye(9),
    "projected_hessian_has_exact_irrep_blocks": projected == expected,
    "three_antisymmetric_modes_are_exact_zeros": projected[6:, 6:] == sp.zeros(3),
    "antisymmetric_modes_do_not_mix": projected[:6, 6:] == sp.zeros(6, 3) and projected[6:, :6] == sp.zeros(3, 6),
    "scalar_determinant_is_exact": scalar_determinant == 32 * r**2 * (4 * l1 * l3 - l2**2),
    "vector_doublet_mass_is_exact": projected[2, 2] == 4 * r * l4 and projected[3, 3] == 4 * r * l4,
    "tensor_doublet_mass_is_exact": projected[4, 4] == 16 * r * l5 and projected[5, 5] == 16 * r * l5,
    "full_so3_slice_recovers_sixfold_wp483_mass": full_so3_projected == sp.diag(*([8 * r * lam] * 6 + [0] * 3)),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP499",
    "domain": "complete renormalizable O(2)-invariant connector potential quadratic in R=SS^T around the invertible isotropic vacuum S=s I",
    "potential_coordinates": {
        "quadratic": ["u*a", "v*(b+c)"],
        "quartic": [
            "lambda_1*a^2",
            "lambda_2*a*(b+c)",
            "lambda_3*(b+c)^2",
            "lambda_4*(d^2+e^2)",
            "lambda_5*((b-c)^2+4*f^2)",
        ],
    },
    "isotropic_stationarity": {
        "u": str(stationary_parameters[u]),
        "v": str(stationary_parameters[v]),
    },
    "physical_hessian": {
        "scalar_block": [[str(value) for value in row] for row in scalar_block.tolist()],
        "scalar_eigenvalues": [str(value) for value in scalar_eigenvalues],
        "vector_doublet_mass_squared": str(4 * r * l4),
        "tensor_doublet_mass_squared": str(16 * r * l5),
        "gauge_zero_multiplicity": 3,
    },
    "strict_local_stability_cone": [
        "s>0",
        "lambda_1>0",
        "4*lambda_1*lambda_3-lambda_2^2>0",
        "lambda_4>0",
        "lambda_5>0",
    ],
    "full_so3_slice": {
        "lambda_1": "lambda",
        "lambda_2": "0",
        "lambda_3": "lambda/2",
        "lambda_4": "2*lambda",
        "lambda_5": "lambda/2",
        "physical_mass_squared": "8*lambda*s^2 with multiplicity six",
    },
    "classification": "Exact locally stable connector-spectrum completion for the symmetry-compatible five-coupling source; it supplies conditional pole coordinates but selects none of the five quartics.",
    "selector": False,
    "rigidifier": bool(projected == expected),
    "instrument": None,
    "smallest_exact_falsifier": "The physical Hessian depends on a two-by-two scalar block and two independent doublet masses, so the old sixfold-degenerate connector pole survives only on the full-SO(3) coefficient slice that is incompatible with the frozen entrance vertex.",
    "remaining_gate": "Derive or freeze the five connector couplings independently, include their beta functions and mixed scalar portals, diagonalize the complete scalar system, and only then recompute residues and total widths in detector units.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp499_o2_connector_hessian.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
