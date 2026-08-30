# Composite transport residues form a filtration

Owner: `marici.Buzzard`

Source locator: `Composite transport residues form a filtration` and `The
residue flag depends on factorization` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean models the exact three-dimensional fixture. One coordinate projection
kills the first direction and another kills the second. Composing them in
either order gives the same endpoint map `diag(0,0,1)`.

Lean characterizes the intermediate kernels exactly:

- killing the first coordinate leaves the first coordinate line as kernel;
- killing the second leaves the second coordinate line as kernel;
- the composite kernel is the plane whose third coordinate is zero.

Explicit basis directions prove that each factorization contributes a
different first residue layer, while both directions lie in the common final
kernel. Thus the endpoint residue agrees but the intermediate flags differ.

## Type-system consequence

Composite excess dimension forgets which logical factor created each residue
direction. A filtered residue belongs to a chosen factorization, not merely to
the endpoint map. Equal composites therefore need a comparison cell before
their filtered defects can be identified.

These are logical factorization layers, not temporal states. This increment
extends the ordinary overlap residue without importing a time index.

## Boundary and missing interfaces

- submodule filtrations and quotient-dimension additivity;
- a general theorem for arbitrary chains of linear transports;
- source-authorized factorization and comparison cells;
- stabilizer torsors for nonunique comparisons;
- triangle coherence for three filtered presentations.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/CompositeTransportResidueFiltration.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
