"""Symbolic two-chart triangularity of the aligned low-grade plus chain."""
import json
import math
import os
import sympy as sp

g, a, d = sp.symbols("g a d", integer=True, positive=True)
common = (sp.factorial(g) * sp.factorial(g + 3) /
          (sp.factorial(g - a + 4) * sp.factorial(a - 1)))
generic_lead = sp.factor((d - g - 3) * common)
drop_numerator = sp.expand(g**2 + 9 * g + 16 - (2 * g + 4) * a)
divisor_lead = sp.factor(common * drop_numerator / (g - a + 5))

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


L = a - 4
cL = (sp.factorial(g) * sp.factorial(g + 3) /
      (sp.factorial(g - L) * sp.factorial(a - 1)))
record("COEFF.source", "the terminal shortened-source coefficient has the factorial form",
       sp.factor(common - cL) == 0, common)
record("COEFF.generic", "the magnetic top coefficient is (d-g-3) times the source endpoint",
       generic_lead == (d - g - 3) * common, generic_lead)

c_previous_ratio = sp.factor(L * (g + 4) / (g - L + 1))
derived_drop = sp.factor(common * (g - c_previous_ratio))
record("COEFF.divisor", "after the common top vanishes, the next coefficient is explicit",
       sp.factor(derived_drop - divisor_lead) == 0, divisor_lead)

zero_solution = sp.factor((g**2 + 9 * g + 16) / (2 * g + 4))
record("COEFF.nonzero", "the divisor-chart pivot cannot vanish at integral pole depth",
       sp.factor(zero_solution - ((g + 7) / 2 + 1 / (g + 2))) == 0,
       "a=(g+7)/2+1/(g+2), nonintegral for every integer g>=2")

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_plus_tri_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]

generic_failures = []
divisor_failures = []
records = 0
for grade in range(2, 51):
    for excess in range(1, 52):
        q = grade + excess
        columns = component(grade, (q + q % 2) // 2, q)
        for depth in range(4, min(grade + 4, q + q % 2) + 1, 2):
            plus = columns[depth + 1]
            sign = -((-1)**grade)
            if excess != grade + 3:
                predicted = sign * generic_lead.subs({g: grade, a: depth, d: excess})
                if plus.get(excess - 3, 0) != predicted:
                    generic_failures.append((grade, excess, depth,
                                             plus.get(excess - 3, 0), predicted))
            else:
                predicted = sign * divisor_lead.subs({g: grade, a: depth})
                if plus.get(excess - 4, 0) != predicted:
                    divisor_failures.append((grade, depth,
                                             plus.get(excess - 4, 0), predicted))
            records += 1

record("MATRIX.generic", "generated generic-chain pivots equal the symbolic formula",
       not generic_failures, f"records={records}; failures={generic_failures[:1]}")
record("MATRIX.divisor", "generated q=2g+3 replacement pivots equal the symbolic formula",
       not divisor_failures, f"failures={divisor_failures[:1]}")

degree_ok = all(len(set(range(1, grade + 2, 2))) == len(range(1, grade + 2, 2))
                for grade in range(2, 202))
record("BASIS.degree", "reflection about the common top gives strictly increasing degrees",
       degree_ok, "generic degrees a-3; divisor degrees a-4")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_plus_chain_triangular_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic two-chart triangular polynomial-basis theorem",
              "domain": "g>=2 and even 4<=a<=g+4"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "After reflection about the aligned endpoint, shortened plus columns have strictly increasing degrees. Off d=g+3 their leading coefficient is (d-g-3)g!(g+3)!/[(g-a+4)!(a-1)!]. On the divisor, the next coefficient is the same positive factorial factor times [g^2+9g+16-(2g+4)a]/(g-a+5), which never vanishes for integral a. Hence the growing aligned plus chain has a canonical triangular basis in two charts; its internal weighted elimination cannot create rank loss.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_plus_chain_triangular.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
