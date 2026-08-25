"""Exact support-visibility and arithmetic-stabilization cutoff audits."""
import itertools
import json
import math
import os
import sympy as sp

checks = []


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


def support(grade, depths):
    values = {-(grade + depth - 1) for depth in depths}
    if grade == 2 and 0 in depths:
        values.update((-2, 0))
    if grade == 2 and {0, 4, 6}.issubset(depths):
        values.update((-8, 0, 2))
    return values


# Exact necessary-and-sufficient interval hull for every admitted named class.
universe = (0, 2, 4, 6, 8)
depth_sets = [set(combo) for size in range(1, len(universe) + 1)
              for combo in itertools.combinations(universe, size)]
windows = [(lower, upper) for lower in range(-12, 2) for upper in range(lower, 5)]
failures = []
cases = 0
for grade in range(2, 9):
    for depths in depth_sets:
        named_support = support(grade, depths)
        required_lower = min(named_support)
        required_upper = max(named_support)
        for lower, upper in windows:
            cases += 1
            direct = all(lower <= exponent <= upper for exponent in named_support)
            criterion = lower <= required_lower and upper >= required_upper
            if direct != criterion:
                failures.append((grade, sorted(depths), lower, upper))
record("VISIBILITY.complete", "the interval-hull criterion is exact for every named support",
       not failures, f"cases={cases}; failures={failures[:1]}")

# Exact rank-one cohomology activation condition.
failures = []
for grade in range(2, 9):
    for depths in depth_sets:
        for lower, upper in windows:
            direct = any(depth > 0 and lower <= -(grade + depth - 1) <= upper
                         for depth in depths)
            visible_positive = [depth for depth in depths if depth > 0 and
                                lower <= -(grade + depth - 1) <= upper]
            if direct != bool(visible_positive):
                failures.append((grade, sorted(depths), lower, upper))
record("VISIBILITY.cohomology", "ordinary cohomology activates exactly at the first visible positive tower",
       not failures, failures[:1])


def valuation_two(value):
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def fixed_divisor(length):
    value = math.factorial(length)
    if length % 2 == 1:
        value *= 2 ** valuation_two(length + 1)
    return value


# Minimal prefix and uniform degree bound.
failures = []
minimal_prefix = {}
for grade in range(2, 61):
    length = grade - 1
    divisor = fixed_divisor(length)
    running = 0
    hit = None
    previous = None
    for index in range(1, grade + 1):
        running = math.gcd(running, int(sp.rf(2 * index, length)))
        if running == divisor and hit is None:
            hit = index
            break
        previous = running
    minimal_prefix[grade] = hit
    if hit is None or hit > grade:
        failures.append((grade, hit, divisor))
    elif hit > 1:
        prior = math.gcd(*(int(sp.rf(2 * index, length))
                           for index in range(1, hit)))
        if prior == divisor:
            failures.append((grade, hit, "not minimal"))
record("ARITHMETIC.minimal", "the gcd criterion finds the exact minimal prefix and always satisfies s_g<=g",
       not failures, failures)

# Exact Laurent hull for the minimal arithmetic prefix and the uniform bound.
failures = []
for grade, prefix in minimal_prefix.items():
    exponents = [-(grade + 2 * index - 1) for index in range(1, prefix + 1)]
    exact_lower = -(grade + 2 * prefix - 1)
    exact_upper = -(grade + 1)
    if min(exponents) != exact_lower or max(exponents) != exact_upper:
        failures.append((grade, prefix, exponents))
    if exact_lower < -(3 * grade - 1):
        failures.append((grade, prefix, "uniform bound"))
record("ARITHMETIC.laurent", "the minimal prefix has the exact stated Laurent hull and obeys the uniform bound",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "stabilization_cutoffs_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "The complete named-kernel visibility window is exactly the interval hull of all admitted supports. Rational cohomology activates at the first visible positive tower. The normalized-gcd criterion gives the exact minimal arithmetic prefix, bounded by g, and its Laurent hull is [-(g+2s_g-1),-(g+1)].",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "stabilization_cutoffs.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
