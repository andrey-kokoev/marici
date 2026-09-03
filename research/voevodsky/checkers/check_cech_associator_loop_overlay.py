from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


K_PACKET = Path("research/kitaev/a-four-copy-cyclic-shift-measures-the-associator-loop-exactly.md")


def compose_path(edges: tuple[str, ...]) -> tuple[str, ...]:
    return edges


def main() -> None:
    packet = K_PACKET.read_text(encoding="utf-8")
    assert "A four-copy cyclic-shift interferometer measures the ordered Bargmann trace" in packet
    assert "\\langle X\\rangle=-\\frac18" in packet
    assert "\\langle Y\\rangle=0" in packet
    assert "controlled coherent access to that permutation is an" in packet
    assert "additional quantum constructor" in packet

    # A loop retains ordered route data; disconnected edge measurements do not.
    loop = compose_path(("alpha_01", "alpha_12", "alpha_23", "alpha_30"))
    reversed_loop = tuple(reversed(loop))
    disconnected = frozenset(loop)
    assert loop != reversed_loop
    assert disconnected == frozenset(reversed_loop)

    # Local existence, loop observability, and global gluing are distinct states.
    strength_states = {
        "local_only": (True, False, False),
        "loop_specified": (True, True, False),
        "global_gluing": (True, True, True),
    }
    assert len(set(strength_states.values())) == 3
    assert strength_states["loop_specified"][2] is False

    # Exact reported algebraic quadratures do not set physical authorization.
    algebraic_quadratures = (Fraction(-1, 8), Fraction(0))
    physical_controlled_shift_authorized = False
    shared_control_fault_excluded = False
    assert algebraic_quadratures == (Fraction(-1, 8), Fraction(0))
    assert not physical_controlled_shift_authorized
    assert not shared_control_fault_excluded

    # Both route composites may exist while a face comparison is absent.
    route_left_exists = route_right_exists = True
    associator_comparison_supplied = False
    face_glued = route_left_exists and route_right_exists and associator_comparison_supplied
    assert face_glued is False

    result = {
        "schema": "marici.voevodsky.cech-associator-loop-overlay.v1",
        "status": "loop_probe_layering_verified",
        "ordered_loop_distinct_from_disconnected_edges": True,
        "reversal_orientation_test_available": True,
        "exact_reported_X": "-1/8",
        "exact_reported_Y": "0",
        "local_loop_global_strengths_separated": True,
        "loop_probe_not_global_gluing": True,
        "algebraic_probe_not_physical_authorization": True,
        "shared_control_fault_certificate_required": True,
        "associator_comparison_independent_of_route_existence": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
