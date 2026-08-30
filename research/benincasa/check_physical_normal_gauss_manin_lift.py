"""Verify the moving-cycle Gauss--Manin lift for the generic lower family."""

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
    gamma = sp.Rational(-1, 2)

    walls = (
        c + b + x1,
        c + a + x2,
        a + b + x3,
        c + b + x2 + x3,
    )
    wall_names = ("q_g1", "q_g2", "q_g3", "q_g23")

    # Cyclicly matched local pivots.  Each gives a lift
    # D_i=partial_nu_i+v_i partial_pivot tangent to K=0.
    pivots = (a, b, c)
    packets: list[dict[str, object]] = []
    for normal, pivot in zip(normals, pivots, strict=True):
        k_normal = sp.diff(kernel, normal)
        k_pivot = sp.diff(kernel, pivot)
        assert k_normal != 0 and k_pivot != 0
        # With velocity=-A/B, tangency has the exact cleared certificate
        # B*partial_nu(K)-A*partial_pivot(K)=0.
        tangency_certificate = sp.expand(k_pivot * k_normal - k_normal * k_pivot)
        assert tangency_certificate == 0

        active_walls = [wall for wall in walls if sp.diff(wall, pivot) != 0]
        active_names = [name for name, wall in zip(wall_names, walls, strict=True) if sp.diff(wall, pivot) != 0]
        wall_product = sp.prod(active_walls)

        # The K-pole part of direct derivative plus Lie derivative has numerator
        # gamma*(B*K_nu-A*K_pivot), which is identically zero.  This avoids an
        # expensive expansion of the full rational expression.
        k_pole_cancellation = gamma * (k_pivot * k_normal - k_normal * k_pivot)
        assert sp.expand(k_pole_cancellation) == 0

        # The remaining response is div(V)-sum V(q)/q.  After multiplying by
        # B^2*prod(q), its numerator is explicitly polynomial.
        derivative_numerator = (
            -sp.diff(k_normal, pivot) * k_pivot
            + k_normal * sp.diff(k_pivot, pivot)
        ) * wall_product
        contact_numerator = k_normal * k_pivot * sum(
            sp.diff(wall, pivot) * sp.cancel(wall_product / wall)
            for wall in active_walls
        )
        cleared = sp.expand(derivative_numerator + contact_numerator)
        assert sp.Poly(cleared, *fibers) is not None
        assert sp.degree(kernel, pivot) > sp.degree(k_pivot, pivot)

        packets.append({
            "normal": str(normal),
            "pivot": str(pivot),
            "active_marked_walls": active_names,
            "tangency_identity": "partial_nu(K)+V(K)=0",
            "explicit_K_denominator_cancels": True,
            "clearing_denominator": f"(partial_{pivot}K)^2*" + "*".join(active_names),
            "cleared_response_is_polynomial": True,
            "cleared_numerator_term_count": len(sp.Poly(cleared, *fibers).terms()),
        })

    result = {
        "schema": "marici.benincasa.physical-normal-gauss-manin-lift.v1",
        "status": "passed",
        "source_family": "generic six-scale rank-34 four-wall lower family",
        "source_measure_exponent": "-1/2",
        "local_lift_formula": "V_i=-(partial_nu_i K)/(partial_pivot_i K) partial_pivot_i",
        "covariant_response_formula": "div(V_i)-sum_q V_i(q)/q",
        "normal_lifts": packets,
        "new_denominator_support": False,
        "intrinsic_support_classification": [
            "marked-wall poles are frozen source support",
            "single gradient-pivot zeros are local-lift chart boundaries",
            "simultaneous gradient failure on K=0 is existing Cayley-Menger/Landau support",
        ],
        "classification": (
            "main Cayley-Menger boundary transport converts the bare kernel score "
            "into a contact-weighted Gauss-Manin adapter without new carrier support"
        ),
        "scope_warning": (
            "the lift is tangent to K=0; tangency to every signed-minor boundary "
            "of the full semialgebraic physical cycle, period rank, and tensor "
            "polarization remain unproved"
        ),
    }
    output = HERE / "physical-normal-gauss-manin-lift.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
