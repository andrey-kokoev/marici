"""Source-derived ports and explicit common-boundary sewing. Exact stdlib only.

Graph pushout is not state equality by itself: require a declared evaluation
context and both faithful value maps. States here are boundary functions.
"""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = ROOT / "research/strominger/checkers/check_carrier_particle_circuits.py"
COMPILER_PATH = ROOT / "research/aspect/scc/categorical_compiler.py"
FIXTURE = ROOT / "research/strominger/inputs/carrier-particle-sewing-v1.json"
PACKET = ROOT / "research/strominger/carrier-particle-sewing.md"
MODEL = ROOT / "research/strominger/scc-models/carrier-particle-sewing-v1.json"
OUT = ROOT / "research/strominger/results/carrier-particle-sewing"
DIAGRAM = ROOT / "research/strominger/contracts/carrier-particle-sewing-v1.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load("carrier_circuit_base", BASE_PATH)
compiler = load("carrier_sewing_compiler", COMPILER_PATH)


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def derived_c_ports(assembly):
    graph = base.projection(assembly, boxes=False)
    incoming, outgoing = Counter(), Counter()
    for u, v in graph["edges"]:
        outgoing[u] += 1
        incoming[v] += 1
    entries = [n for n, k in assembly["nodes"].items() if k == "C" and not incoming[n] and outgoing[n]]
    exits = [n for n, k in assembly["nodes"].items() if k == "C" and incoming[n] and not outgoing[n]]
    if len(entries) != 1 or len(exits) != 1:
        raise ValueError("C boundary is absent or nonunique")
    return {"entry": entries[0], "exit": exits[0]}


def candidate_seams(templates):
    ports = {name: derived_c_ports(a) for name, a in templates.items()}
    return [(ports[a]["exit"], ports[b]["entry"]) for a in sorted(ports) for b in sorted(ports) if a != b]


def graph_pushout(assembly, seams):
    parent = {n: n for n in assembly["nodes"]}

    def find(n):
        while parent[n] != n:
            n = parent[n]
        return n

    for u, v in seams:
        if assembly["nodes"][u] != "C" or assembly["nodes"][v] != "C":
            raise ValueError("graph seam must identify C carriers")
        x, y = find(u), find(v)
        parent[max(x, y)] = min(x, y)
    quotient = {n: find(n) for n in parent}
    fibres = {}
    for n, q in sorted(quotient.items()):
        fibres.setdefault(q, []).append(n)
    primitive = base.edge_provenance(assembly)
    graph = {"nodes": sorted(fibres), "edges": [list(e) for e in sorted({(quotient[e["source"]], quotient[e["target"]]) for e in primitive})]}
    return {"quotient": quotient, "carrier_fibres": fibres, "graph": graph,
            "particle_instances": {pid: {"family": p["family"], "original_walk": p["walk"], "quotient_walk": [quotient[n] for n in p["walk"]]} for pid, p in assembly["particles"].items()},
            "primitive_occurrences": primitive, **base.connectivity(graph)}


def seam_operator(assembly, endpoints, law, contexts, fixture, candidates):
    if tuple(endpoints) not in candidates:
        raise ValueError("not a derived cross-template C exit-to-entry seam")
    common = fixture["common_boundary"]
    if (common["kind"], common["field"], common["values"], fixture["cross_template_only"]) != ("C", "Q", ["0", "1"], True):
        raise ValueError("unsupported common-boundary stratum")
    if contexts != (common["evaluation_context"], common["evaluation_context"]):
        raise ValueError("no common simultaneous evaluation context")
    descriptors = []
    for node in endpoints:
        choices = [p for p in assembly["ports"].values() if p["node"] == node]
        if len(choices) != 1:
            raise ValueError("boundary descriptor missing or ambiguous")
        descriptors.append(choices[0])
    for p, direction in zip(descriptors, ("output", "input")):
        if (p["kind"], p["field"], p["basis"], p["direction"]) != ("C", common["field"], common["values"], direction):
            raise ValueError("boundary descriptor mismatch")
    maps = [law.get("left_restriction"), law.get("right_restriction")]
    if any(m is None for m in maps):
        raise ValueError("missing explicit boundary restriction map")
    if any(len(m) != 2 or sorted(m) != [0, 1] for m in maps):
        raise ValueError("same retained carrier requires faithful binary identifications")
    left, right = maps
    compatible = [(i, j) for i, j in product(range(2), repeat=2) if left[i] == right[j]]
    # Faithfulness makes the common value a complete coordinate on this pullback.
    restriction = [[Q(left[i] == right[j] == s) for i, j in product(range(2), repeat=2)] for s in range(2)]
    extension = base.transpose(restriction)
    projection = base.mm(extension, restriction)
    return {"endpoints": list(endpoints), "contexts": contexts, "left_map": left, "right_map": right,
            "compatible_assignments": compatible, "shared_coordinate": [0, 1],
            "R": restriction, "E": extension, "P": projection,
            "N": subtract(eye(4), projection)}


