# Theta Completion Replaces Factorized Augmentation by a Joint Gaussian Observation

## Euler observation

Write an integer label as

\[
n=\prod_pp^{k_p}.
\]

The Euler colligation treats each valuation coordinate separately. Its local
augmentation row assigns the same coefficient to every valuation state, and a
finite-prime transfer factorizes across primes.

## Theta observation

The completed theta source instead reads the integer label through

\[
w_x(n)=e^{-\pi x n^2}.
\]

In valuation coordinates, let

\[
Q(k)=\sum_pk_p\log p.
\]

Then

\[
w_x(k)=\exp\left(-\pi x e^{2Q(k)}\right).
\]

This observation depends on the joint total logarithmic scale. It is not a
tensor product of independent prime observations.

For two nonzero valuation labels (k\) at (p\) and \(\ell\) at (q\),

\[
w_x(p^kq^\ell)
=e^{-\pi x p^{2k}q^{2\ell}},
\]

whereas the product of separate observations is

\[
w_x(p^k)w_x(q^\ell)
=e^{-\pi x(p^{2k}+q^{2\ell})}.
\]

They are generically unequal. Theta completion synthesizes the joint integer
scale before applying the Gaussian readout.

## Exact mixed derivative

Let (u=\pi x e^{2Q}\) and \(W(Q)=e^{-u}\). Then

\[
W''(Q)=4u(u-1)e^{-u}.
\]

Because every valuation direction enters through the same (Q\), for distinct
primes (p,q\),

\[
\frac{\partial^2w_x}
{\partial k_p\,\partial k_q}
=4(\log p)(\log q)u(u-1)e^{-u}.
\]

The mixed prime incidence is therefore explicit and nonzero except at the
source-defined transition (u=1\). It is rank one in logarithmic label
directions but nonlinear in total scale.

## Completion operation

The source-derived change from Euler to theta presentation is now typed:

1. retain the full labelled valuation packet;
2. synthesize the total log-scale (Q\);
3. apply the Gaussian observation (e^{-\pi x e^{2Q}}\);
4. sum integer labels;
5. perform Poisson reciprocal sewing in (x\);
6. take the Mellin readout.

The order is essential. Applying scalar augmentation prime by prime and then
trying to reconstruct the Gaussian joint weight is impossible: the nonlinear
mixed incidence has already been erased.

## Consequence

This identifies the exact cross-prime capability demanded by Entries 3959 and
3960. Nontrivial completed zeros can arise because theta observation is not a
locally uniform limit of factorized Euler observations. It is a different,
source-authorized joint observation on the same labelled integer carrier.

The finding does not prove zero confinement. Positive Gaussian weights can
still have oscillatory Mellin transforms, and Aspect's hostile sums show that
positive aggregation alone is insufficient. The next theorem must use Poisson
sewing to constrain the transmission zeros of this joint observation.

## Falsifier

Any proposed completed Rosenbrock system whose output row factorizes over
primes cannot reproduce the theta mixed derivative above. Conversely, any
output row fitted directly from \(\Xi\) without deriving the total-scale
Gaussian from the integer source lacks source authority.
