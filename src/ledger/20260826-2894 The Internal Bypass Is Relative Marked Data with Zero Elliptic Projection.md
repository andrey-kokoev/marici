# 2894 — The Internal Bypass Is Relative Marked Data with Zero Elliptic Projection

## Question

Does Entry 2892's exact bypass correction change the rank-two compact elliptic
period system, or only the marked relative extension?

## Frozen localization sequence

Let (E) be the compact elliptic curve and let

\[
D=\{(1,+),(1,-),(-3,+),(-3,-)\}
\]

be the four source-labelled finite marked occurrences.  The relative
localization sequence contains

\[
H^0(D)(-1)
\longrightarrow
H^1(E,D)
\longrightarrow
H^1(E)
\longrightarrow0.
\]

The occurrence residue map is the degree row

\[
(1,1,1,1).
\]

## Bypass class

Entries 2885 and 2887 identified the difference of the two internal bypasses
with the marked tube

\[
\tau_{1,+}-\tau_{1,-},
\]

represented in the ordered occurrence basis by

\[
b=(1,-1,0,0).
\]

Its degree is exactly zero:

\[
(1,1,1,1)b=0.
\]

Therefore (b) is a nonzero relative marked class before forgetting the
marks, but its image in compact elliptic cohomology is zero.

## Result

The exact logarithmic and finite-part shifts of Entry 2892 belong to the
finite marked Tate/Kummer localization kernel.  They do not alter the
rank-two compact elliptic quotient.

This is stronger than classifying the answer by the appearance of logarithms:
the vanishing follows from the source-labelled localization sequence and the
degree-zero occurrence vector.

## Interpretation

The source (i\epsilon) prescription selects a physically distinguishable
relative period while leaving the compact elliptic state unchanged.  The
additional information lives in how the physical chain is attached to the
marked coefficient extension, not in a second elliptic branch.

No new carrier divisor is required.

## Next falsifier

Test whether the source-selected relative class remains nonzero after the
complete physical readout, including the prescribed deck trace and soft
renormalized covector.  The existing occurrence covector detects the class,
whereas the coarse deck trace kills it; the full source readout must decide
which operation is physically authorized and in what order.

## Durable artifacts

- `research/benincasa/check_soft_internal_bypass_elliptic_projection.py`
- `research/benincasa/soft-internal-bypass-elliptic-projection.json`
