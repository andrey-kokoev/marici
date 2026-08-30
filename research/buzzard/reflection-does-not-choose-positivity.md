# Reflection does not choose positivity

Owner: `marici.Buzzard`

Source locator: `Reflection does not choose positivity—but the Hilbert packet
does` in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

The finite carrier is the real line. A scalar quadratic presentation `q` is
`ReflectionInvariant` when `q (-x) = q x`. Positivity and negativity are typed
as separate definiteness predicates.

Lean verifies that both `x ↦ x^2` and `x ↦ -x^2` are reflection invariant.
The first is positive definite; the second is negative definite, and the two
functions are unequal. Consequently reflection invariance does not imply
positive definiteness.

`AuthorizedPositiveMetric` records a form together with both reflection
compatibility and positive definiteness. Its positivity theorem is projection
of supplied data, making the authority boundary visible in the type rather
than deriving positivity from symmetry.

## Hostile countermodel

The negative square is the complete hostile fixture. It has exactly the same
reflection symmetry as the positive square but has the opposite sign at every
nonzero point. Any abstraction with only a reflection field admits both and
cannot select the Hilbert orientation.

## Boundary

This is a one-dimensional real quadratic model, not a full Hermitian-space
formalization. The latter would require:

- a complex or star-field carrier;
- sesquilinearity and conjugate symmetry;
- nondegeneracy and positive definiteness conventions;
- the direct-limit Hilbert metric and unitary bonding maps;
- source provenance distinguishing an authorized metric from an arbitrary
  positive replacement.

The abstraction generalized the independence of symmetry and positivity. It
did not infer source authority from the existence of a mathematically valid
positive form.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ReflectionPositivity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ReflectionPositivity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/reflection-does-not-choose-positivity.md`
