"""Exact normal lifts at the three Cayley--Menger distance endpoints."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    c, a, b = fibers = sp.symbols("c a b")
    p1, p2, p3 = sp.symbols("P1 P2 P3", positive=True)
    n1, n2, n3 = normals = sp.symbols("nu1 nu2 nu3")
    lengths = tuple(sp.sqrt(p**2 + normal) for p, normal in zip((p1, p2, p3), normals, strict=True))
    s1, s2, s3 = (length**2 for length in lengths)

    cm = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, s2, s1],
        [1, a**2, s2, 0, s3],
        [1, b**2, s1, s3, 0],
    ])
    kernel = sp.expand(-cm.det() / 2)
    zero_normals = {normal: 0 for normal in normals}

    # A zero loop distance identifies the loop point with the corresponding
    # external vertex, forcing the other two distances by Euclidean incidence.
    endpoints = {
        "c=0": {
            "substitution": {c: 0, a: p2, b: p1},
            "generators": (c, a - lengths[1], b - lengths[0]),
            "velocities": {
                n1: (0, 0, sp.Rational(1, 2) / p1),
                n2: (0, sp.Rational(1, 2) / p2, 0),
                n3: (0, 0, 0),
            },
        },
        "a=0": {
            "substitution": {c: p2, a: 0, b: p3},
            "generators": (a, c - lengths[1], b - lengths[2]),
            "velocities": {
                n1: (0, 0, 0),
                n2: (sp.Rational(1, 2) / p2, 0, 0),
                n3: (0, 0, sp.Rational(1, 2) / p3),
            },
        },
        "b=0": {
            "substitution": {c: p1, a: p3, b: 0},
            "generators": (b, c - lengths[0], a - lengths[2]),
            "velocities": {
                n1: (sp.Rational(1, 2) / p1, 0, 0),
                n2: (0, 0, 0),
                n3: (0, sp.Rational(1, 2) / p3, 0),
            },
        },
    }

    checks: list[dict[str, object]] = []
    for endpoint, packet in endpoints.items():
        substitution = packet["substitution"]
        central_substitution = zero_normals | substitution
        assert sp.simplify(kernel.subs(central_substitution)) == 0

        for normal in normals:
            vector = packet["velocities"][normal]
            for generator in packet["generators"]:
                transported = sp.diff(generator, normal) + sum(
                    component * sp.diff(generator, fiber)
                    for component, fiber in zip(vector, fibers, strict=True)
                )
                assert sp.simplify(transported.subs(central_substitution)) == 0

            transported_kernel = sp.diff(kernel, normal) + sum(
                component * sp.diff(kernel, fiber)
                for component, fiber in zip(vector, fibers, strict=True)
            )
            assert sp.simplify(transported_kernel.subs(central_substitution)) == 0
            checks.append({
                "endpoint": endpoint,
                "normal": str(normal),
                "incidence_generators_preserved": True,
                "full_cayley_menger_boundary_preserved": True,
                "fiber_velocity": [str(component) for component in vector],
            })

    result = {
        "schema": "marici.benincasa.physical-cycle-endpoint-normal-lifts.v1",
        "status": "passed",
        "primary_source_boundary_statement": (
            "arXiv:2402.06558v3 eqs. (3.8), (A.11)-(A.12): signed minors "
            "define Euclidean embeddability and full CM=0 establishes the contour boundary"
        ),
        "endpoint_count": 3,
        "normal_count": 3,
        "incidence_tangency_checks": len(checks),
        "checks": checks,
        "endpoint_classification": "existing lower-dimensional Cayley-Menger face incidence",
        "new_carrier_support": False,
        "classification": (
            "all three loop-distance endpoints admit source-geometric normal lifts "
            "compatible with their incidence ideals and the full CM boundary"
        ),
        "scope_warning": (
            "the endpoint radial exponent and marked-wall residue pairing are not "
            "recomputed; external triangle degeneration remains a separate support"
        ),
    }
    output = HERE / "physical-cycle-endpoint-normal-lifts.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
