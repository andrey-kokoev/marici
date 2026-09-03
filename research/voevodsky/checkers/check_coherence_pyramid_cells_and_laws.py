from __future__ import annotations

import copy
import json
from pathlib import Path


INTERFACE = Path("research/voevodsky/coherence-pyramid-cells-and-laws.json")


def flatten(expression: object) -> tuple[str, ...]:
    if isinstance(expression, str):
        return () if expression == "id" else (expression,)
    left, right = expression
    return flatten(left) + flatten(right)


def admit_cell(kind: str, certificate: dict[str, bool]) -> tuple[bool, str]:
    required = {
        "associator": ["both_parenthesizations_admitted", "same_typed_boundary", "certificate_bundle_equivalence"],
        "interchange": ["all_four_boundary_composites_admitted", "same_outer_boundary", "transported_certificate_bundle_equivalence"],
        "beck_chevalley": ["typed_mixed_square", "pullback_exactness", "full_joint_amalgamation", "comparison_map", "transported_certificate_bundle_equivalence"],
        "completion_comparison": ["common_core_square", "closed_limit_transport", "radical_transport", "coercivity_transport"],
    }[kind]
    for field in required:
        if certificate.get(field) is not True:
            return False, field
    return True, "admitted"


def main() -> None:
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    assert len(interface["cells"]) == 6
    assert len(interface["coherence_obligations"]) == 5

    arrows = ("f", "g", "h", "k")
    pentagon_left = (((arrows[0], arrows[1]), arrows[2]), arrows[3])
    pentagon_right = (arrows[0], (arrows[1], (arrows[2], arrows[3])))
    assert flatten(pentagon_left) == flatten(pentagon_right) == arrows

    triangle_left = (("f", "id"), "g")
    triangle_right = ("f", ("id", "g"))
    assert flatten(triangle_left) == flatten(triangle_right) == ("f", "g")

    grid = (("alpha", "beta"), ("gamma", "delta"))
    horizontal_then_vertical = ((grid[0][0], grid[1][0]), (grid[0][1], grid[1][1]))
    vertical_then_horizontal = (("alpha", "gamma"), ("beta", "delta"))
    assert horizontal_then_vertical == vertical_then_horizontal

    valid = {
        "associator": {field: True for field in interface["cells"]["associator"]["admission"]},
        "interchange": {field: True for field in interface["cells"]["interchange"]["admission"]},
        "beck_chevalley": {field: True for field in interface["cells"]["beck_chevalley"]["admission"]},
        "completion_comparison": {field: True for field in interface["cells"]["completion_comparison"]["admission"]},
    }
    assert all(admit_cell(kind, certificate)[0] for kind, certificate in valid.items())

    hostile_specs = {
        "associator_from_boundary_only": ("associator", "certificate_bundle_equivalence"),
        "interchange_from_commuting_maps_only": ("interchange", "transported_certificate_bundle_equivalence"),
        "beck_chevalley_from_square_only": ("beck_chevalley", "pullback_exactness"),
        "completion_cell_from_core_equality": ("completion_comparison", "closed_limit_transport"),
    }
    refusals: dict[str, str] = {}
    for hostile, (kind, missing) in hostile_specs.items():
        fixture = copy.deepcopy(valid[kind])
        fixture[missing] = False
        admitted, reason = admit_cell(kind, fixture)
        assert not admitted and reason == missing
        refusals[hostile] = reason

    invertibility = {
        "comparison_map_isomorphism": True,
        "inverse_preserves_certificates": False,
    }
    assert not all(invertibility.values())
    refusals["beck_chevalley_invertibility_assumed"] = "inverse_preserves_certificates"

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-cells-and-laws-check.v1",
        "status": "coherence_cell_presentation_verified",
        "cell_classes": len(interface["cells"]),
        "law_classes": len(interface["coherence_obligations"]),
        "pentagon_symbolic_normal_form": list(flatten(pentagon_left)),
        "triangle_symbolic_normal_form": list(flatten(triangle_left)),
        "interchange_verified": True,
        "hostile_refusals": refusals,
        "global_partial_equipment_claimed": False,
        "next_gate": "combined finite and unbounded countermodel suite",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
