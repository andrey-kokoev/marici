"""Project primary-source Eq. (4.19) edge regulators to C8 fold normals."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
VISIBILITY = ROOT / "results" / "eight-site-rank4-routing-visibility-criterion.json"
TARGET = ROOT / "results" / "eight-site-rank4-source-regulator-fold-chambers.json"


def companion_factor(determinant: sp.Expr, routing: set[sp.Symbol]) -> sp.Expr:
    candidates = [factor for factor, _ in sp.factor_list(determinant)[1] if len(factor.free_symbols & routing) >= 2]
    assert len(candidates) == 1
    return sp.factor(candidates[0])


def main() -> None:
    models = json.loads(MODELS.read_text())["models"]
    visibility = json.loads(VISIBILITY.read_text())
    a, b, c, d, z, k, ell = sp.symbols("a b c d z k l")
    variables = (a, b, c, d, z)
    locals_ = {str(value): value for value in (*variables, k, ell)}
    points = {
        "family_A_surviving_edge_1_free_even": {a: 1, b: 1, c: 1, d: 1, z: sp.sqrt(sp.Rational(32, 5)), k: 1, ell: 0},
        "family_B_surviving_edge_8_free_odd": {a: 1, b: sp.sqrt(sp.Rational(-9, 10)), c: 1, d: 1, z: 1, k: 1, ell: 0},
    }
    audits = []
    for model in models[:2]:
        determinant = sp.sympify(model["jacobian_determinant"], locals=locals_)
        fold = companion_factor(determinant, {a, b, c, z})
        point = points[model["name"]]
        assert sp.simplify(fold.subs(point)) == 0
        gradient = [sp.simplify(sp.diff(fold, variable).subs(point)) for variable in variables]
        regulator_generators = [sp.simplify(-sp.I * value) for value in gradient]
        item = {
            "model": model["name"],
            "fold_point": {str(key): str(value) for key, value in point.items()},
            "fold_gradient_on_edge_energies": [str(value) for value in gradient],
            "eq_4_19_normal_generators": [str(value) for value in regulator_generators],
        }
        if model["name"].startswith("family_A"):
            positive_packet = {a: 1, b: 1, c: 1, d: 1, z: 1}
            negative_packet = {a: 1, b: 1, c: 1, d: 1, z: 2}
            tangent_packet = {a: 1, b: 1, c: 1, d: 1, z: sp.Rational(4) / sp.sqrt(10)}
            normal = lambda packet: sp.simplify(sum(generator * packet[variable] for generator, variable in zip(regulator_generators, variables)))
            values = [normal(packet) for packet in (positive_packet, negative_packet, tangent_packet)]
            assert sp.im(values[0]) > 0 and sp.im(values[1]) < 0 and values[2] == 0
            item.update({
                "positive_regulator_packet_one": {str(key): str(value) for key, value in positive_packet.items()},
                "positive_regulator_packet_two": {str(key): str(value) for key, value in negative_packet.items()},
                "positive_tangent_packet": {str(key): str(value) for key, value in tangent_packet.items()},
                "normal_values": [str(value) for value in values],
                "positive_edge_regulator_cone_crosses_fold_normal_origin": True,
                "betti_chamber_selected": False,
            })
        else:
            # The source cover differentiates in a,b,c,d and retains z as the
            # fifth edge energy.  k,l are Gram-shape parameters, not Eq. (4.19)
            # energy variables.  Hence the edge cone is the complete source
            # regulator image relevant to this fold-normal test.
            assert model["variables"] == ["a", "b", "c", "d"]
            eps_a, eps_b, eps_c = sp.symbols("epsilon_a epsilon_b epsilon_c", positive=True)
            b8_normal = sp.simplify(regulator_generators[0] * eps_a + regulator_generators[1] * eps_b + regulator_generators[2] * eps_c)
            assert sp.re(b8_normal) < 0 and sp.im(b8_normal) > 0
            item.update({
                "positive_edge_regulator_cone_crosses_fold_normal_origin": False,
                "complete_positive_normal_cone": str(b8_normal),
                "normal_cone_location": "strict second quadrant",
                "betti_chamber_selected": True,
                "fixed_nonenergy_parameters": ["k", "l"],
            })
        audits.append(item)

    activated = [item for item in visibility["occurrences"] if item["full_routing_visibility"]]
    family_a_activated = sum("family_A" in next(
        family["model"] for family in json.loads((ROOT / "results" / "eight-site-rank4-face-fold-pairing.json").read_text())["families"]
        if family["source_orbit_key"] == item["source_orbit_key"]
    ) for item in activated)
    checks = {
        "primary_source_prescription": "arXiv:2305.19686v2 Eq. (4.19)",
        "activated_occurrence_count": len(activated),
        "family_A_activated_occurrence_count": family_a_activated,
        "family_A_positive_cone_has_two_opposite_normal_chambers": audits[0]["positive_edge_regulator_cone_crosses_fold_normal_origin"],
        "family_A_affine_betti_selection_is_noncanonical": not audits[0]["betti_chamber_selected"],
        "remaining_B8_occurrence_count": len(activated) - family_a_activated,
        "B8_selection_status": "unique_positive_source_chamber",
        "B8_activated_occurrence_count": len(activated) - family_a_activated,
        "physically_selected_occurrence_count": len(activated) - family_a_activated,
        "physically_unselected_occurrence_count": family_a_activated,
        "physically_dormant_occurrence_count": visibility["checks"]["failed_visibility_occurrence_count"],
    }
    assert checks["activated_occurrence_count"] == 176
    assert checks["family_A_activated_occurrence_count"] == 168
    assert checks["remaining_B8_occurrence_count"] == 8
    packet = {
        "schema": "marici.eight_site_rank4_source_regulator_fold_chambers.v1",
        "typing": {
            "source": "negative-imaginary energy tube of primary-source Eq. (4.19)",
            "map": "first normal derivative of the companion fold divisor under y_e -> y_e-i epsilon_e",
            "scope": "edge-energy regulator cone; k,l regulator transport retained as an explicit missing datum",
        },
        "checks": checks,
        "models": audits,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
