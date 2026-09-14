# A positive relative boundary exists exactly after orthogonal bulk-feature removal, not entrywise finite-part subtraction

## Entrywise subtraction is not positive

Suppose a regulated Gram matrix has an expansion

\[
G_M
=
2MG_{bulk}
+
G_{fin}
+
o(1),
\qquad
G_M\succeq0,
\qquad
G_{bulk}\succeq0.
\]

It does not follow that `G_fin` is positive. For example,

\[
G_M
=
M I
+
\begin{pmatrix}-1&0\\0&1\end{pmatrix}
\]

is positive for `M>=1`, while its finite part is indefinite.

Therefore neither Connes's scalar finite part nor entrywise subtraction from the regulated Halmos Gram block defines a positive boundary feature.

## Bulk GNS space

Let `E_S` be the observer source and let

\[
\Xi_S:E_S\to\mathcal H_{bulk,S}
\]

be the Folner trace-density feature satisfying

\[
\langle
\Xi_S(g_1),
\Xi_S(g_2)
\rangle_{bulk}
=
\tau_S
\left(
U_S(g_2)^*U_S(g_1)
\right).
\]

In particular,

\[
\|\Xi_S(g)\|^2
=
h(1)
\]

for `h=g*g*`.

## Regulated positive feature

For a cutoff packet `alpha=(Lambda,R)`, let

\[
T_{\alpha,S}:E_S\to\mathcal H_{\alpha,S}
\]

be the complete regulated feature. A model choice is the two-channel column

\[
T_{\Lambda,R,S}(g)
=
\begin{pmatrix}
Q_\Lambda P_\Lambda U_S(g)\\
Q_\Lambda(P_R-P_\Lambda)U_S(g)
\end{pmatrix}
\]

in the direct sum of the corresponding Hilbert--Schmidt spaces.

Its Gram kernel

\[
G_\alpha(g_1,g_2)
=
\langle
T_\alpha(g_1),
T_\alpha(g_2)
\rangle
\]

is positive by construction.

## Cutoff-dependent bulk embedding

The translation model supplies a canonical isometry from the bulk density space into each normalized cutoff space. Abstractly, seek isometries

\[
\boxed{
J_{\alpha,S}:
\mathcal H_{bulk,S}
\longrightarrow
\mathcal H_{\alpha,S}
}
\]

and a positive volume scalar `V_alpha` such that the leading regulated feature is

\[
\sqrt{V_\alpha}J_\alpha\Xi_S(g).
\]

In the elementary interval model,

\[
V_M=2M
\]

and

\[
(J_Mk)(x,y)
=(2M)^{-1/2}
1_{[-M,M]}(y)k(x-y).
\]

Direct calculation gives

\[
J_M^*J_M=I.
\]

The absence of a strong limit for `J_Mk` is harmless: `J_M` is supposed to depend on the cutoff.

## Orthogonal residual feature

Let

\[
\Pi_\alpha
=J_\alpha J_\alpha^*
\]

be the orthogonal projection onto the embedded bulk feature. Define

\[
\boxed{
\mathfrak b_{\alpha,S}(g)
=
(I-\Pi_{\alpha,S})
T_{\alpha,S}(g).
}
\]

Then

\[
T_\alpha(g)
=
\Pi_\alpha T_\alpha(g)
+
\mathfrak b_\alpha(g)
\]

is an orthogonal decomposition. Consequently

\[
\boxed{
\langle
T_\alpha(g_1),
T_\alpha(g_2)
\rangle
=
\langle
\Pi_\alpha T_\alpha(g_1),
\Pi_\alpha T_\alpha(g_2)
\rangle
+
\langle
\mathfrak b_\alpha(g_1),
\mathfrak b_\alpha(g_2)
\rangle.
}
\]

The residual Gram kernel

\[
\boxed{
B_\alpha(g_1,g_2)
=
\langle
\mathfrak b_\alpha(g_1),
\mathfrak b_\alpha(g_2)
\rangle
\succeq0
}
\]

is positive at every cutoff.

## Exact matching condition for the counterterm

To recover the expected volume term, one needs

\[
\boxed{
\Pi_\alpha T_\alpha(g)
=
\sqrt{V_\alpha}J_\alpha\Xi_S(g)
+
o_{\mathcal H_\alpha}(1)
}
\]

