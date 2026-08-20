"""Exact Phase-I obstruction from coproducts in the n=8 face poset."""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from sympy import Eq, Symbol, solve


ROOT = Path(__file__).resolve().parents[3]
ENTRY_07 = ROOT / "src/ledger/20260812-07 Surface Operations and the Cut Kernel.md"
ENTRY_46 = (
    ROOT
    / "src/ledger/20260813-46 Closed-Circuit Resolution and the Modular "
    "Counit Target.md"
)
ENTRY_90 = (
    ROOT
    / "src/ledger/20260814-90 Transverse Incidence Skeleton and the Cut-Only "
    "Descent Falsifier.md"
)
VOEVODSKY_CONTEXT = ROOT / "research/voevodsky/context.md"
N8_CHECKER = ROOT / "research/voevodsky/check_n8_scalar_cd_site.rs"
OUT = (
    ROOT
    / "research/grothendieck/results/"
    "phase-i-face-coproduct-idempotence.json"
)


Diagonal = tuple[int, int]
Triangulation = frozenset[Diagonal]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def edge(a: int, b: int) -> Diagonal:
    return (a, b) if a < b else (b, a)


@lru_cache(maxsize=None)
def polygon_triangulations(vertices: tuple[int, ...]) -> tuple[Triangulation, ...]:
    """Enumerate triangulations by the triangle incident to the closing edge."""

    if len(vertices) <= 3:
        return (frozenset(),)

    first = vertices[0]
    last = vertices[-1]
    result: set[Triangulation] = set()

    for pivot_index in range(1, len(vertices) - 1):
        pivot = vertices[pivot_index]
        left = vertices[: pivot_index + 1]
        right = vertices[pivot_index:]
        inserted: set[Diagonal] = set()
        if pivot_index > 1:
            inserted.add(edge(first, pivot))
        if pivot_index < len(vertices) - 2:
            inserted.add(edge(pivot, last))

        for left_triangulation in polygon_triangulations(left):
            for right_triangulation in polygon_triangulations(right):
                result.add(
                    frozenset(
                        set(left_triangulation)
                        | set(right_triangulation)
                        | inserted
                    )
                )

    return tuple(sorted(result, key=lambda item: tuple(sorted(item))))


def support(
    dissection: frozenset[Diagonal],
    triangulations: tuple[Triangulation, ...],
) -> frozenset[Triangulation]:
    """Return the closed face X_S of triangulations containing S."""

    return frozenset(
        triangulation
        for triangulation in triangulations
        if dissection <= triangulation
    )


inputs = [ENTRY_07, ENTRY_46, ENTRY_90, VOEVODSKY_CONTEXT, N8_CHECKER]
for path in inputs:
    assert path.is_file()

triangulations = polygon_triangulations(tuple(range(8)))
assert len(triangulations) == 132
assert all(len(triangulation) == 5 for triangulation in triangulations)

# Two explicit fan triangulations are closed zero-dimensional faces.  They
# have no common diagonal, so the least closed face containing both is the
# whole associahedron X_emptyset, not their two-point set-theoretic union.
left_fan: Triangulation = frozenset(edge(0, vertex) for vertex in range(2, 7))
right_fan: Triangulation = frozenset(edge(1, vertex) for vertex in range(3, 8))
assert left_fan in triangulations
assert right_fan in triangulations
assert left_fan.isdisjoint(right_fan)

left_face = support(left_fan, triangulations)
right_face = support(right_fan, triangulations)
assert left_face == frozenset({left_fan})
assert right_face == frozenset({right_fan})

common_dissection = left_fan & right_fan
categorical_join = support(common_dissection, triangulations)
geometric_union = left_face | right_face
assert len(categorical_join) == 132
assert len(geometric_union) == 2

# Any face containing both fan vertices has constraint set contained in their
# common diagonals.  Here that intersection is empty, so the ambient face is
# the only possible common upper bound face; the two-point union is not X_S.
candidate_common_constraints = [frozenset()]
geometric_union_is_closed_face = any(
    support(candidate, triangulations) == geometric_union
    for candidate in candidate_common_constraints
)
assert geometric_union_is_closed_face is False

