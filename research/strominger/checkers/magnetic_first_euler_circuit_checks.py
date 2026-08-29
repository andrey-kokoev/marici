"""Exact test of the proposed universal first Euler cap circuit."""
import json
import math
import os

prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "first_euler_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]


def add_scaled(total, column, scalar):
    for row, value in column.items():
        total[row] = total.get(row, 0) + scalar * value
        if not total[row]:
            del total[row]


def branch_column(beta, g, q, depth, branch):
    center = 1 - g
    displacement = q + 2
    m = (center - displacement - depth
         if branch == "minus"
         else center + displacement - depth)
    return canonical_column(g, depth, m, beta)


rows = []
failures = []
for beta in range(2, 9):
    for g in range(2, 21):
        q = g + beta - 2
        total = {}
        coefficients = {
            (beta + 1, "plus"): beta,
            (beta, "plus"): g + beta - 1,
            (0, "minus"): (-1) ** g * (g - 1),
        }
        for (depth, branch), scalar in coefficients.items():
            add_scaled(total, branch_column(beta, g, q, depth, branch),
                       scalar)
        gcd = math.gcd(*[abs(value) for value in coefficients.values()])
        row = {
            "beta": beta,
            "g": g,
            "q": q,
            "coefficients": {
                f"{depth},{branch}": value
                for (depth, branch), value in coefficients.items()
            },
            "primitive_gcd": gcd,
            "residual": {str(key): value
                         for key, value in sorted(total.items())},
        }
        rows.append(row)
        if total:
            failures.append(row)

output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_first_euler_circuit_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "exact integer column identity",
        "audit": "2<=beta<=8, 2<=g<=20",
    },
    "identity": (
        "beta P_(beta+1) + (g+beta-1) P_beta "
        "+ (-1)^g (g-1) M_0 = 0 at q=g+beta-2"
    ),
    "case_count": len(rows),
    "failures": failures,
    "all_relations_zero": not failures,
    "primitive_divisor_formula_holds": all(
        row["primitive_gcd"] == math.gcd(row["beta"], row["g"] - 1)
        for row in rows),
    "rows": rows,
    "verdict": (
        "The first Euler threshold hole is an explicit three-column circuit "
        "for every tested beta and grade."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_first_euler_circuit.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(json.dumps({
    "case_count": len(rows),
    "failure_count": len(failures),
    "primitive_divisor_formula_holds": output["primitive_divisor_formula_holds"],
}, sort_keys=True))
raise SystemExit(0 if not failures else 1)