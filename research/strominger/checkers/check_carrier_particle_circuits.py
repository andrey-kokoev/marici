"""Exact finite carrier-circuit experiment. Standard library only; no physics readout.

The Q^2 boundary representation is supplied. Interior generators stay opaque.
A primitive edge shared by two windows is ONE edge with two provenance records,
not two independent operations. Instance lineage is retained separately.
"""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json
from itertools import product as cartesian
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "research/strominger/inputs/carrier-particle-circuits-v1.json"
VIEWER = ROOT / "research/strominger/demos/particle-overlap-tetrahedron/model.mjs"
PACKET = ROOT / "research/strominger/carrier-particle-circuits.md"
MODEL = ROOT / "research/strominger/scc-models/carrier-particle-circuits-v1.json"
RECEIPT = ROOT / "research/strominger/results/carrier-particle-circuits/verification.json"


def atom(name, recipe, fixture):
    result = {"nodes": {}, "particles": {}, "ports": {}, "boxes": {}}
    counts = Counter()
    for family in recipe:
        instance = f"{name}/{family}/{counts[family]}"
        counts[family] += 1
        walk = [f"{name}/{label}" for label in fixture["windows"][family]]
        result["particles"][instance] = {"family": family, "walk": walk}
        for node, label in zip(walk, fixture["windows"][family]):
            result["nodes"][node] = label[0]
    representation = fixture["boundary_representation"]
    for label, spec in fixture["ports"].items():
        node = f"{name}/{spec['carrier']}"
        if node not in result["nodes"]:
            raise ValueError("declared port has no carrier")
        result["ports"][f"{name}/{label}"] = {
            "node": node, "kind": result["nodes"][node],
            "direction": spec["direction"], "field": representation["field"],
            "basis": list(representation["ordered_basis"]),
        }
    return result


def disjoint_union(*assemblies):
    result = {"nodes": {}, "particles": {}, "ports": {}, "boxes": {}}
    for assembly in assemblies:
        for collection in result:
            if result[collection].keys() & assembly[collection].keys():
                raise ValueError("namespace collision; disjoint union cannot erase instances")
            result[collection].update(deepcopy(assembly[collection]))
    return result


def edge_provenance(assembly):
    provenance = {}
    for instance, particle in sorted(assembly["particles"].items()):
        for segment, (source, target) in enumerate(zip(particle["walk"], particle["walk"][1:])):
            provenance.setdefault((source, target), []).append([instance, segment])
    return [{"source": u, "target": v, "occurrences": slots}
            for (u, v), slots in sorted(provenance.items())]


def projection(assembly, boxes=True):
    """Opaque box incidence, NOT an assertion of nonzero coefficient influence."""
    nodes = set(assembly["nodes"])
    edges = {(e["source"], e["target"]) for e in edge_provenance(assembly)}
    if boxes:
        for box_id, box in assembly["boxes"].items():
            box_node = "@" + box_id
            nodes.add(box_node)
            edges.update((assembly["ports"][p]["node"], box_node) for p in box["inputs"])
            edges.update((box_node, assembly["ports"][p]["node"]) for p in box["outputs"])
    return {"nodes": sorted(nodes), "edges": [list(e) for e in sorted(edges)]}


def inventory(assembly):
    return dict(sorted(Counter(p["family"] for p in assembly["particles"].values()).items()))


def connectivity(graph):
    adjacency = {n: set() for n in graph["nodes"]}
    undirected = {n: set() for n in graph["nodes"]}
    for u, v in graph["edges"]:
        adjacency[u].add(v)
        undirected[u].add(v)
        undirected[v].add(u)

    def reachable(start, links):
        seen, todo = set(), [start]
        while todo:
            node = todo.pop()
            if node not in seen:
                seen.add(node)
                todo.extend(links[node] - seen)
        return seen

    reach = {n: reachable(n, adjacency) for n in adjacency}
    remaining, cyclic = set(adjacency), []
    while remaining:
        n = min(remaining)
        component = {m for m in remaining if m in reach[n] and n in reach[m]}
        remaining -= component
        if len(component) > 1 or n in adjacency[n]:
            cyclic.append(sorted(component))
    remaining, components = set(adjacency), []
    while remaining:
        component = reachable(min(remaining), undirected)
        remaining -= component
        components.append(sorted(component))
    return {"weak_components": components, "cyclic_strong_components": cyclic}


