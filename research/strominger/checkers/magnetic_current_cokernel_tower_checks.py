"""Exact bounded checker for the magnetic current-cokernel tower law."""
import json
import os


prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_current_port_sewing_checks.py")
namespace = {"__file__": prefix_path, "__name__": "current_tower_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]
current_defect = namespace["current_defect"]
rank = namespace["rank"]


def column_rank(columns):
    rows = sorted({row for column in columns for row in column})
    return rank([[column.get(row, 0) for column in columns] for row in rows])


def stable_width(g, q):
    ordinary = q + 4 - min(2, max(0, (q - g + 2) // 2))
    return ordinary + (1 if (g, q) == (2, 5) else 0)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


failures = []
observations = 0
for g in range(2, 13):
    for q in range(1, 13):
        width = stable_width(g, q)
        for k in range(0, 13):
            ordinary = component(g, k, q + 2)
            currents = [current_defect(g, a, q)
                        for a in range(0, 2 * k + 1, 2)]
            actual = column_rank(ordinary + currents) - column_rank(ordinary)
            expected = min(k + 1, width)
            observations += 1
            if actual != expected:
                failures.append((g, q, k, actual, expected))

record("TOWER.formula", "all quotient dimensions obey the finite-width law",
       not failures, f"observations={observations}; failures={failures[:1]}")

g0, q0, k0 = 2, 5, 7
ordinary = component(g0, k0, q0 + 2)
currents = [current_defect(g0, a, q0)
            for a in range(0, 2 * k0 + 1, 2)]
actual = column_rank(ordinary + currents) - column_rank(ordinary)
wrong_width = q0 + 4 - min(2, max(0, (q0 - g0 + 2) // 2))
record("FALSIFIER.exception", "omitting the grade-two correction fails first at the known target circuit",
       actual == wrong_width + 1,
       {"source": [g0, q0], "target_q": q0 + 2,
        "actual": actual, "wrong_prediction": wrong_width})
record("TOWER.saturates", "the conjectured width is finite for every fixed g and q",
       all(stable_width(g, q) <= q + 5
           for g in range(2, 501) for q in range(1, 501)),
       "D_(g,q)<=q+5")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_current_cokernel_tower_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact rational rank conjecture",
        "audit": "2<=g<=12, 1<=q<=12, 0<=k<=12",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The a-indexed current classes grow one per pole depth until a finite "
        "width D_(g,q), with a unique extra direction when (g,q)=(2,5) targets "
        "the known grade-two Q=7 exceptional circuit. An unbounded triangular "
        "proof remains open."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_current_cokernel_tower.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
