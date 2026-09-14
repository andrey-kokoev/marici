# Every finite observer packet has a canonical convergent two-polarity positive boundary from the centered Gram matrix

## Finite centered matrix

Fix a finite observer packet

\[
E_0
=
\operatorname{span}
\{g_1,
\ldots,g_m\}.
\]

Let

\[
C_\Lambda(g_i,g_j)
\]

be the polarized centered product-cutoff form. The centered scalar regulator theorem gives entrywise convergence

\[
\boxed{
C_\Lambda
\longrightarrow
W
}
\]

where

\[
W_{ij}
=W_S(g_i*g_j^*).
\]

After replacing `C_Lambda` by its Hermitian part if a finite regulator convention is not exactly Hermitian, both `C_Lambda` and `W` are Hermitian matrices.

Finite dimensionality upgrades entrywise convergence to operator-norm convergence:

\[
\boxed{
\|C_\Lambda-W\|_{op}
\longrightarrow0.
}
\]

## Jordan functional calculus

For a Hermitian matrix `A`, define

\[
A_+
=
\frac{|A|+A}{2},
\qquad
A_-
=
\frac{|A|-A}{2}.
\]

Then

\[
\boxed{
A=A_+-A_-,
\qquad
A_\pm\succeq0,
\qquad
A_+A_-=0.
}
\]

Apply this to the centered cutoff matrix:

\[
C_{\Lambda,+}
=
(C_\Lambda)_+,
\qquad
C_{\Lambda,-}
=
(C_\Lambda)_-.
\]

Likewise define `W_+` and `W_-`.

## Continuity

The scalar functions

\[
x
\longmapsto
x_+
=
\max(x,0),
\qquad
x
\longmapsto
x_-
=
\max(-x,0)
\]

are continuous. Continuous functional calculus in finite dimension gives

\[
\boxed{
C_{\Lambda,+}
\to
W_+,
\qquad
C_{\Lambda,-}
\to
W_-
}
\]

in operator norm.

The square-root function is continuous on the positive half-line, so

\[
\boxed{
C_{\Lambda,+}^{1/2}
\to
W_+^{1/2},
\qquad
C_{\Lambda,-}^{1/2}
\to
W_-^{1/2}.
}
\]

No spectral gap at zero is required.

## Positive boundary legs

Equip `E_0` with an auxiliary orthonormal coordinate basis and define

\[
\boxed{
R_{\Lambda,+}
=C_{\Lambda,+}^{1/2},
\qquad
R_{\Lambda,-}
=C_{\Lambda,-}^{1/2}.
}
\]

For an observer coordinate vector `x`, set

\[
\Phi_\Lambda^{boundary}(x)
=
(R_{\Lambda,+}x,
R_{\Lambda,-}x)
\in
E_0\oplus E_0.
\]

This is an ordinary positive Hilbert feature with Gram matrix

\[
\boxed{
G_\Lambda^{boundary}
=
C_{\Lambda,+}
+
C_{\Lambda,-}
=
|C_\Lambda|
\succeq0.
}
\]

Its two legs converge in operator norm:

\[
\Phi_\Lambda^{boundary}
\longrightarrow
\Phi_\infty^{boundary}
=
(W_+^{1/2},
W_-^{1/2}).
\]

## Signed readout

Let

\[
J
=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]

Then

\[
\boxed{
\langle
\Phi_\Lambda^{boundary}(x),
J\Phi_\Lambda^{boundary}(y)
\rangle
=
x^*C_\Lambda y.
}
\]

At the limit,

\[
\boxed{
\langle
\Phi_\infty^{boundary}(x),
J\Phi_\infty^{boundary}(y)
\rangle
=
x^*W y.
}
\]

Thus the completed Weil form is the signed readout of a convergent positive two-polarity feature.

## Positivity criterion

The negative leg vanishes exactly when

\[
W_-=0.
\]

Equivalently,

