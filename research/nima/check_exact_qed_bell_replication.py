"""Independent-precision and refined-angle replication of the exact QED Bell onset."""

import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def root_worker(dps):
    import mpmath as mp
    from check_exact_qed_bell_onset import bisect_onset, g2

    mp.mp.dps = dps
    g2.cache_clear()
    lo, hi, flo, fhi = bisect_onset(mp.mpf("0.4"), mp.mpf("0.5"), iterations=40)
    return {
        "dps": dps,
        "lo": str(lo),
        "hi": str(hi),
        "midpoint": str((lo + hi) / 2),
        "residual_lo": str(flo),
        "residual_hi": str(fhi),
    }


def angle_worker(item):
    y, k, denominator, dps = item
    import mpmath as mp
    from check_exact_qed_bell_onset import bell, g2

    mp.mp.dps = dps
    g2.cache_clear()
    x = mp.mpf(k) / denominator
    return k, str(x), str(bell(mp.mpf(y), x))


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as pool:
        roots = list(pool.map(root_worker, (35, 55)))

    root_delta = abs(float(roots[0]["midpoint"]) - float(roots[1]["midpoint"]))
    assert root_delta < 2e-12

    denominator = 256
    tasks = [
        (y, k, denominator, 35)
        for y in ("0.4", "0.43")
        for k in range(1, denominator // 2 + 1)
    ]
    with ProcessPoolExecutor(max_workers=8) as pool:
        raw = list(pool.map(angle_worker, tasks, chunksize=1))

    angular = {}
    block = denominator // 2
    for index, y in enumerate(("0.4", "0.43")):
        rows = raw[index * block : (index + 1) * block]
        values = [(int(k), float(v)) for k, _, v in rows]
        monotone = all(values[i][1] >= values[i + 1][1] for i in range(len(values) - 1))
        assert monotone
        angular[y] = {
            "grid": f"x=k/{denominator}, 1<=k<={block}; reflection supplies the other half",
            "sample_count_half_interval": block,
            "monotone_toward_transverse": monotone,
            "minimum": {"x": rows[-1][1], "bell": rows[-1][2]},
            "maximum": {"x": rows[0][1], "bell": rows[0][2]},
            "smallest_adjacent_drop": str(min(values[i][1] - values[i + 1][1] for i in range(len(values) - 1))),
        }

    payload = {
        "schema": "marici.exact-qed-bell-replication.v1",
        "precision_replications": roots,
        "root_midpoint_float_delta": str(root_delta),
        "refined_angular_census": angular,
        "verdict": "The onset is stable under independent 35- and 55-digit evaluations, and the exact Bell magnitude decreases monotonically toward the transverse minimum on a 128-point half-angle grid immediately below and above onset.",
        "scope": "This is a replicated numerical certificate, not a continuum interval proof.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-bell-replication.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"precision_replicated": True, "angular_points": 2 * block, "sha256": payload["content_sha256"]}))
