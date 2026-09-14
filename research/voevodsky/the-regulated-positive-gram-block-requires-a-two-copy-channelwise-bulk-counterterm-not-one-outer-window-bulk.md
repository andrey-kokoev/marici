# The regulated positive Gram block requires a two-copy channelwise bulk counterterm, not one outer-window bulk

## Audit of the combined-window normalization

The combined two-channel isometry

\[
J_{in,ann}(a)
=
V_R^{-1/2}
\begin{pmatrix}
aP_\Lambda\\
a(P_R-P_\Lambda)
\end{pmatrix}
\]

has total volume

\[
V_R
=
\operatorname{vol}(F_R).
\]

Therefore its unnormalized bulk square is

\[
V_R\tau(a^*a).
\]

This is the divergence of the **complete outer-window positive feature**. It is not Connes's counterterm

\[
V_\Lambdah(1)
=
2\log\Lambdah(1),
\]

which belongs only to the first cutoff row.

Thus one combined bulk projection cannot simultaneously normalize the full Gram block and reproduce the first-row counterterm.

## Regular-model calculation

Let `Q` be a translation-invariant Fourier multiplier and `A` a convolution operator. Ignoring boundary commutators for the moment,

\[
QP_iA
\sim
QA P_i.
\]

For the normalized right-compression isometry `J_i(a)=V_i^(-1/2)aP_i`,

\[
\boxed{
J_i^*(QA P_i)
=
\sqrt{V_i}QA.
}
\]

Hence the finite density statement is

\[
\boxed{
V_i^{-1/2}
J_i^*(QP_iA)
\longrightarrow
QA,
}
\]

provided the commutator

\[
[P_i,A]
\]

is negligible in Hilbert--Schmidt norm per unit volume.

If `Q_Lambda -> I` in the relevant Plancherel `L2` sense, the final density limit is `A`.

The unnormalized expression `J_i* T_i` grows like `sqrt(V_i)` and cannot converge to a fixed multiple of `A`. This corrects the earlier unnormalized limit target.

## Two channel volumes

Set

\[
V_{in}
=
\operatorname{vol}(F_\Lambda)
=
2\log\Lambda,
\]

and

\[
V_{ann}
=
\operatorname{vol}(F_R\setminus F_\Lambda)
=
V_R-V_\Lambda.
\]

Each channel has its own exact compression identity:

\[
\|aP_\Lambda\|_{HS}^2
=
V_{in}\tau(a^*a),
\]

\[
\|a(P_R-P_\Lambda)\|_{HS}^2
=
V_{ann}\tau(a^*a).
\]

## Two-copy bulk space

Use

\[
\boxed{
\mathcal H_{bulk}^{(2)}
=
L^2(\mathcal M,\tau)
\oplus
L^2(\mathcal M,\tau).
}
\]

Define the channelwise isometry

\[
\boxed{
J_{\Lambda,R}^{(2)}(a_{in},a_{ann})
=
\begin{pmatrix}
V_{in}^{-1/2}a_{in}P_\Lambda\\
V_{ann}^{-1/2}a_{ann}(P_R-P_\Lambda)
\end{pmatrix}.
}
\]

Orthogonality of the physical windows gives

\[
\boxed{
(J_{\Lambda,R}^{(2)})^*
J_{\Lambda,R}^{(2)}
=I_{\mathcal H_{bulk}^{(2)}}.
}
\]

The observer bulk enters diagonally as

\[
\Delta A
=(A,A).
\]

Before normalization, its channelwise bulk feature is

\[
\boxed{
\begin{pmatrix}
\sqrt{V_{in}}J_{in}A\\
\sqrt{V_{ann}}J_{ann}A
\end{pmatrix}.
}
\]

## Positive matrix-valued counterterm

The Gram kernel of the channelwise bulk feature is

\[
\boxed{
\mathcal C_{\Lambda,R}(g_1,g_2)
=
\begin{pmatrix}
V_{in}&0\\
0&V_{ann}
\end{pmatrix}
\tau
\left(
U(g_2)^*U(g_1)
\right).
}
\]

