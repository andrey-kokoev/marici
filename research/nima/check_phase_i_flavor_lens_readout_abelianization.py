"""Exact flavor test separating commutator-sensitive lens from invariant readout."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FLAVOR = ROOT / "research/flavor/results/nine_link_exact_checks.json"
RIG = ROOT / "research/nima/results/phase-i-abelianized-rig-groupoid.json"
OUT = ROOT / "research/nima/results/phase-i-flavor-lens-readout-abelianization.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


flavor = json.loads(FLAVOR.read_text(encoding="utf-8"))["checks"]
rig = json.loads(RIG.read_text(encoding="utf-8"))
assert rig["verdict"]["abelianized_rig_groupoid_exists"] is True

Permutation = tuple[int, ...]
identity: Permutation = (0, 1, 2)
cycle: Permutation = (1, 2, 0)
transposition: Permutation = (1, 0, 2)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(3))


def inverse(value: Permutation) -> Permutation:
    result = [0] * 3
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


s3 = closure((cycle, transposition))
commutators = {
    compose(compose(compose(left, right), inverse(left)), inverse(right))
    for left, right in itertools.product(s3, repeat=2)
}
commutator_subgroup = closure(tuple(commutators))
assert len(s3) == 6
assert len(commutator_subgroup) == 3
assert cycle in commutator_subgroup

# The exact source transport uses this row cycle and moves row labels, hence
# the sparse chart action is nontrivial on the commutator subgroup.
transport = flavor["s3_cubed_permutation_transport"]
assert "rows cycled 1->2->3->1" in transport["permutation"]
assert transport["holonomy_ratio_new_over_old"] == "1"
assert cycle != identity

# The exact weak-basis audit leaves every listed physical invariant fixed,
# even for a larger nonpermutation U(3) transformation.
rotation = flavor["u3q_rotation"]
symbolic_invariants = rotation["symbolic_invariants_equal"]
concrete_invariants = rotation["concrete_invariants_equal"]
assert all(symbolic_invariants.values())
assert all(concrete_invariants.values())
assert rotation["zero_pattern_destroyed"] is True
assert rotation["phase_changed_under_rotation"] is True

out = {
    "schema": "marici.nima.phase_i_flavor_lens_readout_abelianization.v1",
    "status": "exact_cross_sector_typing_result",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in (FLAVOR, RIG)
    },
    "flavor_symmetry": {
        "factor_group": "S3",
        "group_order": len(s3),
        "commutator_subgroup": "A3",
        "commutator_order": len(commutator_subgroup),
        "source_row_cycle_lies_in_commutator": True,
    },
    "coefficient_lens": {
        "sparse_support_moved_by_commutator": True,
        "holonomy_transported_exactly": True,
        "factors_through_S3_abelianization": False,
    },
    "physical_readout": {
        "all_exact_weak_basis_invariants_preserved": True,
        "sparse_pattern_destroyed_by_larger_gauge_move": True,
        "factors_through_weak_basis_quotient": True,
    },
    "verdict": {
        "all_coefficient_lenses_must_factor_through_arithmetic_abelianization": False,
        "physical_readout_may_factor_through_arithmetic_abelianization": True,
        "abelianized_rig_is_universal_coefficient_object": False,
        "abelianized_rig_remains_candidate_readout_shadow": True,
    },
}

OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
