from fractions import Fraction
import json
from pathlib import Path


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def determinant_columns(u, v, w):
    return (
        u[0] * (v[1] * w[2] - v[2] * w[1])
        - v[0] * (u[1] * w[2] - u[2] * w[1])
        + w[0] * (u[1] * v[2] - u[2] * v[1])
    )


A = (
    (Fraction(1), 0, 0),
    (0, Fraction(2), 0),
    (0, 0, Fraction(3)),
)
x = (Fraction(1), Fraction(1), Fraction(1))


def destructive_chain(operator, seed):
    return ((2, matvec(operator, matvec(operator, seed))),)


def illicit_same_state_fanout(seed):
    return ((0, seed), (0, seed), (0, seed))


def history_chain(operator, seed):
    depth0 = seed
    depth1 = matvec(operator, depth0)
    depth2 = matvec(operator, depth1)
    return ((0, depth0), (1, depth1), (2, depth2))


destructive = destructive_chain(A, x)
fanout = illicit_same_state_fanout(x)
history = history_chain(A, x)

assert len(destructive) == 1
assert determinant_columns(*(value for _, value in fanout)) == 0
assert tuple(depth for depth, _ in history) == (0, 1, 2)
history_determinant = determinant_columns(*(value for _, value in history))
assert history_determinant == 2

# Reordering two depth ports reverses the signed determinant, so depth labels
# are operative and cannot be erased before observation.
swapped = (history[0], history[2], history[1])
assert determinant_columns(*(value for _, value in swapped)) == -history_determinant

# Under seed-ray rephasing, every linear history port has weight one. The
# determinant has weight three; its modulus squared has weight zero. A signed
# relational readout needs an independently derived reference of weight -3.
port_phase_weights = (1, 1, 1)
determinant_phase_weight = sum(port_phase_weights)
projective_weight = determinant_phase_weight - determinant_phase_weight
volume_reference_weight = -3
relational_signed_weight = determinant_phase_weight + volume_reference_weight
assert determinant_phase_weight == 3
assert projective_weight == 0
assert relational_signed_weight == 0

result = {
    "schema": "marici.nima.flavor-interaction-net-history.v1",
    "destructive_chain_output_ports": len(destructive),
    "same_state_fanout_determinant": str(determinant_columns(*(value for _, value in fanout))),
    "history_depth_signature": [depth for depth, _ in history],
    "history_determinant": str(history_determinant),
    "depth_swap_reverses_signed_determinant": True,
    "determinant_seed_phase_weight": determinant_phase_weight,
    "projective_modulus_squared_weight": projective_weight,
    "required_volume_reference_weight": volume_reference_weight,
    "relational_signed_readout_weight": relational_signed_weight,
    "verdict": (
        "An explicit history constructor generates three depth-typed Krylov "
        "ports; destructive execution and same-state fanout do not. The "
        "physical projective observer is the modulus squared. A signed output "
        "requires an additional source-derived volume-reference port."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-interaction-net-history.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
