"""Exact WP133 detector-uncertainty and open-world identification audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    rows, cols = len(a), len(a[0])
    p = 0
    for c in range(cols):
        pivot = next((r for r in range(p, rows) if a[r][c]), None)
        if pivot is None:
            continue
        a[p], a[pivot] = a[pivot], a[p]
        scale = a[p][c]
        a[p] = [x / scale for x in a[p]]
        for r in range(rows):
            if r != p and a[r][c]:
                factor = a[r][c]
                a[r] = [a[r][j] - factor * a[p][j] for j in range(cols)]
        p += 1
    return p


def detector(eta):
    return [[1 - eta, eta, F(0)], [eta, 1 - eta, F(0)], [F(0), F(0), F(1)]]


# WP131 reduced widths induce the frozen toy detector overlap.
gamma_hat_1, gamma_hat_2 = F(1, 25), F(1, 16)
eta = gamma_hat_1 + gamma_hat_2
calibration_uncertainty = F(1, 100)
eta_low, eta_high = eta - calibration_uncertainty, eta + calibration_uncertainty

original = [[F(1), F(0), F(0)], [F(1), F(2), F(0)], [F(0), F(0), F(1)]]
response_central = matmul(detector(eta), original)
response_low = matmul(detector(eta_low), original)
response_high = matmul(detector(eta_high), original)

# Fourth constructor: an isospectral two-adjoint source with different
# nonlinear self-coupling. It duplicates the two-point spectral column.
expanded = [
    [F(1), F(0), F(0), F(1)],
    [F(1), F(2), F(0), F(1)],
    [F(0), F(0), F(1), F(0)],
]
expanded_smeared = matmul(detector(eta), expanded)

# A formal source-derived four-point port responds only to the added nonlinear
# deformation in this normalized hostile packet.
with_four_point = expanded + [[F(0), F(0), F(0), F(1)]]
decoupled_expanded = [[F(1), F(1), F(1), F(1)]]

checks = {
    "derived_overlap_exact": eta == F(41, 400),
    "uncertainty_interval_exact": eta_low == F(37, 400) and eta_high == F(9, 80),
    "central_original_rank_three": rank(response_central) == 3,
    "lower_envelope_rank_three": rank(response_low) == 3,
    "upper_envelope_rank_three": rank(response_high) == 3,
    "detector_determinant_margin": 1 - 2 * eta_high == F(31, 40),
    "expanded_two_point_rank_three": rank(expanded_smeared) == 3,
    "expanded_two_point_kernel_one": 4 - rank(expanded_smeared) == 1,
    "isospectral_columns_equal": [row[0] for row in expanded_smeared] == [row[3] for row in expanded_smeared],
    "formal_four_point_port_restores_rank_four": rank(with_four_point) == 4,
    "decoupled_expanded_rank_one": rank(decoupled_expanded) == 1,
    "decoupled_expanded_kernel_three": 4 - rank(decoupled_expanded) == 3,
}

result = {
    "work_package": "WP133",
    "classification": "conditional rank-three detector is uncertainty-robust on the frozen class but not open-world source-identifying",
    "derived_detector": {
        "eta": str(eta), "calibration_uncertainty": str(calibration_uncertainty),
        "eta_interval": [str(eta_low), str(eta_high)],
        "minimum_determinant_margin": str(1 - 2 * eta_high),
    },
    "original_family": {"size": 3, "rank_across_envelope": 3, "kernel_dimension": 0},
    "expanded_family": {
        "size": 4, "two_point_rank": rank(expanded_smeared),
        "two_point_kernel_dimension": 4 - rank(expanded_smeared),
        "hostile_pair": ["two_adjoint", "isospectral_nonlinear_two_adjoint"],
        "formal_four_point_rank": rank(with_four_point),
    },
    "decoupled_expanded_kernel_dimension": 4 - rank(decoupled_expanded),
    "physical_instrument_established": False,
    "remaining_gate": "absolute-scale selector plus executable two- and four-point quark-Higgs spectroscopy",
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp133_physical_instrument_open_world_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
