# The unconditional Szego-difference factorization builds the two-by-two tower but its remainder is the full reflected multiplier

## Ambient positive kernel

Let `D` be the half-plane or disk obtained from the critical strip by a fixed conformal map. Write `k_D(z,w)` for its Szego kernel. It is positive:

\[
k_D\succeq0.
\]

For any analytic scalar function `Phi` on `D`, the congruence kernel

\[
(\Phi k_D\Phi^*)(z,w)
=
\Phi(z)
k_D(z,w)
\overline{\Phi(w)}
\]

is also positive wherever multiplication by `Phi` is densely defined.

## Exact unconditional difference

For the reflected completed multiplier

\[
\Theta_S=
\frac{E_S^\#}{E_S},
\]

the canonical model-space kernel is

\[
K_S(z,w)
=
k_D(z,w)
-
\Theta_S(z)k_D(z,w)
\overline{\Theta_S(w)}.
\]

Thus, without assuming Schur contractivity,

\[
\boxed{
K_S=G-R_S^*R_S
}
\]

in Kolmogorov form, where

\[
G(z,w)=k_D(z,w)

\]

and `R_S` is the feature map associated with the positive kernel

\[
R_S^*R_S
=

\Theta_Sk_D\Theta_S^*.
\]

At the Hardy-space operator level this is

\[
\boxed{
K_S
\longleftrightarrow
I-M_{\Theta_S}M_{\Theta_S}^*.
}
\]

No RH, innerness, or contractivity assumption enters this identity.

## Two-by-two supersymmetric carrier

Define the block operator

\[
\mathbb Q_S=
\begin{pmatrix}
0&M_{\Theta_S}\\
M_{\Theta_S}^*&0
\end{pmatrix}.
\]

Then

\[
\mathbb Q_S^2
=
\begin{pmatrix}
M_{\Theta_S}M_{\Theta_S}^*&0\\
0&M_{\Theta_S}^*M_{\Theta_S}
\end{pmatrix}
\succeq0.
\]

The signed observation

\[
I-M_{\Theta_S}M_{\Theta_S}^*
\]

is recovered from the first diagonal block together with the ambient identity. This is an unconditional positive supersymmetric bulk with a signed observation boundary.

It is the reproducing-kernel counterpart of the Suzuki Toeplitz complex.

## Exact prime transition identity

If prime `q` is adjoined, then

\[
\Theta_{S\cup\{q\}}
=
\Theta_S\varphi_q,
\qquad
\varphi_q=
\frac{m_q^\#}{m_q}.
\]

The kernel identity

\[
1-ab\bar a\bar b
=
(1-a\bar a)
+
a\bar a(1-b\bar b)
\]

gives

\[
\boxed{
K_{S\cup\{q\}}
=
K_S

+
\Theta_S(z)
\overline{\Theta_S(w)}
K_{\varphi_q}(z,w).
}
\]

This is the exact nonlocal tower transition. It retains all old--new polarization through the factor

\[
\Theta_S(z)
\overline{\Theta_S(w)}.
\]

The new-prime increment is not an orthogonal summand.

## Contratower

Reflection gives

\[
\Theta_S^\#=
\Theta_S^{-1}
\]

where both sides are defined. The reciprocal transition is

\[
\Theta_{S\cup\{q\}}^{-1}
=
\varphi_q^{-1}
\Theta_S^{-1}.
\]

Hence the primal and reciprocal multiplier towers form the commuting square

\[
\begin{matrix}
M_{\Theta_S}&\longrightarrow&M_{\Theta_S\varphi_q}\\
\downarrow *&&\downarrow *\\
M_{\Theta_S}^*&\longleftarrow&M_{\Theta_S\varphi_q}^*.


\]

Tensoring or squaring this block produces the prime-squared transition automatically.

## Why this does not prove positivity

The identity

\[
K_S=k_D-
\Theta_Sk_D\Theta_S^*
\]

is positive if and only if

\[
M_{\Theta_S}M_{\Theta_S}^*
\preceq I,
\]

which is exactly Schur contractivity of `Theta_S`. Therefore the factorization itself does not establish that `R_S` is a contraction.

More importantly, the negative feature

\[
R_S^*R_S=
\Theta_Sk_D\Theta_S^*
\]

is the full reflected-multiplier Hardy feature. It is generally infinite-rank and contains gamma, every prime, and their correlated products. It has not reduced to the two-dimensional endpoint cokernel.

Thus this is a mathematically exact `G-R*R` realization, but not yet the desired endpoint-controlled factorization.

## Minimality obstruction

Suppose one seeks another decomposition

\[
K_S=G_S-B_S^*B_S
\]

with `G_S>=0` and `B_S` of rank two representing only endpoint evaluations. If such a decomposition existed on the unrestricted observer space, then `K_S` would have at most two negative squares.

But the sign-changing prime translation channels can produce arbitrarily large negative Gram matrices unless the gamma bulk correlates them before compression. Therefore finite rank of `B_S` cannot be assumed; it must be proved from a source-derived cancellation.

The Szego decomposition shows exactly what must collapse:

\[
\boxed{
M_{\Theta_S}^*
\text{ must reduce, modulo a positive common bulk, to the physical endpoint map.}
}
\]

This is the same missing identification as `ker L* = endpoint`, now expressed at the reproducing-kernel level.

## Douglas factorization criterion

Let `E_L` denote the two-coordinate endpoint evaluation map on a finite analytic window. To replace the full negative feature by the endpoint feature, one needs a positive operator `A_S` and a contraction `C_S` satisfying

\[
M_{\Theta_S}^*
=
C_SA_S^{1/2}
+
R_{end,S}E_L,
\]

with the two summands orthogonal in the target feature space. Equivalently, the source Gram operator must obey a Douglas-type range inclusion and domination inequality.

Without the orthogonality identity, squaring introduces an uncontrolled cross term and does not reproduce `K_S`.

## Disposition

An unconditional common-bulk factorization and coherent `2x2` tower exist:

\[
\boxed{
K_S
=
k_D-
\Theta_Sk_D\Theta_S^*,
}
\]

\[
\boxed{
K_{S\cup\{q\}}
=
K_S+
\Theta_SK_{\varphi_q}\Theta_S^*.
}
\]

But the negative factor is the full reflected multiplier, not the endpoint pair. The remaining rung-four theorem is precisely a nontrivial reduction of this infinite-rank negative feature, after gamma--prime common-bulk cancellation, to the source-fixed endpoint harmonic cokernel.
