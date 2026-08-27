# Primitive and square currents have half-order and zero-order scale boundaries

## Question

On the compactified scale base \(r=1/p\), what test-function vanishing is
required for the primitive and prime-square currents to act continuously at
the boundary \(r=0\)?

## Weighted scale test spaces

For \(\alpha\ge0\), let \(C_\alpha\) consist locally of functions satisfying

\[
|f(r)|\le C r^\alpha
\qquad(r\downarrow0).
\]

On the critical seam \(s=1/2+it\), define the labelled scale currents

\[
\mu_{1,t}(f)
=
\sum_p p^{-1/2-it}f(p^{-1})
\]

and

\[
\mu_{2,t}(f)
=
\sum_p p^{-1-2it}f(p^{-1}).
\]

## Exact absolute-continuity thresholds

For \(f\in C_\alpha\), the primitive terms are bounded by

\[
C p^{-1/2-\alpha}.
\]

The prime sum converges absolutely precisely above the threshold

\[
\alpha>\frac12.
\]

The square terms are bounded by

\[
C p^{-1-\alpha},
\]

and converge absolutely for

\[
\alpha>0.
\]

At \(t=0\), the boundary cases diverge: the square threshold is the Euler
sum \(\sum_p1/p\), while the primitive threshold has the same exponent one.
Thus the thresholds are sharp for continuous absolute action on these
weighted test spaces.

## Boundary typing

The two arithmetic currents occupy different conormal grades at \(r=0\):

- the primitive current requires more than half an order of vanishing;
- the square current requires any positive order but fails on the constant
  boundary value.

This is the scale-base version of the earlier pro-Gram distinction. The
primitive and square channels cannot be represented by one scalar boundary
functional or one Hilbert norm.

The fifth wall supplies the value coordinate at \(r=0\), but it does not by
itself extend either current across that value. A completed modular current
must provide a source-derived finite-part extension whose boundary term lands
in the constant–delta plane.

## Pullback interpretation

For a labelled section \((r,W_r)\), the weighted prime sums act first on its
scale dependence. The reciprocal windows satisfy \(W_r\to-1\), so they do
not vanish at the boundary. Consequently neither current may be applied to
the window family as an ordinary absolutely convergent scalar sum on the
critical seam.

Subtracting the boundary value gives

\[
W_r+1,
\]

which vanishes rapidly on each fixed compact \(q\)-set as \(r\to0\). This
separates the packet into:

1. an explicit constant-wall coefficient carrying the divergent prime sum;
2. a boundary-vanishing window remainder on which both currents improve.

That subtraction is authorized because \(-1\) is the declared scale-boundary
fiber of the pullback, not a fitted counterterm.

## Remaining gate

The next exact calculation is the finite-part sewing law for the constant
coefficient. One must combine primitive, square, and archimedean boundary
currents before continuation and prove that their total coefficient of the
constant–delta fiber vanishes or becomes a canonical finite distribution.

The route fails if this cancellation depends on zero data, on separately
continuing the primitive prime sum, or on choosing a subtraction other than
the pullback's source-fixed boundary value.

## Result

The scale pullback converts the arithmetic completion problem into a sharp
boundary-regularity statement. Primitive incidence has threshold
\(\alpha>1/2\); square incidence has threshold \(\alpha>0\). Subtracting the
canonical fifth-wall value isolates both divergences in one explicit boundary
coefficient, leaving a rapidly vanishing window remainder.
