"""Exact audit of the maximal D4-abelianized rig-groupoid candidate."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OBSTRUCTION = ROOT / "research/nima/results/phase-i-unit-automorphism-obstruction.json"
OUT = ROOT / "research/nima/results/phase-i-abelianized-rig-groupoid.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


obstruction = json.loads(OBSTRUCTION.read_text(encoding="utf-8"))
assert obstruction["verdict"]["lift_with_U_as_unit_on_full_D4_groupoid_exists"] is False

Permutation = tuple[int, ...]
identity: Permutation = (0, 1, 2, 3)
rotation: Permutation = (1, 2, 3, 0)
reflection: Permutation = (0, 3, 2, 1)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(4))


def inverse(value: Permutation) -> Permutation:
    result = [0] * 4
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def closure(generators: tuple[Permutation, ...]) -> set[Permutation]:
    group = {identity}
    changed = True
    while changed:
        changed = False
        for left in tuple(group):
            for right in generators + tuple(group):
                value = compose(left, right)
                if value not in group:
                    group.add(value)
                    changed = True
    return group


d4 = closure((rotation, reflection))
commutators = {
    compose(compose(compose(left, right), inverse(left)), inverse(right))
    for left, right in itertools.product(d4, repeat=2)
}
commutator_subgroup = closure(tuple(commutators))
assert len(d4) == 8
assert len(commutator_subgroup) == 2


def coset(value: Permutation) -> frozenset[Permutation]:
    return frozenset(compose(value, member) for member in commutator_subgroup)


quotient = {coset(value) for value in d4}
assert len(quotient) == 4


def quotient_product(left: frozenset[Permutation], right: frozenset[Permutation]) -> frozenset[Permutation]:
    return coset(compose(next(iter(left)), next(iter(right))))


assert all(
    quotient_product(left, right) == quotient_product(right, left)
    for left, right in itertools.product(quotient, repeat=2)
)

# A small exact control of the G-labelled finite-set rig. A morphism label is
# a tuple in the abelian quotient; tensor labels are pairwise products.
labels = tuple(sorted(quotient, key=lambda item: sorted(item)))


def tensor_labels(left: tuple[frozenset[Permutation], ...], right: tuple[frozenset[Permutation], ...]):
    return tuple(quotient_product(a, b) for a in left for b in right)


words = tuple(itertools.product(labels, repeat=2))
assert all(len(tensor_labels(left, right)) == len(left) * len(right) for left in words for right in words)
assert all(
    tensor_labels(left, right)
    == tuple(tensor_labels(right, left)[index] for index in (0, 2, 1, 3))
    for left in words
    for right in words
)

# Interchange on labels, the only new condition beyond finite-set bijection
# functoriality.
interchange_checks = 0
for g1, g2, h1, h2 in itertools.product(labels, repeat=4):
    left = quotient_product(quotient_product(g1, g2), quotient_product(h1, h2))
    right = quotient_product(quotient_product(g1, h1), quotient_product(g2, h2))
    assert left == right
    interchange_checks += 1

out = {
    "schema": "marici.nima.phase_i_abelianized_rig_groupoid.v1",
    "status": "exact_algebraic_candidate_not_physically_authorized",
    "input_sha256": {str(OBSTRUCTION.relative_to(ROOT)).replace("\\", "/"): digest(OBSTRUCTION)},
    "unit_automorphisms": {
        "source_group": "D4",
        "source_order": len(d4),
        "commutator_subgroup_order": len(commutator_subgroup),
        "maximal_abelian_quotient": "C2 x C2",
        "quotient_order": len(quotient),
    },
    "rig_groupoid": {
        "objects": "finite U-component sets",
        "morphisms": "bijections labelled by D4_ab on components",
        "addition": "disjoint union",
        "multiplication": "cartesian product with pairwise label product",
        "pi0": "initial semiring",
        "interchange_checks": interchange_checks,
    },
    "verdict": {
        "maximal_unit_compatible_automorphism_quotient_derived": True,
        "abelianized_rig_groupoid_exists": True,
        "quotient_is_physical_realization": False,
        "full_D4_information_retained": False,
        "burnside_witt_physically_derived": False,
    },
    "next_gate": "test whether every declared sector coefficient/readout factors through D4_ab",
}

OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
