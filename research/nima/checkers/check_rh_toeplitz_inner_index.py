import json
from pathlib import Path


def shift_matrix(size, degree=1):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for column in range(size):
        row = column + degree
        if row < size:
            matrix[row][column] = 1
    return matrix


def rank(matrix):
    work = [list(map(float, row)) for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][column] != 0:
                factor = work[r][column]
                work[r] = [work[r][c] - factor * work[pivot_row][c] for c in range(columns)]
        pivot_row += 1
    return pivot_row


rows = []
for size in (2, 3, 5, 8):
    for degree in (1, 2):
        matrix = shift_matrix(size, degree)
        matrix_rank = rank(matrix)
        kernel_dimension = size - matrix_rank
        cokernel_dimension = size - matrix_rank
        # Finite square truncations have index zero because boundary truncation
        # creates both a kernel and cokernel. The stable missing-range count is
        # the degree, while the kernel consists of cutoff escape modes.
        assert matrix_rank == max(0, size - degree)
        assert kernel_dimension == min(size, degree)
        assert cokernel_dimension == min(size, degree)
        rows.append({
            "cutoff": size,
            "inner_degree": degree,
            "rank": matrix_rank,
            "finite_kernel_dimension": kernel_dimension,
            "finite_cokernel_dimension": cokernel_dimension,
            "stable_infinite_toeplitz_index": -degree,
        })

result = {
    "hardy_symbol": "z^m",
    "infinite_kernel_dimension": 0,
    "infinite_cokernel_dimension": "m",
    "infinite_index": "-m",
    "finite_sections": rows,
    "finite_section_warning": "square truncations have artificial cutoff kernels and index zero",
    "degree_one_blaschke_index": -1,
    "reciprocal_inverse_index": 1,
    "global_pair_index": 0,
    "verdict": "sector Toeplitz index detects an inner zero that boundary modulus and global reciprocal index miss",
}

output = Path(__file__).parents[1] / "results" / "rh-toeplitz-inner-index.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