\[
\boxed{
W\succeq0
\quad\Longleftrightarrow\quad
\Phi_{\infty,-}^{boundary}=0.
}
\]

Therefore this construction does not prove Weil positivity. It represents its failure canonically as nonzero mass in the negative boundary leg.

On a packet family dense in the completed Weil domain, vanishing of every negative leg is the usual all-packet positivity gate.

## Independence of auxiliary coordinates

If the packet coordinates are changed by a unitary `U`, then

\[
C_\Lambda
\mapsto
U^*C_\Lambda U.
\]

Functional calculus gives

\[
(U^*C_\Lambda U)_\pm
=
U^*C_{\Lambda,\pm}U.
\]

Thus the two-polarity boundary is canonical up to unitary equivalence relative to the chosen positive source metric.

For a general nonorthonormal observer basis, first identify `E_0` with its Plancherel Gram Hilbert space. This prevents the Jordan decomposition from depending on arbitrary coordinate scaling.

## Relation to the Tate--Hardy boundary

The centered scalar sewing theorem identifies

\[
W
=
W^{Tate--Hardy}.
\]

Hence the limiting legs may equally be written

\[
\boxed{
((W^{Tate--Hardy})_+^{1/2},
(W^{Tate--Hardy})_-^{1/2}).
}
\]

This provides an abstract positive boundary completion of the signed Hardy connection on each finite packet.

## What is and is not constructed

Constructed:

1. positive cutoff-dependent boundary legs on every fixed packet;
2. norm convergence of those legs;
3. exact signed readout equal to the centered cutoff form;
4. limiting signed readout equal to the Weil/Tate--Hardy form.

Not constructed:

1. an orthogonal bulk projection inside the original semilocal Hilbert space;
2. an identification of `R_(Lambda,+/-)` with physical prolate residual operators;
3. successor compatibility under enlargement of observer packets;
4. a global closed two-polarity feature on the completed source domain.

## Failure of automatic packet compatibility

Let `E_0` be a subspace of `E_1`, and let `i:E_0->E_1` be the inclusion. Although

\[
C_\Lambda^{E_0}
=i^*C_\Lambda^{E_1}i,
\]

one generally has

\[
\boxed{
(C_\Lambda^{E_0})_+
\ne
 i^*(C_\Lambda^{E_1})_+i.
}
\]

Compression does not commute with taking positive parts. Therefore the canonical finite-packet legs do not automatically form an inductive system.

This is the exact obstruction to treating packetwise Jordan decompositions as one global positive filler.

## Minimal global requirement

A compatible global construction would require a self-adjoint operator or closed form `A_W` on a declared positive source Hilbert space such that

\[
W(g,h)
=
\langle g,
A_W h\rangle.
\]

Then spectral calculus could define global legs

\[
A_{W,+}^{1/2},
\qquad
A_{W,-}^{1/2}
\]

on their common form domain. Finite packets would be restrictions of this one global feature rather than independent compressions.

Existence and domain control for this global operator are not supplied merely by scalar convergence.

## `C_34` interpretation

At fixed packet rank, the boundary edge can now be realized as

\[
\boxed{
\text{centered cutoff matrix}
\xrightarrow{\text{Jordan dilation}}
\text{positive two-polarity feature}
\xrightarrow{J}
\text{Tate--Weil signed form}.
}
\]

Every finite packet has this filler, and its boundary legs converge.

The unresolved coherence is in the packet-successor and physical-carrier directions, not in the finite matrix limit.

## Disposition

For every fixed finite observer packet,

\[
\boxed{
C_\Lambda
\to W
\Longrightarrow
(C_{\Lambda,+}^{1/2},
C_{\Lambda,-}^{1/2})
\to
(W_+^{1/2},
W_-^{1/2}).
}
\]

This is a canonical convergent positive two-polarity completion of the centered scalar `C_34` sewing. It does not establish Weil positivity or identify the abstract Jordan legs with the semilocal prolate residual legs.
