"""High-precision hostile reconnaissance for the far-wall remainder ratio."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "primitive-fourth-cumulant-transfer-normal-form.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "primitive_fourth_cumulant_remainder_recon.json"
)

mp.mp.dps = 60


def raw_log_moments(t: mp.mpf, q: mp.mpf) -> tuple[mp.mpf, ...]:
    def integrand(y: mp.mpf, order: int) -> mp.mpf:
        if y == 0:
            return mp.mpf("0")
        h = mp.log1p(t * y) / t
        weight = (
            mp.exp(-y)
            * (1 + t * (y - mp.mpf(3) / 2))
            * mp.power(1 + t * y, mp.mpf(1) / 4)
            * mp.power(h, q)
        )
        return weight * mp.power(mp.log(h), order)

    return tuple(
        mp.quad(lambda y: integrand(y, order), [0, 1, mp.inf])
        for order in range(4)
    )


def cumulants(raw: tuple[mp.mpf, ...]) -> tuple[mp.mpf, ...]:
    mean = raw[1] / raw[0]
    second = raw[2] / raw[0]
    third = raw[3] / raw[0]
    variance = second - mean**2
    skew = third - 3 * mean * second + 2 * mean**3
    return mean, variance, skew


def margin(t: mp.mpf, q: mp.mpf) -> mp.mpf:
    mean_q, variance_q, skew_q = cumulants(raw_log_moments(t, q))
    mean_minus, variance_minus, skew_minus = cumulants(
        raw_log_moments(t, q - 1)
    )
    d = mean_q - mean_minus
    variance_step = variance_minus - variance_q
    skew_step = skew_q - skew_minus
    A = 1 - q * d
    b = variance_step / d**2
    c = skew_step / d**3
    return 2 + A + 3 * A * b - (1 - A) * c


def truncation(t: mp.mpf, q: mp.mpf) -> mp.mpf:
    a3 = 4 * q**3
    a4 = -q**3 * (92 * q - 53) / 4
    a5 = q**3 * (1520 * q**2 - 776 * q + 297) / 16
    return a3 * t**3 + a4 * t**4 + a5 * t**5


wall_values = (60, 75, 100, 150, 200)
q_values = tuple(mp.mpf(4) + mp.mpf(index) / 2 for index in range(13))
samples = []
for wall in wall_values:
    t = mp.mpf(1) / wall
    for q in q_values:
        actual = margin(t, q)
        truncated = truncation(t, q)
        remainder = actual - truncated
        reserve = mp.mpf(5) * q**3 * t**3 / 2
        samples.append(
            {
                "wall_c": wall,
                "q": float(q),
                "margin": mp.nstr(actual, 20),
                "remainder": mp.nstr(remainder, 20),
                "reserve": mp.nstr(reserve, 20),
                "absolute_remainder_over_reserve": float(
                    abs(remainder) / reserve
                ),
            }
        )

worst = max(samples, key=lambda item: item["absolute_remainder_over_reserve"])
rows_by_wall = {
    wall: sorted(
        (item for item in samples if item["wall_c"] == wall),
        key=lambda item: item["q"],
    )
    for wall in wall_values
}
rows_by_q = {
    float(q): sorted(
        (item for item in samples if item["q"] == float(q)),
        key=lambda item: item["wall_c"],
        reverse=True,
    )
    for q in q_values
}
q_ratio_steps = [
    row[index + 1]["absolute_remainder_over_reserve"]
    - row[index]["absolute_remainder_over_reserve"]
    for row in rows_by_wall.values()
    for index in range(len(row) - 1)
]
t_ratio_steps = [
    row[index + 1]["absolute_remainder_over_reserve"]
    - row[index]["absolute_remainder_over_reserve"]
    for row in rows_by_q.values()
    for index in range(len(row) - 1)
]
checks = {
    "all_sampled_remainders_have_order_six_orientation": all(
        mp.mpf(item["remainder"]) < 0 for item in samples
    ),
    "all_sampled_remainders_fit_inside_proved_reserve": all(
        item["absolute_remainder_over_reserve"] < 1 for item in samples
    ),
    "remainder_ratio_is_largest_at_declared_near_corner": (
        worst["wall_c"] == 60 and worst["q"] == 10.0
    ),
    "sampled_remainder_ratio_increases_with_q": min(q_ratio_steps) > 0,
    "sampled_remainder_ratio_increases_with_t": min(t_ratio_steps) > 0,
    "high_precision_reconnaissance_is_not_reported_as_proof": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "decimal_precision": mp.mp.dps,
        "wall_values": wall_values,
        "q_grid": {"minimum": 4.0, "maximum": 10.0, "step": 0.5},
        "sample_count": len(samples),
        "worst_sample": worst,
        "smallest_positive_q_ratio_step": min(q_ratio_steps),
        "smallest_positive_t_ratio_step": min(t_ratio_steps),
        "samples": samples,
        "status": "high_precision_reconnaissance_only",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "The transformed fixed-measure quadrature is hostile discovery "
        "evidence. It is not interval arithmetic and does not prove a "
        "uniform remainder bound."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
