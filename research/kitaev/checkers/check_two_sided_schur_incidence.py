#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/two-sided-schur-incidence.json"


def loads(matrix):
    alpha = max(sum(abs(matrix[i, j]) for j in range(matrix.cols))
                for i in range(matrix.rows))
    gamma = max(sum(abs(matrix[i, j]) for i in range(matrix.rows))
                for j in range(matrix.cols))
    return alpha, gamma


def block_gram(r):
    return Matrix.vstack(
        Matrix.hstack(Matrix.eye(r.rows), r),
        Matrix.hstack(r.T, Matrix.eye(r.cols)),
    )


def main():
    diffuse = Rational(1, 2) * Matrix.eye(5)
    alpha, gamma = loads(diffuse)
    hs_squared = sum(x * x for x in diffuse)
    gram = block_gram(diffuse)
    assert hs_squared == Rational(5, 4) > 1
    assert alpha == gamma == Rational(1, 2)
    assert min(gram.eigenvals(), key=lambda z: float(z)) == Rational(1, 2)

    pileup = Matrix([Rational(1, 2)] * 4)
    row_load, column_load = loads(pileup)
    pileup_gram = block_gram(pileup)
    assert row_load == Rational(1, 2)
    assert column_load == 2
    assert pileup_gram.det() == 0
    assert pileup_gram.nullspace()

    hadamard = Rational(1, 4) * Matrix([
        [1, 1, 1, 1], [1, -1, 1, -1],
        [1, 1, -1, -1], [1, -1, -1, 1],
    ])
    hrow, hcol = loads(hadamard)
    hgram = block_gram(hadamard)
    assert hrow == hcol == 1
    assert min(hgram.eigenvals(), key=lambda z: float(z)) == Rational(1, 2)

    payload = {
        "schema": "marici.kitaev.two_sided_schur_incidence.v1",
        "status": "pass",
        "diffuse_fixture": {
            "squared_hilbert_schmidt_norm": str(hs_squared),
            "max_row_load": str(alpha), "max_column_load": str(gamma),
            "certified_lower_bound": "1/2",
        },
        "one_sided_failure": {
            "max_row_load": str(row_load),
            "max_column_load": str(column_load),
            "operator_norm": "1", "block_gram_singular": True,
        },
        "absolute_value_loss": {
            "max_row_load": str(hrow), "max_column_load": str(hcol),
            "actual_operator_norm": "1/2", "actual_gram_lower_bound": "1/2",
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
