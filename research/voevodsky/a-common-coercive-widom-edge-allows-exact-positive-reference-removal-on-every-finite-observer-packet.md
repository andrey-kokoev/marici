# A common coercive Widom edge allows exact positive reference removal on every finite observer packet

## Tate and reference Gram matrices

Fix a finite observer packet `E_0`. Let

\[
G_\Lambda^T
\]

be the positive residual Gram matrix for the Tate-scattered cutoff pair after volume-bulk removal, and let

\[
G_\Lambda^0
\]

be the corresponding positive Gram matrix for the pure-translation/reference cutoff pair.

Both matrices are positive semidefinite.

Define their signed relative difference

\[
\boxed{
D_\Lambda
=G_\Lambda^T-G_\Lambda^0.
}
\]

The centered signed regulator theorem targets

\[
\boxed{
D_\Lambda
\longrightarrow
W
}
\]

on the packet, where `W` is the finite Weil/Tate Gram matrix.

## Common Widom edge hypothesis

Assume both positive matrices have the same leading edge form:

\[
\boxed{
\frac1{L_\Lambda}
G_\Lambda^T
\longrightarrow
G_{edge},
\qquad
\frac1{L_\Lambda}
G_\Lambda^0
\longrightarrow
G_{edge},
}
\]

where

\[
L_\Lambda
\to\infty
\]

is the Widom edge scale, schematically `L_Lambda=log c_Lambda`.

After quotienting the edge-null source directions, assume

\[
\boxed{
G_{edge}>0
}
\]

on `E_0`.

This is the finite-packet coercivity needed to identify a common positive edge bulk.

## Jordan parts of the relative matrix

Define

\[
(D_\Lambda)_+
=
\frac{|D_\Lambda|+D_\Lambda}{2},
\qquad
(D_\Lambda)_-
=
\frac{|D_\Lambda|-D_\Lambda}{2}.
\]

Then

\[
D_\Lambda
=(D_\Lambda)_+
-
(D_\Lambda)_-,
\]

with both parts positive semidefinite.

## Exact common Gram candidate

Set

\[
\boxed{
C_\Lambda
=G_\Lambda^T
-(D_\Lambda)_+.
}
\]

Since

\[
G_\Lambda^T-G_\Lambda^0
=(D_\Lambda)_+-(D_\Lambda)_-,
\]

one also has the exact identity

\[
\boxed{
C_\Lambda
=G_\Lambda^0
-(D_\Lambda)_-.
}
\]

Therefore

\[
\boxed{
G_\Lambda^T
=C_\Lambda+(D_\Lambda)_+,
}
\]

\[
\boxed{
G_\Lambda^0
=C_\Lambda+(D_\Lambda)_-.
}
\]

The only remaining question is positivity of `C_Lambda`.

## Eventual positivity

Because `D_Lambda->W`, the matrices `D_Lambda` and `(D_Lambda)_+` are uniformly bounded on the fixed packet.

Let

\[
\alpha
=
\lambda_{min}(G_{edge})
>0.
\]

Common normalized edge convergence gives, for sufficiently large cutoff,

\[
G_\Lambda^T
\succeq
\frac\alpha2
L_\LambdaI.
\]

Choose `M` with

\[
(D_\Lambda)_+
\preceq
MI
\]

for all sufficiently large `Lambda`. Then

\[
C_\Lambda
\succeq
\left(
\frac\alpha2
L_\Lambda-M
\right)I.
\]

Hence

\[
\boxed{
C_\Lambda\succeq0
}
\]

for all sufficiently large cutoffs.

Thus `C_Lambda` is an honest common positive Gram matrix, not an entrywise counterterm.

## Positive feature realization

Let

\[
E_\Lambda
=C_\Lambda^{1/2},
\]

\[
R_{\Lambda,+}
=(D_\Lambda)_+^{1/2},
\qquad
R_{\Lambda,-}
=(D_\Lambda)_-^{1/2}.
\]

Then the Tate and reference positive features admit realizations

\[
\boxed{
\Phi_\Lambda^T(x)
=(E_\Lambda x,
R_{\Lambda,+}x),
}
\]

\[
\boxed{
\Phi_\Lambda^0(x)
=(E_\Lambda x,
R_{\Lambda,-}x).
}
\]

Their ordinary Gram matrices are exactly

\[
(\Phi_\Lambda^T)^*
\Phi_\Lambda^T
=G_\Lambda^T,
\]

\[
(\Phi_\Lambda^0)^*
\Phi_\Lambda^0
=G_\Lambda^0.
\]

The leading edge feature `E_Lambda` is literally shared.

## Orthogonal common-edge removal

Remove the common first slot. The remaining two-polarity boundary is

\[
\boxed{
\Phi_\Lambda^{finite}(x)
=(R_{\Lambda,+}x,
R_{\Lambda,-}x).
}
\]

Its positive Gram matrix is

