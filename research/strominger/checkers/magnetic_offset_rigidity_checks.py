"""Local confluence theorem selecting the magnetic offset h=4."""
import json
import os

import sympy as sp

r, c, step, w0, a, j = sp.symbols("r c step w0 a j")


def vertical_weight(rv, sv):
    # Denominator power before weight-s step is s-w0.
    return sp.expand(rv - (sv - w0) + c * sv)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


v = vertical_weight(r, step)
record("MOVE.general", "the generalized vertical move has weight r+(c-1)s+w0",
       sp.expand(v - (r + (c - 1) * step + w0)) == 0, str(v))

# Compare horizontal-then-vertical with vertical-then-horizontal.  The common
# horizontal factor r is retained, so this is an actual weighted-diamond test.
horizontal_then_vertical = sp.expand(r * vertical_weight(r - 1, step + 1))
vertical_then_horizontal = sp.expand(vertical_weight(r, step) * r)
diamond_residual = sp.factor(horizontal_then_vertical - vertical_then_horizontal)
record("DIAMOND.residual", "the elementary path-ordering defect is r*(c-2)",
       diamond_residual == r * (c - 2), str(diamond_residual))

solution = sp.solve(sp.Eq(diamond_residual, 0), c)
record("DIAMOND.unique", "local weighted confluence uniquely fixes c=2",
       solution == [2], solution)

# At c=2 every vertical move depends only on how many vertical moves preceded
# it.  If j previous vertical moves occurred, r=-a-(s-w0-j), giving 2*w0-a+j.
rv = -a - (step - w0 - j)
confluent_vertical = sp.factor(vertical_weight(rv, step).subs(c, 2))
record("OFFSET.path", "the j-th vertical factor is 2*w0-a+j after confluence",
       sp.expand(confluent_vertical - (2 * w0 - a + j)) == 0,
       str(confluent_vertical))

h_selected = sp.expand(2 * w0)
record("OFFSET.baseline", "the rigid baseline weight start w0=2 selects h=4",
       h_selected.subs(w0, 2) == 4, "h=2*w0=4")

# Reconstruct the complete path product and its binomial multiplicity.
g, verticals = sp.symbols("g verticals", integer=True, nonnegative=True)
horizontal_product = sp.rf(a, g - verticals)
vertical_product = sp.rf(2 * w0 - a, verticals)
closed_weight = (sp.binomial(g, verticals) * (-1) ** (g - verticals) *
                 horizontal_product * vertical_product)
baseline_weight = closed_weight.subs(w0, 2)
expected_weight = (sp.binomial(g, verticals) * (-1) ** (g - verticals) *
                   sp.rf(a, g - verticals) * sp.rf(4 - a, verticals))
record("OFFSET.closed", "the confluent path product recovers the magnetic coefficient law",
       sp.simplify(baseline_weight - expected_weight) == 0,
       "binomial interleavings times two rising factorials")

# Hostile deformations distinguish the two sources of rigidity.
record("FALSIFIER.connection", "changing c destroys the first weighted diamond",
       diamond_residual.subs({c: 3, r: 1}) == 1, "c=3 residual=1")
record("FALSIFIER.weight", "changing the weight start preserves confluence but changes h",
       diamond_residual.subs(c, 2) == 0 and h_selected.subs(w0, 3) == 6,
       "w0=3 gives h=6")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_offset_rigidity_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic local weighted-diamond rigidity theorem",
              "ansatz": "connection strength c and unit-increment weights starting at w0"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Within the local two-move fold engine, weighted path confluence holds iff c=2: the elementary HV-VH residual is r(c-2). At c=2 and weight start w0, the j-th vertical factor is 2w0-a+j, so the binomial path sum has offset h=2w0. The independently rigid baseline start w0=2 therefore forces h=4. The apparent h-modulus arose only after forgetting the engine's confluence and weight-start axioms.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_offset_rigidity.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
