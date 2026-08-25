"""Constructor explanation of the grade-two q=1 magnetic circuit."""
import json
import math
import os
import sympy as sp


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def path_coefficients(g, a, m):
    source = [math.comb(g, j) * (-1) ** (g - j) *
              rising(a, g - j) * rising(4 - a, j)
              for j in range(g + 1)]
    output = [m * source[0]]
    output += [(m + j) * source[j] +
               (m + j - 1 - g) * source[j - 1]
               for j in range(1, g + 1)]
    output.append(m * source[g])
    return output


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m)) if value}


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


columns = [canonical_column(2, 0, -2), canonical_column(2, 0, 0)]
rows = sorted(set(columns[0]) | set(columns[1]))
matrix = sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])
record("SUPPORT.one", "both grade-two q=1 states collapse to the single row R1",
       rows == [1], rows)
record("STATE.equal", "the two surviving observation records are identical",
       matrix == sp.Matrix([[-40, -40]]), matrix.tolist())
primitive = sp.Matrix([1, -1])
record("CIRCUIT.primitive", "the unique primitive circuit is (1,-1)",
       matrix * primitive == sp.zeros(1, 1), primitive.T.tolist())

g = sp.symbols("g", integer=True, positive=True)
carrier = (g - 2) * sp.rf(4, g)
generated_failures = []
for grade in range(2, 21):
    plus = canonical_column(grade, 0, 2 - grade)
    if plus.get(2, 0) != carrier.subs(g, grade):
        generated_failures.append((grade, plus.get(2, 0), carrier.subs(g, grade)))
record("JET.carrier", "the second q=1 observation has carrier (g-2)*rf(4,g)",
       not generated_failures, f"2<=g<=20; failures={generated_failures[:1]}")
record("JET.unique_loss", "the carrier vanishes in the domain exactly at grade two",
       [grade for grade in range(2, 101) if carrier.subs(g, grade) == 0] == [2],
       carrier)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_e1_circuit_explanation_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact local constructor explanation",
              "locus": {"g": 2, "q": 1}},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The q=1 component has a second observation carried by (g-2)*rf(4,g), so it disappears uniquely at grade two. The two remaining source states then have the identical R1 record -40, forcing the primitive circuit (1,-1) and hence 1-zb^-2.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_e1_circuit_explanation.json"),
          "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
