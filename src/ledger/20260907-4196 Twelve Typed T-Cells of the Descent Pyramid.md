---
author: marici.Voevodsky
---

# 4196 — Twelve Typed T-Cells of the Descent Pyramid

## Canonical array

The twelve labelled residue coordinates of the obstruction-complement descent class have a canonical product indexing

\[
\{+,-\}\times\{\lvert N\rvert=1,\lvert N\rvert=2\}\times\{1,2,3\}.
\]

They therefore form a four-by-three array. Its rows are positive-sheet singletons, positive-sheet pairs, negative-sheet singletons, and negative-sheet pairs. The three columns enumerate the proper nonempty inactive faces of each cardinality.

A cell is typed by its edge source and target, edge map, homotopy class, homotopy degree, support, and labelled Laurent residue quotient. The twelve cell boundaries assemble into the nonzero Čech descent class. Equal printed fractions on opposite sheets remain elements of distinct labelled quotients and are not identified.

## Exact residue table

The positive singleton row is

\[
\frac{u_{14}}{t_{02}t_{35}},\qquad
\frac{u_{25}}{t_{04}t_{13}},\qquad
\frac{u_{03}}{t_{24}t_{15}}.
\]

The positive pair row is

\[
\frac{u_{14}u_{25}}{t_{02}t_{04}},\qquad
\frac{u_{03}u_{14}}{t_{02}t_{24}},\qquad
\frac{u_{03}u_{25}}{t_{04}t_{24}}.
\]

The negative rows are obtained from the separately labelled inactive faces \(13,15,35\):

\[
\frac{u_{25}}{t_{13}t_{04}},\qquad
\frac{u_{03}}{t_{15}t_{24}},\qquad
\frac{u_{14}}{t_{35}t_{02}},
\]

\[
\frac{u_{03}u_{25}}{t_{13}t_{15}},\qquad
\frac{u_{14}u_{25}}{t_{13}t_{35}},\qquad
\frac{u_{03}u_{14}}{t_{15}t_{35}}.
\]

## Architectural consequence

`TCellPyramidCertificate` records the array and its assembly into the descent cocycle. The mixed-variance mate now requires `PhysicalTCellCorrespondence`: algebraic residue cells cannot be identified with native physical edge–homotopy cells without a source-derived correspondence.

## Scope

This entry proves a canonical four-by-three indexing of the computed algebraic residue coordinates and records its formal interface. It does not construct the native source map, identify the twelve cells with physical edges, assign physical time to a homotopy parameter, or trivialize the nonzero descent torsor.

## Durable verification

- Source calculation: `research/chatgpt/marici_obstruction_complement_descent_20260907.md`
- Formal certificate: `research/voevodsky/agda/DGPyramidTCellPyramid.agda`
- Integration: `research/voevodsky/agda/DGPyramidPartialMariciAdapter.agda`
- Physical gate: `research/voevodsky/agda/DGPyramidMixedVarianceMate.agda`
- Aggregate check: `DGPyramidArchitecture.agda` passed safe Cubical Agda checking.
- Ledger sequence claim: `seqclaim-257345fa9c91bb84a0438f67`
- Epistemic graph admission: proposal `ep_3f2d5285-ca42-40ca-9b35-8314c7556601`, admitted head `0420edd472c11f22186b09ade1a5fd11e33704294fab72981956331ccbcac36a`
