def matrix_rank(matrix, tolerance=1e-9):
    work = [[complex(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = max(range(rank, rows), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) <= tolerance:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][j] - factor * work[rank][j] for j in range(columns)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


residues = [0, 1, 2, 3]
phase_kernel = [[(1j) ** (r * s) for s in residues] for r in residues]
assert matrix_rank(phase_kernel) == 4

s3_left = [0, 2, 3]
s3_right = [0, 1, 3]
s3_kernel = [[(1j) ** (r * s) for s in s3_right] for r in s3_left]
assert matrix_rank(s3_kernel) == 3

even = [0, 2]
even_kernel = [[(1j) ** (r * s) for s in even] for r in even]
assert even_kernel == [[1, 1], [1, 1]]
assert matrix_rank(even_kernel) == 1


def binary_decomposition_phase(r, s):
    a, b = divmod(r, 2)
    c, d = divmod(s, 2)
    controlled_s = (1j) ** (b * d)
    cz_ad = (-1) ** (a * d)
    cz_bc = (-1) ** (b * c)
    return controlled_s * cz_ad * cz_bc


for r in residues:
    for s in residues:
        assert binary_decomposition_phase(r, s) == (1j) ** (r * s)

print(
    {
        "status": "passed",
        "interaction_schmidt_ranks": {
            "full_mod4": 4,
            "s3_selected_support": 3,
            "even_support": 1,
        },
        "binary_decomposition": "CS(b,d) CZ(a,d) CZ(b,c)",
        "native_lens": "ququart_Clifford",
        "binary_lens": "requires_controlled_S",
        "theorem": "orientation_requires_constructor_and_faithful_lens",
    }
)
