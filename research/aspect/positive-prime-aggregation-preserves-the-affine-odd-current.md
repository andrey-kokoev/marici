# Positive prime aggregation preserves the affine odd current

## Local current as a positive integral

For a valuation interval of length `ell`, common forcing `f` produces the odd
affine displacement

`J_f(ell,z)=f((1-exp(-(1/2-z)ell))/(1/2-z)`

`                 -(1-exp(-(1/2+z)ell))/(1/2+z))`.

It has the integral form

`J_f(ell,z)=2f integral_0^ell exp(-u/2)sinh(zu) du`.

Consequently, for `f>0`, `ell>0`, and real `0<z<1/2`, every local current is
strictly positive.  Reciprocal reversal makes it strictly negative for
`-1/2<z<0`.

## Prime aggregation

Let `ell_p=log p` and assign nonnegative source weights `w_p`, with at least
one positive weight.  At any finite cutoff,

`J_X(z)=sum_(p in X) w_p J_f(log p,z)`

has the same sign as `z` throughout the real critical strip.  No cancellation
is possible there.  Arithmetic sampling and positive aggregation therefore
preserve the finite-place source current erased by the archimedean limit.

The statement survives increasing cutoffs whenever the weighted sum
converges.  It does not need unique factorization beyond identifying the
prime-labelled generators; its force comes from positivity of the source
measure.

## Seam behavior

On the critical seam `z=i tau`,

`J_f(ell,i tau)=2if integral_0^ell exp(-u/2)sin(tau u) du`.

The current is purely imaginary, but its imaginary part is strictly positive
for `tau>0`.  Indeed, writing `theta=tau ell`, its numerator is

`tau-exp(-ell/2)(tau cos(theta)+(1/2)sin(theta))`.

If `sin(theta)<=0`, positivity is immediate.  If `sin(theta)>0`, use
`sin(theta)/theta<=1`, `cos(theta)<=1`, and
`exp(ell/2)>1+ell/2`.  The numerator is again strictly positive.

Thus positive prime aggregation cannot cancel the affine current on the seam
either.  The actual phase distinction is:

- off the seam along the real strip, positivity forbids cancellation;
- on the seam, the current rotates to a sign-definite imaginary quadrature.

This is stronger than the generic positive Haar-deficit cosine transform,
which may have zeros.  The affine current uses a one-sided decreasing
exponential kernel and its sine transform has no positive-frequency zero.
Any cancellation must therefore enter through signed weights, subtraction of
the forcing reservoir, infinite completion outside the admitted convergence
class, or a different boundary projection.

## Optical test

Use one unequal-loss two-mode segment for each selected prime length `log p`.
Drive every segment through the same-sign common displacement and combine the
difference ports with positive gains.  A dark aggregate output at real
`0<z<1/2` falsifies the affine Green model or the claimed source-sign
calibration.  After rotation to `z=i tau`, the orthogonal quadrature must
remain bright with a fixed sign for every `tau>0`; a dark port there is an
even sharper falsifier.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_positive_prime_affine_aggregation.py
```
