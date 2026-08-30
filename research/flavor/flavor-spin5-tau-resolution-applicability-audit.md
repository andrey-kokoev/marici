# Spin(5) tau-resolution applicability audit (WP899)

## Question

Does the existing WP251--WP256 tau pilot supply the calibrated Gaussian
resolution parameter required by WP898?

## Typed observable mismatch

No. WP253 records the visible invariant mass of one reconstructed muon and one
hadronic tau candidate,

\[
m_{mu\tau_h}^{\rm vis}.
\]

This observable contains tau-decay neutrino loss, decay-angle variation,
selection effects, and detector response. It is not an event-level residual
between a reconstructed parent mass and a known generator parent mass. A broad
visible-mass histogram therefore does not measure the Gaussian \(\sigma\) in
WP898's additive parent-line convolution.

The serialized pilot supplies none of the five application fields:

1. true parent mass joined event by event;
2. reconstructed parent-mass estimator;
3. centered residual calibration;
4. Gaussian core fit with covariance;
5. non-Gaussian tail budget.

Its applicability vector is consequently \((0,0,0,0,0)\). WP256's nonzero
source-relative leave-one-out residual
\(12641608/354073635\) is consistent with this failure: even dividing by the
source label does not produce a universal exact response shape.

## First nonfaithful arrow

The failed substitution is

\[
\text{visible tau-pair mass spread}
\not\longrightarrow
\text{calibrated parent-mass resolution kernel}.
\]

WP898 remains a valid conditional theorem, but no numerical resolution floor
is currently certified by the tau pilot.

## Repair

The direct-pole execution must retain generator ancestry and either construct
a calibrated parent estimator or replace the Gaussian model by a full
conditional response kernel

\[
K(m_{m vis}\mid m_{m parent},\Gamma,q,\eta)
\]

with nuisance coordinate \(\eta\). The zero-width and finite-width cards must
then be compared with common seeds or an independently declared sampling
design. The smallest falsifier is a tail or mass-dependent efficiency effect
whose induced six-bin drift exceeds the preregistered tolerance.

WP899 is an interface no-go, not a failure of the finite tau discriminator and
not a selector result.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp899_spin5_tau_resolution_applicability_audit.py
~~~
