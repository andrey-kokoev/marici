# Normalized right compression gives the exact cutoff-dependent bulk isometry on the regular scaling carrier

## Setting

Let `G` be the abelian unimodular scaling group, represented regularly on

\[
H_G=L^2(G,dg).
\]

Let

\[
\mathcal M=VN(G)
\]

and let `tau` be its Plancherel trace. Its GNS Hilbert space is

\[
L^2(\mathcal M,\tau).
\]

For a finite-volume measurable window `F subset G`, let

\[
P_F=M_{1_F}.
\]

## Exact compression identity

For `a,b in L^2(M,tau)`, the right-compressed operators

\[
aP_F,
\qquad
bP_F
\]

are Hilbert--Schmidt. Their pairing is

\[
\langle aP_F,bP_F\rangle_{HS}
=
\operatorname{Tr}
(P_Fa^*bP_F).
\]

The diagonal density of the translation-invariant operator `a*b` is constant and equal to `tau(a*b)`. Therefore

\[
\boxed{
\operatorname{Tr}
(P_Fa^*bP_F)
=
\operatorname{vol}(F)\tau(a^*b).
}
\]

For convolution kernels this is the direct identity

\[
\int_F
\int_G
\overline{k_a(xy^{-1})}k_b(xy^{-1})dxdy
=
\operatorname{vol}(F)
\langle k_a,k_b\rangle_2.
\]

No asymptotic limit is needed.

## Bulk isometry

Define

\[
\boxed{
J_F:
L^2(\mathcal M,\tau)
\longrightarrow
\mathcal L^2(H_G),
\qquad
J_F(a)
=
\operatorname{vol}(F)^{-1/2}aP_F.
}
\]

Then

\[
\boxed{
J_F^*J_F=I.
}
\]

Thus `J_F` is the exact cutoff-dependent bulk isometry required by the relative-boundary construction.

Its range consists of translation-covariant kernels with input variable restricted to `F`.

## Observer normalization

For `a=U(g)`,

\[
\|J_FU(g)\|_{HS}^2
=
\tau(U(g)^*U(g))
=
\|g\|_2^2.
\]

For `h=g*g*`, this is

\[
\boxed{
\|J_FU(g)\|_{HS}^2
=h(1).
}
\]

Before normalization,

\[
\|U(g)P_F\|_{HS}^2
=
\operatorname{vol}(F)h(1),
\]

which derives the volume counterterm at feature level.

## Two-channel window decomposition

Let

\[
F_{in}
\subset
F_{out}
\]

have finite volume. Define the annulus

\[
F_{ann}=F_{out}\setminus F_{in}.
\]

The projections satisfy

\[
P_{in}P_{ann}=0,
\qquad
P_{in}+P_{ann}=P_{out}.
\]

Define

\[
\boxed{
J_{in,ann}(a)
=
\operatorname{vol}(F_{out})^{-1/2}
\begin{pmatrix}
aP_{in}\\
aP_{ann}
\end{pmatrix}.
}
\]

The direct-sum Hilbert--Schmidt norm gives

\[
\begin{aligned}
\langle
J_{in,ann}(a),
J_{in,ann}(b)
\rangle
&=
\operatorname{vol}(F_{out})^{-1}
\operatorname{Tr}
(P_{out}a^*bP_{out})\\
&=
\tau(a^*b).
\end{aligned}
\]

Hence

\[
\boxed{
J_{in,ann}^*J_{in,ann}=I.
}
\]

This is the exact bulk isometry into the same two-channel space used by the regulated Gram construction.

## Semilocal specialization

For a regular model of the semilocal scaling direction, take

\[
G=C_S
\]

or the regular logarithmic-module quotient after compact/norm-one directions are separated. This does **not** by itself identify the geometric representation on `L^2(X_S)` with one copy of the regular representation. Applying the construction to `X_S` requires its direct-integral spectral decomposition, including multiplicity, and proof that the physical cutoffs correspond to finite-volume right compressions in that decomposition.

Subject to that representation-comparison gate, let

\[
F_{out}=F_R,
\qquad
F_{in}=F_\Lambda,
\]

with

\[
\operatorname{vol}(F_\Lambda)
=2\log\Lambda
\]

under Connes's normalization.

Then

