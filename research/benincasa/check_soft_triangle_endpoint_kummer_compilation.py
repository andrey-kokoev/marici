"""Compile the soft-triangle exceptional quartic from endpoint Kummer covers."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    u, v, a, p, A = sp.symbols("u v a p A", nonzero=True)
    kappa = (u + 1 / u) / 2
    xi = (v + 1 / v) / 2
    delta_kappa = (u - 1 / u) / 2
    delta_xi = (v - 1 / v) / 2
    delta = sp.factor(delta_kappa * delta_xi)

    k_exc_A = sp.expand(
        A**2
        - (10 + 8 * kappa * xi) * p**2 * A
        + (16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9) * p**4
    )
    root_uv = sp.factor(p**2 * (5 + 2 * (u * v + 1 / (u * v))))
    root_u_over_v = sp.factor(p**2 * (5 + 2 * (u / v + v / u)))
    compiled = sp.factor((A - root_uv) * (A - root_u_over_v))

    identities = {
        "kappa_endpoint_cover": sp.factor(delta_kappa**2 - (kappa**2 - 1)) == 0,
        "xi_endpoint_cover": sp.factor(delta_xi**2 - (xi**2 - 1)) == 0,
        "plus_combination_is_uv": sp.factor(
            kappa * xi + delta - (u * v + 1 / (u * v)) / 2
        ) == 0,
        "minus_combination_is_u_over_v": sp.factor(
            kappa * xi - delta - (u / v + v / u) / 2
        ) == 0,
        "quartic_compiles_exactly": sp.factor(k_exc_A - compiled) == 0,
    }

    def transform(expr, replacement):
        return sp.factor(expr.subs(replacement, simultaneous=True))

    deck = {
        "u_inverse": {
            "root_uv_image": str(transform(root_uv, {u: 1 / u})),
            "root_u_over_v_image": str(transform(root_u_over_v, {u: 1 / u})),
            "swaps_roots": (
                sp.factor(transform(root_uv, {u: 1 / u}) - root_u_over_v) == 0
                and sp.factor(transform(root_u_over_v, {u: 1 / u}) - root_uv) == 0
            ),
        },
        "v_inverse": {
            "root_uv_image": str(transform(root_uv, {v: 1 / v})),
            "root_u_over_v_image": str(transform(root_u_over_v, {v: 1 / v})),
            "swaps_roots": (
                sp.factor(transform(root_uv, {v: 1 / v}) - root_u_over_v) == 0
                and sp.factor(transform(root_u_over_v, {v: 1 / v}) - root_uv) == 0
            ),
        },
        "simultaneous_inverse": {
            "preserves_each_root": (
                sp.factor(transform(root_uv, {u: 1 / u, v: 1 / v}) - root_uv) == 0
                and sp.factor(
                    transform(root_u_over_v, {u: 1 / u, v: 1 / v})
                    - root_u_over_v
                ) == 0
            ),
        },
    }
    identities["deck_action_closes_on_two_roots"] = all(
        packet.get("swaps_roots", packet.get("preserves_each_root", False))
        for packet in deck.values()
    )
    if not all(identities.values()):
        raise AssertionError({name: value for name, value in identities.items() if not value})

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-endpoint-kummer-compilation.v1",
        "endpoint_covers": {
            "kappa": "(u+u^-1)/2",
            "xi": "(v+v^-1)/2",
            "branch_support": ["kappa=1", "kappa=-1", "xi=1", "xi=-1"],
        },
        "a_squared_roots": {
            "uv": str(root_uv),
            "u_over_v": str(root_u_over_v),
        },
        "compiled_factorization": str(compiled),
        "deck_action": deck,
        "checks": identities,
        "status": "exceptional_branch_system_compiled_from_existing_endpoint_kummer_covers",
        "scope": (
            "algebraic branch cover only; marked relative cohomology, "
            "Gauss-Manin extension, integral lattice, and physical periods remain uncomputed"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
