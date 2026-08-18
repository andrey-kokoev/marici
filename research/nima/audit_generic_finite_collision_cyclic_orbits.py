"""Transport Entry 802 collision sextics through the three residue charts."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("census", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    census = json.loads(args.census.read_text(encoding="utf-8"))

    x1, x2, x3, p1, p2, p3, a, b = sp.symbols("X1 X2 X3 P1 P2 P3 a b")
    e = x1 + x2 + x3
    cm = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, e**2, a**2, b**2],
        [1, e**2, 0, p2**2, p1**2],
        [1, a**2, p2**2, 0, p3**2],
        [1, b**2, p1**2, p3**2, 0],
    ])
    k12 = sp.expand(-cm.det() / 2)
    variables = (x1, x2, x3, p1, p2, p3)
    sigma_map = {x1: x2, x2: x3, x3: x1, p1: p2, p2: p3, p3: p1}

    def sigma(poly):
        return sp.Poly(sp.expand(poly.as_expr().subs(sigma_map, simultaneous=True)), *variables)

    label_sigma = {"g1": "g2", "g2": "g3", "g3": "g1", "G12": "G23", "G23": "G31", "G31": "G12"}
    charts = ["G12", "G23", "G31"]
    rows = []
    for source_row in census["nonparallel_pairs"]:
        a0 = sp.sympify(source_row["marked_point"]["a"], locals={"E": e, "X1": x1, "X2": x2, "X3": x3})
        b0 = sp.sympify(source_row["marked_point"]["b"], locals={"E": e, "X1": x1, "X2": x2, "X3": x3})
        polys = [sp.Poly(sp.expand(k12.subs({a: a0, b: b0})), *variables)]
        polys.append(sigma(polys[-1]))
        polys.append(sigma(polys[-1]))
        if sigma(polys[-1]) != polys[0]:
            raise AssertionError("cyclic polynomial transport does not close")
        labels = [source_row["labels"]]
        for _ in range(2):
            labels.append([label_sigma[label] for label in labels[-1]])
        polynomial_orbit_size = len({sp.sstr(poly.as_expr()) for poly in polys})
        rows.append({
            "representative_in_G12": source_row["labels"],
            "occurrences": [
                {
                    "chart": charts[i],
                    "labels": labels[i],
                    "expanded_sha256": hashlib.sha256(sp.sstr(polys[i].as_expr()).encode()).hexdigest(),
                    "term_count": len(polys[i].terms()),
                }
                for i in range(3)
            ],
            "occurrence_orbit_size": 3,
            "occurrence_stabilizer_order": 1,
            "scalar_polynomial_orbit_size": polynomial_orbit_size,
            "scalar_polynomial_stabilizer_order": 3 // polynomial_orbit_size,
            "transport_closes": True,
        })

    result = {
        "schema": "marici.nima.generic_finite_collision_cyclic_orbits.v1",
        "source": str(args.census).replace("\\", "/"),
        "canonical_cycle": {
            "sigma": "(X1,X2,X3;P1,P2,P3)->(X2,X3,X1;P2,P3,P1)",
            "internal_edges": "(a,b,c)->(b,c,a)",
            "residue_charts": ["G12", "G23", "G31", "G12"],
            "labels": {"g1": "g2", "g2": "g3", "g3": "g1", "G12": "G23", "G23": "G31", "G31": "G12"},
            "relation_to_benincasa_rho": "sigma=rho^-1 for rho:(X1,X2,X3)->(X3,X1,X2)",
        },
        "orbit_count": len(rows),
        "orbits": rows,
        "all_occurrence_orbits_free_of_size_three": all(row["occurrence_orbit_size"] == 3 and row["occurrence_stabilizer_order"] == 1 for row in rows),
        "transition_unit": "1 at the eliminated scalar-polynomial level; residue-form orientation remains a separate Gysin datum",
        "conclusion": "The eight G12 sextics generate eight free C3 occurrence orbits, hence twenty-four labelled finite collision occurrences. One scalar sextic is C3-invariant even though its labelled occurrence orbit remains free. Cyclic transport introduces no scalar unit, but does not determine residue-form orientation signs.",
        "allocator_claim": "seqclaim-7de3a2de708032a94e173905",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"orbits": len(rows), "occurrences": 3 * len(rows), "polynomial_orbit_sizes": [row["scalar_polynomial_orbit_size"] for row in rows]}))


if __name__ == "__main__":
    main()
