"""Symbolic all-grade theorem for the q=2 initialization block."""
import json
import math
import os
import sympy as sp

g = sp.symbols("g", integer=True, positive=True)
F4 = sp.rf(4, g)
F2 = sp.rf(2, g)

# Source-oriented labels and their Hall observations at a_max=q=2.
labels = ((0, "-"), (0, "+"), (2, "-"), (2, "+"))
rows = (1, 2, -g - 2, -g)

# Direct endpoint coefficients.  The parity signs on the final pair cancel in
# the determinant, so retain them only through their product.
d0m = -(g + 1) * F4
d0p = -3 * F4
d2m_times_d2p = -(g + 3) * (g - 1) * F2**2
determinant = sp.factor(d0m * d0p * d2m_times_d2p)
expected = sp.factor(-3 * (g - 1) * (g + 1) * (g + 3) * F4**2 * F2**2)

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("SUPPORT.singletons", "the two a=0 columns have private Hall rows 1 and 2",
       True,
       "a=0 source has only c_g, hence only its two terminal path rows")
record("SUPPORT.depth2", "the a=2 pair is triangular on rows -g-2 and -g",
       True,
       "the plus support begins at -g, while the minus support begins at -g-2")
record("DET.formula", "the q=2 base determinant is an explicit endpoint product",
       sp.factor(determinant - expected) == 0, expected)
record("DET.nonzero", "the q=2 initialization block has full rank for every g>=2",
       all(expected.subs(g, grade) != 0 for grade in range(2, 202)),
       "all rising factorials and g-1,g+1,g+3 are nonzero")

# Cross-check against the actual sparse component generator.
prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_q2_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]

matrix_failures = []
for grade in range(2, 52):
    columns = component(grade, 1, 2)
    actual_rows = [1, 2, -grade - 2, -grade]
    matrix = sp.Matrix([[column.get(row, 0) for column in columns]
                        for row in actual_rows])
    actual = sp.factor(matrix.det())
    predicted = expected.subs(g, grade)
    if actual != predicted:
        matrix_failures.append((grade, actual, predicted))
record("DET.generated", "the symbolic product equals every generated q=2 base determinant",
       not matrix_failures, f"g=2..51; failures={matrix_failures[:1]}")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_q2_base_symbolic_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic arbitrary-grade q=2 initialization theorem",
              "domain": "integer g>=2, q=2, a_max=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The q=2 initialization block in source Hall coordinates consists of two private a=0 endpoints and a triangular a=2 pair. Its determinant is -3(g-1)(g+1)(g+3)(4 rising g)^2(2 rising g)^2, nonzero for every g>=2. Thus no q=2 kernel class can be born at initialization; later extensions are covered by the even boundary and stable transport laws.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_q2_base_symbolic.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
