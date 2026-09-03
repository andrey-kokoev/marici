# Two positive Pauli diagonals do not imply effective-block invertibility

## Question

If both diagonal residuals after Schur elimination are positive, does scalar-kernel exclusion follow for the effective two-coordinate block?

## Exact countermodel

Consider the positive semidefinite Hermitian block

\[
A^{\rm eff}=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Both diagonal residuals equal one. Nevertheless

\[
A^{\rm eff}\begin{pmatrix}1\\-1\end{pmatrix}=0.
\]

The Pauli twirl erases the mixed entry:

\[
X A^{\rm eff}X+Y A^{\rm eff}Y=2I.
\]

Thus the two Pauli-observed diagonal loadings are uniformly positive while the unobserved coherent difference mode is an exact null of the effective block.

More generally, for

\[
A^{\rm eff}=\begin{pmatrix}\alpha&w\\\overline w&\beta\end{pmatrix},
\qquad \alpha,\beta>0,
\]

invertibility requires

\[
\alpha\beta-|w|^2>0.
\]

Positive diagonal residuals alone establish only \(\alpha>0\) and \(\beta>0\). They neither bound \(w\) nor prove that the Pauli output family is jointly faithful on the scalar-null quotient.

## Relation to Schur return

The example is compatible with Schur elimination: take no auxiliary coupling, so the return is zero and the displayed matrix is already the effective block. Adding a positive return does not repair the logical gap unless its mixed entry and the raw mixed endpoint entry are both controlled.

## Claim boundary

The two diagonal residual criterion proves survival of the two Pauli-observed coordinates. It proves effective-block kernel exclusion only with one additional premise:

- a determinant/coherence bound \(|w|^2<\alpha\beta\); or
- a theorem that the two Pauli outputs are jointly faithful on the intended quotient and that scalar nullity factors through those outputs.

Neither premise follows from the diagonal theta-mass inequalities.

## Disposition

Reject the direct promotion from two positive diagonal residuals to scalar-null confinement. The next executable local gate is the mixed-coherence determinant bound. The separately requested complete theta-history Gram table remains necessary because it supplies the missing diagonal and mixed entries from source data.
