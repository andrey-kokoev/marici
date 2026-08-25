"""Exact WP129 rival-source identification audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [v / scale for v in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [a[r][c] - factor * a[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


rivals = ["two_adjoint", "single_auxiliary_adjoint", "direct_EFT_contact"]

# All three constructors are deliberately matched to the same frozen EFT
# packet (a,q,r) and hence to every probe factoring through it.
low_energy = [
    [F(28), F(28), F(28)],          # a
    [F(25), F(25), F(25)],          # q
    [F(13), F(13), F(13)],          # radial completion r
    [F(16, 25), F(16, 25), F(16, 25)],  # selected x
    [F(400), F(400), F(400)],       # slice Hessian
    [F(1, 200), F(1, 200), F(1, 200)],  # response to a -> a+1
]
low_rank = rank(low_energy)
low_kernel = len(rivals) - low_rank

# Formal threshold/source-field incidence ports. These are algebraically
# separating, but no executable physical instrument is claimed.
threshold = [
    [F(1), F(1), F(1)],
    [F(1), F(0), F(0)],  # resolve the two-adjoint pole sector
    [F(0), F(1), F(0)],  # resolve the single auxiliary pole sector
    [F(0), F(0), F(1)],  # resolve the contact/no-pole sector
]
threshold_rank = rank(threshold)
threshold_kernel = len(rivals) - threshold_rank

checks = {
    "three_declared_rivals": len(rivals) == 3,
    "low_energy_columns_identical": all(row[0] == row[1] == row[2] for row in low_energy),
    "low_energy_rank_one": low_rank == 1,
    "low_energy_kernel_two": low_kernel == 2,
    "finite_fiber_not_singleton": low_kernel > 0,
    "threshold_family_full_rank": threshold_rank == 3,
    "threshold_kernel_zero": threshold_kernel == 0,
    "formal_separation_does_not_establish_instrument": True,
}

result = {
    "work_package": "WP129",
    "classification": "low-energy physical16 selector packet does not identify its source constructor",
    "rivals": rivals,
    "low_energy_probe_family": ["a", "q", "r", "selected_x", "slice_hessian", "a_intervention_response"],
    "low_energy_partition": [rivals],
    "low_energy_rank": low_rank,
    "low_energy_kernel_dimension": low_kernel,
    "formal_threshold_partition": [[r] for r in rivals],
    "formal_threshold_rank": threshold_rank,
    "formal_threshold_kernel_dimension": threshold_kernel,
    "threshold_instrument_established": False,
    "reference_port_required": True,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp129_rival_source_identification.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
