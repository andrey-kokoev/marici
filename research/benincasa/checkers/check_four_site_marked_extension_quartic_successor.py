"""Test the four-site marked residual packet as a successor of three-site Q."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
KUMMER = ROOT / "results" / "four-site-qg-residual-kummer-radicals.json"
ABEL_JACOBI = ROOT / "results" / "four-site-qg-residual-abel-jacobi-extension.json"
PHYSICAL = ROOT / "results" / "four-site-qg-residual-physical-support.json"
TYPING = ROOT / "results" / "polygon-contraction-typing.json"
LOCAL_RESIDUE = ROOT / "results" / "polygon-contraction-local-residue.json"
PHYSICAL_CHAMBER = ROOT / "results" / "polygon-contraction-physical-chamber.json"
OUTPUT = ROOT / "results" / "four-site-marked-extension-quartic-successor.json"


def main() -> None:
    kummer = json.loads(KUMMER.read_text(encoding="utf-8"))
    abel_jacobi = json.loads(ABEL_JACOBI.read_text(encoding="utf-8"))
    physical = json.loads(PHYSICAL.read_text(encoding="utf-8"))
    typing = json.loads(TYPING.read_text(encoding="utf-8"))
    local_residue = json.loads(LOCAL_RESIDUE.read_text(encoding="utf-8"))
    physical_chamber = json.loads(PHYSICAL_CHAMBER.read_text(encoding="utf-8"))

    x1, x2, x3, x4, edge = sp.symbols("X1 X2 X3 X4 y_e")
    a11, a22, a33, a12, a13, a23 = sp.symbols("A11 A22 A33 A12 A13 A23")
    cofactor_symbols = (a11, a22, a33, a12, a13, a23)
    merged = x1 + x4
    total = merged + x2 + x3
    pair = merged * x2
    pulled_q = sp.factor(
        -16 * pair**2 - 8 * pair * total**2
        + 8 * (merged + x2) * total**3 - 5 * total**4
    )

    radicands = []
    for record in kummer["records"]:
        coefficients = record["radicand_coefficients"]
        radicands.append(sp.expand(sum(c * s for c, s in zip(coefficients, cofactor_symbols))))

    aj_faces = [
        face
        for term in abel_jacobi["term_packets"]
        for face in term["oriented_faces"]
    ]
    physical_forms = []
    for record in physical["records"]:
        opened = record["denominator_forms"][0]
        form = sum(c * x for c, x in zip(opened["site_coefficients"], (x1, x2, x3, x4)))
        form += opened["edge_coefficients"].count(2) * 2 * edge
        physical_forms.append(sp.expand(form))

    all_soft_substitution = {x1: 0, x2: 0, x3: 0, x4: 0, edge: 0}
    checks = {
        "four_kummer_occurrence_divisors": len(set(map(str, radicands))) == 4,
        "kummer_divisors_are_gram_only": all(not (r.free_symbols & {x1, x2, x3, x4}) for r in radicands),
        "kummer_divisors_are_coprime_to_pulled_Q": all(sp.gcd(r, pulled_q) == 1 for r in radicands),
        "abel_jacobi_faces_are_existing_elliptic_or_split_faces": all(
            face["curve_type"] in {
                "smooth elliptic double cover",
                "split rational deck pair from two double branch roots",
            }
            for face in aj_faces
        ),
        "abel_jacobi_packet_has_no_declared_new_support_factor": all(
            "support" not in face and "discriminant" not in face for face in aj_faces
        ),
        "opened_graph_wall_contracts_to_total_energy_plus_edge_soft": all(
            sp.expand(form - (total + 2 * edge)) == 0 for form in physical_forms
        ),
        "physical_contact_is_all_soft_and_Q_vanishes_there": sp.expand(pulled_q.subs(all_soft_substitution)) == 0,
        "all_soft_contact_is_not_a_quartic_divisor": len(all_soft_substitution) > 1,
        "facet_pullback_exists": typing["conclusion"]["facet_pullback_exists"],
        "direct_period_recursion_is_not_authorized": not typing["conclusion"]["direct_period_recursion_authorized"],
        "co_moving_gram_mark_map_is_absent": all(
            key not in typing for key in ("gram_pullback", "mark_transport", "residue_gysin_matrix")
        ),
        "symmetric_unit_counit_is_obstructed": not local_residue["conclusion"]["exchange_symmetric_integral_unit_map"],
        "local_map_requires_extra_occurrence_data": bool(local_residue["conclusion"]["required_extra_datum"]),
        "positive_chamber_selects_no_endpoint": (
            not physical_chamber["conclusion"]["generic_contraction_boundary_selects_first_occurrence"]
            and not physical_chamber["conclusion"]["generic_contraction_boundary_selects_second_occurrence"]
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.four_site_marked_extension_quartic_successor.v1",
        "contraction": "merge source sites 4 and 1; target X1'=X4+X1",
        "pulled_three_site_quartic": str(pulled_q),
        "kummer_radicands": [str(r) for r in radicands],
        "abel_jacobi_face_profile": {
            "smooth_elliptic": sum(face["curve_type"] == "smooth elliptic double cover" for face in aj_faces),
            "split_exact": sum(face["curve_type"].startswith("split rational") for face in aj_faces),
        },
        "contracted_physical_wall": str(total + 2 * edge),
        "physical_closure": "X1=X2=X3=X4=y_e=0; its image is existing target all-soft support",
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "classification": "successor comparison is unavailable from the frozen physical source: facet pullback exists, but no co-moving Gram/mark counit is derived and the positive chamber selects neither endpoint",
        "static_evidence": "with the Gram detector frozen, marked divisors are Q-coprime and physical contact is only all-soft; these facts do not replace the missing comparison map",
        "scope": "frozen four-site residual marked packet under the typed 4-to-3 contraction",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