\[
\boxed{
J_{\Lambda,R,S}(a)
=
\operatorname{vol}(F_R)^{-1/2}
\begin{pmatrix}
aP_\Lambda\\
a(P_R-P_\Lambda)
\end{pmatrix}
}
\]

is an isometry from `L2(VN(C_S),tau_S)` into the regulated two-channel Hilbert--Schmidt space.

## Orientation relative to the earlier feature

The earlier regulated feature was written with left Fourier cutoff:

\[
T_{\Lambda,R,S}(g)
=
\begin{pmatrix}
Q_\Lambda P_\Lambda U_S(g)\\
Q_\Lambda(P_R-P_\Lambda)U_S(g)
\end{pmatrix}.
\]

The exact bulk isometry naturally uses **right compression**:

\[
\begin{pmatrix}
U_S(g)P_\Lambda\\
U_S(g)(P_R-P_\Lambda)
\end{pmatrix}.
\]

These are not the same because `U_S(g)` need not commute with the physical cutoff, and left multiplication by `Q_Lambda` changes the Gram density.

Consequently Gate A separates further:

1. the bulk isometry `J_(Lambda,R,S)` now exists exactly;
2. one must compute the projection of the actual Halmos feature `T_(Lambda,R,S)` onto `ran J_(Lambda,R,S)`.

## Explicit adjoint of the bulk isometry

For a two-channel Hilbert--Schmidt vector `(X_in,X_ann)`, the adjoint is characterized by

\[
\langle a,
J_{in,ann}^*(X_{in},X_{ann})
\rangle_{L^2(\mathcal M,\tau)}
=
\operatorname{vol}(F_{out})^{-1/2}
\left[
\operatorname{Tr}
(P_{in}a^*X_{in})
+
\operatorname{Tr}
(P_{ann}a^*X_{ann})
\right].
\]

Equivalently, `J*X` is the Plancherel-L2 projection of

\[
\operatorname{vol}(F_{out})^{-1/2}
\left(
X_{in}P_{in}
+
X_{ann}P_{ann}
\right)
\]

onto the translation-invariant von Neumann algebra.

Thus the bulk projection

\[
\Pi_{\Lambda,R,S}
=J_{\Lambda,R,S}J_{\Lambda,R,S}^*
\]

is explicit: concatenate the two window channels, average their kernel over the center variable to obtain its translation-invariant component, and re-embed that component by normalized right compression.

## Application to the Halmos feature

For

\[
T(g)
=
\begin{pmatrix}
Q_\Lambda P_\Lambda U(g)\\
Q_\Lambda(P_R-P_\Lambda)U(g)
\end{pmatrix},
\]

the positive residual

\[
\boxed{
\mathfrak b_{\Lambda,R,S}(g)
=
(I-\Pi_{\Lambda,R,S})T_{\Lambda,R,S}(g)
}
\]

is now a completely defined finite-cutoff Hilbert--Schmidt vector.

Its Gram kernel is positive without any limiting argument.

## Corrected remaining estimate

The combined-window normalization carries total volume `vol(F_R)`, not Connes's first-row volume `2 log Lambda`. Also, `J^*T` grows like the square root of volume; only

\[
\operatorname{vol}(F_R)^{-1/2}
J_{\Lambda,R,S}^*T_{\Lambda,R,S}(g)
\]

can have a finite density limit.

A subsequent channel audit gives the correct construction: use two copies of the bulk GNS space, normalized separately by the inner and annular volumes. The resulting positive counterterm is

\[
\operatorname{diag}
\left(
2\log\Lambda,
\operatorname{vol}(F_R)-2\log\Lambda
\right)h(1).
\]

See `the-regulated-positive-gram-block-requires-a-two-copy-channelwise-bulk-counterterm-not-one-outer-window-bulk.md`.

## Disposition

The cutoff-dependent bulk isometry is explicit and exact:

\[
\boxed{
J_{\Lambda,R,S}(a)
=
\operatorname{vol}(F_R)^{-1/2}
\begin{pmatrix}
aP_\Lambda\\
a(P_R-P_\Lambda)
\end{pmatrix}.
}
\]

This constructs the basic compression isometry on the regular scaling carrier. The corrected positive Gram construction uses its channelwise two-copy version. For the actual semilocal carrier, one must additionally transport it through the spectral-multiplicity decomposition of `L^2(X_S)`, establish density-nullity of the cutoff commutators, and identify the limiting positive residual boundary feature.
