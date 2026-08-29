# The two-point symbol test applies only after bilateralization, not to the source half-line history

## Source geometry correction

The source seam operator is not initially bilateral convolution. On the positive half-line it is

\[
(Hc)(t)
=
\int_t^\infty
\Phi(p-t)c(p)\,dp,
\]

with adjoint

\[
(H^{*}y)(p)
=
\int_0^p
\Phi(p-t)y(t)\,dt.
\]

This is an anti-Volterra operator paired with a forward Volterra adjoint. It is a compression of translation-invariant convolution, not itself a normal multiplier operator.

Therefore the previous exact formula

\[
c_\pm
=
\operatorname{dist}
\left(
\mp i,\operatorname{essran}m
\right)
\]

is authoritative only for a proved bilateral completion. It cannot be applied directly to the source half-line history.

## What survives without normality

The shifted-history Gram identity remains exact on the half-line:

\[
D_\pm
=
\frac12(I\pm iH)^{*}(I\pm iH).
\]

Hence the true source-native gate is still

\[
\inf_{\|x\|=1}
\|(I\pm iH)x\|>0.
\]

But this is now a singular-value problem for non-normal Volterra operators. Spectrum or multiplier range alone does not decide it.

## Finite cutoffs

On a finite interval \([0,L]\), the Volterra structure often makes \(I\pm iH_L\) algebraically invertible through a resolvent series. This proves finite existence, not a uniform margin. The inverse norm can grow with \(L\) even when every finite operator has spectrum \(\{1\}\).

Thus the exact completion question is

\[
\sup_L
\|(I\pm iH_L)^{-1}\|<\infty.
\]

This is a pseudospectral and resolvent-growth theorem, not an eigenvalue-exclusion theorem.

## Bilateral dilation requires a comparison theorem

A bilateral operator

\[
(\widetilde Hf)(t)
=
\int_0^\infty\Phi(r)f(t+r)\,dr
\]

does have multiplier \(m\). But to use its two-point distance bound for the source half-line system one must prove a compression or dilation estimate such as

\[
\|(I\pm iH_L)^{-1}\|
\le
C
\|(I\pm i\widetilde H)^{-1}\|
\]

uniformly in \(L\), or a stronger unitary-dilation theorem preserving the relevant shifted resolvents.

Ordinary compression does not preserve inverse bounds automatically. Boundary reflections can create large finite-section pseudospectra invisible in the bilateral symbol.

## Relation to the existing range obstruction

Grothendieck's full tail–seam Gram is faithful but not bounded below on unrestricted packet \(L^2\), due to high-frequency modulation and decay of \(\widehat\Phi\). This does not directly falsify the shifted-history blocks, because their graph energy includes the identity wall. But it proves that the full seam Gram alone cannot supply a uniform auxiliary lower scale in the unrestricted coefficient topology.

The source must choose among:

- the graph energy with an authorized identity-wall term;
- a restricted arithmetic packet topology;
- or a stronger source-derived label regularity energy.

## Exact hostiles

1. Every finite Volterra cutoff has invertible \(I\pm iH_L\), but the inverse norms diverge with \(L\).
2. The bilateral symbol stays uniformly away from \(\pm i\), while half-line finite sections develop large resolvent norms.
3. The full seam Gram is injective but not closed-range; replacing it by graph energy silently changes the source topology unless the wall term is authorized.
4. A restricted arithmetic packet class repairs the margin, but is not stable under the nine admitted constructors.

## Revised frontier

There are now two separate theorems:

1. **Wall–graph authority**
   \[
   S=\frac12(I_{\mathrm{wall}}+H^{*}H).
   \]
2. **Uniform half-line shifted resolvent**
   \[
   \sup_{p,L,\pm}
   \|(I\pm iH_{p,L})^{-1}\|<\infty.
   \]

Only after these are proved may the bilateral two-point symbol test be used as a representation or comparison aid. It is not the source theorem itself.
