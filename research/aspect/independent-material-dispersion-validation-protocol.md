# Independent material-dispersion validation protocol

## Question

What constitutes an independent validation of a sourced optical-material dispersion model, and how should its residuals enter attachment margins?

## Claim boundary

This packet defines the validation design and residual calculus. It contains no source model, fitted parameter, measurement dataset, or agreement result.

## Independence gate

A dataset is independent only when it was not used to fit, select, tune, truncate, or choose the validity band of the tested model. Shared publication, specimen batch, calibration chain, or preprocessing may introduce dependence and must be recorded.

A holdout split created after inspecting all residuals is not independent evidence. If no external dataset exists, preregistered new measurements may provide validation, but their apparatus calibration must not use the tested model as its reference.

## Compatibility pullback

Before comparing model and data, construct the interface descriptor:

- vacuum, air, or medium wavelength convention;
- wavelength or angular-frequency coordinate and orientation;
- refractive index, group index, phase delay, or transfer-function target;
- length, temperature, pressure, polarization, composition, and specimen conditions;
- measurement uncertainty and correlation structure;
- model validity band and excluded poles.

Comparison exists only on the pullback where these descriptors agree or where a sourced conversion map transports one to the other. Equal numerical wavelength values do not establish compatibility.

## Residual enclosure

For measurement interval

\[
y_i\in[\underline y_i,\overline y_i]
\]

and model prediction interval

\[
m_i\in[\underline m_i,\overline m_i],
\]

the residual interval is

\[
r_i=y_i-m_i
\in
[\underline y_i-\overline m_i,
 \overline y_i-\underline m_i].
\]

A pointwise compatibility test asks whether zero lies in each residual interval. A uniform physical-model bound requires an outward enclosure

\[
\sup_{\omega\in\Omega}|r(\omega)|\le R,
\]

including gaps between measurement frequencies through a justified regularity or interpolation bound. The maximum sampled residual alone is not a band-wide bound.

When covariance is available, retain correlated ellipsoidal or likelihood structure rather than replacing it with independent boxes. When it is unavailable, do not manufacture independence.

## Validation dispositions

The comparison has four typed outcomes:

1. **compatible within stated uncertainty:** every tested residual satisfies the preregistered criterion;
2. **rejected on a certified sub-band:** at least one residual interval excludes the admissible tolerance;
3. **inconclusive:** uncertainty or coverage cannot discriminate;
4. **interface mismatch:** units, specimen conditions, or target quantity do not admit comparison.

Passing sampled points validates only the tested model, conditions, and band. It does not validate extrapolation toward a resonance or a different material batch.

## Transport into attachment margins

A certified refractive-index residual bound \(R_n\) becomes a phase error only through the source phase map. For path length \(L\) and vacuum wavelength \(\lambda\), a nondispersive pointwise conversion has form

\[
|\delta\phi|\le
\frac{2\pi L}{\lambda}R_n,
\]

with all quantities enclosed outward. Frequency-dependent derivative residuals similarly contribute to the slope and curvature budgets. The attachment certificate must cite the exact validation band and conditions.

## Deliberate-failure tests

The eventual checker must reject:

- use of fit data as validation data;
- a unit-convention mismatch;
- a validation point outside the model band;
- sampled residuals promoted to continuous coverage without a gap bound;
- residual intervals narrowed by dropping parameter covariance;
- an injected measurement whose interval is disjoint from the model interval.

## Current evidence boundary

The authoritative model-source branch is deferred, and no independent dataset exists in the searched repository scope. The Site exposes no admitted external acquisition surface. Therefore no residual or agreement claim can presently be computed.

## Disposition

The independent-validation protocol is complete, but execution is deferred until both a sourced model and an independently acquired compatible dataset are present. Only certified residual bounds, not nominal agreement or sampled visual fit, may enter physical attachment margins.
