"""Discovery-only real-Euclidean feasibility search for reduced C8 companion walls."""

import json
import math
import os
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import least_squares


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-feasibility.json"
SYMBOLS = sp.symbols("a b c d z k l")


def routing_eigenvalues(k: float, l: float) -> list[float]:
    return [
        2
        + 3 * math.cos(math.pi * j / 4)
        + math.cos(math.pi * j / 2)
        + 2 * k * math.cos(3 * math.pi * j / 4)
        + l * ((-1) ** j)
        for j in range(8)
    ]


def companion(det: sp.Expr) -> sp.Expr:
    factors = sp.factor_list(det)[1]
    supports = [(len(sp.Add.make_args(factor)), factor) for factor, _ in factors]
    largest = max(size for size, _ in supports)
    candidates = [factor for size, factor in supports if size == largest]
    if len(candidates) != 1 or largest < 4:
        raise RuntimeError(f"companion factor is not uniquely maximal: {supports}")
    return candidates[0]


def search(model: dict, seed: int, restarts: int) -> dict:
    equations = [sp.sympify(value) for value in model["cover_equations"]]
    wall = companion(sp.sympify(model["jacobian_determinant"]))
    functions = sp.lambdify(SYMBOLS, equations + [wall], "numpy")
    rng = np.random.default_rng(seed)
    best = None
    psd_weight = float(os.environ.get("MARICI_PSD_WEIGHT", "10"))

    def residual(x: np.ndarray) -> np.ndarray:
        values = np.asarray(functions(*x), dtype=float).reshape(5)
        eig = routing_eigenvalues(float(x[5]), float(x[6]))
        return np.concatenate((values, psd_weight * np.minimum(0.0, eig)))

    lower = np.array([1e-3] * 5 + [-2.0, -2.0])
    upper = np.array([6.0] * 5 + [2.0, 2.0])
    for _ in range(restarts):
        x0 = np.concatenate((rng.uniform(0.1, 3.0, 5), rng.uniform(-0.8, 0.3, 2)))
        fit = least_squares(residual, x0, bounds=(lower, upper), max_nfev=4000)
        raw = np.asarray(functions(*fit.x), dtype=float).reshape(5)
        eig = np.asarray(routing_eigenvalues(float(fit.x[5]), float(fit.x[6])))
        score = max(float(np.max(np.abs(raw))), max(0.0, -float(np.min(eig))))
        if best is None or score < best[0]:
            best = (score, fit.x.copy(), raw, eig, fit.nfev)
    score, point, raw, eig, nfev = best
    return {
        "model": model["name"],
        "discovery_only": True,
        "feasible_candidate": bool(score < 1e-8 and min(point[:5]) > 1e-4),
        "score": score,
        "point": dict(zip(("a", "b", "c", "d", "z", "k", "l"), point.tolist())),
        "equation_residuals": raw.tolist(),
        "routing_eigenvalues": eig.tolist(),
        "minimum_routing_eigenvalue": float(np.min(eig)),
        "companion_factor": str(wall),
        "nfev": int(nfev),
        "psd_weight": psd_weight,
    }


def psd_grid_search(model: dict, seed: int, samples: int) -> dict:
    equations = [sp.sympify(value) for value in model["cover_equations"]]
    wall = companion(sp.sympify(model["jacobian_determinant"]))
    functions = sp.lambdify(SYMBOLS, equations + [wall], "numpy")
    rng = np.random.default_rng(seed)
    best = None
    accepted = 0
    while accepted < samples:
        k, l = rng.uniform(-2.0, 2.0, 2)
        eig = np.asarray(routing_eigenvalues(float(k), float(l)))
        if np.min(eig) < 1e-8:
            continue
        accepted += 1

        def residual(edges: np.ndarray) -> np.ndarray:
            return np.asarray(functions(*edges, k, l), dtype=float).reshape(5)

        for _ in range(3):
            x0 = rng.uniform(0.05, 4.0, 5)
            fit = least_squares(residual, x0, bounds=(1e-3, 8.0), max_nfev=2500)
            raw = residual(fit.x)
            score = float(np.max(np.abs(raw)))
            if best is None or score < best[0]:
                best = (score, fit.x.copy(), raw, eig, k, l)
    score, edges, raw, eig, k, l = best
    return {
        "model": model["name"],
        "psd_samples": samples,
        "feasible_candidate": bool(score < 1e-8 and min(edges) > 1e-4),
        "score": score,
        "point": dict(zip(("a", "b", "c", "d", "z", "k", "l"), [*edges.tolist(), k, l])),
        "equation_residuals": raw.tolist(),
        "routing_eigenvalues": eig.tolist(),
    }


def main() -> None:
    packet = json.loads(SOURCE.read_text())
    restarts = int(os.environ.get("MARICI_RESTARTS", "80"))
    results = [search(model, 8191 + index * 104729, restarts) for index, model in enumerate(packet["models"])]
    psd_samples = int(os.environ.get("MARICI_PSD_SAMPLES", "250"))
    grid_results = [psd_grid_search(model, 65537 + index * 524287, psd_samples) for index, model in enumerate(packet["models"])]
    output = {
        "schema": "marici.eight_site_companion_feasibility.discovery.v1",
        "restarts_per_model": restarts,
        "status": "discovery_only_not_a_certificate",
        "models": results,
        "fixed_psd_models": grid_results,
    }
    TARGET.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"models": len(results), "joint_candidates": sum(item["feasible_candidate"] for item in results), "fixed_psd_candidates": sum(item["feasible_candidate"] for item in grid_results)}))


if __name__ == "__main__":
    main()
