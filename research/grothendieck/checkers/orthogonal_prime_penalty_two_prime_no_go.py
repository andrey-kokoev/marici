"""Dependency-free hostile test of the orthogonal prime-penalty model."""

import json
import math
from pathlib import Path


N = 200_000


def f_partial(a):
    return sum(1 / (k + 0.25) - 1 / (k + 0.25 + a / 2) for k in range(N))


def f_tail_bound(a):
    # Each omitted term is at most (a/2)/(k+1/4)^2; compare with an integral.
    return (a / 2) / (N - 0.75)


def gamma_gram(m, n):
    a, b = math.log(m), math.log(n)
    value = f_partial(a) + f_partial(b) - f_partial(a + b)
    error = f_tail_bound(a) + f_tail_bound(b) + f_tail_bound(a + b)
    return value, error


g22, e22 = gamma_gram(2, 2)
g33, e33 = gamma_gram(3, 3)
g23, e23 = gamma_gram(2, 3)
a = g22 - math.log(2) / math.sqrt(2)
b = g33 - math.log(3) / math.sqrt(3)
c = g23
determinant = a * b - c * c

# First-order plus quadratic interval propagation for (a+da)(b+db)-(c+dc)^2.
det_error = (
    abs(b) * e22
    + abs(a) * e33
    + 2 * abs(c) * e23
    + e22 * e33
    + e23 * e23
)
assert a > e22 and b > e33
assert determinant + det_error < 0

result = {
    "series_terms": N,
    "gamma_22": g22,
    "gamma_33": g33,
    "gamma_23": g23,
    "penalized_22": a,
    "penalized_33": b,
    "determinant": determinant,
    "determinant_error_bound": det_error,
    "determinant_certifiably_negative": True,
    "individual_diagonals_positive": True,
    "orthogonal_prime_penalty_model_falsified": True,
    "actual_Weil_form_falsified": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "orthogonal-prime-penalty-two-prime-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
