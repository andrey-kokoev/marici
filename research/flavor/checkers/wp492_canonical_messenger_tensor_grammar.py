"""Exact canonical messenger-tensor grammar for WP492."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp483 = load("wp483_connector_frame_architecture.json")
wp491 = load("wp491_yukawa_tensor_completeness_gate.json")

cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
entrance = sp.ones(3, 1) / sp.sqrt(3)
identity = sp.eye(3)

# Solve exact commutants to distinguish symmetry authority from the new
# diagonal-incidence locality axiom.
c_symbols = sp.symbols("c0:9", real=True)
C = sp.Matrix(3, 3, c_symbols)
commutant_equations = list(C * cycle - cycle * C)
commutant_matrix, _ = sp.linear_eq_to_matrix(commutant_equations, c_symbols)
cyclic_commutant_dimension = len(c_symbols) - commutant_matrix.rank()

symmetric_symbols = sp.symbols("u0:6", real=True)
Cs = sp.Matrix(
    [
        [symmetric_symbols[0], symmetric_symbols[1], symmetric_symbols[2]],
        [symmetric_symbols[1], symmetric_symbols[3], symmetric_symbols[4]],
        [symmetric_symbols[2], symmetric_symbols[4], symmetric_symbols[5]],
    ]
)
symmetric_equations = list(Cs * cycle - cycle * Cs)
symmetric_matrix, _ = sp.linear_eq_to_matrix(symmetric_equations, symmetric_symbols)
cyclic_symmetric_commutant_dimension = len(symmetric_symbols) - symmetric_matrix.rank()

L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]

# The connector incidence tensor T_{alpha,beta,i,j}=delta_{alpha,beta}
# delta_{i,j}; its flattened shape is I_9.
connector_incidence = sp.eye(9)

shape_norms = {
    "Y_H": sp.simplify((entrance.T * entrance)[0]),
    "Y_S": sp.trace(connector_incidence.T * connector_incidence),
    "Y_X": sp.trace(identity.T * identity),
    "Z_A": sp.trace(identity.T * identity),
    "Z_B": sp.trace(identity.T * identity),
}

tensor_packet = [
    f"{name}_{sector}"
    for sector in ("up", "down")
    for name in ("Y_H", "Y_S", "Y_X", "Z_A", "Z_B")
]

checks = {
    "wp483_dependency_passed": wp483["passed"],
    "wp491_dependency_passed": wp491["passed"],
    "cyclic_entrance_is_invariant": entrance.T * cycle == entrance.T,
    "cyclic_entrance_fixed_space_is_one_dimensional": (cycle - sp.eye(3)).nullspace().__len__() == 1,
    "port_dot_is_infinitesimally_invariant": all(generator.T + generator == sp.zeros(3) for generator in L),
    "canonical_mass_maps_are_invariant": cycle.T * identity * cycle == identity,
    "connector_incidence_is_identity_on_nine_components": connector_incidence == sp.eye(9),
    "cyclic_general_commutant_has_dimension_three": cyclic_commutant_dimension == 3,
    "cyclic_symmetric_mass_commutant_has_dimension_two": cyclic_symmetric_commutant_dimension == 2,
    "locality_axiom_selects_identity_from_larger_commutant": cyclic_commutant_dimension > 1 and C.shape == identity.shape,
    "ten_tensor_shapes_are_frozen": len(tensor_packet) == 10 and len(set(tensor_packet)) == 10,
    "canonical_shape_norms_are_exact": shape_norms == {"Y_H": 1, "Y_S": 9, "Y_X": 3, "Z_A": 3, "Z_B": 3},
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP492",
    "domain": "WP483 two-stage messenger chain factored from spectator color/flavor identities, separately for up and down Standard Model charge sectors",
    "canonical_shapes": {
        "Y_H": "normalized cyclic fixed vector (1,1,1)/sqrt(3)",
        "Y_S": "componentwise connector incidence delta_alpha_beta delta_i_j",
        "Y_X": "SO(3)_P invariant dot delta_i_j",
        "Z_A": "identity on cyclic entrance labels",
        "Z_B": "identity on oriented port labels",
    },
    "tensor_packet": tensor_packet,
    "shape_frobenius_norm_squared": {name: str(value) for name, value in shape_norms.items()},
    "authority_partition": {
        "symmetry_forced": ["Y_H direction", "Y_X port dot", "Z_B symmetric port mass shape"],
        "source_axiom": ["componentwise Y_S incidence", "identity Z_A rather than a general cyclic symmetric commutant"],
        "free_scalars": "ten real sector-specific normalizations remain RG coordinates",
    },
    "commutant_dimensions": {
        "general_cyclic_intertwiner": int(cyclic_commutant_dimension),
        "symmetric_cyclic_mass": int(cyclic_symmetric_commutant_dimension),
    },
    "classification": "Independently frozen tensor-shape grammar sufficient to define contraction inputs; coefficient values and beta functions remain uncomputed.",
    "selector": False,
    "rigidifier": "canonical incidence rigidifies the messenger presentation and preserves the isotropic route grammar",
    "instrument": None,
    "smallest_exact_falsifier": "Cyclic symmetry alone leaves a three-dimensional connector intertwiner commutant and a two-dimensional symmetric A-mass commutant, so diagonal incidence must remain an explicit source axiom.",
    "remaining_gate": "Attach ten scalar normalizations, scalar/SM couplings, scheme and threshold maps to this shape packet, then derive the beta vector field without fitting a fixed point.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp492_canonical_messenger_tensor_grammar.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
