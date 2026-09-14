# Conditional proposal: polynomial characterwise prolate growth would give an o-log sewing bound, but the bare transition norm is infinite

## Characterwise sewing factorization

After finite angular and outer regularization, decompose the sewing trace into angular characters:

\[
\mathcal E_{L,S}(g,h)
=
\sum_\chi
\mathcal E_{L,\chi}(g,h).
\]

For each character, the off-diagonal block factorization gives

\[
\boxed{
|\mathcal E_{L,\chi}(g,h)|
\le
p_{L,\chi}^{1/2}d_\chi(g,h),
}
\]

where

\[
p_{L,\chi}
=
\|P Q(I-P)K_\chi\|_{HS}^2
\]

is the radial prolate transition mass in that angular sector, and

\[
d_\chi(g,h)
=
\|K_\chi[P,U_S(g)U_S(h)^*]K_\chi\|_{HS}
\]

is the observer boundary-commutator norm, with cross-character blocks included below when the observer is not angular diagonal.

The key point is that `p` enters through its square root.

## Polynomial prolate hypothesis

Assume the characterwise radial estimate

\[
\boxed{
p_{L,\chi}
\le
C_S
(1+|\chi|)^d
(1+L).
}
\]

This is the precise polynomial Tate/prolate estimate isolated by the angular-mode analysis.

Then

\[
\boxed{
p_{L,\chi}^{1/2}
\le
C_S^{1/2}
(1+|\chi|)^{d/2}
(1+L)^{1/2}.
}
\]

## Rapid observer boundary decay

Smooth compactly supported observers have rapidly decreasing angular Fourier coefficients. The same is true after taking the cutoff commutator, because the module cutoff is angular invariant.

Thus for every `N`,

\[
\boxed{
d_\chi(g,h)
\le
C_{g,h,N}
(1+|\chi|)^{-N}.
}
\]

For observers in a bounded smooth packet, the constant can be chosen uniformly at fixed `N`.

## Summation

Combine the two bounds:

\[
|\mathcal E_{L,\chi}(g,h)|
\le
C_{S,g,h,N}
(1+L)^{1/2}
(1+|\chi|)^{d/2-N}.
\]

Choose `N` larger than `d/2` plus the polynomial counting dimension of the discrete angular dual. Then

\[
\sum_\chi
(1+|\chi|)^{d/2-N}
<\infty.
\]

Therefore

\[
\boxed{
|\mathcal E_{L,S}(g,h)|
\le
C_{S,g,h}
(1+L)^{1/2}.
}
\]

Since `L=log Lambda`,

\[
\boxed{
\mathcal E_{\Lambda,S}(g,h)
=O_{S,g,h}
(\sqrt{\log\Lambda})
=o_{S,g,h}
(\log\Lambda).
}
\]

This is the pairwise estimate required by the finite-observer-packet Douglas theorem.

## Cross-character observer blocks

If the observer is not diagonal in the angular decomposition, write

\[
d_{\chi,\psi}(g,h)
=
\|K_\chi[P,U_S(g)U_S(h)^*]K_\psi\|_{HS}.
\]

Smoothness gives, for every `N`,

\[
\boxed{
d_{\chi,\psi}(g,h)
\le
C_{g,h,N}
(1+|\chi|+|\psi|)^{-N}.
}
\]

The sewing sum is bounded by terms of the form

\[
p_{L,\chi}^{1/2}
d_{\chi,\psi}(g,h)
\]

or the symmetric product with `p_(L,psi)`. Polynomial counting in two character variables is still dominated by choosing `N` sufficiently large. The same `O(sqrt L)` conclusion follows.

## Regulator removal

The estimate is first proved at finite angular cutoff `K_N` and finite outer cutoff `R`. The majorant above is independent of `N`. Therefore angular dominated convergence permits

\[
N\to\infty.
\]

For the outer cutoff, take the limit at the combined trace-product level. If the finite-annulus sewing stabilizes or has a trace-norm dominated limit, the same bound survives `R->infinity` by Fatou/dominated convergence.

