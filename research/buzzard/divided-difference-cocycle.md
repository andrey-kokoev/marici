# Newman divided-difference cocycle: Lean packet

## Source boundary

This increment formalizes the finite multiplicative core of Grothendieck's
`newman-divided-difference-cocycle.md`. It does not take logarithms or
differentiate moving roots.

## Formal objects and coefficient types

Over an arbitrary field, the pair divided difference is

\[
[f]_{x,y}=\frac{f(x)-f(y)}{x-y}.
\]

Every theorem carries explicit noncollision assumptions. A finite product is
taken over an arbitrary finite pair-index set.

## Theorems and hostile

- `pairDividedDifference_comp` proves the exact composition law.
- `pairDividedDifference_affine` proves that an affine coordinate contributes
  its constant slope.
- `finiteDividedDifferenceProduct_comp` lifts the cocycle to arbitrary finite
  products.
- `finiteDividedDifferenceProduct_affine` gives the factor `a^(card indices)`.
- `square_coordinate_nontrivial_cocycle_hostile` shows the nonlinear square
  coordinate contributes factor `3` on the pair `(2,1)`, versus `1` for the
  identity coordinate.

## Missing interfaces

The entropy statement `J_(g∘f)=J_f+J_g∘f` needs real or complex absolute
values, positivity/nonvanishing of every factor, logarithms of finite products,
and the precise squared-Vandermonde factor of two. The dynamic identity needs
collision-free differentiable root paths and chain rules. The corrected
entropy is exactly coordinate covariance; it creates no additional RH
positivity. Any arithmetic correction must be independently sourced.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/DividedDifferenceCocycle.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
