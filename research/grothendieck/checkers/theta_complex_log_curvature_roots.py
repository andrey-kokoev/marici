"""Search complex zeros of the completed theta logarithmic curvature."""
import cmath
import json
import math
from pathlib import Path


def next_polynomial(coefficients, p):
    result = [0j] * (len(coefficients) + 1)
    for degree, coefficient in enumerate(coefficients):
        result[degree] += p * coefficient
        result[degree + 1] -= 2 * coefficient
        if degree:
            result[degree] += 2 * degree * coefficient
    return result


POLYNOMIALS = {}
for p in (2.5, 4.5):
    family = [[1 + 0j]]
    for _ in range(4):
        family.append(next_polynomial(family[-1], p))
    POLYNOMIALS[p] = family


def evaluate_polynomial(coefficients, x):
    value = 0j
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def phi_jets(u, max_label, highest=3):
    exponential_two_u = cmath.exp(2 * u)
    totals = [0j] * (highest + 1)
    for label in range(1, max_label + 1):
        c = math.pi * label * label
        x = c * exponential_two_u
        for order in range(highest + 1):
            first = 4 * c * c * cmath.exp(4.5 * u - x) * evaluate_polynomial(POLYNOMIALS[4.5][order], x)
            second = 6 * c * cmath.exp(2.5 * u - x) * evaluate_polynomial(POLYNOMIALS[2.5][order], x)
            totals[order] += first - second
    return totals


def numerator_and_derivative(u, max_label):
    phi, first, second, third = phi_jets(u, max_label, 3)
    numerator = phi * second - first * first
    derivative = phi * third - first * second
    scale = abs(phi * second) + abs(first * first)
    return numerator, derivative, scale, phi, first


def newton(seed, max_label=28, iterations=40):
    u = seed
    for _ in range(iterations):
        if not (math.isfinite(u.real) and math.isfinite(u.imag)):
            return None
        if abs(u.real) > 3 or abs(u.imag) >= 0.76:
            return None
        try:
            numerator, derivative, _, _, _ = numerator_and_derivative(u, max_label)
        except OverflowError:
            return None
        if abs(derivative) < 1e-280:
            return None
        step = numerator / derivative
        u -= step
        if abs(step) < 2e-13:
            return u
    return None


roots = []
for real_index in range(31):
    for imag_index in range(1, 30):
        seed = complex(real_index / 20, imag_index / 40)
        root = newton(seed)
        if root is None or root.real < -1e-9 or not (1e-8 < root.imag < 0.75):
            continue
        if any(abs(root - known) < 1e-8 for known in roots):
            continue
        roots.append(root)

roots.sort(key=abs)
candidates = []
for root in roots:
    checks = []
    for cutoff in (28, 36):
        numerator, derivative, scale, phi, first = numerator_and_derivative(root, cutoff)
        critical_z = -first / phi
        checks.append({
            "max_label": cutoff,
            "relative_curvature_numerator_residual": abs(numerator) / scale,
            "curvature_numerator_derivative_absolute": abs(derivative),
            "phi_absolute": abs(phi),
            "critical_z": [critical_z.real, critical_z.imag],
        })
    stable = abs(complex(*checks[0]["critical_z"]) - complex(*checks[1]["critical_z"])) < 1e-10
    candidates.append({
        "u": [root.real, root.imag],
        "absolute_u": abs(root),
        "checks": checks,
        "critical_z_stable_across_label_cutoffs": stable,
        "critical_t_from_final_cutoff": [
            (complex(*checks[-1]["critical_z"]) ** 2).real,
            (complex(*checks[-1]["critical_z"]) ** 2).imag,
        ],
    })

result = {
    "search_rectangle": {"real_u": [0, 1.5], "imag_u": [0.05, 0.7]},
    "natural_series_strip": "abs(Im u) < pi/4",
    "seed_spacing": [0.05, 0.025],
    "candidate_count": len(candidates),
    "candidates": candidates,
    "nearest_candidate": candidates[0] if candidates else None,
    "interval_certified": False,
    "search_exhaustive_or_root_count_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-complex-log-curvature-roots.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"candidate_count={len(candidates)}")
    for candidate in candidates:
        print(f"u={candidate['u']} abs_u={candidate['absolute_u']:.12g} checks={candidate['checks']}")
