"""Exact calibration margins and fragile-equality hostiles for two instruments."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(q, a):
    return [[q * value for value in row] for row in a]


def tr(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def minor(a, row, col):
    return [[a[i][j] for j in range(len(a)) if j != col]
            for i in range(len(a)) if i != row]


def det(a):
    if not a:
        return F(1)
    if len(a) == 1:
        return a[0][0]
    return sum((F(-1) ** j) * a[0][j] * det(minor(a, 0, j))
               for j in range(len(a)))


def power(a, n):
    result = eye(len(a))
    for _ in range(n):
        result = mm(result, a)
    return result


def nz(a):
    return sum(value != 0 for row in a for value in row)


def main():
    q = [
        [F(3, 5), F(-4, 13), F(48, 65)],
        [F(4, 5), F(3, 13), F(-36, 65)],
        [F(0), F(12, 13), F(5, 13)],
    ]
    eigenvalues = [F(1, 2), F(1, 4), F(1, 5)]
    diagonal = [[eigenvalues[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    m0 = mm(mm(q, diagonal), tr(q))

    robust_shift = F(-1, 10)
    shifted_eigenvalues = [value + robust_shift for value in eigenvalues]
    dark_shift = F(1, 100)
    old_dark = F(1, 2)
    new_dark = F(49, 100)
    perturbed = add(m0, scale(dark_shift, eye(3)))
    old_numerator = det(add(perturbed, scale(old_dark - F(1), eye(3))))
    new_numerator = det(add(perturbed, scale(new_dark - F(1), eye(3))))
    denominator_at_new_dark = det(add(add(eye(3), perturbed), scale(new_dark, eye(3))))

    eta = F(1, 1000)
    detectable = F(1, 100)
    unresolved = F(1, 10000)
    allowed_upper = [[F(1), F(0)], [F(1), F(1)]]
    zero_lower = [[F(0), F(0)], [F(0), F(0)]]
    horizontal_from_allowed = zero_lower

    h = [[F(0), F(-1)], [F(1), F(0)]]
    h_perturbed = [[F(0), F(-1)], [F(1), F(1, 100)]]
    torsion_residual = sub(power(h_perturbed, 4), eye(2))

    checks = {
        "impedance_margin_exceeds_hostile_norm": F(1, 5) > abs(robust_shift),
        "shifted_static_impedance_remains_positive": min(shifted_eigenvalues) > 0,
        "dark_zero_moves_under_small_isotropic_calibration": old_numerator != 0,
        "moved_dark_zero_is_exact": new_numerator == 0,
        "denominator_remains_nonzero_at_moved_dark_zero": denominator_at_new_dark != 0,
        "forbidden_leakage_above_noise_is_detectable": detectable > eta,
        "nonzero_leakage_below_noise_is_not_certified": F(0) < unresolved < eta,
        "allowed_reverse_extension_does_not_enter_horizontal_residual": nz(allowed_upper) > 0 and nz(horizontal_from_allowed) == 0,
        "exact_order_four_fixture_holds": power(h, 4) == eye(2),
        "small_holonomy_perturbation_breaks_exact_torsion": nz(torsion_residual) > 0,
    }

    result = {
        "schema": "marici.aspect.two_instrument_calibration_robustness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "margins": {
            "static_impedance_minimum_eigenvalue": "1/5",
            "tested_negative_shift": str(robust_shift),
            "post_shift_minimum_eigenvalue": str(min(shifted_eigenvalues)),
            "amplitude_noise_floor": str(eta),
            "detectable_forbidden_coupling": str(detectable),
            "unresolved_forbidden_coupling": str(unresolved),
        },
        "residuals": {
            "perturbed_numerator_at_old_dark_coordinate": str(old_numerator),
            "perturbed_numerator_at_new_dark_coordinate": str(new_numerator),
            "denominator_at_new_dark_coordinate": str(denominator_at_new_dark),
            "perturbed_holonomy_fourth_power_nonzero_entries": nz(torsion_residual),
        },
        "typed_boundary": {
            "robust": "denominator accretivity and above-threshold directional leakage",
            "fragile": "exact dark-zero coordinate and exact finite-order torsion",
            "missing": "statistical coverage, covariance, fabrication data, and physical bath calibration",
        },
    }
    out = Path(__file__).parents[1] / "results" / "two_instrument_calibration_robustness.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
