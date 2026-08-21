"""Exact descent audit for the positive-sheet selector on all branch quotients."""

import json
from pathlib import Path


rows = []
fiber_checks = 0
for branch in range(32):
    retained = (~branch) & 31
    fibers = {}
    for g in range(32):
        fibers.setdefault(g & retained, []).append(g)
    delta = [int(g == 0) for g in range(32)]
    trace = [1] * 32
    delta_constant = True
    trace_constant = True
    witness = None
    for fiber in fibers.values():
        dvals = {delta[g] for g in fiber}
        tvals = {trace[g] for g in fiber}
        fiber_checks += len(fiber)
        if len(dvals) != 1:
            delta_constant = False
            witness = witness or fiber
        if len(tvals) != 1:
            trace_constant = False
    assert trace_constant
    assert delta_constant == (branch == 0)
    rows.append({
        "branch_subset_mask": branch,
        "kernel_order": 1 << branch.bit_count(),
        "quotient_order": len(fibers),
        "positive_selector_descends": delta_constant,
        "orbit_trace_descends": trace_constant,
        "first_failed_fiber": witness,
    })

result = {
    "schema": "marici.cosmology.five_site_branch_selector_descent.v1",
    "branch_quotients": len(rows),
    "nontrivial_branch_quotients": 31,
    "fiber_checks": fiber_checks,
    "positive_selector_pass_count": sum(r["positive_selector_descends"] for r in rows),
    "trace_pass_count": sum(r["orbit_trace_descends"] for r in rows),
    "rows": rows,
    "passed": True,
    "verdict": "the frozen positive-sheet selector descends only on the identity quotient",
}
out = Path(__file__).with_name("results") / "five-site-branch-selector-descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("branch_quotients", "fiber_checks", "positive_selector_pass_count", "trace_pass_count", "passed")}))
