import json
from itertools import product
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v12 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v12.json").read_text(
        encoding="utf-8"
    )
)

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
alpha, beta = sp.symbols("alpha beta", nonzero=True)
G = list(product((0, 1), repeat=2))


def add(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    return ((g[0] + h[0]) % 2, (g[1] + h[1]) % 2)


def rho(g: tuple[int, int]) -> sp.Matrix:
    return (X ** g[0]) * (Z ** g[1])


def omega(g: tuple[int, int], h: tuple[int, int]) -> int:
    return (-1) ** (g[1] * h[0])


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b * a.inv() * b.inv())


cocycle_holds = all(
    omega(g, h) * omega(add(g, h), k) == omega(h, k) * omega(g, add(h, k))
    for g, h, k in product(G, repeat=3)
)
projective_product_holds = all(
    sp.simplify(rho(g) * rho(h) - omega(g, h) * rho(add(g, h))) == sp.zeros(2)
    for g, h in product(G, repeat=2)
)

family = v12["nonabelian_framed_spectral_family"]
all_terms = (
    set(v12["object_types"])
    | set(v12["arrow_types"])
    | set(v12["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v12["forbidden_promotions"])
)

missing_markers = (
    "projective_unitary_bundle",
    "pu_r_connection",
    "central_extension",
    "multiplier_2_cocycle",
    "bundle_gerbe",
    "projective_holonomy",
)

checks = {
    "v12_is_frozen": v12["cell_creation_during_replay"] is False,
    "pauli_loops_are_unitary": X.conjugate().T * X == I2 and Z.conjugate().T * Z == I2,
    "torus_generators_commute_projectively": X * Z == -(Z * X),
    "projective_commutator_is_central_minus_identity": commutator(X, Z) == -I2,
    "projective_product_law_holds_for_all_group_pairs": projective_product_holds,
    "multiplier_satisfies_full_2_cocycle_law": cocycle_holds,
    "multiplier_is_not_symmetric": omega((1, 0), (0, 1)) != omega((0, 1), (1, 0)),
    "scalar_rephasing_cannot_remove_commutator": commutator(alpha * X, beta * Z) == -I2,
    "v12_exact_torus_relation_rejects_packet": "all_path_groupoid_and_braid_relations_hold_as_matrix_equalities" in family["required_laws"] and X * Z != Z * X,
    "v12_has_no_projective_or_cocycle_carrier": not any(marker in term.lower() for term in all_terms for marker in missing_markers),
    "coherent_projective_transport_is_not_an_honest_u2_representation": projective_product_holds and X * Z != Z * X,
}

result = {
    "schema": "marici.aspect.v12-projective-torus-falsifier.v1",
    "status": "frozen_v12_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "the projective Z2 x Z2 Pauli representation rho(a,b)=X^a Z^b with multiplier (-1)^(b c)",
    "failure": "the transport is coherent in PU(2) with a nontrivial U(1) 2-cocycle, but v12 demands an honest U(2) representation and has no carrier for the central multiplier",
    "required_future_repair": "projective unitary bundles or central extensions with an explicit multiplier 2-cocycle, cocycle gauge law, and gerbe-level specialization before choosing an honest lift",
}

out = root / "results" / "v12_projective_torus_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v12_falsified" else 1)