uniformly on bounded observer packets, or an explicitly controlled weaker version sufficient for Gram convergence.

Then

\[
\langle
\Pi_\alpha T_\alpha(g_1),
\Pi_\alpha T_\alpha(g_2)
\rangle
=
V_\alpha
\langle
\Xi_S(g_1),
\Xi_S(g_2)
\rangle_{bulk}
+
o(1).
\]

For `g_1=g_2=g`, this is

\[
V_\alphah(1)+o(1).
\]

This is a feature-level derivation of the counterterm rather than numerical subtraction after trace.

## Boundary convergence criterion

A positive limiting boundary form exists if the residual features converge in a common target or form a Cauchy net after admitted transition isometries:

\[
\boxed{
\mathfrak b_{\alpha,S}(g)
\longrightarrow
\mathfrak b_S(g)
\in
\mathcal H_{bdry,S}.
}
\]

Then

\[
B_S(g_1,g_2)
=
\langle
\mathfrak b_S(g_1),
\mathfrak b_S(g_2)
\rangle
\]

is automatically positive, and

\[
B_S(g,g)
=
\|\mathfrak b_S(g)\|^2
\ge0.
\]

This is the precise positive replacement for taking the entrywise finite part of `G_alpha`.

## Necessary kernel condition

The assignment of a bulk component from the regulated feature is well-defined only if

\[
\ker T_\alpha
\subseteq
\ker\Xi_S.
\]

Equivalently, by Douglas factorization, the bulk Gram kernel must be dominated at each cutoff scale:

\[
V_\alpha
\Xi_S^*\Xi_S
\preceq
c_\alphaT_\alpha^*T_\alpha
\]

for some finite `c_alpha`, with the sharp asymptotic normalization needed to obtain an isometric bulk embedding.

Unlike the failed inside-to-outside contraction, this condition compares the complete regulated feature with its translation-density quotient.

## Relation to the Eisenstein range

If the closure of `ran E_S` is the radical/bulk module, the required isometry must identify

\[
\mathcal H_{bulk,S}
\cong
\overline{
\operatorname{ran}E_S
}^{\tau_S}
\]

and realize `J_(alpha,S)` as its cutoff embedding.

The statement "quotient by `ran E_S`" is therefore shorthand for the orthogonal residual construction

\[
(I-J_\alpha J_\alpha^*)T_\alpha,
\]

not an algebraic quotient followed by an arbitrary choice of representative.

## Compatibility with the Halmos block

The complete two-channel feature retains both rows of the positive Halmos colligation. Since `Pi_alpha` is an orthogonal projection in the complete feature space, the residual two-by-two Gram matrix remains positive.

The first-row Connes functional is a nonpositive readout of this matrix. To identify its finite part with the residual norm, one still needs the boundary sewing identity

\[
\boxed{
W_{completed,S}(g*g^*)
=
\|\mathfrak b_S(g)\|^2.
}
\]

That identity is not implied by bulk removal alone.

## Two independent gates

The positive problem now separates cleanly:

### Gate A: bulk embedding

Construct `J_(alpha,S)` and prove the counterterm matching

\[
\Pi_\alpha T_\alpha
\sim
\sqrt{V_\alpha}J_\alpha\Xi_S.
\]

### Gate B: boundary identification

Prove residual convergence and identify its Gram form with the completed Weil form, including endpoint--gamma and Sonin contributions.

Gate A is a trace-density/Folner theorem. Gate B is the arithmetic prolate/Sonin theorem.

## Refinement consequence

The positive semantic stages are now more accurately:

1. regulated two-channel feature;
2. bulk GNS feature;
3. cutoff-dependent bulk isometry;
4. orthogonal bulk projection;
5. residual boundary feature;
6. residual limit;
7. Weil boundary identification.

These cannot all be represented by one scalar renormalization node.

## Disposition

A positive relative boundary is obtained only through

\[
\boxed{
\mathfrak b_{\alpha,S}
=
(I-J_{\alpha,S}J_{\alpha,S}^*)
T_{\alpha,S}.
}
\]

Its Gram form is positive at every cutoff. The exact remaining tasks are construction of the semilocal bulk isometries and identification of the limiting residual norm with the completed Weil form.
