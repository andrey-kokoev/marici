#!/usr/bin/env python3
"""Verify cancellation of external/fiber normal defects for all-soft K_CM."""

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


def main():
    rows = []
    for coefficient, exponents in TERMS:
        external_degree = sum(exponents[:4])
        fiber_degree = sum(exponents[4:])
        total_degree = external_degree + fiber_degree
        assert total_degree == 6
        rows.append({
            "coefficient": coefficient,
            "exponents": exponents,
            "external_degree": external_degree,
            "fiber_degree": fiber_degree,
            "total_degree": total_degree,
            "normal_defect_cancellation": (fiber_degree - 6) + external_degree,
        })
    assert all(row["normal_defect_cancellation"] == 0 for row in rows)
    assert len({row["fiber_degree"] for row in rows}) > 1

    packet = {
        "term_count": len(rows),
        "full_radial_identity": "(R_ext+R_fib)(K)=6K",
        "fiber_degrees_present": sorted({row["fiber_degree"] for row in rows}),
        "fiber_eigenvector": False,
        "external_eigenvector": False,
        "branch_normal_identity": "R_ext(K)|_{K=0}=-R_fib(K)|_{K=0}",
        "termwise_cancellation_verified": True,
        "typed_conclusion": "Only the unsplit full-radial contraction descends to the CM branch.",
    }
    out = Path(__file__).with_name("all-soft-radial-fiber-defect-cancellation.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
