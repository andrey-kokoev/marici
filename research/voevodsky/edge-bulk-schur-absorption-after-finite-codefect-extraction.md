# Edge--bulk Schur absorption after finite co-defect extraction

Let `P` be the finite dangerous bulk space and let `Q=I-P`. After adjoining
the rescaled edge channel to `Q`, write the form as

\[
\mathcal A=
\begin{pmatrix}
 F & B^*\\
 B & C
\end{pmatrix}
\quad\text{on }P\oplus Q.
\]

Assume the normalized bulk/edge complement estimate

\[
C\ge \alpha Q,
\qquad \alpha>0.
\]

For any finite tail map `Y:P->Q`, set

\[
Z=I_P-Y,
\qquad
J=Z^*\mathcal AZ,
\qquad
R=Q\mathcal AZ.
\]

Completing the square gives the range-compatible identity

\[
\mathcal A[Zp+q]
=J[p]+2\Re\langle Rp,q\rangle+C[q],
\]

and hence

\[
\mathcal A\ge0
\quad\Longleftarrow\quad
J-\alpha^{-1}R^*R\ge0.
\]

This is the required edge--bulk Schur absorption theorem. It does not require
an operator-norm-continuous threshold family, nor an exact inverse of `C`.
Only three quantities must be certified:

1. a complement floor `alpha` after finite co-defect extraction;
2. the finite candidate form `J`;
3. the range-compatible residual Gram `R^*R`.

For a raw block estimate, taking `Y=0` yields the familiar sufficient
condition

\[
F\ge fI,
\quad C\ge\alpha I,
\quad \|B\|^2<f\alpha.
\]

The regularized version is substantially sharper when `F` has near-null
modes, because only the component of the cross term missed by `Y` is charged
to the complement floor.

In the rescaled edge model, `C` must include the full endpoint--prime Hankel
discrepancy, not a single entering translation. Thus this theorem isolates the
arithmetic task cleanly: prove a complement floor for the discrepancy operator
and put its finitely many near-unit modes into `P`.
