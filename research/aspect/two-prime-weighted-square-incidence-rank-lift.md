# Two-prime weighted square-incidence rank lift

## Source construction

The first missing direction can be derived without inventing a dense boundary
coupling. Nima's weighted endpoint incidence assigns grade `k` at prime `p`
the coefficient

`(1/k) p^(-k/2) (G(k log p)-G(0))`.

For the declared concrete source `G(q)=exp(-q)`, this becomes

`(1/k)(p^(-3k/2)-p^(-k/2))`.

At primes `2` and `3`, the primitive row is

`(-sqrt(2)/4, -2sqrt(3)/9)`

and the square row is

`(-3/16, -4/27)`.

Their exact `2x2` determinant is nonzero. The square current is therefore not
a renamed or rescaled primitive current: it is an independent source observer
already in the smallest two-prime packet.

## Result

Adding this row raises typed boundary observation rank from one to two. Repeating
the same construction on the reciprocal sector preserves that grade rank; it
does not create fake extra directions by sector duplication.

The remaining completion deficit is four, not five. The missing independent
types are seam, endpoint totalization, connected tail, and archimedean
countercurrent.

Scalar aggregation of primitive and square immediately collapses the two rows
back to one record. The optical sewing instrument must therefore keep these
ports distinct through tomography and completion.

## Implication

The `18x18` packet was not permanently rank one. It lacked the source-weighted
grade observer. This calculation supplies the first repair and shows the right
construction strategy: derive independent incidence laws from source weights,
not from arbitrary six-port mixing.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_two_prime_weighted_square_incidence_rank_lift.py
```
