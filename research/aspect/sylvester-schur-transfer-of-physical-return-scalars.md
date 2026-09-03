# Sylvester–Schur transfer of physical return scalars

## Question

Can the physical trace and Fredholm determinant gate be computed without explicitly taking square roots or reconstructing every entry of the normalized return?

## Transfer identity

On the reduced supports where \(A\) and \(D\) are invertible, the normalized return

\[
K=A^{-1/2}CD^{-1}C^*A^{-1/2}
\]

is similar to

\[
\widetilde K=A^{-1}CD^{-1}C^*.
\]

Cyclicity and Sylvester's determinant identity give

\[
\operatorname{tr}K
=
\operatorname{tr}(D^{-1}C^*A^{-1}C)
\]

and

\[
\det(I-K)
=
\det(I-D^{-1}C^*A^{-1}C).
\]

Thus both scalar gates may be evaluated on the hidden support, whichever side has simpler source coordinates.

## Schur determinant ratio

For the full physical block form

\[
G=
\begin{pmatrix}
A&C\\
C^*&D
\end{pmatrix},
\]

Schur factorization gives

\[
\frac{\det G}{\det A\det D}
=
\det(I-D^{-1}C^*A^{-1}C)
=
\det(I-K).
\]

The return Fredholm scalar is therefore the normalized determinant of the complete coupled physical form. This is a stronger source target than an entrywise fit: derive \(G,A,D\) from the same wall–history–tail/PV constructor and compare their reduced determinants.

## Support gate

If \(D\) or \(A\) is singular, the displayed determinant ratio is undefined. Replacing inverses by pseudoinverses does not repair the formula on the unreduced ambient space because null directions contribute extra unit factors to \(\det(I-K)\) while \(\det A\det D=0\). One must first specify the source-derived supports, prove that \(C\) descends between them, and take reduced determinants there.

## Cross-prime boundary

These are pointwise identities. They do not construct prime diagonality, nonadjacent Green-return factorization, or a cross-prime Markov composition. A uniform lower bound still requires source control of the normalized block determinant over all primes.

## Verification

`research/aspect/checkers/check_return_scalar_transfer.py` verifies trace cycling, Sylvester equality, and the Schur determinant ratio on an exact rational coupled block, and confirms that a singular hidden block makes the ambient determinant ratio undefined.

## Disposition

The owner handoff is sharpened to a block-form calculation: supply reduced physical \(G_p,A_p,D_p\), verify support descent of \(C_p\), and bound

\[
\det G_p/(\det A_p\det D_p)
\]

uniformly away from zero while retaining \(\operatorname{tr}K_p<2\). No normalized square-root construction is required after these source objects exist.
