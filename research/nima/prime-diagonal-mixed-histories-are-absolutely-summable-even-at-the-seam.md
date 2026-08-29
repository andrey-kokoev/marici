# Prime-diagonal mixed histories are absolutely summable even at the seam

## Local mixed form hypothesis

Fix a prime \(p\), put \(L_p=\log p\), and let

\[
\beta_p
\]

be the unweighted local mixed Green/Stokes form produced by the adjacent history cell.

The local history estimates imply the natural growth target

\[
\|\beta_p\|
\le
C L_p.
\]

This allows one factor of \(\sqrt{L_p}\) from each endpoint history. A sharper boundary-only estimate may improve this, but linear logarithmic growth is already sufficient.

## Frozen arithmetic coefficient

The primitive endpoint contributes

\[
p^{-1/2-\sigma-it},
\]

and the square endpoint contributes

\[
\frac12p^{-1-2it}.
\]

Therefore the same-prime mixed coefficient has magnitude

\[
\frac12p^{-3/2-\sigma}.
\]

Define the prime-diagonal finite form

\[
b_\alpha^{(X)}(\sigma)
=
\frac12
\sum_{p\le X}
p^{-3/2-\sigma}
e^{i\vartheta_p}
\beta_p,
\]

where the phase \(e^{i\vartheta_p}\) is fixed by the source orientation and spectral parameter.

## Absolute operator-norm convergence

Under the local logarithmic bound,

\[
\left\|
\frac12p^{-3/2-\sigma}
e^{i\vartheta_p}
\beta_p
\right\|
\le
\frac C2
\frac{\log p}{p^{3/2+\sigma}}.
\]

The majorant converges already at the seam:

\[
\sum_p\frac{\log p}{p^{3/2}}<\infty.
\]

Hence

\[
b_\alpha^{(X)}(\sigma)
\]

is Cauchy in operator norm uniformly for every \(\sigma\ge0\), provided the assembly is prime-diagonal and the local forms share the declared source domains.

More precisely,

\[
\sup_{\sigma\ge0}
\|b_\alpha^{(Y)}(\sigma)-b_\alpha^{(X)}(\sigma)\|
\le
\frac C2
\sum_{X<p\le Y}
\frac{\log p}{p^{3/2}}.
\]

The right side tends to zero as \(X,Y\to\infty\).

## Important consequence

The primitive diagonal history diverges at the seam because its squared weight is \(p^{-1}\). The primitive-to-square mixed form has the stronger product weight \(p^{-3/2}\), so it may converge absolutely even when the primitive endpoint vector itself is only distributional.

Thus these are different gates:

- primitive self-energy needs Laplace rigging and wall residue;
- prime-diagonal primitive–square mixed energy may extend strongly to the seam.

One must not transfer the primitive diagonal divergence automatically to the mixed block.

## Cutoff naturality

If each finite form is defined by restricting the same local family,

\[
b_\alpha^{(Y)}|_X
=
b_\alpha^{(X)}
\]

is exact for \(X\le Y\). No renormalization depending on the upper cutoff is needed in the prime-diagonal mixed channel.

This naturality fails if local normalizations are recomputed after changing \(X\).

## When Kitaev's first falsifier remains live

A termwise Stokes family can fail to be Cauchy only if at least one of the following occurs:

1. the local norm grows faster than the summable threshold;
2. cross-prime mixed terms are authorized;
3. the domains vary incompatibly with \(p\) or \(X\);
4. cutoff-dependent chart normalizations destroy restriction naturality;
5. the source topology is stronger than the operator norm controlled above.

For local growth

\[
\|\beta_p\|\asymp p^\rho,
\]

the seam sum is absolutely convergent only when

\[
\rho<\frac12
\]

up to logarithmic factors.

The source logarithmic history growth lies safely below this threshold.

## Cross-prime extension

If the complete Green form contains terms

\[
\beta_{p,q},
\qquad p\ne q,
\]

the one-prime estimate does not suffice. One must test the weighted kernel

\[
K_{p,q}
=
p^{-1/2-\sigma}
q^{-1}
\beta_{p,q}
\]

by a Schur, Hilbert–Schmidt, or form-boundedness criterion.

The absence of primitive arithmetic flux at \(pq\) does not forbid an analytic cross-prime Green interaction. Therefore prime-diagonal assembly must be source-proved, not assumed.

## Radical and closability gates remain

Absolute convergence does not imply radical annihilation. Every local form must satisfy compatible kernel inclusions, or the sum may act on a global zero-energy direction.

Likewise a bounded form on quotient completions does not automatically yield a closable graph relation on the original primitive and square riggings.

Thus convergence can close before descent and graph realization.

## Revised first attack

The direct analytic attack should begin by proving the local bound

\[
\|\beta_p\|\le C\log p
\]

on a common source core and determining whether the source assembly is prime-diagonal.

If both hold, then:

- cutoff naturality is exact;
- off-seam uniformity extends through \(\sigma=0\) for the mixed block;
- operator-norm convergence is immediate;
- the first live difficulties move to radical descent, orientation, and closable pullback.

## Current frontier

The best local-to-global falsifier is now sharply conditional. It cannot occur for a prime-diagonal family with logarithmically bounded local Stokes forms, because the frozen primitive–square coefficient product is absolutely summable at the seam.

The next source calculation is therefore:

\[
\text{derive }\beta_p
\quad\text{and prove}\quad
\|\beta_p\|=O(\log p),
\]

while auditing whether any cross-prime Green blocks are present.
