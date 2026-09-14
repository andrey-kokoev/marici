#!/usr/bin/env python3
"""Exact-rank and numerical-margin study for finite shell probes."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/voevodsky/apparatus_conditioned_shell_probe_cutoff_study.md"
RESULT = ROOT / "research/voevodsky/results/apparatus_conditioned_shell_probe_cutoffs.json"
CUTOFFS = (70, 120, 240, 480, 522, 525, 960)
SETTINGS = ((5, 6), (3, 4), (7, 10), (2, 3))
MODULI = (1000000007, 1000000009)


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def graph(cutoff):
    ps = primes_upto(cutoff // 2 + 2)
    edges = []
    for shell0, (p, q) in enumerate(zip(ps, ps[1:])):
        for k in range(1, cutoff // (p * q) + 1):
            edges.append((k * p * q, shell0 + 1, k, k * p, k * q))
    edges.sort()
    vertices = sorted({e[3] for e in edges} | {e[4] for e in edges})
    vi = {v: i for i, v in enumerate(vertices)}
    boundary = np.zeros((len(vertices), len(edges)), dtype=float)
    for col, edge in enumerate(edges):
        boundary[vi[edge[3]], col] = -1.0
        boundary[vi[edge[4]], col] = 1.0
    return edges, vertices, vi, boundary


def sparse_rows(edges, vertices, vi, modulus, setting=None):
    rows = [{} for _ in vertices]
    for col, edge in enumerate(edges):
        if setting is None:
            weight = 1
        else:
            numerator, denominator = setting
            tmod = numerator * pow(denominator, modulus - 2, modulus) % modulus
            weight = pow(tmod, edge[1], modulus)
        for index, sign in ((vi[edge[3]], -1), (vi[edge[4]], 1)):
            rows[index][col] = sign * weight % modulus
    return rows


def rank_mod(rows, modulus):
    basis = {}
    for source in rows:
        row = {k: v % modulus for k, v in source.items() if v % modulus}
        while row:
            lead = min(row)
            if lead not in basis:
                inv = pow(row[lead], modulus - 2, modulus)
                row = {k: v * inv % modulus for k, v in row.items() if v * inv % modulus}
                basis[lead] = row
                break
            factor = row[lead]
            for k, v in basis[lead].items():
                value = (row.get(k, 0) - factor * v) % modulus
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
    return len(basis)


def null_basis(boundary):
    _, singular, vh = np.linalg.svd(boundary, full_matrices=True)
    tolerance = max(boundary.shape) * np.finfo(float).eps * (singular[0] if singular.size else 1.0)
    rank = int(np.sum(singular > tolerance))
    return vh[rank:].T, rank, tolerance


checks = {}
census = {}
for cutoff in CUTOFFS:
    edges, vertices, vi, boundary = graph(cutoff)
    F, numerical_boundary_rank, boundary_tolerance = null_basis(boundary)
    exact_by_count = []
    numerical_by_count = []
    previous_sigma_min = 0.0
    stacked_blocks = []
    base_rows = {p: sparse_rows(edges, vertices, vi, p) for p in MODULI}
    for count, setting in enumerate(SETTINGS, 1):
        numerator, denominator = setting
        t = numerator / denominator
        weights = np.array([t**edge[1] for edge in edges])
        stacked_blocks.append(boundary @ (weights[:, None] * F))
        response = np.vstack(stacked_blocks)
        singular = np.linalg.svd(response, compute_uv=False)
        sigma_max = float(singular[0]) if singular.size else 0.0
        sigma_min = float(singular[-1]) if singular.size else 0.0
        numerical_rank_tol = max(response.shape) * np.finfo(float).eps * max(sigma_max, 1.0)
        numerical_rank = int(np.sum(singular > numerical_rank_tol))
        ranks = []
        for modulus in MODULI:
            rows = list(base_rows[modulus])
            for used in SETTINGS[:count]:
                rows += sparse_rows(edges, vertices, vi, modulus, used)
            ranks.append(rank_mod(rows, modulus))
        exact_full = all(rank == len(edges) for rank in ranks)
        checks[f"modular_ranks_agree_{cutoff}_{count}"] = len(set(ranks)) == 1
        checks[f"exact_numeric_status_agrees_{cutoff}_{count}"] = exact_full == (numerical_rank == F.shape[1])
        checks[f"cumulative_margin_monotone_{cutoff}_{count}"] = sigma_min + 1e-12 >= previous_sigma_min
        previous_sigma_min = max(previous_sigma_min, sigma_min)
        exact_by_count.append({"setting_count": count, "joint_ranks": ranks, "full_edge_rank": exact_full})
        numerical_by_count.append({
            "setting_count": count,
            "response_rank": numerical_rank,
            "cycle_dimension": int(F.shape[1]),
            "sigma_min": sigma_min,
            "sigma_max": sigma_max,
            "condition_number": sigma_max / sigma_min if sigma_min > numerical_rank_tol else None,
            "rank_tolerance": numerical_rank_tol,
        })
    jmax = max((edge[1] for edge in edges), default=0)
    dynamic = []
    for numerator, denominator in SETTINGS:
        t = numerator / denominator
        factor = t**jmax if jmax else 1.0
        dynamic.append({
            "t": f"{numerator}/{denominator}",
            "j_max": jmax,
            "minimum_shell_factor": factor,
            "amplitude_db": 20.0 * math.log10(factor),
        })
    first_full = next((item["setting_count"] for item in exact_by_count if item["full_edge_rank"]), None)
    census[str(cutoff)] = {
        "vertices": len(vertices),
        "edges": len(edges),
        "shell_count": jmax,
        "cycle_dimension": int(F.shape[1]),
        "numerical_boundary_rank": numerical_boundary_rank,
        "boundary_svd_tolerance": boundary_tolerance,
        "first_exact_full_setting_count": first_full,
        "exact": exact_by_count,
        "numerical": numerical_by_count,
        "dynamic_range": dynamic,
    }

checks["cutoff_960_included"] = "960" in census
checks["cutoff_960_single_setting_deficient"] = not census["960"]["exact"][0]["full_edge_rank"]
checks["no_apparatus_promotion"] = "does not certify an apparatus cutoff" in PACKET.read_text()
checks = {name: bool(value) for name, value in checks.items()}
result = {
    "schema": "marici.voevodsky.apparatus-conditioned-shell-probe-cutoffs.v1",
    "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest(),
    "settings": [f"{a}/{b}" for a, b in SETTINGS],
    "coordinate_norm": "Euclidean ordered edge and vertex coordinates",
    "checks": checks,
    "passed": all(checks.values()),
    "census": census,
    "disposition": {
        "mathematical_output": "finite exact ranks and coordinate singular margins",
        "physical_cutoff": "pending measured KrakenSDR transfer, calibration-error, and joint-noise bounds",
        "acceptance_rule": "sigma_min exceeds apparatus operator-error bound in matching normalized coordinates",
    },
}
RESULT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "passed": result["passed"],
    "checks": len(checks),
    "first_full_counts": {k: v["first_exact_full_setting_count"] for k, v in census.items()},
    "cutoff_960_sigma_min": census["960"]["numerical"][-1]["sigma_min"],
}))
raise SystemExit(0 if result["passed"] else 1)
