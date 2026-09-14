# Route-residue optical probe acceptance protocol

## Question

What measurements would admit or reject a claimed optical realization of the shell-generating route-residue probe?

## Claim boundary

This protocol defines finite-cutoff acceptance tests from measured transfer, detector, loss, uncertainty, and noise data. Conditional distinguishability through a compatible faithful probe is already fixed by the composition structure; the protocol tests whether an apparatus constructs such a probe with calibrated reach. It does not supply those data or set an apparatus-specific confidence level. The inherited term `common-history operator` denotes a coarse composition readout and has no temporal interpretation.

## Declared finite packet

Freeze one arithmetic cutoff, its edge list, incidence matrix \(\partial\), and an exact cycle basis \(F\). Declare shell labels \(j(e)\), probe settings \(t_n\), optical input modes, detector bins, and all normalization conventions before collecting the discriminating data.

## Transfer calibration

Measure the complex transfer matrix \(M_n\) from shell-labelled input modes to optical modes at every setting. Fit no shell reassignment after observing residue sensitivity. The ideal intertwining target is

\[
M_n\iota-\iota D_{t_n}=0.
\]

Record a validated operator-norm uncertainty \(\varepsilon_{M,n}\). Acceptance requires

\[
\|M_n\iota-\iota D_{t_n}\|
\leq\varepsilon_{M,n}
\]

for every used setting, together with injectivity of \(\iota\) on the tested shell packet.

## Detector pullback

Measure the detector coupler \(\widetilde C\) independently of the cycle test. Compare

\[
\widetilde C\iota
\]

with the declared finite common-history operator \(C\). Record uncertainty \(\varepsilon_C\) and require

\[
\|\widetilde C\iota-C\|
\leq\varepsilon_C.
\]

This prevents a detector optimized after seeing a target countercycle from being called a realization of common history.

## Loss normalization

For each setting, retain detected and no-detection counts. Reconstruct the detected effects and loss effect and test

\[
\sum_iE_{i,n}+E_{{\rm loss},n}=I
\]

within the independently estimated normalization uncertainty. Do not renormalize detected events to unit total.

## Residue sensitivity certificate

Construct the measured differential response restricted to exact cycles,

\[
R=\begin{pmatrix}R_0F\\R_1F\\\vdots\end{pmatrix}.
\]

Let \(\widehat R\) be the estimated matrix and let \(\eta_R\) bound its operator error. A sufficient robust injectivity certificate is

\[
\sigma_{\min}(\widehat R)>\eta_R.
\]

This criterion has no fitted detection threshold: it compares the smallest measured singular value with the complete propagated uncertainty bound. Failure leaves an unresolved or detected null direction.

## Noise and Fisher form

Estimate the joint noise covariance \(N\) across detector bins, probe settings, and loss channels from independent repetitions. Require positivity and a lower spectral bound on the measured response range. Then form

\[
Q=R^*N^{-1}R.
\]

Propagate uncertainty in both \(R\) and \(N\). Report the smallest confidence-bounded eigenvalue of \(Q\) on cycle coordinates. Positivity without a lower uncertainty margin does not certify residue detection.

## Deliberate controls

The protocol requires:

1. a zero-cycle control, which should produce no differential residue signal;
2. the exact four-edge rectangle, whose unmodulated history cancels;
3. a modulated rectangle expected to produce nonzero response;
4. an injected synthetic blind direction, which the rank test must reject;
5. a removed-loss analysis, which must fail normalization rather than silently pass.

## Decision

Admit physical route-residue coupling at the declared cutoff only if transfer intertwining, detector pullback, loss normalization, robust cycle injectivity, and noise positivity all pass with preregistered uncertainty construction. Failure of any item identifies its own residual; no other passing item repairs it.

## Disposition

The research frontier is now experimental rather than algebraically underspecified. The first missing objects are calibrated transfer matrices, detector pullback data, loss counts, and joint noise samples from an apparatus with independently addressable shell modes.
