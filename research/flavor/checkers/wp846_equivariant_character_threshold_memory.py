"""Exact WP846 audit of representation-valued threshold memory."""

import json
from pathlib import Path
import sympy as sp


def anomaly(charges, power):
    return sum(sp.Integer(q)**power for q in charges)


def diameter(charges):
    return max(charges)-min(charges)


def character(charges, z):
    return sp.expand(sum(z**q for q in charges))


def main() -> None:
    base = [1, 2, 3]
    vectorlike_hostile = [1, 2, 3, 4, -4]
    active = [2, 3]
    heavy = [1]
    z = sp.symbols("z", nonzero=True)
    roots = [1, -1, sp.I, -sp.I]
    fourier = sp.Matrix([[root**q for q in range(4)] for root in roots])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_linear_anomaly_is_six", anomaly(base, 1) == 6, anomaly(base, 1))
    check("primitive_cubic_anomaly_is_thirty_six", anomaly(base, 3) == 36, anomaly(base, 3))
    check("vectorlike_hostile_preserves_both_odd_anomalies",
          anomaly(vectorlike_hostile, 1) == anomaly(base, 1)
          and anomaly(vectorlike_hostile, 3) == anomaly(base, 3),
          (anomaly(vectorlike_hostile, 1), anomaly(vectorlike_hostile, 3)))
    check("same_anomalies_do_not_fix_diameter",
          diameter(base) == 2 and diameter(vectorlike_hostile) == 8,
          (diameter(base), diameter(vectorlike_hostile)))
    full_character = character(base, z)
    active_character = character(active, z)
    heavy_character = character(heavy, z)
    check("primitive_equivariant_character_is_exact",
          full_character == z+z**2+z**3, full_character)
    check("threshold_character_sews_exactly",
          sp.expand(active_character+heavy_character-full_character) == 0,
          (active_character, heavy_character))
    check("active_particle_support_loses_diameter",
          diameter(active) == 1, diameter(active))
    sewn_support = sorted(set(active+heavy))
    check("sewn_character_support_restores_uv_diameter",
          sewn_support == base and diameter(sewn_support) == 2,
          (sewn_support, diameter(sewn_support)))
    check("diameter_selected_fixed_point_survives_on_sewn_character",
          sp.Rational(1, diameter(sewn_support)) == sp.Rational(1, 2),
          sp.Rational(1, diameter(sewn_support)))
    check("four_holonomy_port_matrix_is_invertible",
          fourier.det() != 0, fourier.det())
    check("four_holonomy_ports_reconstruct_all_bounded_coefficients",
          fourier.rank() == 4, fourier.rank())
    check("reference_holonomy_is_an_added_relational_port",
          len(roots) == 4 and fourier.rank() == 4,
          "four background-holonomy settings on bounded support")

    result = {
        "work_package": "WP846",
        "title": "Equivariant character threshold memory",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "ordinary_anomaly_hostile": "charges {1,2,3} and {1,2,3,4,-4} share A1=6,A3=36 but have diameters 2 and 8",
        "threshold_sewing": "(z^2+z^3)+z=z+z^2+z^3",
        "preserved_selector": "diameter of sewn character support is 2, so x*=1/2",
        "finite_probe": "four evaluations at 1,-1,i,-i reconstruct support coefficients q=0,1,2,3",
        "classification": "conditional representation-valued threshold repair with finite faithful relational probe",
        "changed_groupoid": "background holonomy is an added reference port; the experiment is relative to its stabilizer",
        "remaining_source_gate": "derive full-character threshold matching from an equivariant source index and realize controlled calibrated holonomy ports in physical16 detector units",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp846_equivariant_character_threshold_memory.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
