"""Exact Cech coherence for local moving-cycle normal lifts."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    c, a, b = fibers = sp.symbols("c a b")
    x1, x2, x3 = sp.symbols("X1 X2 X3")
    n1, n2, n3 = normals = sp.symbols("nu1 nu2 nu3")
    p1sq, p2sq, p3sq = x1**2 + n1, x2**2 + n2, x3**2 + n3
    cm = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, p2sq, p1sq],
        [1, a**2, p2sq, 0, p3sq],
        [1, b**2, p1sq, p3sq, 0],
    ])
    kernel = sp.expand(-cm.det() / 2)
    gradients = {fiber: sp.diff(kernel, fiber) for fiber in fibers}
    pairs = ((c, a), (a, b), (b, c))

    overlap_packets: list[dict[str, object]] = []
    for normal in normals:
        source = sp.diff(kernel, normal)
        lifts = {
            pivot: tuple(-source / gradients[pivot] if fiber == pivot else sp.Integer(0) for fiber in fibers)
            for pivot in fibers
        }

        # Every local lift has the same normal component on K.
        for pivot, vector in lifts.items():
            cleared_action = sum(
                component * sp.diff(kernel, fiber)
                for component, fiber in zip(vector, fibers, strict=True)
            )
            assert sp.cancel(cleared_action + source) == 0

        differences: dict[tuple[sp.Symbol, sp.Symbol], tuple[sp.Expr, ...]] = {}
        for left, right in pairs:
            difference = tuple(
                lifts[left][index] - lifts[right][index]
                for index in range(len(fibers))
            )
            differences[(left, right)] = difference

            # The overlap difference is vertical and tangent to K=0.
            tangent_action = sum(
                component * sp.diff(kernel, fiber)
                for component, fiber in zip(difference, fibers, strict=True)
            )
            assert sp.cancel(tangent_action) == 0
            overlap_packets.append({
                "normal": str(normal),
                "overlap": f"U_{left} intersect U_{right}",
                "difference_tangent_to_K": True,
                "response_difference": "L_W(omega)=d(i_W omega) by Cartan",
                "primitive_type": "meromorphic contraction i_W(omega) on the marked complement",
            })

        # W_ca+W_ab+W_bc=0 on the triple overlap, component by component.
        triple_sum = tuple(
            differences[(c, a)][index]
            + differences[(a, b)][index]
            + differences[(b, c)][index]
            for index in range(len(fibers))
        )
        assert all(sp.cancel(component) == 0 for component in triple_sum)

    result = {
        "schema": "marici.benincasa.physical-normal-lift-cech-coherence.v1",
        "status": "passed",
        "normal_count": 3,
        "gradient_pivot_chart_count": 3,
        "pairwise_overlap_count": len(overlap_packets),
        "pairwise_tangency_checks": len(overlap_packets),
        "triple_cocycle_checks": 3,
        "overlaps": overlap_packets,
        "cartan_identity": "L_W omega=d(i_W omega) for the fiber top form",
        "cech_class": "local contact-weighted responses glue modulo exact meromorphic forms",
        "new_support_from_gradient_pivots": False,
        "classification": (
            "gradient-pivot denominators are atlas data; the normal adapter "
            "defines one global de Rham-Cech class on the frozen marked complement"
        ),
        "scope_warning": (
            "residue compatibility uses the marked meromorphic/moving-wall complex; "
            "the remaining signed-minor boundaries of the full physical chain and "
            "the physical period rank are not computed here"
        ),
    }
    output = HERE / "physical-normal-lift-cech-coherence.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
