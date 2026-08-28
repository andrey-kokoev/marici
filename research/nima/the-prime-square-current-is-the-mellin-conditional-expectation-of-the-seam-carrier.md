# The Prime-Square Current Is the Mellin Conditional Expectation of the Seam Carrier

## Mellin conjugation on the labelled carrier

For a finite prime packet, let

\[
b_p=\frac{c_p}{\sqrt p}
\]

and form the seam carrier

\[
K=bb^*.
\]

Mellin transport acts diagonally on the labelled amplitude:

\[
(U_t b)_p=p^{-it}b_p.
\]

It therefore acts on carriers by conjugation,

\[
\alpha_t(K)=U_tKU_t^*,
\]

with matrix entries

\[
\alpha_t(K)_{pq}
=
e^{-it\log(p/q)}K_{pq}.
\]

The diagonal is fixed. Every off-diagonal entry lies in the nonzero character
sector indexed by \(\log(p/q)\).

## Haar averaging is diagonal projection

Take the invariant mean over the Mellin flow:

\[
\mathbb E_{\mathrm M}(K)
=
\operatorname{Mean}_t\alpha_t(K).
\]

Distinct prime ratios have nonzero frequencies off the diagonal. Haar
orthogonality gives

\[
\mathbb E_{\mathrm M}(K)_{pq}
=
\begin{cases}
|c_p|^2/p,&p=q,\\
0,&p\ne q.
\end{cases}
\]

Hence

\[
\mathbb E_{\mathrm M}(bb^*)
=
\operatorname{diag}(|c_p|^2/p).
\]

This is exactly the labelled prime-square current.

## Reconciliation of the earlier collision

The seam carrier and prime-square density share a diagonal but are not the
same carrier. Their lawful relationship is a directed route from the seam
carrier, through Mellin conditional expectation, to the prime-square current.

The map is positive, unital on the carrier algebra, idempotent, and preserves
the fixed-point diagonal. It is not invertible. The off-diagonal relationship
energy is its kernel component:

\[
K-\mathbb E_{\mathrm M}(K).
\]

Thus prime-square observation is a symmetry reduction of the seam carrier.
Attempting to reconstruct the seam from the square current reverses a
noninvertible conditional expectation and necessarily adds information.

## Ordered-port consequence

There are now two legitimate routes with distinct output types:

1. retain \(K\) and observe its Mellin orbit;
2. apply \(\mathbb E_{\mathrm M}\) and retain only the invariant square
   current.

They commute only after another application of the fixed-point projection.
Calling the outputs equal because their diagonals agree erases the
nontrivial-character sectors.

The minimum comparison cell is the residual

\[
R_{\mathrm M}(K)
=
K-\mathbb E_{\mathrm M}(K).
\]

For two nonzero prime amplitudes this residual has zero diagonal and negative
determinant, reproducing the earlier two-prime falsifier.

## Completion gate

For trace-class \(K\), the conditional expectation is contractive and extends
normally. The normalized Euler cutoff, however, escapes trace-class
compactness into the prime-harmonic corona. The remaining question is whether
the corona enlargement carries a compatible conditional expectation and
retains the residual as a module, rather than only its zero-frequency state.

