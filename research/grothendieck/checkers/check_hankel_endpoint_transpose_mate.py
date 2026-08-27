"""Exact finite mate identity for a Hankel history map and endpoint covector."""

from fractions import Fraction
import json


moments = (Fraction(3), Fraction(5), Fraction(7), Fraction(11), Fraction(13))
H = tuple(tuple(moments[i + j] for j in range(3)) for i in range(3))
endpoint = (Fraction(1), Fraction(0), Fraction(0))
vectors = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(-1)),
    (Fraction(2), Fraction(-3), Fraction(5)),
)


def matvec(matrix, vector):
    return tuple(sum((row[j] * vector[j] for j in range(len(vector))), Fraction(0)) for row in matrix)


def pairing(covector, vector):
    return sum((covector[j] * vector[j] for j in range(len(vector))), Fraction(0))


pulled_back = tuple(sum((endpoint[i] * H[i][j] for i in range(3)), Fraction(0)) for j in range(3))

checks = {
    "hankel_matrix_is_symmetric": all(H[i][j] == H[j][i] for i in range(3) for j in range(3)),
    "transpose_endpoint_is_first_source_row": pulled_back == H[0],
    "mate_identity_on_test_family": all(
        pairing(endpoint, matvec(H, vector)) == pairing(pulled_back, vector)
        for vector in vectors
    ),
    "pulled_back_covector_is_nonzero": any(value != 0 for value in pulled_back),
}

result = {
    "schema": "marici.grothendieck.hankel-endpoint-transpose-mate.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "H": [[str(x) for x in row] for row in H],
        "endpoint": [str(x) for x in endpoint],
        "pulled_back_endpoint": [str(x) for x in pulled_back],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
