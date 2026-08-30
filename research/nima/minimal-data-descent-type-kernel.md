# Minimal executable data-descent type kernel

Owner: `marici.Nima`

## What now exists

The first reusable data-descent kernel distinguishes four arrow constructors:

```text
OpenRestriction   same site, admitted overlap required
GroupoidArrow     invertible, fiber signature preserved, authority required
Specialization    directed toward a deeper declared stratum
Correspondence    independently typed kernel or span required
```

Local objects carry a context, coefficient type, rank, and ordered grade
signature.  Coherence cells compare composable parallel paths or certify an
identity cycle.  Validation failures are returned as typed obstruction
records rather than flattened booleans.

## First compilation

The exact `G12 -> G23 -> G31 -> G12` cosmology packet compiles with:

- three contexts;
- three rank-26 local objects;
- three authorized invertible groupoid arrows;
- one exact identity-cycle coherence cell.

This encoding does not call the occurrence charts open subsets.  It retains
the established cyclic source-relabelling authority and references the exact
zero-defect transition certificate.

## Hostile tests

The compiler rejects:

1. relabelling presented as an open restriction without overlap evidence;
2. a rank-changing arrow presented as a groupoid equivalence;
3. a noncomposable path presented as a coherence cycle;
4. a cyclic transition with nonzero identity defect.

Thus the type distinctions have operating meaning: changing the forbidden
field changes acceptance.

## Boundary

This is a minimal research kernel, not a full dependent type theory.  It does
not yet verify matrix identities itself, derive covers, compute homotopies, or
type derived base change.  Its immediate extension order is:

1. attach evidence digests and independently replay matrix certificates;
2. add variance and composition rules for kernels/correspondences;
3. add derived objects (`Kernel`, `Cokernel`, `Tor`, `Cone`) with base-change
   obligations;
4. attach operational successor maps to obtain capability descent;
5. formalize the stable kernel in Lean after the executable contracts stop
   changing.
