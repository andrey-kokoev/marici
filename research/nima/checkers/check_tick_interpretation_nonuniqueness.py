"""Exact polynomial certificate for a DECLARED stochastic interpretation class.

Not an Agda evaluator: this checks the analytic counterexample's algebra.
The connection to full Bool Ticks uses TickRetainedStructure's separately
checked classification. No unitary or autonomous-flow claim is made.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def poly(*coefficients):
    out = list(map(F, coefficients)) or [F(0)]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


ZERO, ONE = poly(0), poly(1)


def add(a, b):
    return poly(*(sum((p[i] if i < len(p) else F(0)) for p in (a, b))
                  for i in range(max(len(a), len(b)))))


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly(*out)


def evaluate(p, t):
    return sum(c * t**i for i, c in enumerate(p))


def reverse(p):
    out, power = ZERO, ONE
    for c in p:
        out = add(out, poly(*(c * x for x in power)))
        power = mul(power, poly(1, -1))
    return out


def bernstein2(p):
    assert len(p) <= 3
    a, b, c = tuple(p) + (F(0),) * (3 - len(p))
    return (a, a + b / 2, a + b + c)


def basis(q):
    return tuple(F(i == q) for i in range(4))


def leg(model, q, active):
    # active=2 flips the first bit; active=1 flips the second.
    other = 3 ^ active
    weights = ((poly(1, -1), poly(0, 1), ZERO) if model == "straight"
               else (poly(1, -2, 1), poly(0, 1), poly(0, 1, -1)))
    result = [ZERO] * 4
    for state, weight in zip((q, q ^ active, q ^ other), weights):
        result[state] = weight
    return tuple(result)


def value(curve, t):
    return tuple(evaluate(p, t) for p in curve)


checks = []


def check(name, condition):
    checks.append({"property": name, "passed": bool(condition)})
    if not condition:
        raise AssertionError(name)


witnesses = []
for q in range(4):
    for active, schedule in ((2, "leftFirst"), (1, "rightFirst")):
        other = 3 ^ active
        curves = {}
        for model in ("straight", "bowed"):
            first = leg(model, q, active)
            second = leg(model, q ^ active, other)
            curves[model] = (first, second)
            prefix = f"{q}/{schedule}/{model}"
            check(prefix + "/source", value(first, F(0)) == basis(q))
            check(prefix + "/middle", value(first, F(1)) == basis(q ^ active))
            check(prefix + "/seam", value(first, F(1)) == value(second, F(0)))
            check(prefix + "/target", value(second, F(1)) == basis(q ^ 3))
            for n, curve in enumerate((first, second)):
                total = ZERO
                for p in curve:
                    total = add(total, p)
                check(prefix + f"/leg{n}/normalization-identity", total == ONE)
                check(prefix + f"/leg{n}/nonnegative-on-unit-interval",
                      all(c >= 0 for p in curve for c in bernstein2(p)))
            backward = tuple(tuple(reverse(p) for p in curve)
                             for curve in (second, first))
            check(prefix + "/reverse-start", value(backward[0], F(0)) == basis(q ^ 3))
            check(prefix + "/reverse-seam", value(backward[0], F(1)) == value(backward[1], F(0)))
            check(prefix + "/reverse-end", value(backward[1], F(1)) == basis(q))
            check(prefix + "/double-reverse",
                  tuple(tuple(reverse(p) for p in curve) for curve in reversed(backward))
                  == (first, second))

        # This coordinate vanishes on BOTH entire straight legs. The bowed
        # first leg has value 1/4 there at its midpoint. No change of the
        # global time parameter can make those path images equal.
        missing = q ^ other
        straight = curves["straight"]
        bowed = curves["bowed"]
        check(f"{q}/{schedule}/global-straight-invariant",
              straight[0][missing] == ZERO and straight[1][missing] == ZERO)
        witness = evaluate(bowed[0][missing], F(1, 2))
        check(f"{q}/{schedule}/bowed-outside-straight-image", witness == F(1, 4))
        witnesses.append({"source": q, "schedule": schedule,
                          "missing_coordinate": missing, "bowed_midpoint_value": str(witness)})

result = {
    "schema": "marici.nima.tick-interpretation-nonuniqueness.v1",
    "status": "pass",
    "arithmetic": "exact rational polynomial coefficients",
    "scope": "continuous stochastic schedule interpolations; not unitary flows or an Agda evaluator",
    "parameter_domain": "[0,2], with two polynomial unit-interval legs",
    "obstruction": "one coordinate is identically zero on the whole straight path but equals 1/4 on the bowed path",
    "consequence": "no parameter substitution represents the bowed path as the straight path; hence no time-reparameterization equivalence",
    "checks": checks,
    "witnesses": witnesses,
}
path = Path(__file__).resolve().parents[1] / "results" / "tick-interpretation-nonuniqueness.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {len(checks)}/{len(checks)} exact checks; {len(witnesses)} image obstructions")
print("Scope: declared stochastic interpolation class, not unitary dynamics.")
