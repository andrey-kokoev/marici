# RH forces strict positivity on distinct finite translate packets

## Question

Can the semidefinite boundary actually occur for a finite fixed-width Gaussian translate observer when all translate labels are distinct?

## Conditional spectral form

Under RH, the completed fixed-width kernel has a positive zero-side representation

\[
K_\sigma(a-b)
=
\sum_\gamma w_{\sigma,\gamma}
 e^{i(a-b)\gamma},
\qquad w_{\sigma,\gamma}>0,
\]

with ordinates repeated according to the source convention. For coefficients `c_j`,

\[
c^*G_Ic
=
\sum_\gamma w_{\sigma,\gamma}
\left|
\sum_jc_je^{ia_j\gamma}
\right|^2.
\]

A null vector therefore makes the exponential polynomial

\[
P(u)=\sum_jc_je^{ia_ju}
\]

vanish at every distinct zero ordinate.

## Zero-density mismatch

For distinct real frequencies `a_j`, a nonzero exponential polynomial has only linearly many real zeros in `[-T,T]`:

\[
N_P(T)=O_I(T).
\]

The source zero set has superlinear distinct-ordinate growth. One route is the Riemann--von Mangoldt count combined, under RH, with the classical multiplicity bound

\[
m(\rho)=O\!\left(\frac{\log |\gamma|}{\log\log |\gamma|}\right),
\]

which gives at least order `T log log T` distinct ordinates up to height `T`. Therefore no nonzero `P` can vanish on the full support. Hence `c=0` and

\[
G_I>0
\]

for every finite packet of distinct translates.

## Repeated labels

If a packet repeats a translate, its Gram matrix has an exact algebraic null vector obtained by subtracting the duplicate columns. These are presentation nulls, not spectral boundary phenomena. Quotienting packet repetitions restores the distinct-label statement.

## Consequence for tail decisions

Assuming RH and the cited distinct-zero growth input, every fixed finite distinct packet has a positive eigenvalue margin. Since arithmetic tail enclosures shrink to zero, some finite prime cutoff eventually certifies that packet as positive definite.

This is pointwise in the packet. It does not supply a cutoff uniform over all ranks, translate separations, or heat widths; minimum eigenvalues may approach zero along observer refinement.

## Logical boundary

The argument uses the positive zero-side representation and therefore cannot prove RH from the prime side. Its role is diagnostic: if RH holds, the exact semidefinite boundary lane is unnecessary for distinct finite translate packets. Boundary certificates remain necessary for repeated labels, quotient presentations, and more general observer families.

## Disposition

Refine the four-valued meta-observer protocol. For distinct finite Gaussian translate packets, RH predicts eventual `positive_definite`, not merely semidefinite admission. Persistent unresolved status at one fixed packet is compatible with slow bounds but not with a zero limiting eigenvalue under RH and the distinct-zero growth theorem.
