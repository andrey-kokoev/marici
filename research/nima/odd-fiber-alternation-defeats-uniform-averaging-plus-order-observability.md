# Odd-fiber alternation defeats uniform averaging-plus-order observability

## Exact escape sequence

For odd fiber size \(r\), let

\[
a_r=(1,-1,1,-1,\ldots,1)^T.
\]

The order matrix satisfies

\[
S_ra_r=0.
\]

The coordinate sum of \(a_r\) is one, so averaging plus order is jointly
faithful at each finite \(r\). But

\[
\lVert a_r\rVert=\sqrt r.
\]

For the unit vector

\[
x_r=\frac{a_r}{\sqrt r},
\]

we obtain

\[
S_rx_r=0,
\qquad
\sum_i(x_r)_i=\frac1{\sqrt r}\longrightarrow0.
\]

If the averaging port is normalized by \(1/r\), its output decays even faster:

\[
E_rx_r=\frac1{r\sqrt r}.
\]

Thus the stacked averaging-plus-order observation map has no
cutoff-independent lower bound.

## Interpretation

The order port detects every finite mean-zero state, but its odd-dimensional
kernel approaches the mean-zero hyperplane as the fiber grows. Finite
transversality is not uniform transversality.

This is the same completion pattern seen earlier in other coordinates:

- each finite cutoff has full rank;
- the exceptional direction changes with cutoff;
- its remaining visible component tends to zero;
- completion acquires an escaping state unless another typed port or topology
  excludes the sequence.

## Required additional structure

At least one further source-derived mechanism is necessary:

1. a parity-sensitive port that detects odd alternation uniformly;
2. a coefficient topology assigning growing norm to alternating packets;
3. a refinement law forbidding these packets from forming a completed state;
4. a boundary current whose pairing with \(a_r\) remains bounded below.

The positive Mellin window may detect the vector at each finite cutoff, but its
adjacent-label sensitivity already collapses. It cannot be assumed to repair
this sequence without an explicit uniform estimate.

## Finite falsifier

For every proposed completion, evaluate the normalized odd alternating packet.
If every declared output tends to zero while the source norm remains one, the
completion-stability claim is false.

