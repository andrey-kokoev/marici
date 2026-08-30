"""Small hostile C2 test for the conjugation-graph correspondence."""

import sympy as sp

beta = sp.Rational(3, 4)
height = sp.Rational(2)
zeros = [
    beta + sp.I * height,
    beta - sp.I * height,
    1 - beta + sp.I * height,
    1 - beta - sp.I * height,
]


def kernel(rho: sp.Expr, sigma: sp.Expr) -> sp.Expr:
    z = rho - sp.Rational(1, 2)
    w = sigma - sp.Rational(1, 2)
    return sp.simplify(((z + w) / 2) ** 2 / (1 + z * w))


graph_trace = sp.simplify(sum(kernel(rho, sp.conjugate(rho)) for rho in zeros))
product_trace = sp.simplify(sum(kernel(rho, sigma) for rho in zeros for sigma in zeros))
assert graph_trace == sp.Rational(4, 81)
assert product_trace != graph_trace

# Two free C2 orbits: pullback repeats orbit values; pushforward sums fibers.
q_pull = sp.Matrix([[1, 0], [1, 0], [0, 1], [0, 1]])
q_push = q_pull.T
assert q_push * q_pull == 2 * sp.eye(2)
assert (q_pull.T * q_pull) == 2 * sp.eye(2)

# A fixed point changes the scalar norm into an orbit-cardinality operator.
fixed_pull = sp.Matrix([[1, 0], [0, 1], [0, 1]])
fixed_norm = fixed_pull.T * fixed_pull
assert fixed_norm == sp.diag(1, 2)

print(f"graph_trace={graph_trace}")
print(f"independent_product_trace={product_trace}")
print("graph_trace_not_product_trace=True")
print("free_C2_pull_push=2*I")
print(f"fixed_point_pull_push={fixed_norm}")
print("physical_relative_chain_pushforward_constructed=False")

