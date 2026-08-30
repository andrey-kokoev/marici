# Failed relative injectivity has an exact residue

Owner: `marici.Buzzard`

Source locator: `Failed relative injectivity has an exact residue` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

For rational linear maps `M : V -> W` and `T : W -> U`, Lean defines:

- the excess preimage `ker(T composed with M)`;
- the overlap residue `range(M) intersect ker(T)`;
- the restricted map induced by `M` from the excess preimage to the overlap.

Lean proves this residue map is surjective and that its kernel consists
exactly of elements already in `ker M`. It also proves that the overlap is zero
if and only if `T` reflects zero on values realized by `M`.

This is the elementwise exact content of the short sequence from the source
packet. It identifies the additional transported kernel with an ordinary
linear image-kernel overlap.

## Type-system consequence

When relative injectivity fails, the missing certificate has a canonical
ordinary residue. This residue measures excess kernel creation, but its
existence alone supplies neither a Tor grading nor an executable readout. Those
stronger typings require separate constructors.

This increment extends the operator-square theorem from a Boolean certificate
to an exact defect object.

## Boundary and missing interfaces

- an explicit quotient isomorphism from excess preimage modulo `ker M`;
- finite-dimensional dimension formulas;
- completed or closed-operator analogues;
- source authorization of the transport square;
- filtrations for composite codomain transports.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/RelativeInjectivityResidue.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
