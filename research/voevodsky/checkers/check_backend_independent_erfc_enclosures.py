from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp


CONTRACT = Path("research/voevodsky/backend-independent-erfc-enclosures-v1.json")


def taylor_erfc_enclosure(x: mp.mpf, K: int) -> tuple[mp.mpf, mp.mpf]:
    terms = [x ** (2 * k + 1) / (mp.factorial(k) * (2 * k + 1)) for k in range(K)]
    partial_erf = 2 / mp.sqrt(mp.pi) * sum((-1) ** k * term for k, term in enumerate(terms))
    omitted = x ** (2 * K + 1) / (mp.factorial(K) * (2 * K + 1))
    ratio = x**2 * (2 * K + 1) / ((K + 1) * (2 * K + 3))
    assert ratio < 1
    absolute_tail = 2 / mp.sqrt(mp.pi) * omitted / (1 - ratio)
    center = 1 - partial_erf
    return center - absolute_tail, center + absolute_tail


def odd_double_factorial(n: int) -> int:
    return math.prod(range(1, n + 1, 2)) if n >= 1 else 1


def asymptotic_erfc_enclosure(x: mp.mpf, K: int) -> tuple[mp.mpf, mp.mpf]:
    series = sum(
        (-1) ** k * odd_double_factorial(2 * k - 1) / (2 * x**2) ** k
        for k in range(K)
    )
    next_term = mp.mpf(odd_double_factorial(2 * K - 1)) / (2 * x**2) ** K
    prefactor = mp.exp(-x**2) / (mp.sqrt(mp.pi) * x)
    approximation = prefactor * series
    remainder = prefactor * next_term
    if K % 2 == 0:
        return approximation, approximation + remainder
    return approximation - remainder, approximation


def main() -> None:
    json.loads(CONTRACT.read_text(encoding="utf-8"))
    mp.mp.dps = 80

    taylor_widths = []
    for text, K in (("0.02", 8), ("1.0", 18), ("3.0", 45), ("4.0", 65)):
        x = mp.mpf(text)
        lower, upper = taylor_erfc_enclosure(x, K)
        truth = mp.erfc(x)
        assert lower <= truth <= upper
        taylor_widths.append(upper - lower)

    asymptotic_widths = []
    for text, K in (("4.0", 8), ("6.0", 8), ("12.0", 8)):
        x = mp.mpf(text)
        lower, upper = asymptotic_erfc_enclosure(x, K)
        truth = mp.erfc(x)
        assert lower <= truth <= upper
        asymptotic_widths.append(upper - lower)

    # Both constructions overlap at x=4.
    tl, tu = taylor_erfc_enclosure(mp.mpf(4), 65)
    al, au = asymptotic_erfc_enclosure(mp.mpf(4), 8)
    assert max(tl, al) <= min(tu, au)

    result = {
        "schema":"marici.voevodsky.backend-independent-erfc-enclosures-check.v1",
        "status":"hybrid_erfc_enclosure_fixtures_verified",
        "taylor_points_checked":4,
        "asymptotic_points_checked":3,
        "overlap_at_x4":True,
        "max_taylor_width":str(max(taylor_widths)),
        "max_asymptotic_width":str(max(asymptotic_widths)),
        "high_precision_containment_only":True,
        "directed_elementary_backend":False,
        "gamma_series_interval":False,
        "source_D2_certification":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
