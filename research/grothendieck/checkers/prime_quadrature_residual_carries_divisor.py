import json
import sympy as sp


x, s, rho = sp.symbols("x s rho")
sigma = sp.symbols("sigma", positive=True, real=True)
L = sp.symbols("L", positive=True, real=True)
K = 7
local_series = sum(x**k for k in range(1, K + 1))
local_rational_series = sp.series(x / (1 - x), x, 0, K + 1).removeO()

# Near a simple zeta zero u=rho, -zeta'/zeta(u) has principal part
# -1/(u-rho).  With u=s+1 the shifted pole is s=rho-1; subtracting 1/s
# cannot cancel it unless rho=1, which is not a nontrivial zero.
s0 = rho - 1
principal_residual = -1 / (s - s0) - 1 / s
shifted_residue = sp.simplify(sp.limit((s - s0) * principal_residual, s, s0))

checks = {
    "prime_power_geometric_series": sp.expand(local_series - local_rational_series) == 0,
    "shifted_zero_residue_survives": shifted_residue == -1,
    "continuous_laplace_transform": sp.integrate(sp.exp(-sigma * L), (L, 0, sp.oo)) == 1 / sigma,
}

result = {
    "schema": "marici.grothendieck.prime_quadrature_residual_carries_divisor.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "arithmetic_transform": "sum_n Lambda(n)/n * exp(-s log n) = -zeta'(s+1)/zeta(s+1)",
    "continuous_transform": "integral_0^infinity exp(-sL)dL = 1/s",
    "residual": "-zeta'(s+1)/zeta(s+1)-1/s",
    "nontrivial_pole": "s=rho-1 with residue -1",
}

print(json.dumps(result, indent=2, sort_keys=True))
