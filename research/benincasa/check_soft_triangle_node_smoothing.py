"""Source-derived higher-normal smoothing of the soft-triangle A1 nodes."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, p, kappa, xi, a = sp.symbols("x p kappa xi a")
    y = p + x * kappa / 2
    z = p - x * kappa / 2
    e = x + y + z
    b = e + x * xi
    x2, y2, z2, e2 = x**2, y**2, z**2, e**2
    h = x2 + y2 - z2

    f = x2 * a**4 - h * a**2 * b**2 + y2 * b**4
    g_a = h * (x2 + e2) - 2 * x2 * (y2 + e2)
    g_b = h * (y2 + e2) - 2 * y2 * (x2 + e2)
    h0 = z2 * ((e2 - y2) * (e2 - x2) + e2 * z2)
    pulled = sp.expand(f + g_a * a**2 + g_b * b**2 + h0)
    normalized = sp.cancel(pulled / x**2)
    k0 = sp.factor(normalized.subs(x, 0))
    k1 = sp.factor(sp.diff(normalized, x).subs(x, 0))
    k2 = sp.factor(sp.diff(normalized, x, 2).subs(x, 0) / 2)

    nodes = []
    for kap in (-1, 1):
        for xx in (-1, 1):
            magnitude = 3 if kap * xx == 1 else 1
            for tau in (-magnitude, magnitude):
                substitution = {kappa: kap, xi: xx, a: p * tau}
                leading = sp.factor(k0.subs(substitution))
                first = sp.factor(k1.subs(substitution))
                second = sp.factor(k2.subs(substitution))
                assert leading == 0
                order = 1 if first != 0 else (2 if second != 0 else None)
                nodes.append({
                    "kappa": kap,
                    "xi": xx,
                    "t": tau,
                    "physical_positive_incidence": tau > 0,
                    "first_normal_smoothing": str(first),
                    "second_normal_smoothing": str(second),
                    "first_nonzero_normal_order": order,
                })

    physical = [node for node in nodes if node["physical_positive_incidence"]]
    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-node-smoothing.v1",
        "exceptional_kernel": str(k0),
        "first_normal_kernel": str(k1),
        "second_normal_kernel": str(k2),
        "nodes": nodes,
        "physical_nodes": physical,
        "physical_first_order_nonzero_count": sum(
            node["first_nonzero_normal_order"] == 1 for node in physical
        ),
        "physical_second_order_first_count": sum(
            node["first_nonzero_normal_order"] == 2 for node in physical
        ),
        "status": "source_higher_normal_orders_evaluated_at_all_endpoint_nodes",
        "scope": (
            "normal smoothing coefficients only; Picard-Lefschetz signs require "
            "the oriented local comparison and square-root normalization"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
