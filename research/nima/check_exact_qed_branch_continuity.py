"""Regression audit for the physical (w,z) branches in exact one-loop QED."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import bell, solve_wz


mp.mp.dps = 35


def branch_defect(xi, xj, w, z):
    if xi < 0 and xj < 0:
        return max(abs(mp.im(w)), abs(mp.im(z)))
    if xi > 0 and xj < 0:
        return abs(z - w / abs(w) ** 2)
    return abs(z + mp.conj(w))


if __name__ == "__main__":
    rows = []
    for x in map(mp.mpf, ("0.1", "0.2", "0.3")):
        previous = None
        for y in map(mp.mpf, ("0.5", "0.6", "0.7", "0.8", "0.9")):
            triples = (
                (y, -y * x),
                (-y * x, -y * (1 - x)),
                (-y * (1 - x), y),
            )
            defects = []
            for xi, xj in triples:
                w, z = solve_wz(xi, xj)
                defects.append(branch_defect(xi, xj, w, z))
            value = bell(y, x)
            jump = mp.mpf(0) if previous is None else abs(value - previous)
            rows.append(
                {
                    "x": str(x),
                    "y": str(y),
                    "bell": str(value),
                    "adjacent_energy_jump": str(jump),
                    "maximum_branch_relation_defect": str(max(defects)),
                }
            )
            previous = value

    max_defect = max(mp.mpf(row["maximum_branch_relation_defect"]) for row in rows)
    max_jump = max(mp.mpf(row["adjacent_energy_jump"]) for row in rows)
    assert max_defect < mp.mpf("1e-20")
    assert max_jump < mp.mpf("0.02")
    payload = {
        "schema": "marici.exact-one-loop-qed-branch-continuity.v1",
        "source": "arXiv:2312.16966v2 below-threshold Regions I-III",
        "rows": rows,
        "maximum_branch_relation_defect": str(max_defect),
        "maximum_adjacent_energy_jump": str(max_jump),
        "verdict": "All three crossed master-integral evaluations remain on their prescribed physical branches; the previously observed discontinuities are absent.",
        "scope": "Bounded regression grid, not a continuum or interval-arithmetic proof.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-branch-continuity.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "max_defect": str(max_defect), "max_jump": str(max_jump)}))
