"""Held-out SOURCE-arrow falsifier for common geometric point transports.

Exit zero means the falsification experiment passed, NOT that its candidate
survived. Positions are not identified with complete carrier-response states.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "research/strominger/inputs/carrier-common-law-geometry-v1.json"
PACKET = ROOT / "research/strominger/carrier-common-law-geometric-falsification.md"
MODEL = ROOT / "research/strominger/scc-models/carrier-common-law-geometry-v1.json"
BASE_PATH = ROOT / "research/strominger/checkers/check_carrier_particle_circuits.py"
OUT = ROOT / "research/strominger/results/carrier-common-law-geometry"
spec = importlib.util.spec_from_file_location("geometry_falsifier_matrix_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def sub(x, y):
    return [a - b for a, b in zip(x, y)]


def square(v, metric):
    return sum(x * y for x, y in zip(v, base.mv(metric, v)))


def run(report, source):
    f = json.loads(FIXTURE.read_text(encoding="utf-8"))
    checks = report["checks"]

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    body = re.search(r"export const lattice\s*=\s*(\{[^;]+\});", source).group(1)
    raw = json.loads(re.sub(r"\b([CM][0-9]+)\s*:", r'"\1":', body))
    points = {name: [Q(x) for x in v] for name, v in raw.items()}
    routes = {}
    for name, text in re.findall(r"id:\s*['\"](proton|neutron|electron)['\"][^{}\n]*?nodes:\s*\[([^\]]+)\]", source):
        routes[name] = re.findall(r"['\"]([CM][0-9]+)['\"]", text)
    expected = json.loads(base.FIXTURE.read_text(encoding="utf-8"))["windows"]
    check("actual_source_routes_match_corrected_words", routes == expected)
    check("source_points_are_three_coordinate_affine_points", set(points) == set(expected["proton"] + ["M1", "C2"]) and all(len(v) == 3 for v in points.values()))
    supported_hex = "exportconsthexBasis={a:[1,0,0],b:[.5,0,Math.sqrt(3)/2],c:[0,1,0]};"
    check("hex_metric_uses_declared_source_basis", supported_hex in re.sub(r"\s", "", source))

    def edge(reference):
        route, index = routes[reference["route"]], reference["segment"]
        return route[index], route[index + 1]

    training = {kind: edge(ref) for kind, ref in f["training"].items()}
    held = {kind: edge(ref) for kind, ref in f["held_out"].items()}
    learned = {kind: sub(points[v], points[u]) for kind, (u, v) in training.items()}
    predictions = {}
    for kind, (u, v) in held.items():
        predicted = add(points[u], learned[kind])
        predictions[kind] = {"source": u, "target": v, "predicted": predicted,
                             "observed": points[v], "residual": sub(predicted, points[v])}
    check("held_out_A_occurrence_succeeds_without_refit", predictions["A"]["residual"] == [0, 0, 0])
    residual = predictions["B"]["residual"]
    check("held_out_B_occurrence_fails_by_one_realization_unit", residual == [1, 0, 0])
    check("proton_trained_B_predicts_C2_instead_of_C1", predictions["B"]["predicted"] == points["C2"] and predictions["B"]["target"] == "C1")

    occurrences = defaultdict(dict)
    for family, route in routes.items():
        for segment, (u, v) in enumerate(zip(route, route[1:])):
            kind = {("C", "M"): "A", ("M", "C"): "B", ("C", "C"): "T"}[(u[0], v[0])]
            record = occurrences[kind].setdefault((u, v), {"displacement": sub(points[v], points[u]), "windows": []})
            record["windows"].append([family, segment])
    check("shared_B_training_edge_is_not_double_counted", len(occurrences["B"]) == 2 and len(occurrences["B"][("M0", "C1")]["windows"]) == 2)
    consistent = {kind: len({tuple(v["displacement"]) for v in records.values()}) == 1 for kind, records in occurrences.items()}
    check("entire_translation_parameter_class_is_inconsistent_only_at_B", consistent == {"A": True, "B": False, "T": True})
    b_records = list(occurrences["B"].values())
    coefficient = [[1], [1]]
    augmented = [[1, record["displacement"][0]] for record in b_records]
    check("no_common_B_even_if_both_occurrences_are_fitted", base.rank(coefficient) == 1 and base.rank(augmented) == 2)
    check("two_arrow_obstruction_is_minimal", all(len({tuple(record["displacement"]) for record in b_records[:i] + b_records[i + 1:]}) == 1 for i in range(2)))

    metric_cart = [[Q(i == j) for j in range(3)] for i in range(3)]
    metric_hex = [[Q(1), Q(0), Q(1, 2)], [Q(0), Q(1), Q(0)], [Q(1, 2), Q(0), Q(1)]]
    check("Cartesian_residual_norm_squared_is_one", square(residual, metric_cart) == 1)
    check("hexagonal_residual_norm_squared_is_one", square(residual, metric_hex) == 1)
    separation = sub(points["M1"], points["M0"])
    check("distinct_M_points_have_same_B_target", separation != [0, 0, 0] and held["B"][1] == training["B"][1] == "C1")
    check("isometric_B_has_unit_squared_distance_defect", square(separation, metric_hex) - square(sub(points[held["B"][1]], points[training["B"][1]]), metric_hex) == 1)
    scale, origin = [Q(2), Q(1), Q(3)], [Q(5), Q(-2), Q(4)]
    changed = {name: [s * x + o for s, x, o in zip(scale, p, origin)] for name, p in points.items()}
    u, v = training["B"]
    transformed_delta = sub(changed[v], changed[u])
    u, v = held["B"]
    transformed_residual = sub(add(changed[u], transformed_delta), changed[v])
    check("honest_affine_chart_change_cannot_remove_residual", transformed_residual == [s * x for s, x in zip(scale, residual)] and transformed_residual != [0, 0, 0])
    transported_metric = [[metric_hex[i][j] / (scale[i] * scale[j]) for j in range(3)] for i in range(3)]
    check("metric_transport_preserves_residual_norm", square(transformed_residual, transported_metric) == 1)

    collapse = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    check("predeclared_affine_collapse_can_fit_B_points", all(base.mv(collapse, points[u]) == points[v] for u, v in occurrences["B"]))
    check("affine_collapse_erases_realization_direction_in_point_chart", base.mv(collapse, separation) == [0, 0, 0] and separation != [0, 0, 0])
    predicted_endpoint = add(predictions["B"]["predicted"], learned["T"])
    check("frozen_T_does_not_hide_B_failure_at_electron_endpoint", sub(predicted_endpoint, points["C2"]) == residual)
    fake_t = [Q(0)] * 3
    check("endpoint_only_refit_can_hide_primitive_mismatch", add(predictions["B"]["predicted"], fake_t) == points["C2"] and add(points["C1"], fake_t) != points["C2"])
    check("retained_midpoint_rejects_endpoint_only_spoof", predictions["B"]["predicted"] != points["C1"])
    report.update({"points": points, "routes": routes, "training": training, "held_out": held,
        "learned_translations": learned, "held_out_predictions": predictions,
        "primitive_constraints": {kind: [{"edge": list(edge), **record} for edge, record in records.items()] for kind, records in occurrences.items()},
        "common_translation_consistency": consistent,
        "minimal_B_constraint": {"coefficient": coefficient, "augmented": augmented, "ranks": [1, 2]},
        "affine_chart_control": {"scale": scale, "origin": origin, "residual": transformed_residual, "transported_hex_metric": transported_metric},
        "affine_collapse_control": {"linear_part": collapse, "forced_kernel_direction": separation,
            "status": "Distinct predeclared rival fits point observations; not a source-derived full-state law"},
        "endpoint_only_spoof": {"changed_T_displacement": fake_t, "predicted_midpoint": predictions["B"]["predicted"], "observed_midpoint": points["C1"]},
        "classification": "geometric_translation_class_falsified",
        "scientific_disposition": {"common_point_translations": "FALSIFIED", "injective_B_point_maps": "FALSIFIED", "general_affine_B": "compatible only if its linear part kills M1-M0", "full_carrier_state_common_law": "NOT TESTED; state operator and source context maps not supplied"},
        "nonpromotion": "Coinciding target positions/carrier identities do not prove equal response contents or information loss in a complete state operator."})


def main():
    f = json.loads(FIXTURE.read_text(encoding="utf-8"))
    source_path = ROOT / f["source"]
    paths = [FIXTURE, PACKET, MODEL, BASE_PATH, base.FIXTURE, source_path, Path(__file__).resolve()]
    report = {"schema": "marici.strominger.common-law-geometry.verification.v1", "recorded_at": datetime.now(timezone.utc).isoformat(), "checks": {},
        "zero_exit_semantics": "falsification experiment verified; geometric candidate did not survive",
        "source_sha256": {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report, source_path.read_text(encoding="utf-8"))
        report["status"] = "pass"
    except Exception as error:
        report["status"], report["error"] = "fail", repr(error)
        raise
    finally:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "verification.json").write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
        print(json.dumps({"status": report["status"], "classification": report.get("classification", "execution_failure"), "check_groups": len(report["checks"]), "receipt": str((OUT / "verification.json").relative_to(ROOT)).replace("\\", "/")}))


if __name__ == "__main__":
    main()
