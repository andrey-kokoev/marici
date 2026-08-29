"""Exact bounded checker for the two-wedge full-depth current conjecture."""
import json
import os


prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "two_wedge_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]
current_defect = namespace["current_defect"]
rank = namespace["rank"]


def component(g, cutoff, q):
    center = 1 - g
    return [canonical_column(g, a, m, 4)
            for a in range(cutoff + 1)
            for m in (center - q - a, center + q - a)]


def width(g, q, cutoff=30):
    ordinary = component(g, cutoff, q + 2)
    currents = [current_defect(g, a, q, 4)
                for a in range(cutoff + 1)]
    return rank(ordinary + currents) - rank(ordinary)


def predicted_width(g, q):
    high = q >= 2 * g + 1
    low = g >= 4 and min(3, g - 3) <= q <= g - 3
    return 2 if high or low else 1


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


observations = []
failures = []
for g in range(2, 13):
    for q in range(1, 21):
        actual = width(g, q)
        expected = predicted_width(g, q)
        observations.append((g, q, actual, expected))
        if actual != expected:
            failures.append((g, q, actual, expected))

record("WEDGE.formula", "all full-depth widths obey the two-wedge formula",
       not failures, f"cases={len(observations)}; failures={failures[:1]}")
record("WEDGE.high", "the high boundary q=2g+1 has width two",
       all(width(g, 2 * g + 1) == 2 for g in range(2, 10)),
       "2<=g<=9")
record("WEDGE.high_outside", "the adjacent point q=2g has width one outside the low wedge",
       all(width(g, 2 * g) == 1 for g in range(2, 10)),
       "sharp high boundary")
record("WEDGE.low", "every admitted low-wedge point has width two",
       all(width(g, q) == 2
           for g in range(4, 13)
           for q in range(min(3, g - 3), g - 2)),
       "sharp reflected collision band")
record("WEDGE.middle", "a nonempty middle width-one band separates the wedges",
       all(width(g, q) == 1
           for g in range(6, 10)
           for q in range(g - 2, 2 * g + 1)),
       "g-2<=q<=2g")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_full_depth_two_wedge_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact rational-rank conjecture",
        "audit": "2<=g<=12, 1<=q<=20, consecutive cutoff N=30",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The consecutive-depth current cokernel has width two exactly on a "
        "high separation wedge and a low collision wedge in the bounded audit; "
        "the intervening band has one intrinsic current class."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_full_depth_two_wedge.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
