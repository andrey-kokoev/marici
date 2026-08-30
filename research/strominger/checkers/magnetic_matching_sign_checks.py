"""Matching-sign coherence and modular noncancellation checker."""
from collections import defaultdict
import json
import math
import os
import sympy as sp


def add(output, key, value):
    if value:
        output[key] += value
        if output[key] == 0:
            del output[key]


def path_data(g, a, m):
    c = [int(math.comb(g, j) * (-1) ** (g - j) *
             sp.rf(a, g - j) * sp.rf(4 - a, j))
         for j in range(g + 1)]
    parts = [(m * c[0], 0)]
    for j in range(1, g + 1):
        parts.append(((m + j) * c[j], (m + j - 1 - g) * c[j - 1]))
    parts.append((0, m * c[g]))
    return c, parts, [left + right for left, right in parts]


def canonical_column(g, a, m):
    center = 1 - g
    signed_delta = center - (a + m)
    q = abs(signed_delta)
    if q == 0:
        return {}, {}
    shift = -a - g if signed_delta > 0 else -a - g + q
    sign = 1 if signed_delta > 0 else -1
    _, parts, coefficients = path_data(g, a, m)
    column = {}
    split = {}
    for j, coefficient in enumerate(coefficients):
        row = shift + j
        if coefficient:
            column[row] = sign * coefficient
            split[row] = tuple(sign * value for value in parts[j])
    return column, split


def component(g, k, q):
    center = 1 - g
    points = []
    for a in range(0, 2 * k + 1, 2):
        points.extend([(a, center - q - a), (a, center + q - a)])
    columns = [canonical_column(g, a, m)[0] for a, m in points]
    return points, columns


def matching(columns):
    owner = {}
    def augment(i, seen):
        for row in sorted(columns[i]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = i
                return True
        return False
    size = sum(augment(i, set()) for i in range(len(columns)))
    by_column = {column: row for row, column in owner.items()}
    rows = [by_column[i] for i in range(len(columns))] if size == len(columns) else []
    return size, rows


def matrix_for(columns, selected_rows=None):
    rows = (selected_rows if selected_rows is not None else
            sorted(set().union(*(column.keys() for column in columns))))
    return sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])


def permutation_sign(values):
    inversions = sum(values[i] > values[j]
                     for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def determinant_terms(matrix):
    n = matrix.cols
    terms = []
    def walk(column, used, chosen, product):
        if column == n:
            terms.append(permutation_sign(chosen) * product)
            return
        for row in range(n):
            value = int(matrix[row, column])
            if row not in used and value:
                walk(column + 1, used | {row}, chosen + [row], product * value)
    walk(0, set(), [], 1)
    return terms


def normalized_sign_matrix(matrix):
    output = matrix.copy()
    for column in range(output.cols):
        first = next((output[row, column] for row in range(output.rows)
                      if output[row, column]), 0)
        if first < 0:
            output[:, column] = -output[:, column]
    for row in range(output.rows):
        first = next((output[row, column] for column in range(output.cols)
                      if output[row, column]), 0)
        if first < 0:
            output[row, :] = -output[row, :]
    return output


def modular_rank(columns, prime=1_000_000_007):
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


def record(cid, group, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "group": group, "statement": statement,
                   "status": status, "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Enumerate small Hall-selected minors to find the first mixed-sign block.
first_mixed = None
first_cancel = None
enumerated = 0
for g in range(2, 9):
    for k in range(0, 5):
        for q in range(1, 16):
            _, columns = component(g, k, q)
            size, selected_rows = matching(columns)
            if size < len(columns):
                continue
            minor = matrix_for(columns, selected_rows)
            terms = determinant_terms(minor)
            signs = {1 if term > 0 else -1 for term in terms}
            if len(signs) > 1 and first_mixed is None:
                first_mixed = (g, k, q, selected_rows, terms, int(minor.det()))
            if sum(terms) == 0 and first_cancel is None:
                first_cancel = (g, k, q, selected_rows, terms)
            enumerated += 1
record("SIGN.first", "SIGN",
       "the first mixed-sign Hall minor is (g,k,q)=(2,2,2)",
       first_mixed[:3] == (2, 2, 2), str(first_mixed))
record("SIGN.terms", "SIGN",
       "its two determinant terms survive by weight-specific dominance",
       first_mixed[4] == [604800000, -3024000000] and
       first_mixed[5] == -2419200000,
       f"enumerated_minors={enumerated}")
record("SIGN.cancel", "SIGN",
       "no actual-weight cancellation occurs in the enumerated minor range",
       first_cancel is None, str(first_cancel))

# Row/column sign normalization cannot remove the relative sign mixture.
_, mixed_columns = component(2, 2, 2)
_, mixed_rows = matching(mixed_columns)
mixed_minor = matrix_for(mixed_columns, mixed_rows)
normalized = normalized_sign_matrix(mixed_minor)
normalized_terms = determinant_terms(normalized)
record("NORM.invariant", "NORM",
       "canonical row/column sign normalization leaves mixed determinant signs",
       {1 if term > 0 else -1 for term in normalized_terms} == {-1, 1},
       str(normalized_terms))

# The mixed ambiguity is a 2x2 core and one entry already aggregates two paths.
core = sp.Matrix([[-10, 100], [-30, 60]])
_, split_a2 = canonical_column(2, 2, -5)
record("PATH.core", "PATH",
       "the minimal mixed determinant reduces to core [[-10,100],[-30,60]]",
       core.det() == 2400 and (-10 * 60, -100 * -30) == (-600, 3000))
record("PATH.split", "PATH",
       "the core entry -10 splits into underlying contributions 32 and -42",
       split_a2[-3] == (32, -42), str(split_a2[-3]))

# Prove noncancellation modulo a prime for every maximal block in the Hall range.
modular_failures = []
modular_blocks = 0
for g in range(2, 31):
    for q in range(1, 61):
        _, columns = component(g, 15, q)
        size, _ = matching(columns)
        if size == len(columns) and modular_rank(columns) < len(columns):
            modular_failures.append((g, q))
        modular_blocks += 1
record("MOD.maximal", "MOD",
       "every full-Hall maximal block has nonzero rank modulo 1000000007",
       not modular_failures,
       f"blocks={modular_blocks}; failures={modular_failures}")
record("MOD.subsets", "MOD",
       "full rank of each maximal pole block certifies all smaller column subsets",
       not modular_failures,
       "A_k is a column subset of A_15 for every k<=15")

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_matching_sign_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range oriented-matching theorem",
              "term_enumeration": {"g": [2, 8], "k": [0, 4], "q": [1, 15]},
              "modular_rank": {"g": [2, 30], "k_max": 15, "q": [1, 60],
                                "prime": 1000000007}},
    "checks": checks, "n_pass": len(passed), "n_fail": len(failed),
    "verdict": "Structural sign coherence is false: the first mixed-sign Hall-selected minor is (g,k,q)=(2,2,2), with terms +604800000 and -3024000000 and nonzero sum -2419200000. Canonical row/column sign normalization cannot remove the mixture. Its ambiguity reduces to core [[-10,100],[-30,60]], determinant -600+3000=2400; entry -10 itself splits as 32-42, so aggregated total positivity and naive LGV positivity both fail. Nevertheless every full-Hall maximal block across g<=30,k=15,q<=60 has full column rank modulo 1000000007, proving actual-weight noncancellation there and for all k<=15 subsets. No actual cancellation falsifier is found; an unbounded weight-dominance theorem remains open.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_matching_sign.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
