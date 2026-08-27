# The moving-seam derivative is exactly the local Green forcing

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact boundary-current theorem with sampling obstruction

## Window transform

For the completed positive source (Phi), define

\[
W_L(d)=2\int_0^L\Phi(q)\Phi(q+d)\,dq
\]

and take its odd separation transform

\[
\mathcal K_{W_L}(z)
=\int_0^\infty W_L(d)\sinh(zd)\,dd.
\]

Differentiation at the moving seam gives

\[
\partial_LW_L(d)=2\Phi(L)\Phi(L+d).
\]

The transported half-tails satisfy

\[
H_+(L,z)-H_-(L,z)
=2\int_0^\infty\Phi(L+d)\sinh(zd)\,dd.
\]

Therefore

\[
\partial_L\mathcal K_{W_L}(z)
=\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr).
\]

The right side is exactly the unsymmetrized local forcing density in the
doubled Green identity. The missing source current was already present as the
derivative of the finite moving-seam window.

## Global accumulation

At (L=0), the window vanishes. Under source decay,

\[
W_L(d)\longrightarrow\rho(d)
\]

as (L\to\infty). Hence

\[
\mathcal K(z)
=\int_0^\infty
\partial_L\mathcal K_{W_L}(z)\,dL.
\]

Thus the entire odd forcing is an accumulated boundary variation. This is an
exact source-current interpretation, not a formal antiderivative invented
after seeing the residual.

## Arithmetic sampling obstruction

The prime-scale recursion of ledger 3042 does not provide all seam positions.
For a fixed prime it supplies only

\[
L=\log p,
\]

and valuation iteration supplies integer multiples (k\log p). Across all
prime powers, these positions form a discrete arithmetic subset of the
positive scale axis.

Therefore the continuous identity does not yet imply arithmetic telescoping.
One still needs a source-derived quadrature or incidence law converting the
prime-power seam samples into the full (L)-integral, together with the
archimedean remainder. Inventing interpolation weights would merely repackage
the forcing.

## Meaning

The programme has separated two statements:

1. The doubled forcing is a genuine moving-boundary current. This is proved.
2. The arithmetic constructor packet reconstructs and cancels its total
   endpoint variation. This remains open.

The second statement is now the precise global theorem. Its smallest
falsifier is a finite prime-power packet for which any proposed source-derived
quadrature leaves a nonzero window increment.

## Verification

The checker proves the exact discrete analogue on a symbolic finite source:
one-step window growth equals the local forcing cell, the empty window is zero,
and the terminal window equals the full forcing sum.
