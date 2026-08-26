import json
from fractions import Fraction as F
from math import comb


def derivative(p):
    return [F(k) * p[k] for k in range(1, len(p))]


def add(a, b):
    n = max(len(a), len(b))
    return [(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0) for k in range(n)]


def subtract(a, b):
    return add(a, [-v for v in b])


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def shift(p, a):
    out = [F(0)] * len(p)
    for k, pk in enumerate(p):
        for r in range(k + 1):
            out[r] += pk * F(comb(k, r)) * a ** (k - r)
    return out


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


f = [F(2), F(-3), F(5), F(1)]
L = F(2)
M = F(3)
tail = shift(f, L)

derivative_covariant = shift(derivative(f), L) == derivative(tail)
global_y_tail = shift(multiply([F(0), F(1)], f), L)
transported_y_tail = multiply([L, F(1)], tail)
naive_residual = trim(subtract(global_y_tail, multiply([F(0), F(1)], tail)))
expected_residual = trim([L * v for v in tail])
two_cut_coordinate = [L + M, F(1)]
iterated_coordinate = add([M, F(1)], [L])

potential = [F(1), F(-2), F(3)]
D_then_cut = shift(add(derivative(f), multiply(potential, f)), L)
cut_then_transported_D = add(derivative(tail), multiply(shift(potential, L), tail))

result = {
    "schema": "marici.grothendieck.weyl_cut_covariance.v1",
    "checks": {
        "derivative_is_translation_covariant": derivative_covariant,
        "global_coordinate_transports_to_y_plus_L": global_y_tail == transported_y_tail,
        "naive_unshifted_coordinate_has_bulk_L_residual": naive_residual == expected_residual and any(naive_residual),
        "affine_cut_origins_compose_additively": two_cut_coordinate == iterated_coordinate,
        "general_first_order_operator_covariant_with_shifted_coefficients": D_then_cut == cut_then_transported_D,
    },
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
