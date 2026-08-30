"""Exact coherent-tree versus traced-loop connector-port split for WP500."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp492 = load("wp492_canonical_messenger_tensor_grammar.json")
wp499 = load("wp499_o2_connector_hessian.json")

s = sp.symbols("s", positive=True)
sqrt2 = sp.sqrt(2)

# Use the WP498 adapted row basis. The normalized coherent entrance is h=e0.
# The traced-route weight inherited from the equal cyclic basis is D=I/3.
h = sp.Matrix([1, 0, 0])
D = sp.eye(3) / 3
S0 = s * sp.eye(3)

tree_port = sp.simplify(S0.T * h)
tree_gram = sp.simplify(tree_port * tree_port.T)
loop_gram = sp.simplify(S0.T * D * S0)

# WP499's six normalized physical symmetric connector modes.
physical_modes = [
    sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 1 / sqrt2, 0], [0, 0, 1 / sqrt2]]),
    sp.Matrix([[0, 1 / sqrt2, 0], [1 / sqrt2, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 1 / sqrt2], [0, 0, 0], [1 / sqrt2, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 1 / sqrt2, 0], [0, 0, -1 / sqrt2]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1 / sqrt2], [0, 1 / sqrt2, 0]]),
]


def symmetric_coordinates(matrix):
    return sp.Matrix(
        [
            matrix[0, 0],
            matrix[1, 1],
            matrix[2, 2],
            sqrt2 * matrix[0, 1],
            sqrt2 * matrix[0, 2],
            sqrt2 * matrix[1, 2],
        ]
    )


tree_jacobian = sp.Matrix.hstack(*[mode.T * h for mode in physical_modes])
loop_variations = [sp.simplify((mode.T * S0 + S0.T * mode) / 3) for mode in physical_modes]
loop_jacobian = sp.Matrix.hstack(*[symmetric_coordinates(change) for change in loop_variations])

# A shared frame and shared normalized entrance give collinear up/down tree
# coefficient vectors, regardless of their two scalar normalizations.
cu, cd = sp.symbols("c_u c_d", nonzero=True)
two_sector_ports = sp.Matrix.hstack(cu * tree_port, cd * tree_port)
tree_kernel_basis = sp.Matrix.hstack(physical_modes[1].reshape(9, 1), physical_modes[4].reshape(9, 1), physical_modes[5].reshape(9, 1))

checks = {
    "wp492_dependency_passed": wp492["passed"],
    "wp499_dependency_passed": wp499["passed"],
    "tree_port_is_single_coherent_vector": tree_port == sp.Matrix([s, 0, 0]),
    "tree_outer_product_has_rank_one": tree_gram.rank() == 1,
    "normalized_traced_loop_gram_is_isotropic": loop_gram == s**2 * sp.eye(3) / 3,
    "traced_loop_gram_has_rank_three": loop_gram.rank() == 3,
    "traced_loop_determinant_is_exact": sp.factor(loop_gram.det()) == s**6 / 27,
    "tree_physical_mode_jacobian_has_rank_three": tree_jacobian.rank() == 3,
    "loop_physical_mode_jacobian_has_rank_six": loop_jacobian.rank() == 6,
    "tree_blind_physical_subspace_has_dimension_three": len(tree_jacobian.nullspace()) == 3,
    "declared_transverse_trace_and_tensor_modes_are_tree_blind": tree_jacobian * sp.Matrix.hstack(
        sp.eye(6)[:, 1], sp.eye(6)[:, 4], sp.eye(6)[:, 5]
    ) == sp.zeros(3, 3),
    "shared_up_down_tree_ports_are_collinear": two_sector_ports.rank() == 1,
    "loop_and_tree_grams_are_not_equal": loop_gram != tree_gram,
    "formal_loop_response_has_no_physical_connector_kernel": loop_jacobian.det() != 0,
    "tree_kernel_witness_has_three_independent_modes": tree_kernel_basis.rank() == 3,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP500",
    "domain": "WP492 normalized equal entrance, componentwise connector incidence, identity messenger masses, shared connector frame, and the WP499 six-mode physical connector tangent space",
    "tree_operation": {
        "contraction": "p=S^T h",
        "vacuum_port": [str(value) for value in tree_port],
        "outer_product_rank": int(tree_gram.rank()),
        "physical_mode_response_rank": int(tree_jacobian.rank()),
        "physical_mode_kernel_dimension": len(tree_jacobian.nullspace()),
        "blind_irreps": ["transverse-trace singlet", "traceless-tensor doublet"],
    },
    "closed_loop_operation": {
        "contraction": "W_loop=S^T D S with D=I_3/3 from the normalized equal-route trace",
        "vacuum_gram": [[str(value) for value in row] for row in loop_gram.tolist()],
        "gram_rank": int(loop_gram.rank()),
        "gram_determinant": str(sp.factor(loop_gram.det())),
        "formal_physical_mode_response_rank": int(loop_jacobian.rank()),
        "physical_mode_kernel_dimension": len(loop_jacobian.nullspace()),
    },
    "two_sector_tree_matching": {
        "port_rank": int(two_sector_ports.rank()),
        "consequence": "With one shared frame and one shared entrance shape, the up/down linear-word coefficient vectors are collinear. Scalar normalizations do not create two independent flavor directions.",
    },
    "normalization_correction": "WP483's unweighted S^T S is recovered only if the equal entrance components are left unnormalized or the factor three is absorbed into the scalar coupling. Under WP492's normalized shape, the explicit route trace is S^T S/3.",
    "classification": "Source-typing separation: the loop portal is a full-rank formal connector probe and rigidifier, while the executable tree matching is rank three on connector fluctuations and rank one in adjoint-port space. They are not interchangeable readouts.",
    "selector": False,
    "rigidifier": bool(loop_gram.rank() == 3),
    "instrument": None,
    "smallest_exact_falsifier": "At S=s I, the coherent tree outer product has rank one while the normalized closed-loop Gram has rank three and determinant s^6/27.",
    "remaining_gate": "Declare three independently labelled external entrance channels or another source-derived rank-three tree map if the connector is to reproduce a generic physical16 Yukawa pair; separately derive a physical threshold instrument capable of resolving the six-dimensional loop-Gram response before assigning connector residues or widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp500_tree_loop_port_split.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