This matrix is positive. Its first diagonal entry is exactly

\[
2\log\Lambdah(1).
\]

Its second diagonal entry records the additional annular divergence of the positive completion. The off-diagonal bulk entries vanish because the two input windows are orthogonal.

This is the common positive counterterm matrix that entrywise scalar subtraction lacked.

## Channelwise orthogonal residual

Let

\[
\Pi_{\Lambda,R}^{(2)}
=
J_{\Lambda,R}^{(2)}
(J_{\Lambda,R}^{(2)})^*.
\]

For the actual regulated Halmos feature

\[
T_{\Lambda,R}(g)
=
\begin{pmatrix}
Q_\Lambda P_\Lambda A\\
Q_\Lambda(P_R-P_\Lambda)A
\end{pmatrix},
\]

define

\[
\boxed{
\mathfrak b_{\Lambda,R}(g)
=
(I-\Pi_{\Lambda,R}^{(2)})
T_{\Lambda,R}(g).
}
\]

This residual has a positive Gram matrix at every finite cutoff. The two-copy projection removes the bulk of each channel without conflating the `Lambda` and `R` divergences.

## Boundary commutator

The actual feature uses `QP_iA`, whereas the exact bulk model uses `QA P_i`. Their difference is

\[
QP_iA-QA P_i
=
Q[P_i,A].
\]

Thus the first remaining Gate-A estimate is explicit:

\[
\boxed{
\frac1{V_i}
\|Q_\Lambda[P_i,A]\|_{HS}^2
\longrightarrow0.
}
\]

For compactly supported convolution kernels on the logarithmic line, the commutator is supported near the two window boundaries, so its squared Hilbert--Schmidt norm is `O(1)` while `V_i -> infinity`. This proves density-nullity in the elementary model.

The semilocal version requires uniform control over the norm-one and `S`-unit directions.

## Fourier-cutoff density

After boundary commutators are removed in density, the projected bulk symbol is `Q_Lambda A`. To recover `A`, one needs

\[
\boxed{
\|(I-Q_\Lambda)A\|_{L^2(\mathcal M,\tau)}
\longrightarrow0.
}
\]

This is strong convergence of the Fourier cutoffs on the Plancherel GNS vector of the observer. It follows in the regular model from monotone exhaustion when the cutoff projections increase strongly to `I`.

The physical and Fourier cutoffs in Connes's theorem scale together, so the actual semilocal estimate must retain that dependence.

## Corrected Gate A

Bulk Gate A now consists of:

1. exact channelwise isometries `J_in` and `J_ann`;
2. density-nullity of `Q[P_i,A]`;
3. Plancherel convergence `(I-Q_Lambda)A -> 0`;
4. transport through the multiplicity decomposition of `L2(X_S)`.

The first item is proved on the regular carrier. Items two and three hold in the elementary translation model. Their semilocal forms and item four remain to be established.

## Refinement consequence

The positive refinement needs two bulk legs, not one. This does not necessarily add another sequential node, but it changes the bulk stage from a single object to a two-channel matrix object carrying the positive counterterm

\[
\operatorname{diag}(V_{in},V_{ann})h(1).
\]

The first-row signed trace forgets the annular diagonal. The positive completion must retain it until the boundary quotient is taken.

## Disposition

The correct bulk removal for the regulated positive Gram block is

\[
\boxed{
\mathcal H_{bulk}^{(2)}
=
L^2(VN(C_S),\tau_S)^{\oplus2},
}
\]

with channelwise cutoff embeddings and counterterm matrix

\[
\boxed{
\mathcal C_{\Lambda,R,S}
=
\begin{pmatrix}
2\log\Lambda&0\\
0&
\operatorname{vol}(F_R)-2\log\Lambda
\end{pmatrix}
h(1).
}
\]

This exactly matches Connes's first-row volume term while retaining the additional positive-completion divergence as a separately typed annular bulk coordinate.
