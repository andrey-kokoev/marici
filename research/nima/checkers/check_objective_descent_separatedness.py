import itertools
import json
from fractions import Fraction
from pathlib import Path


def zero_matrix(size):
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def bits(index, n):
    return tuple((index >> (n - 1 - i)) & 1 for i in range(n))


def index_from_bits(values):
    out = 0
    for value in values:
        out = (out << 1) | value
    return out


def partial_trace(matrix, n, keep):
    keep = tuple(sorted(keep))
    drop = tuple(i for i in range(n) if i not in keep)
    out_size = 2 ** len(keep)
    out = zero_matrix(out_size)
    for row in range(2 ** n):
        row_bits = bits(row, n)
        for col in range(2 ** n):
            col_bits = bits(col, n)
            if any(row_bits[i] != col_bits[i] for i in drop):
                continue
            out_row = index_from_bits(tuple(row_bits[i] for i in keep))
            out_col = index_from_bits(tuple(col_bits[i] for i in keep))
            out[out_row][out_col] += matrix[row][col]
    return out


n = 3
size = 2 ** n
plus = zero_matrix(size)
minus = zero_matrix(size)
for matrix in (plus, minus):
    matrix[0][0] = Fraction(1, 2)
    matrix[7][7] = Fraction(1, 2)
plus[0][7] = plus[7][0] = Fraction(1, 2)
minus[0][7] = minus[7][0] = Fraction(-1, 2)

assert plus != minus

proper_fragment_results = []
for width in (1, 2):
    for keep in itertools.combinations(range(n), width):
        plus_reduced = partial_trace(plus, n, keep)
        minus_reduced = partial_trace(minus, n, keep)
        assert plus_reduced == minus_reduced
        proper_fragment_results.append({
            "keep": list(keep),
            "equal": True,
        })

delta = [[plus[i][j] - minus[i][j] for j in range(size)] for i in range(size)]
assert any(entry != 0 for row in delta for entry in row)
for width in (1, 2):
    for keep in itertools.combinations(range(n), width):
        reduced_delta = partial_trace(delta, n, keep)
        assert all(entry == 0 for row in reduced_delta for entry in row)

result = {
    "status": "pass",
    "claim": "proper-fragment objective descent is not separated for global GHZ phase",
    "global_states_distinct": True,
    "proper_fragment_restrictions": proper_fragment_results,
    "all_proper_restrictions_equal": True,
    "nonzero_global_kernel_direction": True,
    "source_anchor_recovers_kernel_direction": False,
    "typed_residual": "nonseparated_global_phase",
}

out = Path(__file__).parents[1] / "results" / "objective-descent-separatedness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

