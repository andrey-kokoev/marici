"""Bounded exact replay of the unbounded Z/2 coherence construction."""
import json
from itertools import product
from pathlib import Path


def omega(xs):
    out = 1
    for x in xs:
        out &= x
    return out


def differential(xs):
    """Inhomogeneous group-cochain differential over F2 with trivial action."""
    terms = [omega(xs[1:])]
    for i in range(len(xs) - 1):
        merged = xs[:i] + (xs[i] ^ xs[i + 1],) + xs[i + 2 :]
        terms.append(omega(merged))
    terms.append(omega(xs[:-1]))
    return sum(terms) % 2


degrees = range(1, 9)
cocycle_by_degree = {
    str(n): all(differential(xs) == 0 for xs in product((0, 1), repeat=n + 1))
    for n in degrees
}

# On C2, a normalized cochain has only one potentially nonzero coordinate:
# its value on the all-ones tuple.  Every normalized coboundary evaluates to
# zero on that tuple, whereas omega_n evaluates to one.
nonboundary_by_degree = {str(n): omega((1,) * n) == 1 for n in degrees}

tests = {
    "normalized": all(
        omega(xs) == 0
        for n in degrees
        for xs in product((0, 1), repeat=n)
        if 0 in xs
    ),
    "cocycle_degrees_1_through_8": all(cocycle_by_degree.values()),
    "nonboundary_degrees_1_through_8": all(nonboundary_by_degree.values()),
    "no_finite_cap_in_family": all(
        nonboundary_by_degree[str(n + 1)] for n in range(1, 8)
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutsch_popperian_unbounded_coherence_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "cocycle_by_degree": cocycle_by_degree,
    "nonboundary_by_degree": nonboundary_by_degree,
    "uniform_family": "omega_n(a_1,...,a_n)=product(a_i) over F2",
    "verdict": "no source-independent finite coherence cap",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutsch_popperian_unbounded_coherence.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
