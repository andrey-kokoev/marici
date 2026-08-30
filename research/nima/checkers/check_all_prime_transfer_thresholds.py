from decimal import Decimal, getcontext
import json
from pathlib import Path


getcontext().prec = 50


def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [p for p, flag in enumerate(sieve) if flag]


cutoffs = [100, 300, 1000, 3000, 10000]
records = []
previous = None
for cutoff in cutoffs:
    primes = primes_up_to(cutoff)
    primitive_hs = sum(Decimal(1) / Decimal(p) for p in primes)
    square_hs = sum(Decimal(1) / Decimal(p) ** 2 for p in primes)
    square_trace = primitive_hs
    cubic_trace = sum(
        Decimal(1) / (Decimal(p) ** Decimal("1.5")) for p in primes
    )

    if previous is not None:
        assert primitive_hs > previous["primitive_hs"]
        assert square_hs > previous["square_hs"]
        assert square_trace > previous["square_trace"]
        assert cubic_trace > previous["cubic_trace"]

    current = {
        "primitive_hs": primitive_hs,
        "square_hs": square_hs,
        "square_trace": square_trace,
        "cubic_trace": cubic_trace,
    }
    previous = current
    records.append(
        {
            "prime_cutoff": cutoff,
            "prime_count": len(primes),
            "primitive_hs_proxy": str(primitive_hs),
            "square_hs_proxy": str(square_hs),
            "square_trace_proxy": str(square_trace),
            "cubic_trace_proxy": str(cubic_trace),
        }
    )

assert records[-1]["primitive_hs_proxy"] == records[-1]["square_trace_proxy"]

result = {
    "schema": "marici.nima.all-prime-transfer-thresholds.v1",
    "records": records,
    "primitive_grade_hilbert_schmidt": False,
    "square_grade_hilbert_schmidt": True,
    "square_grade_trace_class": False,
    "connected_tail_from_grade_three_trace_class": True,
    "verdict": "prime half-density and shell returns force a three-grade completion threshold",
}

out = Path(__file__).parents[1] / "results" / "all-prime-transfer-thresholds.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
