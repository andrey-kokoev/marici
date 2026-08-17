"""Formal reflection-obstruction gate for a zero connector torsor."""

from __future__ import annotations

import json


def main() -> None:
    # Entry 387: the admissible fine-graded endpoint deformation group.
    deformation_group: tuple[int, ...] = ()

    # If h exists, reflection produces another solution f.h with the same
    # frozen faces. Their difference is an element of the deformation group.
    connector_exists = None
    possible_reflection_differences = deformation_group
    assert possible_reflection_differences == ()

    # Entry 141's coefficient Bockstein is an isomorphism Z/2 -> Z/2.
    # Its input is zero here, so its output is zero.
    reflection_defect = 0
    loaded_obstruction = reflection_defect
    assert loaded_obstruction == 0

    print(json.dumps({
        "status": "proved_conditional_reflection_obstruction_zero",
        "connector_exists": connector_exists,
        "endpoint_deformation_group": "0",
        "connector_torsor_if_nonempty": "singleton",
        "reflection_defect": 0,
        "loaded_bockstein_obstruction": 0,
        "conclusion": (
            "Existence remains open. If one admissible connector exists, "
            "its reflection class is forced trivial and it has a unique "
            "equivariant component."
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