# In every thin category, if a binary coproduct exists then X coproduct X = X:
# it is the least upper bound of X with itself.  Hence every additive class is
# idempotent, and cancellation in its Grothendieck group sends every class to
# zero.  The booleans below record the exact algebraic implication being used.
empty_face: frozenset[Triangulation] = frozenset()
empty_is_initial = empty_face <= left_face
self_coproduct = left_face | left_face
self_coproduct_is_self = self_coproduct == left_face
unit_freeness_counterexample = self_coproduct_is_self
generator = Symbol("x")
group_completion_solutions = solve(
    Eq(generator + generator, generator), generator
)
group_completion_forces_generator_zero = group_completion_solutions == [0]
assert empty_is_initial
assert self_coproduct_is_self
assert unit_freeness_counterexample
assert group_completion_forces_generator_zero

# Independent enumeration control: no pair was assumed accidentally unique.
disjoint_triangulation_pairs = sum(
    1
    for left, right in combinations(triangulations, 2)
    if left.isdisjoint(right)
)
assert disjoint_triangulation_pairs > 0

packet = {
    "schema": (
        "marici.grothendieck.phase_i_face_coproduct_idempotence.v1"
    ),
    "demonstrated_strength": [
        "unbounded thin-category theorem",
        "exact finite n=8 witness",
    ],
    "compatibility_preflight": {
        "coefficient_domain": None,
        "coefficient_prime": None,
        "ambient_carrier_arity": 8,
        "source_category": "closed scalar face incidence poset",
        "morphisms": "face inclusions",
        "filtration_stage": "coefficient-neutral carrier incidence",
        "pole_depths": "not_applicable",
        "input_sha256": {rel(path): sha256(path) for path in inputs},
    },
    "finite_model": {
        "octagon_triangulation_count": len(triangulations),
        "diagonals_per_triangulation": len(left_fan),
        "left_fan": [list(diagonal) for diagonal in sorted(left_fan)],
        "right_fan": [list(diagonal) for diagonal in sorted(right_fan)],
        "common_diagonal_count": len(common_dissection),
        "disjoint_triangulation_pair_count": disjoint_triangulation_pairs,
        "geometric_union_cardinality": len(geometric_union),
        "categorical_join_cardinality": len(categorical_join),
        "join_support_excess": len(categorical_join) - len(geometric_union),
        "geometric_union_is_closed_face": geometric_union_is_closed_face,
        "empty_object_is_initial": empty_is_initial,
    },
    "categorical_theorem": {
        "poset_coproduct": "X_S join X_T = X_(S intersection T)",
        "self_coproduct": "X join X = X",
        "self_coproduct_is_self": self_coproduct_is_self,
        "all_positive_unit_powers_collapse": True,
        "additive_isomorphism_class_monoid": "idempotent join semilattice",
        "group_completion_relation": "[X]+[X]=[X] implies [X]=0",
        "group_completion_relation_solutions": [
            str(solution) for solution in group_completion_solutions
        ],
        "grothendieck_group": "zero_group",
    },
    "deliberate_failure": {
        "naive_claim": (
            "the established face-incidence coproduct is a "
            "multiplicity-sensitive disjoint union whose unit powers form N"
        ),
        "claim_holds": False,
        "required_distinction": "U coproduct U is not isomorphic to U",
        "observed_equality": "U coproduct U = U",
        "nonzero_obstruction": {
            "two_vertex_union_to_join_support_excess": (
                len(categorical_join) - len(geometric_union)
            )
        },
    },
    "scope_boundary": {
        "formal_finite_coproduct_completion_contradicted": False,
        "surface_disjoint_union_contradicted": False,
        "missing_proof": (
            "a coefficient-neutral multiplicity-bearing disjoint coproduct "
            "with injections and the universal mapping property"
        ),
        "import_risk": (
            "indexing a free completion by finite sets or lists supplies the "
            "natural-number multiplicity that Phase I is meant to derive"
        ),
    },
    "verdict": {
        "empty_object_derived_in_n8_incidence": True,
        "incidence_poset_coproduct_exists": True,
        "incidence_poset_coproduct_is_disjoint_union": False,
        "unbounded_unit_freeness": False,
        "initial_semiring_N_derived": False,
        "group_completion_Z_derived": False,
        "arithmetic_derived": False,
    },
    "deferred": [
        "formal finite-disjoint-coproduct completion",
        "source-derived coproduct injections and mapping property",
        "distributive carrier tensor",
        "unique additive decomposition",
        "Burnside/Witt operations",
        "Euler product",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
