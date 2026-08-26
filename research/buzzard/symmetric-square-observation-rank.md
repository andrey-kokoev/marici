# Port count is not symmetric-square rank

Owner: `marici.Buzzard`

Source locator: `Port count must be replaced by symmetric-square rank` and
`Symmetry closure does not create new observations` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean distinguishes six nominal outputs from six independent pairing
measurements. The hostile observation retains all three even polarized probes
but replaces the odd mixed probe by a duplicate odd basis probe. Two distinct
pairings with positive odd blocks then give identical six-port output.

In parity-multiplicity coordinates, reflection fixes the two even coordinates
and negates the two odd coordinates. Lean defines the six-component restricted
symmetric-square row and proves for every probe `v` that `v` and its reflected
image induce exactly the same row.

The concrete probe `(1,2,3,4)` and its reflection both produce
`(1,4,4,9,16,24)`.

## Type-system consequence

Port cardinality is not a faithful observation invariant. The relevant datum
is the span or rank of the induced symmetric-square rows. Likewise, closing a
probe family under an already imposed symmetry does not increase its power to
distinguish invariant pairings.

This abstraction specializes the six-probe reconstruction theorem by exposing
its independence premise. It rejects both duplicate-port inflation and
symmetry-orbit inflation.

## Boundary and missing interfaces

- a general finite-family rank interface for symmetric-square rows;
- source-derived admissible probe constructors;
- the physical parity-coordinate comparison;
- complex Hermitian analogues using conjugate products;
- a source feature germ whose even jets span the six-dimensional target.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/SymmetricSquareObservationRank.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
