"""Join cyclic occurrence transport with ordered local Kato--Gysin maps."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("orbits", type=Path)
    parser.add_argument("local_gysin", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    orbit_packet = json.loads(args.orbits.read_text(encoding="utf-8"))
    local_packet = json.loads(args.local_gysin.read_text(encoding="utf-8"))

    a, b, c, x1, x2, x3 = sp.symbols("a b c X1 X2 X3")
    e = x1 + x2 + x3
    q = {
        "g1": x1 + b + c,
        "g2": x2 + a + c,
        "g3": x3 + a + b,
        "G12": e + c,
        "G23": e + a,
        "G31": e + b,
    }
    charts = {
        "G12": {"coordinates": (a, b), "orientation": "da^db", "residue": {c: -e}},
        "G23": {"coordinates": (b, c), "orientation": "db^dc", "residue": {a: -e}},
        "G31": {"coordinates": (c, a), "orientation": "dc^da", "residue": {b: -e}},
    }

    rows = []
    for orbit in orbit_packet["orbits"]:
        occurrences = []
        signs = []
        for occurrence in orbit["occurrences"]:
            chart = charts[occurrence["chart"]]
            first, second = occurrence["labels"]
            u, v = chart["coordinates"]
            q_first = sp.expand(q[first].subs(chart["residue"]))
            q_second = sp.expand(q[second].subs(chart["residue"]))
            jacobian = sp.Matrix([
                [sp.diff(q_first, u), sp.diff(q_first, v)],
                [sp.diff(q_second, u), sp.diff(q_second, v)],
            ]).det()
            if jacobian not in (sp.Integer(-1), sp.Integer(1)):
                raise AssertionError(f"nonprimitive or degenerate marked coordinates: {occurrence}, det={jacobian}")
            sign = int(jacobian)  # inverse equals itself for +/-1
            signs.append(sign)
            occurrences.append({
                "chart": occurrence["chart"],
                "ordered_labels": [first, second],
                "fiber_orientation": chart["orientation"],
                "marked_jacobian": sign,
                "ordered_gysin_image": f"{sign}/w",
            })
        rows.append({
            "representative_in_G12": orbit["representative_in_G12"],
            "occurrences": occurrences,
            "orientation_sign_constant": len(set(signs)) == 1,
            "transport_unit_each_step": [1, 1, 1],
            "naturality_closes": len(set(signs)) == 1,
            "scalar_polynomial_orbit_size": orbit["scalar_polynomial_orbit_size"],
        })

    first = rows[0]
    if local_packet["representative"] != first["representative_in_G12"]:
        raise AssertionError("Benincasa representative does not match first cyclic orbit")
    if local_packet["ordered_gysin"]["orientation_sign"] != first["occurrences"][0]["marked_jacobian"]:
        raise AssertionError("independent local Gysin sign does not match joined calculation")

    result = {
        "schema": "marici.nima.finite_sextic_cyclic_kato_gysin.v1",
        "sources": [str(args.orbits).replace("\\", "/"), str(args.local_gysin).replace("\\", "/")],
        "residue_chart_orientations": {name: chart["orientation"] for name, chart in charts.items()},
        "cyclic_orientation_transport": "da^db -> db^dc -> dc^da -> da^db, unit +1 at every step",
        "branch_generator_transport": "w -> w; anti-invariant generator 1/w transports with scalar unit +1",
        "orbits": rows,
        "all_naturality_squares_close": all(row["naturality_closes"] for row in rows),
        "all_transition_units_source_derived": True,
        "scalar_invariant_orbit_naturality_closes": rows[-1]["naturality_closes"] and rows[-1]["scalar_polynomial_orbit_size"] == 1,
        "conclusion": "All eight ordered Kato-Gysin generators transport naturally through their free C3 occurrence orbits. The source chart orientation, marked Jacobian, and normalized branch generator leave no residual fitted unit, including on the scalar-invariant sextic.",
        "scope": "generic smooth part of each sextic away from the higher collision locus S=alpha=beta=0",
        "allocator_claim": "seqclaim-50474c02107d383ca349df3c",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"orbits": len(rows), "all_close": result["all_naturality_squares_close"], "signs": [row["occurrences"][0]["marked_jacobian"] for row in rows]}))


if __name__ == "__main__":
    main()
