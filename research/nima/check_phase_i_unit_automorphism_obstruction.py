"""Exact D4 certificate obstructing a lift of pi_0 multiplication to the Carrier groupoid."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEMIRING = ROOT / "research/nima/results/phase-i-endomorphism-semiring.json"
ASSEMBLY = ROOT / "research/grothendieck/results/phase-i-unmarked-assembly-obstruction.json"
OUT = ROOT / "research/nima/results/phase-i-unit-automorphism-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


semiring = json.loads(SEMIRING.read_text(encoding="utf-8"))
assembly = json.loads(ASSEMBLY.read_text(encoding="utf-8"))
assert semiring["verdict"]["conditional_initial_semiring_on_pi0_derived"] is True
assert assembly["finite_model"]["dihedral_group_order"] == 8

Permutation = tuple[int, ...]


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


identity: Permutation = (0, 1, 2, 3)
rotation: Permutation = (1, 2, 3, 0)
reflection: Permutation = (0, 3, 2, 1)


def closure(generators: tuple[Permutation, ...]) -> set[Permutation]:
    group = {identity}
    changed = True
    while changed:
        changed = False
        for left in tuple(group):
            for right in generators + tuple(group):
                product = compose(left, right)
                if product not in group:
                    group.add(product)
                    changed = True
    return group


d4 = closure((rotation, reflection))
assert len(d4) == 8
rs = compose(rotation, reflection)
sr = compose(reflection, rotation)
assert rs != sr

# If a bifunctor tensor had U as two-sided unit, functoriality on the commuting
# arrows (r,id) and (id,s) in Aut(U)xAut(U) would force their images r and s
# in Aut(U) to commute. The explicit D4 pair falsifies that necessary law.
left_product_pair = ((rotation, identity), (identity, reflection))
right_product_pair = ((identity, reflection), (rotation, identity))
assert (
    compose(left_product_pair[0][0], left_product_pair[1][0]),
    compose(left_product_pair[0][1], left_product_pair[1][1]),
) == (
    compose(right_product_pair[0][0], right_product_pair[1][0]),
    compose(right_product_pair[0][1], right_product_pair[1][1]),
)

out = {
    "schema": "marici.nima.phase_i_unit_automorphism_obstruction.v1",
    "status": "exact_finite_no_go",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in (SEMIRING, ASSEMBLY)
    },
    "carrier_unit_candidate": "cyclic quadrilateral U with source relabelling D4",
    "finite_certificate": {
        "automorphism_group_order": len(d4),
        "rotation": rotation,
        "reflection": reflection,
        "rotation_after_reflection": rs,
        "reflection_after_rotation": sr,
        "commute": False,
    },
    "necessary_law": (
        "automorphisms of a monoidal unit commute; equivalently, functoriality "
        "of tensor sends the commuting source arrows (r,id) and (id,s) to "
        "commuting arrows r and s"
    ),
    "verdict": {
        "pi0_initial_semiring_refuted": False,
        "lift_with_U_as_unit_on_full_D4_groupoid_exists": False,
        "component_permutation_quotient_may_lift": True,
        "burnside_witt_from_full_carrier_derived": False,
    },
    "next_gate": (
        "Any power/Witt construction must either retain the D4 automorphisms "
        "in a higher coherent object or declare and justify a quotient to the "
        "component-permutation groupoid."
    ),
}

OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
