# A positive Gaussian mixture falsifies archimedean endpoint dominance

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source-generated falsifier

## Positive completed source

Take the even positive Schwartz source

\[
\Phi(u)=e^{-u^2}+e^{-2u^2}.
\]

Its bilateral Laplace transform depends on (w=z^2):

\[
X(w)=\sqrt\pi
\left(
e^{w/4}+2^{-1/2}e^{w/8}
\right).
\]

Put

\[
w_0=-4\log2+8\pi i.
\]

Then

\[
e^{w_0/8}=-2^{-1/2},
\qquad
e^{w_0/4}=\frac12,
\]

so (X(w_0)=0). The derivative with respect to (w) is

\[
X'(w_0)=\frac{\sqrt\pi}{16}\ne0.
\]

Thus this is a simple zero strictly away from the negative real (w)-ray that
represents the critical line.

## Positive precursor

Let

\[
L=\frac14-\partial_u^2.
\]

Its inverse on the line has the positive Green kernel

\[
G(u)=e^{-|u|/2}.
\]

Therefore

\[
K=L^{-1}\Phi=G*\Phi
\]

is even, smooth, decaying, and strictly positive. It satisfies (K'(0)=0),
and its origin autocorrelation jets have the signs derived in ledger 3049:

\[
\rho_K(0)>0,
\qquad
\rho_K''(0)<0.
\]

The completion symbol (1/4-w_0) is nonzero, so the off-ray zero belongs to
the precursor transform as well; it is not one of the polynomial completion
zeros.

## Falsified theorem

The following package does not confine zeros:

1. positive even completed source;
2. positive decaying archimedean precursor;
3. exact completion differential;
4. fixed-sign origin Sobolev jets;
5. exact terminal-forcing factorization.

All five hold here, yet the completed transform has a simple off-ray zero.
Consequently the precursor odd bulk can overcome or balance the origin jets.
Archimedean endpoint dominance is false as a universal theorem.

## What remains theta-specific

The actual theta source has more than positivity and Gaussian decay: it is a
labelled lattice sum with exact prime-scale and Poisson correspondences. Those
relations must constrain the precursor odd bulk before aggregation. No theorem
depending only on the archimedean source shape can finish the argument.

## Verification

The exact checker verifies the closed-form zero, its simplicity, its nonzero
distance from the critical ray, and the nonvanishing completion symbol.
