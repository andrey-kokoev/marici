"""Wide two-prime and exact checker for the primary-chart failure locus."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def determinant_mod(columns, rows, prime):
    n = len(columns)
    work = [[columns[j].get(rows[i], 0) % prime for j in range(n)]
            for i in range(n)]
    result = 1
    for column in range(n):
        pivot = next((i for i in range(column, n) if work[i][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result = result * value % prime
        inverse = pow(value, prime - 2, prime)
        for i in range(column + 1, n):
            if work[i][column]:
                factor = work[i][column] * inverse % prime
                for j in range(column, n):
                    work[i][j] = (work[i][j] - factor * work[column][j]) % prime
    return result % prime


def rank_mod(columns, prime):
    basis = {}
    for source in columns:
        vector = {row: value % prime for row, value in source.items() if value % prime}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                inverse = pow(vector[pivot], prime - 2, prime)
                basis[pivot] = {row: value * inverse % prime
                                for row, value in vector.items()}
                break
            factor = vector[pivot]
            for row, value in basis[pivot].items():
                updated = (vector.get(row, 0) - factor * value) % prime
                if updated:
                    vector[row] = updated
                elif row in vector:
                    del vector[row]
    return len(basis)


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


primes = (1_000_000_007, 1_000_000_009)
candidates = []
defect_loci = set()
cases = 0
for g in range(2, 16):
    for q in range(1, 51):
        for k in range(0, min(30, q // 2 + 5) + 1):
            columns = component(g, k, q)
            try:
                rows = hall_rows(columns)
            except AssertionError:
                defect_loci.add((g, q))
                continue
            if all(determinant_mod(columns, rows, prime) == 0 for prime in primes) and \
               all(rank_mod(columns, prime) == len(columns) for prime in primes):
                candidates.append((g, q, k))
            cases += 1

onsets = [(g, q, min(k for gg, qq, k in candidates if (gg, qq) == (g, q)))
          for g, q in sorted({(g, q) for g, q, _ in candidates})]
expected_onsets = [(g, 2 * g + 8, g // 2 + 4) for g in range(2, 16, 2)]
record("LOCUS.onsets", "all chart-failure onsets obey q=2g+8 and k=g/2+4",
       onsets == expected_onsets, str(onsets))
record("LOCUS.parity", "the primary-chart failure family contains only even grades",
       all(g % 2 == 0 for g, _, _ in onsets), str(onsets))
record("RANK.defects", "true rank-defect loci remain only (2,1) and (2,7)",
       defect_loci == {(2, 1), (2, 7)}, str(sorted(defect_loci)))

# Confirm each modular onset exactly and exhibit the one-row alternate chart.
exact = []
for g, q, k in onsets:
    columns = component(g, k, q)
    primary_rows = hall_rows(columns)
    primary = sp.Matrix([[item.get(row, 0) for item in columns]
                         for row in primary_rows])
    alternate_rows = [3 if row == 1 else row for row in primary_rows]
    alternate = sp.Matrix([[item.get(row, 0) for item in columns]
                           for row in alternate_rows])
    exact.append((g, q, k, int(primary.det()), int(alternate.det())))
record("EXACT.primary", "every modular onset has exactly zero primary determinant",
       all(primary == 0 for _, _, _, primary, _ in exact), str(exact))
record("EXACT.alternate", "the uniform row exchange 1->3 is nonzero at every onset",
       all(alternate != 0 for _, _, _, _, alternate in exact),
       f"confirmed={len(exact)}")
record("LOCUS.source", "the onset pole depth obeys a=2k=q-g=g+8",
       all(2 * k == q - g == g + 8 for g, q, k in onsets), str(onsets))
record("COVERAGE.wide", "the two-prime sweep covers more than twelve thousand blocks",
       cases > 12000, f"cases={cases}; candidates={len(candidates)}")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_chart_locus_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "wide finite-range arithmetic chart-locus theorem",
              "g": [2, 15], "q": [1, 50], "k_max": 30,
              "primes": list(primes)},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "The preferred maximal-minor chart has an injective zero family at even grades satisfying q=2g+8, with onset k=g/2+4 and pole depth a=q-g=g+8. Seven onsets through g=14 are confirmed exactly; replacing target row 1 by row 3 gives a nonzero alternate minor at every onset. No odd-grade chart-zero family appears, and true rank defects remain only (2,1),(2,7). This is a wide finite theorem, not a symbolic proof that the arithmetic family is exhaustive for unbounded parameters."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_chart_locus.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
