# Calibration drift versus state signal

## Question

When can efficiency drift between calibration and unknown-state exposures imitate a path–polarization signal, and what interleaved-reference assumptions separate them?

## Claim boundary

This packet treats binary channels with multiplicative efficiency drift. It derives a worst-case expectation bias bound and an exact affine-drift correction. It does not assume that workflow order is physical time or that real detector drift is affine.

## Drift model

Let calibration determine efficiencies \(\eta_+,\eta_->0\). During the unknown-state exposure suppose

\[
\eta'_\pm=\eta_\pm(1+\delta_\pm),
\qquad |\delta_\pm|\le\varepsilon<1.
\]

For true Pauli expectation \(m\), division by stale calibration produces

\[
q_+=(1+\delta_+)\frac{1+m}{2},
\qquad
q_-=(1+\delta_-)\frac{1-m}{2}.
\]

If these corrected clicks are normalized, the inferred expectation is

\[
\widehat m=rac{q_+-q_-}{q_++q_-}.
\]

Direct subtraction gives

\[
\widehat m-m=
\frac{(1-m^2)(\delta_+-\delta_-)}
{2\left(1+\delta_+(1+m)/2+\delta_-(1-m)/2\right)}.
\]

The denominator is at least \(1-\varepsilon\), so

\[
|\widehat m-m|
\le
\frac{\varepsilon(1-m^2)}{1-\varepsilon}
\le
\frac{\varepsilon}{1-\varepsilon}.
\]

Common-mode drift \(\delta_+=\delta_-\) cancels in the normalized expectation. Differential drift is the confounder.

## Exact indistinguishability witness

Take stale calibrated efficiencies \((1/2,1/2)\). A true state with \(m=0\) and measurement efficiencies \((3/4,1/4)\) yields

\[
(c_+,c_-,c_\varnothing)=(3/8,1/8,1/2).
\]

The same records arise with no drift and state expectation \(m=1/2\). Thus one calibration followed by one unknown exposure cannot distinguish differential efficiency drift from state signal, even when no-click records are retained.

## Interleaved references

Introduce a declared workflow coordinate \(u\in[0,1]\) indexing operations between two reference exposures. It has no physical-time meaning unless a separate map to a physical clock is supplied.

If each efficiency is affine in \(u\),

\[
\eta_o(u)=(1-u)\eta_o(0)+u\eta_o(1),
\]

then full-support reference measurements at \(u=0\) and \(u=1\) determine the efficiency exactly at every known intermediate coordinate. Correcting the unknown exposure with this interpolation restores the ideal probabilities.

Endpoint references do not identify nonaffine drift. A midpoint deviation can preserve both endpoint calibrations while biasing the unknown-state reconstruction. Under bounded but otherwise arbitrary drift, interleaving supplies uncertainty intervals rather than exact correction.

## Multi-setting consequence

The argument applies independently to every setting–outcome channel. Nine-setting tomography remains identifiable under an admitted shared drift model only when the reference schedule makes every model parameter identifiable and all unknown exposures have known workflow coordinates. Otherwise drift directions that overlap the fifteen Pauli signal directions remain gauge-like confounders.

## Exact diagnostic

An exact rational checker verifies the drift/state indistinguishability pair, the general bound on a rational grid, cancellation of common-mode drift, exact affine interpolation and state recovery, and a nonlinear midpoint falsifier invisible to endpoint references.

## Disposition

Differential calibration drift can exactly imitate a quantum-state expectation. The bias is bounded by \(\varepsilon(1-m^2)/(1-\varepsilon)\) under relative drift bound \(\varepsilon\). Two interleaved full-support references correct drift exactly only under a declared affine workflow-coordinate model; endpoint agreement alone does not validate that model.
