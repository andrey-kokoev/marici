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

    def err(code: str, subject: str, detail: str):
        errors.append(TypeErrorRecord(code, subject, detail))

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
