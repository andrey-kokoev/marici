# Canonical half-line antipode: Lean packet

## Source boundary

This increment formalizes the finite route/covector content of Grothendieck's
`canonical-half-line-antipode-is-source-fixed-but-universal.md`. It does not
construct the half-line transform or assert that an arbitrary decomposition
is the source-selected one.

## Formal objects and assumptions

Over an arbitrary field `K`, `TwoRouteState K` and `TwoRouteCovector K` are
two-coordinate vectors. Their incidence pairing is

\[
c_0r_0+c_1r_1.
\]

`equalRouteCovector` is the source-frame coordinate `(1,1)`. A diagonal route
rescaling acts covariantly on the state and contragrediently on the covector.

## Theorems and hostile

- `routePairing_contragredient_invariant` proves that the incidence scalar is
  invariant under simultaneous state/covector transport.
- `equalRoute_zero_iff_antipode` proves, when the second route is nonzero,
  that zero incidence in the equal-covector chart is equivalent to route ratio
  `-1`.
- `antipodal_incidence_can_be_offSeam` supplies a typed finite hostile whose
  route is `(1,-1)` and whose independent locus tag is `offSeam`.

The hostile records the missing interface rather than making a geometric
claim: route incidence has no map to spectral locus until such a map is
source-derived.

## Missing interfaces

Faithful source specialization requires an even super-exponentially decaying
function, an entire half-line transform, a proof that contour splitting fixes
the equal covector and its orientation, reciprocal transport `H(z) ↦ H(-z)`,
and the conjugacy identity on the chosen seam. The modulated-Gaussian
universality hostile needs the analytic interfaces already listed in the
coverage ledger. A labelled modular relation excluding off-seam antipodal
incidence remains an active RH-strength conjectural input and is not assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/HalfLineAntipode.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
