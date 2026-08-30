# Prime-square countercurrent renormalizes local valuation volume

## Finite relative determinant

Grothendieck's canonical local valuation two-cycle has oriented volume

`v_p=1-p^(-1)`.

The ordinary finite product `V_X=product_(p<=X) v_p` collapses to zero.  Do
not divide by its completed limit.  Retain at the same finite cutoff the
first primitive logarithmic countercurrent

`P_X=sum_(p<=X) p^(-1)`

The coefficient `p^(-1)` is the square of the primitive amplitude
`p^(-1/2)`.  It is therefore the even prime-square channel, not the odd
primitive coorientation current.  Form the relative determinant

`R_X=V_X exp(P_X)`.

This is source ordered: local exterior evaluation occurs first, the primitive
countercurrent is attached at the same cutoff, and only then is completion
taken.

## Convergence theorem

Its logarithm is

`log R_X=sum_(p<=X) [log(1-p^(-1))+p^(-1)]`.

For `0<x<=1/2`,

`0 <= -log(1-x)-x <= x^2/(2(1-x)) <= x^2`.

Therefore the absolute value of the tail is bounded by `sum_p p^(-2)`, which
converges.  The limit

`R_infinity=product_p (1-p^(-1)) exp(p^(-1))`

exists and is strictly positive.

The prime-square term is exactly what must be retained: omitting it gives zero,
while changing its coefficient to `c` leaves a residual `(c-1) sum 1/p`, so
the relative product tends to zero for `c<1` and infinity for `c>1`.
Finiteness and nonvanishing uniquely select coefficient one.

## Meaning

The local two-cycle and prime-square boundary current now form a canonical
relative determinant line at finite cutoff.  This does not contract the two
completed covectors and does not insert a Hilbert pivot.  It cancels only the
universal first-order completion anomaly.  Prime-square and higher terms
remain as an absolutely convergent source constant.

The odd primitive channel retains the bivector coorientation.  It must not be
identified with this even determinant countercurrent.

This is the first global scalar quantity in the current branch that survives
completion without a smoothing time or subtraction scale.

## Optical realization

For each admitted prime channel, measure the local oriented minor `1-1/p`.
Accumulate its logarithm together with the preregistered prime-square reference
`1/p` in the same cutoff clock.  The observable is

`log R_X=sum_(p<=X) [log(1-1/p)+1/p]`.

It must approach a finite negative constant.  Three high-information
falsifiers are:

- omit the prime-square countercurrent: the trace drifts to negative infinity;
- use coefficient `1+epsilon`: the trace drifts with the prime harmonic sum;
- misalign the two cutoff clocks: the cancellation loses telescoping
  provenance even when a finite numerical fit looks stable.

## Remaining gate

The relative determinant solves the scalar normalization anomaly of the
canonical local valuation cycles.  The RH-bearing boundary theorem still
requires a source map connecting this determinant line to the completed
hyperfunction response and its Green coorientation.

## Verification

```text
uv run python research/aspect/checkers/check_prime_square_countercurrent_relative_determinant.py
```
