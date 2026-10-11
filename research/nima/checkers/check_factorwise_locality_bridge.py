"""Exact factorwise-locality test and source-to-generator bridge audit.

The Agda source supplies discrete one-factor flips. The matrix model adds a
complex-linear generator lift; this checker tests whether the retained finite
annotation constraints force that lift to be factorwise local.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import check_native_square_controlled_hamiltonian as native

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/factorwise-locality-bridge.json"
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def sub(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))

def comm(a, b):
    return sub(native.mm(a, b), native.mm(b, a))

def is_zero(a):
    return all(x == 0 for row in a for x in row)

with redirect_stdout(io.StringIO()):
    source = native.main()
I, L, R, PL, PR = (source[k] for k in ("I", "L", "R", "PL", "PR"))
M = native.mm(PL, PR)
ZL = tuple(tuple(F(v) if i == j else F(0) for j in range(4))
           for i, v in enumerate((1, 1, -1, -1)))
ZR = tuple(tuple(F(v) if i == j else F(0) for j in range(4))
           for i, v in enumerate((1, -1, 1, -1)))

# Freshness of the source-level discrete square proof and its exact inputs.
source_proof = json.loads((ROOT / "results/agda-NativeSquareHamiltonianSkeleton.json")
                          .read_text(encoding="utf-8-sig"))
check("native-square-Agda-closure-passed", source_proof["passed"]
      and source_proof["ignore_interfaces"] and source_proof["inputs_stable_during_check"])
for name in ("NativeSquareHamiltonianSkeleton.agda", "ObserverCoherenceCube.agda"):
    check(f"Agda-source-current/{name}", source_proof["owner_source_inventory_sha256"][name]
          == hashlib.sha256((ROOT / "agda" / name).read_bytes()).hexdigest())
skeleton = (ROOT / "agda/NativeSquareHamiltonianSkeleton.agda").read_text(encoding="utf-8")
check("source-explicitly-stops-before-complex-generator-lift",
      "complex coefficients, exponential or physical Hamiltonian are asserted here." in skeleton)

# The source flips are genuinely factorwise on the Bool x Bool carrier.
check("left-source-map-is-first-factor-flip", L == tuple(tuple(F(i == (j ^ 2))
      for j in range(4)) for i in range(4)))
check("right-source-map-is-second-factor-flip", R == tuple(tuple(F(i == (j ^ 1))
      for j in range(4)) for i in range(4)))

# Factorwise operator criterion: an operator on the left factor commutes with
# the right-factor X,Z generators, and conversely. X_L=L, X_R=R.
check("baseline-left-generator-is-factorwise",
      is_zero(comm(PL, R)) and is_zero(comm(PL, ZR)))
check("baseline-right-generator-is-factorwise",
      is_zero(comm(PR, L)) and is_zero(comm(PR, ZL)))
Cleft, Cright = comm(M, ZR), comm(M, ZL)
check("mixed-term-breaks-left-factor-locality", not is_zero(Cleft))
check("mixed-term-breaks-right-factor-locality", not is_zero(Cright))

# For H_L(k)=P_L+kP_LP_R and H_R(k)=P_R+kP_LP_R, the exact cross-factor
# commutators are k[M,Z_R] and k[M,Z_L]. Since the coefficient matrices are
# nonzero over Q, factorwise locality in this family holds iff k=0.
for k in (0, 2):
    HL = native.add(PL, native.scale(k, M))
    HR = native.add(PR, native.scale(k, M))
    check(f"left-cross-commutator-formula/{k}", comm(HL, ZR) == native.scale(k, Cleft))
    check(f"right-cross-commutator-formula/{k}", comm(HR, ZL) == native.scale(k, Cright))
    check(f"factorwise-locality-iff-zero-in-family/{k}",
          (is_zero(comm(HL, ZR)) and is_zero(comm(HR, ZL))) == (k == 0))

# The k=2 countermodel satisfies the already checked finite class conditions,
# while failing the stronger factorwise-locality condition.
prior = json.loads((ROOT / "results/tick-unitary-image-nonuniqueness.json").read_text())
prior_checks = set(prior["checks"])
required = {"Hermitian/2", "commuting/2", "axis-symmetry/2",
            "exact-nonnegative-joint-eigenvalues/2/0/0",
            "exact-nonnegative-joint-eigenvalues/2/0/1",
            "exact-nonnegative-joint-eigenvalues/2/1/0",
            "exact-nonnegative-joint-eigenvalues/2/1/1",
            "corner/2/0/0", "corner/2/0/1", "corner/2/1/0", "corner/2/1/1",
            "rival-not-tensor-local"}
check("k2-countermodel-passes-current-class-and-fails-locality",
      required <= prior_checks and prior["status"] == "pass")

result = {
    "schema": "marici.nima.factorwise-locality-bridge.v1",
    "status": "pass",
    "checks": checks,
    "check_count": len(checks),
    "operator_family": "H_L(k)=P_L+k P_L P_R; H_R(k)=P_R+k P_L P_R",
    "factorwise_locality_test": "commute with the other factor's X and Z generators",
    "exact_criterion": "within this rational one-parameter family, both generators are factorwise local iff k=0",
    "source_result": "the Bool x Bool source operations are factorwise flips",
    "bridge_status": "the Agda skeleton explicitly does not assert complex linearization, exponentiation, or a Hamiltonian lift",
    "countermodel": "k=2 satisfies the declared finite annotation class but violates factorwise locality",
    "disposition": "discrete source locality is verified; it does not by itself constrain the added continuous generator lift. A source-derived locality-preserving lift remains open.",
    "scope": "exact finite Bool square and declared C4 generator family; not a theorem about an unspecified physical or integrated source model",
    "source_sha256": hashlib.sha256(skeleton.encode()).hexdigest(),
    "matrix_checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
