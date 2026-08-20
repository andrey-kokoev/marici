"""Construct a three-object sparse weak-basis groupoid composition test."""
import itertools
import json
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares, minimize_scalar

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wp7_ensemble import build_texture, observables17, SIGMA  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ensemble = json.loads((RESULTS / "wp7_ensemble.json").read_text())


def matrices(record):
    edge = record["phase_edge"]
    theta = np.array(record["log_mags"]+[record["phi"]])
    return build_texture(
        *record["member"], edge[0], tuple(edge[1:]), theta)


def phase_alignment(va, vb):
    def residual(z):
        p = np.exp(1j*np.r_[0.0, z[:2]])
        d = np.exp(1j*z[2:])
        error = p[:, None]*va-vb*d[None, :]
        return np.r_[error.real.ravel(), error.imag.ravel()]
    rng = np.random.default_rng(1701)
    starts = [np.zeros(5)]+[
        rng.uniform(-np.pi, np.pi, 5) for _ in range(24)]
    solves = [
        least_squares(
            residual, start, xtol=1e-14, ftol=1e-14, gtol=1e-14,
            max_nfev=5000)
        for start in starts
    ]
    solve = min(solves, key=lambda item: np.linalg.norm(residual(item.x)))
    return (np.exp(1j*np.r_[0.0, solve.x[:2]]),
            np.exp(1j*solve.x[2:]), float(np.linalg.norm(residual(solve.x))))


def arrow(ya, yb):
    yau, yad = ya
    ybu, ybd = yb
    lua, _, rhua = np.linalg.svd(yau)
    lda, _, rhda = np.linalg.svd(yad)
    lub, _, rhub = np.linalg.svd(ybu)
    ldb, _, rhdb = np.linalg.svd(ybd)
    p, d, phase_residual = phase_alignment(
        lua.conj().T@lda, lub.conj().T@ldb)
    result = (
        lub@np.diag(p)@lua.conj().T,
        rhua.conj().T@np.diag(p.conj())@rhub,
        rhda.conj().T@np.diag(d.conj())@rhdb,
    )
    mapped_u = result[0]@yau@result[1]
    mapped_d = result[0]@yad@result[2]
    scale = np.sqrt(np.linalg.norm(ybu)**2+np.linalg.norm(ybd)**2)
    return result, {
        "phase_alignment_residual": phase_residual,
        "relative_yukawa_residual": float(
            np.sqrt(np.linalg.norm(mapped_u-ybu)**2
                    +np.linalg.norm(mapped_d-ybd)**2)/scale),
    }


points = []
for orbit in ensemble["orbits"]:
    for record in orbit["viable_minima"]:
        yu, yd = matrices(record)
        points.append({
            "orbit": orbit["orbit_index"],
            "record": record,
            "chart": (
                orbit["orbit_index"], tuple(record["member"]),
                tuple(record["phase_edge"])),
            "matrices": (yu, yd),
            "obs": observables17(yu, yd)/SIGMA,
        })

best = None
for triple in itertools.combinations(points, 3):
    if len({point["chart"] for point in triple}) < 3:
        continue
    separations = [
        float(np.max(np.abs(triple[i]["obs"]-triple[j]["obs"])))
        for i, j in ((0, 1), (1, 2), (0, 2))
    ]
    score = max(separations)
    if best is None or score < best[0]:
        best = (score, triple, separations)

score, triple, separations = best
g01, a01 = arrow(triple[0]["matrices"], triple[1]["matrices"])
g12, a12 = arrow(triple[1]["matrices"], triple[2]["matrices"])
g02, a02 = arrow(triple[0]["matrices"], triple[2]["matrices"])
composed = (
    g12[0]@g01[0],
    g01[1]@g12[1],
    g01[2]@g12[2],
)

def closure_objective(alpha):
    return float(
        np.linalg.norm(np.exp(1j*alpha)*composed[0]-g02[0])**2
        +np.linalg.norm(np.exp(-1j*alpha)*composed[1]-g02[1])**2
        +np.linalg.norm(np.exp(-1j*alpha)*composed[2]-g02[2])**2)

closure = minimize_scalar(
    closure_objective, bounds=(-np.pi, np.pi), method="bounded",
    options={"xatol": 1e-14})

yu0, yd0 = triple[0]["matrices"]
yu2, yd2 = triple[2]["matrices"]
mapped_u = composed[0]@yu0@composed[1]
mapped_d = composed[0]@yd0@composed[2]
action_residual = float(
    np.sqrt(np.linalg.norm(mapped_u-yu2)**2
            +np.linalg.norm(mapped_d-yd2)**2)
    /np.sqrt(np.linalg.norm(yu2)**2+np.linalg.norm(yd2)**2))

out = {
    "schema": "marici.flavor.weak_basis_groupoid_composition.v1",
    "status": "three_object_composition_audit",
    "triple": [{
        "orbit": point["orbit"],
        "member": point["record"]["member"],
        "phase_edge": point["record"]["phase_edge"],
        "phi_folded": point["record"]["phi_folded"],
    } for point in triple],
    "pairwise_max_observable_separation_sigma": separations,
    "maximum_pairwise_observable_separation_sigma": score,
    "pairwise_arrow_audits": [a01, a12, a02],
    "composed_action_relative_yukawa_residual": action_residual,
    "direct_vs_composed_mod_common_stabilizer_chordal_residual":
        float(np.sqrt(closure.fun)),
    "minimizing_common_stabilizer_phase": float(closure.x),
}
(RESULTS / "wp10_weak_basis_groupoid_composition.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
