# 2289 — The Completed Observer Complex Is Horizontally Compatible with the Elliptic and Marked-Relative Systems

## Type correction

The rank-three observer occurrence space and the rank-three marked wall
quotient must not be identified from matching ranks.

The observer basis is

\[
(12,23,31),
\]

whereas Entry 851's marked quotient basis is induced by

\[
(\Omega_{111},\Omega_{101},\Omega_{110})
\]

and carries one top and two wall-residue directions.  The frozen source
currently supplies no map identifying these differently typed labels.

## Canonical external product

Let \(\mathbb V\) be either the rank-two elliptic Gauss--Manin system or the
rank-twelve marked-relative system, with connection \(\nabla_{\mathbb V}\).
Let \(P\) be the constant three-occurrence bundle.  The direct Gaussian
observer matrix is

\[
Q=
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix},
\qquad
\det Q=-6.
\]

The canonical comparison is the external tensor product

\[
1_{\mathbb V}\otimes Q:
\mathbb V\otimes P
\longrightarrow
\mathbb V\otimes P.
\]

Because \(Q\) is constant in the Gauss--Manin base,

\[
(\nabla_{\mathbb V}\otimes1)(1\otimes Q)
=
(1\otimes Q)(\nabla_{\mathbb V}\otimes1).
\]

Thus the observer map is horizontal without altering either sector's
connection.

## Exact contraction

The adjugate is

\[
\operatorname{adj}(Q)=
\begin{pmatrix}
-2&-2&-2\\
-2&1&1\\
0&3&-3
\end{pmatrix},
\]

with

\[
Q\operatorname{adj}(Q)=-6I_3.
\]

Therefore \(Q^{-1}=\operatorname{adj}(Q)/(-6)\) is a constant horizontal
contracting homotopy.  Consequently

\[
\boxed{
\operatorname{Cone}(1_{\mathbb V}\otimes Q)\simeq0
}
\]

for both coefficient systems.  Numerically,

\[
\det(I_2\otimes Q)=(-6)^2=36,
\]

\[
\det(I_{12}\otimes Q)=(-6)^{12}=2176782336.
\]

## Consequence

The elliptic and marked-relative coefficient objects do not resurrect the
observer kernel closed in Entries 2283 and 2288.  Compatibility is achieved by
the shared external product/six-functor calculus while retaining
sector-specific coefficient objects.

This verifies H2's expected architecture at the observer-complex level:

\[
\boxed{
\text{shared labelled observer Carrier}
+\text{horizontal external product}
+\text{sector-specific Gauss--Manin coefficients}.
}
\]

It does not construct an internal map from contact occurrences to the marked
wall quotient.  Such an identification remains prohibited without a
source-derived labelled localization morphism.

## Verification

`research/benincasa/checkers/observer_gauss_manin_external_product.rs` verifies
the adjugate identity and tensor-product determinants at ranks two and twelve.
