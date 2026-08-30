"""Minimal parity-port completion and kernel-rerouting checks."""
import json
import os
import sympy as sp

alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
checks = []


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


observer = sp.Matrix([[alpha, beta], [gamma, delta]])
plucker = alpha * delta - beta * gamma
adjugate = sp.Matrix([[delta, -beta], [-gamma, alpha]])
record("ATLAS.adjugate", "the symbolic reconstruction numerator is the adjugate",
       adjugate * observer == plucker * sp.eye(2))

magnetic = sp.Matrix([[1, -1]])
candidate = sp.Matrix([[gamma, delta]])
completion = magnetic.col_join(candidate)
record("MAGNETIC.minor", "a complement to M is faithful exactly off gamma+delta=0",
       sp.factor(completion.det()) == gamma + delta)

electric = sp.Matrix([[1, 1]])
character_observer = electric.col_join(magnetic)
record("CHARACTER.split", "the source-authorized E,M pair has determinant -2",
       character_observer.det() == -2 and
       character_observer.inv() * character_observer == sp.eye(2))

# Abstract rerouting on the two one-dimensional parity kernels.
ker_m = magnetic.nullspace()[0]
ker_e = electric.nullspace()[0]
record("REROUTE.magnetic", "E is nonzero on the magnetic blind direction",
       (electric * ker_m)[0] == 2)
record("REROUTE.electric", "M is nonzero on the electric blind direction",
       abs((magnetic * ker_e)[0]) == 2)

# A second magnetic-proportional observation adds no information.
lam = sp.symbols("lam")
duplicate = magnetic.col_join(lam * magnetic)
record("FAIL.duplicate", "a proportional second port leaves the blind line intact",
       duplicate.rank() == 1 and duplicate * ker_m == sp.zeros(2, 1))

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "parity_port_completion_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Two scalar sheet ports reconstruct exactly when their Plucker determinant is nonzero. A complement to M=(1,-1) is sufficient iff gamma+delta is nonzero. Reflection authority canonically selects E=(1,1), and each parity port is injective on the other port's kernel.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "parity_port_completion.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
