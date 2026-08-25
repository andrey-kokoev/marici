"""Minimal executable type kernel for Marici data-descent packets."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
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


@dataclass(frozen=True)
class TypeErrorRecord:
    code: str
    subject: str
    detail: str


def _signature(obj: dict[str, Any]) -> tuple[Any, ...]:
    return (obj["coefficient_type"], obj["rank"], tuple(obj.get("grades", [])))


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
