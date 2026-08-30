"""Physical incidence of the eight soft-triangle endpoint nodes."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, p, kappa, xi, t = sp.symbols("x p kappa xi t", positive=False)
    y = p + x * kappa / 2
    z = p - x * kappa / 2
    energy = x + y + z
    c = -energy
    a = p * t
    b = energy + x * xi

    face_base = sp.factor(((y + z) ** 2 - x**2) * ((y - z) ** 2 - x**2))
    face_loop_b = sp.factor(((c + b) ** 2 - x**2) * ((c - b) ** 2 - x**2))
    face_loop_a = sp.factor(((c + a) ** 2 - y**2) * ((c - a) ** 2 - y**2))
    exceptional_loop_a = sp.factor(face_loop_a.subs(x, 0) / p**4)

    checks = {
        "base_interval": sp.factor(
            face_base - x**2 * (kappa**2 - 1) * (4 * p**2 - x**2)
        ) == 0,
        "xi_interval": sp.factor(
            face_loop_b
            - x**2
            * (xi**2 - 1)
            * (4 * p + x * xi + x)
            * (4 * p + x * xi + 3 * x)
        ) == 0,
        "t_interval": sp.factor(
            exceptional_loop_a - (t**2 - 1) * (t**2 - 9)
        ) == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    algebraic_nodes = []
    physical_nodes = []
    for epsilon in (-1, 1):
        for delta in (-1, 1):
            magnitude = 3 if epsilon * delta == 1 else 1
            for tau in (-magnitude, magnitude):
                marked = []
                if delta == -1:
                    marked.append("q_g1 soft-normal endpoint")
                if tau == 1:
                    marked.append("q_g2/q_g31 divided collision")
                if tau == -3:
                    marked.append("q_g3")
                node = {
                    "kappa": epsilon,
                    "xi": delta,
                    "t": tau,
                    "physical_positive_incidence": 1 <= tau <= 3,
                    "marked_support": marked,
                    "unmarked_boundary_count": 3 - len(marked),
                }
                algebraic_nodes.append(node)
                if node["physical_positive_incidence"]:
                    physical_nodes.append(node)

    assert len(algebraic_nodes) == 8
    assert len(physical_nodes) == 4
    assert sorted(len(node["marked_support"]) for node in physical_nodes) == [0, 1, 1, 2]

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-physical-node-incidence.v1",
        "exceptional_physical_ranges": {
            "kappa": "[-1,1]",
            "xi": "[-1,1]",
            "t": "[1,3]",
        },
        "face_initial_forms": {
            "base": "4*p^2*(kappa^2-1)",
            "loop_b": "16*p^2*(xi^2-1)",
            "loop_a": "(t^2-1)*(t^2-9)",
        },
        "algebraic_nodes": algebraic_nodes,
        "physical_nodes": physical_nodes,
        "physical_node_count": len(physical_nodes),
        "physical_local_milnor_rank_before_relations": len(physical_nodes),
        "marked_incidence_profile": [0, 1, 1, 2],
        "checks": checks,
        "status": "four_of_eight_nodes_meet_the_literal_positive_exceptional_current",
        "scope": (
            "support incidence only; no claim that the physical current has "
            "nonzero intersection number with each local vanishing cycle"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
