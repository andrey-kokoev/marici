"""High-precision spot audit of the actual-source shifted-Gaussian formula.

This is a numerical cross-check, not an interval proof. It compares two source
quadratures, three prime cutoffs, and the first 60 verified critical-line zeros.
"""

import json
import math
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60
POINTS = [
    ("small-zero", mp.mpf("0.08"), mp.mpf("0")),
    ("transition-zero", mp.mpf("0.275"), mp.mpf("0")),
    ("transition-middle", mp.mpf("0.275"), mp.mpf("5")),
    ("transition-far", mp.mpf("0.275"), mp.mpf("15")),
    ("transition-edge", mp.mpf("0.275"), mp.mpf("25")),
    ("false-near-contact", mp.mpf("0.943562886148058"), mp.mpf("6.6")),
    ("large-middle", mp.mpf("2"), mp.mpf("10")),
]
CUTOFFS = (500_000, 1_000_000, 2_000_000)


def von_mangoldt_table(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    terms = []
    for p in range(2, limit + 1):
        if sieve[p]:
            lp = mp.log(p)
            n = p
            while n <= limit:
                terms.append((n, lp, mp.log(n)))
                if n > limit // p:
                    break
                n *= p
    terms.sort()
    return terms


def endpoint(t, x):
    return mp.exp(t / 4 - t * x * x) * mp.cos(t * x)


def gamma_transformed(t, x, radius=None):
    root = mp.sqrt(t)
    def integrand(y):
        return mp.exp(-y*y) * mp.re(mp.digamma(mp.mpf("0.25") + mp.j*(x + y/root)/2))
    if radius is None:
        val = mp.quad(integrand, [-mp.inf, 0, mp.inf])
    else:
        val = mp.quad(integrand, [-radius, 0, radius])
    return -mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t)) + val/(4*mp.pi*root)


def prime_sum(t, x, terms, cutoff):
    total = mp.mpf("0")
    for n, lp, ln in terms:
        if n > cutoff:
            break
        total += lp/mp.sqrt(n) * mp.exp(-(ln*ln)/(4*t)) * mp.cos(x*ln)
    return -total/(2*mp.sqrt(mp.pi*t))


terms = von_mangoldt_table(max(CUTOFFS))
zeros = [mp.im(mp.zetazero(k)) for k in range(1, 61)]
rows = []
for label, t, x in POINTS:
    g_inf = gamma_transformed(t, x)
    g_12 = gamma_transformed(t, x, mp.mpf(12))
    prime_values = [prime_sum(t, x, terms, cutoff) for cutoff in CUTOFFS]
    source = endpoint(t, x) + g_inf + prime_values[-1]
    zero_side = mp.fsum(
        (mp.exp(-t*(gamma-x)**2) + mp.exp(-t*(gamma+x)**2))/2
        for gamma in zeros
    )
    rows.append({
        "label": label,
        "t": mp.nstr(t, 20),
        "xi": mp.nstr(x, 20),
        "endpoint": mp.nstr(endpoint(t, x), 30),
        "gamma_infinite": mp.nstr(g_inf, 30),
        "gamma_radius_12": mp.nstr(g_12, 30),
        "gamma_difference": mp.nstr(abs(g_inf-g_12), 8),
        "prime_by_cutoff": {str(c): mp.nstr(v, 30) for c, v in zip(CUTOFFS, prime_values)},
        "last_cutoff_difference": mp.nstr(abs(prime_values[-1]-prime_values[-2]), 8),
        "source_value": mp.nstr(source, 30),
        "first_60_zero_value": mp.nstr(zero_side, 30),
        "source_zero_difference": mp.nstr(source-zero_side, 12),
    })

result = {
    "schema": "marici.high-precision-source-spot-audit.v1",
    "certified": False,
    "decimal_digits": mp.mp.dps,
    "zero_count": len(zeros),
    "rows": rows,
    "limitations": [
        "mpmath quadrature is not interval enclosed",
        "prime cutoff tail is estimated only by cutoff comparison",
        "zero-side tail is not formally bounded",
        "zero-side comparison uses the first 60 computed critical-line zeros",
    ],
}
out = Path(__file__).parents[1] / "results" / "high-precision-source-spot-audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({r["label"]: {"source": r["source_value"], "zeros": r["first_60_zero_value"], "delta": r["source_zero_difference"]} for r in rows}, indent=2))
