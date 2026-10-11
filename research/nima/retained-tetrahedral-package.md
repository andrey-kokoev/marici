# Retained tetrahedral packages and downward recovery

## Problem and scope

The target is a reusable output containing its complete typed derivation boundary: vertices, six edges, four faces and a filler. Boundary extraction should recover actual terms, not guess inhabitants from type names. This construction is specifically for **path coherence in an arbitrary type**, using `MarkedTetrahedronCoherence`; it does not assume an arbitrary WG relation is invertible or admits tetrahedral fillers.

SCC obligation: forward construction of a typed package, compatibility of repeated boundary extraction, and a hostile against recovery after a lossy readout. The owner-local model is `scc-models/retained-tetrahedral-package.json`.

## Checked implementation

`agda/RetainedTetrahedralPackage.agda` defines:

- `Cells.Vertices`: four retained vertices in a declared type.
- `Cells.Over.Surface`: a boundary indexed by those vertices, with six actual edge paths and all four actual triangle witnesses.
- `Filler surface`: the tetrahedral comparison between the two face-composition routes of that exact surface.
- `Package`: a dependent pair of the surface and its filler; `Full` additionally pairs in the four vertices.
- `FacePackage` and `EdgePackage`: reusable lower-dimensional packages that include their endpoints and their witnesses. Four face extractions and three edge extractions implement descent. Six shared-edge equations check that descending through adjacent faces returns the same full edge package.
- `recover-surface`, `recover-filler`, and `reassemble`: exact projection and reassembly, without proof erasure.

The filler alone is not asserted to reconstruct an erased surface. The recoverable object is the dependent pair that explicitly retains it. Nor do separately extracted faces retain a pointer to their parent tetrahedron.

## Construction, not only storage

A `Horn` retains the six edges and faces 012, 123 and 013. `complete` reuses the existing `Tetrahedra.Over.unique023` theorem to construct face 023 together with the filler. This is a marked **path-horn** completion theorem, not a theorem that every fully prescribed surface fills.

`forget-complete` recovers the supplied horn definitionally. `complete-forget` recovers an arbitrary completed package up to a path with that horn fixed, using the contractibility of the completion fiber. `horn-iso` records both directions. A request/answer WG constructs these packages, retains the vertices and original horn, and returns the witnessed completion transition. It does not invent compatibility for unrelated relations.

## Recovering a type and then its term

`TypedValue ℓ` is the dependent pair of a type and one of its inhabitants. Instantiating the vertex type with `TypedValue ℓ` gives:

- `recover-type p i`: the retained type at vertex `i`;
- `recover-term p i`: a term of exactly that recovered type.

The fixture uses Boolean negation as a univalent type path, with its dependent term path from `(Bool, false)` to `(Bool, true)`. A horn is completed, then vertex 1 is recovered as type `Bool` and term `true`. Descending through face 012 and edge 01 recovers that same typed vertex. Thus the fixture is not limited to reflexive edges or identical endpoint values.

A vertex that retained only a type would not support this term projection. The inhabitant is retained data, not reconstructed from the type alone.

## Hostile and disposition

`LossyDiagonal` repackages the existing ordinary/twisted marked tetrahedra at four fixed `Bool` vertices in the universe. Their diagonals agree but their first edges differ. `no-recovery` proves that no decoder of that diagonal alone can recover every such fixed-vertex package. Keeping the vertices fixed is essential to this comparison; an unrestricted path of packages could also move the boundary indices.

The result is a full typed package with checked downward recovery and a theorem-backed horn-completion WG. The mathematical completion and lossy-diagonal obstruction are reused from the existing marked-coherence work; the new contribution is the explicit vertex/surface/face/edge packaging, typed-value recovery and common WG interface. It does not establish arbitrary proof search, universal type inhabitation, arbitrary fully marked surface filling, or reversibility of erased computation.

## Verification

Run `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module RetainedTetrahedralPackage -Fresh`. The fresh safe Cubical receipt and log are `results/agda-RetainedTetrahedralPackage.json` and `.log`; the pre-existing `TypedGeneratorLayers.agda` import warning remains. The SCC checker validates the receipt and recorded source/compiler inventories rather than treating registration as a proof. No commit or new ledger entry is included.
