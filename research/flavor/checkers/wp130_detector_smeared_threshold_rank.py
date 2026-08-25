"""Exact WP130 detector-smeared threshold-rank audit."""

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


rivals = ["two_adjoint", "single_auxiliary_adjoint", "direct_contact"]

# Rows: low pole bin, high pole bin, subtracted contact channel.
# Columns: frozen rival constructors. Residues are normalized before looking
# at detector responses.
ideal = [
    [F(1), F(0), F(0)],
    [F(1), F(2), F(0)],
    [F(0), F(0), F(1)],
]

eta = F(1, 4)
resolved_kernel = [
    [1 - eta, eta, F(0)],
    [eta, 1 - eta, F(0)],
    [F(0), F(0), F(1)],
]
resolved = matmul(resolved_kernel, ideal)

merged_kernel = [
    [F(1), F(1), F(0)],
    [F(1), F(1), F(0)],
    [F(0), F(0), F(1)],
]
merged = matmul(merged_kernel, ideal)

# Below all thresholds, matching makes the one admitted low-energy contact
# record identical by construction.
decoupled = [[F(1), F(1), F(1)]]

ideal_rank = rank(ideal)
resolved_rank = rank(resolved)
merged_rank = rank(merged)
decoupled_rank = rank(decoupled)

checks = {
    "ideal_spectral_rank_three": ideal_rank == 3,
    "finite_overlap_rank_three": resolved_rank == 3,
    "finite_overlap_kernel_zero": 3 - resolved_rank == 0,
    "fully_merged_rank_two": merged_rank == 2,
    "fully_merged_kernel_one": 3 - merged_rank == 1,
    "merged_hostile_pair_equal": [row[0] for row in merged] == [row[1] for row in merged],
    "decoupled_rank_one": decoupled_rank == 1,
    "decoupled_kernel_two": 3 - decoupled_rank == 2,
    "contact_constructor_remains_separate_when_thresholds_merge": [row[2] for row in merged] != [row[0] for row in merged],
    "resolution_parameter_predeclared": eta == F(1, 4),
}

result = {
    "work_package": "WP130",
    "classification": "threshold faithfulness is resolution-relative; no established physical instrument",
    "rivals": rivals,
    "probe": "detector-smeared absorptive spectral bins plus subtracted contact channel",
    "ranks": {"ideal": ideal_rank, "finite_overlap_eta_1_over_4": resolved_rank, "fully_merged": merged_rank, "decoupled": decoupled_rank},
    "kernel_dimensions": {"ideal": 3 - ideal_rank, "finite_overlap_eta_1_over_4": 3 - resolved_rank, "fully_merged": 3 - merged_rank, "decoupled": 3 - decoupled_rank},
    "hostile_threshold_equivalent_pair": ["two_adjoint", "single_auxiliary_adjoint"],
    "reference_port_required": True,
    "physical_instrument_established": False,
    "instrument_gate": "gauge/Lorentz-complete SM portal, reachable energy, calibrated widths and resolution",
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp130_detector_smeared_threshold_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
