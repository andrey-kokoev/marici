# Carrier Archimedean smooth-completion functor audit

## Question

Is the Archimedean analytic lens genuinely absent, or can it be constructed canonically from the conditional component semiring?

## Canonical decategorified chain

Under the free disjoint-union hypothesis, there is a canonical chain

`Surf_U^disjoint-union -> pi_0 -> M -> G(M) -> Frac(G(M)) -> R`.

The first map sends an object to its connected-component class and every isomorphism to equality of classes. The next objects are respectively the initial semiring, its ordered group completion, its ordered fraction field, and its complete Archimedean ordered-field completion. Each step is fixed by a universal property.

The positive multiplicative group of the final field has its canonical smooth structure and Haar measure up to scalar. Requiring self-dual additive Fourier measure fixes the additive normalization; the relative additive/multiplicative Haar ratio then supplies the half-density. Identity tangent fixes logarithm. Thus a canonical Archimedean lens can be constructed from `pi_0` in principle.

## Exact limitation

This composite factors through `pi_0` and kills all source automorphisms, including the noncommuting `D4` action. It is therefore a decategorified arithmetic realization, not a faithful realization of the occurrence-resolved Carrier groupoid. Physical packets already exhibit readouts that detect source commutators, so this projection cannot serve as a universal physical realization or justify transporting every sector selection.

The distinction removes a false requirement: the zeta spline arithmetic lens need not be faithful to every Carrier automorphism. It must instead declare that it is a `pi_0` realization and prove that every constructor used by the spline descends through that quotient.

## Remaining descent test

Disjoint union and derived multiplication descend by construction. Gaussian scale, Fourier transform, Haar comparison, and Mellin characters live after completion. What is not yet proved is that the theta/Poisson source constructor used by the completed-zeta packet is the image of a pre-quotient Carrier constructor rather than an independently supplied analytic operation.

A hostile realization can share the same `pi_0 -> R` object map while assigning no pre-quotient Fourier/Poisson morphism. It reproduces arithmetic labels and weights but not source transport.

## Disposition

The Archimedean smooth completion is canonically available as a conditional `pi_0` arithmetic lens; its absence was overstated. It is intentionally nonfaithful on Carrier automorphisms. The next missing arrow is constructor descent: a source-derived pre-quotient operation whose completed image is the Gaussian Fourier--Poisson transport used in the zeta spline.
