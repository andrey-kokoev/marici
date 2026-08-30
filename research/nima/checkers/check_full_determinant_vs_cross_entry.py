def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_at(z):
    return (
        (2 * z, -1j + z),
        (1j + z, 2 * z),
    )


z = 1j
matrix = matrix_at(z)

assert abs(matrix[0][1]) < 1e-12
assert abs(determinant_2x2(matrix)) > 1e-12

# The imaginary part is Im(z) times [[2,1],[1,2]], whose principal
# minors are positive.
imaginary_part = ((2.0, 1.0), (1.0, 2.0))
assert imaginary_part[0][0] > 0
assert determinant_2x2(imaginary_part) > 0

print("strict Herglotz matrix: positive imaginary part")
print("cross entry vanishes at z=i")
print("full determinant remains nonzero")
