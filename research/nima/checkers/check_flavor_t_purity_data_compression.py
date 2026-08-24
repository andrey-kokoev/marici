"""Does the texture ensemble sharpen t-purity beyond fitted OBS17 data?"""

import cmath
import glob
import json
import math
import sys
from pathlib import Path

import numpy as np

flavor_root = Path(__file__).parents[2] / "flavor"
sys.path.insert(0, str(flavor_root / "checkers"))
import wp7_ensemble as wp7


def ckm(s12, s13, s23, delta):
    c12, c13, c23 = (math.sqrt(1 - x * x) for x in (s12, s13, s23))
    phase = cmath.exp(1j * delta)
    return (
        (c12 * c13, s12 * c13, s13 / phase),
        (-s12 * c23 - c12 * s23 * s13 * phase,
         c12 * c23 - s12 * s23 * s13 * phase, s23 * c13),
        (s12 * s23 - c12 * c23 * s13 * phase,
         -c12 * s23 - s12 * c23 * s13 * phase, c23 * c13),
    )


def invert(row, masses):
    e1 = sum(masses)
    e2 = sum(masses[i] * masses[j] for i in range(3) for j in range(i + 1, 3))
    e3 = math.prod(masses)
    weights = [abs(z) ** 2 for z in row]
    d0 = sum(weights[i] * masses[i] for i in range(3))
    beta = e3 * sum(weights[i] / masses[i] for i in range(3))
    d1 = (beta * d0 - e3) / ((e1 - d0) * d0 - e2 + beta)
    p0 = math.prod(d0 - x for x in masses)
    p1 = math.prod(d1 - x for x in masses)
    return p0 / (d1 - d0), p1 / (d0 - d1)


def ft_from_obs(values):
    yu, yc, _yt, yd, ys, yb, vus, vub, vcb = values[:9]
    gamma = math.radians(values[14])
    s13 = vub
    c13 = math.sqrt(1 - s13 * s13)
    s12, s23 = vus / c13, vcb / c13
    v = ckm(s12, s13, s23, gamma)
    a = [[abs(z) for z in row] for row in v]
    ratio = -(v[0][0] * v[0][2].conjugate()) / (v[1][0] * v[1][2].conjugate())
    sin_gamma = abs(math.sin(cmath.phase(ratio)))
    down = (yd * yd, ys * ys, yb * yb)
    edge02, edge12 = invert(v[2], down)
    dd = (down[2] - down[1]) * (down[2] - down[0]) * (down[1] - down[0])
    triple = a[0][0] * a[1][0] * a[1][2] ** 2 * sin_gamma
    return ((yc * yc - yu * yu) * dd * triple
            / (yc * yc * edge02 * math.sqrt(edge12)))


sheet_values = []
for path in sorted(glob.glob(str(flavor_root / "results" / "wp15b_dense_orbit*.json"))):
    data = json.load(open(path, encoding="utf-8"))
    for half in data["s3_orbits"]:
        for member_result in half["member_results"]:
            member = tuple(member_result["member"])
            for minimum in member_result["viable_minima"]:
                if minimum["chi2"] >= 4:
                    continue
                phase_edge = minimum["phase_edge"]
                theta = np.array(minimum["log_mags"] + [minimum["phi"]])
                yu, yd = wp7.build_texture(member[0], member[1], phase_edge[0],
                                            (phase_edge[1], phase_edge[2]), theta)
                obs = wp7.observables17(yu, yd)
                if np.all(np.isfinite(obs)):
                    sheet_values.append(ft_from_obs(obs))

rng = np.random.default_rng(2092)
null_values = []
while len(null_values) < 12100:
    direction = rng.normal(size=len(wp7.CENTRAL))
    direction /= np.linalg.norm(direction)
    radius = 2 * rng.random() ** (1 / len(wp7.CENTRAL))
    sample = wp7.CENTRAL + radius * direction * wp7.SIGMA
    try:
        value = ft_from_obs(sample)
    except (ValueError, ZeroDivisionError):
        continue
    if math.isfinite(value):
        null_values.append(value)

sheets = np.array(sheet_values)
null = np.array(null_values)
sheet_std, null_std = float(sheets.std()), float(null.std())
sheet_mean, null_mean = float(sheets.mean()), float(null.mean())
checks = {
    "all_1210_viable_sheets_recovered": len(sheets) == 1210,
    "texture_ensemble_is_more_concentrated": sheet_std < 0.5 * null_std,
    "sheet_mean_not_distinctly_shifted_from_null_median": abs(sheet_mean - float(np.median(null))) < null_std,
    "all_sheet_values_remain_below_one": float(sheets.max()) < 1,
}
report = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "sheet_count": len(sheets),
    "null_count": len(null),
    "null_region": "uniform OBS17 chi-square ball with radius 2",
    "sheet_mean": sheet_mean,
    "sheet_std": sheet_std,
    "sheet_range": [float(sheets.min()), float(sheets.max())],
    "null_mean": null_mean,
    "null_std": null_std,
    "null_quantiles_16_50_84": [float(x) for x in np.quantile(null, [0.16, 0.5, 0.84])],
    "concentration_ratio": sheet_std / null_std,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
