"""Exact split-monomorphism certificates for source-generated observers."""
import json
import os
import sympy as sp

checks = []


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Z_2 character transform: joint electric/magnetic readout is split faithful.
hadamard = sp.Matrix([[1, 1], [1, -1]])
inverse = hadamard / 2
record("Z2.split", "the parity observer has the half-Hadamard left inverse",
       inverse * hadamard == sp.eye(2))
record("Z2.single", "either single parity port has a one-dimensional kernel",
       sp.Matrix([[1, 1]]).nullspace() == [sp.Matrix([-1, 1])] and
       sp.Matrix([[1, -1]]).nullspace() == [sp.Matrix([1, 1])])

# Boolean zeta transform on all subsets of a four-element route set.
n = 4
subsets = list(range(1 << n))
zeta = sp.Matrix([[int((source & target) == target) for source in subsets]
                  for target in subsets])
mobius = sp.Matrix([[((-1) ** ((source ^ target).bit_count())
                             if (source & target) == source else 0)
                    for target in subsets] for source in subsets])
record("BOOLEAN.split", "Boolean Mobius inversion is a source-derived left inverse",
       mobius * zeta == sp.eye(1 << n))

# A rank statement alone is not a typed reconstruction certificate: changing
# the codomain gauge changes the inverse while preserving rank.
gauge = sp.diag(*range(1, (1 << n) + 1))
gauged = gauge * zeta
gauged_inverse = zeta.inv() * gauge.inv()
record("TYPING.gauge", "a typed codomain gauge requires the transported inverse",
       gauged.rank() == zeta.rank() and gauged_inverse * gauged == sp.eye(1 << n) and
       mobius * gauged != sp.eye(1 << n))

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "source_observer_split_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Boolean score inversion and the joint parity observer are split monomorphisms with explicit source-derived left inverses. Individual parity ports are not faithful. Algebraic rank survives codomain gauge, but the reconstruction certificate must be transported with the typing map.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "source_observer_split.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
