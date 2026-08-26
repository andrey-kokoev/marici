# Xi multiplicity amplification: Lean packet

## Source boundary

This increment formalizes the finite local obstruction in Grothendieck's
`xi-weyl-multiplicity-repair.md`. It does not assume RH, real zeros, or a
Herglotz representation.

## Formal objects and coefficient types

Over a commutative ring, `repeatedRootJordan λ` is

\[
\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},
\]

the multiplication operator on the local principal-ideal quotient at a
double root. `amplifiedRepeatedRoot λ` is the semisimple diagonal matrix
`λ I₂`.

## Theorems and hostile

- `jordan_symmetrizer_first_diagonal_zero` proves algebraically that every
  metric satisfying `H J = Jᵀ H` has `H₀₀=0`.
- `repeatedRootJordan_has_no_positive_symmetrizer` concludes that no such
  metric can even satisfy the necessary positive first-basis condition.
- `amplifiedRepeatedRoot_characteristic` proves that semisimple amplification
  has characteristic factor `(z-λ)²`.
- `double_root_three_object_hostile` instantiates the distinction at `λ=1`.

Thus a scalar atom, a nonreduced Jordan quotient, and a multiplicity-amplified
semisimple operator cannot be identified.

## Missing interfaces

The Xi application requires meromorphic `-Xi'/Xi`, recovery of positive
integer multiplicity from pole residues, a real-support theorem equivalent to
Nevanlinna positivity/RH, construction of the Hilbert direct sum, compact
resolvent and regularized determinant convergence, and a source-derived
semisimplification map. The scalar Herglotz model alone records residue mass,
not eigenspace dimension. None of these analytic or RH-strength inputs is
assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/MultiplicityAmplification.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
