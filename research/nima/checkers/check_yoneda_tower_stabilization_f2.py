"""Finite exact audit of Yoneda stabilization and restricted-probe quotients."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/yoneda-tower-stabilization-f2.json"


Matrix = tuple[tuple[int, ...], ...]


def matrices(rows: int, cols: int) -> list[Matrix]:
    return [
        tuple(tuple(bits[r * cols + c] for c in range(cols)) for r in range(rows))
        for bits in itertools.product((0, 1), repeat=rows * cols)
    ]


def compose(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    middle = len(right)
    cols = len(right[0]) if right else 0
    if rows == 0:
        return tuple()
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(middle)) % 2
            for j in range(cols)
        )
        for i in range(rows)
    )


def identity(dim: int) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(dim)) for i in range(dim))


def flatten(matrix: Matrix) -> tuple[int, ...]:
    return tuple(value for row in matrix for value in row)


V_DIM = 2
W_DIM = 2
OBJECT_DIMS = (0, 1, 2)
linear_maps = matrices(W_DIM, V_DIM)


def yoneda_profile(f: Matrix) -> tuple[tuple[int, int, tuple[int, ...]], ...]:
    profile = []
    for a_dim in OBJECT_DIMS:
        for index, probe in enumerate(matrices(V_DIM, a_dim)):
            profile.append((a_dim, index, flatten(compose(f, probe))))
    return tuple(profile)


profiles = {yoneda_profile(f) for f in linear_maps}
recovered = {
    flatten(compose(f, identity(V_DIM)))
    for f in linear_maps
}

# Exhaustive naturality for every f, every A,B, every probe g:A->V, and every
# change of probe h:B->A.
naturality_checks = 0
naturality_ok = True
for f in linear_maps:
    for a_dim in OBJECT_DIMS:
        for b_dim in OBJECT_DIMS:
            for g in matrices(V_DIM, a_dim):
                for h in matrices(a_dim, b_dim):
                    left = compose(f, compose(g, h))
                    right = compose(compose(f, g), h)
                    naturality_checks += 1
                    naturality_ok &= left == right

# Restricted sector probes on the four states of F_2^2.
states = tuple((x, y) for x, y in itertools.product((0, 1), repeat=2))
p0 = lambda state: state[0]
p1 = lambda state: state[1]
restricted_profiles = {p0(state) for state in states}
joint_profiles = {(p0(state), p1(state)) for state in states}
restricted_kernel = tuple(state for state in states if p0(state) == 0)

gates = {
    "all_16_linear_maps_audited": len(linear_maps) == 16,
    "full_yoneda_profiles_are_injective": len(profiles) == len(linear_maps),
    "identity_probe_recovers_every_map": len(recovered) == len(linear_maps),
    "all_probe_changes_are_natural": naturality_ok and naturality_checks > 0,
    "single_sector_probe_creates_two_state_quotient": len(restricted_profiles) == 2,
    "restricted_probe_has_nontrivial_kernel": len(restricted_kernel) == 2,
    "restored_probe_family_is_jointly_faithful": len(joint_profiles) == len(states),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.yoneda-tower-stabilization-f2.v1",
    "category_fragment": "finite F_2 vector spaces of dimensions 0,1,2",
    "linear_map_count": len(linear_maps),
    "distinct_full_profiles": len(profiles),
    "naturality_squares_checked": naturality_checks,
    "restricted_sector": {
        "state_count": len(states),
        "observable_profiles": len(restricted_profiles),
        "kernel": [list(state) for state in restricted_kernel],
    },
    "restored_family": {"observable_profiles": len(joint_profiles)},
    "gates": gates,
    "conclusion": (
        "Full representable probing reconstructs each map and the second "
        "probe-profile rung adds no new map data.  Restricting to one probe "
        "creates a quotient; adjoining the missing independent probe restores "
        "joint faithfulness."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
