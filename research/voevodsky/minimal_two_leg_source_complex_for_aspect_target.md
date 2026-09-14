# Minimal two-leg source complex for the Aspect target

## Question

What is the smallest chain complex that retains the logarithmic and blow-up face legs separately while deriving their residue cancellation internally?

## Claim boundary

This constructs the unique minimal free algebraic shape compatible with the two target columns and their opposite residues. Its generators remain formal; no geometric relative pair or homology--de Rham pairing is asserted.

## Source complex

Let

\[
A_1=\mathbb Z e_{\log}\oplus\mathbb Z e_{\rm face},
\qquad
A_0=\mathbb Z r,
\]

with differential

\[
d_A=
\begin{pmatrix}1&-1\end{pmatrix}.
\]

Thus

\[
d_Ae_{\log}=r,
\qquad
d_Ae_{\rm face}=-r,
\]

and the primitive cycle is

\[
e_{\log}+e_{\rm face}.
\]

## Target map

Let the degree-one map send

\[
e_{\log}\mapsto(1,0)^T,
\qquad
e_{\rm face}\mapsto(0,1)^T.
\]

Let the degree-zero map send

\[
r\mapsto(1,-1,1)^T.
\]

Then

\[
D_{\rm res}F_1
=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}
=F_0d_A.
\]

The source cycle maps to

\[
F_1(e_{\log}+e_{\rm face})=(1,1)^T.
\]

## Homology

The source has

\[
H_1(A)\cong\mathbb Z,
\qquad H_0(A)=0.
\]

The map is an isomorphism from \(H_1(A)\) onto the target's closed relative line. Its mapping cone again has

\[
H_2=H_1=0,
\qquad H_0\cong\mathbb Z^2.
\]

## Minimality

Keeping two legs distinct requires at least two degree-one generators. Since each has nonzero boundary and the boundaries are opposite, at least one degree-zero generator is required. Primitivity forces the boundary row to be equivalent over \(\mathbb Z\) to \((1,-1)\). Therefore this is the minimal free two-leg chain shape up to integral basis change and sign.

## Geometric acceptance test

A source realization must now supply a relative pair with two labelled chains whose boundaries are the same oriented boundary class with opposite signs. A cycle-form integration map must send that boundary class to \((1,-1,1)^T\), the chains to the two target legs, and their sum to \((1,1)^T\).

## Computed result

Every chain square vanishes, the source cycle maps to \((1,1)^T\), and the source has integral homology \(H_1\cong\mathbb Z\), \(H_0=0\). The cone has \(H_2=H_1=0\), \(H_0\cong\mathbb Z^2\). Determinantal divisors are units, so no torsion or hidden denominator occurs. Neither individual leg is a source cycle.

## Disposition

The minimal free two-leg source shape is fixed up to integral basis change and sign:

\[
\mathbb Z^2\xrightarrow{(1,-1)}\mathbb Z.
\]

Its geometric realization remains absent. The next object is now concrete: a relative pair with two labelled chains sharing one oriented boundary class with opposite signs, together with its cycle-form integration map.
