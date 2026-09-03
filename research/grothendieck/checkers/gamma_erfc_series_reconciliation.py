"""Reconcile the gamma heat integral with its accelerated erfc series."""
from __future__ import annotations

import json
from pathlib import Path
import mpmath as mp


def integral_value(t: mp.mpf) -> mp.mpf:
    f = lambda r: (mp.exp(-r) - mp.exp(-r / 4 - r * r / (16 * t))) / (-mp.expm1(-r))
    return mp.quad(f, [0, 1, mp.inf])


def odd_double_factorial(k: int) -> int:
    if k == 0:
        return 1
    value = 1
    for j in range(1, k + 1):
        value *= 2 * j - 1
    return value


def accelerated_series(t: mp.mpf, cutoff: int, terms: int) -> mp.mpf:
    total = mp.mpf("0")
    for m in range(cutoff):
        a = mp.mpf(m) + mp.mpf(1) / 4
        x = 2 * mp.sqrt(t) * a
        scaled_erfc = mp.exp(x * x) * mp.erfc(x)
        total += 1 / mp.mpf(m + 1) - 2 * mp.sqrt(mp.pi * t) * scaled_erfc

    a0 = mp.mpf(cutoff) + mp.mpf(1) / 4
    tail = mp.digamma(a0) - mp.digamma(cutoff + 1)
    for k in range(1, terms):
        coefficient = (-1) ** (k + 1) * odd_double_factorial(k) / (8 * t) ** k
        tail += coefficient * mp.zeta(2 * k + 1, a0)
    return total + tail


def main() -> None:
    mp.mp.dps = 80
    cutoff = 200
    asymptotic_terms = 7
    values = []
    for text in ("0.001", "0.004", "0.01", "0.025", "0.05", "0.08"):
        t = mp.mpf(text)
        direct = integral_value(t)
        series = accelerated_series(t, cutoff, asymptotic_terms)
        first_omitted_k = asymptotic_terms
        a0 = mp.mpf(cutoff) + mp.mpf(1) / 4
        omitted_bound = (
            odd_double_factorial(first_omitted_k)
            / (8 * t) ** first_omitted_k
            * mp.zeta(2 * first_omitted_k + 1, a0)
        )
        decreasing_ratio_bound = (2 * first_omitted_k + 1) / (8 * t * a0**2)
        residual = series - direct
        assert abs(residual) <= omitted_bound
        assert decreasing_ratio_bound < 1
        values.append({
            "t": text,
            "direct_integral": mp.nstr(direct, 30),
            "accelerated_series": mp.nstr(series, 30),
            "residual": mp.nstr(residual, 12),
            "first_omitted_tail_bound": mp.nstr(omitted_bound, 12),
            "decreasing_ratio_bound": mp.nstr(decreasing_ratio_bound, 12),
        })
    result = {
        "cutoff": cutoff,
        "asymptotic_terms": asymptotic_terms,
        "certified": False,
        "values": values,
    }
    output = Path(__file__).parents[1] / "results" / "gamma-erfc-series-reconciliation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
