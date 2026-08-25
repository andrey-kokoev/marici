"""Sector-neutral completion and finite linear observation interface.

This is a conservative extension layer over Nima's data-descent v2 compiler.
It never changes the base validator and never infers an operator, kernel, or
executable port from topology or support alone.
"""

from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction
from typing import Any

from data_descent_kernel import TypeErrorRecord, compile_packet as compile_v2


EXTENSION_MECHANISMS = {
    "bounded_unique_continuous_extension",
    "unique_continuous_locally_convex_extension",
    "closable_graph_closure",
    "closed_form_friedrichs_extension",
}


def _rank(rows: list[list[Fraction]]) -> int:
    matrix = [row[:] for row in rows]
    if not matrix:
        return 0
    row_count, column_count = len(matrix), len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((r for r in range(pivot_row, row_count) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or not matrix[r][column]:
                continue
            scale = matrix[r][column]
            matrix[r] = [a - scale * b for a, b in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def _matrix(spec: dict[str, Any]) -> list[list[Fraction]]:
    rows, columns = spec.get("shape", [0, 0])
    matrix = [[Fraction(0) for _ in range(columns)] for _ in range(rows)]
    for row, column, value in spec.get("entries", []):
        if 0 <= row < rows and 0 <= column < columns:
            matrix[row][column] += Fraction(str(value))
    return matrix


def validate_generic(packet: dict[str, Any]) -> list[TypeErrorRecord]:
    errors: list[TypeErrorRecord] = []

    def err(code: str, subject: str, detail: str) -> None:
        errors.append(TypeErrorRecord(code, subject, detail))

    spaces = {item["id"]: item for item in packet.get("completion_spaces", [])}
    operators = {item["id"]: item for item in packet.get("completion_operators", [])}
    completions = {item["id"]: item for item in packet.get("completion_interfaces", [])}
    comparisons = {item["id"]: item for item in packet.get("kernel_comparisons", [])}
    derived_objects = {item["id"]: item for item in packet.get("derived_objects", [])}

    for cid, completion in completions.items():
        source, target = completion.get("source_space"), completion.get("completed_space")
        if source not in spaces or target not in spaces:
            err("unknown_completion_space", cid, f"{source}->{target}")
        topology = completion.get("topology", {})
        if not topology.get("kind") or not topology.get("separation"):
            err("untyped_completion_topology", cid, str(topology))
        if completion.get("constructor_kind") != "topology_bearing_completion":
            err("completion_as_ordinary_base_change", cid, str(completion.get("constructor_kind")))
        embedding = completion.get("dense_embedding", {})
        if not embedding.get("map") or not embedding.get("injective") or not embedding.get("dense"):
            err("invalid_dense_embedding", cid, str(embedding))
        if not embedding.get("evidence"):
            err("missing_density_evidence", cid, "density requires evidence")
        completion_map = completion.get("completion_map", {})
        if not completion_map.get("map") or not completion_map.get("universal_property_evidence"):
            err("missing_completion_map", cid, str(completion_map))
        source_operator = operators.get(completion.get("source_operator"))
        extended_operator = operators.get(completion.get("extended_operator"))
        if source_operator is None or extended_operator is None:
            err("unknown_completion_operator", cid, f"{completion.get('source_operator')}->{completion.get('extended_operator')}")
        source_target = completion.get("source_target_space")
        completed_target = completion.get("completed_target_space")
        if source_target not in spaces or completed_target not in spaces:
            err("unknown_completion_target_space", cid, f"{source_target}->{completed_target}")
        target_embedding = completion.get("target_embedding", {})
        if not target_embedding.get("map") or not target_embedding.get("injective") or not target_embedding.get("evidence"):
            err("invalid_target_embedding", cid, str(target_embedding))
        proof = completion.get("extension_well_defined", {})
        mechanism = proof.get("mechanism")
        if mechanism not in EXTENSION_MECHANISMS:
            err("unknown_extension_mechanism", cid, str(mechanism))
        if not proof.get("unique") or not proof.get("proof_evidence"):
            err("operator_extension_not_canonical", cid, "unique evidenced extension required")
        square = completion.get("operator_extension_square", {})
        if not square.get("commutes") or not square.get("evidence"):
            err("operator_extension_square_defect", cid, str(square))
        if completion.get("manufactured_from_completion_only", False):
            err("completion_manufactures_operator", cid, "topology alone cannot choose the extension")
        if extended_operator is not None:
            operator_domain = extended_operator.get("operator_domain")
            if mechanism in {"bounded_unique_continuous_extension", "unique_continuous_locally_convex_extension"}:
                if operator_domain != target:
                    err("continuous_extension_domain_defect", cid, f"{operator_domain}!={target}")
            elif mechanism in {"closable_graph_closure", "closed_form_friedrichs_extension"}:
                if not operator_domain or operator_domain == target or not extended_operator.get("dense_domain_evidence"):
                    err("unbounded_extension_domain_untyped", cid, str(operator_domain))
                if not extended_operator.get("closed"):
                    err("unbounded_extension_not_closed", cid, str(extended_operator.get("closed")))

    for kid, comparison in comparisons.items():
        if comparison.get("completion") not in completions:
            err("unknown_kernel_completion", kid, str(comparison.get("completion")))
        source_dim = comparison.get("source_kernel_dimension")
        completed_dim = comparison.get("completed_kernel_dimension")
        square = comparison.get("comparison_square", {})
        rank = square.get("map_rank")
        if not square.get("commutes") or not square.get("evidence"):
            err("kernel_comparison_square_defect", kid, str(square))
        if not isinstance(rank, int) or rank < 0 or rank > min(source_dim, completed_dim):
            err("invalid_kernel_comparison_rank", kid, str(rank))
        if square.get("injective") and rank != source_dim:
            err("noninjective_kernel_comparison", kid, f"rank {rank} != {source_dim}")
        groups = comparison.get("class_groups", [])
        kinds = {"descends", "completion_only", "derived_completion_obstruction"}
        if any(group.get("classification") not in kinds for group in groups):
            err("unknown_completed_kernel_class", kid, str(groups))
        total = sum(group.get("dimension", 0) for group in groups)
        descended = sum(group.get("dimension", 0) for group in groups if group.get("classification") == "descends")
        completion_only = [group for group in groups if group.get("classification") == "completion_only"]
        derived = [group for group in groups if group.get("classification") == "derived_completion_obstruction"]
        if total != completed_dim:
            err("kernel_partition_dimension_defect", kid, f"{total}!={completed_dim}")
        if descended != rank:
            err("descended_kernel_rank_defect", kid, f"{descended}!={rank}")
        for group in completion_only:
            if not group.get("graph_limit_evidence") or group.get("tor_object") is not None:
                err("completion_only_class_mistyped", f"{kid}:{group.get('id')}", "ordinary graph-limit evidence and no Tor object required")
        for group in derived:
            if not group.get("tor_object") or not group.get("derived_evidence"):
                err("derived_completion_obstruction_untyped", f"{kid}:{group.get('id')}", "Tor reference and evidence required")
            elif group["tor_object"] not in derived_objects or derived_objects[group["tor_object"]].get("kind") != "Tor":
                err("invalid_derived_completion_obstruction", f"{kid}:{group.get('id')}", str(group.get("tor_object")))
        defect = comparison.get("completion_defect_dimension")
        if defect != sum(group.get("dimension", 0) for group in derived):
            err("completion_defect_dimension_mismatch", kid, str(defect))

    support_ids = {item["id"] for item in packet.get("support_objects", [])}
    kernel_ids = set(comparisons)
    for identification in packet.get("support_identifications", []):
        endpoints = {identification.get("left"), identification.get("right")}
        if endpoints & support_ids and endpoints & kernel_ids:
            err("characteristic_support_is_not_kernel_support", identification["id"], str(endpoints))

    for fiber in packet.get("finite_linear_observation_fibers", []):
        fid = fiber["id"]
        comparison = comparisons.get(fiber.get("kernel_comparison"))
        if comparison is None:
            err("unknown_observation_kernel", fid, str(fiber.get("kernel_comparison")))
            continue
        kernel_dimension = comparison["completed_kernel_dimension"]
        if fiber.get("kernel_dimension") != kernel_dimension:
            err("kernel_dimension_port_count_conflation", fid, f"declared {fiber.get('kernel_dimension')} != kernel {kernel_dimension}")
        ports = fiber.get("ports", [])
        matrix_spec = fiber.get("observation_matrix", {})
        matrix = _matrix(matrix_spec)
        shape = matrix_spec.get("shape", [0, 0])
        if shape != [len(ports), kernel_dimension]:
            err("observation_matrix_shape_defect", fid, f"{shape} != {[len(ports), kernel_dimension]}")
        unavailable = [port["id"] for port in ports if port.get("availability") != "available"]
        if unavailable:
            err("unavailable_port_is_not_zero_port", fid, ",".join(unavailable))
        for port in ports:
            if not port.get("execution_evidence") or not port.get("source_authority"):
                err("unexecutable_observation_port", f"{fid}:{port['id']}", "execution and source authority required")
        rank = _rank(matrix)
        if rank != fiber.get("declared_rank"):
            err("observation_rank_certificate_defect", fid, f"computed {rank}")
        faithful = rank == kernel_dimension
        if faithful != fiber.get("faithful"):
            err("observation_faithfulness_defect", fid, str(faithful))
        deletion_ranks = [_rank(matrix[:index] + matrix[index + 1:]) for index in range(len(matrix))]
        computed_minimal = faithful and all(value < kernel_dimension for value in deletion_ranks)
        certificate = fiber.get("deletion_certificate", {})
        if certificate.get("ranks") != deletion_ranks:
            err("port_deletion_certificate_defect", fid, str(deletion_ranks))
        if certificate.get("minimal") != computed_minimal:
            err("port_minimality_defect", fid, str(computed_minimal))
        if any(port.get("availability") == "unavailable" and port.get("zero_value_witness") for port in ports):
            err("unavailable_port_is_not_zero_port", fid, "a value cannot be assigned to an unavailable port")

    for compression in packet.get("spectral_compressions", []):
        if compression.get("operator") not in operators:
            err("unknown_compression_operator", compression["id"], str(compression.get("operator")))
        if not compression.get("compact_resolvent_evidence"):
            err("missing_compact_resolvent_evidence", compression["id"], "spectral exhaustion requires compact resolvent")
        if not compression.get("finite_rank") or not compression.get("strongly_converges_to_identity"):
            err("invalid_spectral_compression", compression["id"], "finite rank and strong exhaustion required")
        if compression.get("rh_bearing_kernel_claim", False):
            err("unauthorized_rh_kernel_claim", compression["id"], "compression alone carries no RH kernel theorem")

    return errors


def compile_packet(packet: dict[str, Any]) -> dict[str, Any]:
    base = compile_v2(packet)
    errors = [TypeErrorRecord(**item) for item in base["errors"]]
    errors.extend(validate_generic(packet))
    return {
        **base,
        "valid": not errors,
        "error_count": len(errors),
        "errors": [asdict(error) for error in errors],
        "completion_interface_count": len(packet.get("completion_interfaces", [])),
        "kernel_comparison_count": len(packet.get("kernel_comparisons", [])),
        "linear_observation_fiber_count": len(packet.get("finite_linear_observation_fibers", [])),
        "spectral_compression_count": len(packet.get("spectral_compressions", [])),
        "extension": "marici.generic-completion-interface.v1",
    }
