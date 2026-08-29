import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
t = sp.Rational(6, 5)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])

words = [
    sp.eye(3),
    X,
    Y,
    X**2,
    Y**2,
    X*Y+Y*X,
    sp.I*(X*Y-Y*X),
    X*Y*X,
    Y*X*Y,
]
word_names = [
    "I", "X", "Y", "X^2", "Y^2", "{X,Y}",
    "i[X,Y]", "XYX", "YXY",
]

def hermitian_coordinates(matrix):
    return sp.Matrix([
        matrix[0, 0], matrix[1, 1], matrix[2, 2],
        sp.re(matrix[0, 1]), sp.im(matrix[0, 1]),
        sp.re(matrix[0, 2]), sp.im(matrix[0, 2]),
        sp.re(matrix[1, 2]), sp.im(matrix[1, 2]),
    ])

assert all(word == word.conjugate().T for word in words)
basis = sp.Matrix.hstack(*[hermitian_coordinates(word) for word in words])
basis_det = sp.factor(basis.det())
assert basis_det == -sp.Rational(27936, 625)
assert basis.rank() == 9

# Exact reconstruction of a generic Hermitian target proves that the word
# coefficients are unique and target-dependent.
h = sp.symbols("h0:9", real=True)
target_coordinates = sp.Matrix(h)
coefficients = sp.simplify(basis.inv()*target_coordinates)
assert sp.simplify(basis*coefficients-target_coordinates) == sp.zeros(9, 1)
assert all(any(coefficient.has(value) for coefficient in coefficients) for value in h)

# A quadratic real spectral polynomial in Y independently assigns its three
# eigenvalues, so an arbitrary positive nondegenerate Hd spectrum is reachable.
r = sp.sqrt(86)/5
vandermonde = sp.Matrix([[1, -r, r**2], [1, 0, 0], [1, r, r**2]])
spectral_det = sp.factor(vandermonde.det())
assert spectral_det != 0

# The common Hermitian commutant is only the scalar line.
a = sp.symbols("a0:9", real=True)
generic = sum((a[k]*words[k] for k in range(9)), sp.zeros(3))
equations = list(generic*X-X*generic)+list(generic*Y-Y*generic)
commutant_matrix, _ = sp.linear_eq_to_matrix(equations, a)
assert commutant_matrix.rank() == 8

# Deliberate-failure test: removing the explicitly noncommuting Hermitian word
# i[X,Y] leaves an eight-dimensional compiler and a nonzero missing direction.
reduced = sp.Matrix.hstack(*[
    hermitian_coordinates(word)
    for index, word in enumerate(words) if index != 6
])
assert reduced.rank() == 8
missing_left_kernel = reduced.T.nullspace()
assert len(missing_left_kernel) == 1
missing_obstruction = sp.factor(
    (missing_left_kernel[0].T*hermitian_coordinates(words[6]))[0]
)
assert missing_obstruction != 0

result = {
    "schema": "marici.flavor.wp1014.v1",
    "status": "PASS",
    "selected_pair": "WP1009 X,Y representative",
    "hermitian_word_basis": word_names,
    "basis_rank": basis.rank(),
    "basis_determinant": str(basis_det),
    "common_hermitian_commutant_dimension": 9-commutant_matrix.rank(),
    "down_spectral_interpolation_basis": ["I", "Y", "Y^2"],
    "down_vandermonde_determinant": str(spectral_det),
    "quotient_capacity": "arbitrary positive nondegenerate Gram pair modulo simultaneous weak-basis conjugation",
    "coefficient_status": "nine Hu coefficients and three Hd spectral coefficients are solved from the target",
    "contextual_partition": "singleton only after supplying the target coefficients; without them the image is the complete admissible quotient",
    "classification": "universal covariant compiler; neither selector nor rigidifier",
    "deliberate_failure": {
        "removed_word": "i[X,Y]",
        "reduced_rank": reduced.rank(),
        "missing_direction_obstruction": str(missing_obstruction),
    },
    "claim_boundary": "algebraic reachability is not a source law, executable control, calibrated instrument, or numerical prediction",
    "remaining_gate": "a source principle must restrict or determine compiler coefficients before any readout comparison",
}

out = ROOT/"results"/"wp1014_mixed_word_universal_compiler.json"
out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print("WP1014 PASS: mixed words span all Hermitian 3x3 targets but select none")
