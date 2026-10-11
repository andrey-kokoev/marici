"""Exact, dependency-free checks for ledger Cardano/CRT assembly examples."""
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

# Polynomial ring Q[u,v,p,q,s], represented without symbolic dependencies.
ZERO = (0, 0, 0, 0, 0)

def constant(n):
    return {ZERO: Q(n)} if n else {}

def variable(i):
    exponent = list(ZERO)
    exponent[i] = 1
    return {tuple(exponent): Q(1)}

def add(*polynomials):
    out = defaultdict(Q)
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            out[exponent] += coefficient
    return {e: c for e, c in out.items() if c}

def scale(polynomial, n):
    return {e: c * n for e, c in polynomial.items() if c * n}

def mul(a, b):
    out = defaultdict(Q)
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[tuple(x + y for x, y in zip(ea, eb))] += ca * cb
    return {e: c for e, c in out.items() if c}

def power(a, n):
    out = constant(1)
    for _ in range(n):
        out = mul(out, a)
    return out

u, v, p, q, s = [variable(i) for i in range(5)]
x = add(u, v)
residual = add(power(x, 3), mul(p, x), q)
constraints = add(power(u, 3), power(v, 3), q,
                  mul(add(scale(mul(u, v), 3), p), x))
delta = add(scale(power(q, 2), Q(1, 4)), scale(power(p, 3), Q(1, 27)))
t_plus = add(scale(q, Q(-1, 2)), s)
t_minus = add(scale(q, Q(-1, 2)), scale(s, -1))
checks = {
    "cardano_residual_polynomial_identity": residual == constraints,
    "cardano_quadratic_sum": add(t_plus, t_minus, q) == {},
    "cardano_quadratic_product": add(mul(t_plus, t_minus), scale(power(p, 3), Q(1, 27))) == add(delta, scale(power(s, 2), -1)),
}

# Exact worked Cardano branch: p=-6, q=-9, sqrt(delta)=7/2, u=2, v=1.
pp, qq, uu, vv = Q(-6), Q(-9), Q(2), Q(1)
dd = qq * qq / 4 + pp ** 3 / 27
checks["cardano_worked_branch"] = (
    dd == Q(49, 4) and uu ** 3 == -qq / 2 + Q(7, 2)
    and vv ** 3 == -qq / 2 - Q(7, 2) and uu * vv == -pp / 3
    and (uu + vv) ** 3 + pp * (uu + vv) + qq == 0
)
# Retaining the cubic sum without the product witness gives a wrong root.
bad_residual = (1 + 1) ** 3 - 2
checks["cardano_missing_product_rejected"] = (1 ** 3 + 1 ** 3 == 2 and bad_residual == 6)
checks["cardano_zero_branch"] = 0 ** 3 + 0 * 0 + 0 == 0

assemble = lambda a, b: (10 * a + 6 * b) % 15
decompose = lambda x: (x % 3, x % 5)
pairs = list(product(range(3), range(5)))
checks["crt_all_15_pair_round_trips"] = all(decompose(assemble(a, b)) == (a, b) for a, b in pairs)
checks["crt_all_15_residue_round_trips"] = all(assemble(*decompose(x)) == x for x in range(15))
checks["crt_each_endpoint_invertible_onto_image"] = (
    len({10 * a % 15 for a in range(3)}) == 3
    and all((10 * a % 15) % 3 == a for a in range(3))
    and len({6 * b % 15 for b in range(5)}) == 5
    and all((6 * b % 15) % 5 == b for b in range(5))
)
checks["crt_worked_solution"] = assemble(2, 3) == 8
bad_crt = (10 * 2 + 5 * 3) % 15
checks["crt_bad_coefficient_rejected"] = decompose(bad_crt) != (2, 3)
checks["noncoprime_incompatible_residues_rejected"] = not any(x % 4 == 1 and x % 6 == 2 for x in range(12))
checks["noncoprime_compatible_example"] = [x for x in range(12) if x % 4 == 1 and x % 6 == 3] == [9]

result = {
    "schema": "marici.voevodsky.cardano-crt-witnessed-assembly.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "cardano_example": {"p": -6, "q": -9, "u": 2, "v": 1, "root": 3},
    "cardano_negative_residual": bad_residual,
    "crt_example": {"moduli": [3, 5], "residues": [2, 3], "solution_mod_15": 8},
    "crt_negative": {"wrong_coefficient": 5, "assembled": bad_crt, "residues": decompose(bad_crt)},
    "scope": "Exact polynomial identities and exhaustive mod-15 CRT; not a geometric or 2-Segal identification, automated formula discovery, or global branch-free Cardano inverse.",
    "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).resolve().parents[1] / "results" / "cardano_crt_witnessed_assembly.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["passed"]:
    raise SystemExit(1)
