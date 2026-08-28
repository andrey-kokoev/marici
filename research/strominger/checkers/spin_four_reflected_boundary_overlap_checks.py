"""Full sparse spin-four hostile for the reflected affine-overlap prediction."""
from collections import defaultdict
import json
import math
from pathlib import Path


SPIN = 4
N = 4 * SPIN - 1


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def path_coefficients(spin, grade, depth, m_value):
    # Covariant spin-s fold: the spin-two factor 4-a becomes 2s-a.
    folded = [
        math.comb(grade, j)
        * (-1) ** (grade - j)
        * rising(depth, grade - j)
        * rising(2 * spin - depth, j)
        for j in range(grade + 1)
    ]
    output = [m_value * folded[0]]
    output += [
        (m_value + j) * folded[j]
        + (m_value + j - 1 - grade) * folded[j - 1]
        for j in range(1, grade + 1)
    ]
    output.append(m_value * folded[grade])
    return output


def canonical_column(spin, grade, depth, m_value):
    delta = 1 - grade - (depth + m_value)
    shift = -depth - grade if delta > 0 else -depth - grade + abs(delta)
    sign = 1 if delta > 0 else -1
    return {
        shift + j: sign * value
        for j, value in enumerate(path_coefficients(spin, grade, depth, m_value))
        if value
    }


def component(spin, grade):
    q = 2 * grade + 4 * spin
    k = grade // 2 + 2 * spin
    center = 1 - grade
    return [
        canonical_column(spin, grade, depth, m_value)
        for depth in range(0, 2 * k + 1, 2)
        for m_value in (center - q - depth, center + q - depth)
    ]


def hall_rows(columns):
    owner = {}

    def augment(column, seen):
        for row in sorted(columns[column]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = column
                return True
        return False

    matched = sum(augment(column, set()) for column in range(len(columns)))
    if matched != len(columns):
        raise AssertionError((matched, len(columns)))
    by_column = {column: row for row, column in owner.items()}
    return [by_column[column] for column in range(len(columns))]


def rank_mod(matrix, prime=1_000_000_007):
    work = [[value % prime for value in row] for row in matrix]
    n_rows = len(work)
    n_cols = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(n_cols):
        pivot = next((row for row in range(pivot_row, n_rows)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], prime - 2, prime)
        work[pivot_row] = [(value * inverse) % prime for value in work[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][j] - factor * work[pivot_row][j]) % prime
                for j in range(n_cols)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


matrix_records = []
for grade in range(2, 12, 2):
    columns = component(SPIN, grade)
    rows = hall_rows(columns)
    matrix = [[column.get(row, 0) for column in columns] for row in rows]
    matrix_rank = rank_mod(matrix)
    relation = [
        (2 * grade + N) * matrix[rows.index(1)][column]
        - (3 * grade + N) * matrix[rows.index(0)][column]
        for column in range(len(columns))
    ]
    divisor = math.gcd(2 * grade + N, 3 * grade + N)
    active = [
        [1, (2 * grade + N) // divisor],
        [0, -(3 * grade + N) // divisor],
    ]
    matrix_records.append({
        "grade": grade,
        "q": 2 * grade + 4 * SPIN,
        "k": grade // 2 + 2 * SPIN,
        "shape": [len(matrix), len(columns)],
        "rank_mod_1000000007": matrix_rank,
        "left_nullity_mod_1000000007": len(matrix) - matrix_rank,
        "active_left_cocircuit": active,
        "predicted_relation_zero": all(value == 0 for value in relation),
        "predicted_row_ratio": [3 * grade + N, 2 * grade + N],
    })


def joint_chart(x, y):
    return ((3 * x - 2 * y) % N, (3 * y - 2 * x) % N)


fibers = defaultdict(list)
for x in range(N):
    for y in range(N):
        fibers[joint_chart(x, y)].append((x, y))

joint_image_size = len(fibers)
fiber_sizes = sorted({len(value) for value in fibers.values()})
zero_fiber = fibers[(0, 0)]

gates = [
    all(item["left_nullity_mod_1000000007"] == 1 for item in matrix_records),
    all(item["predicted_relation_zero"] for item in matrix_records),
    all(len(item["active_left_cocircuit"]) == 2 for item in matrix_records),
    joint_image_size == 45,
    fiber_sizes == [5],
    len(zero_fiber) == 5,
    (3, 12) in zero_fiber,
]

result = {
    "schema": "marici.strominger.spin_four_reflected_boundary_overlap.v1",
    "spin": SPIN,
    "predicted_affine_order": N,
    "source_operator": "covariant spin-s Laurent fold with factor 2s-a",
    "matrix_records": matrix_records,
    "joint_chart_matrix": [[3, -2], [-2, 3]],
    "joint_domain_size": N * N,
    "joint_image_size": joint_image_size,
    "joint_fiber_sizes": fiber_sizes,
    "zero_fiber": [list(item) for item in zero_fiber],
    "fivefold_overlap_verified": joint_image_size == 45 and fiber_sizes == [5],
    "physical_higher_spin_source_authority": "conditional_on_spin_four_covariant_source",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "spin_four_reflected_boundary_overlap_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
