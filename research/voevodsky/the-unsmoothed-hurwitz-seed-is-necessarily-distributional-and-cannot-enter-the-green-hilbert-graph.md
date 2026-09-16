# The unsmoothed Hurwitz seed is necessarily distributional and cannot enter the Green Hilbert graph

## Question

Can the completed rational-coset support seed itself belong to the weighted second-order Green graph used by the radial four-port observer?

## Claim boundary

No. Before Mellin transform the seed is an atomic radial distribution. Endpoint subtraction removes its Mellin pole but does not remove the infinitely many interior delta atoms. Therefore it cannot be an \(H^1\), \(H^2\), or weighted relative Sobolev vector. The interface must remain rigged-dual or add an independently authorized smoothing map.

## Radial atomic form

For \(0<a<1\), radial logarithmic pushforward of

$$
P_a=\sum_{n\in\mathbb Z}\delta_{n+a}
$$

has the form

$$
\mathcal R_{\log}P_a
=
\sum_{n\in\mathbb Z}
\omega_{n,a}
\delta_{\log|n+a|},
$$

with nonzero half-density weights \(\omega_{n,a}\) determined by the chosen Mellin normalization. Its Mellin transform is the symmetric Hurwitz section.

The support points are discrete and unbounded. On every compact interval containing one such point, the distribution has a nonzero delta singularity.

## Sobolev obstruction

Every one-dimensional \(H^1_{\rm loc}\) vector has a locally absolutely continuous representative and contains no delta atom. The retained Green graph is stronger: its elements have locally absolutely continuous value and first derivative, with weighted \(L^2\) first and second derivatives.

Therefore

$$
\mathcal R_{\log}P_a
\notin H^1_{\rm loc}
$$

and hence

$$
\mathcal R_{\log}P_a
\notin\mathcal H_{{\rm rel},a_0}^2
$$

for every seam \(a_0\).

## Why endpoint subtraction does not help

The subtraction

$$
\frac{2}{s-1}
$$

removes the universal Mellin endpoint pole. In radial variables it changes an endpoint/asymptotic distribution. It does not cancel the individual atoms at \(\log|n+a|\). Consequently the finite-part seed remains a distribution rather than a Green-graph vector.

## Correct interface types

Two admissible routes remain:

1. retain the seed in the strong dual of the rapid Mellin/radial test space and formulate sewing through contragredient pairings;
2. apply a source-derived Fourier-commuting smoothing operator before asking for Green-graph membership, then prove cutoff and endpoint compatibility.

Embedding the unsmoothed seed directly into the Green Hilbert graph is impossible.

## Consequence for the Gram test

The previously proposed Hilbert orbit-Gram equality is not typed for the raw seed. On the rigged-dual route it must be replaced by preservation of the test/dual pairing and the four boundary character coefficients. A Hilbert Gram test becomes available only after a declared smoothing or regularization.

## Disposition

Green-graph membership of the unsmoothed Hurwitz seed is rejected. The canonical seed establishes a distributional G4 interface only. The next constructive choice is explicit: contragredient strong-dual sewing or source-authorized Fourier-equivariant smoothing.