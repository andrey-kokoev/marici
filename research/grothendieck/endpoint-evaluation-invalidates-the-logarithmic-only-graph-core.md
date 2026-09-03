# Endpoint evaluation invalidates the logarithmic-only graph core

## Defect

The previous graph-core reduction treated endpoint evaluation as bounded after an unspecified Bargmann transport and then concluded that the gamma logarithmic weight determined the whole graph topology. This is not established and is generally false for the original spectral test function.

If `f` is represented by a Fourier variable `x`, analytic continuation gives schematically

\[
f(i/2)=\int \widehat f(x)e^{-x/2}\,dx,
\qquad
f(-i/2)=\int \widehat f(x)e^{x/2}\,dx.
\]

These functionals are not bounded in the ordinary real-line `L^2` norm, nor in a norm strengthened only by a logarithmic spectral multiplier. A unitary Bargmann transform does not turn them into bounded reproducing-kernel evaluations unless an explicit intertwining identity proves that the original endpoint functional is the claimed Fock evaluation.

## Required endpoint topology

A common source domain must control two-sided exponential Fourier moments. One admissible sufficient norm has a component of the form

\[
\int |\widehat f(x)|^2e^{(1+\epsilon)|x|}\,dx,
\qquad\epsilon>0,
\]

which bounds both endpoint evaluations by Cauchy--Schwarz. The precise exponent depends on the explicit-formula convention.

The true common graph topology must combine:

1. this endpoint exponential control;
2. the gamma logarithmic multiplication domain;
3. the labelled prime-row norm;
4. heat and translation invariance on a common core.

## Revised Fock gate

Bargmann--Fock space remains a candidate only if the selected Segal--Bargmann map satisfies a source-derived equality

\[
E_\pm(f)=\langle\mathcal Bf,k_\pm\rangle_{\mathcal F}
\]

for the actual endpoint functionals `E_+/-`, with `k_+/-` belonging to the chosen Fock space. This is an intertwining theorem, not a consequence of generic bounded point evaluation in Fock space.

## Core question reopened

Gaussian translates are a core for the logarithmic gamma multiplication domain, but that proves only the gamma part. To recover the full theorem, finite differences of Gaussian translates must converge in the stronger endpoint--gamma--prime graph topology. Gaussian decay makes this plausible for each derivative, but density of their span in the exponentially weighted Fourier domain requires a separate weighted completeness proof.

## Disposition

Withdraw the claim that bounded endpoint and prime rows leave only the gamma graph topology. Retain the gamma-core lemma as a sector theorem. Reopen the common form-core gate at the endpoint intertwiner and two-sided exponential-weight density.
