from fractions import Fraction
import json
from pathlib import Path


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = work[r][col]
            work[r] = [work[r][c] - factor * work[pivot_row][c] for c in range(cols)]
        pivot_row += 1
    return pivot_row


# Source coordinates are (P,Q,M).
primitive_observers = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
completed_and_seam = ((1, 1, 1), (0, 0, 1))
even_odd_seam = ((1, 1, 0), (1, -1, 0), (0, 0, 1))

assert rank(primitive_observers) == 3
assert rank(completed_and_seam) == 2
assert rank(even_odd_seam) == 3

lost_tail = (1, -1, 0)
assert all(sum(row[i] * lost_tail[i] for i in range(3)) == 0 for row in completed_and_seam)

# Present-record completeness does not imply instrument completeness. Two
# states have identical primitive present records but different continuation.
present_left = (Fraction(2), Fraction(3), Fraction(5))
present_right = (Fraction(2), Fraction(3), Fraction(5))
continuation_left = (Fraction(0), Fraction(0), Fraction(0))
continuation_right = (Fraction(1), Fraction(0), Fraction(0))
assert present_left == present_right
assert continuation_left != continuation_right

# A full instrument record includes both present value and update state.
instrument_left = (present_left, continuation_left)
instrument_right = (present_right, continuation_right)
assert instrument_left != instrument_right

# Finite odd scalar summaries cannot be promoted to complete odd-channel
# observations. Record the exact external theorem as an architectural gate;
# this checker verifies only that one scalar odd row repairs the three-dimensional
# toy carrier, not the function-valued completion.
finite_dimensional_odd_row_repairs_toy = rank(even_odd_seam) == 3
finite_odd_tower_authorized_for_function_channel = False

result = {
    "schema": "marici.nima.rh-three-observer-dpc.v1",
    "primitive_pqm_rank": rank(primitive_observers),
    "completed_scalar_plus_seam_rank": rank(completed_and_seam),
    "completed_scalar_plus_seam_kernel_witness": list(lost_tail),
    "even_odd_seam_rank": rank(even_odd_seam),
    "finite_dimensional_odd_row_repairs_toy": finite_dimensional_odd_row_repairs_toy,
    "finite_odd_tower_authorized_for_function_channel": finite_odd_tower_authorized_for_function_channel,
    "equal_present_records_can_have_different_continuations": True,
    "instrument_records_separate_continuations": True,
    "verdict": (
        "Retaining P,Q,M is the minimal linearly complete three-channel carrier. "
        "A+M erases P-Q. One odd scalar repairs only the finite toy; no fixed "
        "finite moment tower is complete for the function-valued odd channel. "
        "Operational completeness further requires record-labelled updates."
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-three-observer-dpc.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
