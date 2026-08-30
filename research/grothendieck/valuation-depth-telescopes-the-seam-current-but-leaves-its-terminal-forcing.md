# Valuation depth telescopes the seam current but leaves its terminal forcing

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact correction and terminal-boundary obstruction

## Correction to the sampling picture

Fix one prime (p) and write (L=\log p). Its valuation depths give the
ordered seam positions

\[
0,L,2L,3L,\ldots.
\]

These are not merely point samples of the moving-seam derivative. Consecutive
positions bound intervals that partition the full positive scale axis.

For the autocorrelation window

\[
W_R(d)=2\int_0^R\Phi(q)\Phi(q+d)\,dq,
\]

define the valuation-depth increment

\[
\Delta_{p,k}W(d)
=W_{(k+1)L}(d)-W_{kL}(d).
\]

Then

\[
\Delta_{p,k}W(d)
=2\int_{kL}^{(k+1)L}\Phi(q)\Phi(q+d)\,dq.
\]

Summing over all valuation depths gives the exact pre-aggregation coboundary

\[
\sum_{k\ge0}\Delta_{p,k}W(d)
=W_\infty(d)-W_0(d)
=\rho(d).
\]

The same statement holds after the odd separation transform. Thus no
von-Mangoldt point quadrature is required to reconstruct the forcing. Ledger
3046 remains correct for the point-quadrature shortcut, but that shortcut is
not forced by the valuation-chain architecture.

## The terminal boundary survives

Coboundary does not mean cancellation. The initial window is zero, while the
terminal window is the full autocorrelation. Therefore

\[
\sum_{k\ge0}\Delta_{p,k}\mathcal K_W(z)
=\mathcal K(z).
\]

The valuation chain reconstructs the entire Green forcing as its boundary at
infinite depth. It does not make that boundary vanish.

This sharply relocates the problem: the primitive and square currents need not
approximate a continuous integral, but the completed source still needs a
law disposing of the terminal autocorrelation current.

## Reciprocal reflection is tautological here

Suppose the direct zero-state identity is

\[
2aE=-2\operatorname{Re}\mathcal K(z).
\]

Reciprocal reflection sends (a\mapsto-a) and
(mathcal K(z)\mapsto-\mathcal K(z)). The reflected identity is merely the
negative of the first. Adding them cancels both the horizontal energy and the
forcing; subtracting them reproduces the original equation.

Therefore reciprocal oddness alone cannot remove the terminal current while
retaining the (aE) term needed for zero confinement. An additional source
incidence must act differently on energy and terminal forcing.

## Remaining theorem

The exact target is now:

> Derive an archimedean or modular endpoint incidence that cancels the terminal
> autocorrelation current without simultaneously cancelling the horizontal
> bulk energy.

This incidence must be constructed before imposing a zero and must fail on the
positive two-cell hostile source. A plain reciprocal copy cannot do the job.

## Verification

The checker proves finite symbolic valuation-block telescoping, verifies the
nonzero terminal window, and confirms that reciprocal summation gives a
tautology while reciprocal subtraction returns the original identity.
