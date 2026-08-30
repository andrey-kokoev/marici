"""Type audit for the magnetic discrete crossing incidence."""
import json
import os


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


def excess(g, q):
    return q - g


def cutoff_extension(g, q, k):
    return {"g": g, "q": q, "d": excess(g, q), "k": k + 1}


def adjacent_excess(g, q, k):
    return {"g": g, "q": q + 2, "d": excess(g, q + 2), "k": k}


for g in range(2, 21):
    for q in range(g + 1, g + 32):
        for k in range(1, 11):
            state = {"g": g, "q": q, "d": excess(g, q), "k": k}
            raised_k = cutoff_extension(g, q, k)
            raised_d = adjacent_excess(g, q, k)
            record_id = None
            if raised_k["q"] != state["q"] or raised_k["d"] != state["d"]:
                record_id = (g, q, k, "cutoff_changed_component")
                break
            if raised_d["q"] != state["q"] + 2 or raised_d["d"] != state["d"] + 2:
                record_id = (g, q, k, "adjacency_failed_to_change_component")
                break
        if record_id:
            break
    if record_id:
        break

record("TYPE.cutoff", "cutoff extension preserves q and d",
       record_id is None, "2<=g<=20; g<q<=g+31; 1<=k<=10")
record("TYPE.component", "d-to-d+2 at fixed grade is exactly q-to-q+2",
       all(excess(g, q + 2) == excess(g, q) + 2
           for g in range(2, 21) for q in range(g + 1, g + 32)),
       "d=q-g")
record("TYPE.inequivalent", "cutoff transfer and excess adjacency have different codomains",
       all(cutoff_extension(g, q, k) != adjacent_excess(g, q, k)
           for g in range(2, 21) for q in range(g + 1, g + 32)
           for k in range(1, 11)),
       "one changes k; the other changes q and d")

crossings = [
    {"left_d": 5, "right_d": 7, "incidence": 1},
    {"left_d": 11, "right_d": 13, "incidence": -1},
]
record("CROSSING.labels", "both reported crossings are adjacent excess-label pairs",
       all(item["right_d"] - item["left_d"] == 2 for item in crossings),
       crossings)
record("AUTHORITY.no_transport", "the known fixed-q transfer cannot authorize either crossing edge",
       all(item["right_d"] != item["left_d"] for item in crossings),
       "fixed-q transfer preserves d")

# Hostile laundering fixture: relabel k-extension as d-extension.
g, q, k = 6, 11, 3
actual = cutoff_extension(g, q, k)
laundered_claim = adjacent_excess(g, q, k)
record("FALSIFIER.laundering", "a cutoff constructor fails the claimed inter-component codomain",
       actual != laundered_claim,
       {"source": {"g": g, "q": q, "d": q-g, "k": k},
        "actual": actual, "claimed": laundered_claim})

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_intercomponent_adjacency_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "exact type audit with bounded replay",
        "definitions": {"d": "q-g", "cutoff_transfer": "k->k+1 at fixed q"},
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The discrete sign incidences are exact on ordered excess labels, but "
        "they are not morphism-level crossing charges under the known magnetic "
        "transfer. Moving d by two changes component q; the proved cutoff "
        "constructor changes k at fixed q. A source-derived inter-component "
        "correspondence is a genuinely missing constructor."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_intercomponent_adjacency.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
