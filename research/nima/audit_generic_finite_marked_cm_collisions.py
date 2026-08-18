"""Census finite pairwise marked-section collisions on the generic CM curve."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    e, x1, x2, x3, p1, p2, p3, a, b = sp.symbols("E X1 X2 X3 P1 P2 P3 a b")
    cm_matrix = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, e**2, a**2, b**2],
        [1, e**2, 0, p2**2, p1**2],
        [1, a**2, p2**2, 0, p3**2],
        [1, b**2, p1**2, p3**2, 0],
    ])
    k = sp.expand(-cm_matrix.det() / 2)
    energy_sum = x1 + x2 + x3
    parameters = (x1, x2, x3, p1, p2, p3)

    # Every nonparallel pair fixes one source-labelled point (a0,b0).
    points = {
        "g1__g2": (e - x2, e - x1),
        "g1__g3": (x1 - e - x3, e - x1),
        "g1__G23": (-e, e - x1),
        "g2__g3": (e - x2, x2 - e - x3),
        "g2__G31": (e - x2, -e),
        "g3__G23": (-e, e - x3),
        "g3__G31": (e - x3, -e),
        "G23__G31": (-e, -e),
    }

    rows = []
    for labels, (a0, b0) in points.items():
        collision = sp.Poly(sp.expand(k.subs({a: a0, b: b0, e: energy_sum})), *parameters)
        _, factors = sp.factor_list(collision.as_expr(), *parameters)
        text = sp.sstr(collision.as_expr())
        rows.append({
            "labels": labels.split("__"),
            "marked_point": {"a": sp.sstr(a0), "b": sp.sstr(b0)},
            "collision_equation": f"K_CM({sp.sstr(a0)},{sp.sstr(b0)})=0",
            "expanded_term_count": len(collision.terms()),
            "total_degree": collision.total_degree(),
            "factor_count_over_Q": len(factors),
            "factor_degrees": [sp.Poly(factor, *parameters).total_degree() for factor, _ in factors],
            "expanded_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "classification": "restriction of the frozen Cayley-Menger determinant to a source-labelled marked intersection",
        })

    parallel = [
        {"labels": ["g1", "G31"], "coincidence_condition": "X1+2*X2+2*X3=0"},
        {"labels": ["g2", "G23"], "coincidence_condition": "2*X1+X2+2*X3=0"},
    ]

    result = {
        "schema": "marici.nima.generic_finite_marked_cm_collisions.v1",
        "residue": "q_G12=0 with c=-E",
        "site_energy_relation": "E=X1+X2+X3",
        "cm_normalization": "K_CM=-det(CM)/2",
        "source_marked_sections": {
            "g1": "b=E-X1", "g2": "a=E-X2", "g3": "a+b=-X3", "G23": "a=-E", "G31": "b=-E"
        },
        "nonparallel_pair_count": len(rows),
        "nonparallel_pairs": rows,
        "parallel_pairs": parallel,
        "new_projected_resultant_divisor_count": len(rows),
        "projected_resultant_type": "eight irreducible sextics over Q after E=X1+X2+X3",
        "new_unlabelled_carrier_factor": False,
        "conclusion": "The external parameter base acquires eight irreducible sextic collision resultants, but every one is canonically K_CM evaluated at a source-labelled marked intersection. The remaining two collisions are linear marked-incidence coincidences. These are new projected coefficient discriminants, not unlabelled carrier components.",
        "allocator_claim": "seqclaim-4a9da02b9ab2b00469868db4",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"nonparallel_pairs": len(rows), "parallel_pairs": len(parallel), "factor_counts": [row["factor_count_over_Q"] for row in rows]}))


if __name__ == "__main__":
    main()
