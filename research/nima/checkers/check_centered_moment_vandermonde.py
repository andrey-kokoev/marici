from fractions import Fraction


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        value = a[col][col]
        out *= value
        a[col] = [x / value for x in a[col]]
        for row in range(col + 1, n):
            factor = a[row][col]
            a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return out


def centered_moment_matrix(values):
    r = len(values)
    columns = [[Fraction(1) for _ in values]]
    for power in range(1, r):
        raw = [Fraction(x) ** power for x in values]
        mean = sum(raw) / r
        columns.append([x - mean for x in raw])
    return [[columns[col][row] for col in range(r)] for row in range(r)]


values = [1, 2, 4, 7]
matrix = centered_moment_matrix(values)
det = determinant(matrix)
vandermonde = Fraction(1)
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        vandermonde *= values[j] - values[i]

assert det == vandermonde
assert det > 0

duplicate = [1, 2, 2, 7]
assert determinant(centered_moment_matrix(duplicate)) == 0

reversed_values = list(reversed(values))
assert determinant(centered_moment_matrix(reversed_values)) == vandermonde

print("distinct scale labels: centered moments span the fiber complement")
print(f"oriented determinant: {det}")
print("duplicate scale label: cyclicity fails")
