# Positive coherence forces a two-parameter nonuniform refinement through a regulated Gram space and radical quotient

## Correction to the naive positive lift

Set

\[
P=P_\Lambda,
\qquad
Q=F_SP_\Lambda F_S^{-1},
\qquad
A=U_S(g).
\]

The formal inside and outside channels are

\[
B_\Lambda=QP_\Lambda A,
\qquad
C_\Lambda=Q(I-P_\Lambda)A.
\]

Although `B_Lambda` is Hilbert--Schmidt under the cutoff hypotheses, `C_Lambda` is generally not. The outside region has infinite scaling volume, and convolution smoothing does not remove the infinite center-of-mass integral.

Therefore the unregulated Gram expression

\[
\begin{pmatrix}
\langle B,B\rangle&\langle B,C\rangle\\
\langle C,B\rangle&\langle C,C\rangle
\end{pmatrix}
\]

is not a typed Hilbert-space object.

This invalidates any direct positive eight-stage filler that inserts the full outside channel without another regulator.

## Second physical cutoff

Choose

\[
R>\Lambda
\]

and define

\[
C_{\Lambda,R}
=
Q_\Lambda(P_R-P_\Lambda)A.
\]

Both

\[
B_\Lambda=Q_\Lambda P_\Lambda A
\]

and `C_(Lambda,R)` are Hilbert--Schmidt. Hence the regulated Gram matrix

\[
\boxed{
\mathcal G_{\Lambda,R,S}(g)
=
\begin{pmatrix}
\|B_\Lambda\|_{HS}^2&
\langle B_\Lambda,C_{\Lambda,R}\rangle_{HS}\\
\langle C_{\Lambda,R},B_\Lambda\rangle_{HS}&
\|C_{\Lambda,R}\|_{HS}^2
\end{pmatrix}
\succeq0
}
\]

is mathematically legitimate at finite `(Lambda,R)`.

The regulated first-row observation is

\[
\operatorname{Tr}
(P_\Lambda Q_\Lambda P_RAA^*)
=
\|B_\Lambda\|_{HS}^2
+
\langle B_\Lambda,C_{\Lambda,R}\rangle_{HS}.
\]

Connes's product trace is recovered only after taking `R -> infinity` in this combined expression.

## Why numerical finite parts do not preserve positivity

The outside square

\[
\|C_{\Lambda,R}\|_{HS}^2
\]

generally diverges with annular scaling volume as `R -> infinity`. This divergence is absent from Connes's first-row trace and is not removed by

\[
2\|g\|^2\log\Lambda.
\]

Subtracting scalar counterterms separately from the four Gram entries need not preserve positive semidefiniteness. Therefore the signed asymptotic quotient cannot simply be applied entrywise to obtain a positive filler.

## Required common radical quotient

A positive limit requires a feature-level asymptotic decomposition

\[
\boxed{
Q_\Lambda P_RU_S(g)
=
\sqrt{2\log\Lambda}\Xi_S(g)
+
F_{\Lambda,R,S}(g),
}
\]

where:

1. `Xi_S(g)` lies in one common asymptotic/radical subspace;
2. `||Xi_S(g)||^2=||g||^2=h(1)`;
3. the divergent and finite pieces are orthogonal, or are separated by a positive quotient construction;
4. `F_(Lambda,R,S)` converges after quotienting the radical;
5. the construction is compatible with adjoining places and with the two cutoff orientations.

The expected radical is the closure of the range of the semilocal Eisenstein map.

Quotienting a Hilbert space by a closed subspace preserves positivity. Numerically subtracting a divergent scalar after trace does not.

## Revised positive edge stages

A positive geometry-to-trace route must distinguish at least the following semantic operations:

1. observer insertion `A=U_S(g)`;
2. inner physical cutoff `P_Lambda`;
3. Fourier cutoff `Q_Lambda`;
4. outer physical cutoff `P_R`;
5. inside/annular channel decomposition;
6. positive two-by-two Gram feature;
7. common asymptotic Eisenstein/radical feature;
8. Hilbert quotient or orthogonal conditioning;
9. correlated two-parameter limit `(Lambda,R(Lambda))->infinity`;
10. completed positive boundary form.

The old eight-node `C_24` route combined or omitted stages 4, 7, and 8 because they are unnecessary for the signed scalar theorem.

They cannot be represented as identity degeneracies in the positive category: each changes the domain, trace ideal, or Hilbert quotient.

## Consequence for uniform refinement

The existing uniform eight-node refinement remains valid in the signed asymptotic category. It is not sufficient for positive coherence.

A positive refinement must first enlarge the geometry--trace and spectral--trace routes by the second regulator and radical quotient. The source--spectral route need not acquire corresponding substantive operations; it can be padded by degeneracies after a common refinement is chosen.

Thus the correct positive architecture is a **nonuniform semantic factorization followed by a uniform common subdivision**:

\[
\boxed{
\text{factor each edge by its actual operations}
\quad\longrightarrow\quad
\text{take a common simplicial refinement}.
}
\]

If all ten displayed stages are retained separately, the common edges require ten nodes rather than eight. This is a sufficient stage count, not a proof of minimality.

## Relation to the 343 count

The current

\[
343=7^3
\]

count belongs to the seventh edgewise subdivision of the signed asymptotic tetrahedron.

A nine-arrow positive refinement would instead have

\[
9^3=729
\]

elementary tetrahedra under the same edgewise-subdivision convention.

This `729` is provisional: it applies only if the ten-stage list above is accepted without merging adjacent operations. The positive simplex itself has not yet been constructed, so these are candidate cells, not certified equivalences.

Current counts are therefore

\[
\boxed{
343/343
\text{ signed asymptotic cells},
}
\]

and

\[
\boxed{
0/729
\text{ candidate positive cells under the ten-node refinement}.
}
\]

The previous notation `0/343 positive cells` remains meaningful only as the statement that none of the old signed cells has yet been positively lifted.

## Exact next theorem

The next theorem should not be an abstract contraction between unregulated layer spaces. It should construct the asymptotic feature map `Xi_S` and prove that

\[
\left[
Q_\Lambda P_RU_S(g)

ight]
\in
\mathcal H_{\Lambda,R,S}/\overline{\operatorname{ran}E_S}
\]

has a cutoff-independent positive limit whose boundary trace equals the completed Weil form.

Only after this quotient theorem can the Halmos mode contraction and Sonin boundary sewing be tested on a legitimate Hilbert carrier.

## Disposition

The positive refinement decision is now definite:

\[
\boxed{
\text{eight uniform nodes are insufficient for the currently typed positive route}.}
\]

A second volume cutoff and a common radical quotient are substantive, nondegenerate stages. The appropriate replacement is a nonuniform edge factorization with a ten-node common refinement as the first explicit candidate.
