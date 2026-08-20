"""Lie-algebra stabilizers and sparse-support orbit intersections."""
import json
import sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wp7_ensemble import build_texture, mask_slots  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
packet = json.loads(
    (RESULTS / "wp10_regular_multisheet_fiber.json").read_text())


def u3_basis():
    basis = []
    for i in range(3):
        value = np.zeros((3, 3), complex)
        value[i, i] = 1j
        basis.append(value)
    for i in range(3):
        for j in range(i+1, 3):
            real = np.zeros((3, 3), complex)
            real[i, j] = 1
            real[j, i] = -1
            basis.append(real)
            imag = np.zeros((3, 3), complex)
            imag[i, j] = 1j
            imag[j, i] = 1j
            basis.append(imag)
    return basis


BASIS = u3_basis()


def real_vector(*matrices):
    flat = np.concatenate([value.ravel() for value in matrices])
    return np.r_[flat.real, flat.imag]


def numerical_rank(matrix):
    singular = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular > singular[0]*1e-9))
    gap = (float(singular[rank-1]/singular[rank])
           if 0 < rank < len(singular) and singular[rank] > 0 else None)
    return rank, singular, gap


def audit_texture(yu, yd, chart):
    columns = []
    support_columns = []
    zero_u = np.abs(yu) < 1e-14
    zero_d = np.abs(yd) < 1e-14
    for group in range(3):
        for generator in BASIS:
            xq = generator if group == 0 else np.zeros((3, 3), complex)
            xu = generator if group == 1 else np.zeros((3, 3), complex)
            xd = generator if group == 2 else np.zeros((3, 3), complex)
            du = xq@yu-yu@xu
            dd = xq@yd-yd@xd
            columns.append(real_vector(du, dd))
            support_columns.append(real_vector(du[zero_u], dd[zero_d]))
    action = np.stack(columns, axis=1)
    normal = np.stack(support_columns, axis=1)
    action_rank, _, action_gap = numerical_rank(action)
    normal_rank, _, normal_gap = numerical_rank(normal)
    mu, md = chart["member"]
    labels = ([("u", *slot) for slot in mask_slots(mu)]
              +[("d", *slot) for slot in mask_slots(md)])
    chart_columns = []
    for sector, i, j in labels:
        du = np.zeros((3, 3), complex)
        dd = np.zeros((3, 3), complex)
        target = yu if sector == "u" else yd
        (du if sector == "u" else dd)[i, j] = target[i, j]
        chart_columns.append(real_vector(du, dd))
    du = np.zeros((3, 3), complex)
    dd = np.zeros((3, 3), complex)
    sector, i, j = chart["phase_edge"]
    target = yu if sector == "u" else yd
    (du if sector == "u" else dd)[i, j] = 1j*target[i, j]
    chart_columns.append(real_vector(du, dd))
    chart_tangent = np.stack(chart_columns, axis=1)
    chart_rank, _, chart_gap = numerical_rank(chart_tangent)
    combined_rank, _, combined_gap = numerical_rank(
        np.hstack((action, chart_tangent)))
    chart_orbit_intersection_dimension = (
        action_rank+chart_rank-combined_rank)
    stabilizer_dimension = 27-action_rank
    support_preserving_generator_dimension = 27-normal_rank
    return {
        "stabilizer_dimension": stabilizer_dimension,
        "weak_basis_orbit_dimension": action_rank,
        "support_preserving_generator_dimension":
            support_preserving_generator_dimension,
        "sparse_support_orbit_intersection_tangent_dimension":
            support_preserving_generator_dimension-stabilizer_dimension,
        "action_rank_gap": action_gap,
        "support_constraint_rank_gap": normal_gap,
        "gauge_fixed_boundary_chart_dimension": chart_rank,
        "gauge_fixed_chart_weak_basis_orbit_intersection_dimension":
            chart_orbit_intersection_dimension,
        "chart_rank_gap": chart_gap,
        "combined_action_chart_rank_gap": combined_gap,
    }


records = []
for audit in packet["audits"]:
    chart = audit["chart"]
    face = audit["coordinate_face_continuation"]
    mu, md = chart["member"]
    edge = chart["phase_edge"]
    sides = []
    for name, key, drop_key in (
            ("source", "source_limit_log_parameters", "suppressed_edge_label"),
            ("partner", "partner_limit_log_parameters",
             "partner_vanishing_edge_label")):
        theta = np.array(face[key])
        yu, yd = build_texture(mu, md, edge[0], tuple(edge[1:]), theta)
        sector, i, j = face[drop_key]
        (yu if sector == "u" else yd)[i, j] = 0
        sides.append({"side": name, **audit_texture(yu, yd, chart)})
    records.append({"chart": chart, "sides": sides})

out = {
    "schema": "marici.flavor.boundary_weak_basis_stabilizer.v1",
    "status": "complete_lie_algebra_rank_audit",
    "boundary_texture_count": 2*len(records),
    "stabilizer_dimensions": sorted({
        side["stabilizer_dimension"]
        for record in records for side in record["sides"]}),
    "sparse_support_orbit_intersection_tangent_dimensions": sorted({
        side["sparse_support_orbit_intersection_tangent_dimension"]
        for record in records for side in record["sides"]}),
    "gauge_fixed_chart_weak_basis_orbit_intersection_dimensions": sorted({
        side["gauge_fixed_chart_weak_basis_orbit_intersection_dimension"]
        for record in records for side in record["sides"]}),
    "records": records,
}
(RESULTS / "wp10_boundary_weak_basis_stabilizer.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
