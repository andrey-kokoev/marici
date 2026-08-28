# Seam-length rigging makes the primitive common mode continuous

## Source-derived coefficient norm

The seam attached to prime \(p\) has length \(L_p=\log p\). Use that
existing source quantity to define the prime coefficient space

\[
\mathcal C_{\rm seam}
=
\left\{
x:
\sum_p(\log p)|x_p|^2<\infty
\right\}.
\]

This is not an arbitrary regularization parameter. The same factor is the
dual-cost scale of a fixed seam interval.

## Primitive functional

The common primitive mode acts on finite packets by

\[
\ell_{\rm prim}(x)
=
\sum_p p^{-1/2}x_p.
\]

Cauchy–Schwarz in the seam-length norm gives

\[
|\ell_{\rm prim}(x)|^2
\leq
\left(
\sum_p(\log p)|x_p|^2
\right)
\left(
\sum_p\frac1{p\log p}
\right).
\]

The prime series on the right converges. Therefore the primitive common mode
is a continuous functional on \(\mathcal C_{\rm seam}\).

The same functional is not continuous on unweighted \(\ell^2(\mathbb P)\),
because its squared dual norm is \(\sum_p1/p\).

## Compatibility with source transports

Mellin modulation acts diagonally:

\[
(U_tx)_p=p^{it}x_p.
\]

It preserves the seam-length norm exactly. Reciprocal conjugation

\[
(Jx)_p=\overline{x_p}
\]

is antiunitary, and prime cutoffs form a dense directed family.

Thus the rigging retains the transports already authorized by the source
instead of suppressing them.

## Joint incidence

Write the source columns as

\[
b_p=p^{-1/2}\phi+r_p.
\]

The common component extends as the bounded rank-one operator

\[
x\longmapsto\phi\ell_{\rm prim}(x).
\]

A sufficient condition for the residual synthesis to be Hilbert–Schmidt from
\(\mathcal C_{\rm seam}\) is

\[
\sum_p\frac{\lVert r_p\rVert^2}{\log p}<\infty.
\]

The full joint incidence then becomes a bounded operator without deleting the
primitive direction.

## Why this does not finish completion

Many heavier coefficient weights would also make the primitive functional
continuous. The point of \(\log p\) is source selection: it is already the
seam length and therefore requires no fitted exponent.

The square return grade, joint Schur operator, reciprocal low-grade pairing,
and archimedean cap still need continuity in this topology. Bounded incidence
alone does not prove that the complete relative determinant exists.

## DPC verdict

Resolved:

- an explicit source-derived prime coefficient rigging;
- continuity of the primitive common-mode functional;
- unitary Mellin modulation and reciprocal conjugation;
- a sufficient residual Hilbert–Schmidt condition.

Withheld:

- continuity of the full return map;
- third-Schatten control of the joint Schur operator;
- the projective-infinity and archimedean boundary ports;
- zero-state implications.

The finite falsifier for the unweighted topology is the normalized prime
half-density packet. The same packet is uniformly controlled in the
seam-length topology.

## Verification

The checker `check_seam_length_prime_rigging.py` compares the unweighted and
seam-length dual budgets over increasing prime cutoffs and verifies exact
phase and conjugation invariance on finite packets.
