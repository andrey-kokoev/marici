# Normalized Gram convergence gives eventual Douglas equivalences on every finite observer packet

## Finite observer packet

Let

\[
E_0
=
\operatorname{span}
\{g_1,
\ldots,
g_m\}
\]

be a finite-dimensional observer-amplitude packet. Let

\[
G_0(g,h)
=
\tau_S
\left(
U_S(h)^*U_S(g)
\right)
\]

be its Plancherel Gram form.

After quotienting any source null vectors, assume

\[
G_0>0
\]

on `E_0`.

Let

\[
\Phi_\Lambda:E_0
\to
\mathcal K_\Lambda
\]

be a positive cutoff feature with Gram form

\[
G_\Lambda
=
\Phi_\Lambda^*
\Phi_\Lambda.
\]

For the positive triple feature, one expects volume

\[
V_\Lambda
=2\log\Lambda.
\]

## Normalized convergence hypothesis

Assume

\[
\boxed{
\frac1{V_\Lambda}
G_\Lambda
\longrightarrow
G_0
}
\]

entrywise on `E_0`.

Because `E_0` is finite-dimensional, entrywise convergence in one basis is equivalent to operator-norm convergence relative to `G_0`.

Thus for every `epsilon in (0,1)`, there is `Lambda_0(E_0,epsilon)` such that

\[
\boxed{
(1-\varepsilon)
V_\Lambda G_0
\preceq
G_\Lambda
\preceq
(1+\varepsilon)
V_\Lambda G_0
}
\]

for all `Lambda>=Lambda_0`.

## Eventual kernel stability

The lower bound implies

\[
G_\Lambda(g,g)=0
\Longrightarrow
G_0(g,g)=0.
\]

Since `G_0` is positive definite on the source quotient,

\[
\boxed{
\ker(\Phi_\Lambda|_{E_0})=0
}
\]

for every sufficiently large cutoff.

Hence cutoff comparison maps are well-defined in both directions on each fixed finite packet.

## Douglas domination between two cutoffs

For `Lambda,Lambda'>=Lambda_0`, combine the upper bound at `Lambda'` with the lower bound at `Lambda`:

