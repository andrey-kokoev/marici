# First-nonzero-jet atlas

Owner: `marici.Buzzard`

Source locator: `Source-generated jet atlas` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

`transformedJet correction r jet m` models the most general finite
lower-triangular change needed at order `m`: the leading coefficient is
`jet m / r`, while arbitrary correction coefficients multiply strictly lower
jets. The coefficient type is an arbitrary commutative field. The gauge `r`
must be nonzero.

`FirstNonzeroAt jet m` records both premises separately: every coefficient
below `m` is zero, and coefficient `m` is nonzero.

Lean proves:

- all lower-triangular correction terms vanish at the first nonzero index;
- the first nonzero coefficient transforms contragrediently as `jet m / r`;
- every nonzero gauge preserves the first-nonzero index.

This is the exact algebraic core of the claimed jet-chart covariance. It does
not derive the triangular transformation law from analytic differentiation;
that law remains a source-supplied interface.

## Hostile finite-depth example

For every finite depth `d`, `beyondDepthJet d` is zero at every index through
`d` and equals one at `d + 1`. Lean therefore proves that no fixed finite
inspection depth detects every nonzero formal jet family.

The countermodel is formal rather than analytic. To instantiate it with
analytic functions, use the polynomial `z^(d+1)` after fixing derivative
normalization conventions. Analytic nonzero germs also require an independent
identity-theorem premise to guarantee that some coefficient is nonzero.

## Boundary

The abstraction generalized the lower-triangular covariance statement and
the finite-depth obstruction. It did not formalize a global analytic section,
pointwise minimization, measurability, executable search, a uniform
multiplicity bound, or source authority for a target jet metric.

Missing convention-fixed interfaces are derivative normalization, the exact
gauge action on jets, the analytic function/germ type, and the theorem linking
nonzero germs to finite order of vanishing.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/JetAtlas.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/JetAtlas.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/first-nonzero-jet-atlas.md`
