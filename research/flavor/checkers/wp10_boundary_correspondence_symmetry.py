"""Test whether limiting boundary arrows are declared S3^3/rephasing maps."""
import itertools
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
packet = json.loads(
    (RESULTS / "wp10_regular_multisheet_fiber.json").read_text())
PERMS = list(itertools.permutations(range(3)))
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def mask_slots(mask):
    return [slot for k, slot in enumerate(SLOTS) if mask & (1 << k)]


def entries(chart):
    mu, md = chart["member"]
    return ([("u", *slot) for slot in mask_slots(mu)]
            +[("d", *slot) for slot in mask_slots(md)])


records = []
for audit in packet["audits"]:
    chart = audit["chart"]
    face = audit["coordinate_face_continuation"]
    labels = entries(chart)
    source_drop = tuple(face["suppressed_edge_label"])
    partner_drop = tuple(face["partner_vanishing_edge_label"])
    source_theta = np.array(face["source_limit_log_parameters"])
    partner_theta = np.array(face["partner_limit_log_parameters"])
    source = {
        label: source_theta[i] for i, label in enumerate(labels)
        if label != source_drop
    }
    partner = {
        label: partner_theta[i] for i, label in enumerate(labels)
        if label != partner_drop
    }
    support_matches = 0
    best_log_residual = float("inf")
    best_permutation = None
    for pq, pu, pd in itertools.product(PERMS, repeat=3):
        def transport(label):
            sec, i, j = label
            return (sec, pq[i], (pu if sec == "u" else pd)[j])
        transported = {transport(label): value
                       for label, value in source.items()}
        if set(transported) != set(partner):
            continue
        support_matches += 1
        residual = max(abs(value-partner[label])
                       for label, value in transported.items())
        if residual < best_log_residual:
            best_log_residual = float(residual)
            best_permutation = {
                "q_rows": pq, "u_columns": pu, "d_columns": pd}
    finite_best_residual = (
        best_log_residual if np.isfinite(best_log_residual) else None)
    records.append({
        "chart": chart,
        "source_deleted_edge": source_drop,
        "partner_deleted_edge": partner_drop,
        "same_labelled_boundary_face": source_drop == partner_drop,
        "support_isomorphism_count": support_matches,
        "best_surviving_log_magnitude_residual": finite_best_residual,
        "best_support_permutation": best_permutation,
        "declared_permutation_rephasing_candidate":
            bool(finite_best_residual is not None
                 and finite_best_residual < 1e-5),
    })

out = {
    "schema": "marici.flavor.boundary_correspondence_symmetry.v1",
    "status": "complete_s3_cubed_magnitude_audit",
    "boundary_arrow_count": len(records),
    "same_labelled_face_count": sum(
        r["same_labelled_boundary_face"] for r in records),
    "support_isomorphic_count": sum(
        r["support_isomorphism_count"] > 0 for r in records),
    "permutation_rephasing_candidate_count": sum(
        r["declared_permutation_rephasing_candidate"] for r in records),
    "records": records,
}
(RESULTS / "wp10_boundary_correspondence_symmetry.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