def digest(data):
    return sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def evaluated_diagram(witnesses):
    """Tokens hash complete computed maps, never unproved word relations."""
    objects, arrows, cells = {}, [], []
    for name, source, target, left, right, factorizations in witnesses:
        objects[source] = {"id": source}
        objects[target] = {"id": target}
        ids = []
        for side, value, factorization in zip(("left", "right"), (left, right), factorizations):
            aid = name + "_" + side
            ids.append(aid)
            arrows.append({"id": aid, "source": source, "target": target,
                           "map_token": digest(value), "evaluated_map": value,
                           "factorization": factorization})
        cells.append({"id": name, "kind": "evaluated_composite_equality", "routes": [[a] for a in ids], "threshold": "exact_zero"})
    return {"id": "carrier-particle-sewing-v1", "objects": list(objects.values()), "arrows": arrows,
            "cells": cells, "obstructions": [], "claims": [],
            "scope": "Only computed finite realizations; checker verifies matrices and finite functions. No primitive word relation or unsupported higher cell promoted."}


def run(report):
    base.run(report)  # Fresh baseline controls; does not rewrite the base receipt.
    checks = report["checks"]

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    def refuses(name, operation):
        try:
            operation()
        except ValueError as error:
            report.setdefault("refusals", {})[name] = str(error)
            check(name, True)
        else:
            check(name, False)

    f = json.loads(FIXTURE.read_text())
    old = json.loads((ROOT / f["source_fixture"]).read_text())
    templates = {n: base.atom(n, old["recipes"]["H"], old) for n in ("A", "B")}
    pair = base.disjoint_union(*templates.values())
    ports = {n: derived_c_ports(a) for n, a in templates.items()}
    check("C_ports_derived_from_P_E_edges", ports == {n: {"entry": n + "/C0", "exit": n + "/C2"} for n in templates})
    deuterium = base.atom("D", old["recipes"]["D"], old)
    check("neutron_changes_return_core_not_C_boundary", derived_c_ports(deuterium) == {"entry": "D/C0", "exit": "D/C2"})
    seams = candidate_seams(templates)
    check("two_oriented_cross_template_seams", seams == [("A/C2", "B/C0"), ("B/C2", "A/C0")])
    assemblies = []
    for size in range(3):
        for selection in combinations(seams, size):
            glued = graph_pushout(pair, selection)
            check("seam_count_" + str(len(assemblies)) + "_preserves_instances", len(glued["particle_instances"]) == 4 and Counter(p["family"] for p in glued["particle_instances"].values()) == Counter({"proton": 2, "electron": 2}))
            assemblies.append({"seams": selection, **glued})
    check("graph_gluing_sizes_10_9_9_8", [len(a["graph"]["nodes"]) for a in assemblies] == [10, 9, 9, 8])
    check("graph_gluing_connectivity", [len(a["weak_components"]) for a in assemblies] == [2, 1, 1, 1])
    check("only_reciprocal_gluing_closes_intertemplate_return", [len(a["cyclic_strong_components"]) for a in assemblies] == [0, 0, 0, 1])
    check("reciprocal_cycle_has_six_vertices_not_extra_wire_edges", len(assemblies[-1]["cyclic_strong_components"][0]) == 6)
    reverse_glue = graph_pushout(pair, list(reversed(seams)))
    check("graph_pushout_order_independent_with_all_fibres", assemblies[-1]["quotient"] == reverse_glue["quotient"] and assemblies[-1]["carrier_fibres"] == reverse_glue["carrier_fibres"])
    context = (f["common_boundary"]["evaluation_context"],) * 2
    law = f["seams"]["identity"]
    construct = lambda spec=law, contexts=context, assembly=pair, endpoint=seams[0]: seam_operator(assembly, endpoint, spec, contexts, f, seams)
    s = construct()
    r, e, p, n = (s[k] for k in ("R", "E", "P", "N"))
    check("identity_seam_derived_from_equal_value_assignments", s["compatible_assignments"] == [(0, 0), (1, 1)])
    check("restriction_extension_reconstructs_shared_carrier", base.mm(r, e) == eye(2))
    check("compatibility_projection_is_idempotent", base.mm(p, p) == p)
    check("compatibility_projection_rank_two", base.rank(p) == 2)
    check("shared_coordinate_is_faithful_on_pullback", len({law["left_restriction"][i] for i, j in s["compatible_assignments"]}) == len(s["compatible_assignments"]) == 2)
    encoder = r + n
    decoder = [row_e + row_i for row_e, row_i in zip(e, eye(4))]
    check("shared_plus_residual_packet_recovers_all_four_coordinates", base.mm(decoder, encoder) == eye(4))
    check("residual_is_transverse_to_compatible_domain", base.mm(r, n) == [[0] * 4 for _ in range(2)])
    check("restriction_alone_loses_mismatches", base.mv(r, [0, 1, 0, 0]) == [0, 0] and base.mv(n, [0, 1, 0, 0]) == [0, 1, 0, 0])
    compatible_witness = base.mv(p, [1, 1, 1, 1])
    check("equal_value_seam_has_nonproduct_compatibility_pattern", compatible_witness == [1, 0, 0, 1] and base.product_determinant(compatible_witness) == 1)
    check("diagonal_extension_is_not_tensor_square_cloning", base.mv(e, [1, 1]) != base.tensor_vector([1, 1], [1, 1]))
    check("seam_not_any_old_invertible_sign_box", all(p != x["full_matrix"] for x in report["diagonal_sign_class"]["candidates"]))
    refuses("no_default_missing_boundary_map", lambda: construct(spec={"left_restriction": [0, 1]}))
    refuses("different_evaluation_contexts_do_not_glue", lambda: construct(contexts=(context[0], "another-evaluation")))
    refuses("internal_C1_is_not_an_external_seam_port", lambda: construct(endpoint=("A/C1", "B/C0")))
    refuses("same_template_return_not_an_intertemplate_seam", lambda: construct(endpoint=("A/C2", "A/C0")))
    refuses("nonfaithful_boundary_map_is_not_carrier_identification", lambda: construct(spec={"left_restriction": [0, 0], "right_restriction": [0, 1]}))
    mismatch = deepcopy(pair)
    mismatch["ports"]["B/entry"]["field"] = "F2"
    refuses("coefficient_field_mismatch_blocks_sewing", lambda: construct(assembly=mismatch))
    twisted = construct(spec=f["seams"]["twisted"])
    check("twisted_map_changes_operator_without_changing_graph_gluing", twisted["P"] != p and twisted["compatible_assignments"] == [(0, 1), (1, 0)])
    census, faithful = [], []
    for left in product(range(2), repeat=2):
        for right in product(range(2), repeat=2):
            compatible = [(i, j) for i, j in product(range(2), repeat=2) if left[i] == right[j]]
            census.append({"left_map": left, "right_map": right, "compatible_assignments": compatible})
            if sorted(left) == [0, 1] and sorted(right) == [0, 1]:
                operator = construct(spec={"left_restriction": list(left), "right_restriction": list(right)})
                pa = [[Q(left[i] == j) for i in range(2)] for j in range(2)]
                pb = [[Q(right[i] == j) for i in range(2)] for j in range(2)]
                check("faithful_seam_" + str(len(faithful)) + "_explicit_value_transport", operator["R"] == base.mm(r, base.tensor_matrix(pa, pb)))
                faithful.append(operator)
    check("boundary_map_census_16_spans_only_four_faithful", len(census) == 16 and len(faithful) == 4)
    check("unfaithful_maps_change_pullback_cardinality", Counter(len(x["compatible_assignments"]) for x in census) == Counter({0: 2, 2: 12, 4: 2}))
    check("all_faithful_seams_have_two_retained_assignments", all(len(x["compatible_assignments"]) == 2 and base.rank(x["P"]) == 2 for x in faithful))
    i2, i4, i16 = eye(2), eye(4), eye(16)
    r_left = base.mm(base.tensor_matrix(i2, r), base.tensor_matrix(r, i4))
    r_right = base.mm(base.tensor_matrix(r, i2), base.tensor_matrix(i4, r))
    both_e = base.tensor_matrix(e, e)
    both_n = subtract(i16, base.mm(both_e, r_left))
    both_encoder = r_left + both_n
    both_decoder = [row_e + row_i for row_e, row_i in zip(both_e, i16)]
    check("two_seam_restriction_order_commutes", r_left == r_right == base.tensor_matrix(r, r))
    check("two_seam_compatible_domain_has_dimension_four", base.rank(r_left) == 4)
    check("two_seam_residual_has_dimension_twelve", base.rank(both_n) == 12)
    check("two_seam_full_packet_reconstruction", base.mm(both_decoder, both_encoder) == i16)
    x = [[0, 1], [1, 0]]
    relabel_left, relabel_right = base.mm(r, base.tensor_matrix(x, x)), base.mm(x, r)
    check("simultaneous_value_relabeling_is_covariant", relabel_left == relabel_right)
    witnesses = [
        ("graph_pushout_order", "labelled_carriers_10", "quotient_carriers_8", assemblies[-1]["quotient"], reverse_glue["quotient"], [["seam_A_to_B", "seam_B_to_A"], ["seam_B_to_A", "seam_A_to_B"]]),
        ("restriction_order", "Q16_boundary_assignments", "Q4_shared_assignments", r_left, r_right, [["R_tensor_I4", "I2_tensor_R"], ["I4_tensor_R", "R_tensor_I2"]]),
        ("retained_reconstruction", "Q16_boundary_assignments", "Q16_boundary_assignments", base.mm(both_decoder, both_encoder), i16, [["encode_shared_and_residual", "decode"], ["identity"]]),
        ("common_value_relabeling", "Q4_pair_assignments", "Q2_common_value", relabel_left, relabel_right, [["X_tensor_X", "R"], ["R", "X"]]),
    ]
    diagram = evaluated_diagram(witnesses)
    compiled = compiler.compile_diagram(diagram)
    check("SCC_evaluated_composites_have_four_verified_cells", compiled["passed"] and len(compiled["cells"]) == 4 and all(c["passed"] for c in compiled["cells"]))
    corrupt = deepcopy(diagram)
    arrow = next(a for a in corrupt["arrows"] if a["id"] == "restriction_order_left")
    arrow["evaluated_map"][0][0] += 1
    arrow["map_token"] = digest(arrow["evaluated_map"])
    bad = compiler.compile_diagram(corrupt)
    residual = subtract(arrow["evaluated_map"], r_right)
    check("coherence_hostile_fails_exactly_at_changed_cell", not bad["passed"] and [c["id"] for c in bad["cells"] if not c["passed"]] == ["restriction_order"] and base.rank(residual) == 1)
    DIAGRAM.parent.mkdir(parents=True, exist_ok=True)
    DIAGRAM.write_text(json.dumps(diagram, indent=2, default=str) + "\n")
    report["sewing"] = {"derived_ports": ports, "candidate_seams": seams, "assembly_cases": assemblies,
        "canonical_seam": s, "twisted_seam": twisted, "all_16_boundary_spans": census, "four_faithful_seams": faithful,
        "single_seam_encoder": encoder, "single_seam_decoder": decoder,
        "two_seam_source_factor_order": ["A/exit", "B/entry", "B/exit", "A/entry"],
        "two_seam_restriction": r_left, "two_seam_extension": both_e, "two_seam_residual": both_n,
        "two_seam_encoder": both_encoder, "two_seam_decoder": both_decoder,
        "categorical_diagram": str(DIAGRAM.relative_to(ROOT)).replace("\\", "/"),
        "diagram_sha256": sha256(DIAGRAM.read_bytes()).hexdigest(), "compiled_cells": compiled,
        "corruption_residual_rank": base.rank(residual)}
    report["survivor"] = "P/N/E graphs constrain C seam endpoints. Explicit common-context faithful value maps then force a pullback restriction, not a freely chosen sign box. Full ambient reconstruction requires the mismatch residual."
    report["missing_constructor"] = "P/N/E incidence does not select which seam/value identification occurs, native generator/junction maps, or a binding/stability law."


def main():
    paths = [FIXTURE, PACKET, MODEL, BASE_PATH, base.FIXTURE, base.VIEWER, COMPILER_PATH, Path(__file__).resolve()]
    report = {"schema": "marici.strominger.carrier-particle-sewing.verification.v1", "recorded_at": datetime.now(timezone.utc).isoformat(),
              "scope": "Forward graph sewing and static boundary-function pullback on supplied binary value spaces", "checks": {},
              "source_sha256": {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report["status"] = "pass"
    except Exception as error:
        report["status"] = "fail"
        report["error"] = repr(error)
        raise
    finally:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "verification.json").write_text(json.dumps(report, indent=2, default=str) + "\n")
        print(json.dumps({"status": report["status"], "check_groups": len(report["checks"]), "receipt": str((OUT / "verification.json").relative_to(ROOT)).replace("\\", "/")}))


if __name__ == "__main__":
    main()