\[
\boxed{
|D_\Lambda|
=(D_\Lambda)_+
+(D_\Lambda)_-.
}
\]

With fundamental symmetry

\[
J
=
\operatorname{diag}(I,-I),
\]

its signed readout is

\[
\boxed{
(\Phi_\Lambda^{finite})^*
J
\Phi_\Lambda^{finite}
=D_\Lambda.
}
\]

Thus common-edge removal is positive and exact.

## Convergence of finite legs

Since

\[
D_\Lambda
\to W
\]

in finite-dimensional operator norm, continuous functional calculus gives

\[
(D_\Lambda)_\pm^{1/2}
\longrightarrow
W_\pm^{1/2}.
\]

Therefore

\[
\boxed{
\Phi_\Lambda^{finite}
\longrightarrow
(W_+^{1/2},
W_-^{1/2})
}
\]

in operator norm on the packet.

This is the canonical finite-packet Tate boundary constructed previously, now obtained by exact removal of a common positive Widom edge Gram.

## Relation to physical feature spaces

The construction above is source-Gram exact. To realize it inside the original physical Tate and reference residual carriers, use polar decomposition.

If

\[
X_\Lambda^T:
E_0
\to
\mathcal H_\Lambda^T
\]

has Gram `G_Lambda^T`, then it differs from the canonical feature `(E_Lambda,R_(Lambda,+))` by a partial isometry on the observer-generated range. The same holds for the reference feature.

Thus packetwise physical embeddings exist up to unitary freedom. What is not automatic is that the shared canonical `E_Lambda` corresponds to one pre-existing common closed subspace of both physical carriers without applying these observer-dependent polar transports.

## Why subtraction of square roots was wrong

Directly comparing

\[
(G_\Lambda^T)^{1/2}
-
(G_\Lambda^0)^{1/2}
\]

cancels a common term of size `sqrt(L_Lambda)` and typically tends to zero when `D_Lambda=O(1)`. It does not retain the finite signed difference.

The correct positive lift decomposes the **difference matrix** into its Jordan parts while retaining a shared positive Gram `C_Lambda`.

## Edge-null directions

If `G_edge` has a kernel, eventual positivity of `C_Lambda` is not automatic there. Decompose

\[
E_0
=
\operatorname{supp}G_{edge}
\oplus
\ker G_{edge}.
\]

On the support, the coercive argument applies. On the kernel, one must inspect the finite matrices directly. A bounded negative direction of `C_Lambda` in the edge kernel obstructs common positive removal.

Therefore the exact finite-packet acceptance test is

\[
\boxed{
C_\Lambda
=G_\Lambda^T-(D_\Lambda)_+
\succeq0.
}
\]

Common leading asymptotics prove it only on coercive edge support.

## Packet compatibility

The operation

\[
D_\Lambda
\mapsto
(D_\Lambda)_\pm
\]

again does not commute with compression to smaller packets. Therefore independently constructed `C_Lambda` need not be successor-compatible.

A global coherent version requires one closed relative operator `D_Lambda` on a common source Hilbert space and global spectral calculus before packet restriction. Finite-packet positivity alone does not construct that operator.

## Global target

A global reference-edge theorem should provide closed positive forms

\[
g_\Lambda^T,
\bindnasrepma
g_\Lambda^0
\]

on one graph domain, with form difference represented by a self-adjoint operator `D_Lambda`, such that:

\[
D_\Lambda
\to
A_S
\]

in strong resolvent/form sense, and

\[
g_\Lambda^T
-(D_\Lambda)_+
=
g_\Lambda^0
-(D_\Lambda)_-
\succeq0.
\]

Then global spectral calculus yields coherent common-edge and finite residual features.

## Revised positive sewing theorem

On every fixed packet, the following inputs suffice:

1. `G_Lambda^T>=0` and `G_Lambda^0>=0`;
2. common coercive normalized Widom limit;
3. bounded signed difference `D_Lambda->W`.

They imply:

\[
\boxed{
\begin{aligned}
G_\Lambda^T
&=C_\Lambda+(D_\Lambda)_+,\\
G_\Lambda^0
&=C_\Lambda+(D_\Lambda)_-,\\
C_\Lambda&\succeq0,\\
(D_\Lambda)_\pm^{1/2}
&\to W_\pm^{1/2}.
\end{aligned}
}
\]

This is a genuine positive lift of relative trace subtraction.

## Disposition

A common coercive `log c` edge law and finite signed regulator convergence produce an exact positive common-edge decomposition:

\[
\boxed{
G_\Lambda^T
=C_\Lambda+(D_\Lambda)_+,
\qquad
G_\Lambda^0
=C_\Lambda+(D_\Lambda)_-,
\qquad
C_\Lambda\succeq0.
}
\]

After orthogonally deleting the shared `C_Lambda` feature, the residual legs converge to the canonical two-polarity Tate boundary. The remaining analytic input is the observer-weighted common Widom law and, for global coherence, a common closed-form realization before packet restriction.
