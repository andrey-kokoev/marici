"""Minimal executable type kernel for Marici data-descent packets."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
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
    }
