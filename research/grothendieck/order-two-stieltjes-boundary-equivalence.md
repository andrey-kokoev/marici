# The order-two boundary representation is exactly the scalar Stieltjes gate

Let

\[
 F(x)=(4x-1)S(x)
\]

on the positive axis, with the forced boundary normalization `F(1/4)=0`.
Under the usual convergence assumptions, the following representations are
equivalent.

First, `S` is Stieltjes:

\[
 S(x)=\int_0^\infty\frac{d\mu(\lambda)}{x+\lambda},
 \qquad d\mu\ge0.                                      \tag{1}
\]

Second, `F'` is Stieltjes of order two:

\[
 F'(x)=\int_0^\infty\frac{d\rho(\lambda)}{(x+\lambda)^2},
 \qquad d\rho\ge0.                                    \tag{2}
\]

The measures are related by

\[
 d\rho(\lambda)=(1+4\lambda)d\mu(\lambda),\qquad
 d\mu(\lambda)=\frac{d\rho(\lambda)}{1+4\lambda}.     \tag{3}
\]

## Forward direction

For one Stieltjes atom,

\[
 \frac{d}{dx}\frac{4x-1}{x+\lambda}
 =\frac{1+4\lambda}{(x+\lambda)^2}.
\]

Integrating against `d mu` proves (2) and the first relation in (3).

## Reverse direction

Integrating (2) gives

\[
 F(x)=C-\int_0^\infty\frac{d\rho(\lambda)}{x+\lambda}.
\]

The normalization `F(1/4)=0` fixes

\[
 C=\int_0^\infty\frac{4\,d\rho(\lambda)}{1+4\lambda}.
\]

The atomwise identity

\[
 \frac{1}{4x-1}
 \left(\frac4{1+4\lambda}-\frac1{x+\lambda}\right)
 =\frac1{(1+4\lambda)(x+\lambda)}
\]

then yields (1) with the second measure in (3).

## Strategic consequence

The order-two representation is not a softer intermediate conjecture. For the
completed Xi boundary source it is the scalar Stieltjes/RH condition in a
different coordinate. Finite curvature and Loewner certificates test finite
compressions of this gate, but no finite rank can establish the full measure.

The extra explanatory target remains meaningful: construct `rho` or its Gram
space from the prime--theta correspondence without first reading it from the
zero divisor. That construction would explain self-adjointness; merely proving
existence by locating the zeros would be circular for this program.

This equivalence does not prove RH.

## Durable verification

- Checker: `checkers/order_two_stieltjes_boundary_equivalence.py`
- Result: `results/order-two-stieltjes-boundary-equivalence.json`
