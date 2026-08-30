# Mellin half-density transport exactly preserves the bilateral trace frame

## Translation representation

On the two Wronskian moment coordinates, bilateral translation by \(L\) acts as

\[
T_L=
\begin{pmatrix}
e^{L/2}&0\\
0&e^{-L/2}
\end{pmatrix}.
\]

This is not unitary in one fixed Euclidean metric. The source-covariant metric transported from the seam fiber is

\[
G_L
=
T_L^{-*}T_L^{-1}
=
\begin{pmatrix}
e^{-L}&0\\
0&e^L
\end{pmatrix}.
\]

It satisfies the exact transport identity

\[
T_{L\to M}^{*}G_M T_{L\to M}=G_L,
\qquad
T_{L\to M}=T_MT_L^{-1}.
\]

Thus Mellin translation is unitary between the object-indexed metric fibers.

## Infinitesimal compatibility

The generator is

\[
A=
\begin{pmatrix}
\frac12&0\\
0&-\frac12
\end{pmatrix}.
\]

The moving metric obeys the Lyapunov equation

\[
\partial_LG_L+A^{*}G_L+G_LA=0.
\]

Hence the connection is flat and metric-compatible. There is no local modular defect in the bilateral trace plane.

## Uniform frame identity

At the seam, the even and odd columns are

\[
F_0
=
m
\begin{pmatrix}
1&\frac12\\
1&-\frac12
\end{pmatrix}.
\]

At scale \(L\),

\[
F_L=T_LF_0.
\]

Therefore

\[
F_L^{*}G_LF_L
=
F_0^{*}F_0
=
|m|^2
\begin{pmatrix}
2&0\\
0&\frac12
\end{pmatrix}.
\]

The two frame eigenvalues are independent of \(L\). The apparent Euclidean angle collapse is exactly a coordinate artifact once the Mellin half-density metric is treated as part of the typed target fiber.

## Qualification at the Adams end

The family \(G_L\) is not uniformly equivalent to one fixed Euclidean metric as \(L\to\infty\). Therefore this theorem authorizes an object-indexed Hilbert bundle, not a single fixed Hilbert completion.

For Adams grades \(k\), the physical displacement is \(k\log p\). Completion along an infinite Adams ray is valid only in one of two forms:

- retain the grade-indexed metric fibers and use the isometric transport maps;
- exhibit a source end object whose topology absorbs the half-density regrading.

Conjugating every fiber back to \(G_0\) is legitimate only when that conjugation is itself the declared Mellin trivialization.

## Consequence

Conditional on the already frozen Mellin half-density law, the reciprocal rank-two trace cell has an exact, scale-independent frame margin. No additional normalization or fitted connection is required.

The next unresolved arrow is no longer trace rank. It is the source incidence map from this bilateral even-odd trace cell into the causal-history auxiliary block, with preservation of the transported metric and prime label.
