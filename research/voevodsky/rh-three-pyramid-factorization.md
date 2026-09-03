# RH as a three-pyramid factorization

## Question

Should the RH construction use several coherence pyramids rather than demand one pyramid carry analytic completion, arithmetic presentation, and positivity?

## Claim boundary

Multiple pyramids improve typing and error localization. They do not create the missing positivity theorem.

## Pyramid A: analytic coherence

Its apex is the completed centered analytic object \((\Xi,\rho_{\rm an})\). Its layers are:

- the function-valued theta–Mellin square;
- Poisson reciprocity and polar normalization;
- reciprocal affine fillers;
- cutoff and orbit completion.

This pyramid establishes that the completed object exists and that its presentations commute. It does not orient its spectral distribution positively.

## Pyramid B: arithmetic presentation

Its apex is \(\rho_{\rm ar}\), presented by the coupled explicit formula

\[
\Theta=\Theta_{\rm endpoint}+\Theta_{\rm gamma}+\Theta_{\rm prime}.
\]

Its layers contain sector source maps, imaginary-character crossing, common analytic continuation, and cancellation before scalarization. The endpoint Toeplitz deficit proves that this pyramid cannot be decomposed into positive sector pyramids.

The cross-pyramid normalization cell is

\[
\rho_{\rm an}\simeq\rho_{\rm ar}.
\]

This cell is now available at classical strength.

## Pyramid C: positivity probes

Its apex is the positive cone inside even tempered distributions. Its equivalent faithful faces are:

- global scalar heat complete monotonicity for every \(k\geq0\) and \(t>0\);
- all translate ranks at one fixed Gaussian width;
- positive Bernstein or Bochner measure realization;
- extension to the full Schwartz test space.

The probe cell from Pyramid B is

\[
K_\sigma(d)=
\langle\rho_{\rm ar},e^{-2\sigma u^2}e^{-idu}\rangle.
\]

## RH as the missing lift

RH is not another filler inside Pyramid A. It is the existence of a lift

\[
\rho_{\rm ar}\longrightarrow
\mathcal S'(\mathbb R)_{\geq0}
\]

compatible with the normalization and probe cells. Equivalently, the arithmetic apex must land in the positivity apex.

This explains the repeated failed promotions:

- analytic completion fills Pyramid A but supplies no positivity lift;
- sectorwise estimates live inside Pyramid B but destroy required cancellation;
- finite jets and scalar values are nonfaithful projections of Pyramid C;
- reconstructing Gram atoms from zeros reverses the lift.

## Two versus three pyramids

Three pyramids are the provenance-preserving presentation: analytic construction, arithmetic presentation, and positivity reflection remain distinct. Since the comparison between the first two is already proved, they may be quotiented to one representation pyramid, leaving an equivalent two-pyramid diagram:

\[
\text{completed representation}
\longrightarrow
\text{faithful positivity probes}.
\]

The three-pyramid version is safer for research because it exposes exactly where endpoint–gamma–prime cancellation enters. A fourth pyramid is not justified by a new object or functor.

## Disposition

The architecture supports the operator's proposal. RH must factor across pyramids, but the only missing cross-pyramid datum is the positivity lift for the coupled arithmetic apex. The acceptance test is an all-order sign-preserving factorization or a one-width all-rank Gram theorem derived without zero-location input.
