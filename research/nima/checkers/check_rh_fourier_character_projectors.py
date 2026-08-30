#!/usr/bin/env python3
"""Exact spectral-projector construction for the finite five-cell quotient."""

import json
from pathlib import Path


def identity(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))


def close(a, b, eps=1e-12):
    return all(abs(a[i][j] - b[i][j]) < eps for i in range(len(a)) for j in range(len(a[0])))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def encode_matrix(a):
    return [[{"real": round(complex(x).real, 12), "imag": round(complex(x).imag, 12)} for x in row] for row in a]


def main():
    f = (
        (0, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 0, -1),
        (0, 0, 1, 0),
    )
    one = identity(4)
    powers = [one]
    for _ in range(3):
        powers.append(mul(powers[-1], f))
    assert close(mul(powers[-1], f), one)

    characters = [1, -1, 1j, -1j]
    projectors = {}
    total = scale(0, one)
    for lam in characters:
        p = scale(0, one)
        for k in range(4):
            p = add(p, scale((lam ** (-k)) / 4, powers[k]))
        assert close(mul(p, p), p)
        assert close(mul(f, p), scale(lam, p))
        assert abs(trace(p) - 1) < 1e-12
        projectors[str(lam)] = p
        total = add(total, p)
    assert close(total, one)

    for i, lam in enumerate(characters):
        for mu in characters[i + 1:]:
            assert close(mul(projectors[str(lam)], projectors[str(mu)]), scale(0, one))

    result = {
        "schema": "marici.rh-fourier-character-projectors.v1",
        "characters": ["1", "-1", "i", "-i"],
        "projector_ranks": [1, 1, 1, 1],
        "idempotent": True,
        "pairwise_orthogonal": True,
        "sum_is_identity": True,
        "source_formula": "P_lambda=(1/4) sum_{k=0}^3 lambda^(-k) F^k",
        "finite_boundary_descent": "canonically_separated",
        "completion_gate": "exclude_character_multiplicity_growth_and_prove_projector_continuity",
        "projectors": {key: encode_matrix(value) for key, value in projectors.items()}
    }
    out = Path(__file__).parents[1] / "results" / "rh-fourier-character-projectors.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "projectors"}, indent=2))


if __name__ == "__main__":
    main()
