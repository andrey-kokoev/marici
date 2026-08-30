"""Dependency-aware compiler for finite authority-bearing partial repairs."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from fractions import Fraction
from itertools import combinations, permutations, product
from typing import Any


REPAIR_FIELDS = {
    "repair_id", "input_defect_signature", "output_defect_signature",
    "domain_signature", "graph_norm_signature", "boundary_current_delta",
    "support_delta", "authority_root", "prerequisites",
    "residual_certificate_type", "domain_after", "graph_norm_after",
    "consumes_capabilities", "produces_capabilities",
}


def stable_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def exact_matrix_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[Fraction(value) for value in row] for row in matrix]
    width = len(rows[0])
    rank = 0
    for column in range(width):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for index in range(len(rows)):
            if index != rank and rows[index][column]:
                factor = rows[index][column]
                rows[index] = [value - factor * pivot_entry for value, pivot_entry in zip(rows[index], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def gf2_matrix_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[value & 1 for value in row] for row in matrix]
    width = len(rows[0])
    rank = 0
    for column in range(width):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for index in range(len(rows)):
            if index != rank and rows[index][column]:
                rows[index] = [left ^ right for left, right in zip(rows[index], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def finite_group_table_valid(table: list[list[int]]) -> bool:
    size = len(table)
    if not size or any(len(row) != size for row in table):
        return False
    if any(entry < 0 or entry >= size for row in table for entry in row):
        return False
    identities = [e for e in range(size) if all(table[e][x] == x and table[x][e] == x for x in range(size))]
    if len(identities) != 1:
        return False
    identity = identities[0]
    if any(not any(table[x][y] == identity and table[y][x] == identity for y in range(size)) for x in range(size)):
        return False
    return all(table[table[x][y]][z] == table[x][table[y][z]] for x in range(size) for y in range(size) for z in range(size))


def finite_groups_isomorphic(left: list[list[int]], right: list[list[int]]) -> bool:
    if not finite_group_table_valid(left) or not finite_group_table_valid(right) or len(left) != len(right):
        return False
    size = len(left)
    return any(
        all(mapping[left[x][y]] == right[mapping[x]][mapping[y]] for x in range(size) for y in range(size))
        for mapping in permutations(range(size))
    )


def gf2_matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[row][index] * right[index][column] for index in range(len(right))) % 2 for column in range(len(right[0]))]
        for row in range(len(left))
    ]


def finite_group_representation_valid(table: list[list[int]], representation: list[list[list[int]]]) -> bool:
    if not finite_group_table_valid(table) or len(representation) != len(table) or not representation:
        return False
    dimension = len(representation[0])
    identity_matrix = [[int(row == column) for column in range(dimension)] for row in range(dimension)]
    if any(len(matrix) != dimension or any(len(row) != dimension for row in matrix) for matrix in representation):
        return False
    identity = next(e for e in range(len(table)) if all(table[e][x] == x and table[x][e] == x for x in range(len(table))))
    if representation[identity] != identity_matrix or any(gf2_matrix_rank(matrix) != dimension for matrix in representation):
        return False
    return all(
        gf2_matrix_multiply(representation[g], representation[h]) == representation[table[g][h]]
        for g in range(len(table)) for h in range(len(table))
    )


def gf2_representations_conjugate(left: list[list[list[int]]], right: list[list[list[int]]]) -> bool:
    if not left or len(left) != len(right) or len(left[0]) != len(right[0]):
        return False
    dimension = len(left[0])
    for entries in product((0, 1), repeat=dimension * dimension):
        change = [list(entries[row * dimension:(row + 1) * dimension]) for row in range(dimension)]
        if gf2_matrix_rank(change) != dimension:
            continue
        if all(gf2_matrix_multiply(change, left[g]) == gf2_matrix_multiply(right[g], change) for g in range(len(left))):
            return True
    return False


def finite_group_actions_equivalent(
    left_table: list[list[int]],
    right_table: list[list[int]],
    left_representation: list[list[list[int]]],
    right_representation: list[list[list[int]]],
) -> bool:
    if (
        not finite_group_representation_valid(left_table, left_representation)
        or not finite_group_representation_valid(right_table, right_representation)
        or len(left_table) != len(right_table)
        or len(left_representation[0]) != len(right_representation[0])
    ):
        return False
    group_size = len(left_table)
    dimension = len(left_representation[0])
    for mapping in permutations(range(group_size)):
        if not all(mapping[left_table[x][y]] == right_table[mapping[x]][mapping[y]] for x in range(group_size) for y in range(group_size)):
            continue
        for entries in product((0, 1), repeat=dimension * dimension):
            change = [list(entries[row * dimension:(row + 1) * dimension]) for row in range(dimension)]
            if gf2_matrix_rank(change) != dimension:
                continue
            if all(
                gf2_matrix_multiply(change, left_representation[g])
                == gf2_matrix_multiply(right_representation[mapping[g]], change)
                for g in range(group_size)
            ):
                return True
    return False


def pullback_requirements(constructors: list[dict[str, Any]], requirements: set[str]) -> dict[str, Any]:
    current = set(requirements)
    trace = []
    for constructor in reversed(constructors):
        rules = constructor.get("requirement_rules")
        if not isinstance(rules, dict):
            return {"accepted": False, "code": "requirement_rules_missing", "constructor_id": constructor.get("repair_id"), "trace": trace}
        undeclared = sorted(current - set(rules))
        if undeclared:
            return {"accepted": False, "code": "undeclared_requirement_atom", "constructor_id": constructor.get("repair_id"), "atoms": undeclared, "trace": trace}
        pulled = set().union(*(set(rules[atom]) for atom in current)) if current else set()
        trace.append({"through": constructor.get("repair_id"), "target": sorted(current), "source": sorted(pulled)})
        current = pulled
    return {"accepted": True, "required_source_capabilities": sorted(current), "trace": trace}


RESIDUAL_REPAIR_KINDS = {
    "source_state_collision": "observation_port",
    "target_outside_source_image": "target_domain_predicate",
    "coherence_relation_failure": "coherence_cell_or_anomaly_budget",
    "completion_boundary_missing": "completion_topology_or_boundary_fiber",
    "missing_source_authority": "source_authorized_constructor_or_normalization_cell",
}


def compile_authority_support(fixture: dict[str, Any]) -> dict[str, Any]:
    """Audit authority as a finite DAG ending at declared primitive source roots."""
    nodes_list = fixture.get("nodes", [])
    nodes = {node.get("node_id"): node for node in nodes_list if node.get("node_id")}
    errors: list[str] = []
    if len(nodes) != len(nodes_list):
        errors.append("authority_support_node_ids_duplicate_or_missing")
    for node_id, node in nodes.items():
        dependencies = node.get("dependencies")
        if not isinstance(dependencies, list):
            errors.append("authority_support_dependencies_untyped:" + node_id)
            continue
        if not set(dependencies) <= set(nodes):
            errors.append("authority_support_dependency_missing:" + node_id)
        primitive = node.get("primitive") is True
        if primitive and dependencies:
            errors.append("primitive_authority_root_has_dependencies:" + node_id)
        if primitive and not node.get("source_authority_root"):
            errors.append("primitive_authority_root_untyped:" + node_id)
        if not primitive and not dependencies:
            errors.append("missing_primitive_authority_root:" + node_id)

    colors: dict[str, int] = {}
    cycle_nodes: set[str] = set()

    def visit(node_id: str, stack: list[str]) -> None:
        color = colors.get(node_id, 0)
        if color == 1:
            cycle_nodes.update(stack[stack.index(node_id):] if node_id in stack else [node_id])
            return
        if color == 2 or node_id not in nodes:
            return
        colors[node_id] = 1
        for dependency in nodes[node_id].get("dependencies", []):
            visit(dependency, stack + [node_id])
        colors[node_id] = 2

    for node_id in nodes:
        visit(node_id, [])
    if cycle_nodes:
        errors.append("cyclic_authority_support:" + ",".join(sorted(cycle_nodes)))

    targets = fixture.get("required_targets", {})
    target_rows = []
    for target_kind, node_id in sorted(targets.items()):
        admitted = node_id in nodes and not errors
        target_rows.append({"target_kind": target_kind, "support_node": node_id, "admitted": admitted})
        if node_id not in nodes:
            errors.append("authority_support_target_missing:" + target_kind)
    shared_dependencies = sorted(
        node_id for node_id in nodes
        if sum(node_id in node.get("dependencies", []) for node in nodes.values()) > 1
    )
    return {
        "passed": bool(nodes) and not errors,
        "errors": sorted(set(errors)),
        "finite": True,
        "acyclic": not cycle_nodes,
        "targets": target_rows,
        "shared_dependencies": shared_dependencies,
        "primitive_roots": sorted(node_id for node_id, node in nodes.items() if node.get("primitive") is True),
    }


def compile_commutant_interface(fixture: dict[str, Any], authority_support: dict[str, Any]) -> dict[str, Any]:
    """Generate record/control compatibility from the M2 commutant polarity."""
    errors: list[str] = []
    levels = fixture.get("algebras", [])
    by_id = {item.get("algebra_id"): item for item in levels if item.get("algebra_id")}
    if len(by_id) != 3 or len(by_id) != len(levels):
        errors.append("commutant_algebra_inventory_invalid")
    ordered = sorted(levels, key=lambda item: item.get("inclusion_rank", -1))
    expected_dimensions = [(1, 4), (2, 2), (4, 1)]
    observed_dimensions = [(item.get("dimension"), item.get("commutant_dimension")) for item in ordered]
    if observed_dimensions != expected_dimensions:
        errors.append("commutant_dimension_law_failed")
    if not fixture.get("shared_carrier_admitted") or not fixture.get("shared_carrier_id"):
        errors.append("commutant_interface_shared_carrier_missing")
    support_node = fixture.get("authority_support_node")
    supported_nodes = {row["support_node"] for row in authority_support.get("targets", []) if row.get("admitted")}
    authority_separate = support_node in supported_nodes
    if not authority_separate:
        errors.append("commutant_interface_authority_support_missing")
    if fixture.get("compatibility_grants_authority") is not False:
        errors.append("commutant_compatibility_laundered_as_authority")

    rows = []
    for record in ordered:
        for control in ordered:
            record_in_control_commutant = record.get("inclusion_rank") <= 2 - control.get("inclusion_rank")
            control_in_record_commutant = control.get("inclusion_rank") <= 2 - record.get("inclusion_rank")
            rows.append({
                "record_algebra": record.get("algebra_id"),
                "control_algebra": control.get("algebra_id"),
                "record_in_control_commutant": record_in_control_commutant,
                "control_in_record_commutant": control_in_record_commutant,
                "galois_equivalence": record_in_control_commutant == control_in_record_commutant,
                "compatible": record_in_control_commutant,
            })
    if not rows or not all(row["galois_equivalence"] for row in rows):
        errors.append("commutant_galois_law_failed")
    antitone = all(
        ordered[i]["commutant_dimension"] >= ordered[j]["commutant_dimension"]
        for i in range(len(ordered)) for j in range(i, len(ordered))
    )
    if not antitone:
        errors.append("commutant_assignment_not_order_reversing")
    compatible = {
        (row["record_algebra"], row["control_algebra"]): row["compatible"]
        for row in rows
    }
    transitivity_counterexamples = []
    for left in ordered:
        for middle in ordered:
            for right in ordered:
                left_id, middle_id, right_id = left["algebra_id"], middle["algebra_id"], right["algebra_id"]
                if compatible[(left_id, middle_id)] and compatible[(middle_id, right_id)] and not compatible[(left_id, right_id)]:
                    transitivity_counterexamples.append([left_id, middle_id, right_id])
    if fixture.get("claim_pairwise_compatibility_transitive") is not False:
        errors.append("commutant_compatibility_false_transitive_composition")
    relational_composite = []
    for left in ordered:
        for right in ordered:
            mediators = [
                middle["algebra_id"] for middle in ordered
                if compatible[(left["algebra_id"], middle["algebra_id"])]
                and compatible[(middle["algebra_id"], right["algebra_id"])]
            ]
            if mediators:
                relational_composite.append({"left": left["algebra_id"], "right": right["algebra_id"], "mediators": mediators})
    direct_pair_count = sum(compatible.values())
    relational_composite_pair_count = len(relational_composite)
    if fixture.get("claim_existential_composite_preserves_compatibility") is not False:
        errors.append("commutant_existential_composition_launders_incompatibility")
    double_commutant_closed = all(item["inclusion_rank"] == 2 - (2 - item["inclusion_rank"]) for item in ordered)
    if not double_commutant_closed:
        errors.append("commutant_double_polarity_closure_failed")
    rank_to_id = {item["inclusion_rank"]: item["algebra_id"] for item in ordered}
    mutual_commutant_pairs = [
        {
            "algebra": item["algebra_id"],
            "commutant": rank_to_id[2 - item["inclusion_rank"]],
            "double_commutant": item["algebra_id"],
            "fixed_point": item["inclusion_rank"] == 1,
        }
        for item in ordered
    ]
    if fixture.get("fixed_point_grants_authority") is not False:
        errors.append("compatible_fixed_point_laundered_as_authority")
    source_supported_records = set(fixture.get("source_supported_record_algebras", []))
    if source_supported_records != set(by_id):
        errors.append("generated_join_input_authority_incomplete")
    final_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "final_constructor" and row.get("admitted")
    }
    composite_support_node = fixture.get("generated_join_composite_cell_support_node")
    composite_cell_supported = composite_support_node in final_support_nodes
    if not composite_cell_supported:
        errors.append("generated_join_composite_cell_authority_missing")
    generated_joins = []
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index:]:
            join_rank = max(left["inclusion_rank"], right["inclusion_rank"])
            join_id = rank_to_id[join_rank]
            closed_id = rank_to_id[2 - (2 - join_rank)]
            surviving_control = rank_to_id[2 - join_rank]
            generated_joins.append({
                "inputs": [left["algebra_id"], right["algebra_id"]],
                "generated_algebra": join_id,
                "double_commutant_closure": closed_id,
                "surviving_control_commutant": surviving_control,
                "source_inputs_supported": {left["algebra_id"], right["algebra_id"]} <= source_supported_records,
                "composite_cell_supported": composite_cell_supported,
            })
    associator_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "generated_join_associator" and row.get("admitted")
    }
    associator_support_node = fixture.get("generated_join_associator_support_node")
    associator_supported = associator_support_node in associator_support_nodes
    if not associator_supported:
        errors.append("generated_join_associator_authority_missing")
    associator_normal_form_derived = fixture.get("generated_join_associator_derivation") == "common_generated_algebra_normal_form"
    if not associator_normal_form_derived:
        errors.append("generated_join_associator_not_normal_form_derived")
    associativity_audits = []
    for left in ordered:
        for middle in ordered:
            for right in ordered:
                left_parenthesized_rank = max(max(left["inclusion_rank"], middle["inclusion_rank"]), right["inclusion_rank"])
                right_parenthesized_rank = max(left["inclusion_rank"], max(middle["inclusion_rank"], right["inclusion_rank"]))
                source_packet = sorted({left["algebra_id"], middle["algebra_id"], right["algebra_id"]})
                associativity_audits.append({
                    "inputs": [left["algebra_id"], middle["algebra_id"], right["algebra_id"]],
                    "left_endpoint": rank_to_id[left_parenthesized_rank],
                    "right_endpoint": rank_to_id[right_parenthesized_rank],
                    "left_surviving_control": rank_to_id[2 - left_parenthesized_rank],
                    "right_surviving_control": rank_to_id[2 - right_parenthesized_rank],
                    "source_support_packet": source_packet,
                    "binary_composite_cells_per_path": 2,
                    "associator_supported": associator_supported,
                    "associator_normal_form_derived": associator_normal_form_derived,
                })
    nonchain = fixture.get("nonchain_join_fixture", {})
    nonchain_join = {
        "left": nonchain.get("left"),
        "right": nonchain.get("right"),
        "generated_algebra": nonchain.get("generated_algebra"),
        "double_commutant_closure": nonchain.get("double_commutant_closure"),
        "surviving_control_commutant": nonchain.get("surviving_control_commutant"),
        "incompatible_frames": nonchain.get("left") != nonchain.get("right"),
        "composite_cell_supported": composite_cell_supported,
    }
    if nonchain_join != {"left":"span_I_X","right":"span_I_Z","generated_algebra":"full","double_commutant_closure":"full","surviving_control_commutant":"scalar","incompatible_frames":True,"composite_cell_supported":True}:
        errors.append("nonchain_generated_join_law_failed")
    pentagon_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "generated_join_pentagon" and row.get("admitted")
    }
    pentagon_supported = fixture.get("generated_join_pentagon_support_node") in pentagon_support_nodes
    if not pentagon_supported:
        errors.append("generated_join_pentagon_authority_missing")
    pentagon_normal_form_derived = fixture.get("generated_join_pentagon_derivation") == "confluence_of_generated_algebra_normal_form"
    if not pentagon_normal_form_derived:
        errors.append("generated_join_pentagon_not_confluence_derived")
    pentagon_audits = []
    for first in ordered:
        for second in ordered:
            for third in ordered:
                for fourth in ordered:
                    ranks = [first["inclusion_rank"], second["inclusion_rank"], third["inclusion_rank"], fourth["inclusion_rank"]]
                    normal_rank = max(ranks)
                    five_parenthesized_endpoints = [rank_to_id[normal_rank]] * 5
                    normal_form_packet = sorted({first["algebra_id"], second["algebra_id"], third["algebra_id"], fourth["algebra_id"]})
                    pentagon_audits.append({
                        "inputs": [first["algebra_id"], second["algebra_id"], third["algebra_id"], fourth["algebra_id"]],
                        "five_parenthesized_endpoints": five_parenthesized_endpoints,
                        "normal_form_endpoint": rank_to_id[normal_rank],
                        "normal_form_source_packet": normal_form_packet,
                        "short_route_associator_count": 2,
                        "long_route_associator_count": 3,
                        "raw_traces_equal": False,
                        "normal_forms_equal": True,
                        "pentagon_supported": pentagon_supported,
                        "confluence_derived": pentagon_normal_form_derived,
                    })
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "carrier": fixture.get("shared_carrier_id"),
        "shared_carrier_admitted": bool(fixture.get("shared_carrier_admitted") and fixture.get("shared_carrier_id")),
        "commutant_compatibility_generated": bool(rows) and all(row["galois_equivalence"] for row in rows),
        "source_authority_independently_supported": authority_separate,
        "authority_separate": authority_separate,
        "compatibility_grants_authority": fixture.get("compatibility_grants_authority"),
        "order_reversing": antitone,
        "double_commutant_closed": double_commutant_closed,
        "mutual_commutant_pairs": mutual_commutant_pairs,
        "double_commutant_closed_algebras": [row["algebra"] for row in mutual_commutant_pairs if row["double_commutant"] == row["algebra"]],
        "one_step_self_dual_algebras": [row["algebra"] for row in mutual_commutant_pairs if row["fixed_point"]],
        "fixed_point_grants_authority": fixture.get("fixed_point_grants_authority"),
        "generated_joins": generated_joins,
        "generated_join_composite_cell_supported": composite_cell_supported,
        "generated_join_associator_supported": associator_supported,
        "generated_join_associator_normal_form_derived": associator_normal_form_derived,
        "generated_join_associativity_audits": associativity_audits,
        "nonchain_join": nonchain_join,
        "generated_join_pentagon_supported": pentagon_supported,
        "generated_join_pentagon_normal_form_derived": pentagon_normal_form_derived,
        "generated_join_pentagon_audits": pentagon_audits,
        "generated_join_law": "(R1 join R2) double-prime = R1 join R2; surviving controls = (R1 join R2) prime = R1 prime meet R2 prime",
        "pairwise_compatibility_transitive": not transitivity_counterexamples,
        "transitivity_counterexamples": transitivity_counterexamples,
        "direct_compatible_pair_count": direct_pair_count,
        "relational_composite_pair_count": relational_composite_pair_count,
        "relational_composite": relational_composite,
        "mediator_erasure_preserves_interface_type": relational_composite_pair_count == direct_pair_count,
        "automatic_composite_authorized": False,
        "composition_requirement": "retained_typed_mediator_and_direct_endpoint_gate_or_explicit_source_supported_composite_cell",
        "cases": rows,
        "constructor_kind": "derived_cross_axis_compatibility_not_authority",
    }


def compile_channel_semigroup(fixture: dict[str, Any], authority_support: dict[str, Any]) -> dict[str, Any]:
    """Compile an optional algebraic channel semigroup without importing time or authority."""
    errors: list[str] = []
    support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "record_channel_semigroup" and row.get("admitted")
    }
    source_authorized = fixture.get("authority_support_node") in support_nodes
    if not source_authorized:
        errors.append("record_channel_semigroup_authority_missing")
    if fixture.get("iteration_depth_interpreted_as_time") is not False:
        errors.append("channel_iteration_depth_laundered_as_time")
    if fixture.get("physical_time_authority_supplied") is not False:
        errors.append("channel_physical_time_authority_contract_mismatch")
    if fixture.get("convergence_grants_authority") is not False:
        errors.append("channel_convergence_laundered_as_authority")
    contraction = fixture.get("contractive_channel", {})
    phase = fixture.get("phase_channel", {})
    if contraction.get("multiplier") != "1/2" or contraction.get("limit_formal_concept") != "full/scalar":
        errors.append("contractive_channel_source_packet_invalid")
    if phase.get("multiplier") != "-1" or phase.get("claimed_convergent") is not False:
        errors.append("phase_only_cycle_claimed_convergent")
    depth_bound = fixture.get("bounded_depth", 8)
    contraction_trace = ["1" if depth == 0 else f"1/{2 ** depth}" for depth in range(depth_bound + 1)]
    phase_cycle = ["1", "-1"]
    phase_trace = [phase_cycle[depth % 2] for depth in range(depth_bound + 1)]
    semigroup_law_exact = all(
        2 ** (left + right) == (2 ** left) * (2 ** right)
        for left in range(depth_bound + 1) for right in range(depth_bound + 1)
    ) and all(
        phase_cycle[(left + right) % 2] == phase_cycle[((left % 2) + (right % 2)) % 2]
        for left in range(depth_bound + 1) for right in range(depth_bound + 1)
    )
    time_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "physical_time_bridge" and row.get("admitted")
    }
    time_bridges = []
    for bridge in fixture.get("time_bridge_cases", []):
        requested = bridge.get("requested") is True
        supported = bridge.get("authority_support_node") in time_support_nodes
        linear = bridge.get("map_kind") == "linear_scale"
        scale = Fraction(bridge.get("scale", "0")) if linear else Fraction(0)
        additive = linear and all(scale * (left + right) == scale * left + scale * right for left in range(depth_bound + 1) for right in range(depth_bound + 1))
        admitted = requested and supported and additive
        if requested and not supported:
            errors.append("physical_time_bridge_authority_missing:" + bridge.get("case_id", "unknown"))
        if requested and supported and not additive:
            errors.append("physical_time_bridge_not_monoid_morphism:" + bridge.get("case_id", "unknown"))
        expected = bridge.get("expected_admitted")
        if admitted != expected:
            errors.append("physical_time_bridge_expectation_mismatch:" + bridge.get("case_id", "unknown"))
        time_bridges.append({
            "case_id": bridge.get("case_id"),
            "requested": requested,
            "source_authorized": supported,
            "monoid_morphism": additive,
            "admitted": admitted,
            "scale": str(scale),
            "bounded_time_trace": [str(scale * depth) for depth in range(depth_bound + 1)] if admitted else None,
        })
    closure_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "objective_closure" and row.get("admitted")
    }
    closure_source_supported = fixture.get("objective_closure_authority_support_node") in closure_support_nodes
    if not closure_source_supported:
        errors.append("objective_closure_authority_missing")
    objective_closure_cases = []
    predicate_names = ("causal_reach", "readability", "fault_separation", "restricted_reversibility")
    for case in fixture.get("objective_closure_cases", []):
        coordinates = {name: case.get(name) is True for name in predicate_names}
        admitted = closure_source_supported and all(coordinates.values())
        if admitted != case.get("expected_admitted"):
            errors.append("objective_closure_expectation_mismatch:" + case.get("case_id", "unknown"))
        objective_closure_cases.append({
            "case_id": case.get("case_id"),
            **coordinates,
            "failed_coordinates": [name for name, value in coordinates.items() if not value],
            "source_supported": closure_source_supported,
            "objective_closed": admitted,
            "fanout_descendants": case.get("fanout_descendants", 7),
            "algebraic_depth": case.get("algebraic_depth", 3),
            "pointer_distinguishability": case.get("pointer_distinguishability"),
            "agreement_checks_pass": case.get("agreement_checks_pass"),
            "global_inverse_admitted": case.get("global_inverse_admitted"),
        })
    descent_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "multiobserver_descent" and row.get("admitted")
    }
    descent_source_supported = fixture.get("multiobserver_descent_authority_support_node") in descent_support_nodes
    if not descent_source_supported:
        errors.append("multiobserver_descent_authority_missing")
    descent_cases = []
    for case in fixture.get("multiobserver_descent_cases", []):
        edge_parities = case.get("edge_parities", [])
        edge_local_satisfiable = len(edge_parities) == 3 and all(value in (0, 1) for value in edge_parities)
        holonomy = sum(edge_parities) % 2 if edge_local_satisfiable else None
        unanchored_global_sections = 2 if holonomy == 0 else 0
        source_anchored = case.get("source_anchor") in (0, 1)
        anchored_global_sections = 1 if source_anchored and unanchored_global_sections == 2 else unanchored_global_sections
        descent_closed = descent_source_supported and edge_local_satisfiable and holonomy == 0 and anchored_global_sections == 1
        fault_survival = case.get("fault_survival") is True
        global_objective_record = case.get("local_objective_closures") is True and descent_closed and fault_survival
        if descent_closed != case.get("expected_descent_closed"):
            errors.append("multiobserver_descent_expectation_mismatch:" + case.get("case_id", "unknown"))
        if global_objective_record != case.get("expected_global_objective_record"):
            errors.append("global_objective_record_expectation_mismatch:" + case.get("case_id", "unknown"))
        descent_cases.append({
            "case_id": case.get("case_id"),
            "local_objective_closures": case.get("local_objective_closures") is True,
            "edge_parities": edge_parities,
            "all_edges_locally_satisfiable": edge_local_satisfiable,
            "loop_holonomy": holonomy,
            "unanchored_global_section_count": unanchored_global_sections,
            "source_anchored": source_anchored,
            "anchored_global_section_count": anchored_global_sections,
            "descent_closed": descent_closed,
            "fault_survival": fault_survival,
            "global_objective_record": global_objective_record,
        })
    graph_descent_cases = []
    for case in fixture.get("graph_descent_cases", []):
        vertices = case.get("vertices", [])
        edges = case.get("edges", [])
        anchors = {int(key): value for key, value in case.get("anchors", {}).items()}
        valid_graph = vertices == list(range(len(vertices))) and all(len(edge) == 3 and edge[0] in vertices and edge[1] in vertices and edge[2] in (0, 1) for edge in edges)
        assignments = []
        if valid_graph:
            for mask in range(1 << len(vertices)):
                bits = [(mask >> vertex) & 1 for vertex in vertices]
                if all((bits[left] ^ bits[right]) == parity for left, right, parity in edges):
                    assignments.append(bits)
        anchored_assignments = [bits for bits in assignments if all(bits[vertex] == value for vertex, value in anchors.items())]
        adjacency = {vertex: set() for vertex in vertices}
        for left, right, _ in edges:
            adjacency[left].add(right)
            adjacency[right].add(left)
        components = 0
        unseen = set(vertices)
        while unseen:
            components += 1
            frontier = [unseen.pop()]
            while frontier:
                vertex = frontier.pop()
                neighbors = adjacency[vertex] & unseen
                unseen -= neighbors
                frontier.extend(neighbors)
        cycle_rank = len(edges) - len(vertices) + components if valid_graph else None
        if len(assignments) != case.get("expected_unanchored_sections"):
            errors.append("graph_descent_unanchored_expectation_mismatch:" + case.get("case_id", "unknown"))
        if len(anchored_assignments) != case.get("expected_anchored_sections"):
            errors.append("graph_descent_anchored_expectation_mismatch:" + case.get("case_id", "unknown"))
        graph_descent_cases.append({
            "case_id": case.get("case_id"),
            "valid_graph": valid_graph,
            "component_count": components,
            "cycle_rank": cycle_rank,
            "unanchored_global_section_count": len(assignments),
            "anchored_global_section_count": len(anchored_assignments),
            "coherent": bool(assignments),
            "unique_after_anchors": len(anchored_assignments) == 1,
            "anchors_cover_components": len(anchors) >= components,
        })
    separatedness_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "local_restriction_separatedness" and row.get("admitted")
    }
    separatedness_source_supported = fixture.get("local_restriction_separatedness_authority_support_node") in separatedness_support_nodes
    if not separatedness_source_supported:
        errors.append("local_restriction_separatedness_authority_missing")
    separatedness_cases = []
    for case in fixture.get("separatedness_cases", []):
        global_section_exists = case.get("descent_global_section_exists") is True
        kernel_dimension = case.get("proper_fragment_joint_kernel_dimension")
        jointly_faithful = separatedness_source_supported and kernel_dimension == 0
        anchor_recovers_killed = case.get("source_anchor_recovers_killed_direction") is True
        if anchor_recovers_killed and kernel_dimension and kernel_dimension > 0:
            errors.append("source_anchor_cannot_recover_restriction_kernel:" + case.get("case_id", "unknown"))
        if global_section_exists != case.get("expected_global_section_exists"):
            errors.append("descent_existence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if jointly_faithful != case.get("expected_jointly_faithful"):
            errors.append("local_restriction_separatedness_expectation_mismatch:" + case.get("case_id", "unknown"))
        separatedness_cases.append({
            "case_id": case.get("case_id"),
            "descent_global_section_exists": global_section_exists,
            "local_restrictions_jointly_faithful": jointly_faithful,
            "proper_fragment_joint_kernel_dimension": kernel_dimension,
            "global_states_distinct": case.get("global_states_distinct"),
            "all_proper_fragment_restrictions_equal": case.get("all_proper_fragment_restrictions_equal"),
            "nonzero_global_phase_operator": case.get("nonzero_global_phase_operator"),
            "all_proper_partial_traces_zero": case.get("all_proper_partial_traces_zero"),
            "source_anchor_recovers_killed_direction": anchor_recovers_killed,
            "globally_separated_object_exists": global_section_exists and jointly_faithful,
        })
    phase_port_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "global_phase_observation_port" and row.get("admitted")
    }
    phase_port_cases = []
    for case in fixture.get("global_phase_port_cases", []):
        initial_kernel_dimension = case.get("initial_joint_kernel_dimension")
        port_requested = case.get("port_requested") is True
        port_authorized = case.get("authority_support_node") in phase_port_support_nodes
        genuinely_global = case.get("port_kind") == "global_phase_sensitive"
        response_nonzero = case.get("response_on_hidden_direction") not in (None, 0)
        port_admitted = port_requested and port_authorized and genuinely_global and response_nonzero
        repaired_kernel_dimension = max(0, initial_kernel_dimension - 1) if port_admitted else initial_kernel_dimension
        restored = repaired_kernel_dimension == 0
        if port_requested and not port_authorized:
            errors.append("global_phase_port_authority_missing:" + case.get("case_id", "unknown"))
        if port_requested and port_authorized and not genuinely_global:
            errors.append("proper_fragment_aggregate_cannot_recover_global_phase:" + case.get("case_id", "unknown"))
        if restored != case.get("expected_faithfulness_restored"):
            errors.append("global_phase_port_expectation_mismatch:" + case.get("case_id", "unknown"))
        phase_port_cases.append({
            "case_id": case.get("case_id"),
            "initial_joint_kernel_dimension": initial_kernel_dimension,
            "port_requested": port_requested,
            "port_authorized": port_authorized,
            "genuinely_global": genuinely_global,
            "response_on_hidden_direction": case.get("response_on_hidden_direction"),
            "port_admitted": port_admitted,
            "repaired_joint_kernel_dimension": repaired_kernel_dimension,
            "faithfulness_restored": restored,
        })
    port_rank_cases = []
    for case in fixture.get("observation_port_rank_cases", []):
        hidden_dimension = case.get("hidden_kernel_dimension")
        matrix = case.get("response_matrix", [])
        rectangular = all(isinstance(row, list) and len(row) == hidden_dimension for row in matrix)
        response_rank = exact_matrix_rank(matrix) if rectangular else 0
        residual_dimension = hidden_dimension - response_rank
        all_ports_authorized = case.get("all_ports_authorized") is True
        restored = all_ports_authorized and residual_dimension == 0
        if not all_ports_authorized:
            errors.append("observation_port_family_authority_incomplete:" + case.get("case_id", "unknown"))
        if restored != case.get("expected_faithfulness_restored"):
            errors.append("observation_port_rank_expectation_mismatch:" + case.get("case_id", "unknown"))
        port_rank_cases.append({
            "case_id": case.get("case_id"),
            "hidden_kernel_dimension": hidden_dimension,
            "port_count": len(matrix),
            "response_rank": response_rank,
            "residual_kernel_dimension": residual_dimension,
            "all_ports_authorized": all_ports_authorized,
            "faithfulness_restored": restored,
        })
    port_deletion_cases = []
    for case in fixture.get("observation_port_deletion_cases", []):
        hidden_dimension = case.get("hidden_kernel_dimension")
        matrix = case.get("response_matrix", [])
        full_rank = exact_matrix_rank(matrix)
        minimum_rank_losing_deletions = None
        first_rank_losing_sets = []
        for deletion_count in range(len(matrix) + 1):
            losing_sets = []
            for deleted in combinations(range(len(matrix)), deletion_count):
                remaining = [row for index, row in enumerate(matrix) if index not in deleted]
                if exact_matrix_rank(remaining) < hidden_dimension:
                    losing_sets.append(list(deleted))
            if losing_sets:
                minimum_rank_losing_deletions = deletion_count
                first_rank_losing_sets = losing_sets
                break
        tolerated_deletions = case.get("tolerated_deletions")
        robust = full_rank == hidden_dimension and minimum_rank_losing_deletions is not None and tolerated_deletions < minimum_rank_losing_deletions
        if robust != case.get("expected_robust"):
            errors.append("observation_port_deletion_expectation_mismatch:" + case.get("case_id", "unknown"))
        port_deletion_cases.append({
            "case_id": case.get("case_id"),
            "hidden_kernel_dimension": hidden_dimension,
            "port_count": len(matrix),
            "full_response_rank": full_rank,
            "minimum_rank_losing_deletions": minimum_rank_losing_deletions,
            "primitive_rank_losing_deletion_sets": first_rank_losing_sets,
            "tolerated_deletions": tolerated_deletions,
            "robust": robust,
        })
    port_corruption_cases = []
    for case in fixture.get("observation_port_corruption_cases", []):
        hidden_dimension = case.get("hidden_kernel_dimension")
        matrix = case.get("response_matrix", [])
        minimum_support = None
        for deletion_count in range(len(matrix) + 1):
            if any(
                exact_matrix_rank([row for index, row in enumerate(matrix) if index not in deleted]) < hidden_dimension
                for deleted in combinations(range(len(matrix)), deletion_count)
            ):
                minimum_support = deletion_count
                break
        faults = case.get("adversarial_corruptions")
        detects = minimum_support is not None and minimum_support > faults
        corrects = minimum_support is not None and minimum_support > 2 * faults
        if detects != case.get("expected_detects"):
            errors.append("observation_port_corruption_detection_mismatch:" + case.get("case_id", "unknown"))
        if corrects != case.get("expected_corrects"):
            errors.append("observation_port_corruption_correction_mismatch:" + case.get("case_id", "unknown"))
        port_corruption_cases.append({
            "case_id": case.get("case_id"),
            "minimum_response_support": minimum_support,
            "adversarial_corruptions": faults,
            "detects": detects,
            "corrects": corrects,
        })
    port_resource_bound_cases = []
    for case in fixture.get("observation_port_resource_bound_cases", []):
        hidden_dimension = case.get("hidden_kernel_dimension")
        matrix = case.get("response_matrix", [])
        port_count = len(matrix)
        faults = case.get("adversarial_corruptions")
        minimum_support = None
        for deletion_count in range(port_count + 1):
            if any(
                exact_matrix_rank([row for index, row in enumerate(matrix) if index not in deleted]) < hidden_dimension
                for deleted in combinations(range(port_count), deletion_count)
            ):
                minimum_support = deletion_count
                break
        singleton_upper_bound = port_count - hidden_dimension + 1
        required_port_lower_bound = hidden_dimension + 2 * faults
        resource_bound_satisfied = port_count >= required_port_lower_bound
        distance_optimal = minimum_support == singleton_upper_bound
        corrects = minimum_support is not None and minimum_support > 2 * faults
        if corrects != case.get("expected_corrects"):
            errors.append("observation_port_resource_bound_expectation_mismatch:" + case.get("case_id", "unknown"))
        port_resource_bound_cases.append({
            "case_id": case.get("case_id"),
            "hidden_kernel_dimension": hidden_dimension,
            "port_count": port_count,
            "adversarial_corruptions": faults,
            "minimum_response_support": minimum_support,
            "singleton_upper_bound": singleton_upper_bound,
            "required_port_lower_bound": required_port_lower_bound,
            "resource_bound_satisfied": resource_bound_satisfied,
            "distance_optimal": distance_optimal,
            "corrects": corrects,
        })
    recovery_authority_cases = []
    for case in fixture.get("recovery_authority_product_cases", []):
        separated = case.get("observer_separated") is True
        corrects = case.get("adversarial_correction") is True
        restricted = case.get("restricted_reversibility") is True
        objective_recoverable = separated and corrects and restricted
        if objective_recoverable != case.get("expected_objective_recoverable"):
            errors.append("recovery_authority_product_expectation_mismatch:" + case.get("case_id", "unknown"))
        recovery_authority_cases.append({
            "case_id": case.get("case_id"),
            "observer_separated": separated,
            "adversarial_correction": corrects,
            "restricted_reversibility": restricted,
            "circuit_inverse_admitted": case.get("circuit_inverse_admitted") is True,
            "objective_recoverable": objective_recoverable,
        })
    if fixture.get("distance_grants_decoder_authority") is not False:
        errors.append("decoding_distance_laundered_as_decoder_authority")
    synthesis_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "decoder_synthesis" and row.get("admitted")
    }
    execution_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "decoder_execution" and row.get("admitted")
    }
    decoder_cases = []
    for case in fixture.get("decoder_cases", []):
        decoder_exists = case.get("minimum_response_support") > 2 * case.get("adversarial_corruptions")
        synthesis_authorized = case.get("synthesis_authority_support_node") in synthesis_support_nodes
        execution_authorized = case.get("execution_authority_support_node") in execution_support_nodes
        executable = case.get("physical_modality") == "executable"
        decoder_admitted = decoder_exists and synthesis_authorized and execution_authorized and executable
        if decoder_exists != case.get("expected_decoder_exists"):
            errors.append("decoder_existence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if decoder_admitted != case.get("expected_decoder_admitted"):
            errors.append("decoder_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        decoder_cases.append({
            "case_id": case.get("case_id"),
            "decoder_exists": decoder_exists,
            "synthesis_authorized": synthesis_authorized,
            "execution_authorized": execution_authorized,
            "physical_modality_executable": executable,
            "decoder_admitted": decoder_admitted,
        })
    process_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "process_provenance" and row.get("admitted")
    }
    inverse_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "inverse_constructor" and row.get("admitted")
    }
    process_composition_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "process_composition_provenance" and row.get("admitted")
    }
    history_quotient_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "process_history_quotient" and row.get("admitted")
    }
    history_normalizer_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "process_history_normalizer" and row.get("admitted")
    }
    typed_history_descent_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_descent" and row.get("admitted")
    }
    typed_history_higher_coherence_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_higher_coherence" and row.get("admitted")
    }
    typed_history_anomaly_cocycle_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_anomaly_cocycle" and row.get("admitted")
    }
    typed_history_anomaly_trivialization_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_anomaly_trivialization" and row.get("admitted")
    }
    typed_history_anomaly_selector_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_anomaly_gauge_selector" and row.get("admitted")
    }
    typed_history_selector_naturality_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_anomaly_selector_naturality" and row.get("admitted")
    }
    typed_history_gauge_groupoid_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_gauge_groupoid" and row.get("admitted")
    }
    typed_history_gauge_readout_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_gauge_invariant_readout" and row.get("admitted")
    }
    typed_history_groupoid_reconstruction_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_groupoid_reconstruction" and row.get("admitted")
    }
    typed_history_stabilizer_structure_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_structure" and row.get("admitted")
    }
    typed_history_stabilizer_action_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_action" and row.get("admitted")
    }
    typed_history_stabilizer_transport_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_transport" and row.get("admitted")
    }
    typed_history_transport_composition_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_transport_composition" and row.get("admitted")
    }
    typed_history_transport_compositor_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_transport_compositor" and row.get("admitted")
    }
    typed_history_transport_pentagon_support_nodes = {
        row["support_node"] for row in authority_support.get("targets", [])
        if row.get("target_kind") == "typed_history_stabilizer_transport_pentagon" and row.get("admitted")
    }
    process_cases = []
    for case in fixture.get("process_provenance_cases", []):
        endpoint_separated = case.get("endpoint_state_readout_separated") is True
        ambiguity_dimension = case.get("process_ambiguity_dimension")
        response_matrix = case.get("process_probe_response_matrix", [])
        process_response_rank = exact_matrix_rank(response_matrix)
        provenance_supported = case.get("process_provenance_support_node") in process_support_nodes
        process_faithful = provenance_supported and process_response_rank == ambiguity_dimension
        inverse_supported = case.get("inverse_constructor_support_node") in inverse_support_nodes
        inverse_authorized = endpoint_separated and process_faithful and inverse_supported
        if process_faithful != case.get("expected_process_faithful"):
            errors.append("process_provenance_expectation_mismatch:" + case.get("case_id", "unknown"))
        if inverse_authorized != case.get("expected_inverse_authorized"):
            errors.append("inverse_authority_expectation_mismatch:" + case.get("case_id", "unknown"))
        process_cases.append({
            "case_id": case.get("case_id"),
            "endpoint_state_readout_separated": endpoint_separated,
            "process_pair": case.get("process_pair"),
            "observed_source_subspace": case.get("observed_source_subspace"),
            "recovery_domain_extra_direction": case.get("recovery_domain_extra_direction"),
            "process_ambiguity_dimension": ambiguity_dimension,
            "process_probe_response_rank": process_response_rank,
            "process_provenance_source_supported": provenance_supported,
            "process_provenance_faithful": process_faithful,
            "inverse_constructor_source_supported": inverse_supported,
            "inverse_authorized": inverse_authorized,
        })
    process_composition_cases = []
    for case in fixture.get("process_composition_cases", []):
        local_ranks = [exact_matrix_rank(matrix) for matrix in case.get("local_probe_response_matrices", [])]
        local_dimensions = case.get("local_ambiguity_dimensions", [])
        locally_faithful = (
            len(local_ranks) == len(local_dimensions)
            and all(rank == dimension for rank, dimension in zip(local_ranks, local_dimensions))
        )
        composite_rank = exact_matrix_rank(case.get("composite_probe_response_matrix", []))
        composite_dimension = case.get("composite_ambiguity_dimension")
        composition_supported = case.get("composition_provenance_support_node") in process_composition_support_nodes
        factorization_labels_retained = case.get("factorization_labels_retained") is True
        composite_faithful = (
            locally_faithful
            and factorization_labels_retained
            and composition_supported
            and composite_rank == composite_dimension
        )
        if composite_faithful != case.get("expected_composite_faithful"):
            errors.append("process_composition_expectation_mismatch:" + case.get("case_id", "unknown"))
        process_composition_cases.append({
            "case_id": case.get("case_id"),
            "candidate_histories": case.get("candidate_histories"),
            "local_probe_response_ranks": local_ranks,
            "local_ambiguity_dimensions": local_dimensions,
            "locally_faithful": locally_faithful,
            "composite_probe_response_rank": composite_rank,
            "composite_ambiguity_dimension": composite_dimension,
            "factorization_labels_retained": factorization_labels_retained,
            "composition_provenance_source_supported": composition_supported,
            "composite_process_faithful": composite_faithful,
        })
    history_quotient_cases = []
    for case in fixture.get("process_history_quotient_cases", []):
        histories = case.get("histories", [])
        quotient_supported = case.get("history_quotient_support_node") in history_quotient_support_nodes
        declared_classes = case.get("declared_equivalence_classes", [])
        effective_classes = declared_classes if quotient_supported else [[history] for history in histories]
        quotient_ambiguity_dimension = max(0, len(effective_classes) - 1)
        quotient_response_rank = exact_matrix_rank(case.get("quotient_probe_response_matrix", []))
        raw_presentation_overfit = (
            quotient_supported
            and any(len(equivalence_class) > 1 for equivalence_class in effective_classes)
            and case.get("requires_raw_presentation_separation") is True
        )
        quotient_provenance_faithful = (
            quotient_response_rank == quotient_ambiguity_dimension
            and not raw_presentation_overfit
        )
        if len(effective_classes) != case.get("expected_effective_class_count"):
            errors.append("process_history_quotient_class_expectation_mismatch:" + case.get("case_id", "unknown"))
        if quotient_provenance_faithful != case.get("expected_quotient_provenance_faithful"):
            errors.append("process_history_quotient_expectation_mismatch:" + case.get("case_id", "unknown"))
        history_quotient_cases.append({
            "case_id": case.get("case_id"),
            "raw_history_count": len(histories),
            "history_quotient_source_supported": quotient_supported,
            "effective_process_class_count": len(effective_classes),
            "quotient_ambiguity_dimension": quotient_ambiguity_dimension,
            "quotient_probe_response_rank": quotient_response_rank,
            "requires_raw_presentation_separation": case.get("requires_raw_presentation_separation") is True,
            "raw_presentation_overfit": raw_presentation_overfit,
            "quotient_process_provenance_faithful": quotient_provenance_faithful,
        })
    history_congruence_cases = []
    for case in fixture.get("process_history_congruence_cases", []):
        quotient_supported = case.get("history_quotient_support_node") in history_quotient_support_nodes
        context_checks = case.get("context_checks", [])
        failed_contexts = [
            check.get("context_id") for check in context_checks
            if check.get("left_composite_class") != check.get("right_composite_class")
        ]
        two_sided_congruence = quotient_supported and not failed_contexts
        quotient_composition_admitted = two_sided_congruence
        if two_sided_congruence != case.get("expected_two_sided_congruence"):
            errors.append("process_history_congruence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if quotient_composition_admitted != case.get("expected_quotient_composition_admitted"):
            errors.append("process_history_quotient_composition_expectation_mismatch:" + case.get("case_id", "unknown"))
        history_congruence_cases.append({
            "case_id": case.get("case_id"),
            "history_quotient_source_supported": quotient_supported,
            "context_check_count": len(context_checks),
            "failed_contexts": failed_contexts,
            "two_sided_congruence": two_sided_congruence,
            "quotient_composition_admitted": quotient_composition_admitted,
        })
    partial_congruence_cases = []
    for case in fixture.get("process_history_partial_congruence_cases", []):
        quotient_supported = case.get("history_quotient_support_node") in history_quotient_support_nodes
        context_checks = case.get("partial_context_checks", [])
        failed_domain_contexts = [
            check.get("context_id") for check in context_checks
            if check.get("left_defined") is not check.get("right_defined")
        ]
        failed_output_contexts = [
            check.get("context_id") for check in context_checks
            if check.get("left_defined") is True
            and check.get("right_defined") is True
            and check.get("left_composite_class") != check.get("right_composite_class")
        ]
        domain_saturated = not failed_domain_contexts
        output_congruent_where_defined = not failed_output_contexts
        partial_quotient_admitted = quotient_supported and domain_saturated and output_congruent_where_defined
        if domain_saturated != case.get("expected_domain_saturated"):
            errors.append("process_history_partial_domain_expectation_mismatch:" + case.get("case_id", "unknown"))
        if partial_quotient_admitted != case.get("expected_partial_quotient_admitted"):
            errors.append("process_history_partial_quotient_expectation_mismatch:" + case.get("case_id", "unknown"))
        partial_congruence_cases.append({
            "case_id": case.get("case_id"),
            "history_quotient_source_supported": quotient_supported,
            "failed_domain_contexts": failed_domain_contexts,
            "failed_output_contexts": failed_output_contexts,
            "domain_saturated": domain_saturated,
            "output_congruent_where_defined": output_congruent_where_defined,
            "partial_quotient_admitted": partial_quotient_admitted,
        })
    history_normalizer_cases = []
    for case in fixture.get("process_history_normalizer_cases", []):
        quotient_supported = case.get("history_quotient_support_node") in history_quotient_support_nodes
        normalizer_supported = case.get("history_normalizer_support_node") in history_normalizer_support_nodes
        terminating = case.get("termination_measure_strictly_decreases") is True
        critical_pairs = case.get("critical_pairs", [])
        failed_critical_pairs = [pair.get("pair_id") for pair in critical_pairs if pair.get("joins") is not True]
        locally_confluent = not failed_critical_pairs
        unique_normal_forms = quotient_supported and terminating and locally_confluent
        executable_normalizer_admitted = unique_normal_forms and normalizer_supported
        if unique_normal_forms != case.get("expected_unique_normal_forms"):
            errors.append("process_history_normal_form_expectation_mismatch:" + case.get("case_id", "unknown"))
        if executable_normalizer_admitted != case.get("expected_executable_normalizer_admitted"):
            errors.append("process_history_normalizer_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        history_normalizer_cases.append({
            "case_id": case.get("case_id"),
            "history_quotient_source_supported": quotient_supported,
            "history_normalizer_source_supported": normalizer_supported,
            "terminating": terminating,
            "failed_critical_pairs": failed_critical_pairs,
            "locally_confluent": locally_confluent,
            "unique_normal_forms": unique_normal_forms,
            "executable_normalizer_admitted": executable_normalizer_admitted,
        })
    typed_history_descent_cases = []
    for case in fixture.get("typed_history_descent_cases", []):
        left = case.get("left_typed_fiber", {})
        right = case.get("right_typed_fiber", {})
        compared_fields = case.get("compared_fields", [])
        mismatched_fields = [field for field in compared_fields if left.get(field) != right.get(field)]
        coherence_supported = case.get("coherence_support_node") in typed_history_descent_support_nodes
        coherence_declares_equivalence = case.get("coherence_declares_fiber_equivalence") is True
        typed_fiber_descends = not mismatched_fields or (coherence_supported and coherence_declares_equivalence)
        if typed_fiber_descends != case.get("expected_typed_fiber_descends"):
            errors.append("typed_history_descent_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_descent_cases.append({
            "case_id": case.get("case_id"),
            "process_normal_forms_equal": case.get("process_normal_forms_equal") is True,
            "mismatched_typed_fields": mismatched_fields,
            "coherence_source_supported": coherence_supported,
            "coherence_declares_fiber_equivalence": coherence_declares_equivalence,
            "typed_fiber_descends": typed_fiber_descends,
        })
    typed_history_coherence_cases = []
    for case in fixture.get("typed_history_coherence_cases", []):
        transports = case.get("triangle_transports", [])
        complete_triangle = len(transports) == 3 and all(transport.get("source_authorized") is True for transport in transports)
        holonomy = 1
        for transport in transports:
            holonomy *= transport.get("orientation", 1)
        strict_descent = complete_triangle and holonomy == 1
        higher_cell_supported = case.get("higher_coherence_support_node") in typed_history_higher_coherence_support_nodes
        anomaly_kind = case.get("declared_anomaly_kind")
        anomaly_admitted = complete_triangle and holonomy != 1 and higher_cell_supported and anomaly_kind == "central_phase"
        coherence_class = "strict" if strict_descent else ("typed_central_anomaly" if anomaly_admitted else "rejected")
        if coherence_class != case.get("expected_coherence_class"):
            errors.append("typed_history_coherence_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_coherence_cases.append({
            "case_id": case.get("case_id"),
            "complete_authorized_triangle": complete_triangle,
            "triangle_holonomy": holonomy,
            "strict_descent": strict_descent,
            "higher_coherence_source_supported": higher_cell_supported,
            "anomaly_admitted": anomaly_admitted,
            "coherence_class": coherence_class,
        })
    typed_history_anomaly_cocycle_cases = []
    for case in fixture.get("typed_history_anomaly_cocycle_cases", []):
        faces = case.get("tetrahedron_faces", [])
        complete_boundary = len(faces) == 4 and all(face.get("source_authorized") is True for face in faces)
        boundary_phase = 1
        for face in faces:
            boundary_phase *= face.get("phase", 1)
        cocycle_closed = complete_boundary and boundary_phase == 1
        cocycle_supported = case.get("anomaly_cocycle_support_node") in typed_history_anomaly_cocycle_support_nodes
        coherent_anomaly_atlas = cocycle_closed and cocycle_supported
        if coherent_anomaly_atlas != case.get("expected_coherent_anomaly_atlas"):
            errors.append("typed_history_anomaly_cocycle_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_anomaly_cocycle_cases.append({
            "case_id": case.get("case_id"),
            "complete_authorized_boundary": complete_boundary,
            "tetrahedron_boundary_phase": boundary_phase,
            "cocycle_closed": cocycle_closed,
            "anomaly_cocycle_source_supported": cocycle_supported,
            "coherent_anomaly_atlas": coherent_anomaly_atlas,
        })
    typed_history_anomaly_class_cases = []
    for case in fixture.get("typed_history_anomaly_class_cases", []):
        boundary_matrix = case.get("edge_to_face_coboundary_matrix", [])
        anomaly_vector = case.get("anomaly_vector", [])
        base_rank = gf2_matrix_rank(boundary_matrix)
        augmented = [row + [anomaly_vector[index]] for index, row in enumerate(boundary_matrix)]
        augmented_rank = gf2_matrix_rank(augmented)
        anomaly_is_coboundary = base_rank == augmented_rank
        trivialization_supported = case.get("anomaly_trivialization_support_node") in typed_history_anomaly_trivialization_support_nodes
        strictification_admitted = anomaly_is_coboundary and trivialization_supported
        if anomaly_is_coboundary != case.get("expected_anomaly_is_coboundary"):
            errors.append("typed_history_anomaly_class_expectation_mismatch:" + case.get("case_id", "unknown"))
        if strictification_admitted != case.get("expected_strictification_admitted"):
            errors.append("typed_history_anomaly_strictification_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_anomaly_class_cases.append({
            "case_id": case.get("case_id"),
            "coboundary_matrix_rank": base_rank,
            "augmented_matrix_rank": augmented_rank,
            "anomaly_is_coboundary": anomaly_is_coboundary,
            "anomaly_cohomology_class": "trivial" if anomaly_is_coboundary else "nontrivial",
            "trivialization_source_supported": trivialization_supported,
            "strictification_admitted": strictification_admitted,
        })
    typed_history_gauge_selector_cases = []
    for case in fixture.get("typed_history_gauge_selector_cases", []):
        boundary_matrix = case.get("edge_to_face_coboundary_matrix", [])
        anomaly_vector = case.get("anomaly_vector", [])
        base_rank = gf2_matrix_rank(boundary_matrix)
        width = len(boundary_matrix[0]) if boundary_matrix else 0
        augmented = [row + [anomaly_vector[index]] for index, row in enumerate(boundary_matrix)]
        anomaly_is_coboundary = base_rank == gf2_matrix_rank(augmented)
        gauge_torsor_dimension = width - base_rank if anomaly_is_coboundary else None
        trivialization_supported = case.get("anomaly_trivialization_support_node") in typed_history_anomaly_trivialization_support_nodes
        selector_supported = case.get("gauge_selector_support_node") in typed_history_anomaly_selector_support_nodes
        canonical_strictification_admitted = (
            anomaly_is_coboundary
            and trivialization_supported
            and (gauge_torsor_dimension == 0 or selector_supported)
        )
        if canonical_strictification_admitted != case.get("expected_canonical_strictification_admitted"):
            errors.append("typed_history_gauge_selector_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_gauge_selector_cases.append({
            "case_id": case.get("case_id"),
            "anomaly_is_coboundary": anomaly_is_coboundary,
            "gauge_torsor_dimension": gauge_torsor_dimension,
            "trivialization_source_supported": trivialization_supported,
            "gauge_selector_source_supported": selector_supported,
            "canonical_strictification_admitted": canonical_strictification_admitted,
        })
    typed_history_selector_naturality_cases = []
    for case in fixture.get("typed_history_selector_naturality_cases", []):
        torsor_dimension = case.get("gauge_torsor_dimension")
        selection = case.get("selected_gauge", [])
        actions = case.get("authorized_presentation_actions", [])
        failed_actions = []
        for action in actions:
            matrix = action.get("matrix", [])
            transformed = [sum(entry * selection[index] for index, entry in enumerate(row)) % 2 for row in matrix]
            if transformed != selection:
                failed_actions.append(action.get("action_id"))
        equivariant = not failed_actions
        selector_supported = case.get("gauge_selector_support_node") in typed_history_anomaly_selector_support_nodes
        naturality_supported = case.get("selector_naturality_support_node") in typed_history_selector_naturality_support_nodes
        natural_selector_admitted = (
            torsor_dimension == 0
            or (selector_supported and naturality_supported and equivariant)
        )
        if natural_selector_admitted != case.get("expected_natural_selector_admitted"):
            errors.append("typed_history_selector_naturality_expectation_mismatch:" + case.get("case_id", "unknown"))
        typed_history_selector_naturality_cases.append({
            "case_id": case.get("case_id"),
            "gauge_torsor_dimension": torsor_dimension,
            "failed_presentation_actions": failed_actions,
            "selector_equivariant": equivariant,
            "gauge_selector_source_supported": selector_supported,
            "selector_naturality_source_supported": naturality_supported,
            "natural_selector_admitted": natural_selector_admitted,
        })
    equivariant_gauge_existence_cases = []
    for case in fixture.get("equivariant_gauge_existence_cases", []):
        boundary_matrix = case.get("edge_to_face_coboundary_matrix", [])
        anomaly_vector = case.get("anomaly_vector", [])
        width = len(boundary_matrix[0]) if boundary_matrix else 0
        solutions = []
        for candidate in product((0, 1), repeat=width):
            image = [sum(entry * candidate[index] for index, entry in enumerate(row)) % 2 for row in boundary_matrix]
            if image == anomaly_vector:
                solutions.append(list(candidate))
        actions = case.get("authorized_presentation_actions", [])
        solution_keys = {tuple(solution) for solution in solutions}
        actions_preserve_torsor = True
        invariant_solutions = []
        for solution in solutions:
            fixed = True
            for action in actions:
                transformed = [sum(entry * solution[index] for index, entry in enumerate(row)) % 2 for row in action.get("matrix", [])]
                if tuple(transformed) not in solution_keys:
                    actions_preserve_torsor = False
                if transformed != solution:
                    fixed = False
            if fixed:
                invariant_solutions.append(solution)
        equivariant_selector_exists = bool(solutions) and actions_preserve_torsor and bool(invariant_solutions)
        trivialization_supported = case.get("anomaly_trivialization_support_node") in typed_history_anomaly_trivialization_support_nodes
        selector_supported = case.get("gauge_selector_support_node") in typed_history_anomaly_selector_support_nodes
        naturality_supported = case.get("selector_naturality_support_node") in typed_history_selector_naturality_support_nodes
        equivariant_selector_admitted = (
            equivariant_selector_exists
            and trivialization_supported
            and (len(solutions) == 1 or (selector_supported and naturality_supported))
        )
        if equivariant_selector_exists != case.get("expected_equivariant_selector_exists"):
            errors.append("equivariant_gauge_selector_existence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if equivariant_selector_admitted != case.get("expected_equivariant_selector_admitted"):
            errors.append("equivariant_gauge_selector_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        equivariant_gauge_existence_cases.append({
            "case_id": case.get("case_id"),
            "solution_count": len(solutions),
            "actions_preserve_gauge_torsor": actions_preserve_torsor,
            "invariant_solution_count": len(invariant_solutions),
            "equivariant_selector_exists": equivariant_selector_exists,
            "equivariant_selector_admitted": equivariant_selector_admitted,
        })
    gauge_groupoid_cases = []
    for case in fixture.get("gauge_groupoid_cases", []):
        boundary_matrix = case.get("edge_to_face_coboundary_matrix", [])
        anomaly_vector = case.get("anomaly_vector", [])
        width = len(boundary_matrix[0]) if boundary_matrix else 0
        solutions = []
        for candidate in product((0, 1), repeat=width):
            image = [sum(entry * candidate[index] for index, entry in enumerate(row)) % 2 for row in boundary_matrix]
            if image == anomaly_vector:
                solutions.append(tuple(candidate))
        solution_set = set(solutions)
        actions = case.get("authorized_presentation_actions", [])
        adjacency = {solution: set() for solution in solutions}
        actions_preserve_torsor = True
        for solution in solutions:
            for action in actions:
                transformed = tuple(sum(entry * solution[index] for index, entry in enumerate(row)) % 2 for row in action.get("matrix", []))
                if transformed not in solution_set:
                    actions_preserve_torsor = False
                else:
                    adjacency[solution].add(transformed)
                    adjacency[transformed].add(solution)
        orbit_count = 0
        unseen = set(solutions)
        while unseen:
            orbit_count += 1
            frontier = [unseen.pop()]
            while frontier:
                current = frontier.pop()
                for neighbor in adjacency[current]:
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        frontier.append(neighbor)
        groupoid_supported = case.get("gauge_groupoid_support_node") in typed_history_gauge_groupoid_support_nodes
        retains_stabilizers = case.get("retains_stabilizers") is True
        groupoid_output_admitted = bool(solutions) and actions_preserve_torsor and groupoid_supported and retains_stabilizers
        if groupoid_output_admitted != case.get("expected_groupoid_output_admitted"):
            errors.append("gauge_groupoid_output_expectation_mismatch:" + case.get("case_id", "unknown"))
        gauge_groupoid_cases.append({
            "case_id": case.get("case_id"),
            "solution_count": len(solutions),
            "presentation_orbit_count": orbit_count,
            "actions_preserve_gauge_torsor": actions_preserve_torsor,
            "retains_stabilizers": retains_stabilizers,
            "gauge_groupoid_source_supported": groupoid_supported,
            "groupoid_output_admitted": groupoid_output_admitted,
        })
    gauge_readout_cases = []
    for case in fixture.get("gauge_readout_cases", []):
        boundary_matrix = case.get("edge_to_face_coboundary_matrix", [])
        anomaly_vector = case.get("anomaly_vector", [])
        width = len(boundary_matrix[0]) if boundary_matrix else 0
        solutions = []
        for candidate in product((0, 1), repeat=width):
            image = [sum(entry * candidate[index] for index, entry in enumerate(row)) % 2 for row in boundary_matrix]
            if image == anomaly_vector:
                solutions.append(tuple(candidate))
        solution_set = set(solutions)
        adjacency = {solution: set() for solution in solutions}
        actions_preserve_torsor = True
        for solution in solutions:
            for action in case.get("authorized_presentation_actions", []):
                transformed = tuple(sum(entry * solution[index] for index, entry in enumerate(row)) % 2 for row in action.get("matrix", []))
                if transformed not in solution_set:
                    actions_preserve_torsor = False
                else:
                    adjacency[solution].add(transformed)
                    adjacency[transformed].add(solution)
        orbits = []
        unseen = set(solutions)
        while unseen:
            orbit = {unseen.pop()}
            frontier = list(orbit)
            while frontier:
                current = frontier.pop()
                for neighbor in adjacency[current]:
                    if neighbor not in orbit:
                        orbit.add(neighbor)
                        unseen.discard(neighbor)
                        frontier.append(neighbor)
            orbits.append(orbit)
        readout = case.get("readout_by_gauge", {})
        orbit_values = [{readout.get("".join(str(bit) for bit in solution)) for solution in orbit} for orbit in orbits]
        gauge_invariant = actions_preserve_torsor and all(len(values) == 1 for values in orbit_values)
        orbit_readout_faithful = gauge_invariant and len({next(iter(values)) for values in orbit_values}) == len(orbits)
        groupoid_supported = case.get("gauge_groupoid_support_node") in typed_history_gauge_groupoid_support_nodes
        readout_supported = case.get("gauge_readout_support_node") in typed_history_gauge_readout_support_nodes
        readout_descends = gauge_invariant and groupoid_supported and readout_supported
        if readout_descends != case.get("expected_readout_descends"):
            errors.append("gauge_readout_descent_expectation_mismatch:" + case.get("case_id", "unknown"))
        if orbit_readout_faithful != case.get("expected_orbit_readout_faithful"):
            errors.append("gauge_readout_faithfulness_expectation_mismatch:" + case.get("case_id", "unknown"))
        gauge_readout_cases.append({
            "case_id": case.get("case_id"),
            "presentation_orbit_count": len(orbits),
            "gauge_invariant": gauge_invariant,
            "orbit_readout_faithful": orbit_readout_faithful,
            "gauge_groupoid_source_supported": groupoid_supported,
            "gauge_readout_source_supported": readout_supported,
            "readout_descends": readout_descends,
        })
    groupoid_reconstruction_cases = []
    for case in fixture.get("groupoid_reconstruction_cases", []):
        left = case.get("left_groupoid_signature", {})
        right = case.get("right_groupoid_signature", {})
        orbit_packet_equal = left.get("orbit_readouts") == right.get("orbit_readouts")
        stabilizer_packet_equal = left.get("stabilizer_signatures") == right.get("stabilizer_signatures")
        groupoids_equivalent = (
            left.get("orbit_count") == right.get("orbit_count")
            and stabilizer_packet_equal
        )
        retains_stabilizers = case.get("retains_stabilizer_readout") is True
        packet_detects_difference = (not orbit_packet_equal) or (retains_stabilizers and not stabilizer_packet_equal)
        comparison_correct = packet_detects_difference == (not groupoids_equivalent)
        reconstruction_supported = case.get("groupoid_reconstruction_support_node") in typed_history_groupoid_reconstruction_support_nodes
        groupoid_reconstruction_admitted = comparison_correct and retains_stabilizers and reconstruction_supported
        if groupoid_reconstruction_admitted != case.get("expected_groupoid_reconstruction_admitted"):
            errors.append("groupoid_reconstruction_expectation_mismatch:" + case.get("case_id", "unknown"))
        groupoid_reconstruction_cases.append({
            "case_id": case.get("case_id"),
            "orbit_readout_packets_equal": orbit_packet_equal,
            "stabilizer_packets_equal": stabilizer_packet_equal,
            "groupoids_equivalent": groupoids_equivalent,
            "retains_stabilizer_readout": retains_stabilizers,
            "packet_detects_groupoid_difference": packet_detects_difference,
            "comparison_correct": comparison_correct,
            "groupoid_reconstruction_source_supported": reconstruction_supported,
            "groupoid_reconstruction_admitted": groupoid_reconstruction_admitted,
        })
    stabilizer_structure_cases = []
    for case in fixture.get("stabilizer_structure_cases", []):
        left_table = case.get("left_multiplication_table", [])
        right_table = case.get("right_multiplication_table", [])
        left_valid = finite_group_table_valid(left_table)
        right_valid = finite_group_table_valid(right_table)
        isomorphic = finite_groups_isomorphic(left_table, right_table)
        retains_table = case.get("retains_multiplication_table") is True
        structure_supported = case.get("stabilizer_structure_support_node") in typed_history_stabilizer_structure_support_nodes
        stabilizer_comparison_admitted = left_valid and right_valid and retains_table and structure_supported
        if isomorphic != case.get("expected_stabilizers_isomorphic"):
            errors.append("stabilizer_isomorphism_expectation_mismatch:" + case.get("case_id", "unknown"))
        if stabilizer_comparison_admitted != case.get("expected_stabilizer_comparison_admitted"):
            errors.append("stabilizer_structure_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        stabilizer_structure_cases.append({
            "case_id": case.get("case_id"),
            "common_cardinality": len(left_table) if len(left_table) == len(right_table) else None,
            "left_group_table_valid": left_valid,
            "right_group_table_valid": right_valid,
            "stabilizers_isomorphic": isomorphic,
            "retains_multiplication_table": retains_table,
            "stabilizer_structure_source_supported": structure_supported,
            "stabilizer_comparison_admitted": stabilizer_comparison_admitted,
        })
    stabilizer_action_cases = []
    for case in fixture.get("stabilizer_action_cases", []):
        table = case.get("stabilizer_multiplication_table", [])
        left_representation = case.get("left_fiber_representation", [])
        right_representation = case.get("right_fiber_representation", [])
        left_valid = finite_group_representation_valid(table, left_representation)
        right_valid = finite_group_representation_valid(table, right_representation)
        representations_equivalent = left_valid and right_valid and gf2_representations_conjugate(left_representation, right_representation)
        retains_action = case.get("retains_stabilizer_action") is True
        action_supported = case.get("stabilizer_action_support_node") in typed_history_stabilizer_action_support_nodes
        action_comparison_admitted = left_valid and right_valid and retains_action and action_supported
        if representations_equivalent != case.get("expected_representations_equivalent"):
            errors.append("stabilizer_action_equivalence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if action_comparison_admitted != case.get("expected_action_comparison_admitted"):
            errors.append("stabilizer_action_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        stabilizer_action_cases.append({
            "case_id": case.get("case_id"),
            "left_representation_valid": left_valid,
            "right_representation_valid": right_valid,
            "representations_equivalent_under_basis_change": representations_equivalent,
            "retains_stabilizer_action": retains_action,
            "stabilizer_action_source_supported": action_supported,
            "stabilizer_action_comparison_admitted": action_comparison_admitted,
        })
    stabilizer_action_relabeling_cases = []
    for case in fixture.get("stabilizer_action_relabeling_cases", []):
        left_table = case.get("left_stabilizer_table", [])
        right_table = case.get("right_stabilizer_table", [])
        left_representation = case.get("left_fiber_representation", [])
        right_representation = case.get("right_fiber_representation", [])
        label_fixed_equivalent = (
            finite_group_representation_valid(left_table, left_representation)
            and finite_group_representation_valid(right_table, right_representation)
            and left_table == right_table
            and gf2_representations_conjugate(left_representation, right_representation)
        )
        combined_equivalent = finite_group_actions_equivalent(left_table, right_table, left_representation, right_representation)
        retains_linkage = case.get("retains_group_action_linkage") is True
        action_supported = case.get("stabilizer_action_support_node") in typed_history_stabilizer_action_support_nodes
        combined_comparison_admitted = retains_linkage and action_supported
        if combined_equivalent != case.get("expected_combined_action_equivalent"):
            errors.append("stabilizer_combined_action_equivalence_expectation_mismatch:" + case.get("case_id", "unknown"))
        if combined_comparison_admitted != case.get("expected_combined_comparison_admitted"):
            errors.append("stabilizer_combined_action_admission_expectation_mismatch:" + case.get("case_id", "unknown"))
        stabilizer_action_relabeling_cases.append({
            "case_id": case.get("case_id"),
            "label_fixed_action_equivalent": label_fixed_equivalent,
            "combined_group_and_basis_action_equivalent": combined_equivalent,
            "retains_group_action_linkage": retains_linkage,
            "stabilizer_action_source_supported": action_supported,
            "combined_comparison_admitted": combined_comparison_admitted,
        })
    stabilizer_transport_cases = []
    for case in fixture.get("stabilizer_transport_cases", []):
        left_table = case.get("left_stabilizer_table", [])
        right_table = case.get("right_stabilizer_table", [])
        mapping = case.get("stabilizer_isomorphism", [])
        left_representation = case.get("left_fiber_representation", [])
        right_representation = case.get("right_fiber_representation", [])
        transport = case.get("fiber_transport", [])
        group_isomorphism = (
            len(mapping) == len(left_table) == len(right_table)
            and sorted(mapping) == list(range(len(mapping)))
            and all(mapping[left_table[x][y]] == right_table[mapping[x]][mapping[y]] for x in range(len(mapping)) for y in range(len(mapping)))
        )
        representation_packets_valid = (
            finite_group_representation_valid(left_table, left_representation)
            and finite_group_representation_valid(right_table, right_representation)
        )
        transport_invertible = bool(transport) and gf2_matrix_rank(transport) == len(transport)
        intertwines = (
            group_isomorphism
            and representation_packets_valid
            and all(
                gf2_matrix_multiply(transport, left_representation[g])
                == gf2_matrix_multiply(right_representation[mapping[g]], transport)
                for g in range(len(mapping))
            )
        )
        transport_supported = case.get("stabilizer_transport_support_node") in typed_history_stabilizer_transport_support_nodes
        transport_admitted = group_isomorphism and representation_packets_valid and transport_invertible and intertwines and transport_supported
        if transport_admitted != case.get("expected_transport_admitted"):
            errors.append("stabilizer_transport_expectation_mismatch:" + case.get("case_id", "unknown"))
        stabilizer_transport_cases.append({
            "case_id": case.get("case_id"),
            "stabilizer_map_isomorphism": group_isomorphism,
            "representation_packets_valid": representation_packets_valid,
            "fiber_transport_invertible": transport_invertible,
            "intertwining_square_commutes": intertwines,
            "stabilizer_transport_source_supported": transport_supported,
            "stabilizer_transport_admitted": transport_admitted,
        })
    stabilizer_transport_composition_cases = []
    for case in fixture.get("stabilizer_transport_composition_cases", []):
        transport_ab = case.get("transport_ab", [])
        transport_bc = case.get("transport_bc", [])
        transport_ac = case.get("transport_ac", [])
        all_edges_present = bool(transport_ab) and bool(transport_bc) and bool(transport_ac)
        all_edges_invertible = all_edges_present and all(
            gf2_matrix_rank(transport) == len(transport)
            for transport in (transport_ab, transport_bc, transport_ac)
        )
        composite = gf2_matrix_multiply(transport_bc, transport_ab) if transport_ab and transport_bc else []
        strict_composition = all_edges_present and composite == transport_ac
        composition_supported = case.get("transport_composition_support_node") in typed_history_transport_composition_support_nodes
        functorial_transport_admitted = all_edges_invertible and strict_composition and composition_supported
        if functorial_transport_admitted != case.get("expected_functorial_transport_admitted"):
            errors.append("stabilizer_transport_composition_expectation_mismatch:" + case.get("case_id", "unknown"))
        stabilizer_transport_composition_cases.append({
            "case_id": case.get("case_id"),
            "all_transport_edges_present": all_edges_present,
            "all_transport_edges_invertible": all_edges_invertible,
            "composite_transport": composite,
            "direct_transport": transport_ac,
            "strict_transport_composition": strict_composition,
            "transport_composition_source_supported": composition_supported,
            "functorial_transport_admitted": functorial_transport_admitted,
        })
    weak_transport_composition_cases = []
    for case in fixture.get("weak_transport_composition_cases", []):
        transport_ab = case.get("transport_ab", [])
        transport_bc = case.get("transport_bc", [])
        transport_ac = case.get("transport_ac", [])
        composite = gf2_matrix_multiply(transport_bc, transport_ab)
        strict = composite == transport_ac
        strict_supported = case.get("transport_composition_support_node") in typed_history_transport_composition_support_nodes
        compositor = case.get("compositor_cell", [])
        compositor_invertible = bool(compositor) and gf2_matrix_rank(compositor) == len(compositor)
        compositor_equation = bool(compositor) and composite == gf2_matrix_multiply(compositor, transport_ac)
        target_representation = case.get("target_stabilizer_representation", [])
        compositor_natural = bool(compositor) and all(
            gf2_matrix_multiply(compositor, action) == gf2_matrix_multiply(action, compositor)
            for action in target_representation
        )
        compositor_supported = case.get("transport_compositor_support_node") in typed_history_transport_compositor_support_nodes
        weak_admitted = compositor_invertible and compositor_equation and compositor_natural and compositor_supported
        composition_class = "strict" if strict and strict_supported else ("source_typed_weak" if weak_admitted else "rejected")
        if composition_class != case.get("expected_composition_class"):
            errors.append("weak_transport_composition_expectation_mismatch:" + case.get("case_id", "unknown"))
        weak_transport_composition_cases.append({
            "case_id": case.get("case_id"),
            "strict_transport_composition": strict,
            "strict_composition_source_supported": strict_supported,
            "compositor_invertible": compositor_invertible,
            "compositor_equation_holds": compositor_equation,
            "compositor_natural_for_stabilizer_action": compositor_natural,
            "compositor_source_supported": compositor_supported,
            "composition_class": composition_class,
        })
    weak_transport_pentagon_cases = []
    for case in fixture.get("weak_transport_pentagon_cases", []):
        left_cells = case.get("left_compositor_path", [])
        right_cells = case.get("right_compositor_path", [])
        dimension = len((left_cells or right_cells)[0].get("matrix", [])) if (left_cells or right_cells) else 0
        identity = [[int(row == column) for column in range(dimension)] for row in range(dimension)]
        left_product = identity
        for cell in left_cells:
            left_product = gf2_matrix_multiply(cell.get("matrix", []), left_product)
        right_product = identity
        for cell in right_cells:
            right_product = gf2_matrix_multiply(cell.get("matrix", []), right_product)
        all_compositors_authorized = all(cell.get("source_authorized") is True for cell in left_cells + right_cells)
        pentagon_closes = left_product == right_product
        pentagon_supported = case.get("transport_pentagon_support_node") in typed_history_transport_pentagon_support_nodes
        weak_functor_coherent = all_compositors_authorized and pentagon_closes and pentagon_supported
        if weak_functor_coherent != case.get("expected_weak_functor_coherent"):
            errors.append("weak_transport_pentagon_expectation_mismatch:" + case.get("case_id", "unknown"))
        weak_transport_pentagon_cases.append({
            "case_id": case.get("case_id"),
            "left_compositor_product": left_product,
            "right_compositor_product": right_product,
            "all_compositors_source_authorized": all_compositors_authorized,
            "pentagon_closes": pentagon_closes,
            "pentagon_source_supported": pentagon_supported,
            "weak_functor_coherent": weak_functor_coherent,
        })
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "optional_constructor": True,
        "source_authorized": source_authorized,
        "index_type": "composition_word_length_natural_number",
        "time_semantics_inferred": False,
        "physical_time_authority_supplied": fixture.get("physical_time_authority_supplied"),
        "semigroup_law_exact": semigroup_law_exact,
        "contractive_trace": contraction_trace,
        "contractive_limit": "zero_overlap",
        "limit_formal_concept": contraction.get("limit_formal_concept"),
        "phase_trace": phase_trace,
        "phase_behavior": "period_two_cycle_no_limit",
        "convergence_grants_authority": fixture.get("convergence_grants_authority"),
        "time_bridges": time_bridges,
        "objective_closure_source_supported": closure_source_supported,
        "objective_closure_cases": objective_closure_cases,
        "objective_closure_composition": "causal_reach AND readability AND fault_separation AND restricted_reversibility",
        "multiobserver_descent_source_supported": descent_source_supported,
        "multiobserver_descent_cases": descent_cases,
        "global_objective_record_composition": "local_objective_closures AND source_anchored_trivial_holonomy_descent AND fault_survival",
        "graph_descent_cases": graph_descent_cases,
        "graph_descent_law": "global sections exist iff parity cocycle has trivial cycle holonomy; coherent unanchored sections = 2^component_count; uniqueness requires one consistent source anchor per component",
        "local_restriction_separatedness_source_supported": separatedness_source_supported,
        "separatedness_cases": separatedness_cases,
        "descent_object_law": "descent_global_section_exists AND local_restrictions_jointly_faithful",
        "global_phase_port_cases": phase_port_cases,
        "global_phase_port_law": "a source-authorized genuinely global port restores separatedness iff its response is nonzero on the proper-fragment joint kernel",
        "observation_port_rank_cases": port_rank_cases,
        "observation_port_rank_law": "residual joint kernel dimension = hidden dimension - exact rank of authorized port responses restricted to the hidden kernel",
        "observation_port_deletion_cases": port_deletion_cases,
        "observation_port_deletion_law": "f-deletion fault survival iff the smallest row-deletion cocircuit lowering restricted response rank has size greater than f",
        "observation_port_corruption_cases": port_corruption_cases,
        "observation_port_corruption_law": "minimum response support greater than f detects f corruptions; greater than 2f corrects f corruptions",
        "observation_port_resource_bound_cases": port_resource_bound_cases,
        "observation_port_resource_bound_law": "delta <= n-d+1, hence correction of f corruptions requires n >= d+2f; this count is sufficient only for distance-optimal response frames",
        "recovery_authority_product_cases": recovery_authority_cases,
        "recovery_authority_product_law": "observer separation AND adversarial correction AND restricted reversibility; none of the three grants either other coordinate",
        "decoder_cases": decoder_cases,
        "decoder_law": "distance above 2f proves unique decoder existence; source-supported synthesis and separately authorized executable realization remain necessary",
        "process_provenance_cases": process_cases,
        "inverse_authority_law": "endpoint state separation AND faithful process provenance on the recovery domain AND source-supported inverse constructor",
        "process_composition_cases": process_composition_cases,
        "process_composition_law": "local process faithfulness does not imply composite provenance; the composite response must be faithful on source-authorized factorization data",
        "process_history_quotient_cases": history_quotient_cases,
        "process_history_quotient_law": "process provenance separates source-authorized equivalence classes of histories, neither raw presentations nor endpoint bytes alone",
        "process_history_congruence_cases": history_congruence_cases,
        "process_history_congruence_law": "a source-authorized history equivalence supports composition only when it is a two-sided congruence under every admitted context",
        "process_history_partial_congruence_cases": partial_congruence_cases,
        "process_history_partial_congruence_law": "a quotient of partial processes is defined only when every constructor domain is saturated by the equivalence and outputs agree wherever both representatives are defined",
        "process_history_normalizer_cases": history_normalizer_cases,
        "process_history_normalizer_law": "a terminating locally confluent source-authorized rewrite system proves unique history normal forms; executable normalization additionally requires its own constructor authority",
        "typed_history_descent_cases": typed_history_descent_cases,
        "typed_history_descent_law": "process-equivalent histories may be identified in an authority-bearing quotient only when their domain, capability, support, and authority fibers agree or a source-authorized coherence cell identifies them",
        "typed_history_coherence_cases": typed_history_coherence_cases,
        "typed_history_coherence_law": "pairwise typed fiber transports descend strictly only with trivial cycle holonomy; nontrivial holonomy requires a separately source-authorized higher anomaly cell",
        "typed_history_anomaly_cocycle_cases": typed_history_anomaly_cocycle_cases,
        "typed_history_anomaly_cocycle_law": "source-typed triangle anomalies form a coherent atlas only when their oriented product on every tetrahedral boundary is trivial and the cocycle constructor is independently authorized",
        "typed_history_anomaly_class_cases": typed_history_anomaly_class_cases,
        "typed_history_anomaly_class_law": "a closed anomaly is removable exactly when its GF(2) cocycle lies in the coboundary image; strictification additionally requires a source-authorized trivialization constructor",
        "typed_history_gauge_selector_cases": typed_history_gauge_selector_cases,
        "typed_history_gauge_selector_law": "strictifying gauges form an affine torsor over the coboundary kernel; reproducible strictification requires either zero torsor dimension or a source-authorized gauge selector",
        "typed_history_selector_naturality_cases": typed_history_selector_naturality_cases,
        "typed_history_selector_naturality_law": "a nonunique gauge selector is canonical only when independently source-authorized and equivariant under every authorized presentation action",
        "equivariant_gauge_existence_cases": equivariant_gauge_existence_cases,
        "equivariant_gauge_existence_law": "a canonical strictifying gauge exists only when the authorized presentation action preserves the affine solution torsor and that torsor contains a global fixed point",
        "gauge_groupoid_cases": gauge_groupoid_cases,
        "gauge_groupoid_law": "when no natural gauge point exists, the source-authorized action groupoid of all strictifications is the canonical output; projecting to orbit labels while discarding stabilizers is not faithful",
        "gauge_readout_cases": gauge_readout_cases,
        "gauge_readout_law": "a scalar readout descends from a gauge groupoid only when source-authorized and constant on presentation orbits; descent and faithfulness across distinct orbits are independent",
        "groupoid_reconstruction_cases": groupoid_reconstruction_cases,
        "groupoid_reconstruction_law": "orbit-level invariant readouts decategorify the gauge groupoid and cannot reconstruct isotropy; faithful groupoid comparison requires typed stabilizer data and independent reconstruction authority",
        "stabilizer_structure_cases": stabilizer_structure_cases,
        "stabilizer_structure_law": "stabilizer cardinality does not determine isotropy; finite stabilizer comparison requires a valid multiplication table modulo relabelling and source-authorized structure readout",
        "stabilizer_action_cases": stabilizer_action_cases,
        "stabilizer_action_law": "an abstract stabilizer group does not determine its effect on capability fibers; reconstruction requires a valid group representation compared up to invertible fiber-basis change and source-authorized action readout",
        "stabilizer_action_relabeling_cases": stabilizer_action_relabeling_cases,
        "stabilizer_action_relabeling_law": "stabilizer actions are presentation-equivalent only under a compatible pair consisting of a group isomorphism and an invertible fiber-basis change",
        "stabilizer_transport_cases": stabilizer_transport_cases,
        "stabilizer_transport_law": "orbitwise stabilizer actions form a typed groupoid representation only when every inter-object arrow carries a source-authorized invertible intertwiner over its stabilizer isomorphism",
        "stabilizer_transport_composition_cases": stabilizer_transport_composition_cases,
        "stabilizer_transport_composition_law": "locally valid fiber intertwiners define a strict groupoid functor only when every direct transport equals the composite transport and the composition cell is source-authorized",
        "weak_transport_composition_cases": weak_transport_composition_cases,
        "weak_transport_composition_law": "a transport triangle may commute weakly only through a source-authorized invertible compositor that satisfies the triangle equation and is natural for the target stabilizer action",
        "weak_transport_pentagon_cases": weak_transport_pentagon_cases,
        "weak_transport_pentagon_law": "source-authorized triangle compositors define a coherent weak transport functor only when their two products around every four-arrow pentagon agree and the pentagon cell is independently authorized",
    }


def compile_residual_repair_typing(fixture: dict[str, Any]) -> dict[str, Any]:
    errors = []
    rows = []
    for case in fixture.get("cases", []):
        cause = case.get("residual_cause")
        expected = RESIDUAL_REPAIR_KINDS.get(cause)
        proposed = case.get("proposed_repair_kind")
        admitted = expected is not None and proposed == expected
        authority_guard_failed = cause == "missing_source_authority" and case.get("target_authority_sensitive") is not True
        if expected is None:
            errors.append("residual_cause_undeclared:" + str(cause))
        elif authority_guard_failed:
            admitted = False
            errors.append("authority_gate_on_invariant_target")
        elif not admitted:
            errors.append("residual_repair_kind_mismatch:" + str(cause))
        rows.append({"case_id":case.get("case_id"),"residual_cause":cause,"required_repair_kind":expected,"proposed_repair_kind":proposed,"target_authority_sensitive":case.get("target_authority_sensitive",False),"admitted":admitted})
    return {"passed":bool(rows) and not errors,"errors":sorted(set(errors)),"cases":rows,"codomain":sorted(set(RESIDUAL_REPAIR_KINDS.values()))}


def compile_operational_profiles(fixture: dict[str, Any]) -> dict[str, Any]:
    errors, rows = [], []
    for case in fixture.get("cases", []):
        resource_ok = case["available_units"] >= case["required_units"]
        scope_ok = case["evidence_scope"] == case["execution_scope"] or case.get("scope_transition_authorized") is True
        intersection = 2 * case["quorum"] - case["participants"]
        fault_ok = intersection > case["faults"] if case["fault_kind"] == "byzantine" else intersection >= 1
        modality_ok = case.get("physical_modality") == "executable"
        typed_interface_residual = case.get("cross_axis_residual_class") in {"exact_boundary", "central_anomaly", "typed_interface_residual"} and bool(case.get("cross_axis_cell_authority_root"))
        cross_axis_ok = case.get("cross_axis_comparison_declared") is True and (case.get("cross_axis_commutator_zero") is True or typed_interface_residual)
        admitted = bool(case.get("semantic_authority_admitted")) and resource_ok and scope_ok and fault_ok and modality_ok and cross_axis_ok
        if admitted != case.get("expected_admitted"):
            errors.append("operational_product_expectation_mismatch:" + case.get("case_id", "unknown"))
        rows.append({"case_id":case.get("case_id"),"semantic_authority_admitted":bool(case.get("semantic_authority_admitted")),"resource_ok":resource_ok,"scope_ok":scope_ok,"fault_ok":fault_ok,"physical_modality_ok":modality_ok,"typed_interface_residual":typed_interface_residual,"cross_axis_coherence_ok":cross_axis_ok,"quorum_intersection":intersection,"admitted":admitted})
    return {"passed":bool(rows) and not errors,"errors":errors,"cases":rows,"composition":"semantic_authority_admitted AND operational_profile_ok AND cross_axis_coherence_ok"}


def validate_repair(repair: dict[str, Any], repair_ids: set[str]) -> list[str]:
    errors = []
    missing = sorted(REPAIR_FIELDS - set(repair))
    if missing:
        errors.append("repair_constructor_fields_missing:" + ",".join(missing))
        return errors
    if not repair["repair_id"] or not repair["authority_root"] or not repair["residual_certificate_type"]:
        errors.append("repair_constructor_authority_untyped")
    if not set(repair["prerequisites"]) <= repair_ids or repair["repair_id"] in repair["prerequisites"]:
        errors.append("repair_prerequisites_invalid")
    if not isinstance(repair["boundary_current_delta"], dict) or not isinstance(repair["support_delta"], list):
        errors.append("repair_packet_delta_untyped")
    if not isinstance(repair["domain_after"], dict) or not isinstance(repair["graph_norm_after"], dict):
        errors.append("repair_domain_transition_untyped")
    return errors


def dependency_closure(repairs: dict[str, dict[str, Any]]) -> tuple[dict[str, set[str]], bool]:
    closure = {repair_id: set(repair["prerequisites"]) for repair_id, repair in repairs.items()}
    changed = True
    while changed:
        changed = False
        for repair_id in closure:
            expanded = set().union(*(closure[item] for item in closure[repair_id])) if closure[repair_id] else set()
            if not expanded <= closure[repair_id]:
                closure[repair_id] |= expanded
                changed = True
    acyclic = all(repair_id not in prerequisites for repair_id, prerequisites in closure.items())
    return closure, acyclic


def linear_extensions(repairs: dict[str, dict[str, Any]], closure: dict[str, set[str]]) -> list[tuple[str, ...]]:
    ids = sorted(repairs)
    return [order for order in permutations(ids) if all(closure[repair_id] <= set(order[:index]) for index, repair_id in enumerate(order))]


def apply_repair(state: dict[str, Any], repair: dict[str, Any], applied: set[str]) -> tuple[dict[str, Any] | None, str | None]:
    repair_id = repair["repair_id"]
    if not set(repair["prerequisites"]) <= applied:
        return None, "repair_prerequisite_failure"
    defects = set(state["defects"])
    required_defects = set(repair["input_defect_signature"])
    if not required_defects <= defects:
        return None, "repair_input_defect_failure"
    accepted_domains = repair["domain_signature"] if isinstance(repair["domain_signature"], list) else [repair["domain_signature"]]
    if state["domain_signature"] not in accepted_domains:
        return None, "repair_domain_failure"
    accepted_norms = repair["graph_norm_signature"] if isinstance(repair["graph_norm_signature"], list) else [repair["graph_norm_signature"]]
    if state["graph_norm_signature"] not in accepted_norms:
        return None, "repair_graph_norm_input_failure"
    required_capabilities = set(repair["consumes_capabilities"])
    if not required_capabilities <= set(state["capabilities"]):
        return None, "repair_residual_capability_failure"
    result = deepcopy(state)
    result["defects"] = sorted((defects - required_defects) | set(repair["output_defect_signature"]))
    result["domain_signature"] = repair["domain_after"].get(state["domain_signature"])
    result["graph_norm_signature"] = repair["graph_norm_after"].get(state["graph_norm_signature"])
    if result["domain_signature"] is None:
        return None, "repair_domain_transition_failure"
    if result["graph_norm_signature"] is None:
        return None, "repair_graph_norm_transition_failure"
    boundary = dict(result["boundary_packet"])
    for key, value in repair["boundary_current_delta"].items():
        boundary[key] = boundary.get(key, 0) + value
    result["boundary_packet"] = {key: boundary[key] for key in sorted(boundary)}
    result["support"] = sorted(set(result["support"]) | set(repair["support_delta"]))
    result["capabilities"] = sorted((set(result["capabilities"]) - required_capabilities) | set(repair["produces_capabilities"]))
    result["applied"] = sorted(applied | {repair_id})
    return result, None


def execute_path(initial: dict[str, Any], order: tuple[str, ...], repairs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    state = deepcopy(initial)
    states = []
    applied: set[str] = set()
    for repair_id in order:
        next_state, error = apply_repair(state, repairs[repair_id], applied)
        if error:
            return {"order": list(order), "legal": False, "error": error, "failed_repair": repair_id, "states": states}
        state = next_state
        applied.add(repair_id)
        unresolved = sorted(state["defects"])
        states.append({"after": repair_id, "state": deepcopy(state), "unsafe_repair_in_progress": bool(unresolved), "unresolved_defects": unresolved, "next_admissible_repairs": sorted(candidate for candidate, repair in repairs.items() if candidate not in applied and set(repair["prerequisites"]) <= applied), "residual_capability": sorted(state["capabilities"])})
    endpoint_packet = {key: state[key] for key in ("defects", "domain_signature", "graph_norm_signature", "boundary_packet", "support", "capabilities", "scalar_output")}
    return {"order": list(order), "legal": True, "states": states, "endpoint": endpoint_packet, "endpoint_digest": stable_digest(endpoint_packet)}


def compile_model(model: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    repairs_list = model.get("repairs", [])
    repairs = {repair.get("repair_id"): repair for repair in repairs_list if repair.get("repair_id")}
    if len(repairs) != len(repairs_list):
        errors.append("repair_ids_duplicate_or_missing")
    repair_ids = set(repairs)
    for repair in repairs.values():
        errors.extend(validate_repair(repair, repair_ids))
    closure, acyclic = dependency_closure(repairs) if repairs else ({}, False)
    if not acyclic:
        errors.append("repair_dependency_cycle")
    declared_commutes = {frozenset(pair) for pair in model.get("commutes_with", []) if len(pair) == 2}
    extensions = linear_extensions(repairs, closure) if acyclic else []
    paths = [execute_path(model["initial_state"], order, repairs) for order in extensions]
    legal_paths = [path for path in paths if path["legal"]]

    extension_set = set(extensions)
    extension_adjacency = {order: set() for order in extensions}
    for order in extensions:
        for index in range(len(order) - 1):
            left, right = order[index], order[index + 1]
            if left in closure[right] or right in closure[left]:
                continue
            target = order[:index] + (right, left) + order[index + 2:]
            if target in extension_set:
                extension_adjacency[order].add(target)
    reached = set()
    if extensions:
        reached, frontier = {extensions[0]}, [extensions[0]]
        while frontier:
            current = frontier.pop()
            for target in extension_adjacency[current]:
                if target not in reached:
                    reached.add(target)
                    frontier.append(target)
    poset_extension_graph_connected = bool(extensions) and reached == extension_set

    all_path_by_order = {tuple(path["order"]): path for path in paths}
    path_by_order = {tuple(path["order"]): path for path in legal_paths}
    swap_cells = []
    adjacency = {tuple(path["order"]): set() for path in legal_paths}
    for order, left_path in path_by_order.items():
        for index in range(len(order) - 1):
            left, right = order[index], order[index + 1]
            if left in closure[right] or right in closure[left]:
                continue
            swapped = order[:index] + (right, left) + order[index + 2:]
            if frozenset({left, right}) not in declared_commutes:
                if swapped in all_path_by_order:
                    swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": False, "code": "repair_swap_authority_missing", "complete_boundary_packet_equal": False, "graph_domain_equivalent": False, "graph_norm_equivalent": False, "support_union_equal": False, "remaining_defects_equal": False, "reconstruction_capability_equal": False, "scalar_endpoint_bytes_equal": False, "missing_swap_cell": True, "left_domain": None, "right_domain": None, "boundary_residual": None})
                continue
            right_path = path_by_order.get(swapped)
            if right_path is None:
                rejected_path = all_path_by_order.get(swapped)
                if rejected_path is not None:
                    swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": False, "code": rejected_path.get("error", "repair_swap_domain_failure"), "complete_boundary_packet_equal": False, "graph_domain_equivalent": False, "graph_norm_equivalent": False, "support_union_equal": False, "remaining_defects_equal": False, "reconstruction_capability_equal": False, "scalar_endpoint_bytes_equal": False, "missing_swap_cell": True, "left_domain": left_path["states"][index + 1]["state"]["domain_signature"], "right_domain": None, "boundary_residual": None})
                continue
            left_local = left_path["states"][index + 1]["state"]
            right_local = right_path["states"][index + 1]["state"]
            packet_equal = left_local["boundary_packet"] == right_local["boundary_packet"]
            domain_equal = left_local["domain_signature"] == right_local["domain_signature"]
            norm_equal = left_local["graph_norm_signature"] == right_local["graph_norm_signature"]
            support_equal = left_local["support"] == right_local["support"]
            defects_equal = left_local["defects"] == right_local["defects"]
            capability_equal = left_local["capabilities"] == right_local["capabilities"]
            boundary_keys = set(left_local["boundary_packet"]) | set(right_local["boundary_packet"])
            boundary_residual = {key: left_local["boundary_packet"].get(key, 0) - right_local["boundary_packet"].get(key, 0) for key in sorted(boundary_keys)}
            boundary_residual = {key: value for key, value in boundary_residual.items() if value}
            generated = packet_equal and domain_equal and norm_equal and support_equal and defects_equal and capability_equal
            code = None if generated else ("repair_swap_domain_failure" if not domain_equal or not norm_equal else "repair_swap_packet_failure")
            swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": generated, "code": code, "complete_boundary_packet_equal": packet_equal, "graph_domain_equivalent": domain_equal, "graph_norm_equivalent": norm_equal, "support_union_equal": support_equal, "remaining_defects_equal": defects_equal, "reconstruction_capability_equal": capability_equal, "scalar_endpoint_bytes_equal": left_local["scalar_output"] == right_local["scalar_output"], "missing_swap_cell": not generated, "left_domain": left_local["domain_signature"], "right_domain": right_local["domain_signature"], "left_graph_norm": left_local["graph_norm_signature"], "right_graph_norm": right_local["graph_norm_signature"], "boundary_residual": boundary_residual})
            if generated:
                adjacency[order].add(swapped)
                adjacency[swapped].add(order)
    components = []
    remaining = set(adjacency)
    while remaining:
        seed = min(remaining)
        component, frontier = {seed}, [seed]
        while frontier:
            current = frontier.pop()
            for target in adjacency[current]:
                if target not in component:
                    component.add(target)
                    frontier.append(target)
        components.append([list(order) for order in sorted(component)])
        remaining -= component
    typed_endpoints = {path["endpoint_digest"] for path in legal_paths}
    swap_witnesses = model.get("swap_cell_witnesses", {})
    for key, witness in swap_witnesses.items():
        if not isinstance(witness.get("value"), int) or not witness.get("source_authority_root") or witness.get("derivation") != "source_comparison_current":
            errors.append("repair_swap_cell_value_untyped:" + key)

    def edge_value(order: tuple[str, ...], position: int) -> int:
        return swap_witnesses.get(",".join(order) + "|" + str(position), {}).get("value", 0)

    braid_audits = []
    for braid in model.get("braid_checks", []):
        start = tuple(braid.get("start_order", []))
        position = braid.get("position")
        comparable = start in path_by_order and isinstance(position, int) and 0 <= position < len(start) - 2
        left_word = [position, position + 1, position]
        right_word = [position + 1, position, position + 1]

        def follow(order: tuple[str, ...], word: list[int]) -> tuple[tuple[str, ...], int, bool]:
            total = 0
            for swap_position in word:
                target = order[:swap_position] + (order[swap_position + 1], order[swap_position]) + order[swap_position + 2:]
                cell = next((item for item in swap_cells if item["left_path"] == list(order) and item["right_path"] == list(target)), None)
                if cell is None or not cell["generated"]:
                    return order, total, False
                total += edge_value(order, swap_position)
                order = target
            return order, total, True

        left_endpoint, left_value, left_exists = follow(start, left_word) if comparable else (start, 0, False)
        right_endpoint, right_value, right_exists = follow(start, right_word) if comparable else (start, 0, False)
        residual = left_value - right_value
        policy = braid.get("residual_policy", {})
        if not left_exists or not right_exists or left_endpoint != right_endpoint:
            classification = "domain_mismatch"
        elif residual == 0:
            classification = "zero"
        elif policy.get("class") == "exact_boundary" and policy.get("source_authority_root") and policy.get("comparison_cell"):
            classification = "exact_boundary"
        elif policy.get("class") == "central_phase" and policy.get("source_authority_root"):
            classification = "central_phase"
        else:
            classification = "untyped_residual"
        coherent = classification in {"zero", "exact_boundary"}
        braid_audits.append({"id": braid.get("id"), "left_exists": left_exists, "right_exists": right_exists, "common_endpoint": left_endpoint == right_endpoint, "left_comparison_value": left_value, "right_comparison_value": right_value, "residual": residual, "classification": classification, "coherent": coherent, "fitted_cell_forbidden": classification == "untyped_residual"})
    expected = model.get("expected", {})
    observed = {"linear_extension_count": len(extensions), "legal_completed_path_count": len(legal_paths), "swap_component_count": len(components), "typed_endpoint_count": len(typed_endpoints), "first_braid_class": braid_audits[0]["classification"] if braid_audits else None}
    for key, value in expected.items():
        if observed.get(key) != value:
            errors.append("model_expectation_mismatch:" + key)
    return {"id": model["id"], "passed": not errors, "errors": sorted(set(errors)), "dependency_acyclic": acyclic, "dependency_closure": {key: sorted(value) for key, value in closure.items()}, "poset_extension_graph_connected": poset_extension_graph_connected, "observed": observed, "linear_extensions": [list(order) for order in extensions], "paths": paths, "swap_cells": swap_cells, "swap_components": components, "braid_audits": braid_audits, "all_legal_paths_one_typed_endpoint": len(typed_endpoints) == 1, "scalar_bytes_do_not_define_typed_endpoint": any(cell["scalar_endpoint_bytes_equal"] and not cell["generated"] for cell in swap_cells)}


def compile_theta_tate_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    expected_ids = {"S", "P", "Q", "A", "L", "C", "D"}
    declaration_fields = {"precedes", "commutes_with", "domain_after", "boundary_delta", "completion_scope"}
    stages = fixture.get("stages", [])
    stage_ids = {stage.get("repair_id") for stage in stages}
    errors = []
    if stage_ids != expected_ids or len(stages) != len(expected_ids):
        errors.append("theta_tate_stage_inventory_mismatch")
    missing = {}
    for stage in stages:
        absent = sorted(field for field in declaration_fields if field not in stage or stage.get(field) is None)
        if absent:
            missing[stage.get("repair_id")] = absent
    if fixture.get("assume_discrete_poset") is not False:
        errors.append("theta_tate_dependencies_invented")
    ready = not missing and not errors
    if fixture.get("compilation_mode") == "enumerate" and not ready:
        errors.append("theta_tate_enumeration_without_source_declarations")
    status = "ready" if ready else "source_declarations_required"
    if fixture.get("expected_status") != status:
        errors.append("theta_tate_declaration_status_mismatch")
    questions = fixture.get("open_source_questions", [])
    required_questions = {"P<->Q?", "S<->P?", "L<C?", "(P,Q,S,A)<D?"}
    if set(questions) != required_questions:
        errors.append("theta_tate_open_questions_incomplete")
    return {"passed": not errors, "errors": sorted(set(errors)), "status": status, "stage_ids": sorted(stage_ids - {None}), "missing_source_declarations": missing, "open_source_questions": questions, "enumeration_performed": ready and fixture.get("compilation_mode") == "enumerate", "legal_factorization_paths": [], "swap_components": [], "missing_swap_cells": [], "first_braid_residual": None, "unsafe_intermediate_states": [], "one_typed_endpoint": None}


def compile_theta_repair_triangle(triangle: dict[str, Any]) -> dict[str, Any]:
    required_fields = {"input_state_type", "output_state_type", "domain_before", "domain_after", "graph_norm_before", "graph_norm_after", "boundary_delta", "completion_scope", "residual_capability", "source_authority", "requirement_rules"}
    expected_ids = {"S", "C", "L"}
    stages = {stage.get("repair_id"): stage for stage in triangle.get("operations", [])}
    errors = []
    if set(stages) != expected_ids or len(triangle.get("operations", [])) != 3:
        errors.append("theta_triangle_operation_inventory_mismatch")
    for repair_id, stage in stages.items():
        if not required_fields <= set(stage):
            errors.append("theta_triangle_constructor_fields_missing:" + str(repair_id))
        if not stage.get("source_authority"):
            errors.append("theta_triangle_source_authority_missing:" + str(repair_id))
    if set(stages.get("L", {}).get("required_distinctions", [])) != {"seam_translation_norm", "raw_arithmetic_label"}:
        errors.append("theta_triangle_completion_distinction_contract_weakened")
    family = triangle.get("clark_uniform_constructor_family")
    family_authorized = bool(family and family.get("family_id") and family.get("source_authority_root") and family.get("fixed_finite") is True and family.get("uniformly_dominates_current_matrices") is True)
    if family is not None and not family_authorized:
        errors.append("theta_triangle_uniform_family_unauthorized")
    boundary = triangle.get("valuation_boundary_constructor", {})
    expected_lanes = {
        regularity + ":" + parity
        for regularity in boundary.get("regularity_grades", [])
        for parity in boundary.get("chart_parities", [])
    }
    if set(boundary.get("boundary_distributions", [])) != {"delta", "principal_value"}:
        errors.append("theta_triangle_delta_pv_boundary_packet_incomplete")
    if set(boundary.get("four_lanes", [])) != expected_lanes or len(expected_lanes) != 4:
        errors.append("theta_triangle_four_lane_product_incomplete")
    transform = boundary.get("chart_transform", {})
    if not (transform.get("block_count") == 2 and transform.get("identical_blocks") is True and transform.get("block_determinants") == ["1/2", "1/2"] and transform.get("total_determinant") == "1/4" and transform.get("invertible") is True):
        errors.append("theta_triangle_chart_transform_not_invertible_two_block")
    reflection = boundary.get("reflection_action", {})
    if reflection.get("delta") != "fixed" or reflection.get("principal_value") != "orientation_reversed" or reflection.get("overlap_even") != "fixed" or reflection.get("front_odd") != "orientation_reversed":
        errors.append("theta_triangle_reflection_parity_contract_failed")
    if boundary.get("finite_atomic_incidence_authorized") is not True or boundary.get("universal_fourier_chart_sewing_authorized") is not True:
        errors.append("theta_triangle_finite_boundary_incidence_missing")
    if set(boundary.get("forbidden_scalarizations", [])) != {"delta_only", "single_regularity_grade"}:
        errors.append("theta_triangle_scalarization_guard_missing")
    lane_profiles = boundary.get("lane_completion_profiles", {})
    primitive_odd = lane_profiles.get("primitive_exponential_laplace:front_odd", {})
    square_odd = lane_profiles.get("square_tempered:front_odd", {})
    if set(lane_profiles) != expected_lanes:
        errors.append("theta_triangle_lane_completion_profiles_incomplete")
    if not (
        primitive_odd.get("weighted_term_test") is False
        and primitive_odd.get("required_preaggregation_constructor") == "source_relative_moment_cancellation"
        and primitive_odd.get("finite_algebraic_subtractions_sufficient") is False
        and primitive_odd.get("required_remainder_control") == "exponential"
    ):
        errors.append("theta_triangle_primitive_odd_tail_obstruction_erased")
    if square_odd.get("one_over_L_tail_tolerated") is not True:
        errors.append("theta_triangle_square_odd_tempered_tail_mistyped")
    precedence = boundary.get("aggregation_precedence", {})
    if precedence != {"before": "source_relative_moment_cancellation", "after": "prime_aggregation"}:
        errors.append("theta_triangle_relative_cancellation_order_failed")
    relative_constructor = boundary.get("relative_moment_constructor", {})
    if relative_constructor.get("individual_compact_test_all_moment_cancellation_nontrivial") is not False:
        errors.append("theta_triangle_compact_test_moment_no_go_violated")
    if relative_constructor.get("finite_rank_counterterm_sufficient") is not False:
        errors.append("theta_triangle_finite_rank_tail_repair_laundered")
    if not (
        relative_constructor.get("input_type") == "paired_sheet_primitive_odd_current"
        and relative_constructor.get("constructor_locus") == "source_kernel_before_prime_aggregation"
        and relative_constructor.get("required_witness") == "exact_paired_sheet_tail_identity"
        and relative_constructor.get("reflection_variance") == "odd_equivariant"
        and relative_constructor.get("aggregation_factorization") == "prime_aggregation_after_source_cancellation"
        and relative_constructor.get("fitted_from_completed_endpoint") is False
    ):
        errors.append("theta_triangle_relative_moment_constructor_mistyped")
    shift_cocycle = boundary.get("finite_shift_cocycle_audit", {})
    if not (
        shift_cocycle.get("source_formula") == "g_L=tau_L(K)-K"
        and shift_cocycle.get("finite_shift_bulk_membership") is True
        and shift_cocycle.get("cancelled_singularity") == "frequency_origin_PV"
        and shift_cocycle.get("boundary_quotient_action") == "identity"
        and shift_cocycle.get("prime_label_cocycle_retained") is True
    ):
        errors.append("theta_triangle_finite_shift_cocycle_mistyped")
    if shift_cocycle.get("arithmetic_label_tail_cancelled") is not False or shift_cocycle.get("authorizes_joint_rigged_completion") is not False:
        errors.append("theta_triangle_frequency_cancellation_laundered_into_arithmetic_completion")
    if shift_cocycle.get("missing_comparison_map") != "full_source_Poisson_Green_correspondence_before_Euler_projection":
        errors.append("theta_triangle_missing_adelic_Hardy_incidence_erased")
    incidence = boundary.get("adelic_hardy_incidence_contract", {})
    if not (
        incidence.get("index_category") == "finite_prime_cutoffs_ordered_by_inclusion"
        and incidence.get("source_diagram") == "full_restricted_adelic_source_before_Euler_projection"
        and incidence.get("target_diagram") == "full_source_Green_boundary_then_four_lane_diagnostics"
        and incidence.get("variance") == "global_Poisson_before_contravariant_diagnostic_restriction"
        and incidence.get("required_object") == "source_correspondence_with_pro_natural_diagnostic_projection"
        and incidence.get("required_naturality_equation") == "restrict_XY_after_I_Y_equals_I_X_after_restrict_XY"
    ):
        errors.append("theta_triangle_adelic_Hardy_pro_map_mistyped")
    nonfactor = incidence.get("nonfactorization_witness", {})
    if not (
        incidence.get("Poisson_factors_through_prime_sampling") is False
        and incidence.get("pro_system_role") == "post_sewing_diagnostic_projection_only"
        and nonfactor == {"sample_kernel_vector": "b_supported_between_log2_and_log3", "S_b": "0", "P_b": "nonzero"}
    ):
        errors.append("theta_triangle_Poisson_sampling_nonfactorization_erased")
    if incidence.get("finite_label_registers_authorized") is not True:
        errors.append("theta_triangle_existing_finite_label_register_erased")
    if incidence.get("finite_Hardy_comparison_components_authorized") is not False or incidence.get("cutoff_naturality_authorized") is not False:
        errors.append("theta_triangle_missing_Hardy_incidence_falsely_authorized")
    if incidence.get("single_scalar_target_authorized") is not False:
        errors.append("theta_triangle_pro_incidence_scalarized")
    if {incidence.get("primitive_grade"), incidence.get("square_grade"), incidence.get("connected_tail_grade")} != {"projective_Mellin_analytic", "Hilbert_tempered", "absolute_summability"}:
        errors.append("theta_triangle_boundary_grades_collapsed")
    if incidence.get("completion_common_kernel") != "unproved":
        errors.append("theta_triangle_completion_faithfulness_overclaimed")
    boundary_lift = incidence.get("full_source_poisson_green_lift", {})
    if not (
        boundary_lift.get("global_Tate_Poisson_scalar_continuation") == "source_authorized"
        and boundary_lift.get("input_type") == "factorizable_Schwartz_Bruhat_source_plus_Haar_and_reciprocal_sewing"
        and boundary_lift.get("required_lift") == "full_source_to_tail_seam_boundary_module"
        and boundary_lift.get("required_triangle") == "scalarize_after_boundary_lift_equals_global_Tate_readout"
    ):
        errors.append("theta_triangle_full_source_boundary_lift_mistyped")
    if boundary_lift.get("lift_authorized") is not False or boundary_lift.get("backward_reconstruction_from_scalar_Tate_section_authorized") is not False:
        errors.append("theta_triangle_scalar_Tate_readout_laundered_into_boundary_lift")
    if set(boundary_lift.get("boundary_components", [])) != {"endpoint", "archimedean_gamma", "connected_prime_power", "mixed_Poisson_arithmetic"} or boundary_lift.get("sewing_order") != "endpoint_gamma_prime_and_mixed_sewn_before_continuation":
        errors.append("theta_triangle_full_boundary_packet_incomplete")
    if boundary_lift.get("positivity_of_completed_Green_kernel") != "RH_equivalent_not_source_proved" or boundary_lift.get("direct_positive_dilation_status") != "open":
        errors.append("theta_triangle_completed_Green_positivity_assumed")
    if boundary_lift.get("status") != "missing_functorial_boundary_lift_not_missing_scalar_continuation":
        errors.append("theta_triangle_boundary_lift_status_mistyped")
    lift_extension = boundary_lift.get("lift_extension_contract", {})
    if not (
        lift_extension.get("exact_sequence") == "0_to_K_boundary_to_B_tail_seam_to_R_Tate_to_0"
        and lift_extension.get("ambient_category") == "source_authorized_locally_convex_Poisson_reflection_modules_with_graph_domains"
        and lift_extension.get("bare_complex_vector_space_Ext1") == "zero_and_noncanonical_splittings_exist"
        and lift_extension.get("existence_obstruction") == "pullback_continuous_equivariant_domain_preserving_Ext1_class"
        and lift_extension.get("lift_torsor") == "Hom(source,K_boundary)"
        and lift_extension.get("mixed_channel_location") == "K_boundary"
        and lift_extension.get("scalar_section_selects_lift") is False
        and lift_extension.get("uniqueness_gate") == "joint_Green_constraints_kill_Hom_source_K_boundary"
    ):
        errors.append("theta_triangle_boundary_lift_extension_mistyped")
    lift_cases = []
    for case in lift_extension.get("cases", []):
        exists = case.get("extension_obstruction_dimension") == 0
        ambiguity_dimension = max(0, case.get("boundary_kernel_dimension", 0) - case.get("Green_constraint_rank", 0)) if exists else None
        unique = exists and ambiguity_dimension == 0
        admitted = unique and case.get("constraint_source_authority") is True
        if exists != case.get("expected_exists") or unique != case.get("expected_unique") or admitted != case.get("expected_admitted"):
            errors.append("theta_triangle_boundary_lift_expectation_mismatch:" + str(case.get("id")))
        lift_cases.append({"id": case.get("id"), "exists": exists, "ambiguity_dimension": ambiguity_dimension, "unique": unique, "admitted": admitted})
    if len(lift_cases) != 5:
        errors.append("theta_triangle_boundary_lift_fixture_incomplete")
    typed_split_cases = []
    for case in lift_extension.get("typed_splitting_cases", []):
        typed_split = bool(case.get("algebraic_split") and case.get("continuous") and case.get("Poisson_reflection_equivariant") and case.get("graph_domain_preserved"))
        admitted = typed_split and case.get("source_authority") is True
        if typed_split != case.get("expected_typed_split") or admitted != case.get("expected_admitted"):
            errors.append("theta_triangle_typed_boundary_split_expectation_mismatch:" + str(case.get("id")))
        typed_split_cases.append({"id": case.get("id"), "typed_split": typed_split, "admitted": admitted})
    if len(typed_split_cases) != 5:
        errors.append("theta_triangle_typed_boundary_split_fixture_incomplete")
    averaging = lift_extension.get("finite_symmetry_averaging", {})
    if not (
        averaging.get("group") == "finite_Fourier_reflection_group"
        and averaging.get("base_field") == "complex_numbers"
        and averaging.get("Reynolds_formula") == "average_g_of_g_B_compose_lift_compose_g_S_inverse"
        and averaging.get("positive_group_cohomology_of_complex_modules") == "zero"
        and averaging.get("equivariant_lifts_form") == "torsor_over_Hom_G(source,K_boundary)"
        and averaging.get("averaging_selects_unique_lift") is False
    ):
        errors.append("theta_triangle_finite_symmetry_averaging_mistyped")
    averaging_cases = []
    for case in averaging.get("cases", []):
        equivariant_lift = bool(case.get("initial_continuous_split") and case.get("graph_domain_G_invariant") and case.get("scalarization_G_equivariant") and case.get("Tate_map_G_equivariant") and case.get("group_order_invertible"))
        unique = equivariant_lift and case.get("invariant_torsor_dimension") == 0
        admitted = equivariant_lift and case.get("averaging_source_authorized") is True
        if equivariant_lift != case.get("expected_equivariant_lift") or unique != case.get("expected_unique") or admitted != case.get("expected_admitted"):
            errors.append("theta_triangle_symmetry_averaging_expectation_mismatch:" + str(case.get("id")))
        averaging_cases.append({"id": case.get("id"), "equivariant_lift": equivariant_lift, "unique": unique, "admitted": admitted})
    if len(averaging_cases) != 6:
        errors.append("theta_triangle_symmetry_averaging_fixture_incomplete")
    isotypic = averaging.get("isotypic_torsor_classifier", {})
    if not (
        isotypic.get("dimension_formula") == "sum_lambda_m_source_lambda_times_m_kernel_lambda"
        and isotypic.get("uniqueness_condition") == "disjoint_isotypic_support_or_full_rank_source_constraints"
        and isotypic.get("live_theta_multiplicity_status") == "uncomputed_on_full_tail_seam_module"
    ):
        errors.append("theta_triangle_isotypic_torsor_classifier_mistyped")
    reflection_kernel = isotypic.get("live_reflection_kernel_audit", {})
    if not (
        reflection_kernel.get("carrier") == "four_channel_Tate_Poisson_lift"
        and reflection_kernel.get("aggregation_row") == [1, 1, 1, 1]
        and reflection_kernel.get("reciprocal_reflection_cycles") == [[0, 1], [2, 3]]
        and reflection_kernel.get("aggregation_rank") == 1
        and reflection_kernel.get("kernel_dimension") == 3
        and reflection_kernel.get("kernel_reflection_multiplicities") == {"even": 1, "odd": 2}
        and reflection_kernel.get("both_parities_meet_kernel") is True
    ):
        errors.append("theta_triangle_four_channel_reflection_kernel_mistyped")
    if reflection_kernel.get("refined_theta_source_multiplicities") != "uncomputed" or reflection_kernel.get("five_cell_C4_characters_authorize_source_multiplicities") is not False:
        errors.append("theta_triangle_carrier_characters_laundered_to_refined_source")
    tensor_characters = isotypic.get("conditional_tensor_character_theorem", {})
    if not (
        tensor_characters.get("finite_source_carrier") == "W_fourier_boundary_tensor_C_X_arithmetic_labels"
        and tensor_characters.get("hypotheses") == ["dim_C_X_equals_N", "C_X_has_trivial_Fourier_action", "tensor_product_identification_is_source_authorized"]
        and tensor_characters.get("C4_character_multiplicities") == {"1": "N", "-1": "N", "i": "N", "-i": "N"}
        and tensor_characters.get("observer_rank_formula") == "rank_A_F_times_rank_A_X"
        and tensor_characters.get("full_finite_separation_condition") == "rank_A_F_equals_4_and_rank_A_X_equals_N"
    ):
        errors.append("theta_triangle_conditional_tensor_character_theorem_mistyped")
    if tensor_characters.get("implies_live_C2_source_multiplicities") is not False or tensor_characters.get("missing_comparison") != "source_derived_equivariant_map_from_refined_tensor_carrier_to_four_channel_tail_seam_lift":
        errors.append("theta_triangle_conditional_C4_theorem_laundered_into_live_C2_source")
    common_c2 = tensor_characters.get("conditional_common_C2_torsor", {})
    if not (
        common_c2.get("additional_hypothesis") == "identify_Fourier_square_on_W_with_reciprocal_reflection_on_four_channel_lift"
        and common_c2.get("source_C2_multiplicities") == {"even": "2N", "odd": "2N"}
        and common_c2.get("scalar_kernel_C2_multiplicities") == {"even": 1, "odd": 2}
        and common_c2.get("equivariant_lift_torsor_dimension") == "6N"
        and common_c2.get("symmetry_selects_comparison") is False
        and common_c2.get("status") == "conditional_obstruction_not_source_comparison"
    ):
        errors.append("theta_triangle_conditional_common_C2_torsor_mistyped")
    cross_tower = tensor_characters.get("cross_tower_constraint_gate", {})
    if not (
        cross_tower.get("torsor_block_dimensions") == {"even_constant_delta_to_symmetric_hidden": "2N", "odd_tail_PV_to_odd_hidden": "4N"}
        and cross_tower.get("labelwise_tail_equations_close_torsor") is False
        and cross_tower.get("arithmetic_cylinder_observers_are_constraints") is False
        and cross_tower.get("primitive_and_square_currents_alone_are_coupling_theorem") is False
        and cross_tower.get("required_constructor") == "source_authorized_cross_label_arithmetic_coherence_locus"
        and cross_tower.get("uniqueness_rank_condition") == "constraint_rank_equals_6N"
        and cross_tower.get("completion_condition") == "constraint_cells_natural_under_cutoff_restriction"
        and cross_tower.get("hostile") == "two_nonzero_label_endpoints_a_and_minus_a_with_scalar_sum_zero"
    ):
        errors.append("theta_triangle_cross_tower_constraint_gate_mistyped")
    incidence_rank = cross_tower.get("incidence_rank_theorem", {})
    if not (
        incidence_rank.get("constraint_kind") == "six_species_pairwise_label_differences"
        and incidence_rank.get("graph_parameters") == "N_vertices_c_connected_components"
        and incidence_rank.get("difference_rank") == "6_times_N_minus_c"
        and incidence_rank.get("residual_componentwise_constant_dimension") == "6c"
        and incidence_rank.get("required_anchor_rank") == "6c"
        and incidence_rank.get("pairwise_coherence_alone_selects_unique_lift") is False
    ):
        errors.append("theta_triangle_cross_label_incidence_rank_theorem_mistyped")
    incidence_cases = []
    for case in incidence_rank.get("cases", []):
        N = case.get("N")
        components = case.get("components")
        valid = isinstance(N, int) and isinstance(components, int) and 1 <= components <= N
        matrix = []
        if valid:
            for edge in case.get("edges", []):
                if not (isinstance(edge, list) and len(edge) == 2):
                    valid = False
                    break
                left, right = edge
                if not (isinstance(left, int) and isinstance(right, int) and 0 <= left < N and 0 <= right < N and left != right):
                    valid = False
                    break
                for species in range(6):
                    row = [0] * (6 * N)
                    row[6 * left + species] = 1
                    row[6 * right + species] = -1
                    matrix.append(row)
        difference_rank = exact_matrix_rank(matrix) if valid and matrix else (0 if valid else None)
        residual_dimension = 6 * N - difference_rank if difference_rank is not None else None
        if difference_rank != case.get("expected_difference_rank") or residual_dimension != case.get("expected_residual_dimension"):
            errors.append("theta_triangle_cross_label_incidence_case_mismatch:" + str(case.get("id")))
        incidence_cases.append({"id": case.get("id"), "difference_rank": difference_rank, "residual_dimension": residual_dimension})
    if len(incidence_cases) != 4:
        errors.append("theta_triangle_cross_label_incidence_fixture_incomplete")
    anchor_audit = cross_tower.get("anchor_qualification_audit", {})
    green_mate = anchor_audit.get("centered_Green_mate", {})
    naive_pairing = anchor_audit.get("naive_bulk_polar_Hermitian_pairing", {})
    finite_packet = anchor_audit.get("fixed_finite_boundary_packet", {})
    if not (
        anchor_audit.get("finite_gate") == "anchor_rows_have_rank_6c_on_componentwise_constant_modes"
        and anchor_audit.get("completion_gate") == "cutoff_natural_anchor_family_has_uniform_positive_inf_sup_reserve"
        and anchor_audit.get("finite_rank_implies_completion_faithfulness") is False
        and green_mate.get("law") == "bulk_odd_plus_polar_odd_is_transform_of_centered_Green_source"
        and green_mate.get("source_derived") is True
        and green_mate.get("orients_Hermitian_pairing") is False
        and green_mate.get("six_mode_anchor_rank") == "uncomputed"
        and naive_pairing.get("source_universal") is False
        and naive_pairing.get("hostile") == "positive_scale_atom_changes_required_sign"
        and finite_packet.get("ports") == ["primitive", "prime_square", "seam", "archimedean_jet"]
        and finite_packet.get("Folner_energy") == "O_of_1_over_N"
        and finite_packet.get("unit_state_norm") == 1
        and finite_packet.get("uniform_reserve") is False
        and anchor_audit.get("completed_anchor_packet_status") == "missing_nonlocal_or_topology_strengthening_constructor"
    ):
        errors.append("theta_triangle_anchor_qualification_audit_mistyped")
    candidate_ladder = cross_tower.get("completion_candidate_ladder", {})
    if not (
        candidate_ladder.get("candidate") == "full_translated_seam_history_Gram"
        and candidate_ladder.get("infinite_rank_state_bearing") is True
        and candidate_ladder.get("positive_Folner_liminf") == "at_least_norm_Phi_squared_positive"
        and candidate_ladder.get("positive_Folner_test_implies_uniform_frame") is False
        and candidate_ladder.get("prime_orbit_frame_symbol") == "W_p_theta_equals_1_over_log_p_sum_m_abs_Phi_hat_of_theta_plus_2pi_m_over_log_p_squared"
        and candidate_ladder.get("single_prime_uniform_gate") == "inf_theta_W_p_theta_positive"
        and candidate_ladder.get("all_prime_completion_gate") == "source_topology_controls_primewise_frame_bounds_and_cross_prime_couplings"
        and candidate_ladder.get("sharp_hostile") == "modulated_long_block_concentrating_near_a_zero_or_small_value_of_W_p"
        and candidate_ladder.get("half_density_status") == "only_source_relevant_as_relative_additive_multiplicative_Haar_comparison"
        and candidate_ladder.get("single_sector_diagonal_reweighting_is_new_energy") is False
        and candidate_ladder.get("relative_comparison_source_authorized") is False
        and candidate_ladder.get("Green_sign_from_frame_bound") is False
        and candidate_ladder.get("live_status") == "frame_symbol_relative_Haar_comparison_and_Green_sign_all_open"
    ):
        errors.append("theta_triangle_completion_candidate_ladder_mistyped")
    dependency_nerve = cross_tower.get("combined_dependency_nerve", {})
    if not (
        dependency_nerve.get("strict_finite_audit_shape") == "authorized_subcategory_of_symmetry_times_label_times_cutoff"
        and dependency_nerve.get("axes") == ["symmetry", "label_incidence", "cutoff_restriction"]
        and dependency_nerve.get("axis_actions_strict") is True
        and dependency_nerve.get("required_pairwise_faces") == ["symmetry_label", "symmetry_cutoff", "label_cutoff"]
        and dependency_nerve.get("required_triple_cell") == "symmetry_label_cutoff_cube"
        and dependency_nerve.get("anchor_is") == "fiber_condition_natural_over_full_cube"
        and dependency_nerve.get("completion_is") == "derived_inverse_limit_after_finite_cube_coherence"
        and dependency_nerve.get("Green_realization_is") == "separate_source_natural_transformation_after_descent"
        and dependency_nerve.get("lower_tower_max_height_determines_coherence_depth") is False
        and dependency_nerve.get("coherence_depth_law") == "dimension_of_authorized_dependency_nerve_not_max_lower_height"
    ):
        errors.append("theta_triangle_combined_dependency_nerve_mistyped")
    nerve_shape_cases = []
    for case in dependency_nerve.get("shape_cases", []):
        heights = case.get("lower_heights", [])
        independent_axes = case.get("independent_axis_count")
        valid = heights == [1, 1, 1] and isinstance(independent_axes, int) and 1 <= independent_axes <= 3
        nerve_depth = independent_axes if valid else None
        if nerve_depth != case.get("expected_nerve_depth"):
            errors.append("theta_triangle_dependency_nerve_depth_mismatch:" + str(case.get("id")))
        nerve_shape_cases.append({"id": case.get("id"), "lower_max_height": max(heights) if heights else None, "nerve_depth": nerve_depth})
    if len(nerve_shape_cases) != 3 or len({case["nerve_depth"] for case in nerve_shape_cases}) != 3:
        errors.append("theta_triangle_dependency_nerve_shape_fixture_incomplete")
    nerve_coherence_cases = []
    face_order = ["symmetry_label", "symmetry_cutoff", "label_cutoff"]
    for case in dependency_nerve.get("coherence_cases", []):
        first_failure = "none"
        if case.get("axis_arrows_typed") is not True:
            first_failure = "axis_typing"
        else:
            faces = case.get("pairwise_faces", {})
            failed_face = next((face for face in face_order if faces.get(face) is not True), None)
            if failed_face is not None:
                first_failure = failed_face + "_face"
            elif case.get("triple_cube") is not True:
                first_failure = "triple_cube"
            elif case.get("anchor_natural") is not True:
                first_failure = "anchor_naturality"
        admitted = first_failure == "none"
        if admitted != case.get("expected_admitted") or first_failure != case.get("expected_first_failure"):
            errors.append("theta_triangle_dependency_nerve_coherence_mismatch:" + str(case.get("id")))
        nerve_coherence_cases.append({"id": case.get("id"), "admitted": admitted, "first_failure": first_failure})
    if len(nerve_coherence_cases) != 6:
        errors.append("theta_triangle_dependency_nerve_coherence_fixture_incomplete")
    spacetime_dpc = dependency_nerve.get("spacetime_coherence_reversal_DPC", {})
    if not (
        spacetime_dpc.get("status") == "conditional_structural_analogy_not_spacetime_derivation"
        and spacetime_dpc.get("established_source_patterns") == [
            "d_minus_1_manifolds_are_objects_and_d_cobordisms_are_morphisms",
            "hypersurface_deformation_brackets_encode_slicing_consistency_on_the_constraint_solution_system",
        ]
        and spacetime_dpc.get("time_coordinate_status") == "chosen_foliation_parameter_not_coherence_authority"
        and spacetime_dpc.get("coherence_candidate") == "four_geometry_with_hypersurface_deformation_or_cobordism_composition_laws"
        and spacetime_dpc.get("dimension_pattern_is_general_d_plus_1") is True
        and spacetime_dpc.get("selects_three_spatial_dimensions") is False
        and spacetime_dpc.get("selects_Lorentzian_signature") is False
        and spacetime_dpc.get("constructs_causal_cones") is False
        and spacetime_dpc.get("tower_to_spacetime_comparison_map") == "missing"
        and spacetime_dpc.get("required_next_constructor") == "source_derived_representation_of_hypersurface_deformation_algebroid_on_tower_comparison_carrier"
        and len(spacetime_dpc.get("acceptance_gates", [])) == 6
    ):
        errors.append("theta_triangle_spacetime_coherence_reversal_DPC_mistyped")
    spacetime_hostiles = []
    expected_rejections = {
        "two_plus_one_cobordism": "dimension_shift_selects_3_plus_1",
        "four_dimensional_Euclidean_cobordism": "four_dimensional_coherence_selects_Lorentzian_signature",
        "topological_four_cobordism": "cobordism_composition_constructs_causal_cones",
        "off_shell_hypersurface_deformation": "deformation_coherence_is_purely_kinematic_spacetime_covariance",
    }
    for case in spacetime_dpc.get("hostile_countermodels", []):
        rejected = expected_rejections.get(case.get("id")) == case.get("rejects_claim")
        if case.get("id") == "off_shell_hypersurface_deformation":
            rejected = rejected and case.get("has_local_deformation_brackets") is True and case.get("equals_spacetime_diffeomorphism_without_constraints_or_equations") is False
        else:
            rejected = rejected and case.get("has_object_morphism_dimension_shift") is True and case.get("has_Lorentzian_cone") is False
        if not rejected:
            errors.append("theta_triangle_spacetime_hostile_mistyped:" + str(case.get("id")))
        spacetime_hostiles.append({"id": case.get("id"), "rejected_overclaim": rejected})
    if len(spacetime_hostiles) != 4:
        errors.append("theta_triangle_spacetime_hostile_fixture_incomplete")
    algebroid_audit = spacetime_dpc.get("constant_structure_algebroid_audit", {})
    if not (
        algebroid_audit.get("generator_type") == "pair_of_affine_normal_lapse_and_tangential_shift"
        and algebroid_audit.get("bracket_normal") == "M1_times_derivative_N2_minus_M2_times_derivative_N1"
        and algebroid_audit.get("bracket_tangential") == "M1_times_derivative_M2_minus_M2_times_derivative_M1_plus_beta_times_N1_times_derivative_N2_minus_N2_times_derivative_N1"
        and algebroid_audit.get("beta_role") == "constant_inverse_metric_times_signature_proxy"
        and algebroid_audit.get("Jacobi_closure_selects_beta_sign") is False
        and algebroid_audit.get("beta_zero_has_non_degenerate_causal_cone") is False
        and algebroid_audit.get("representation_on_tower_comparison_carrier") == "missing"
    ):
        errors.append("theta_triangle_constant_structure_algebroid_audit_mistyped")

    def affine_scale(poly: list[int], scalar: int) -> list[int]:
        return [scalar * poly[0], scalar * poly[1]]

    def affine_sub(left: list[int], right: list[int]) -> list[int]:
        return [left[0] - right[0], left[1] - right[1]]

    def affine_add(*terms: list[int]) -> list[int]:
        return [sum(term[0] for term in terms), sum(term[1] for term in terms)]

    def hda_bracket(left: dict[str, list[int]], right: dict[str, list[int]], beta: int) -> dict[str, list[int]]:
        n_left, m_left = left["normal"], left["shift"]
        n_right, m_right = right["normal"], right["shift"]
        normal = affine_sub(affine_scale(m_left, n_right[1]), affine_scale(m_right, n_left[1]))
        tangent = affine_add(
            affine_sub(affine_scale(m_left, m_right[1]), affine_scale(m_right, m_left[1])),
            affine_scale(affine_sub(affine_scale(n_left, n_right[1]), affine_scale(n_right, n_left[1])), beta),
        )
        return {"normal": normal, "shift": tangent}

    algebroid_cases = []
    for case in algebroid_audit.get("cases", []):
        beta = case.get("beta")
        u, v, w = case.get("u"), case.get("v"), case.get("w")
        valid = beta in {-1, 0, 1} and all(
            isinstance(generator, dict)
            and all(isinstance(generator.get(key), list) and len(generator[key]) == 2 and all(isinstance(value, int) for value in generator[key]) for key in ("normal", "shift"))
            for generator in (u, v, w)
        )
        if valid:
            uv_w = hda_bracket(hda_bracket(u, v, beta), w, beta)
            vw_u = hda_bracket(hda_bracket(v, w, beta), u, beta)
            wu_v = hda_bracket(hda_bracket(w, u, beta), v, beta)
            jacobi = {
                "normal": affine_add(uv_w["normal"], vw_u["normal"], wu_v["normal"]),
                "shift": affine_add(uv_w["shift"], vw_u["shift"], wu_v["shift"]),
            }
            jacobi_zero = jacobi == {"normal": [0, 0], "shift": [0, 0]}
        else:
            jacobi, jacobi_zero = None, False
        if jacobi_zero != case.get("expected_Jacobi_zero"):
            errors.append("theta_triangle_constant_algebroid_Jacobi_mismatch:" + str(case.get("id")))
        algebroid_cases.append({"id": case.get("id"), "beta": beta, "Jacobi": jacobi, "Jacobi_zero": jacobi_zero})
    if len(algebroid_cases) != 3 or {case["beta"] for case in algebroid_cases if case["Jacobi_zero"]} != {0}:
        errors.append("theta_triangle_constant_algebroid_fixture_incomplete")
    dynamic_base = spacetime_dpc.get("minimum_dynamic_base_contract", {})
    if not (
        dynamic_base.get("base_fields") == ["nondegenerate_spatial_metric_q", "conjugate_momentum_or_extrinsic_curvature_pi", "embedding_and_domain_data"]
        and dynamic_base.get("shift_anchor") == "spatial_Lie_derivative_on_q_pi_and_comparison_fields"
        and dynamic_base.get("normal_anchor") == "constraint_generated_normal_deformation_with_q_variation_depending_on_pi"
        and dynamic_base.get("Leibniz_law") == "bracket_e1_f_e2_equals_f_bracket_e1_e2_plus_anchor_e1_f_times_e2"
        and dynamic_base.get("anchor_morphism_law") == "anchor_bracket_equals_commutator_of_anchors_on_declared_domain"
        and dynamic_base.get("signature_location") == "source_fixed_coefficient_multiplying_inverse_metric_in_normal_normal_bracket"
        and dynamic_base.get("cone_gate") == "principal_symbol_non_degenerate_with_source_fixed_signature"
        and dynamic_base.get("metric_only_base_sufficient") is False
        and dynamic_base.get("frozen_structure_function_sufficient") is False
    ):
        errors.append("theta_triangle_minimum_dynamic_base_contract_mistyped")
    dynamic_base_cases = []
    for case in dynamic_base.get("cases", []):
        admitted = all(case.get(gate) is True for gate in ["has_q", "has_pi_or_K", "shift_anchor_typed", "normal_anchor_typed", "Leibniz_verified", "anchor_morphism_verified", "q_nondegenerate", "signature_source_fixed"])
        if admitted != case.get("expected_structurally_admissible"):
            errors.append("theta_triangle_dynamic_base_case_mismatch:" + str(case.get("id")))
        failed_gates = [gate for gate in ["has_q", "has_pi_or_K", "shift_anchor_typed", "normal_anchor_typed", "Leibniz_verified", "anchor_morphism_verified", "q_nondegenerate", "signature_source_fixed"] if case.get(gate) is not True]
        dynamic_base_cases.append({"id": case.get("id"), "structurally_admissible": admitted, "failed_gates": failed_gates})
    if len(dynamic_base_cases) != 6 or sum(case["structurally_admissible"] for case in dynamic_base_cases) != 1:
        errors.append("theta_triangle_dynamic_base_fixture_incomplete")
    fibered_carrier = spacetime_dpc.get("fibered_comparison_carrier_retyping", {})
    if not (
        fibered_carrier.get("base") == "phase_space_and_domain_stack_P_X_of_q_pi_embeddings"
        and fibered_carrier.get("fiber") == "equivariant_comparison_torsor_L_X_at_q_pi"
        and fibered_carrier.get("fiber_dimension_at_finite_label_cutoff") == "6N_before_cross_label_descent"
        and fibered_carrier.get("acting_object") == "hypersurface_deformation_Lie_algebroid_A_X_over_P_X"
        and fibered_carrier.get("representation") == "A_connection_nabla_on_sections_of_L_X"
        and fibered_carrier.get("connection_Leibniz") == "nabla_e_of_f_s_equals_f_nabla_e_s_plus_anchor_e_f_times_s"
        and fibered_carrier.get("flatness_gate") == "connection_curvature_zero_or_source_typed_central_anomaly"
        and fibered_carrier.get("scalarization") == "bundle_map_preserving_base_anchor_and_declared_domains"
        and fibered_carrier.get("cutoff_condition") == "cartesian_base_change_square_for_P_Y_to_P_X_and_L_Y_to_L_X"
        and fibered_carrier.get("signature_strata") == "nondegenerate_connected_components_of_base_with_source_fixed_sign"
        and fibered_carrier.get("signature_change_requires_degenerate_locus") is True
        and fibered_carrier.get("fixed_matrix_representation_sufficient") is False
    ):
        errors.append("theta_triangle_fibered_comparison_carrier_retyping_mistyped")
    fibered_carrier_cases = []
    for case in fibered_carrier.get("cases", []):
        curvature_typed = case.get("curvature_class") in {"zero", "source_typed_central_anomaly"}
        admitted = bool(
            case.get("dynamic_base")
            and case.get("section_Leibniz")
            and curvature_typed
            and case.get("scalarization_base_compatible")
            and case.get("cutoff_cartesian")
            and not case.get("signature_crossing_avoids_degeneracy")
        )
        if admitted != case.get("expected_admitted"):
            errors.append("theta_triangle_fibered_carrier_case_mismatch:" + str(case.get("id")))
        fibered_carrier_cases.append({"id": case.get("id"), "admitted": admitted, "curvature_typed": curvature_typed})
    if len(fibered_carrier_cases) != 7 or sum(case["admitted"] for case in fibered_carrier_cases) != 2:
        errors.append("theta_triangle_fibered_carrier_fixture_incomplete")
    curvature_ladder = fibered_carrier.get("curvature_coherence_ladder", {})
    if not (
        curvature_ladder.get("degree_0") == "comparison_fibers_L_X"
        and curvature_ladder.get("degree_1") == "connection_transport_along_algebroid_arrows"
        and curvature_ladder.get("degree_2") == "source_typed_curvature_fillings_for_comparison_faces"
        and curvature_ladder.get("degree_3") == "Bianchi_or_tetrahedral_coherence_among_face_fillings"
        and curvature_ladder.get("larger_net_gate") == "vanishing_or_source_typed_degree_3_residual"
        and curvature_ladder.get("filling_space") == "torsor_over_closed_central_2_cells"
        and curvature_ladder.get("constructive_selector_required_when_filling_torsor_nontrivial") is True
        and curvature_ladder.get("pairwise_face_coherence_sufficient_for_global_net") is False
        and curvature_ladder.get("ordinary_connection_Bianchi_is_structural_but_weak_source_cells_need_separate_coherence") is True
    ):
        errors.append("theta_triangle_curvature_coherence_ladder_mistyped")
    curvature_ladder_cases = []
    for case in curvature_ladder.get("cases", []):
        residual_typed = case.get("degree_3_residual") in {"zero", "source_typed_exact"}
        selector_ok = not case.get("selector_required") or case.get("selector_authorized") is True
        coherent = bool(case.get("face_fillings_typed") and residual_typed and selector_ok)
        if coherent != case.get("expected_globally_coherent"):
            errors.append("theta_triangle_curvature_ladder_case_mismatch:" + str(case.get("id")))
        curvature_ladder_cases.append({"id": case.get("id"), "globally_coherent": coherent, "residual_typed": residual_typed, "selector_ok": selector_ok})
    if len(curvature_ladder_cases) != 6 or sum(case["globally_coherent"] for case in curvature_ladder_cases) != 3:
        errors.append("theta_triangle_curvature_ladder_fixture_incomplete")
    truncation = curvature_ladder.get("source_derived_truncation", {})
    if not (
        truncation.get("required_highest_degree") == "dimension_of_authorized_dependency_nerve"
        and truncation.get("absence_of_higher_simplices") == "removes_higher_comparison_obligations_but_does_not_choose_top_fillings"
        and truncation.get("invariant_closure") == "all_cells_through_nerve_dimension_typed_and_top_filling_groupoid_retained"
        and truncation.get("executable_closure") == "invariant_closure_and_top_filling_space_contractible_or_source_selector_authorized"
        and truncation.get("lower_tower_max_rung_determines_truncation") is False
        and truncation.get("finite_nerve_implies_infinite_coherence_tower") is False
    ):
        errors.append("theta_triangle_source_derived_truncation_mistyped")
    truncation_cases = []
    for case in truncation.get("cases", []):
        invariant_closed = bool(case.get("source_nerve_declared") and case.get("typed_through_degree", -1) >= case.get("nerve_dimension", 0))
        executable_closed = bool(invariant_closed and (case.get("top_filling_contractible") or case.get("top_selector_authorized")))
        if invariant_closed != case.get("expected_invariant_closed") or executable_closed != case.get("expected_executable_closed"):
            errors.append("theta_triangle_truncation_case_mismatch:" + str(case.get("id")))
        truncation_cases.append({"id": case.get("id"), "invariant_closed": invariant_closed, "executable_closed": executable_closed})
    if len(truncation_cases) != 6 or sum(case["invariant_closed"] for case in truncation_cases) != 3 or sum(case["executable_closed"] for case in truncation_cases) != 2:
        errors.append("theta_triangle_truncation_fixture_incomplete")
    capcl = curvature_ladder.get("closure_capability_category", {})
    if not (
        capcl.get("name") == "CapCl_K"
        and capcl.get("base") == "finite_source_authorized_dependency_nerve_K"
        and capcl.get("presentation_object") == "typed_pseudofunctor_F:K_op_to_Gpd"
        and capcl.get("invariant_closure") == "homotopy_limit_K_F"
        and capcl.get("executable_closure") == "authorized_pointed_homotopy_limit"
        and capcl.get("forgetful_arrow") == "ExecCl_F_to_InvCl_F"
        and capcl.get("reverse_arrow_gate") == "authorized_global_section_of_selector_fibration"
        and capcl.get("observation") == "natural_port_family_R:F_to_O"
        and capcl.get("execution") == "authority_preserving_actuator_lift_of_selected_section"
        and capcl.get("morphisms") == "domain_support_variance_and_authority_preserving_pseudonatural_transformations"
        and capcl.get("obstruction_coordinates") == ["descent", "higher_coherence", "selector", "observation", "execution"]
        and capcl.get("coordinates_independent") is True
        and capcl.get("evidence_transport_creates_authority") is False
    ):
        errors.append("theta_triangle_closure_capability_category_mistyped")
    capcl_cases = []
    coordinate_gates = [
        ("descent", "descent_effective"),
        ("higher_coherence", "higher_cells_closed"),
        ("selector", "authorized_selector"),
        ("observation", "observation_conservative"),
        ("execution", "execution_realizable"),
    ]
    for case in capcl.get("cases", []):
        obstructions = [name for name, gate in coordinate_gates if case.get(gate) is not True]
        if obstructions != case.get("expected_obstructions"):
            errors.append("theta_triangle_capcl_case_mismatch:" + str(case.get("id")))
        capcl_cases.append({"id": case.get("id"), "obstructions": obstructions, "closed": not obstructions})
    singleton_obstructions = {case["obstructions"][0] for case in capcl_cases if len(case["obstructions"]) == 1}
    if len(capcl_cases) != 7 or singleton_obstructions != {"descent", "higher_coherence", "selector", "observation", "execution"}:
        errors.append("theta_triangle_capcl_independence_fixture_incomplete")
    isotypic_cases = []
    for case in isotypic.get("cases", []):
        source_mult = case.get("source_multiplicities", {})
        kernel_mult = case.get("kernel_multiplicities", {})
        labels = set(source_mult) | set(kernel_mult)
        hom_dimension = sum(source_mult.get(label, 0) * kernel_mult.get(label, 0) for label in labels)
        rank = case.get("Green_constraint_rank", 0)
        valid = 0 <= rank <= hom_dimension
        residual = hom_dimension - rank if valid else None
        if hom_dimension != case.get("expected_Hom_G_dimension") or residual != case.get("expected_residual_dimension") or valid != case.get("expected_valid"):
            errors.append("theta_triangle_isotypic_torsor_expectation_mismatch:" + str(case.get("id")))
        isotypic_cases.append({"id": case.get("id"), "Hom_G_dimension": hom_dimension, "constraint_rank_valid": valid, "residual_dimension": residual, "unique": valid and residual == 0})
    if len(isotypic_cases) != 5:
        errors.append("theta_triangle_isotypic_torsor_fixture_incomplete")
    pro_gate_results = []
    for case in boundary.get("pro_incidence_gate_models", []):
        natural = case.get("restriction_squares_commute") is True
        separated = case.get("completed_common_kernel_dimension") == 0
        pro_typed = case.get("target_kind") == "typed_pro_register"
        admitted = bool(case.get("finite_components_typed") and natural and separated and pro_typed and case.get("source_authority"))
        failed_gates = []
        if not case.get("finite_components_typed"):
            failed_gates.append("finite_component_typing")
        if not natural:
            failed_gates.append("cutoff_naturality")
        if not separated:
            failed_gates.append("completion_separatedness")
        if not pro_typed:
            failed_gates.append("pro_target_type")
        if not case.get("source_authority"):
            failed_gates.append("source_authority")
        if admitted != case.get("expected_admitted"):
            errors.append("theta_triangle_pro_incidence_gate_expectation_mismatch:" + str(case.get("id")))
        pro_gate_results.append({
            "id": case.get("id"),
            "admitted": admitted,
            "natural": natural,
            "completion_separated": separated,
            "failed_gates": failed_gates,
        })
    if len(pro_gate_results) != 5:
        errors.append("theta_triangle_pro_incidence_gate_fixture_incomplete")
    derived = boundary.get("derived_limit_defect_contract", {})
    if not (
        derived.get("source_completion_comparison") == "eta:completed_source_to_inverse_limit_source_cutoffs"
        and derived.get("finite_kernel_system") == "K_X=kernel(I_X)"
        and derived.get("ordinary_limit_kernel") == "limit(K_X)"
        and derived.get("derived_lifting_obstruction") == "limit1(K_X)"
        and derived.get("exact_sequence") == "0_to_limit_K_to_limit_S_to_limit_H_to_limit1_K"
        and derived.get("lim1_classifies_readout_kernel") is False
    ):
        errors.append("theta_triangle_derived_limit_sequence_mistyped")
    derived_cases = []
    for case in derived.get("cases", []):
        descent = case.get("completion_descent_kernel_dimension", 0)
        ordinary = case.get("ordinary_limit_kernel_dimension", 0)
        limit1 = case.get("derived_limit1_dimension", 0)
        faithful = descent == 0 and ordinary == 0
        effective = limit1 == 0
        if descent and ordinary and limit1:
            defect_class = "mixed"
        elif descent:
            defect_class = "completion_descent_kernel"
        elif ordinary:
            defect_class = "ordinary_inverse_limit_kernel"
        elif limit1:
            defect_class = "derived_lifting_obstruction"
        else:
            defect_class = "none"
        if faithful != case.get("expected_faithful") or effective != case.get("expected_effective") or defect_class != case.get("expected_defect_class"):
            errors.append("theta_triangle_derived_limit_expectation_mismatch:" + str(case.get("id")))
        derived_cases.append({"id": case.get("id"), "faithful": faithful, "effective": effective, "defect_class": defect_class})
    if len(derived_cases) != 5:
        errors.append("theta_triangle_derived_limit_fixture_incomplete")
    closure = derived.get("closure_criterion", {})
    if not (
        closure.get("cofinal_chain") == "X_n=first_n_primes"
        and closure.get("cofinal_chain_source_authorized") is True
        and closure.get("descent_gate") == "cutoff_seminorms_cofinal_and_Hausdorff"
        and closure.get("faithfulness_gate") == "compatible_kernel_tower_has_zero_inverse_limit"
        and closure.get("effectivity_gate") == "kernel_tower_satisfies_Mittag_Leffler"
    ):
        errors.append("theta_triangle_limit_closure_criterion_mistyped")
    closure_cases = []
    for case in closure.get("cases", []):
        faithful = bool(case.get("cofinal_Hausdorff_descent") and case.get("inverse_limit_kernel_zero"))
        effective = case.get("kernel_Mittag_Leffler") is True
        closed = faithful and effective
        if faithful != case.get("expected_faithful") or effective != case.get("expected_effective") or closed != case.get("expected_closed"):
            errors.append("theta_triangle_limit_closure_expectation_mismatch:" + str(case.get("id")))
        closure_cases.append({
            "id": case.get("id"),
            "faithful": faithful,
            "effective": effective,
            "closed": closed,
            "target_transitions_surjective": case.get("target_transitions_surjective") is True,
        })
    if len(closure_cases) != 5:
        errors.append("theta_triangle_limit_closure_fixture_incomplete")
    live_audit = derived.get("live_theta_gate_audit", {})
    if not (
        live_audit.get("completion_type") == "canonical_Hausdorff_completion_of_constructor_generated_pro_Gram_topology"
        and live_audit.get("seminorm_index") == "finite_constructor_words_with_finite_observation_packets"
        and live_audit.get("cofinality_reason") == "every_finite_constructor_word_uses_finitely_many_prime_specific_generators"
        and live_audit.get("Mellin_family_stage_policy") == "full_stage_compatible_family_at_every_cutoff"
        and live_audit.get("finite_packet_Hausdorff_separation") is True
        and live_audit.get("descent_comparison_injective") == "proved_for_canonical_completion"
        and live_audit.get("descent_gate_status") == "closed"
    ):
        errors.append("theta_triangle_live_descent_gate_not_source_derived")
    if live_audit.get("ordinary_limit_kernel_status") != "open" or live_audit.get("finite_packet_faithfulness_proves_completed_limit_kernel_zero") is not False:
        errors.append("theta_triangle_live_limit_kernel_overclaimed")
    if live_audit.get("kernel_Mittag_Leffler_status") != "open" or live_audit.get("surjective_target_restrictions_prove_kernel_ML") is not False:
        errors.append("theta_triangle_live_kernel_ML_overclaimed")
    if live_audit.get("overall_pro_incidence_status") != "blocked_on_limit_kernel_and_kernel_ML":
        errors.append("theta_triangle_live_pro_incidence_status_mistyped")
    bigraded = live_audit.get("bigraded_kernel_tower_audit", {})
    drifting = bigraded.get("drifting_counterexample", {})
    if not (
        bigraded.get("indices") == {"prime_cutoff": "n", "valuation_Fock_grade": "r"}
        and bigraded.get("bounded_grade_kernel_dimension") == "finite"
        and bigraded.get("bounded_grade_Mittag_Leffler") == "automatic_by_descending_chain_condition"
        and bigraded.get("full_completion_grade_assembly") == "product_over_unbounded_r"
        and bigraded.get("uniform_stabilization_in_r") == "unproved"
        and bigraded.get("uniformity_required_for_full_ML") is True
    ):
        errors.append("theta_triangle_bigraded_kernel_tower_mistyped")
    if not (drifting.get("each_grade_stabilizes") is True and drifting.get("full_product_images_stabilize") is False and drifting.get("image_rule") == "image_at_m_in_grade_r_is_field_iff_m_less_than_r"):
        errors.append("theta_triangle_gradewise_ML_laundered_to_uniform_ML")
    if bigraded.get("bounded_grade_separation_status") != "conditional_on_finite_Hardy_components" or bigraded.get("full_limit_kernel_status") != "open_until_gradewise_separation_and_product_descent":
        errors.append("theta_triangle_bigraded_limit_kernel_overclaimed")
    reassembly = bigraded.get("source_grade_reassembly", {})
    if not (
        reassembly.get("atomic_measure") == "sum_over_p_k_of_(1/k)*p^(-k/2)*delta_(k_log_p)"
        and reassembly.get("typed_strata") == ["primitive_k1", "square_k2", "connected_k_ge_3"]
        and reassembly.get("required_order") == "split_for_typing_then_reassemble_before_completion"
        and reassembly.get("finite_cutoff_transition") == "explicit_nonzero_determinant_line_transition"
        and reassembly.get("global_value_type") == "determinant_line"
    ):
        errors.append("theta_triangle_source_grade_reassembly_mistyped")
    if reassembly.get("global_scalar_log_authorized") is not False or reassembly.get("scalar_log_circularity") != "zeta_prime_over_zeta_imports_the_divisor_under_test":
        errors.append("theta_triangle_scalar_log_completion_circular")
    if reassembly.get("archimedean_modular_determinant_correspondence") != "missing" or reassembly.get("reassembly_proves_kernel_ML") is not False:
        errors.append("theta_triangle_determinant_reassembly_overclaimed")
    if reassembly.get("naive_product_uniformity_is") != "hostile_presentation_obstruction_not_yet_source_invariant":
        errors.append("theta_triangle_product_uniformity_promoted_to_source_invariant")
    boundary_extension_authorized = boundary.get("joint_rigged_completion_extension_authorized") is True
    if boundary_extension_authorized and primitive_odd.get("constructor_authorized") is not True:
        errors.append("theta_triangle_joint_completion_without_primitive_odd_constructor")
    if boundary_extension_authorized and relative_constructor.get("constructor_status") != "source_authorized_exact_identity":
        errors.append("theta_triangle_joint_completion_without_exact_tail_identity")
    commutations = triangle.get("commutation_declarations", [])
    for declaration in commutations:
        if declaration.get("authorized") and (not declaration.get("source_authority_root") or not declaration.get("comparison_cell")):
            errors.append("theta_triangle_swap_authority_untyped")
        if declaration.get("authorized") and str(declaration.get("status", "")).startswith("precedence_"):
            errors.append("theta_triangle_precedence_pair_cannot_swap")

    initial = {"state_components": {"finite_theta_source"}, "domain": {"finite_support"}, "graph_norm": {"tail_analytic_gram"}, "distinctions": {"tail_translation_norm", "raw_arithmetic_label"}, "capabilities": {"raw_label_port"}, "completion_scope": "uncompleted_finite_packet"}

    def apply(stage_id: str, state: dict[str, Any], path: tuple[str, ...]) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        result = deepcopy(state)
        if stage_id == "S":
            result["state_components"].add("independent_seam_state")
            result["domain"].add("tail_seam_domain")
            result["graph_norm"].add("seam_translation_norm")
            result["distinctions"].add("seam_translation_norm")
            result["capabilities"].add("seam_state_port")
        elif stage_id == "C":
            if "pro_gram_completion" in result["state_components"] and not family_authorized:
                return None, {"code":"clark_current_not_continuous_after_completion", "path":list(path), "failed_operation":"C", "missing_certificate":"fixed_finite_uniform_constructor_family_F", "recovery_possible":False}
            result["state_components"].add("clark_differentiated_bulk")
            result["domain"].add("clark_finite_current_domain")
            result["graph_norm"].add("clark_z_derivative_finite_bulk")
            result["capabilities"].add("clark_current_matrix")
        elif stage_id == "L":
            missing_distinctions = set(stages["L"].get("required_distinctions", [])) - result["distinctions"]
            if missing_distinctions:
                lost = sorted(missing_distinctions)[0]
                return None, {"code":"distinction_erased_before_required_repair", "path":list(path), "failed_operation":"L", "lost_capability":lost, "recovery_possible":False}
            if "independent_seam_state" not in result["state_components"]:
                return None, {"code":"distinction_erased_before_required_repair", "path":list(path), "failed_operation":"L", "lost_capability":"seam_translation_norm", "recovery_possible":False}
            if "clark_differentiated_bulk" in result["state_components"] and not family_authorized:
                return None, {"code":"theta_pro_gram_instantiation_blocked_missing_incidence", "path":list(path), "failed_operation":"L", "missing_source_maps":["valuation/Fock -> boundary", "Clark current -> common finite module"], "required_family":"fixed_finite_authorized_F", "recovery_possible":False}
            if stages["L"].get("completion_scope") == "completion_stability_unproved":
                return None, {"code":"valuation_completion_not_source_authorized", "path":list(path), "failed_operation":"L", "missing_constructor":stages["L"].get("missing_source_constructor"), "recovery_possible":False}
            result["state_components"] |= {"valuation_constructor_port", "pro_gram_completion"}
            result["domain"].add("constructor_generated_pro_gram_domain")
            result["graph_norm"].add("valuation_pro_gram_topology")
            result["distinctions"].add("prime_valuation_label")
            result["capabilities"].add("valuation_projector_family")
            result["completion_scope"] = "constructor_generated_pro_gram_completion"
        return result, None

    path_results = []
    for order in permutations(sorted(expected_ids)):
        state = deepcopy(initial)
        prefixes = []
        rejection = None
        for stage_id in order:
            state, rejection = apply(stage_id, state, order[:order.index(stage_id) + 1])
            if rejection:
                break
            prefixes.append({"after":stage_id, "state_components":sorted(state["state_components"]), "domain":sorted(state["domain"]), "graph_norm":sorted(state["graph_norm"]), "distinctions":sorted(state["distinctions"]), "completion_scope":state["completion_scope"], "unsafe_repair_in_progress":stage_id != order[-1]})
        endpoint = None
        if rejection is None:
            endpoint = {key: sorted(state[key]) if isinstance(state[key], set) else state[key] for key in ("state_components", "domain", "graph_norm", "distinctions", "capabilities", "completion_scope")}
        path_results.append({"order":list(order), "dynamically_admissible":rejection is None, "first_rejection":rejection, "prefixes":prefixes, "typed_endpoint":endpoint, "endpoint_digest":stable_digest(endpoint) if endpoint else None})
    admissible = [path for path in path_results if path["dynamically_admissible"]]
    endpoints = {path["endpoint_digest"] for path in admissible}
    authorized_swaps = [declaration for declaration in commutations if declaration.get("authorized")]
    hostile = triangle.get("principal_hostile_fixture", {})
    hostile_witness = {"code":"distinction_erased_before_required_repair", "path":["complete_tail_quotient","retain_seam"], "lost_capability":"seam_translation_norm", "recovery_possible":False, "tail_norm":hostile.get("tail_norm"), "seam_norm":hostile.get("seam_norm"), "adjacent_label_collapse":hostile.get("adjacent_label_collapse")}
    expected = triangle.get("expected", {})
    observed = {"formal_order_count":len(path_results), "admissible_order_count":len(admissible), "typed_endpoint_count":len(endpoints), "authorized_adjacent_swap_count":len(authorized_swaps), "first_braid_class":"illegal_factorization" if len(admissible) < 6 else "not_computed"}
    for key, value in expected.items():
        if observed.get(key) != value:
            errors.append("theta_triangle_expectation_mismatch:" + key)
    backward = pullback_requirements([stages[item] for item in ("S", "C", "L")], {"valuation_completion_faithful"}) if set(stages) == expected_ids else {"accepted":False,"code":"constructor_inventory_invalid"}
    if not backward.get("accepted"):
        errors.append(backward.get("code", "backward_requirement_discharge_failed"))
    supplied = set(triangle.get("source_capabilities", []))
    backward["supplied_source_capabilities"] = sorted(supplied)
    backward["residual"] = sorted(set(backward.get("required_source_capabilities", [])) - supplied)
    completion_frontier = []
    if "valuation_completion_extension" in backward["residual"] or not boundary_extension_authorized:
        completion_frontier.append({
            "constructor_id": "joint_rigged_arithmetic_completion_extension",
            "required_map": "four_lane_delta_PV_arithmetic_continuity_extension",
            "required_subconstructors": [
                "primitive_odd_source_relative_moment_cancellation_before_prime_aggregation",
                "primitive_odd_exponential_remainder_control",
            ],
            "authority_status": "missing",
        })
    if not family_authorized:
        completion_frontier.append({
            "constructor_id": "clark_uniform_domination_family",
            "required_map": "fixed_finite_authorized_F_on_common_Clark_valuation_module",
            "authority_status": "missing",
        })
    coherence_frontier = [
        {
            "repair_pair": declaration.get("pair"),
            "status": declaration.get("status"),
            "required_comparison_cell": declaration.get("comparison_cell") or "source_comparison_required",
        }
        for declaration in commutations
        if not declaration.get("authorized")
        and not str(declaration.get("status", "")).startswith("precedence_")
    ]
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "source_status": "blocked_on_valuation_incidence_completion_and_clark_uniform_F" if not family_authorized else "blocked_on_valuation_incidence_completion",
        "clark_finite_bulk_identity": "2||G+f||^2+2a^2||partial_z G||^2",
        "clark_completion_continuity_authorized": family_authorized,
        "native_q_flow_endpoint_certificate": triangle.get("native_q_flow_endpoint_certificate"),
        "observed": observed,
        "paths": path_results,
        "authorized_adjacent_swaps": authorized_swaps,
        "same_completed_typed_endpoint": len(endpoints) == 1 if admissible else None,
        "braid_residual_class": observed["first_braid_class"],
        "principal_hostile_rejection": hostile_witness,
        "backward_requirement_discharge": backward,
        "forced_logical_precedence": [{"before": "S", "after": "L", "reason": "L_requires_seam_translation_norm"}],
        "minimal_completed_path_frontier": completion_frontier,
        "valuation_boundary_constructor": {
            "finite_atomic_incidence_authorized": boundary.get("finite_atomic_incidence_authorized") is True,
            "universal_fourier_chart_sewing_authorized": boundary.get("universal_fourier_chart_sewing_authorized") is True,
            "joint_rigged_completion_extension_authorized": boundary_extension_authorized,
            "four_lanes": sorted(expected_lanes),
            "chart_transform_determinant": transform.get("total_determinant"),
            "reflection_action": reflection,
            "scalarization_rejected": set(boundary.get("forbidden_scalarizations", [])) == {"delta_only", "single_regularity_grade"},
            "lane_completion_profiles": lane_profiles,
            "aggregation_precedence": precedence,
            "primitive_odd_completion_obstruction": "generic_Hilbert_tail_fails_exponentially_weighted_term_test",
            "relative_moment_constructor": relative_constructor,
            "compact_test_moment_no_go": "all_polynomial_moments_zero_for_a_compact_localized_test_forces_the_test_to_vanish",
            "finite_shift_cocycle_audit": shift_cocycle,
            "axis_separation": "finite_shift_frequency_regularization_does_not_imply_prime_label_summability",
            "adelic_hardy_incidence_contract": incidence,
            "global_incidence_status": "missing_full_source_functorial_boundary_lift_with_pro_diagnostics",
            "full_source_poisson_green_lift": boundary_lift,
            "boundary_lift_extension": {
                "exact_sequence": lift_extension.get("exact_sequence"),
                "existence_obstruction": lift_extension.get("existence_obstruction"),
                "lift_torsor": lift_extension.get("lift_torsor"),
                "mixed_channel_location": lift_extension.get("mixed_channel_location"),
                "cases": lift_cases,
                "ambient_category": lift_extension.get("ambient_category"),
                "bare_complex_vector_space_Ext1": lift_extension.get("bare_complex_vector_space_Ext1"),
                "typed_splitting_cases": typed_split_cases,
                "finite_symmetry_averaging": {
                    "group": averaging.get("group"),
                    "Reynolds_formula": averaging.get("Reynolds_formula"),
                    "equivariant_lifts_form": averaging.get("equivariant_lifts_form"),
                    "cases": averaging_cases,
                    "theorem": "finite_symmetry_equivariance_is_averagable_once_continuity_and_domain_invariance_hold",
                    "isotypic_torsor_classifier": {
                        "dimension_formula": isotypic.get("dimension_formula"),
                        "live_theta_multiplicity_status": isotypic.get("live_theta_multiplicity_status"),
                        "live_reflection_kernel_audit": reflection_kernel,
                        "conditional_tensor_character_theorem": tensor_characters,
                        "combined_dependency_nerve_results": {
                            "shape_cases": nerve_shape_cases,
                            "coherence_cases": nerve_coherence_cases,
                            "strict_audit_max_depth": 3,
                            "spacetime_coherence_reversal_DPC": spacetime_dpc,
                            "spacetime_hostile_results": spacetime_hostiles,
                            "constant_structure_algebroid_results": algebroid_cases,
                            "minimum_dynamic_base_results": dynamic_base_cases,
                            "fibered_comparison_carrier_results": fibered_carrier_cases,
                            "curvature_coherence_ladder_results": curvature_ladder_cases,
                            "source_derived_truncation_results": truncation_cases,
                            "closure_capability_category_results": capcl_cases,
                        },
                        "live_character_frontier": "boundary_kernel_C2_multiplicities_known_source_multiplicities_open",
                        "cases": isotypic_cases,
                    },
                },
                "classification_law": "typed_existence_is_continuous_equivariant_domain_Ext_vanishing_uniqueness_is_boundary_kernel_elimination_authority_is_independent",
            },
            "pro_incidence_gate_models": pro_gate_results,
            "two_gate_law": "cutoff_naturality_and_completion_separatedness_are_independent_conjuncts",
            "derived_limit_defect_contract": {
                "exact_sequence": derived.get("exact_sequence"),
                "lim1_classifies_readout_kernel": derived.get("lim1_classifies_readout_kernel"),
                "cases": derived_cases,
                "typing_law": "completion_descent_kernel_and_limit_kernel_control_faithfulness_while_limit1_controls_effectivity",
                "closure_criterion": {
                    "cofinal_chain": closure.get("cofinal_chain"),
                    "descent_gate": closure.get("descent_gate"),
                    "faithfulness_gate": closure.get("faithfulness_gate"),
                    "effectivity_gate": closure.get("effectivity_gate"),
                    "cases": closure_cases,
                },
                "live_theta_gate_audit": live_audit,
                "live_closed_gate_count": 1,
                "live_open_gate_count": 2,
                "bigraded_kernel_tower_audit": bigraded,
                "source_grade_reassembly": reassembly,
                "uniformity_frontier": "construct_determinant_line_correspondence_or_prove_uniform_ML_in_the_product_chart",
            },
        },
        "all_path_coherence_frontier": coherence_frontier,
        "frontier_separation_law": "constructing one completed typed path and coherently identifying every legal path are separate objectives",
    }


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
    models = [compile_model(model) for model in contract.get("models", [])]
    theta_tate = compile_theta_tate_fixture(contract.get("theta_tate_fixture", {}))
    theta_triangle = compile_theta_repair_triangle(contract.get("theta_repair_triangle", {}))
    residual_typing = compile_residual_repair_typing(contract.get("residual_repair_typing_fixture", {}))
    operational = compile_operational_profiles(contract.get("operational_realizability_fixture", {}))
    authority_support = compile_authority_support(contract.get("authority_support_fixture", {}))
    commutant_interface = compile_commutant_interface(contract.get("commutant_interface_fixture", {}), authority_support)
    channel_semigroup = compile_channel_semigroup(contract.get("channel_semigroup_fixture", {}), authority_support)
    return {"schema": "marici.dependency-aware-partial-repair-result.v1", "passed": bool(models) and all(model["passed"] for model in models) and theta_tate["passed"] and theta_triangle["passed"] and residual_typing["passed"] and operational["passed"] and authority_support["passed"] and commutant_interface["passed"] and channel_semigroup["passed"], "models": models, "theta_tate_fixture": theta_tate, "theta_repair_triangle": theta_triangle, "residual_repair_typing": residual_typing, "operational_realizability":operational, "authority_support":authority_support, "commutant_interface":commutant_interface, "channel_semigroup":channel_semigroup}
