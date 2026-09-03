"""Numerical source-side scout of the {1,2,3,6} Weil Gaussian rectangle.

Discovery evidence only: mpmath quadrature and a Gaussian prime-tail cutoff are
not directed interval certificates.
"""

import json
import math
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

DISPLACEMENTS = [mp.mpf("0"), mp.log(2), mp.log(3), mp.log(6), mp.log(mp.mpf(3) / 2)]
TIMES = [mp.mpf(x) for x in ("0.03", "0.05", "0.08", "0.12", "0.16", "0.2")]
TAIL_EXPONENT = mp.mpf(100)


def von_mangoldt_table(limit: int):
    values = [mp.mpf("0") for _ in range(limit + 1)]
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        logp = mp.log(p)
        power = p
        while power <= limit:
            values[power] = logp
            if power > limit // p:
                break
            power *= p
        start = p * p
        if start <= limit:
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return values


def cutoff_for(t, max_a):
    log_cutoff = max_a + mp.sqrt(4 * t * TAIL_EXPONENT)
    return int(mp.ceil(mp.e ** log_cutoff))


def gamma_term(t, a):
    constant = -mp.log(mp.pi) / (4 * mp.sqrt(mp.pi * t)) * mp.e ** (-a * a / (4 * t))

    def integrand(u):
        return (
            mp.e ** (-t * u * u)
            * mp.cos(a * u)
            * mp.re(mp.digamma(mp.mpf("0.25") + mp.j * u / 2))
        )

    integral = 2 * mp.quad(integrand, [0, mp.inf])
    return constant + integral / (4 * mp.pi)


def prime_term(t, a, mangoldt):
    total = mp.mpf("0")
    for n in range(2, len(mangoldt)):
        lam = mangoldt[n]
        if not lam:
            continue
        logn = mp.log(n)
        total += lam / mp.sqrt(n) * (
            mp.e ** (-(logn - a) ** 2 / (4 * t))
            + mp.e ** (-(logn + a) ** 2 / (4 * t))
        )
    return -total / (4 * mp.sqrt(mp.pi * t))


def endpoint_term(t, a):
    return mp.e ** (t / 4) * mp.cosh(a / 2)


def source_kernel(t, a, mangoldt):
    return endpoint_term(t, a) + gamma_term(t, a) + prime_term(t, a, mangoldt)


def as_text(value):
    return mp.nstr(value, 18)


def main():
    rows = []
    for t in TIMES:
        cutoff = cutoff_for(t, max(DISPLACEMENTS))
        mangoldt = von_mangoldt_table(cutoff)
        values = {as_text(a): source_kernel(t, a, mangoldt) for a in DISPLACEMENTS}
        k0 = values[as_text(DISPLACEMENTS[0])]
        normalized = [values[as_text(a)] / k0 for a in DISPLACEMENTS]
        _, r, s, c, d = normalized
        d_plus = (1 + c) * (1 + d) - (r + s) ** 2
        d_minus = (1 - c) * (1 - d) - (r - s) ** 2
        rows.append(
            {
                "t": as_text(t),
                "prime_cutoff": cutoff,
                "K0": as_text(k0),
                "r_log2": as_text(r),
                "s_log3": as_text(s),
                "c_log6": as_text(c),
                "d_log3_over_2": as_text(d),
                "D_plus": as_text(d_plus),
                "D_minus": as_text(d_minus),
                "sample_positive": bool(k0 > 0 and d_plus >= 0 and d_minus >= 0),
            }
        )

    result = {
        "schema": "marici.grothendieck.gaussian-translation-weil-rectangle-scout.v1",
        "status": "discovery_only",
        "tail_exponent_cutoff": as_text(TAIL_EXPONENT),
        "rows": rows,
        "all_sampled_rectangles_positive": all(row["sample_positive"] for row in rows),
        "claim_boundary": "Non-directed mpmath quadrature and truncated prime sum; no certified sign or RH claim.",
    }
    output = Path(__file__).parents[1] / "results" / "gaussian-translation-weil-rectangle-scout.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
