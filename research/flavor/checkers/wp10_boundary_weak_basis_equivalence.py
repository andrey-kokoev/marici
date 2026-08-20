"""Construct explicit U(3)^3 intertwiners for limiting boundary arrows."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution, least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wp7_ensemble import build_texture  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
packet = json.loads(
    (RESULTS / "wp10_regular_multisheet_fiber.json").read_text())


def phase_alignment(va, vb):
    # Solve P Va = Vb D with diagonal unitary P,D; fix P_0=1.
    def residual(z):
        p = np.exp(1j*np.r_[0.0, z[:2]])
        d = np.exp(1j*z[2:])
        error = p[:, None]*va-vb*d[None, :]
        return np.r_[error.real.ravel(), error.imag.ravel()]
    solve = least_squares(
        residual, np.zeros(5), xtol=1e-14, ftol=1e-14, gtol=1e-14,
        max_nfev=5000)
    p = np.exp(1j*np.r_[0.0, solve.x[:2]])
    d = np.exp(1j*solve.x[2:])
    return p, d, float(np.linalg.norm(residual(solve.x)))


def stabilizer_matrices(rh, alpha, beta):
    right = rh.conj().T
    q = np.exp(1j*alpha)*np.eye(3)
    wd_h = np.exp(-1j*alpha)*np.eye(3)
    phases = np.array([
        np.exp(-1j*alpha), np.exp(-1j*alpha), np.exp(-1j*beta)])
    wu_h = right@np.diag(phases)@right.conj().T
    return q, wu_h, wd_h


def double_coset_chordal(q, wu_h, wd_h, rhua, rhub):
    identity = np.eye(3)
    def objective(z):
        hs_q, hs_u, hs_d = stabilizer_matrices(rhua, z[0], z[1])
        ht_q, ht_u, ht_d = stabilizer_matrices(rhub, z[2], z[3])
        # Composition for Y -> Q Y W^dagger reverses order in W^dagger.
        tq = ht_q@q@hs_q
        tu = hs_u@wu_h@ht_u
        td = hs_d@wd_h@ht_d
        return float(
            np.linalg.norm(tq-identity)**2
            +np.linalg.norm(tu-identity)**2
            +np.linalg.norm(td-identity)**2)
    solves = [
        differential_evolution(
            objective, [(-np.pi, np.pi)]*4, seed=seed, tol=1e-11,
            polish=True, workers=1)
        for seed in (17, 29, 43)
    ]
    distances = [float(np.sqrt(solve.fun)) for solve in solves]
    best = solves[int(np.argmin(distances))]
    return (min(distances), [float(value) for value in best.x],
            max(distances)-min(distances))


records = []
for audit in packet["audits"]:
    chart = audit["chart"]
    face = audit["coordinate_face_continuation"]
    a = np.array(face["source_limit_log_parameters"])
    b = np.array(face["partner_limit_log_parameters"])
    mu, md = chart["member"]
    edge = chart["phase_edge"]
    yau, yad = build_texture(mu, md, edge[0], tuple(edge[1:]), a)
    ybu, ybd = build_texture(mu, md, edge[0], tuple(edge[1:]), b)
    lua, sua, rhua = np.linalg.svd(yau)
    lda, sda, rhda = np.linalg.svd(yad)
    lub, sub, rhub = np.linalg.svd(ybu)
    ldb, sdb, rhdb = np.linalg.svd(ybd)
    va = lua.conj().T@lda
    vb = lub.conj().T@ldb
    p, d, ckm_residual = phase_alignment(va, vb)
    q = lub@np.diag(p)@lua.conj().T
    wu_h = rhua.conj().T@np.diag(p.conj())@rhub
    wd_h = rhda.conj().T@np.diag(d.conj())@rhdb
    up_error = ybu-q@yau@wu_h
    down_error = ybd-q@yad@wd_h
    (double_coset_distance, stabilizer_parameters,
     double_coset_replication_spread) = double_coset_chordal(
         q, wu_h, wd_h, rhua, rhub)
    scale = np.sqrt(np.linalg.norm(ybu)**2+np.linalg.norm(ybd)**2)
    records.append({
        "chart": chart,
        "ckm_phase_alignment_residual": ckm_residual,
        "relative_yukawa_intertwining_residual": float(
            np.sqrt(np.linalg.norm(up_error)**2+np.linalg.norm(down_error)**2)
            /scale),
        "up_singular_value_residual": float(np.linalg.norm(sua-sub)),
        "down_singular_value_residual": float(np.linalg.norm(sda-sdb)),
        "common_left_unitarity_residual": float(
            np.linalg.norm(q.conj().T@q-np.eye(3))),
        "up_right_unitarity_residual": float(
            np.linalg.norm(wu_h@wu_h.conj().T-np.eye(3))),
        "down_right_unitarity_residual": float(
            np.linalg.norm(wd_h@wd_h.conj().T-np.eye(3))),
        "stabilizer_double_coset_minimum_chordal_distance":
            double_coset_distance,
        "minimizing_stabilizer_parameters": stabilizer_parameters,
        "double_coset_distance_three_seed_spread":
            double_coset_replication_spread,
    })

out = {
    "schema": "marici.flavor.boundary_weak_basis_equivalence.v1",
    "status": "explicit_unitary_intertwiner_audit",
    "arrow_count": len(records),
    "maximum_relative_yukawa_intertwining_residual": max(
        r["relative_yukawa_intertwining_residual"] for r in records),
    "maximum_unitarity_residual": max(
        max(r["common_left_unitarity_residual"],
            r["up_right_unitarity_residual"],
            r["down_right_unitarity_residual"]) for r in records),
    "stabilizer_double_coset_minimum_chordal_distances": [
        r["stabilizer_double_coset_minimum_chordal_distance"]
        for r in records],
    "maximum_double_coset_distance_three_seed_spread": max(
        r["double_coset_distance_three_seed_spread"] for r in records),
    "records": records,
}
(RESULTS / "wp10_boundary_weak_basis_equivalence.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
