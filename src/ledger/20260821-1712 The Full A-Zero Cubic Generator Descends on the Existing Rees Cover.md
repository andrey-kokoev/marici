# 1712 — The Full A-Zero Cubic Generator Descends on the Existing Rees Cover

## All-order falsifier

Entry 1711 checks the first two normal grades.  Determine whether a new
logarithmic or deck-twisted extension appears at higher order.

## Completed strict transform

In the weighted coordinates

\[
A=\varepsilon^2,
\qquad
C=\varepsilon c,
\]

the only denominator in the complete generator is

\[
D=1+2\varepsilon^2ty.
\]

It restricts to `1` on the exceptional divisor.  Therefore

\[
D^{-1}=\sum_{k\geq0}(-2\varepsilon^2ty)^k
\]

and `log D` are regular formal series there.  The rational numerator is

\[
c^2y^2+2\varepsilon cxy+\varepsilon^2x^2.
\]

The deck transformation preserving the physical coordinates `A,C` is

\[
(\varepsilon,c)\longmapsto(-\varepsilon,-c).
\]

Both `D` and the numerator are invariant.  Thus the complete generating germ
has trivial deck character.

## Narrow result

\[
\boxed{
\text{the full correlated cubic generator extends and descends on the existing covariance Rees cover at every normal order.}
}
\]

No finite-order logarithmic extension or new coefficient chart appears.  The
logarithm already present in the bulk generator has no local monodromy around
`epsilon=0` because its argument is a unit.

The checker verifies the exact rational-series recurrence and deck parity
through order thirty.  The all-order statement follows from the displayed
closed form, not from extrapolation of the finite census.

## Durable artifacts

- `research/benincasa/checkers/cubic_generator_all_order_rees.rs`
- `research/benincasa/results/cubic-generator-all-order-rees.json`
- `research/benincasa/cubic-generator-all-order-rees.md`

## Next falsifier

Test one genuinely non-Gaussian input coefficient rather than a Gaussian state
followed by cubic evolution.  Add a predeclared connected third cumulant to the
initial state and determine whether the same finite generating presentation
and Rees chart survive, or whether the input cumulant requires a new completed
coefficient extension.
