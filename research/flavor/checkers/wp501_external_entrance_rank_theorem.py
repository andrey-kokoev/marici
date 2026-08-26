"""Exact externally distinguishable connector-entrance rank theorem for WP501."""

import itertools
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp500 = load("wp500_tree_loop_port_split.json")

s = sp.symbols("s", positive=True)
S0 = s * sp.eye(3)

# General three-channel determinant identity.
h_symbols = sp.symbols("h0:9", real=True)
H3 = sp.Matrix(3, 3, h_symbols)
s_symbols = sp.symbols("q0:9", real=True)
S = sp.Matrix(3, 3, s_symbols)
P3 = H3 * S
W3 = sp.simplify(P3.T * P3)
determinant_identity = sp.factor(W3.det() - H3.det() ** 2 * S.det() ** 2)

# Cauchy-Binet gives the exact full-rank criterion for any number of channels.
h4_symbols = sp.symbols("k0:12", real=True)
H4 = sp.Matrix(4, 3, h4_symbols)
minor_squares = sum(
    H4[list(rows), :].det() ** 2 for rows in itertools.combinations(range(4), 3)
)
cauchy_binet_identity = sp.factor((H4.T * H4).det() - minor_squares)

# Rank caps and hostile currently admitted preparations.
H1 = sp.Matrix([[1, 2, 3]])
H2 = sp.Matrix([[1, 0, 0], [0, 1, 0]])
blind_two_channel = sp.Matrix([0, 0, 1])

cu, cd = sp.symbols("c_u c_d", nonzero=True)
h_equal = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
H_shared = sp.Matrix.vstack((cu * h_equal).T, (cd * h_equal).T)
W_shared = sp.simplify((H_shared * S0).T * (H_shared * S0))

H_orthogonal = sp.eye(3)
P_orthogonal = H_orthogonal * S0
W_orthogonal = sp.simplify(P_orthogonal.T * P_orthogonal)

# Generic full-rank preparations separate port directions but are isotropic
# only on the stronger orthonormal-frame locus.
x, y, z = sp.symbols("x y z", positive=True)
H_weighted = sp.diag(x, y, z)
W_weighted = sp.simplify((H_weighted * S0).T * (H_weighted * S0))

checks = {
    "wp500_dependency_passed": wp500["passed"],
    "one_channel_rank_is_at_most_one": H1.rank() == 1,
    "two_channel_rank_is_at_most_two": H2.rank() == 2,
    "two_channel_hostile_blind_vector_is_exact": H2 * blind_two_channel == sp.zeros(2, 1),
    "three_channel_gram_determinant_identity_is_exact": determinant_identity == 0,
    "four_channel_cauchy_binet_identity_is_exact": cauchy_binet_identity == 0,
    "shared_up_down_preparations_have_rank_one": H_shared.rank() == 1,
    "shared_up_down_gram_has_rank_one": W_shared.rank() == 1,
    "three_orthogonal_preparations_have_rank_three": P_orthogonal.rank() == 3,
    "three_orthogonal_preparations_give_isotropic_gram": W_orthogonal == s**2 * sp.eye(3),
    "three_orthogonal_gram_determinant_is_exact": sp.factor(W_orthogonal.det()) == s**6,
    "generic_weighted_full_rank_gram_is_positive_diagonal": W_weighted == s**2 * sp.diag(x**2, y**2, z**2),
    "full_rank_does_not_imply_isotropy": W_weighted.subs({x: 1, y: 2, z: 3}) != s**2 * sp.eye(3),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP501",
    "domain": "real externally distinguishable entrance preparations H with connector tree map P=H S and invertible connector vacuum S",
    "rank_theorem": {
        "statement": "rank(P)=rank(H) for invertible S; a faithful three-direction tree port exists exactly when rank(H)=3",
        "minimum_external_channel_count": 3,
        "three_channel_gram_determinant": "det(P^T P)=det(H)^2 det(S)^2",
        "general_channel_criterion": "det(H^T H) is the sum of squares of all three-by-three row minors",
    },
    "hostile_cases": {
        "one_channel_maximum_rank": int(H1.rank()),
        "two_independent_channels_rank": int(H2.rank()),
        "two_channel_blind_direction": [str(value) for value in blind_two_channel],
        "shared_up_down_rank": int(H_shared.rank()),
    },
    "minimal_sufficient_packet": {
        "preparation_matrix": "H=I_3",
        "vacuum_tree_map": "P=s I_3",
        "tree_gram": "s^2 I_3",
        "rank": int(P_orthogonal.rank()),
    },
    "selector_rigidifier_split": "Rank three is the faithfulness condition. Isotropy additionally requires H^T H proportional to I and is a stronger rigidifier condition; neither condition selects its common normalization.",
    "physical_typing": "The row labels must remain distinguishable at preparation and readout. Three hidden internal copies that are coherently summed still implement one channel, not three.",
    "classification": "Exact necessary-and-sufficient constructor theorem for repairing WP500's tree-port kernel; the theorem specifies a source capability but does not establish an existing physical realization.",
    "selector": False,
    "rigidifier": bool(W_orthogonal == s**2 * sp.eye(3)),
    "instrument": None,
    "smallest_exact_falsifier": "Any entrance preparation matrix H with rank below three leaves a nonzero adjoint-port vector in ker(H), even when the connector frame S is invertible.",
    "remaining_gate": "Name a physically admitted three-channel preparation whose labels survive to independently calibrated readouts, derive its gauge-invariant renormalizable vertices, and test whether detector-level response retains rank three under mixing, widths, and resolution.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp501_external_entrance_rank_theorem.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
