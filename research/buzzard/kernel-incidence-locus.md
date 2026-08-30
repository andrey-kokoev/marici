# Restricted kernel birth is an incidence locus

Owner: `marici.Buzzard`

Source locator: `The intrinsic jump locus is an incidence locus` and `The
barcode belongs to a pair` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean defines the restricted kernel of a map on an admitted domain and proves
it is exactly the intersection of that domain with the bulk kernel. In the
finite boundary fixture, the first-coordinate Lagrangian has trivial
nonzero incidence with the bulk kernel, while the kernel-generated Lagrangian
has nontrivial incidence.

Lean proves generally that every injective simultaneous transport carries an
intersection to the intersection of the transported sets. Coordinate exchange
therefore preserves incidence when both members of the pair move.

The hostile one-sided fixture starts with a line intersecting itself
nontrivially. Exchanging only the domain to the other coordinate line while
holding the kernel reference fixed destroys the nontrivial intersection.

## Type-system consequence

The intrinsic defect object is the pair `(boundary domain, bulk kernel)`, not
an isolated domain. Simultaneous transport is a coordinate change; one-sided
transport changes the represented problem. A kernel-jump locus can therefore
be defined as incidence without claiming spectral flow, a Maslov index, or a
continuous source family.

This increment refines the selector-wall theorem into a chart-independent
incidence criterion.

## Boundary and missing interfaces

- linear subspaces and intersection dimensions rather than set predicates;
- a source-derived operator transport square;
- a continuous family of closed Lagrangian domains;
- gap topology and crossing orientations;
- higher-multiplicity determinantal incidence strata.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/KernelIncidenceLocus.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
