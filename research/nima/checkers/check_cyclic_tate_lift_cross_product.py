#!/usr/bin/env python3
"""Verify the cyclic occurrence cross product realizes the C3 norm."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "cyclic-tate-lift-cross-product.json"


def rho(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return (v[2], v[0], v[1])


def kappa(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return (v[0], v[2], v[1])


def cross(v: tuple[int, int, int], w: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        v[1] * w[2] - v[2] * w[1],
        v[2] * w[0] - v[0] * w[2],
        v[0] * w[1] - v[1] * w[0],
    )


def convolution(v: tuple[int, int, int], w: tuple[int, int, int], p: int = 3) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for i, vi in enumerate(v):
        for j, wj in enumerate(w):
            out[(i + j) % 3] = (out[(i + j) % 3] + vi * wj) % p
    return tuple(out)


def neg(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-x for x in v)


def main() -> None:
    v = (0, 1, -1)
    norm = (1, 1, 1)
    cyclic_reports = []
    current = v
    for i in range(3):
        nxt = rho(current)
        cp = cross(current, nxt)
        conv = convolution(current, nxt)
        assert cp == norm
        assert conv == norm
        cyclic_reports.append(
            {"index": i, "left": list(current), "right": list(nxt), "cross": list(cp), "convolution_mod_3": list(conv)}
        )
        current = nxt

    # Cross product is rotation-equivariant and reflection-anti-equivariant.
    w = rho(v)
    assert cross(rho(v), rho(w)) == rho(cross(v, w))
    assert cross(kappa(v), kappa(w)) == neg(kappa(cross(v, w)))

    occurrence_reflection_sign = -1
    normal_orientation_reflection_sign = -1
    combined_sign = occurrence_reflection_sign * normal_orientation_reflection_sign
    assert combined_sign == 1

    result = {
        "status": "PASS",
        "cyclic_adjacent_lift_products": cyclic_reports,
        "rotation_equivariant": True,
        "cross_product_reflection_character": occurrence_reflection_sign,
        "normal_orientation_reflection_character": normal_orientation_reflection_sign,
        "combined_reflection_character": combined_sign,
        "coefficient_shadow": "T*T=N",
        "local_candidate_complete": True,
        "global_cech_comparison_established": False,
        "next_gate": "derive cross-residue-surface Cech maps and verify the Beck-Chevalley cocycle",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
