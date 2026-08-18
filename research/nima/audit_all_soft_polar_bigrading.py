#!/usr/bin/env python3
"""Exact fiber-degree normal form for the all-soft polar support."""

import json
from pathlib import Path


TERMS = [
    (1,(4,0,0,2,0,0)),(-1,(2,2,0,0,2,0)),(1,(2,0,2,0,2,0)),
    (-1,(2,0,0,2,2,0)),(1,(2,2,0,0,0,2)),(-1,(2,0,2,0,0,2)),
    (-1,(2,0,0,2,0,2)),(-1,(2,2,0,2,0,0)),(-1,(2,0,2,2,0,0)),
    (1,(2,0,0,4,0,0)),(1,(0,2,0,0,4,0)),(-1,(0,2,0,0,2,2)),
    (-1,(0,0,2,0,2,2)),(1,(0,0,0,2,2,2)),(1,(0,4,0,0,2,0)),
    (-1,(0,2,2,0,2,0)),(-1,(0,2,0,2,2,0)),(1,(0,0,2,0,0,4)),
    (-1,(0,2,2,0,0,2)),(1,(0,0,4,0,0,2)),(-1,(0,0,2,2,0,2)),
    (1,(0,2,2,2,0,0)),
]


def evaluate(terms, point):
    return sum(c * __import__("math").prod(x**e for x, e in zip(point, exps))
               for c, exps in terms)


def main():
    pieces = {0: [], 2: [], 4: []}
    for term in TERMS:
        fiber_degree = sum(term[1][4:])
        assert fiber_degree in pieces
        pieces[fiber_degree].append(term)

    samples = [(1,2,3,5,7,11), (2,1,4,3,5,9), (3,5,2,7,4,1)]
    for point in samples:
        k0, k2, k4 = (evaluate(pieces[d], point) for d in (0,2,4))
        K = evaluate(TERMS, point)
        polar = 2*k2 + 4*k4
        assert K == k0 + k2 + k4
        assert 2*K - polar == 2*(k0-k4)
        assert polar // 2 == k2 + 2*k4

    # Both endpoint binary quadratics have the same exact discriminant.
    for p1, p2, p3 in [(2,3,5), (3,4,6), (5,7,11)]:
        lam = p1**4 + p2**4 + p3**4 - 2*p1**2*p2**2 - 2*p1**2*p3**2 - 2*p2**2*p3**2
        disc_k0 = (p1**2+p2**2-p3**2)**2 - 4*p1**2*p2**2
        disc_k4 = (-p1**2-p2**2+p3**2)**2 - 4*p1**2*p2**2
        assert disc_k0 == lam == disc_k4

    packet = {
        "fiber_degree_term_counts": {str(d): len(pieces[d]) for d in (0,2,4)},
        "decomposition": "K=K0+K2+K4",
        "polar_operator": "R_fib(K)=2K2+4K4",
        "equivalent_polar_ideal": ["K0-K4", "K2+2K4"],
        "linear_change_determinant": "1/2 (inverse determinant 2)",
        "K0": "P3^2*(E^4-(P1^2+P2^2-P3^2)E^2+P1^2P2^2)",
        "K4": "P1^2*a^4+(-P1^2-P2^2+P3^2)*a^2*b^2+P2^2*b^4",
        "endpoint_discriminants": "Delta(K0 in E^2)=Delta(K4 in a^2/b^2)=Lambda(P1,P2,P3)",
        "carrier_codimension": 2,
        "classification": "source-derived polar coefficient support, not a new divisor",
    }
    out = Path(__file__).with_name("all-soft-polar-bigrading.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