Thus the conclusion for the unregulated sewing remains conditional on the previously isolated outer-cutoff product convergence, but no additional logarithmic loss occurs during angular removal.

## Normalized positive Gram convergence

Connes's product trace has pairwise asymptotic

\[
\mathcal T_{\Lambda,S}(g,h)
=
2\log\LambdaG_0(g,h)
+W_S(g*h^*)
+o(1).
\]

The positive triple Gram form satisfies

\[
G_\Lambda^+(g,h)
=
\mathcal T_{\Lambda,S}(g,h)
-
\mathcal E_{\Lambda,S}(g,h).
\]

Using the `o(log Lambda)` sewing bound gives

\[
\boxed{
\frac1{2\log\Lambda}
G_\Lambda^+(g,h)
\longrightarrow
G_0(g,h).
}
\]

Hence every fixed finite observer packet with nondegenerate `G_0` eventually has strict Douglas cutoff equivalences.

## Uniform finite-packet statement

Let

\[
E_0
=
\operatorname{span}
\{g_1,
\ldots,g_m\}.
\]

There are finitely many polarized pairs `(g_i,g_j)`. The constants in the `O(sqrt(log Lambda))` bounds can be maximized over those pairs. Therefore normalized Gram convergence holds in matrix/operator norm on `E_0`.

This verifies the analytic hypothesis of the finite-packet Douglas theorem, subject only to the characterwise polynomial prolate estimate and outer-cutoff product convergence.

## What remains conditional

Two inputs are not yet source-proved in the full semilocal carrier:

1. the polynomial characterwise prolate estimate
   \[
   p_{L,\chi}
   \le
   C(1+|\chi|)^d(1+L);
   \]
2. removal of the second physical cutoff in the combined observer-weighted sewing product.

The localized Hardy/Tate calculation strongly motivates the first but does not yet identify every normalization with the exact quotient operator. The regular half-line model proves stabilization for the second only in its translation-invariant kernel setting.

## Why no linear cancellation theorem is needed

The earlier strong-Szego discussion allowed a possible linear sewing coefficient

\[
La_\chi(g,h).
\]

The weighted Cauchy estimate shows that, under the polynomial transition and rapid observer-boundary hypotheses, the **total** sewing is only `O(sqrt L)`. Therefore its linear coefficient must vanish after observer-weighted angular assembly:

\[
\boxed{
\sum_\chi
a_\chi(g,h)=0.
}
\]

This cancellation is a consequence of positive transition control and observer localization, not a separate symbolic identity.

A finite relative phase term may still survive inside the `O(sqrt L)` envelope.

## Positivity limitation

The result proves normalized positive bulk convergence. It does not identify the finite part

\[
G_\Lambda^+
-
2\log\LambdaG_0,
\]

because an `O(sqrt(log Lambda))` sewing term can still diverge. Full positive boundary convergence requires the stronger relative Hardy/Widom asymptotic.

## Subsequent correction

The bare characterwise quantity `p_(L,chi)=||PQ(I-P)K_chi||_HS^2` is generally infinite in the continuous radial Hardy model. The `O(sqrt L)` argument therefore does not apply as written. Only the observer-localized `O(L)` estimate remains established. See `correction-the-characterwise-bare-hardy-transition-is-not-hilbert-schmidt-so-the-sqrt-log-sewing-bound-is-unproved.md`.

## Disposition

The following implication is conditional on a finite centered/relative replacement for the bare transition norm:

\[
\boxed{
\begin{aligned}
&	ext{polynomial characterwise prolate transition}\\
&+
\text{rapid observer boundary decay}\\
&+
\text{outer product convergence}
\end{aligned}
\Longrightarrow
\mathcal E_{\Lambda,S}(g,h)
=o(\log\Lambda).
}
\]

This is sufficient to promote every fixed finite observer packet from cutoff correspondences to eventual normalized Douglas equivalences. The remaining finite-boundary problem is strictly sharper than the bulk coherence problem.
