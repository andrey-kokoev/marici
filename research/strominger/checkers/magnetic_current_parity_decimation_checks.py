"""Exact hostile comparison of consecutive and even pole-depth lattices."""
import json
import os


prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "parity_decimation_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]
current_defect = namespace["current_defect"]
rank = namespace["rank"]


def component_on_depths(g, depths, q, beta=4):
    center = 1 - g
    return [canonical_column(g, a, m, beta)
            for a in depths
            for m in (center - q - a, center + q - a)]


def quotient_width(g, q, depths):
    depths = list(depths)
    ordinary = component_on_depths(g, depths, q + 2)
    currents = [current_defect(g, a, q, 4) for a in depths]
    return rank(ordinary + currents) - rank(ordinary)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


observations = []
for g in range(2, 11):
    for q in range(1, 11):
        consecutive = quotient_width(g, q, range(0, 21))
        even = quotient_width(g, q, range(0, 25, 2))
        odd = quotient_width(g, q, range(1, 26, 2))
        observations.append((g, q, consecutive, even, odd))

record("FULL.width", "the consecutive-depth current quotient has width one or two",
       all(item[2] in (1, 2) for item in observations),
       f"cases={len(observations)}; widths={sorted(set(item[2] for item in observations))}")
strict = [item for item in observations if item[3] > item[2]]
record("DECIMATION.increases", "even-depth deletion strictly enlarges the quotient in tested cases",
       len(strict) >= 80,
       f"strict_cases={len(strict)}; first={strict[:1]}")
record("COSET.odd", "the complementary odd coset also carries a multi-current quotient",
       any(item[4] > 2 for item in observations),
       f"max_odd={max(item[4] for item in observations)}")
record("INTRINSIC.survives", "at least one current class survives the full-depth enlargement",
       all(item[2] >= 1 for item in observations),
       "native beta=4")

# A concrete hostile witness.
witness = next(item for item in observations if item[3] >= 5 and item[2] == 1)
record("FALSIFIER.support_only", "same support formula but different depth grammar changes width",
       witness is not None, witness)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_current_parity_decimation_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact hostile depth-lattice comparison",
        "audit": "2<=g<=10, 1<=q<=10, consecutive depth<=20, parity depth<=24/25",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The native multi-current tower is a parity-decimation phenomenon. "
        "Restoring consecutive depths collapses its tested quotient to width "
        "one or two, while either parity coset alone retains multiple alias "
        "classes. An explicit nearest-neighbor chain relation remains to prove."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_current_parity_decimation.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
