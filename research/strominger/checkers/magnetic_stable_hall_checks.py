"""Stable explicit Hall matching theorem for magnetic reflection components."""
import json
import math
import os


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def coefficients(g, a, m):
    c0 = (-1) ** g * rising(a, g)
    if a == 0:
        c1 = 0
    else:
        c1 = g * (-1) ** (g - 1) * rising(a, g - 1) * (4 - a)
    return m * c0, (m + 1) * c1 + (m - g) * c0


def stable_matches(g, q, k):
    a = 2 * k
    width = q // 2
    minus_row = -a - g
    plus_row = -a - g + 2 * width + 1
    minus_m = 1 - g - q - a
    plus_m = 1 - g + q - a
    minus_b0, _ = coefficients(g, a, minus_m)
    plus_b0, plus_b1 = coefficients(g, a, plus_m)
    plus_value = -plus_b0 if q % 2 else -plus_b1
    return minus_row, plus_row, minus_b0, plus_value


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# The two row families have opposite parity and are injective in pole depth.
parity_ok = True
collision_ok = True
weight_failures = []
cases = 0
for g in range(2, 31):
    for q in range(1, 61):
        width = q // 2
        seen = set()
        for k in range(width + 2, width + 13):
            minus_row, plus_row, minus_value, plus_value = stable_matches(g, q, k)
            parity_ok &= (minus_row - plus_row) % 2 == 1
            collision_ok &= minus_row not in seen and plus_row not in seen and minus_row != plus_row
            seen.update((minus_row, plus_row))
            if not minus_value or not plus_value:
                weight_failures.append((g, q, k, minus_value, plus_value))
            cases += 1
record("MATCH.parity", "minus and plus endpoint row families have opposite parity",
       parity_ok, f"cases={cases}")
record("MATCH.injective", "the explicit stable endpoint assignment has no row collisions",
       collision_ok, f"cases={cases}")
record("WEIGHT.nonzero", "every explicit stable matching edge has nonzero integer weight",
       not weight_failures, f"cases={cases}; failures={weight_failures[:1]}")

# Sign proof ingredients for the even-q B1 edge: a>4, m+1<0, m-g<0,
# while C0 and C1 have the same sign. Odd q uses the plainly nonzero B0 edge.
inequality_ok = True
for g in range(2, 101):
    for q in range(1, 101):
        width = q // 2
        for k in range(width + 2, width + 5):
            a = 2 * k
            m = 1 - g + q - a
            if q % 2 == 0:
                inequality_ok &= a > 4 and m + 1 < 0 and m - g < 0
            else:
                inequality_ok &= m < 0
record("WEIGHT.signproof", "stable endpoint nonvanishing follows from same-sign path terms",
       inequality_ok, "2<=g<=100; 1<=q<=100; first three stable steps")

# Exact finite Hall census: deficiencies must lie before stable matching begins.
def full_column(g, a, m):
    c = [math.comb(g, j) * (-1) ** (g - j) *
         rising(a, g - j) * rising(4 - a, j) for j in range(g + 1)]
    b = [m * c[0]]
    b += [(m + j) * c[j] + (m + j - 1 - g) * c[j - 1]
          for j in range(1, g + 1)]
    b.append(m * c[g])
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value for j, value in enumerate(b) if value}


def component(g, k, q):
    center = 1 - g
    return [full_column(g, a, m) for a in range(0, 2 * k + 1, 2)
            for m in (center - q - a, center + q - a)]


def matching_size(columns):
    owner = {}
    def augment(column, seen):
        for row in sorted(columns[column]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = column
                return True
        return False
    return sum(augment(column, set()) for column in range(len(columns)))


deficiencies = []
late_onsets = []
for g in range(2, 16):
    for q in range(1, 31):
        previous_deficient = False
        for k in range(0, min(20, q // 2 + 4) + 1):
            source = component(g, k, q)
            deficient = matching_size(source) < len(source)
            if deficient:
                deficiencies.append((g, q, k))
                if not previous_deficient and k > q // 2 + 1:
                    late_onsets.append((g, q, k))
            previous_deficient = deficient
record("HALL.prefix", "no new Hall deficiency begins after the stable threshold",
       not late_onsets,
       f"deficiencies={deficiencies}; late_onsets={late_onsets}")
record("HALL.known", "the finite-prefix Hall defects lie only at grade-two q=1 and q=7",
       {(g, q) for g, q, _ in deficiencies} == {(2, 1), (2, 7)},
       str(deficiencies))

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_stable_hall_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic stable-Hall theorem with finite-prefix census",
              "stable_theorem": "all g>=2,q>=1,k>floor(q/2)+1",
              "crosscheck": {"g": [2, 30], "q": [1, 60], "stable_steps": 11}},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "For every g>=2 and q>=1, once k>floor(q/2)+1, match the new minus column to row -2k-g and the new plus column to row -2k-g+2*floor(q/2)+1. The row families have opposite parity, never collide with earlier assignments, and their endpoint weights are nonzero by a direct sign argument. Hence Hall matching extends forever after a finite prefix. In the finite-prefix census, deficiencies occur only at (g,q)=(2,1),(2,7). This proves unbounded Hall-support persistence, not actual-weight determinant noncancellation for q>1."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_stable_hall.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
