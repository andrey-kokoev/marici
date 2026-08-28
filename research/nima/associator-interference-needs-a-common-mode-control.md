# Associator interference needs a common-mode control

## Question

Can one bright/dark bracketing measurement distinguish an associator phase
from an unknown apparatus phase?

## Claim boundary

No. A single target setting identifies only the product of the associator and
apparatus phases. A control setting identifies the associator only when both
settings share the same calibrated multiplicative nuisance.

## Single-setting ambiguity

Let the desired associator comparison be \(\omega_t\in U(1)\), and let the
interferometer contribute an unknown relative phase \(\kappa_t\). The measured
comparison is

\[
z_t=\kappa_t\omega_t.
\]

For any proposed \(\omega_t\), choose
\(\kappa_t=z_t\omega_t^{-1}\). The target measurement alone therefore cannot
separate source associator from apparatus phase.

In the sign model, the explanation
\((\omega_t,\kappa_t)=(-1,+1)\) and the alternative
\((\omega_t,\kappa_t)=(+1,-1)\)

produce the same dark-port record.

## Common-mode control

Add a control triple with known source associator \(\omega_c=1\). If target and
control share one apparatus factor \(\kappa\), then

\[
z_c=\kappa,
\qquad
\frac{z_t}{z_c}=\omega_t.
\]

The ratio identifies the target associator without selecting \(\kappa\).
Equivalently, the two settings form a relational probe of the apparatus phase.

## The shared-factor gate

The cancellation is valid only if the apparatus contribution is common:

\[
\kappa_t=\kappa_c.
\]

Matching output hardware, equal path lengths, or identical scalar calibration
values do not establish this equality. It requires a source-derived transport
or a differential design proving that every nuisance phase outside the
associator cell is shared.

If \(\kappa_t\) and \(\kappa_c\) vary independently, then

\[
\frac{z_t}{z_c}
=
\frac{\kappa_t}{\kappa_c}\omega_t,
\]

and the ambiguity remains complete.

## Minimal instrument architecture

The operational probe now has two signed observers at two settings:

1. a target bracketing interferometer;
2. a control bracketing interferometer;
3. a source-derived comparison asserting common nuisance transport;
4. a ratio or differential port formed only after that comparison.

The third item is the coherencer. Without it, two measurements are merely two
independent unknown products.

## Cross-sector consequences

- Optical associator probes need a reference triple routed through the same
  phase response as the target triple.
- Flavor interference requires control and signal settings with a proved
  common detector and source phase, not merely similar rates.
- Software constructor-tree comparisons need a control tree whose compiler
  path shares the same normalization and authority transport.
- Boundary-line bracketing tests need a source-derived common determinant
  frame across the control and target tuples.

## DPC

For a controlled higher-coherence experiment:

1. write the target and control readouts as nuisance times source response;
2. test identifiability with independent nuisance factors;
3. derive the common-factor equality from source transport;
4. form the ratio only after that derivation;
5. vary the nuisance jointly and verify invariance;
6. vary it independently as a hostile and require the claim to fail;
7. retain the result as conditional if common-mode transport is not yet
   constructed.

## Disposition

Bracketing interference is necessary but not self-calibrating. One
source-matched control cancels a common apparatus phase exactly. Without the
common-mode constructor, the associator class remains nonidentifiable.

## Verification

The checker check_associator_common_mode_control.py exhausts the binary source
and nuisance signs, proves single-setting nonidentifiability, verifies exact
recovery under a shared nuisance, and constructs independent-nuisance hostile
models with identical observations and opposite associator signs.
