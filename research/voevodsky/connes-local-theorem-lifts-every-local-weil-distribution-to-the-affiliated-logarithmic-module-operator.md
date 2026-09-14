# Connes local theorem lifts every local Weil distribution to the affiliated logarithmic-module operator

## Source

Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Section V, Theorem 3 and equations (28)--(36).

The proof applies uniformly to every local field `K` equipped with a basic additive character and self-dual Haar measure.

## Affiliated logarithmic operator

On

\[
L^2(K,dx),
\]

define the real multiplication operator

\[
\boxed{
\mathcal L_K
=M_{-\log|x|_K}.
}
\]

Its maximal domain is

\[
\operatorname{Dom}
\mathcal L_K
=
\left\{
\psi:
(\log|x|_K)\psi(x)
\in
L^2(K)
\right\}.
\]

Because `-log|x|_K` is real, `mathcal L_K` is self-adjoint as a maximal multiplication operator. It is unbounded above and below and is therefore not positive.

## Fourier-conjugate principal-value operator

Let `F_K` be the additive Fourier transform associated with the basic character. Connes fixes the extension of

\[
\frac{dx}{|1-x|_K}
\]

by the condition that its additive Fourier transform vanish at `1`.

In the proof, the additive Fourier transform of

\[
-\log|u|_K
\]

is, away from zero, the distribution

\[
-\frac{1}{|a|_K},
\]

with the missing delta-at-zero constant fixed by that normalization. Thus

\[
\boxed{
F_K\mathcal L_KF_K^{-1}
=
\operatorname{PV}_{\psi_K}
\left(-\frac1{|a|_K}
\right)
}
\]

as an affiliated/distributional convolution operator on a Schwartz core.

This is the operator behind the normalized local Weil distribution.

## Observer symbol in the local proof

For a compactly supported multiplicative observer `h`, Connes defines

\[
g(u)
=
h((u+1)^{-1})|u+1|_K^{-1}.
\]

After the cutoff kernel calculation, the finite part is

\[
\boxed{
-
\int_K
g(u)\log|u|_Kdu.
}
\]

By Parseval and the normalized Fourier-transform identity, this equals

\[
\boxed{
W_K(h)
=
\int_{K^*}^{\prime}
\frac{h(a^{-1})}{|1-a|_K}d^*a.
}
\]

Therefore the local Weil functional is the observer pairing with the affiliated logarithmic operator:

\[
\boxed{
W_K(h)
=
\langle
M_g,\mathcal L_K
\rangle_{trace/distribution}
}
\]

with the source's symbol map `h -> g`.

## Archimedean place

For `K=R`,

\[
\mathcal L_\infty
=M_{-\log|x|}.
\]

Its Fourier-conjugate principal-value convolution operator is the physical-space realization of the gamma/digamma local term. After the multiplicative Fourier/Mellin transform, its spectral symbol is the archimedean phase derivative

\[
V_\infty(t)
=
-\frac12\log\pi
+
\frac12
\operatorname{Re}
\psi(1/4+it/2)
\]

up to the source normalization.

Thus the previously missing affiliated archimedean operator is not conjectural: it is `M_(-log|x|)` transported through the local Fourier/Mellin identifications.

## Finite places

For `K=Q_p`,

\[
-\log|x|_p
=(\operatorname{ord}_p x)
\log p.
\]

The spectral decomposition by valuation shells gives the complete prime-power translation series after multiplicative Fourier transform. Hence the bounded translation operator

\[
K_p
=
\frac{\log p}{2}
\sum_{k\ge1}
p^{-k/2}
(T_{k\log p}+T_{-k\log p})
\]

is the critical-line spectral image of the same local logarithmic-module operator.

The archimedean and finite-place constructions are therefore instances of one local operator mechanism.

## Semilocal sum

On

\[
A_S=
\prod_{v\in S}K_v,
\]

the module satisfies

\[
-\log|x|_S
=
\sum_{v\in S}
-\log|x_v|_v.
\]

Define the semilocal affiliated operator

\[
\boxed{
\mathcal L_S
=
\sum_{v\in S}
I\otimes\cdots\otimes
M_{-\log|x_v|_v}
\otimes\cdots\otimes I.
}
\]

On the algebraic Schwartz tensor core, this is multiplication by

\[
-\log|x|_S.
\]

Its observer pairing is exactly

\[
\boxed{
W_S(h)
=
\sum_{v\in S}W_v(h).
}
\]

This gives a common semilocal operator before scalar trace.

## Operator lift of `C_34`

The middle of the spectral-to-trace edge can now be written

\[
\boxed{
V_{loc,S}
\xleftrightarrow{\text{Mellin/Fourier}}
\mathcal L_S
\xrightarrow{\text{observer pairing}}
W_S.
}
\]

The first comparison is unitary/distributional transport on the Schwartz core. The second is the local trace-symbol pairing proved in Connes's local theorem.

Thus the feature-level operator gap is substantially reduced: the common feature is the logarithmic module operator `mathcal L_S`.

## Relation to the cutoff finite part

Connes's cutoff proof gives

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
=
2h(1)\log\Lambda
+
\langle
M_{g_h},
\mathcal L_S
\rangle
+
o(1).
\]

Therefore the cutoff finite part and spectral connection are two presentations of the same affiliated-operator pairing.

This is stronger than equality of final scalar formulas, although it still occurs at the level of distributional trace pairing rather than bounded trace-class operator equality.

## Endpoint normalization

The additive-character condition

\[

\widehat{
\operatorname{PV}_{\psi_K}
(1/|x|_K)
}(1)
=0
\]

fixes the delta ambiguity in the Fourier transform of `-log|x|_K`. This is the local boundary normalization appearing in Theorem 3.

It should not be confused with the global pole evaluations at `s=0,1`. The latter enter only after assembling the completed global explicit formula.

## Positivity audit

The local logarithmic operator changes sign:

\[
-\log|x|_K

\ge0
\quad\text{for }|x|_K\le1,
\]

and

\[
-\log|x|_K
\le0
\quad\text{for }|x|_K\ge1.
\]

Thus `mathcal L_S` is not positive. Its local Weil pairing is signed even on positive observer operators.

The operator lift solves coherence of presentations, not rung-four positivity.

## Positive/negative spectral split

The canonical sign decomposition is

\[
\mathcal L_S
=
\mathcal L_S^+
-
\mathcal L_S^-,
\]

where

\[
\mathcal L_S^\pm
=

\max(\pm\mathcal L_S,0)
\succeq0.
\]

Unlike a placewise split, this uses the total semilocal module

\[
-\log|x|_S
\]

and therefore retains cross-place geometry before taking signs.

The remaining positive-factorization problem is to show that, after physical compression and global endpoint completion, the negative spectral part is contractively embedded in the positive part.

## Disposition

Every local Weil term has a uniform affiliated-operator realization:

\[
\boxed{
\mathcal L_v
=M_{-\log|x|_v},
\qquad
W_v(h)
=
\langle M_{g_h},\mathcal L_v\rangle.
}
\]

Their semilocal sum is multiplication by `-log|x|_S`. This fills the archimedean and finite-prime operator-typing portions of `C_34`. The unresolved gate is positivity of the globally completed compression, not existence of the local operator lift.
