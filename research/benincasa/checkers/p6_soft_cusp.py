import json
from pathlib import Path

# At z=v-2:
# 4P6 = z^2 + 2*a(u)z + c(u), with
# a=u(1+2u-2u^2), c=u^2(1-2u)^2.
# For Z=z+a, 4P6=Z^2-(a^2-c).

# Sparse univariate coefficients, ascending in u.
a = [0, 1, 2, -2]
c = [0, 0, 1, -4, 4]

def mul(x, y):
    out = [0] * (len(x) + len(y) - 1)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            out[i+j] += xi*yj
    while out and out[-1] == 0:
        out.pop()
    return out

def sub(x, y):
    out = [0] * max(len(x), len(y))
    for i in range(len(x)):
        out[i] += x[i]
    for i in range(len(y)):
        out[i] -= y[i]
    while out and out[-1] == 0:
        out.pop()
    return out

delta_over_four = sub(mul(a, a), c)
expected = [0, 0, 0, 8, -4, -8, 4]  # 4*u^3*(2-u)*(1-u^2)
assert delta_over_four == expected

# The Jacobian algebra of Z^2-u^3 is Q[u,Z]/(u^2,Z), with basis 1,u.
milnor_basis = ["1", "u"]
assert len(milnor_basis) == 2

packet = {
    "schema": "marici.p6_soft_cusp.v1",
    "center": {"u": 0, "v": 2, "support": ["E_T=0", "X2=0"]},
    "local_coordinates": ["u", "z=v-2", "Z=z+u*(1+2*u-2*u^2)"],
    "completed_square": "4*P6=Z^2-4*u^3*(2-u)*(1-u^2)",
    "unit_at_center": 8,
    "formal_type": "A2: Z^2-U^3",
    "milnor_number": 2,
    "milnor_basis": milnor_basis,
    "classification": "singular coefficient divisor over existing total-energy/site-soft carrier corner",
}
Path("research/benincasa/results/p6-soft-cusp.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
