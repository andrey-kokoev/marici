# RH Schur elimination needs a relative cutoff connection

## Result

Blockwise cutoff compatibility does not make the Schur–Evans comparison natural.

Let a cutoff system have bulk block (A_X), boundary incidence (B_X), scalar block (C_X), and reduced boundary function

\[
S_X=C_X-B_X^*A_X^{-1}B_X.
\]

Suppose a larger cutoff (Y) restricts to the old blocks. This does not imply that (S_Y) restricts to (S_X). The inverse of the enlarged bulk block sees paths through the new internal states, so eliminating those states changes the old boundary feedback.

## Smallest hostile

At the old cutoff, take

\[
A_X=1,\qquad B_X=1,\qquad C_X(z)=z+1.
\]

Then (S_X(z)=z).

At the enlarged cutoff, take

\[
A_Y=
\begin{pmatrix}
1&1/2\\
1/2&1
\end{pmatrix},
\qquad
B_Y=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
C_Y(z)=z+1.
\]

The old (A), (B), and (C) are recovered by restriction. Nevertheless,

\[
B_Y^*A_Y^{-1}B_Y=\frac43,
\qquad
S_Y(z)=z-\frac13.
\]

The zero at (z=0) moves to (z=1/3). Ordinary block restriction therefore fails as a zero-divisor transport law.

## Categorical correction

The cutoff arrow must carry more than embeddings of the four colligation ports. It needs a source-derived relative Schur connection measuring the feedback created by newly admitted internal states:

\[
\Delta_{X,Y}
=
B_Y^*A_Y^{-1}B_Y
-
B_X^*A_X^{-1}B_X.
\]

The scalar block must obey the matching transport law

\[
C_Y-C_X=\Delta_{X,Y}+d\log u_{X,Y}
\]

in the appropriate additive or multiplicative determinant-line coordinate. The transition (u_{X,Y}) must be independently source-derived and nowhere zero. It cannot be defined from the desired zero divisor.

For three cutoffs, the relative increments must telescope. In additive coordinates,

\[
\Delta_{X,Z}=\Delta_{X,Y}+\Delta_{Y,Z}.
\]

In determinant-line coordinates, the corresponding units must satisfy

\[
u_{X,Z}=u_{Y,Z}u_{X,Y}.
\]

This is the missing coherencer in a precise sense: it records the boundary effect of integrating in a new source layer.

## DPC

Candidate: blockwise naturality alone.

Verdict: rejected by the two-state hostile.

Candidate: compensate the feedback increment by fitting (C_Y).

Verdict: algebraically successful but source-circular.

Surviving candidate: derive the relative scalar current and the bulk feedback increment independently from the same labelled source addition, then prove their difference is a nowhere-zero determinant-line transition satisfying the cocycle law.

## Immediate arithmetic test

For one prime or prime-power addition, compute before scalar aggregation:

1. the new-state feedback increment;
2. the endpoint, primitive, square, seam, and archimedean scalar increment;
3. their typed residual;
4. the residual under two additions in both orders.

A single nonzero non-cocyclic residual closes the proposed comparison. Exact agreement for independently constructed additions would establish the first genuine cutoff connection rather than another scalar reformulation.
