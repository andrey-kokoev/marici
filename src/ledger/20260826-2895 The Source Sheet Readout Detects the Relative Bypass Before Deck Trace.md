# 2895 — The Source Sheet Readout Detects the Relative Bypass Before Deck Trace

## Competing readouts

In the ordered occurrence basis

\[
((1,+),(1,-),(-3,+),(-3,-)),
\]

the internal bypass class is

\[
b=(1,-1,0,0).
\]

There are two distinct operations.

The source period uses the analytic boundary value of \(\sqrt{k}\).  The
negative-imaginary \(i\epsilon\) prescription therefore selects the labelled
positive-sheet occurrence, with covector

\[
f_{\rm src}=(1,0,0,0).
\]

The optional coarse deck trace is

\[
T_{\rm deck}=
\begin{pmatrix}
1&1&0&0\\
0&0&1&1
\end{pmatrix}.
\]

## Exact comparison

The source readout detects the bypass:

\[
f_{\rm src}b=1.
\]

The deck trace kills it:

\[
T_{\rm deck}b=0.
\]

These statements do not conflict.  They concern differently typed readouts.
The source integral is defined on one analytic sheet before any optional deck
quotient.  Applying the trace first discards precisely the occurrence polarity
that distinguishes the two bypasses.

## Result

The exact route correction of Entry 2892 survives the source-authorized
physical occurrence readout.  It disappears only under a later coarse trace.
Trace-vanishing is therefore loss of labelled occurrence information, not
evidence that the source-selected relative period is physically trivial.

This preserves the distinction established in Entry 2894:

- compact elliptic projection: zero;
- marked relative source readout: nonzero.

## Consequence

The physical soft readout is an extension-sensitive observable.  Compact
elliptic cohomology alone cannot reconstruct it, even though the underlying
elliptic state is unchanged.

## Next falsifier

Compute the induced affine transport law under composition of successive
marked collisions.  Test whether route corrections add as an abelian
Tate/Kummer cocycle or acquire a nontrivial commutator at intersecting marked
supports.

## Durable artifacts

- `research/benincasa/check_soft_internal_source_readout_order.py`
- `research/benincasa/soft-internal-source-readout-order.json`
