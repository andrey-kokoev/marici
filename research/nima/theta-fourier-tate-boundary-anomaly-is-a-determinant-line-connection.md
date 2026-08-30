# Fourier–Tate boundary anomaly is a determinant-line connection

## Source operator identity

Let (W_N) be the finite-cutoff primal-dual Fourier–Tate sewing map. Let
(Q_+) and (Q_-) be the typed Mellin label generators on its source and
target sectors. Define the transported sewing family

\[
W_N(z)=e^{zQ_-}W_Ne^{zQ_+}.
\]

Its first derivative is

\[
W_N'(0)=Q_-W_N+W_NQ_+.
\]

Therefore the proposed boundary anomaly

\[
\mathcal A_N=Q_-W_N+W_NQ_+
\]

is exactly the connection derivative of the sewing map under opposite-sector
Mellin transport.

This gives the anomaly a direct operator meaning. It is not curvature of
ordinary label translation, since the label generator commutes with that
translation and with diagonal finite-label splits.

## Determinant-line jet

When (W_N(0)) is a square invertible map, Jacobi's identity gives

\[
\left.
\frac{d}{dz}
\log\det W_N(z)
\right|_{z=0}
=
\operatorname{Tr}
\left(
W_N^{-1}\mathcal A_N
\right).
\]

Thus the scalar determinant-frame current is the trace of the full typed
boundary anomaly in the sewing frame.

The converse is false. A nonzero traceless anomaly can be invisible to the
determinant jet. The operator anomaly must therefore be retained until the
source law proves that only its determinant-line component matters.

If (W_N) is rectangular, Fredholm, or a closed relation, the correct object
is the induced connection on its determinant line. A scalar determinant may
not be written until kernels, cokernels, and domains have been typed.

## Exact frame transformation law

Let an independently framed presentation be

\[
\widetilde W(z)=L(z)W(z)R(z),
\]

where (L) and (R) are invertible source-authorized frame maps. Then

\[
\frac{d}{dz}\log\det\widetilde W
=
\frac{d}{dz}\log\det W
+
\operatorname{Tr}(L^{-1}L')
+
\operatorname{Tr}(R^{-1}R').
\]

Presentation coherence therefore requires the primitive current to transform
by the same determinant-line connection terms.

A genuine similarity change

\[
\widetilde W=P^{-1}WP
\]

does not shift the determinant or its logarithmic jet: the two frame terms
cancel. This corrects any overbroad claim that every parameter-dependent basis
change creates a frame anomaly. The anomaly comes from independently changing
the input and output determinant frames, not from ordinary conjugation.

## Relation to the Schur first jet

For a prime-labelled cutoff extension, the local determinant-frame residual is

\[
\mathcal R_{Y/X}
=
j_{Y/X}
-
\operatorname{Tr}
\left(
S_{Y/X}^{-1}S_{Y/X}'
\right)_{z=0}.
\]

The new identification suggests that (j_{Y/X}) must be obtained from the
increment of

\[
\operatorname{Tr}
\left(
W_N^{-1}\mathcal A_N
\right),
\]

together with endpoint and regularization terms. It cannot be assigned from
the diagonal label score alone.

This is the exact bridge between the source-forced logarithmic label shear and
the determinant-line frame law. The shear supplies (Q_+) and (Q_-); the
Fourier–Tate sewing supplies (W_N); their failure to anticommute supplies the
connection anomaly.

## Finite gates

At each cutoff, compute:

1. the typed spaces and domains of (Q_+,Q_-,W_N);
2. the full matrix or relation (mathcal A_N);
3. whether (mathcal A_N) vanishes;
4. whether it is trace class in the sewing frame;
5. the scalar trace of (W_N^{-1}mathcal A_N), when authorized;
6. its increment under one prime-labelled extension;
7. equality with the complete Schur first jet;
8. covariance under one independent source-authorized presentation.

The route fails if the anomaly is zero while a nonzero primitive frame current
is required, if the residual is untyped, if the trace is undefined, or if the
primewise equality fails.

## Decisive interpretation

The only remaining finite candidate for determinant orientation is not bare
translation, label degree, or tail retention. It is the boundary connection
created by the failure of primal-dual Fourier–Tate sewing to anticommute with
the two Mellin generators.

Whether this connection is nonzero, typed, and equal to the primitive Schur
jet is now a direct finite calculation.
