# The endpoint Schur gate is a distinguished feature contraction

## Question

What source object would prove both positivity of the gamma-plus-prime background and admissible subtraction of the endpoint mode?

## Conditional spectral explanation

Under RH, the full heat localizer is the positive zero-side Gram form

\[
L_{\rm full}(t,h)_{ij}
=
\sum_\gamma
 e^{-(t+(i+j)h)\gamma^2}
(1-e^{-h\gamma^2}).
\]

Since

\[
L_{\Gamma+\mathbb P}
=
L_{\rm full}+c_h(t)vv^*,
\qquad
c_h(t)=(e^{h/4}-1)e^{t/4},
\]

the remainder has an additional positive feature at the superunit endpoint coordinate. This explains the positive numerical inertia without treating it as evidence for RH.

## Source feature target

Seek a Hilbert space `H_(t,h)` and a source-derived feature map

\[
R_{t,h}:\mathbb C^{(\mathbb N)}
\longrightarrow\mathcal H_{t,h}
\]

such that

\[
L_{\Gamma+\mathbb P}=R_{t,h}^*R_{t,h}.
\]

The endpoint subtraction is admissible exactly when there is a distinguished vector `q_(t,h)` satisfying

\[
R_{t,h}^*q_{t,h}
=
\sqrt{c_h(t)}\,v,
\qquad
\|q_{t,h}\|\le1.
\]

Then

\[
L_{\rm full}
=
R_{t,h}^*(I-q_{t,h}q_{t,h}^*)R_{t,h}
\succeq0.
\]

This is the factor form of the pseudoinverse Schur condition and avoids choosing matrix inverses at every finite rank.

## Meta-coherence

The feature maps and distinguished vectors must be natural under:

- packet-rank restriction;
- base heat-scale translation;
- rational mesh refinement;
- arithmetic cutoff completion.

Finite restrictions then inherit the same rank-one repair. Observer-dependent Schur vectors do not define a global constructor.

## Why this may be the unlock

The endpoint defect rank is exactly one for every packet and mesh. Therefore the proof no longer asks for an arbitrary positive factor of the completed source. It asks for:

1. a Gram factor of the coupled gamma-plus-prime localizer;
2. one source-fixed contractive feature representing the polar endpoint.

This matches the successful finite-defect pattern in earlier Marici sectors while retaining the arithmetic completion data.

## Falsifiers

The route fails if any of the following occurs:

- `L_(Gamma+P)` has a negative direction;
- the endpoint vector lies outside `ran R*`;
- every representing `q` has norm greater than one;
- representing vectors cannot be chosen coherently across mesh refinement.

The first scan found none of the first defect through rank four, but was uncertified.

## Disposition

Promote the rank-one Schur gate to the primary source-factorization target. A proof should construct `R` and `q` directly from the coupled gamma-plus-prime source; determinant-by-determinant positivity is a shadow of this feature theorem.