import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/strominger/results/capcl_magnetic_q31_outcome.json"


def path_coefficients(g, a, m):
    def rising(value, count):
        return math.prod(value + offset for offset in range(count))

    c = [math.comb(g, j) * (-1) ** (g - j) * rising(a, g - j) * rising(4 - a, j) for j in range(g + 1)]
    b = [m * c[0]]
    for j in range(1, g + 1):
        b.append((m + j) * c[j] + (m + j - 1 - g) * c[j - 1])
    b.append(m * c[g])
    return b


def canonical_column(g, a, m):
    signed_delta = 1 - g - (a + m)
    q = abs(signed_delta)
    shift = -a - g if signed_delta > 0 else -a - g + q
    sign = 1 if signed_delta > 0 else -1
    return {shift + j: sign * value for j, value in enumerate(path_coefficients(g, a, m)) if value}


def component(g, k, q):
    center = 1 - g
    points = []
    for a in range(0, 2 * k + 1, 2):
        points.extend([(a, center - q - a), (a, center + q - a)])
    return [canonical_column(g, a, m) for a, m in points]


def matching_size(columns):
    owner = {}

    def augment(column_index, seen):
        for row in sorted(columns[column_index]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = column_index
                return True
        return False

    return sum(augment(index, set()) for index in range(len(columns)))


def exact_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


records = []
first_counterexample = None
for g in range(2, 21):
    columns = component(g, 10, 31)
    rows = sorted(set().union(*(column.keys() for column in columns)))
    matrix = [[column.get(row, 0) for column in columns] for row in rows]
    rank = exact_rank(matrix)
    hall = matching_size(columns)
    record = {"g": g, "rows": len(rows), "columns": len(columns), "Hall_matching_size": hall, "rank": rank, "nullity": len(columns) - rank}
    records.append(record)
    if first_counterexample is None and rank < len(columns):
        first_counterexample = record

outcome = "confirmed_in_declared_range" if first_counterexample is None else "falsified"
result = {
    "schema": "marici.strominger.capcl-prediction-outcome.v1",
    "prediction_id": "capcl-magnetic-q31-rank-002",
    "outcome": outcome,
    "prediction_confirmed": first_counterexample is None,
    "prediction_falsified": first_counterexample is not None,
    "declared_range": {"q": 31, "g": [2, 20], "k": 10},
    "all_Hall_matchings_complete": all(item["Hall_matching_size"] == item["columns"] for item in records),
    "all_full_matrices_column_faithful": first_counterexample is None,
    "first_counterexample": first_counterexample,
    "records": records,
    "scope_warning": "bounded confirmation is not an unbounded theorem"
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ["prediction_id", "outcome", "all_Hall_matchings_complete", "all_full_matrices_column_faithful", "first_counterexample", "scope_warning"]}, indent=2))
raise SystemExit(0 if first_counterexample is None else 1)
