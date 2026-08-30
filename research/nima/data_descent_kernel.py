"""Minimal executable type kernel for Marici data-descent packets."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any


class ArrowKind(str, Enum):
    OPEN_RESTRICTION = "open_restriction"
    GROUPOID_ARROW = "groupoid_arrow"
    SPECIALIZATION = "specialization"
    CORRESPONDENCE = "correspondence"


class CapabilityStatusKind(str, Enum):
    EXECUTABLE = "Executable"
    CONDITIONAL = "Conditional"
    OBSTRUCTED = "Obstructed"


class CostValueKind(str, Enum):
    KNOWN = "known"
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"


REQUIRED_CIRCUIT_COST_FIELDS = (
    "physical_gate_count",
    "depth",
    "magic_ancilla_count",
)

COMPLETION_EXTENSION_MECHANISMS = {
    "bounded_unique_continuous_extension",
    "unique_continuous_locally_convex_extension",
    "closable_graph_closure",
    "closed_form_friedrichs_extension",
}

AUTHORITY_PERMISSIONS = {
    "physical_source_operation": {"selector", "readout"},
    "physical_relative_cycle": {"observer", "readout"},
    "resource_constructor": {"constructor", "executor"},
    "source_completed_operator": {"readout"},
    "policy_section": {"executor"},
    "algebraic_faithfulness": set(),
    "geometric_support": set(),
}


@dataclass(frozen=True)
class TypeErrorRecord:
    code: str
    subject: str
    detail: str


def _signature(obj: dict[str, Any]) -> tuple[Any, ...]:
    return (obj["coefficient_type"], obj["rank"], tuple(obj.get("grades", [])))


def _fraction(value: Any) -> Fraction:
    return Fraction(str(value))


def _matrix_rank(spec: dict[str, Any]) -> int:
    rows, columns = spec.get("shape", [0, 0])
    matrix = [[Fraction(0) for _ in range(columns)] for _ in range(rows)]
    for row, column, value in spec.get("entries", []):
        if 0 <= row < rows and 0 <= column < columns:
            matrix[row][column] += _fraction(value)
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [a - scale * b for a, b in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def validate(packet: dict[str, Any]) -> list[TypeErrorRecord]:
    errors: list[TypeErrorRecord] = []
    contexts = {x["id"]: x for x in packet.get("contexts", [])}
    objects = {x["id"]: x for x in packet.get("local_objects", [])}
    arrows = {x["id"]: x for x in packet.get("arrows", [])}
    replay_ids = {x["id"] for x in packet.get("evidence_replays", [])}

    def err(code: str, subject: str, detail: str):
        errors.append(TypeErrorRecord(code, subject, detail))

    # Resource-relative capability declarations.  Resource membership and
    # admission are distinct: merely naming transport does not authorize use.
    theories = {x["id"]: x for x in packet.get("resource_theories", [])}
    for tid, theory in theories.items():
        parent = theory.get("extends")
        if parent is not None and parent not in theories:
            err("unknown_parent_resource_theory", tid, str(parent))
        if theory.get("admission") not in {"admitted", "proposed"}:
            err("invalid_resource_theory_admission", tid, str(theory.get("admission")))
        seen_resources: set[str] = set()
        for resource in theory.get("resources", []):
            rid = resource.get("id")
            if not rid or rid in seen_resources:
                err("duplicate_or_missing_resource", tid, str(rid))
                continue
            seen_resources.add(rid)
            if resource.get("admitted") and not resource.get("authority_evidence"):
                err("unauthorized_resource_admission", f"{tid}:{rid}",
                    "admitted resources require source authority evidence")
        if parent is not None and any(x.get("admitted") for x in theory.get("resources", [])):
            if not theory.get("extension_authority"):
                err("unauthorized_resource_theory_extension", tid,
                    "an admitted extension requires explicit extension authority")

    def theory_resources(theory_id: str) -> dict[str, dict[str, Any]]:
        resources: dict[str, dict[str, Any]] = {}
        visited: set[str] = set()
        current = theory_id
        while current in theories and current not in visited:
            visited.add(current)
            theory = theories[current]
            for resource in theory.get("resources", []):
                rid = resource.get("id")
                if rid:
                    resources.setdefault(rid, resource)
            current = theory.get("extends")
        return resources

    def theory_extends(child: str, ancestor: str) -> bool:
        visited: set[str] = set()
        current: str | None = child
        while current in theories and current not in visited:
            if current == ancestor:
                return True
            visited.add(current)
            current = theories[current].get("extends")
        return False

    def validate_cost(cost: Any, subject: str) -> dict[str, str]:
        kinds: dict[str, str] = {}
        if not isinstance(cost, dict):
            err("missing_capability_cost", subject, "cost must be a typed field map")
            return kinds
        for field in REQUIRED_CIRCUIT_COST_FIELDS:
            if field not in cost:
                err("missing_required_cost_field", subject, field)
        for field, value in cost.items():
            if not isinstance(value, dict):
                err("untyped_cost_value", f"{subject}:{field}", repr(value))
                continue
            try:
                kind = CostValueKind(value.get("kind"))
            except ValueError:
                err("unknown_cost_value_kind", f"{subject}:{field}", str(value.get("kind")))
                continue
            kinds[field] = kind.value
            if kind is CostValueKind.KNOWN:
                known = value.get("value")
                if not isinstance(known, int) or isinstance(known, bool) or known < 0:
                    err("invalid_known_cost", f"{subject}:{field}", repr(known))
            elif not value.get("reason"):
                err("missing_cost_reason", f"{subject}:{field}", kind.value)
        return kinds

    capabilities = {x["id"]: x for x in packet.get("capabilities", [])}
    for cid, capability in capabilities.items():
        theory_id = capability.get("resource_theory")
        if theory_id not in theories:
            err("unknown_resource_theory", cid, str(theory_id))
            available: dict[str, dict[str, Any]] = {}
        else:
            available = theory_resources(theory_id)
        status = capability.get("status", {})
        try:
            kind = CapabilityStatusKind(status.get("kind"))
        except ValueError:
            err("unknown_capability_status", cid, str(status.get("kind")))
            continue
        cost_kinds = validate_cost(status.get("cost"), cid)
        used = capability.get("uses_resources", [])
        for rid in used:
            if rid not in available or not available[rid].get("admitted"):
                err("executable_unavailable_resource" if kind is CapabilityStatusKind.EXECUTABLE
                    else "unavailable_declared_resource", cid, rid)

        if kind is CapabilityStatusKind.EXECUTABLE:
            certificates = status.get("certificate", [])
            if not certificates:
                err("missing_execution_certificate", cid, "Executable requires replayable evidence")
            for certificate in certificates:
                if certificate.get("scope") != capability.get("subject"):
                    err("certificate_scope_mismatch", cid, str(certificate.get("scope")))
                if not certificate.get("evidence"):
                    err("missing_execution_evidence", cid, str(certificate.get("id")))
                if certificate.get("replay_id") not in replay_ids:
                    err("unknown_execution_replay", cid, str(certificate.get("replay_id")))
            if any(value == CostValueKind.UNDEFINED.value for value in cost_kinds.values()):
                err("executable_undefined_cost", cid,
                    "an executable circuit may have unknown, but not undefined, cost")
        elif kind is CapabilityStatusKind.CONDITIONAL:
            required = status.get("required_resource", [])
            if not required:
                err("missing_conditional_resource", cid, "Conditional requires a resource lift")
            contract = status.get("preserved_contract", {})
            if not contract.get("preserved") or not contract.get("evidence"):
                err("conditional_contract_not_preserved", cid,
                    "the required resource must preserve an evidenced contract")
        elif kind is CapabilityStatusKind.OBSTRUCTED:
            if not status.get("missing_resource"):
                err("missing_obstruction_resource", cid, "Obstructed requires a missing resource")
            witnesses = status.get("witness", [])
            if not witnesses or any(not x.get("evidence") for x in witnesses):
                err("missing_obstruction_witness", cid, "every obstruction witness needs evidence")
            if any(cost_kinds.get(field) != CostValueKind.UNDEFINED.value
                   for field in REQUIRED_CIRCUIT_COST_FIELDS):
                err("obstructed_cost_must_be_undefined", cid,
                    "an absent circuit has undefined gate, depth, and magic costs")

    status_rank = {
        CapabilityStatusKind.OBSTRUCTED.value: 0,
        CapabilityStatusKind.CONDITIONAL.value: 1,
        CapabilityStatusKind.EXECUTABLE.value: 2,
    }
    for transition in packet.get("capability_status_transitions", []):
        sid, tid = transition.get("source_capability"), transition.get("target_capability")
        source, target = capabilities.get(sid), capabilities.get(tid)
        if source is None or target is None:
            err("unknown_capability_status_endpoint", transition["id"], f"{sid}->{tid}")
            continue
        if source.get("subject") != target.get("subject"):
            err("capability_status_subject_mismatch", transition["id"],
                f'{source.get("subject")}->{target.get("subject")}')
        if not transition.get("evidence"):
            err("missing_capability_status_transition_evidence", transition["id"], "")
        direction = transition.get("kind")
        sr, tr = source["resource_theory"], target["resource_theory"]
        sk, tk = source["status"]["kind"], target["status"]["kind"]
        if direction == "extension":
            if not theory_extends(tr, sr):
                err("invalid_resource_extension", transition["id"], f"{sr}->{tr}")
            if status_rank.get(tk, -1) < status_rank.get(sk, -1):
                err("nonmonotone_capability_extension", transition["id"], f"{sk}->{tk}")
            if not transition.get("preserves_prior"):
                err("resource_extension_rewrites_prior", transition["id"], sid)
        elif direction == "restriction":
            if not theory_extends(sr, tr):
                err("invalid_resource_restriction", transition["id"], f"{sr}->{tr}")
            if status_rank.get(tk, -1) > status_rank.get(sk, -1):
                err("nonrestrictive_capability_forgetting", transition["id"], f"{sk}->{tk}")
        else:
            err("unknown_capability_status_transition", transition["id"], str(direction))

    for oid, obj in objects.items():
        if obj["context"] not in contexts:
            err("unknown_context", oid, obj["context"])

    for aid, arrow in arrows.items():
        try:
            kind = ArrowKind(arrow["kind"])
        except ValueError:
            err("unknown_arrow_kind", aid, arrow["kind"])
            continue
        so, to = objects.get(arrow["source"]), objects.get(arrow["target"])
        if so is None or to is None:
            err("unknown_object", aid, f'{arrow["source"]}->{arrow["target"]}')
            continue
        sc, tc = contexts[so["context"]], contexts[to["context"]]
        if kind is ArrowKind.OPEN_RESTRICTION:
            if not arrow.get("overlap_evidence"):
                err("missing_open_overlap", aid, "restriction requires an admitted open overlap")
            if sc.get("site") != tc.get("site"):
                err("site_mismatch", aid, "open restrictions must inhabit one declared site")
        elif kind is ArrowKind.GROUPOID_ARROW:
            if not arrow.get("invertible"):
                err("noninvertible_groupoid_arrow", aid, "groupoid arrows must be invertible")
            if _signature(so) != _signature(to):
                err("groupoid_fiber_mismatch", aid, "rank/coefficient/grade signature changed")
            if not arrow.get("authority_evidence"):
                err("missing_groupoid_authority", aid, "relabeling/gauge authority is required")
        elif kind is ArrowKind.SPECIALIZATION:
            if sc.get("stratum_depth", 0) >= tc.get("stratum_depth", 0):
                err("specialization_direction", aid, "target must be a deeper declared stratum")
        elif kind is ArrowKind.CORRESPONDENCE:
            if not arrow.get("kernel_or_span"):
                err("missing_correspondence_support", aid, "kernel/span typing is required")

    def path_type(path: list[str], cell_id: str):
        if not path:
            err("empty_path", cell_id, "coherence path is empty")
            return None
        seq = []
        for aid in path:
            if aid not in arrows:
                err("unknown_arrow", cell_id, aid)
                return None
            seq.append(arrows[aid])
        for left, right in zip(seq, seq[1:]):
            if left["target"] != right["source"]:
                err("noncomposable_path", cell_id, f'{left["id"]};{right["id"]}')
                return None
        return seq[0]["source"], seq[-1]["target"], tuple(x["kind"] for x in seq)

    for cell in packet.get("coherence_cells", []):
        typed = [path_type(p, cell["id"]) for p in cell["paths"]]
        typed = [x for x in typed if x is not None]
        if typed and any(x[:2] != typed[0][:2] for x in typed[1:]):
            err("parallel_path_mismatch", cell["id"], "paths have different endpoints")
        if cell.get("law") == "identity_cycle":
            if not typed or typed[0][0] != typed[0][1]:
                err("cycle_not_closed", cell["id"], "identity cycle must be an endomorphism")
            if cell.get("identity_defect") != 0:
                err("nonzero_identity_defect", cell["id"], str(cell.get("identity_defect")))
        if not cell.get("evidence"):
            err("missing_coherence_evidence", cell["id"], "coherence is asserted without evidence")

    # Derived objects and base change.  Nonflat change must never silently use
    # the ordinary tensor product; its Tor grade is part of the type.
    complexes = {x["id"]: x for x in packet.get("complexes", [])}
    derived = {x["id"]: x for x in packet.get("derived_objects", [])}
    for did, obj in derived.items():
        if obj["kind"] not in {"Kernel", "Cokernel", "Cone", "Tor"}:
            err("unknown_derived_kind", did, obj["kind"])
        if obj.get("source_complex") not in complexes:
            err("unknown_source_complex", did, str(obj.get("source_complex")))
    for bc in packet.get("base_changes", []):
        if bc.get("source_complex") not in complexes:
            err("unknown_source_complex", bc["id"], str(bc.get("source_complex")))
        if bc.get("target_context") not in contexts:
            err("unknown_context", bc["id"], str(bc.get("target_context")))
        if not bc.get("flat", False):
            if not bc.get("derived", False):
                err("nonflat_ordinary_base_change", bc["id"], "derived tensor product required")
            if not bc.get("tor_objects"):
                err("missing_tor_grade", bc["id"], "nonflat change requires declared Tor output")
        for tor in bc.get("tor_objects", []):
            if tor not in derived or derived[tor].get("kind") != "Tor":
                err("invalid_tor_reference", bc["id"], tor)
        if not bc.get("comparison_evidence"):
            err("missing_base_change_comparison", bc["id"], "comparison cell/evidence required")

    # Correspondence variance: a kernel/span is a pull--push operation, not a
    # covariant map with erased legs.
    for aid, arrow in arrows.items():
        if arrow.get("kind") != ArrowKind.CORRESPONDENCE.value:
            continue
        if arrow.get("variance") != "contravariant_left_covariant_right":
            err("correspondence_variance_mismatch", aid, str(arrow.get("variance")))
        if not arrow.get("left_leg") or not arrow.get("right_leg"):
            err("missing_correspondence_leg", aid, "both span legs are required")
        if arrow.get("pushforward_required") and not arrow.get("right_proper_or_supported"):
            err("unauthorized_pushforward", aid, "properness or support is required")

    # Finite executable capability fibers.
    fibers = {x["id"]: x for x in packet.get("capability_fibers", [])}
    for fid, fiber in fibers.items():
        ops = {x["id"]: x for x in fiber.get("operations", [])}
        states = set(fiber.get("states", []))
        for oid, op in ops.items():
            table = op.get("action_table", {})
            if set(table) != states or not set(table.values()) <= states:
                err("nonexecutable_operation", f"{fid}:{oid}", "action table is not total on the declared state set")
        identity = fiber.get("identity")
        if identity not in ops:
            err("missing_capability_identity", fid, str(identity))
        comp = {(x["left"], x["right"]): x["result"] for x in fiber.get("composition", [])}
        for a in ops:
            for b in ops:
                if (a, b) not in comp or comp[(a, b)] not in ops:
                    err("incomplete_capability_composition", fid, f"{a};{b}")
                    continue
                expected = {s: ops[a]["action_table"][ops[b]["action_table"][s]] for s in states}
                if expected != ops[comp[(a, b)]]["action_table"]:
                    err("capability_composition_defect", fid, f"{a};{b}")
        diagnostics = set(fiber.get("diagnostics", []))
        for policy in fiber.get("policies", []):
            section = policy.get("section", {})
            if set(section) != diagnostics or not set(section.values()) <= set(ops):
                err("incomplete_policy_section", f"{fid}:{policy['id']}", "policy is not a total section")
            goal = policy.get("goal_state")
            inputs = policy.get("diagnostic_inputs", {})
            if goal is not None:
                for d, state in inputs.items():
                    if d in section and ops[section[d]]["action_table"].get(state) != goal:
                        err("policy_goal_defect", f"{fid}:{policy['id']}", d)

    for tr in packet.get("capability_transitions", []):
        sf, tf = fibers.get(tr.get("source_fiber")), fibers.get(tr.get("target_fiber"))
        if sf is None or tf is None:
            err("unknown_capability_fiber", tr["id"], f'{tr.get("source_fiber")}->{tr.get("target_fiber")}')
            continue
        smap = tr.get("operation_map", {})
        sops, tops = {x["id"] for x in sf["operations"]}, {x["id"] for x in tf["operations"]}
        if set(smap) != sops or set(smap.values()) != tops:
            err("capability_transition_not_bijective", tr["id"], "operation map must be a bijection")
        scomp = {(x["left"], x["right"]): x["result"] for x in sf["composition"]}
        tcomp = {(x["left"], x["right"]): x["result"] for x in tf["composition"]}
        for (a, b), c in scomp.items():
            if a in smap and b in smap and c in smap and tcomp.get((smap[a], smap[b])) != smap[c]:
                err("capability_transition_composition_defect", tr["id"], f"{a};{b}")
        if sf.get("resource_theory") or tf.get("resource_theory"):
            if sf.get("resource_theory") not in theories or tf.get("resource_theory") not in theories:
                err("unknown_resource_theory", tr["id"],
                    f'{sf.get("resource_theory")}->{tf.get("resource_theory")}')
            if not tr.get("evidence"):
                err("missing_capability_transition_evidence", tr["id"],
                    "resource-typed frame changes require evidence")
            sc, tc = sf.get("capability_ref"), tf.get("capability_ref")
            if sc not in capabilities or tc not in capabilities:
                err("unknown_frame_capability", tr["id"], f"{sc}->{tc}")
            elif capabilities[sc]["status"]["kind"] != capabilities[tc]["status"]["kind"]:
                err("frame_transition_status_mismatch", tr["id"], f"{sc}->{tc}")

    # Topology-bearing completion.  Completion changes the admissible space;
    # it does not, by itself, choose an operator or manufacture a kernel.
    spaces = {x["id"]: x for x in packet.get("completion_spaces", [])}
    operators = {x["id"]: x for x in packet.get("completion_operators", [])}
    completions = {x["id"]: x for x in packet.get("completion_interfaces", [])}
    comparisons = {x["id"]: x for x in packet.get("kernel_comparisons", [])}
    for cid, completion in completions.items():
        source, target = completion.get("source_space"), completion.get("completed_space")
        if source not in spaces or target not in spaces:
            err("unknown_completion_space", cid, f"{source}->{target}")
        if completion.get("source_target_space") not in spaces or completion.get("completed_target_space") not in spaces:
            err("unknown_completion_target_space", cid, "source and completed targets must be typed")
        if completion.get("constructor_kind") != "topology_bearing_completion":
            err("completion_as_ordinary_base_change", cid, str(completion.get("constructor_kind")))
        topology = completion.get("topology", {})
        if not topology.get("kind") or not topology.get("separation"):
            err("untyped_completion_topology", cid, str(topology))
        embedding = completion.get("dense_embedding", {})
        if not embedding.get("map") or not embedding.get("injective") or not embedding.get("dense") or not embedding.get("evidence"):
            err("invalid_dense_embedding", cid, str(embedding))
        if not completion.get("completion_map", {}).get("universal_property_evidence"):
            err("missing_completion_map", cid, "completion universal property is required")
        source_operator = operators.get(completion.get("source_operator"))
        extended_operator = operators.get(completion.get("extended_operator"))
        if source_operator is None or extended_operator is None:
            err("unknown_completion_operator", cid, f"{completion.get('source_operator')}->{completion.get('extended_operator')}")
        proof = completion.get("extension_well_defined", {})
        mechanism = proof.get("mechanism")
        if mechanism not in COMPLETION_EXTENSION_MECHANISMS:
            err("unknown_extension_mechanism", cid, str(mechanism))
        if not proof.get("unique") or not proof.get("proof_evidence"):
            err("operator_extension_not_canonical", cid, "unique evidenced extension required")
        square = completion.get("operator_extension_square", {})
        if not square.get("commutes") or not square.get("evidence"):
            err("operator_extension_square_defect", cid, str(square))
        if completion.get("manufactured_from_completion_only", False):
            err("completion_manufactures_operator", cid, "topology alone cannot choose an operator")
        if extended_operator is not None and mechanism in {
            "closable_graph_closure", "closed_form_friedrichs_extension"
        }:
            if not extended_operator.get("closed") or not extended_operator.get("dense_domain_evidence"):
                err("unbounded_extension_not_closed", cid, "closed densely defined extension required")

    for kid, comparison in comparisons.items():
        if comparison.get("completion") not in completions:
            err("unknown_kernel_completion", kid, str(comparison.get("completion")))
        source_dim = comparison.get("source_kernel_dimension")
        completed_dim = comparison.get("completed_kernel_dimension")
        if not isinstance(source_dim, int) or not isinstance(completed_dim, int):
            err("untyped_kernel_dimension", kid, f"{source_dim}->{completed_dim}")
            continue
        square = comparison.get("comparison_square", {})
        rank = square.get("map_rank")
        if not square.get("commutes") or not square.get("evidence"):
            err("kernel_comparison_square_defect", kid, str(square))
        if not isinstance(rank, int) or rank < 0 or rank > min(source_dim, completed_dim):
            err("invalid_kernel_comparison_rank", kid, str(rank))
            rank = 0
        groups = comparison.get("class_groups", [])
        if sum(x.get("dimension", 0) for x in groups) != completed_dim:
            err("kernel_partition_dimension_defect", kid, str(completed_dim))
        if sum(x.get("dimension", 0) for x in groups if x.get("classification") == "descends") != rank:
            err("descended_kernel_rank_defect", kid, str(rank))
        derived_dimension = 0
        for group in groups:
            classification = group.get("classification")
            if classification == "completion_only":
                if not group.get("graph_limit_evidence") or group.get("tor_object") is not None:
                    err("completion_only_class_mistyped", f"{kid}:{group.get('id')}", "graph-limit evidence without Tor required")
            elif classification == "derived_completion_obstruction":
                derived_dimension += group.get("dimension", 0)
                tor = derived.get(group.get("tor_object"))
                if tor is None or tor.get("kind") != "Tor" or not group.get("derived_evidence"):
                    err("derived_completion_obstruction_untyped", f"{kid}:{group.get('id')}", str(group.get("tor_object")))
            elif classification != "descends":
                err("unknown_completed_kernel_class", f"{kid}:{group.get('id')}", str(classification))
        if comparison.get("completion_defect_dimension") != derived_dimension:
            err("completion_defect_dimension_mismatch", kid, str(derived_dimension))

    support_ids = {x["id"] for x in packet.get("support_objects", [])}
    for identification in packet.get("support_identifications", []):
        endpoints = {identification.get("left"), identification.get("right")}
        if endpoints & support_ids and endpoints & set(comparisons):
            err("characteristic_support_is_not_kernel_support", identification["id"], str(endpoints))

    for fiber in packet.get("finite_linear_observation_fibers", []):
        fid = fiber["id"]
        comparison = comparisons.get(fiber.get("kernel_comparison"))
        if comparison is None:
            err("unknown_observation_kernel", fid, str(fiber.get("kernel_comparison")))
            continue
        kernel_dimension = comparison["completed_kernel_dimension"]
        if fiber.get("kernel_dimension") != kernel_dimension:
            err("kernel_dimension_port_count_conflation", fid, str(fiber.get("kernel_dimension")))
        ports = fiber.get("ports", [])
        matrix = fiber.get("observation_matrix", {})
        if matrix.get("shape") != [len(ports), kernel_dimension]:
            err("observation_matrix_shape_defect", fid, str(matrix.get("shape")))
        for port in ports:
            if port.get("availability") != "available":
                err("unavailable_port_is_not_zero_port", f"{fid}:{port.get('id')}", str(port.get("availability")))
            if not port.get("execution_evidence") or not port.get("source_authority"):
                err("unexecutable_observation_port", f"{fid}:{port.get('id')}", "execution and source authority required")
        rank = _matrix_rank(matrix)
        if rank != fiber.get("declared_rank"):
            err("observation_rank_certificate_defect", fid, str(rank))
        if fiber.get("faithful") != (rank == kernel_dimension):
            err("observation_faithfulness_defect", fid, str(rank))
        entries = matrix.get("entries", [])
        deletion_ranks = []
        for deleted in range(len(ports)):
            remapped = []
            for row, column, value in entries:
                if row == deleted:
                    continue
                remapped.append([row - (row > deleted), column, value])
            deletion_ranks.append(_matrix_rank({"shape": [len(ports) - 1, kernel_dimension], "entries": remapped}))
        certificate = fiber.get("deletion_certificate", {})
        if certificate.get("ranks") != deletion_ranks:
            err("port_deletion_certificate_defect", fid, str(deletion_ranks))
        minimal = rank == kernel_dimension and all(x < kernel_dimension for x in deletion_ranks)
        if certificate.get("minimal") != minimal:
            err("port_minimality_defect", fid, str(minimal))

    for compression in packet.get("spectral_compressions", []):
        if compression.get("operator") not in operators:
            err("unknown_compression_operator", compression["id"], str(compression.get("operator")))
        if not compression.get("compact_resolvent_evidence"):
            err("missing_compact_resolvent_evidence", compression["id"], "compact resolvent is required")
        if not compression.get("finite_rank") or not compression.get("strongly_converges_to_identity"):
            err("invalid_spectral_compression", compression["id"], "finite-rank strong exhaustion required")
        if compression.get("rh_bearing_kernel_claim", False):
            err("unauthorized_rh_kernel_claim", compression["id"], "compression alone carries no RH theorem")

    # Authority is typed by provenance.  Faithfulness and support are not
    # authority sources, and transport cannot silently upgrade authority.
    authority_sources = {x["id"]: x for x in packet.get("authority_sources", [])}
    grants = {x["id"]: x for x in packet.get("authority_grants", [])}
    for sid, source in authority_sources.items():
        provenance = source.get("provenance_kind")
        if provenance not in AUTHORITY_PERMISSIONS:
            err("unknown_authority_provenance", sid, str(provenance))
        if not source.get("evidence"):
            err("missing_authority_evidence", sid, "authority provenance requires evidence")
    for gid, grant in grants.items():
        source = authority_sources.get(grant.get("source_authority"))
        if source is None:
            err("unknown_authority_source", gid, str(grant.get("source_authority")))
            continue
        kind = grant.get("authority_kind")
        if kind not in AUTHORITY_PERMISSIONS[source.get("provenance_kind")]:
            err("unauthorized_authority_promotion", gid, f"{source.get('provenance_kind')}->{kind}")
        if not grant.get("subject") or not grant.get("evidence"):
            err("untyped_authority_grant", gid, "subject and evidence required")
    for transport in packet.get("authority_transports", []):
        grant = grants.get(transport.get("source_grant"))
        if grant is None:
            err("unknown_authority_grant", transport["id"], str(transport.get("source_grant")))
            continue
        if transport.get("target_authority_kind") != grant.get("authority_kind"):
            err("authority_transport_upgrade", transport["id"], f"{grant.get('authority_kind')}->{transport.get('target_authority_kind')}")
        if not transport.get("evidence"):
            err("missing_authority_transport_evidence", transport["id"], "transport requires evidence")

    # Conditioned reliability is attached to an authorized readout/executor,
    # not used to create selector authority.
    for certificate in packet.get("conditioned_reliability_certificates", []):
        rid = certificate["id"]
        grant = grants.get(certificate.get("authority_grant"))
        if grant is None or grant.get("authority_kind") not in {"readout", "executor"}:
            err("reliability_without_operational_authority", rid, str(certificate.get("authority_grant")))
        try:
            gamma = _fraction(certificate.get("gamma"))
            terms = certificate.get("errors", {})
            sampling = _fraction(terms.get("sampling"))
            detector = _fraction(terms.get("detector"))
            canonical = _fraction(terms.get("canonical"))
            reset = _fraction(terms.get("reset"))
            if gamma <= 0:
                err("nonpositive_reliability_margin", rid, str(gamma))
                continue
            if min(sampling, detector, canonical, reset) < 0:
                err("negative_reliability_error", rid, str(terms))
                continue
            computed = (sampling + detector) / gamma + canonical + reset
            if _fraction(certificate.get("declared_bound")) != computed:
                err("reliability_bound_mismatch", rid, str(computed))
        except (ValueError, TypeError, ZeroDivisionError):
            err("untyped_reliability_certificate", rid, "rational gamma, errors, and bound required")
        if not certificate.get("evidence"):
            err("missing_reliability_evidence", rid, "conditioned bound requires evidence")

    # A bounded source-relative explanation separates the physical producer
    # from its verifier.  The verifier certifies behavior; it does not produce
    # the capability or inherit the producer's authority.
    for audit in packet.get("source_relative_capability_audits", []):
        aid = audit["id"]
        source = audit.get("physical_source", {})
        model = audit.get("implementation_model", {})
        resources = audit.get("resource_class", {})
        capability = audit.get("implemented_capability", {})
        verifier = audit.get("verification_model", {})
        budgets = audit.get("budgets", {})
        counterfactual = audit.get("counterfactual", {})
        if not source.get("id") or not source.get("evidence"):
            err("untyped_physical_source", aid, str(source))
        if not model.get("id") or not model.get("independently_validated") or not model.get("evidence"):
            err("unvalidated_implementation_model", aid, str(model))
        if not resources.get("id") or not resources.get("descendant_closure") or not resources.get("evidence"):
            err("unclosed_resource_class", aid, str(resources))
        if not capability.get("id") or not capability.get("implementation_evidence"):
            err("unimplemented_capability", aid, str(capability))
        if not verifier.get("id") or not verifier.get("independently_validated") or not verifier.get("evidence"):
            err("unvalidated_verification_model", aid, str(verifier))
        if verifier.get("id") in {source.get("id"), model.get("id")}:
            err("producer_verifier_conflation", aid, str(verifier.get("id")))
        try:
            epsilon = _fraction(budgets.get("epsilon"))
            time = _fraction(budgets.get("time"))
            resource = _fraction(budgets.get("resource"))
            if epsilon < 0 or time <= 0 or resource <= 0:
                err("invalid_capability_audit_budget", aid, str(budgets))
        except (ValueError, TypeError):
            err("untyped_capability_audit_budget", aid, str(budgets))
        if counterfactual.get("removed_resource_class") != resources.get("id"):
            err("counterfactual_wrong_resource_class", aid, str(counterfactual))
        if not counterfactual.get("removes_descendants"):
            err("counterfactual_leaves_resource_descendants", aid, str(counterfactual))
        if not counterfactual.get("nontrivial_capability_change") or not counterfactual.get("evidence"):
            err("counterfactual_not_explanatory", aid, str(counterfactual))
        if audit.get("claims_universal_law", False):
            err("bounded_audit_promoted_to_universal_law", aid, "source-relative audit is not a universal metaphysics")

    return errors


def compile_packet(packet: dict[str, Any]) -> dict[str, Any]:
    errors = validate(packet)
    return {
        "valid": not errors,
        "error_count": len(errors),
        "errors": [e.__dict__ for e in errors],
        "context_count": len(packet.get("contexts", [])),
        "local_object_count": len(packet.get("local_objects", [])),
        "arrow_count": len(packet.get("arrows", [])),
        "coherence_cell_count": len(packet.get("coherence_cells", [])),
        "derived_object_count": len(packet.get("derived_objects", [])),
        "base_change_count": len(packet.get("base_changes", [])),
        "capability_fiber_count": len(packet.get("capability_fibers", [])),
        "resource_theory_count": len(packet.get("resource_theories", [])),
        "capability_count": len(packet.get("capabilities", [])),
        "capability_status_transition_count": len(packet.get("capability_status_transitions", [])),
        "completion_interface_count": len(packet.get("completion_interfaces", [])),
        "kernel_comparison_count": len(packet.get("kernel_comparisons", [])),
        "linear_observation_fiber_count": len(packet.get("finite_linear_observation_fibers", [])),
        "authority_source_count": len(packet.get("authority_sources", [])),
        "authority_grant_count": len(packet.get("authority_grants", [])),
        "reliability_certificate_count": len(packet.get("conditioned_reliability_certificates", [])),
        "source_relative_capability_audit_count": len(packet.get("source_relative_capability_audits", [])),
    }


def replay_evidence(packet: dict[str, Any], site_root: Path, timeout: int = 120) -> dict[str, Any]:
    """Replay site-local Python evidence and verify its declared artifact."""
    results = []
    root = site_root.resolve()
    for ev in packet.get("evidence_replays", []):
        checker = (root / ev["checker"]).resolve()
        artifact = (root / ev["artifact"]).resolve()
        if root not in checker.parents or root not in artifact.parents or checker.suffix != ".py":
            results.append({"id": ev["id"], "passed": False, "code": "evidence_path_refused"})
            continue
        run = subprocess.run([sys.executable, str(checker)], cwd=root, text=True,
                             capture_output=True, timeout=timeout)
        digest = hashlib.sha256(artifact.read_bytes()).hexdigest() if artifact.exists() else None
        data = json.loads(artifact.read_text()) if artifact.exists() else {}
        expected = ev.get("expected", {})
        field_ok = all(data.get(k) == v for k, v in expected.items())
        digest_ok = not ev.get("sha256") or digest == ev["sha256"]
        results.append({"id": ev["id"], "passed": run.returncode == 0 and field_ok and digest_ok,
                        "returncode": run.returncode, "artifact_sha256": digest,
                        "expected_fields_match": field_ok, "expected_digest_match": digest_ok})
    return {"passed": all(x["passed"] for x in results), "results": results}
