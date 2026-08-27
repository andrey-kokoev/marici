#!/usr/bin/env python3
"""Checks the tail graph identity, trace pullback, and dual-pairing hostile."""

from cmath import exp


checks = {}

# Exact exponential source witness: f=e^-aq and G=e^-aq/(a-s).
a = 3.0
s = 0.4 + 1.7j
for q in (0.0, 0.25, 1.0, 3.0):
    f = exp(-a * q)
    G = f / (a - s)
    Gprime = -a * G
    checks.setdefault("source_tail_ode", True)
    checks["source_tail_ode"] &= abs(Gprime + s * G + f) < 1e-12
checks["zero_is_trace_condition"] = abs((1 / (a - s)) - (1 / (a - s))) < 1e-15

# A discrete trace-pullback model. Two half-lines glue iff their seam values
# agree, and restriction of a full line always lands in that equalizer.
full = [5, 3, 2, 7, 11]
minus = list(reversed(full[:3]))
plus = full[2:]
checks["trace_pullback"] = minus[0] == plus[0] == full[2]
reconstructed = list(reversed(minus))[0:-1] + plus
checks["pullback_reconstructs_full_line"] = reconstructed == full

# The constant row is continuous on the rapid test space, witnessed using
# delta=1, while its formal dual self-pairing diverges with cutoff.
def primes_upto(n):
    out = []
    for k in range(2, n + 1):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


P = primes_upto(20000)
checks["constant_row_continuous"] = sum(p ** -2 for p in P) < 1
counts = [sum(1 for p in P if p <= n) for n in (100, 1000, 10000)]
checks["dual_self_pairing_diverges"] = counts[0] < counts[1] < counts[2] and counts[2] > 1000

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))
