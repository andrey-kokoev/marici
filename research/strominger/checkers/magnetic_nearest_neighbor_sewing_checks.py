"""Exact rank-stratum audit for first nearest-neighbor current sewing."""
import json
import os


prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "neighbor_sewing_prefix"}
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


def sewn(g, q, cutoff):
    ordinary = component(g, cutoff, q + 2)
    k0 = current_defect(g, 0, q, 4)
    k1 = current_defect(g, 1, q, 4)
    return rank(ordinary + [k0, k1]) == rank(ordinary + [k0])


def current_width(g, q, cutoff=20):
    ordinary = component(g, cutoff, q + 2)
    currents = [current_defect(g, a, q, 4)
                for a in range(cutoff + 1)]
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
        width = current_width(g, q)
        first = next((cutoff for cutoff in range(1, 21)
                      if sewn(g, q, cutoff)), None)
        observations.append({
            "g": g, "q": q, "width": width, "first_sewn": first,
            "support_prediction": max(g, q + 4),
        })

record("STRATUM.width", "the full-depth quotient has width one or two",
       all(item["width"] in (1, 2) for item in observations),
       {width: sum(item["width"] == width for item in observations)
        for width in (1, 2)})
record("STRATUM.classifies", "K0 and K1 sew exactly in the width-one region",
       all((item["first_sewn"] is not None) == (item["width"] == 1)
           for item in observations),
       "cutoff<=20")
record("STRATUM.monotone", "once the rank relation appears it survives enlargement",
       all(all(sewn(item["g"], item["q"], cutoff)
               for cutoff in range(item["first_sewn"], 21))
           for item in observations if item["first_sewn"] is not None),
       "column-space inclusions")

mismatches = [item for item in observations
              if item["first_sewn"] !=
              (item["support_prediction"] if item["width"] == 1 else None)]
record("FALSIFIER.support", "the naive support threshold fails",
       len(mismatches) == 49,
       f"mismatches={len(mismatches)}; first={mismatches[:1]}")
record("FALSIFIER.two_sided", "support predicts both too late and too early",
       (any(item["first_sewn"] < item["support_prediction"]
            for item in mismatches if item["first_sewn"] is not None) and
        any(item["first_sewn"] > item["support_prediction"]
            for item in mismatches if item["first_sewn"] is not None)),
       "rank geometry is not a monotone support correction")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_nearest_neighbor_sewing_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact Fitting-stratum census",
        "audit": "2<=g<=10, 1<=q<=10, consecutive cutoff<=20",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "First nearest-neighbor sewing is equivalent to the width-one current "
        "stratum, but its onset is not determined by support closure. It is a "
        "maximal-minor/Fitting event requiring a finite local determinant theorem."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_nearest_neighbor_sewing.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
