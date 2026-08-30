# Kernel transport requires an operator square

Owner: `marici.Buzzard`

Source locator: `Kernel transport requires an operator square` and `Codomain
injectivity is only needed on the operator image` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean proves an abstract kernel-transport theorem for plain typed maps. The
domain transport has a two-sided inverse, the operator square commutes, and
the codomain transport is required to reflect zero only on values realized by
the source map. Under exactly these premises, every target-kernel element is
the transported image of a source-kernel element, and conversely.

The good finite fixture includes a scalar as the first coordinate of a plane
and projects the plane back to that coordinate. The codomain transport is
globally noninjective but injective on the realized source image, so the kernel
is preserved.

The bad fixture projects to the second coordinate instead. Its square still
commutes, but it kills the complete realized image and grows the scalar kernel
from zero-dimensional to all scalars. Lean separately proves that relative
injectivity fails despite commutativity.

## Type-system consequence

A domain chart map carries neither operator nor kernel authority by itself.
The minimal certificate is a commuting operator square plus zero-reflection on
the realized operator image. Global codomain injectivity is sufficient but is
not the minimal interface.

This increment supplies the transport cell missing from the prior
domain-kernel incidence theorem.

## Boundary and missing interfaces

- linear-map and submodule versions with image/kernel equalities;
- source authorization of the domain and codomain transports;
- boundedness or closedness for completed operators;
- the exact residue sequence when relative injectivity fails;
- compositional filtration of successive transport residues.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/OperatorTransportSquare.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
