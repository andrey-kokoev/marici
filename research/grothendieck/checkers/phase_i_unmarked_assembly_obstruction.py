"""Exact source-symmetry obstruction to unmarked quadrilateral sewing."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

from sympy.combinatorics import Permutation, PermutationGroup


ROOT = Path(__file__).resolve().parents[3]
ENTRY_27 = (
    ROOT
    / "src/ledger/20260813-27 Regional Core-Filtered Scalar-QTDS Theorem.md"
)
ENTRY_37 = (
    ROOT
    / "src/ledger/20260813-37 All-Arity Rooted-Spine Base-Change Theorem.md"
)
ENTRY_116 = (
    ROOT
    / "src/ledger/20260814-116 Saturated D03 Exit Carrier and the Missing "
    "Thom-Decorated Road Lift.md"
)
ENTRY_117 = (
    ROOT
    / "src/ledger/20260814-117 D03 Thom Endpoint Koszul Hull and the Missing "
    "Road Generizations.md"
)
OUT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-unmarked-assembly-obstruction.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


# Array notation gives exact permutations of the cyclic boundary edges.
rotation = Permutation([1, 2, 3, 0])
reflection = Permutation([0, 3, 2, 1])
cyclic = PermutationGroup([rotation])
dihedral = PermutationGroup([rotation, reflection])

cyclic_elements = list(cyclic.generate_schreier_sims())
dihedral_elements = list(dihedral.generate_schreier_sims())
assert cyclic.order() == 4
assert dihedral.order() == 8

edges = tuple(range(4))
gluing_choices = tuple(itertools.product(edges, repeat=2))
assert len(gluing_choices) == 16


def act(left: Permutation, right: Permutation, pair: tuple[int, int]):
    return (int(left(pair[0])), int(right(pair[1])))


fixed_pairs = [
    pair
    for pair in gluing_choices
    if all(
        act(left, right, pair) == pair
        for left in dihedral_elements
        for right in dihedral_elements
    )
]
assert fixed_pairs == []

rotation_orbit = {
    act(left, right, (0, 0))
    for left in cyclic_elements
    for right in cyclic_elements
}
assert rotation_orbit == set(gluing_choices)

left_mark_stabilizer = [g for g in dihedral_elements if int(g(0)) == 0]
right_mark_stabilizer = [g for g in dihedral_elements if int(g(0)) == 0]
assert len(left_mark_stabilizer) == 2
assert len(right_mark_stabilizer) == 2
assert all(
    act(left, right, (0, 0)) == (0, 0)
    for left in left_mark_stabilizer
    for right in right_mark_stabilizer
)

# Deliberate failure: an unmarked natural connected sewing would require a
# fixed gluing pair. The exact fixed-point set is empty.
naive_canonical_unmarked_sewing_exists = bool(fixed_pairs)
assert naive_canonical_unmarked_sewing_exists is False

inputs = [ENTRY_27, ENTRY_37, ENTRY_116, ENTRY_117]
for path in inputs:
    assert path.is_file()

packet = {
    "schema": (
        "marici.grothendieck."
        "phase_i_unmarked_assembly_obstruction.v1"
    ),
    "demonstrated_strength": [
        "finite-cutoff theorem",
        "source-typed morphism",
    ],
    "compatibility_preflight": {
        "coefficient_domain": None,
        "coefficient_prime": None,
        "ambient_carrier_arity": "(4,4)_to_6",
        "left_boundary_order": list(edges),
        "right_boundary_order": list(edges),
        "source_symmetry": "D4_x_D4 independent relabelling",
        "filtration_stage": "coefficient-neutral carrier assembly",
        "pole_depths": "not_applicable",
        "input_sha256": {rel(path): sha256(path) for path in inputs},
    },
    "finite_model": {
        "left_edge_count": len(edges),
        "right_edge_count": len(edges),
        "gluing_choice_count": len(gluing_choices),
        "cyclic_group_order": int(cyclic.order()),
        "dihedral_group_order": int(dihedral.order()),
        "independent_rotation_orbit_size": len(rotation_orbit),
        "dihedral_fixed_gluing_pairs": fixed_pairs,
        "left_mark_stabilizer_order": len(left_mark_stabilizer),
        "right_mark_stabilizer_order": len(right_mark_stabilizer),
    },
    "deliberate_failure": {
        "naive_claim": (
            "the regional tensor canonically selects an unmarked connected "
            "sewing of two cyclic quadrilateral carriers"
        ),
        "claim_holds": naive_canonical_unmarked_sewing_exists,
        "required_fixed_point_count_minimum": 1,
        "observed_fixed_point_count": len(fixed_pairs),
        "nonzero_obstruction": (
            "E_x_E is one nontrivial C4_x_C4 torsor of size 16"
        ),
    },
    "marked_control": {
        "chosen_pair": [0, 0],
        "fixed_by_mark_stabilizers": True,
        "interpretation": (
            "a supplied cut/interface mark types the regional sewing but is "
            "additional input to an unmarked binary operation"
        ),
    },
    "verdict": {
        "unmarked_connected_binary_assembly_derived": False,
        "marked_regional_assembly_contradicted": False,
        "finite_coproduct_derived": False,
        "carrier_semiring_derived": False,
        "arithmetic_derived": False,
    },
    "deferred": [
        "sum over all sewings",
        "Burnside/Grothendieck completion",
        "lambda operations",
        "big Witt object",
        "Frobenius/Verschiebung",
        "Euler product",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
