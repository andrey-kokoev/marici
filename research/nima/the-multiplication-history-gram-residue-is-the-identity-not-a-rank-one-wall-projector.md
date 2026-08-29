# The multiplication-history Gram residue is the identity, not a rank-one wall projector

## Operator assembled from local histories

Let

\[
L_p=\log p
\]

and define the local history operator on \(L^2(\mathbb R_q)\) by

\[
(\mathcal H_p\psi)(t,q)=W_t(q)\psi(q),
\qquad
t\in[L_p,2L_p].
\]

Use the graph norm

\[
\|\mathcal H_p\psi\|^2
=
\int_{L_p}^{2L_p}
\left(
\|W_t\psi\|^2
+
\|\partial_tW_t\psi\|^2
\right)\,dt.
\]

The off-seam primitive Gram is

\[
G_\sigma
=
\sum_p p^{-1-2\sigma}\mathcal H_p^*\mathcal H_p.
\]

## Large-prime local residue

Take first \(\psi\) with compact \(q\)-support. For fixed \(q\) and \(t\in[L_p,2L_p]\), as \(p\to\infty\),

\[
W_t(q)\longrightarrow-1.
\]

Consequently,

\[
\frac1{L_p}
\int_{L_p}^{2L_p}|W_t(q)|^2\,dt
\longrightarrow1.
\]

The derivative term is concentrated near the moving fronts \(q=\pm t\). For fixed compact \(q\)-support,

\[
\frac1{L_p}
\int_{L_p}^{2L_p}
|\partial_tW_t(q)|^2\,dt
\longrightarrow0.
\]

Dominated convergence therefore gives

\[
\frac1{L_p}\mathcal H_p^*\mathcal H_p
\longrightarrow I
\]

strongly on the compactly supported core.

Thus the local leading Gram direction is the identity on the analytic input space.

## Abelian prime residue

Rewrite

\[
2\sigma G_\sigma
=
2\sigma
\sum_p
\frac{L_p}{p^{1+2\sigma}}
\left(
\frac{\mathcal H_p^*\mathcal H_p}{L_p}
\right).
\]

The scalar weights satisfy

\[
2\sigma
\sum_p\frac{L_p}{p^{1+2\sigma}}
\longrightarrow1.
\]

Combining this Abelian limit with the strong local limit yields, on the declared core,

\[
2\sigma G_\sigma
\longrightarrow I.
\]

The precise extension from the core to a chosen operator topology still requires a uniform domination argument, but the candidate residue is fixed:

\[
R_{\mathrm{seam}}=I.
\]

## Conflict with a rank-one wall claim

On \(L^2(\mathbb R_q)\), the identity has infinite rank. Therefore

\[
R_{\mathrm{seam}}=cP_{\mathrm{wall}}
\]

cannot hold if \(P_{\mathrm{wall}}\) is a rank-one projector inside the same analytic Hilbert space.

The issue is not a rotating residue. It is a carrier mismatch.

The constant window \(-1\) acts by multiplication as \(-I\). Its Gram is \(I\). A rank-one wall appears only when the window itself is represented as one feature vector in a separate five-cell coefficient space.

Hence two representations must not be conflated:

1. **multiplication history**
   \[
   \psi\mapsto W_t\psi,
   \]
   whose wall specialization is \(-I\);

2. **window-feature history**
   \[
   1\mapsto W_t,
   \]
   whose boundary specialization is the one-dimensional constant carrier.

## Correct wall typing

Let \(\mathcal F_{\mathrm{cell}}\) be the source feature space containing the constant basis vector \(e_{\mathrm{wall}}\). Let

\[
\operatorname{Mult}:
\mathcal F_{\mathrm{cell}}
\to
\mathcal B(L^2_q)
\]

be the representation sending

\[
e_{\mathrm{wall}}\mapsto-I.
\]

Then a rank-one coefficient-space residue

\[
P_{\mathrm{wall}}
=
|e_{\mathrm{wall}}\rangle
\langle e_{\mathrm{wall}}|
\]

is represented on analytic states by an identity-type multiplication Gram.

The desired theorem must therefore be stated before applying \(\operatorname{Mult}\):

\[
R_{\mathrm{seam}}^{\mathrm{cell}}
=
cP_{\mathrm{wall}},
\]

followed by

\[
\operatorname{Mult}
\left(
R_{\mathrm{seam}}^{\mathrm{cell}}
\right)
=
I
\]

in the appropriate quadratic representation.

## Consequence for the history definition

Kitaev's map

\[
\mathcal H_p\psi:t\mapsto W_t\psi
\]

is valid for local trace and Stokes analysis, but it has already represented the wall line on every analytic input vector. It cannot by itself prove that the residue had rank one before representation.

To identify the wall canonically, retain a coefficient-valued history

\[
\mathfrak h_p:t\mapsto[W_t]\in\mathcal F_{\mathrm{cell}}
\]

and only then form its Gram and apply the analytic representation.

## Regular-part subtraction

Subtracting

\[
\frac1{2\sigma}P_{\mathrm{wall}}
\]

inside \(L^2_q\) is ill-typed if \(P_{\mathrm{wall}}\) means a rank-one analytic projector. The leading analytic residue there is \(I\).

A source-authorized subtraction must occur in the cell coefficient space and then be transported through the declared representation.

## Hostiles resolved

### Stable high-rank analytic residue

This is not automatically a failure. It is the image of one wall coordinate under a non-rank-preserving multiplication representation.

### False rank-one subtraction

A rank-one projector is subtracted directly from the analytic Gram despite the residue being \(I\). Scalar traces may improve while most singular directions remain.

### Image completion without coefficient provenance

Only multiplication operators are retained. The limit \(I\) exists, but there is no way to prove which source wall coordinate produced it.

## Next theorem

The residue programme now splits cleanly:

1. construct the coefficient-valued five-cell history;
2. prove its rescaled Gram converges to the rank-one constant-wall projector;
3. prove the multiplication representation sends that coefficient residue to the analytic identity residue;
4. define any regular part in coefficient space;
5. transport the regularized relative Green form to analytic states.

This is the exact graph-completion-versus-image-completion distinction at the operator-valued residue level.
