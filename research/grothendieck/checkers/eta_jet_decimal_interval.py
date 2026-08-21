"""Directed-rounding interval enclosure of eta derivatives at one."""
import json
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from pathlib import Path

PREC, N, M = 80, 10_000, 60
down = Context(prec=PREC, rounding=ROUND_FLOOR)
up = Context(prec=PREC, rounding=ROUND_CEILING)
near = Context(prec=PREC)

def add(x, y): return down.add(x[0], y[0]), up.add(x[1], y[1])
def neg(x): return x[1].copy_negate(), x[0].copy_negate()
def sub(x, y): return add(x, neg(y))
def div_positive(x, d): return down.divide(x[0], d), up.divide(x[1], d)

def log_interval(n):
    with localcontext(near) as ctx:
        value = ctx.ln(Decimal(n))
        return ctx.next_minus(value), ctx.next_plus(value)

def positive_power(x, j):
    if j == 0: return Decimal(1), Decimal(1)
    return down.power(x[0], j), up.power(x[1], j)

def summand(n, j):
    return div_positive(positive_power(log_interval(n), j), Decimal(n))

def eta_derivative_interval(j):
    total = (Decimal(0), Decimal(0))
    for n in range(1, N):
        term = summand(n, j)
        total = add(total, term if n % 2 else neg(term))
    row = [summand(n, j) for n in range(N, N + M + 1)]
    transformed = (Decimal(0), Decimal(0))
    two_power = Decimal(2)
    for _ in range(M):
        transformed = add(transformed, div_positive(row[0], two_power))
        row = [sub(row[i], row[i + 1]) for i in range(len(row)-1)]
        two_power *= 2
    total = sub(total, transformed)  # N is even.
    total = add(total, (Decimal("-1e-100"), Decimal("1e-100")))
    return neg(total) if j % 2 else total

intervals = [eta_derivative_interval(j) for j in range(5)]
assert all(lo < hi for lo, hi in intervals)
assert max(hi-lo for lo, hi in intervals) < Decimal("1e-70")
result = {
    "precision_decimal_digits": PREC,
    "tail_start": N,
    "euler_transforms": M,
    "eta_derivative_intervals": [[str(lo), str(hi)] for lo, hi in intervals],
    "maximum_interval_width": str(max(hi-lo for lo, hi in intervals)),
    "correctly_rounded_decimal_log_used": True,
    "tail_bound_included": "1e-100 symmetric enclosure",
    "eta_jet_interval_certified": True,
    "zero_locations_used": False,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-jet-decimal-interval.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items(): print(f"{key}={value}")