\[
G_{\Lambda'}
\preceq
\frac{
(1+\varepsilon)V_{\Lambda'}
}{
(1-\varepsilon)V_\Lambda
}
G_\Lambda.
\]

Therefore Douglas factorization gives a bounded map

\[
T_{\Lambda'\Lambda}^{E_0}:
\overline{
\Phi_\Lambda(E_0)
}
\to
\overline{
\Phi_{\Lambda'}(E_0)
}
\]

with

\[
T_{\Lambda'\Lambda}^{E_0}
\Phi_\Lambda(g)
=
\Phi_{\Lambda'}(g).
\]

Its norm satisfies

\[
\boxed{
\|T_{\Lambda'\Lambda}^{E_0}\|^2
\le
\frac{
(1+\varepsilon)V_{\Lambda'}
}{
(1-\varepsilon)V_\Lambda
}.
}
\]

The reverse map exists with the reciprocal volume ratio bound.

## Volume-normalized features

Define

\[
\widehat\Phi_\Lambda
=V_\Lambda^{-1/2}
\Phi_\Lambda.
\]

Its Gram form is

\[
\widehat G_\Lambda
=V_\Lambda^{-1}G_\Lambda.
\]

The normalized cutoff comparison satisfies

\[
\boxed{
\|\widehat T_{\Lambda'\Lambda}^{E_0}\|^2
\le
\frac{1+\varepsilon}{1-\varepsilon}.
}
\]

As both cutoffs tend to infinity and the Gram errors shrink,

\[
\|\widehat T_{\Lambda'\Lambda}^{E_0}\|
\to1.
\]

Likewise the reverse norm tends to one. Thus the normalized finite-packet feature spaces are asymptotically isometric.

## Canonical realization through the source Gram space

Complete `E_0` in `G_0`; since it is finite-dimensional, call the resulting Hilbert space

\[
\mathcal H(E_0,G_0).
\]

Define

\[
S_\Lambda:
\mathcal H(E_0,G_0)
\to
\overline{\widehat\Phi_\Lambda(E_0)},
\qquad
S_\Lambda g
=
\widehat\Phi_\Lambda(g).
\]

Then

\[
S_\Lambda^*S_\Lambda
=
\widehat G_\Lambda
\to I
\]

in operator norm. For large cutoff, polar decomposition gives

\[
S_\Lambda
=U_\Lambda
|S_\Lambda|,
\]

where

\[
U_\Lambda:
\mathcal H(E_0,G_0)
\xrightarrow{\sim}
\overline{\widehat\Phi_\Lambda(E_0)}
\]

is unitary.

Therefore

\[
\boxed{
U_{\Lambda'}U_\Lambda^*
}
\]

is a canonical unitary comparison after choosing the positive polar factors. It differs from the exact label-preserving Douglas map by the small Gram distortion `|S_Lambda|`.

## Strict label-preserving composition

The Douglas map defined on observer-generated vectors by

\[
T_{\Lambda'\Lambda}
\Phi_\Lambda(g)
=
\Phi_{\Lambda'}(g)
\]

composes strictly:

\[
\boxed{
T_{\Lambda''\Lambda'}
T_{\Lambda'\Lambda}
=
T_{\Lambda''\Lambda}
}
\]

on the finite packet, because all maps retain the same source observer label.

Thus every cutoff-only coherence simplex on a fixed finite packet commutes exactly once the cutoffs exceed its nondegeneracy threshold.

## Application to dyadic towers

At each cutoff and depth, let

\[
\Phi_{\Lambda,n}
\]

be the finite dyadic feature. The depth maps are exact isometries, so

\[
G_{\Lambda,n}
=G_{\Lambda,0}
\]

as total Gram forms.

Consequently the same finite-packet Douglas estimate applies uniformly in dyadic depth:

\[
T_{(\Lambda',n'),(\Lambda,n)}
\]

can be defined by first using the strict depth isometries and then the cutoff comparison, or in the opposite order. Both maps agree on every source-labelled observer vector.

## What normalized convergence is needed

For the positive triple feature,

\[
G_\Lambda(g,h)
=
\operatorname{Tr}
\left(
U_S(h)^*
P_\Lambda Q_\Lambda P_\Lambda
U_S(g)
\right).
\]

The finite-packet hypothesis is

\[
\boxed{
\frac1{2\log\Lambda}
G_\Lambda(g_i,g_j)
\longrightarrow
G_0(g_i,g_j)
}
\]

for every pair in the packet.

Diagonal convergence plus polarization gives all matrix entries. Thus it suffices to establish the leading-density theorem for every finite collection of polarized observer pairs.

## Current analytic status

Connes's theorem supplies the leading density for the nonpositive product trace. Passing it to the positive triple feature requires the sewing term to be `o(log Lambda)` on each polarized observer pair.

The localized Hardy estimate currently gives at most `O(log Lambda)` in the semilocal model. Hence the finite-packet Douglas theorem is conditional on cancellation of the sewing linear coefficient or a sharper `o(log Lambda)` estimate.

Once that scalar pairwise estimate is proved, no further infinite-dimensional operator theorem is needed for any fixed finite packet.

## Why this does not globalize automatically

On the full completed observer space, pointwise convergence

\[
\widehat G_\Lambda(g,h)
\to
G_0(g,h)
\]

does not imply operator-norm convergence. The smallest Gram eigenvalue on growing packets may tend to zero because of prolate near-one/near-zero concentration.

Thus the threshold

\[
\Lambda_0(E_0,\varepsilon)
\]

and Douglas constants need not be uniform as the packet dimension grows.

This is exactly the compact-window coercivity collapse recorded in prior research.

## Count consequence

For every fixed finite packet on which normalized Gram convergence is proved, all cutoff-direction correspondences eventually promote to bounded isomorphisms. Combined with strict dyadic depth maps, every finite truncated coherence cell on that packet is certified at the normalized bulk level.

There is no single global finite count because:

- the cutoff threshold depends on the packet;
- the positive refinement has unbounded dyadic depth;
- no uniform completed-space domination is available.

## Disposition

Finite-packet cutoff promotion is completely controlled by normalized Gram convergence:

\[
\boxed{
V_\Lambda^{-1}G_\Lambda
\to G_0
\quad\Longrightarrow\quad
\text{eventual strict Douglas equivalences on }E_0.
}
\]

The remaining analytic input is pairwise `o(log Lambda)` control of the sewing term. Uniform promotion to the completed observer space is obstructed by collapse of the smallest prolate Gram eigenvalue.
