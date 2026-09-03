# No local positive Weil density

## Question

Can the pre-GNS Weil functional be factored by identifying the explicit-formula distribution itself with a positive measure or pointwise nonnegative density in the \(u\) coordinate?

## Claim boundary

That local mechanism is ruled out conditional on the standard sign and normalization of the prime Dirac terms. Positivity on the restricted heat-polynomial test cone remains open.

## Declared functional

The relevant pre-GNS object is

\[
Q_{t,h}(p)
=
\left\langle
W,
e^{-tu^2}(1-e^{-hu^2})
|p(e^{-hu^2})|^2
\right\rangle.
\]

The desired statement is positivity of \(Q_{t,h}\) on this restricted family. It is not positivity of \(W\) on every nonnegative test function.

## Prime singular support

In the standard explicit formula, the prime contribution contains terms of the form

\[
-\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\]

For every prime power, the coefficient is strictly negative. Endpoint and archimedean contributions are smooth near a nonzero prime locus or are supported elsewhere.

A smooth distribution cannot cancel the coefficient of an isolated Dirac atom. Choose a nonnegative bump \(\phi_\varepsilon\) supported near \(\log n\), equal to one there, and excluding all other singular loci. Then

\[
\langle W,\phi_\varepsilon\rangle
=
-\frac{\Lambda(n)}{\sqrt n}
+O(\varepsilon).
\]

For sufficiently small \(\varepsilon\), this is negative.

Therefore \(W\) is not a positive Radon measure.

## Falsified mechanisms

The following source-factor subclasses are inadmissible:

- a pointwise nonnegative Weil density;
- multiplication by a positive \(u\)-space weight;
- a local square integral
  \[
  Q(f)=\int w(u)|f(u)|^2du,
  \qquad w(u)\geq0,
  \]
  that purports to equal the explicit Weil distribution term by term;
- smoothing the gamma term and claiming that it cancels negative prime atoms distributionally.

The singular coefficients prevent all of them.

## What this does not falsify

The restricted functions

\[
e^{-tu^2}(1-e^{-hu^2})|p(e^{-hu^2})|^2
\]

do not include arbitrary compactly supported bumps. Failure of positivity on the full nonnegative test cone therefore does not imply failure on this restricted algebra.

Possible surviving mechanisms include:

- a nonlocal integral kernel;
- an operator with off-diagonal support coupling;
- positivity only after quotienting by relations in the restricted test algebra;
- a transform that sends the Weil distribution to a positive form without preserving pointwise support;
- an infinite-dimensional reproducing-kernel factor.

## Relation to determinant cross terms

The positive gamma--prime cross contribution in \(D_2\) arises when taking the determinant of the additive matrix

\[
L=L_\Gamma+L_P.
\]

It does not imply a bilinear gamma--prime term in \(W\). Consequently it neither supplies nor requires a source coupling operator. Any nonlocal source factor must be derived independently from \(Q_{t,h}\).

## Remaining source check

The exact explicit-formula convention must be attached to verify:

- the sign of each prime Dirac coefficient;
- the \(n^{-1/2}\) normalization;
- the symmetric loci \(\pm\log n\);
- the support and regularity of endpoint and gamma terms.

Once fixed, the local-positive-measure no-go is exact.

## Disposition

A direct positive density in the explicit-formula coordinate is falsified. The all-rank search must move to nonlocal or restricted-cone positivity of the declared Weil functional. This narrows the surviving source mechanisms without asserting that the restricted cone fails.

## Verification

- `research/voevodsky/no-local-positive-weil-density-v1.json`
- `research/voevodsky/checkers/check_no_local_positive_weil_density.py`
- `research/voevodsky/results/no_local_positive_weil_density.json`
