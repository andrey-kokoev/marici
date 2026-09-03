# Translate collisions force nonuniform meta-observer cutoffs

## Question

Why can pointwise eventual certification of every finite observer packet not be strengthened to one cutoff uniform over all packets of fixed rank?

## Two-point collision

Consider the distinct two-point packet

\[
I_h=(0,h),
\qquad h\ne0.
\]

For a continuous positive difference kernel, its Gram matrix is

\[
G_h=
\begin{pmatrix}
K(0)&K(h)\\
\overline{K(h)}&K(0)
\end{pmatrix},
\]

with minimum eigenvalue

\[
\lambda_{\min}(G_h)=K(0)-|K(h)|.
\]

Continuity gives

\[
\lambda_{\min}(G_h)\longrightarrow0
\qquad(h\to0).
\]

For an even positive spectral measure with finite Gaussian second moment,

\[
K(0)-K(h)
=
\int(1-\cos(hu))\,d\mu_\sigma(u)
=
\frac{h^2}{2}
\int u^2\,d\mu_\sigma(u)+O(h^4).
\]

Thus distinct packets can approach the repetition boundary with a quadratic loss of positivity margin.

## Quantifier consequence

A tail test requires

\[
2\varepsilon_N<\lambda_{\min}(G_h).
\]

For every fixed arithmetic cutoff `N`, sufficiently small nonzero `h` violates this inequality. Therefore even under RH there is no cutoff depending only on observer rank that certifies all distinct rank-two packets.

The valid statement is

\[
\forall I\;\exists N(I),
\]

not

\[
\exists N\;\forall I.
\]

## Geometric strata

Uniformity can be recovered only on compact collision-free packet strata. After quotienting common translation, fix:

- rank at most `r`;
- diameter at most `D`;
- pairwise separation at least `Delta>0`;
- Gaussian width in a compact interval bounded away from zero.

If strict positivity holds pointwise, continuity of the minimum eigenvalue on this compact configuration space gives a positive stratum margin. A cutoff may then be chosen uniformly on that stratum.

This compactness argument is conditional unless the pointwise strictness and continuity inputs are established from the admitted source.

## Meta-observer index correction

Observer packets should not be indexed only by rank. The quantitative index must retain collision geometry:

\[
(r,D,\Delta,\sigma,I).
\]

Dropping `Delta` loses the datum controlling the distance to the presentation-kernel boundary. Repeated-label quotienting removes exact duplicates but does not create a uniform gap for nearly repeated labels.

## Disposition

Retain pointwise eventual tail certification. Reject rank-only uniform cutoff claims. Use collision-free compact strata when a uniform computational budget is needed, and report the separation dependence explicitly.
