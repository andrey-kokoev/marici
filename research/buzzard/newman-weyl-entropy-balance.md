# Newman nonlinear-Weyl entropy balance: Lean packet

## Source boundary

This increment formalizes the convention-fixed finite algebraic identity in
Grothendieck's `newman-weyl-anomaly-entropy-balance.md`. It does not derive the
velocity law from differentiable roots or the Riemann--von Mangoldt map.

## Formal objects and coefficient types

Over an arbitrary commutative ring, the transformed velocity at a finite
index is

\[
v_i=2m_iA_i+C_i.
\]

The entropy-rate pairing is `sum 2 A_i v_i`. Its two named outputs are the
mobility dissipation `4 sum m_i A_i²` and anomaly flux `2 sum A_i C_i`.

Order and positivity statements specialize the coefficient type to the real
numbers.

## Theorems and hostile

- `finiteEntropyRate_decomposition` proves the exact finite identity.
- `finiteEntropyRate_nonnegative_iff_anomaly_bound` proves that nonnegative
  entropy rate is equivalent to the anomaly flux being at least the negative
  mobility dissipation.
- `zero_anomaly_positive_mobility_nonnegative` proves the affine/zero-anomaly
  branch for nonnegative mobilities.
- `positive_mobility_negative_entropy_hostile` uses one site with
  `m=A=1`, `C=-3`: the positive contribution is `4`, anomaly is `-6`, and
  total rate is `-2`.

## Missing interfaces

The Newman specialization requires collision-free differentiable root paths,
the logarithmic Vandermonde gradient, a differentiable coordinate `f`, and
the chain-rule derivation of `m_i=f'(r_i)^2` and `C_i[f]`. The infinitesimal
coordinate expansion requires second and third derivatives with uniform
remainders. Any global anomaly bound for the smooth Riemann--von Mangoldt
coordinate is open. Dropping the anomaly is authorized only after proving it
vanishes, for example in an affine coordinate.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/NewmanWeylEntropyBalance.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
