# Finite Stone adapter: four-element pilot

## Question

Can the existing Marici constructor carry a domain reconstruction, its morphisms,
and its coherence witnesses without acquiring Boolean-specific core operations?
The operator requested a duality/representation adapter rather than more NAND
proof-search tuning.

## Frozen claim boundary

This first pilot is the four-element Boolean algebra `Bool × Bool`, its **actual
minimal nonzero elements**, and all Boolean endomorphisms. Its Stone space has
two points. The full theorem for every finite Boolean algebra is not claimed.
SCC obligations: forward realization and route/coherencer compatibility.

Domain duties: construct Boolean operations/laws, recognize atoms, prove the
algebra/powerset and point/atom round trips, reconstruct every endomorphism,
and prove contravariant composition and naturality. Constructor duties: retain
those typed maps, equivalences, and comparisons using the existing native nodes
and rules. No source change to the core is permitted. Domain theorems are supplied
by this adapter, not automatically discovered by the generic constructor.

Conjecture: the unchanged native interface can express this pilot and preserve
its reconstruction witnesses. Rivals: a missing generic attachment type; a
Boolean-specific operation hidden in the core; or recovery of cardinalities
while morphisms/symmetries are lost. Risky tests are wrong-atom, reversed-variance,
and symmetry-erasure controls, plus proof and core-digest checks. A pass supports
this interface instance, not universal vocabulary reconstruction or convergence.

## Disposition

**Pilot passed.** Fresh safe Cubical Agda compilation and all three intended
compiler rejections passed. The six frozen constructor-core files are unchanged.
No proof of the general finite Stone theorem or general adapter synthesis is
asserted.

### What was constructed

`agda/FiniteStoneDomain.agda` defines the product Boolean algebra from ordinary
Boolean operations and proves its `BooleanStructure` laws. `IsAtom` is the
order-theoretic predicate “nonzero with no smaller nonzero element”; the two
atoms are proved to be exactly `(true,false)` and `(false,true)`, not merely
two labels chosen because their count fits.

The checked maps give

\[
B\cong(\operatorname{Atom}(B)\to\mathrm{Bool}),
\qquad
\mathrm{Bool}\cong\operatorname{Atom}(B).
\]

The representation agrees with atom incidence and preserves bottom, top,
complement, meet and join. Both round trips are explicit. Boolean-valued
subsets give the discrete two-point interpretation; this pilot does not add a
general topological-space library.

`Hom` retains a function and proofs preserving all Boolean operations.
`arrows-iso` reconstructs **every** such endomorphism from a point map and
recovers that point map. `select-identity`, `select-compose`,
`atom-map-compose`, and `atom-naturality` check identity, contravariant
composition, and the reconstruction square—not only matching carrier sizes.

`agda/FiniteStoneAdapter.agda` imports the actual `IndexedConstructorTables`
and `NativeTableRules`. It constructs source and subset nodes, retains the
Boolean structure and representation equivalence, uses native comparisons and
native comparison composition, and packages naturality and variance witnesses.
A recovery witness and its reflexive next-level witness are themselves packaged
using the existing path/higher rules. No automatic witness search is inferred
from that packaging.

### Falsification and remaining boundary

The finite checker independently extracts atoms from the meet table and tests
all **256** raw maps of the four-element carrier. Exactly **four** preserve the
Boolean structure; they correspond to all four maps of the two-point space.
All **16** composition pairs and both point orderings are checked. Six runtime
controls reject wrong/incomplete/duplicated atoms, covariant composition,
cardinality-based atom identification, and a nonunital map.

The kernel rejects `StoneBadAtom`, `StoneBadVariance`, and `StoneBadSymmetry`.
The positive development also proves that the unordered coordinate profile
cannot reconstruct every algebra element. Symmetry survives reconstruction;
there is no atom fixed by the swap. Contractible reconstruction fibers therefore
must not be confused with a one-point atom space.

The test supports the existing interface's ability to **receive and retain this
proved domain adapter**. Because supplied types, functions and witnesses are
already admitted by that interface, this is not evidence that the generic
constructor discovers Stone duality. General finite algebras, arrows between
different algebras, general adapter synthesis, infinite Stone spaces, and
arbitrary-vocabulary convergence remain outside the result. The prior fresh
NAND proof-search task is unchanged.

### Reproduction and evidence

```text
python research/nima/checkers/check_finite_stone.py --runtime-only
pwsh -NoProfile -File research/nima/checkers/check_finite_stone_kernel.ps1
python research/nima/checkers/check_finite_stone.py
python research/aspect/scc/scc.py check nima-finite-stone
```

Do not regenerate `core-freeze.json` to accommodate a changed core. Compiler
receipts bind the source, library, compiler and checker, reject changed inputs,
use fresh interfaces, and record the owned process in the ignored
`.ai/tmp/scc-state/nima-finite-stone-run.json`.

- Fresh kernel execution: `structured_command_execution:e_25120_1791123424344565600_344`.
- Independent audit: `structured_command_execution:e_25120_1791123591127801100_345`.
- Receipts: `research/nima/results/finite-stone-kernel.json` and
  `research/nima/results/finite-stone-audit.json`.
- Handoff, graph admission and Git state: `research/nima/results/finite-stone-handoff.json`.
