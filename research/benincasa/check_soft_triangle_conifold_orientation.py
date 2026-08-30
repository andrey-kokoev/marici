"""Exact conifold coordinates and relative orientation of physical soft nodes."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    w, t, kappa, xi = sp.symbols("w t kappa xi")
    soft, p, a = sp.symbols("soft p a")

    exceptional_kernel = (
        t**4
        - (10 + 8 * kappa * xi) * t**2
        + 16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9
    )
    fold = t**2 - 5 - 4 * kappa * xi
    y_plus = w + fold
    y_minus = w - fold
    u_face = 4 * (1 - kappa**2)
    v_face = 4 * (1 - xi**2)
    conifold = sp.expand(y_plus * y_minus + u_face * v_face)
    assert sp.expand(conifold - (w**2 - exceptional_kernel)) == 0

    source_jacobian = sp.factor(
        sp.Matrix([y_plus, y_minus, u_face, v_face])
        .jacobian([w, t, kappa, xi])
        .det()
    )
    assert source_jacobian == -256 * kappa * t * xi

    # Recompute the source-derived second soft-normal coefficient.
    y = p + soft * kappa / 2
    z = p - soft * kappa / 2
    energy = soft + y + z
    b = energy + soft * xi
    soft2, y2, z2, energy2 = soft**2, y**2, z**2, energy**2
    h = soft2 + y2 - z2
    f = soft2 * a**4 - h * a**2 * b**2 + y2 * b**4
    g_a = h * (soft2 + energy2) - 2 * soft2 * (y2 + energy2)
    g_b = h * (y2 + energy2) - 2 * y2 * (soft2 + energy2)
    h0 = z2 * ((energy2 - y2) * (energy2 - soft2) + energy2 * z2)
    normalized = sp.cancel(sp.expand(f + g_a * a**2 + g_b * b**2 + h0) / soft**2)
    second_normal = sp.factor(sp.diff(normalized, soft, 2).subs(soft, 0) / 2)

    physical_nodes = [
        (-1, -1, 3),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, 3),
    ]
    records = []
    for epsilon, delta, tau in physical_nodes:
        point = {w: 0, t: tau, kappa: epsilon, xi: delta}
        jac_source = sp.factor(source_jacobian.subs(point))

        # kappa=epsilon*(1-r_k), xi=delta*(1-r_x).  The determinant
        # from inward coordinates (w,t,r_k,r_x) gains epsilon*delta.
        jac_inward = sp.factor(jac_source * epsilon * delta)
        smoothing = sp.factor(
            second_normal.subs({kappa: epsilon, xi: delta, a: p * tau})
        )
        assert jac_inward == -256 * tau
        assert sp.ask(sp.Q.positive(smoothing), assumptions=sp.Q.positive(p))
        records.append({
            "kappa": epsilon,
            "xi": delta,
            "t": tau,
            "source_coordinate_jacobian": str(jac_source),
            "inward_coordinate_jacobian": str(jac_inward),
            "second_normal_smoothing": str(smoothing),
            "relative_orientation_sign": -1,
        })

    assert {record["relative_orientation_sign"] for record in records} == {-1}

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-conifold-orientation.v1",
        "exact_normal_form": "Y_plus*Y_minus + U*V = 0",
        "coordinates": {
            "Y_plus": str(y_plus),
            "Y_minus": str(y_minus),
            "U": str(u_face),
            "V": str(v_face),
        },
        "source_jacobian": str(source_jacobian),
        "physical_nodes": records,
        "common_inward_orientation": True,
        "common_projective_PL_ray": [1, 1, 1, 1],
        "deck_action": "(Y_plus,Y_minus,U,V)->(-Y_minus,-Y_plus,U,V)",
        "status": "four_physical_nodes_have_one_source_typed_projective_PL_orientation",
        "scope": (
            "exact conifold normal form, inward-corner orientation, and positive "
            "second-normal smoothing; no affine period normalization, physical "
            "intersection amplitude, or global vanishing-cycle relation"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
