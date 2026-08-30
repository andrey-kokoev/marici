# One displacement rank is insufficient

Owner: `marici.Buzzard`

Source locator: `One displacement rank is still insufficient` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean defines the nilpotent displacements of four-dimensional unipotent Jordan
types `(3,1)` and `(2,2)` directly. It proves their first images are each
two-parameter coordinate planes, giving the same first displacement rank.

For type `(3,1)`, the squared displacement is `(x0,x1,x2,x3) -> (x2,0,0,0)`:
it has a nonzero line image. For type `(2,2)`, the squared displacement is
identically zero. Both cubes vanish. An explicit vector witnesses the squared
distinction.

Thus the structural profiles are `(2,1,0)` and `(2,0,0)` without relying on a
numeric matrix-rank oracle.

## Type-system consequence

One displacement rank distinguishes identity from the basic unipotent hostile
but does not classify higher-dimensional unipotent holonomy. The ranks or
images of all nilpotent powers retain the Jordan partition. This remains a
unipotent classifier only and must not be promoted to arbitrary holonomy.

The abstraction specialized the prior scalar-blindness theorem rather than
claiming a universal rank-profile interface.

## Boundary and missing interfaces

- a general finite-dimensional rank-profile theorem;
- proof recovering nilpotent Jordan partitions from all power ranks;
- polynomial-pencil Smith data for arbitrary rational holonomy;
- source-authorized higher displacement probes;
- completion-ring analogues where field classification may fail.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/HigherDisplacementProfile.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
