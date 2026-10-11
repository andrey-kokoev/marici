"""Bounded proof attempt for the source-to-local-unitary-lift conjecture.

Checks the factorwise C4 realization, then audits whether existing Agda
bridges interpret the full dependent return section as its analytic path.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import check_native_square_controlled_hamiltonian as native

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
OUT = ROOT / "results/source-to-local-lift-attempt.json"
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def sub(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))

def comm(a, b):
    return sub(native.mm(a, b), native.mm(b, a))

def zero(a):
    return all(x == 0 for row in a for x in row)

with redirect_stdout(io.StringIO()):
    model = native.main()
I, L, R, PL, PR = (model[k] for k in ("I", "L", "R", "PL", "PR"))
M = native.mm(PL, PR)
ZL = tuple(tuple(F(v) if i == j else F(0) for j in range(4))
           for i, v in enumerate((1, 1, -1, -1)))
ZR = tuple(tuple(F(v) if i == j else F(0) for j in range(4))
           for i, v in enumerate((1, -1, 1, -1)))

# Validate the source receipts and all source files used in this bridge audit.
receipts = {
    "native": json.loads((ROOT / "results/agda-NativeSquareHamiltonianSkeleton.json").read_text(encoding="utf-8-sig")),
    "tick": json.loads((ROOT / "results/agda-TickRetainedStructure.json").read_text(encoding="utf-8-sig")),
    "return_surface": json.loads((ROOT / "results/agda-TickLocalReturnSection.json").read_text(encoding="utf-8-sig")),
}
for key, receipt in receipts.items():
    check(f"{key}-Agda-closure-receipt-passed", receipt["passed"] and receipt["inputs_stable_during_check"])
source_paths = [
    "agda/NativeSquareHamiltonianSkeleton.agda",
    "agda/ObserverCoherenceCube.agda",
    "agda/TickRetainedStructure.agda",
    "agda/TickEvolutionBridge.agda",
    "agda/TickInterpretationBoundary.agda",
    "agda/TickContinuousSchedules.agda",
    "agda/TickGluedSchedules.agda",
    "agda/RetainedSquareReversal.agda",
    "agda/TickLocalReturnSection.agda",
]
source_hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in source_paths}
check("native-source-inventory-current", all(
    receipts["native"]["owner_source_inventory_sha256"][p.split("/", 1)[1]] == h
    for p, h in source_hashes.items() if p.startswith("agda/Native") or p.endswith("ObserverCoherenceCube.agda")))
check("Tick-classification-source-current", receipts["tick"]["source_sha256"] == source_hashes["agda/TickRetainedStructure.agda"])

# The source-to-matrix construction yields local generators. A left operator
# commutes with generators of the right matrix algebra, and vice versa.
check("left-source-operation-is-local", zero(comm(PL, R)) and zero(comm(PL, ZR)))
check("right-source-operation-is-local", zero(comm(PR, L)) and zero(comm(PR, ZL)))
H0 = native.add(PL, PR)
check("canonical-Hamiltonian-is-positive-sum-of-local-generators",
      H0 == native.add(PL, PR) and native.transpose(H0) == H0
      and all(native.mm(H0, J) == native.scale(l+r, J) and l+r >= 0
              for (l, r), J in model["joints"].items()))
minus = native.zscale(native.ONE, -1)
E = model["E"]
check("unitary-lift-has-source-left-corner", E(minus, native.ONE) == native.cm(L))
check("unitary-lift-has-source-right-corner", E(native.ONE, minus) == native.cm(R))
check("unitary-lift-has-source-joint-corner", E(minus, minus) == native.cm(native.mm(L, R)))
for z, w in ((model["roots"][1], native.ONE), (native.ONE, model["roots"][2]),
             (model["roots"][1], model["roots"][2])):
    U = E(z, w)
    check("sampled-unitarity/" + str(len(checks)), native.cmm(native.adj(U), U) == native.cm(I))

# Existing Agda contracts preserve endpoints and retain the Tick, but explicitly
# stop short of mapping its dependent return-section interior into C4 paths.
bridge = (ROOT / "agda/TickEvolutionBridge.agda").read_text(encoding="utf-8")
interpretation = (ROOT / "agda/TickInterpretationBoundary.agda").read_text(encoding="utf-8")
schedules = (ROOT / "agda/TickContinuousSchedules.agda").read_text(encoding="utf-8")
glued = (ROOT / "agda/TickGluedSchedules.agda").read_text(encoding="utf-8")
check("actual-Tick-schedule-tags-feed-endpoint-realization", "schedule-first" in bridge and "schedule-second" in bridge)
check("return-section-start-endpoints-are-preserved", "return-start-preserved" in bridge and "return-end-preserved" in bridge)
check("return-interior-not-interpreted-by-endpoint-bridge",
      "Only the return section's endpoints are interpreted here." in bridge
      and "interior is not identified with evolve" in bridge)
check("retained-interpretation-stores-source-Tick", "source-tick : B.D.ATick" in interpretation)
check("completion-schedules-disclaim-dependent-return-identification",
      "do not identify this with the" in schedules and "original dependent cubical return section" in schedules)
check("glued-parameter-is-a-pushout-not-cubical-interval",
      "ScheduleParameter = Pushout" in glued and "NOT asserted to be [0,2]" in glued)
return_surface = (ROOT / "agda/TickLocalReturnSection.agda").read_text(encoding="utf-8")
check("completion-valued-return-square-has-four-readout-corners",
      all(name in return_surface for name in ("return-corner-00", "return-corner-10", "return-corner-01", "return-corner-11")))
check("return-surface-matches-retained-section-endpoints",
      "return-section-start-compatible" in return_surface and "return-section-end-compatible" in return_surface)
check("return-surface-joint-continuity-on-bounded-regions",
      "return-surface-continuous" in return_surface and "Joint.evolution-vector-continuous" in return_surface)
check("return-surface-does-not-map-dependent-interior",
      "the section's interior is not identified" in return_surface and "Cubical I" in return_surface)
check("cubical-scalar-endpoint-path-is-ruled-out",
      "zero-not-one : zeroCompletion ≡ oneCompletion → ⊥" in return_surface)
check("cubical-state-path-between-return-endpoints-is-ruled-out",
      "no-cubical-state-path : R.basis (true , true) ≡ R.basis (false , false) → ⊥" in return_surface)

result = {
    "schema": "marici.nima.source-to-local-lift-attempt.v1",
    "status": "partial_attempt_failed_to_prove_full_bridge",
    "attempt_outcome": "+-",
    "intent": "prove",
    "checks": checks,
    "check_count": len(checks),
    "proved_fragment": "After the declared C4 linearization, the canonical PL,PR generators are factorwise local and their unitary exponential has the native source corners. A new Agda completion-valued local square is jointly continuous on explicit bounded regions, has all four extracted readout corners, and matches the retained section's actual start and end. Agda also proves zeroCompletion ≠ oneCompletion, ruling out using an ordinary Cubical path as the scalar time parameter.",
    "unclosed_obligation": "The Agda completion-valued square is parameterized by two Cauchy scalars, not by the dependent cubical coordinates. A cubical path in the scalar completion between its distinct endpoints is impossible, so the missing interface cannot be a direct Cubical I-to-scalar path. No typed map yet sends every point of backward-cell (i,j) into the corresponding metric-parameterized C4 evolution, and the Agda square is not a unitary model.",
    "why-this-is-not-refutation": "The new square supplies endpoint and corner compatibility, and the scalar separation theorem rules out only a direct cubical path parameterization. A relational or external metric-path interface may still connect the cubical section to the Cauchy-parameterized evolution, so the missing full bridge is not refuted.",
    "next_required_input": "A typed interface relating each backward-cell (i,j) value to the metric-parameterized square without asserting a Cubical I → Cauchy-scalar path, plus compatibility with the local unitary C4 evolution.",
    "effort_units_spent_estimate": 3,
    "scope": "fixed Bool/notEquiv source, declared C4 linearization, and the existing Agda return-section interface",
    "source_sha256": source_hashes,
    "attempt_checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in (
    "status", "attempt_outcome", "check_count", "proved_fragment",
    "unclosed_obligation", "why-this-is-not-refutation", "next_required_input",
    "effort_units_spent_estimate")}, indent=2))
