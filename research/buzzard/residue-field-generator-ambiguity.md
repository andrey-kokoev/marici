# Residue field does not determine generator arity

## Lean objects

- `UnivariatePolynomial` is `Polynomial Rat`, the coefficient ring
  \(\mathbb Q[X]\).
- `univariateOriginIdeal` is the singleton-generated ideal \((X)\).
- `univariateOriginIdeal_eq_constantCoeff_ker` identifies \((X)\) with the
  kernel of the constant-coefficient homomorphism
  \(\mathbb Q[X]\to\mathbb Q\).
- `univariateOriginQuotientEquivRat` proves
  \(\mathbb Q[X]/(X)\cong\mathbb Q\).
- `axisIdealQuotientEquivRat`, imported from the existing bivariate
  development, proves \(\mathbb Q[u,v]/(u,v)\cong\mathbb Q\).
- `rationalResidueField_does_not_determine_principality` packages the hostile
  comparison: both ideals are maximal, but \((X)\) is principal and
  \((u,v)\) is not.

## Assumptions and coefficient types

The coefficient field is Lean's `Rat`. The rings are ordinary commutative
polynomial rings `Polynomial Rat` and `MvPolynomial (Fin 2) Rat`. No
Noetherianity, dimension theorem, choice of basis, or classification theorem
is assumed. Noncomputability is used only to construct quotient ring
equivalences.

## Audit conclusion

This increment specializes the existing determinantal-profile work. It does
not support a shared abstraction that derives generator arity from the
residue field: the two explicit kernels have the same residue field and
different minimal generator behavior. Residue-field equivalence therefore
forgets embedding-dimension data.

## Missing interfaces

No typing input is missing for this finite hostile example. A future theorem
about minimal generator number in arbitrary local rings would need a typed
local-ring structure, maximal ideal, residue field, and the cotangent-space
quotient \(\mathfrak m/\mathfrak m^2\). Those interfaces are intentionally not
introduced here because the present cross-sector evidence only requires the
concrete comparison.