def source_matrix(rule):
    """Forward construction from a basis rule; no target matrix/readout fitting."""
    matrix = [[Q(0) for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            if rule == "identity":
                row, coefficient = 2 * i + j, 1
            elif rule == "swap":
                row, coefficient = 2 * j + i, 1
            elif rule == "bilinear_sign":
                row, coefficient = 2 * i + j, (-1) ** (i * j)
            else:
                raise ValueError("unknown source-operation rule")
            matrix[row][2 * i + j] = Q(coefficient)
    return matrix


def attach_box(assembly, box_id, inputs, outputs, rule):
    if box_id in assembly["boxes"]:
        raise ValueError("box identity collision")
    if len(inputs) != 2 or len(outputs) != 2 or len(set(inputs)) != 2 or len(set(outputs)) != 2:
        raise ValueError("a binary box requires two distinct factors per side")
    for port_ids, direction in ((inputs, "output"), (outputs, "input")):
        for port_id in port_ids:
            p = assembly["ports"][port_id]
            if (p["direction"], p["kind"], p["field"], p["basis"]) != (direction, "C", "Q", ["0", "1"]):
                raise ValueError("boundary type, variance, field or ordered basis mismatch")
    source_matrix(rule)
    result = deepcopy(assembly)
    result["boxes"][box_id] = {"inputs": list(inputs), "outputs": list(outputs), "rule": rule}
    return result


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def tensor_vector(a, b):
    return [Q(x) * Q(y) for x in a for y in b]


def tensor_matrix(a, b):
    return [[Q(a[i][k]) * Q(b[j][l]) for k in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for j in range(len(b))]


def rank(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    r = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][column]
        a[r] = [v / scale for v in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = a[i][column]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def operator_tensor_rank(b):
    # R(B)[(i,k),(j,l)] = B[(i,j),(k,l)] for FIXED named factor pairing.
    realigned = [[b[2 * i + j][2 * k + l] for j in range(2) for l in range(2)]
                 for i in range(2) for k in range(2)]
    return rank(realigned)


def product_determinant(v):
    return v[0] * v[3] - v[1] * v[2]


def wire_report(assembly):
    graph = projection(assembly)
    return {"inventory": inventory(assembly), "primitive_edges": edge_provenance(assembly),
            "open_assembly": assembly, "incidence_projection": graph, **connectivity(graph)}


def run(report):
    f = json.loads(FIXTURE.read_text(encoding="utf-8"))
    checks = report["checks"]

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    def refuses(name, operation):
        try:
            operation()
        except ValueError:
            check(name, True)
        else:
            check(name, False)

    found = {}
    pattern = r"id:\s*['\"](proton|neutron|electron)['\"][^{}\n]*?nodes:\s*\[([^\]]+)\]"
    for family, body in re.findall(pattern, VIEWER.read_text(encoding="utf-8")):
        found[family] = re.findall(r"['\"]([CM][0-9]+)['\"]", body)
    check("windows_match_existing_viewer_source", found == f["windows"])
    check("corrected_neutron_has_distinct_outer_carriers", f["windows"]["neutron"] == ["M0", "C1", "M1"])
    h = atom("H", f["recipes"]["H"], f)
    d = atom("D", f["recipes"]["D"], f)
    duplicate = atom("D", f["recipes"]["duplicate_N_control"], f)
    check("H_inventory", inventory(h) == {"electron": 1, "proton": 1})
    check("D_inventory", inventory(d) == {"electron": 1, "neutron": 1, "proton": 1})
    check("H_has_no_directed_return_loop", not connectivity(projection(h))["cyclic_strong_components"])
    check("D_has_exact_C1_M1_return_core", connectivity(projection(d))["cyclic_strong_components"] == [["D/C1", "D/M1"]])
    check("bare_graph_loses_duplicate_neutron", projection(d) == projection(duplicate) and inventory(d) != inventory(duplicate))
    shared = next(e for e in edge_provenance(d) if (e["source"], e["target"]) == ("D/M0", "D/C1"))
    check("shared_primitive_is_one_operation_with_two_window_occurrences", len(shared["occurrences"]) == 2)
    check("all_three_positions_of_each_particle_retained", all(len(p["walk"]) == 3 for p in d["particles"].values()))
    check("opposite_arrows_are_not_cancelled", ["D/C1", "D/M1"] in projection(d)["edges"] and ["D/M1", "D/C1"] in projection(d)["edges"])

    a, b, c = [atom(name, f["recipes"]["H"], f) for name in ("A", "B", "C")]
    pair = disjoint_union(a, b)
    check("disjoint_union_preserves_four_instances", inventory(pair) == {"electron": 2, "proton": 2})
    check("separated_pair_has_two_components", len(connectivity(projection(pair))["weak_components"]) == 2)
    check("disjoint_union_commutes_with_named_instances", pair == disjoint_union(b, a))
    check("disjoint_union_is_associative", disjoint_union(disjoint_union(a, b), c) == disjoint_union(a, disjoint_union(b, c)))
    refuses("namespace_collision_cannot_silently_identify_particles", lambda: disjoint_union(a, a))
    inputs, outputs = ("A/exit", "B/exit"), ("A/entry", "B/entry")
    refuses("M_input_is_not_a_C_output_port", lambda: attach_box(pair, "bad", ("A/excitation", "B/exit"), outputs, "identity"))
    refuses("repeated_factor_is_not_binary_composition", lambda: attach_box(pair, "bad", ("A/exit", "A/exit"), outputs, "identity"))
    wrong_field = deepcopy(pair)
    wrong_field["ports"]["B/exit"]["field"] = "F2"
    refuses("equal_dimension_does_not_repair_field_mismatch", lambda: attach_box(wrong_field, "bad", inputs, outputs, "identity"))
    wrong_basis = deepcopy(pair)
    wrong_basis["ports"]["B/exit"]["basis"] = ["1", "0"]
    refuses("basis_reordering_requires_explicit_transport", lambda: attach_box(wrong_basis, "bad", inputs, outputs, "identity"))

    matrices = {name: source_matrix(spec["rule"]) for name, spec in f["couplers"].items()}
    boxes = {name: attach_box(pair, "B", inputs, outputs, spec["rule"]) for name, spec in f["couplers"].items()}
    identity, swap, sign = [matrices[n] for n in ("independent", "exchange", "pair_sign")]
    check("same_wiring_does_not_select_an_interaction", len({json.dumps(projection(x), sort_keys=True) for x in boxes.values()}) == 1)
    check("all_boxes_preserve_particle_inventory", all(inventory(x) == inventory(pair) for x in boxes.values()))
    check("opaque_box_incidence_connects_the_pair", all(len(connectivity(projection(x))["weak_components"]) == 1 for x in boxes.values()))
    check("opaque_box_incidence_closes_return_paths", all(len(connectivity(projection(x))["cyclic_strong_components"]) == 1 for x in boxes.values()))
    refuses("box_id_collision_is_not_overwrite", lambda: attach_box(boxes["independent"], "B", inputs, outputs, "identity"))

    u, v = f["product_input_witness"]["left"], f["product_input_witness"]["right"]
    product = tensor_vector(u, v)
    moved = {name: mv(matrix, product) for name, matrix in matrices.items()}
    expected_ranks = {"independent": 1, "exchange": 4, "pair_sign": 2}
    expected_determinants = {"independent": 0, "exchange": 0, "pair_sign": -2}
    local_left = tensor_matrix([[1, 1], [0, 1]], [[1, 0], [1, 1]])
    local_right = tensor_matrix([[1, 0], [1, 1]], [[1, 1], [0, 1]])
    for name, matrix in matrices.items():
        check(name + "_operator_tensor_rank", operator_tensor_rank(matrix) == expected_ranks[name])
        check(name + "_output_product_determinant", product_determinant(moved[name]) == expected_determinants[name])
        check(name + "_orthogonal", mm(transpose(matrix), matrix) == identity)
        check(name + "_local_basis_transport_preserves_rank", operator_tensor_rank(mm(mm(local_left, matrix), local_right)) == expected_ranks[name])
    basis = [[1, 0], [0, 1]]
    check("swap_bilinear_identity_on_complete_product_basis", all(mv(swap, tensor_vector(x, y)) == tensor_vector(y, x) for x in basis for y in basis))
    check("nonfactor_operator_need_not_correlate_product_inputs", operator_tensor_rank(swap) > 1 and all(mv(swap, tensor_vector(x, y)) == tensor_vector(y, x) for x in basis for y in basis))
    check("pair_sign_has_nonproduct_output_witness", product_determinant(moved["pair_sign"]) != 0)
    check("coordinate_magnitudes_lose_product_factorization", [x * x for x in moved["independent"]] == [x * x for x in moved["pair_sign"]] and product_determinant(moved["independent"]) != product_determinant(moved["pair_sign"]))
    check("named_factor_pairing_matters", operator_tensor_rank(mm(identity, swap)) != operator_tensor_rank(identity))
    check("consistent_global_factor_reordering_preserves_operators", all(mm(mm(swap, matrix), swap) == matrix for matrix in matrices.values()))
    # No B^2 carrier claim: B goes from named exit ports to entry ports.
    # Interior/return maps are opaque, even though its coordinate array is square.
    patterns = list(cartesian((-1, 1), repeat=4))
    candidates, orbits = [], set()
    for d_signs in patterns:
        chi = d_signs[0] * d_signs[1] * d_signs[2] * d_signs[3]
        diagonal = [[Q(d_signs[i] if i == j else 0) for j in range(4)] for i in range(4)]
        orbit = frozenset(tuple(a[i] * b[j] * d_signs[2 * i + j] for i in range(2) for j in range(2))
                          for a in cartesian((-1, 1), repeat=2) for b in cartesian((-1, 1), repeat=2))
        orbits.add(orbit)
        local_a, local_b = [1, d_signs[2] * d_signs[0]], [d_signs[0], d_signs[1]]
        normalized = [local_a[i] * local_b[j] * d_signs[2 * i + j] for i in range(2) for j in range(2)]
        candidates.append({"signs": d_signs, "full_matrix": diagonal, "chi": chi,
                           "operator_tensor_rank": operator_tensor_rank(diagonal),
                           "full_output": mv(diagonal, product),
                           "output_product_determinant": product_determinant(mv(diagonal, product)),
                           "local_output_sign_normalizer": {"left": local_a, "right": local_b},
                           "normalized_signs": normalized})
    check("sign_class_exhausts_16_independent_sign_patterns", len(candidates) == 16 and len(set(patterns)) == 16)
    check("sign_class_all_preserve_declared_coordinate_metric", all(mm(transpose(x["full_matrix"]), x["full_matrix"]) == identity for x in candidates))
    check("sign_class_has_exactly_two_local_operation_orbits", len(orbits) == 2)
    check("sign_class_orbits_have_eight_members_each", sorted(map(len, orbits)) == [8, 8])
    check("sign_class_chi_is_complete_orbit_invariant", all(len({d[0] * d[1] * d[2] * d[3] for d in orbit}) == 1 for orbit in orbits))
    check("sign_class_normalizer_explicitly_preserves_factor_pairing", all(x["normalized_signs"] == [1, 1, 1, x["chi"]] for x in candidates))
    check("sign_class_product_operator_iff_chi_positive", all((x["operator_tensor_rank"] == 1) == (x["chi"] == 1) for x in candidates))
    check("sign_class_joint_operator_rank_exactly_two", all(x["operator_tensor_rank"] == (1 if x["chi"] == 1 else 2) for x in candidates))
    check("sign_class_product_witness_correlates_iff_chi_negative", all((x["output_product_determinant"] != 0) == (x["chi"] == -1) for x in candidates))
    check("exchange_is_not_a_diagonal_sign_candidate", all(x["full_matrix"] != swap for x in candidates))
    report["diagonal_sign_class"] = {"candidate_count": len(candidates), "orbit_count": len(orbits),
        "equivalence": "Independent named-factor output sign operations; not equality of full operators or a native quotient",
        "invariant": "chi=d00*d01*d10*d11", "candidates": candidates,
        "orbits": [sorted(orbit) for orbit in sorted(orbits, key=lambda orbit: sorted(orbit))]}

    report["assemblies"] = {"H": wire_report(h), "D": wire_report(d), "duplicate_N_control": wire_report(duplicate), "separated_H_pair": wire_report(pair), **{name + "_box": wire_report(x) for name, x in boxes.items()}}
    report["boundary_packet"] = {"field": "Q", "input_factors": list(inputs), "output_factors": list(outputs), "basis_order": ["00", "01", "10", "11"], "product_input": product, "couplers": {name: {"source_rule": f["couplers"][name]["rule"], "full_matrix": matrix, "operator_tensor_rank": operator_tensor_rank(matrix), "full_output": moved[name], "output_product_determinant": product_determinant(moved[name])} for name, matrix in matrices.items()}}
    report["survivor"] = "Keep component-instance lineage, shared primitive provenance, ordered ports and full operators. Port wiring alone does not distinguish independent, exchange and correlating coupling."
    report["missing_constructor"] = "Source-derived interior generator/junction representation, entry-to-exit return map and interaction selection; no end-to-end particle or binding dynamics constructed."


def main():
    report = {"schema": "marici.strominger.carrier-particle-circuits.verification.v1", "recorded_at": datetime.now(timezone.utc).isoformat(), "scope": "finite declared formal carrier fixture, not native atom dynamics", "checks": {}}
    report["source_sha256"] = {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p.read_bytes()).hexdigest() for p in (FIXTURE, VIEWER, PACKET, MODEL, Path(__file__).resolve())}
    try:
        run(report)
        report["status"] = "pass"
    except Exception as error:
        report["status"] = "fail"
        report["error"] = repr(error)
        raise
    finally:
        RECEIPT.parent.mkdir(parents=True, exist_ok=True)
        RECEIPT.write_text(json.dumps(report, indent=2, default=lambda x: str(x) if isinstance(x, Q) else x) + "\n", encoding="utf-8")
        print(json.dumps({"status": report["status"], "check_groups": len(report["checks"]), "receipt": str(RECEIPT.relative_to(ROOT)).replace("\\", "/")}))


if __name__ == "__main__":
    main()
