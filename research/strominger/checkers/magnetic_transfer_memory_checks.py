"""Finite-range support-memory classification for nested magnetic Hall minors."""
from collections import defaultdict
import json
import math
import os


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def path_coefficients(g, a, m):
    c = [math.comb(g, j) * (-1) ** (g - j) *
         rising(a, g - j) * rising(4 - a, j) for j in range(g + 1)]
    output = [m * c[0]]
    output += [(m + j) * c[j] + (m + j - 1 - g) * c[j - 1]
               for j in range(1, g + 1)]
    output.append(m * c[g])
    return output


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    if delta == 0:
        return {}
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m)) if value}


def component(g, k, q):
    center = 1 - g
    return [canonical_column(g, a, m)
            for a in range(0, 2 * k + 1, 2)
            for m in (center - q - a, center + q - a)]


def matching(columns):
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
    size = sum(augment(column, set()) for column in range(len(columns)))
    by_column = {column: row for row, column in owner.items()}
    rows = [by_column[i] for i in range(len(columns))] if size == len(columns) else []
    return size, rows


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


nesting_failures = []
width_failures = []
saturation_failures = []
row_formula_failures = []
observed = defaultdict(list)
steps = 0
for g in range(2, 16):
    for q in range(1, 31):
        previous_rows = None
        for k in range(0, 21):
            source = component(g, k, q)
            size, rows = matching(source)
            if size < len(source):
                previous_rows = None
                continue
            if previous_rows is not None:
                prior = set(previous_rows)
                current = set(rows)
                if not prior <= current:
                    nesting_failures.append((g, q, k, sorted(prior - current)))
                added = [row for row in rows if row not in prior]
                expected_rows = {-2 * k - g,
                                 -2 * k - g + 2 * (q // 2) + 1}
                if k > q // 2 + 1 and set(added) != expected_rows:
                    row_formula_failures.append((g, q, k, added,
                                                 sorted(expected_rows)))
                touched = sorted(set(index // 2 for index, column in
                    enumerate(source[:-2]) for row in added if column.get(row, 0)))
                lag = k - min(touched) if touched else 0
                bound = q // 2
                observed[(g, q)].append(lag)
                if lag > bound:
                    width_failures.append((g, q, k, lag, touched, added))
                steps += 1
            previous_rows = rows
        if g >= 3 and max(observed[(g, q)], default=-1) != q // 2:
            saturation_failures.append((g, q, max(observed[(g, q)], default=-1)))

record("HALL.nested", "every full-Hall row set extends the preceding admitted set",
       not nesting_failures, f"steps={steps}; failures={nesting_failures[:1]}")
record("HALL.rows", "beyond the initial memory window, added rows obey the closed formula",
       not row_formula_failures,
       f"steps={steps}; failures={row_formula_failures[:1]}")
record("MEMORY.bound", "backward interaction never exceeds floor(q/2) pole pairs",
       not width_failures, f"steps={steps}; failures={width_failures[:1]}")
record("MEMORY.minimal", "the floor(q/2) bound is attained for every tested g>=3,q",
       not saturation_failures, f"pairs={13*30}; failures={saturation_failures[:1]}")
record("MEMORY.q1", "q=1 has zero backward memory, recovering scalar triangular transfer",
       all(max(observed[(g, 1)], default=0) == 0 for g in range(3, 16)),
       "3<=g<=15")
record("MEMORY.cutoff", "the memory bound remains fixed as cutoff grows through k=20",
       not width_failures and steps > 7000, f"steps={steps}")

# The smaller proposed width w-1 is genuinely falsified whenever q>=2.
first_tight = None
for g in range(3, 16):
    for q in range(2, 31):
        target = q // 2
        if target in observed[(g, q)]:
            first_tight = first_tight or (g, q, target)
record("FALSIFIER.smaller", "reducing the proposed memory by one fails on an actual interaction",
       first_tight == (3, 2, 1), f"first={first_tight}")
record("SUPPORT.inequality", "interval overlap reduces exactly to d<=floor(q/2)",
       all((2 * d <= 2 * (q // 2) + 1) == (d <= q // 2)
           for q in range(1, 101) for d in range(1, 101)),
       "1<=q,d<=100; parity identity is symbolic")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_transfer_memory_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range Hall-row theorem with symbolic support implication",
              "g": [2, 15], "q": [1, 30], "k": [0, 20]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "Nested full-Hall minors have backward pole-pair memory w(q)=floor(q/2) throughout the tested range. Their two added rows are -2k-g and -2k-g+2*floor(q/2)+1. Comparing the latter with an old path beginning at -2k-g+2d reduces overlap to 2d<=2*floor(q/2)+1, equivalently d<=floor(q/2). Thus the width follows symbolically from the observed row formula. Proving that nested Hall selection for arbitrary parameters, and constructing its transfer matrices, remain open."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_transfer_memory.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
