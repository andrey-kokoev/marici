"""Exact messenger-port rank audit for the three-adjoint portal."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp435 = load("wp435_dynamical_flavon_messenger_completion.json")
wp447 = load("wp447_irreducible_adjoint_triplet.json")
wp478 = load("wp478_messenger_portal_threshold.json")

p1, p2, p3, q1, q2, q3 = sp.symbols("p1 p2 p3 q1 q2 q3", real=True)
p = sp.Matrix([[p1, p2, p3], [q1, q2, q3]])
two_port_gram = sp.simplify(p.T * p)
kernel_witness = sp.Matrix(
    [p2 * q3 - p3 * q2, p3 * q1 - p1 * q3, p1 * q2 - p2 * q1]
)

kappa = sp.symbols("kappa", positive=True)
isotropic_gram = kappa * sp.eye(3)
three_port_matrix = sp.sqrt(kappa) * sp.eye(3)
three_port_gram = sp.simplify(three_port_matrix.T * three_port_matrix)

# The spin-one vacuum has an isotropic adjoint-label trace Gram.
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
vacuum_trace_gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.trace(J[i] * J[j])))

checks = {
    "wp435_dependency_passed": wp435["passed"],
    "wp447_dependency_passed": wp447["passed"],
    "wp478_dependency_passed": wp478["passed"],
    "two_port_gram_determinant_is_identically_zero": sp.factor(two_port_gram.det()) == 0,
    "two_port_gram_rank_is_at_most_two": len(two_port_gram.columnspace()) <= 2,
    "cross_product_is_exact_kernel_witness": sp.simplify(two_port_gram * kernel_witness) == sp.zeros(3, 1),
    "positive_isotropic_gram_has_rank_three": isotropic_gram.rank() == 3,
    "positive_isotropic_gram_has_nonzero_determinant": isotropic_gram.det() == kappa**3,
    "three_canonical_ports_are_sufficient": three_port_gram == isotropic_gram,
    "spin_one_vacuum_trace_gram_is_isotropic": vacuum_trace_gram == 2 * sp.eye(3),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP479",
    "state_domain": "three WP447 adjoints with messenger ports coupling to linear combinations p_alpha_i X_i",
    "portal_pairing": "W=sum_alpha p_alpha^dagger p_alpha on the adjoint-triplet label space",
    "minimal_wp435_ports": {
        "count": 2,
        "labels": ["up", "down"],
        "gram_matrix": [[str(value) for value in row] for row in two_port_gram.tolist()],
        "determinant": str(sp.factor(two_port_gram.det())),
        "kernel_witness": [str(value) for value in kernel_witness],
        "maximum_rank": 2,
    },
    "common_clock_requirement": {
        "pairing": "kappa*I_3",
        "determinant": "kappa^3",
        "rank": 3,
        "reason": "Only an isotropic pairing descends under the oriented adjoint-triplet symmetry used by WP447 and WP467.",
    },
    "minimum_port_theorem": {
        "necessary_ports": 3,
        "sufficient_witness": "P=sqrt(kappa)*I_3",
        "remaining_authority": "The equal-norm orthogonal three-port law and kappa must be derived from the source; algebraic span alone is not executable messenger control.",
    },
    "contextual_partition": {
        "two_ports": "Every source packet has at least one blind adjoint-label direction and breaks or undersamples the isotropic portal.",
        "three_generic_ports": "Can reach rank three but need not be isotropic.",
        "three_orthogonal_equal_ports": "Exactly reproduce the common-clock pairing conditionally.",
    },
    "classification": "Two-port messenger completion is insufficient for descent to the isotropic common-clock selector; a third source-derived port is necessary but not alone sufficient.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument": None,
    "impact_on_existing_spectrum": "WP475-WP476 remain valid only for the independently declared isotropic portal. They are not derived from the minimal two-port WP435 messenger threshold.",
    "smallest_exact_falsifier": "The cross product of the two port vectors is annihilated by their Gram matrix, while kappa*I_3 annihilates no nonzero vector.",
    "remaining_gate": "Construct at least three executable messenger ports with a source symmetry enforcing an equal-norm orthogonal Gram, then redo full threshold matching and the scalar/vector spectral packet.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp479_triplet_portal_port_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
