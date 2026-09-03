# Minimal calibration for lossy Pauli tomography

## Question

What source-authorized calibration design makes nine-setting path–polarization tomography identifiable under static setting- and outcome-dependent multiplicative loss?

## Claim boundary

This packet assumes each setting–outcome channel has a fixed scalar efficiency shared between calibration and unknown-state exposures. It does not cover drift, dark counts, state-dependent loss, detector saturation, or unknown analyzer axes.

## Effective-efficiency model

For each joint Pauli setting \(j=(a,b)\) and outcome \(o=(s,t)\), let

\[
c_{j,o}=\eta_{j,o}p_{j,o}(\rho),
\qquad 0<\eta_{j,o}\le1.
\]

The quantities required for tomography are the thirty-six effective efficiencies \(\eta_{j,o}\). A decomposition into individual path and polarization detector efficiencies is not required for state recovery.

## One-reference calibration

Let \(\rho_{\rm ref}\) be a source-authorized reference whose ideal probabilities \(p_{j,o}(\rho_{\rm ref})\) are known and nonzero for all channels. Measuring it under all nine settings gives

\[
\eta_{j,o}=
\frac{c_{j,o}^{\rm ref}}
{p_{j,o}(\rho_{\rm ref})}.
\]

The maximally mixed state has probability \(1/4\) in every joint Pauli outcome, so one preparation type, exposed under all settings, calibrates all thirty-six effective efficiencies.

For an unknown state,

\[
p_{j,o}(\rho)=c_{j,o}/\eta_{j,o},
\]

and the calibrated Pauli reconstruction applies. The calibration and unknown-state exposures must share the same efficiencies; this is an operational stability assumption requiring its own test.

## Rank condition

With independent channel efficiencies, the calibration map has diagonal sensitivity matrix with entries \(p_{j,o}(\rho_{\rm ref})\). It has rank thirty-six exactly when every reference probability is nonzero.

If one reference outcome has zero probability, its efficiency is unidentifiable and the rank drops by one. Additional references repair the defect only if their ideal probabilities cover every previously zero channel. The general support condition is

\[
\forall(j,o)\;\exists r:
 p_{j,o}(\rho_r)>0.
\]

One full-support reference is therefore minimal in the number of preparation types under this model. Zero references leave the state–efficiency ambiguity already exhibited.

## Factorized-detector gauge

A stronger physical model may factor effective efficiency as

\[
\eta_{(a,b),(s,t)}=
\alpha_{a,s}\beta_{b,t}.
\]

Click data identify the products needed for tomography, but the factors have a scale gauge:

\[
\alpha_{a,s}\mapsto\lambda\alpha_{a,s},
\qquad
\beta_{b,t}\mapsto\lambda^{-1}\beta_{b,t}.
\]

Within the allowed efficiency interval this leaves every product unchanged. Individual detector efficiencies require a gauge-fixing reference channel or independent detector characterization. State recovery does not require choosing that gauge when effective products are calibrated directly.

## Source authority

The reference density operator and its preparation map must be independently justified. Calling an observed approximately uniform record “maximally mixed” would absorb detector imbalance into the reference and invalidate calibration. A physical implementation could use verified depolarization or a randomized ensemble, but its density matrix must be established independently of the detector being calibrated.

## Exact diagnostic

An exact rational checker assigns thirty-six nonzero efficiencies, calibrates them from a uniform full-support reference, and recovers a state with \(XX\) correlation \(1/2\). Setting one reference probability to zero reduces rank from thirty-six to thirty-five. Two distinct factor pairs with the same product exhibit the detector-factor gauge.

## Disposition

Under static multiplicative channel loss, one source-authorized full-support reference preparation measured across all nine settings is sufficient and preparation-count minimal for effective-efficiency calibration. Full support is the exact rank condition. Factorized detector parameters retain a scale gauge, but calibrated effective products suffice for tomography. Drift and nonmultiplicative loss remain outside this theorem.
