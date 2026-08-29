# Endpoint loading requires Green energy beyond the resolved boundary return

## Nested Schur cell

Let \(E\) be the real endpoint plane, \(H\) the positive auxiliary history space, and

\[
\mathcal G
=
\begin{pmatrix}
A&C\\
C^{*}&D
\end{pmatrix},
\qquad
D>0.
\]

After eliminating the auxiliary history, the endpoint form is

\[
G_{\mathrm{eff}}
=
A-R,
\qquad
R=CD^{-1}C^{*}.
\]

Auxiliary positivity controls \(D\). Endpoint loading is the independent requirement

\[
R<A.
\]

Equivalently,

\[
\left\|
A^{-1/2}RA^{-1/2}
\right\|<1.
\]

## Saturation theorem

Suppose the endpoint energy is defined only by the same resolved history that produces the return:

\[
A=CD^{-1}C^{*}.
\]

Then

\[
G_{\mathrm{eff}}=0.
\]

Thus exact trace realization and a positive auxiliary block do not by themselves leave any endpoint reserve. If the source endpoint Gram is merely the pullback of the auxiliary history energy, the second contraction gate saturates identically.

This is the endpoint analogue of the earlier one-vector zero-Schur-reserve result.

## Required residual decomposition

The source must produce a decomposition

\[
A
=
R+Q,
\qquad
Q>0.
\]

Then

\[
G_{\mathrm{eff}}=Q.
\]

The residual \(Q\) must be independently typed. Candidate sources include:

- real two-window bulk overlap not determined by endpoint traces;
- derivative energy orthogonal to the minimal history extension;
- an archimedean or wall energy retained before elimination;
- a source cell interior mode whose boundary is the endpoint packet.

It cannot be added solely to force positivity.

## Reciprocal polarizations

If reflection diagonalizes the endpoint plane into \(E_+\oplus E_-\), both residual sectors must remain positive:

\[
Q_+>0,
\qquad
Q_->0.
\]

An averaged determinant or scalar endpoint energy can conceal saturation of one reciprocal sheet.

The endpoint-loading margin is

\[
\delta_{\mathrm{load}}
=
1-
\max_{\pm}
\left\|
A_\pm^{-1/2}
R_\pm
A_\pm^{-1/2}
\right\|.
\]

## Completion requirement

On compact off-seam regions, source continuity and finite-dimensionality turn strict positivity of \(Q(\sigma)\) into a uniform lower bound, provided no prime or grade normalization drives the residual to zero.

The exact theta trace matrix proves incidence rank, not residual positivity. A separate Green decomposition must expose \(Q\).

## Next source calculation

Compute the real two-window endpoint Gram \(A_p\) and subtract the resolved twisted-history return \(R_p\). The first decisive output is not a determinant but the residual matrix

\[
Q_p=A_p-R_p.
\]

If \(Q_p=0\), the current first Adams cell is a perfect realization with no coercive reserve. If \(Q_p>0\), the endpoint-loading gate closes locally and its uniformity can be audited.
