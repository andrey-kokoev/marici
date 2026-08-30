# Hidden three-body phase falsifier

## Question

Can both bracketings pass every lower-excitation and proper-marginal control
while an ordinary route-local interaction produces a false associator residual?

## Exact hostile

Compare the identity circuit with a controlled three-body phase that acts as
the identity on seven computational carrier branches and multiplies `111` by
minus one.

Every input containing at most two occupied wings sees exactly the identity.
Therefore all vacuum, one-wing, two-wing, pairwise HOM, linear transfer, and
proper-subsystem calibrations can agree between the routes.

On the three-wing coherent carrier, the hidden phase maps the plus GHZ
coherence to the minus GHZ coherence. At `gamma=3/5`, the expected curve

```text
3/5, 0, -3/5, 0
```

becomes

```text
-3/5, 0, 3/5, 0.
```

If only one bracketing contains this phase, the apparent associator residual is

```text
6/5, 0, -6/5, 0.
```

Every proper reduced state remains unchanged.

## Distinction from the triad-mode hostile

The Bargmann gate calibrates the native ternary phase of the photons' internal
mode Gram matrix. This hostile is a path-conditional three-body phase inside
the sewing circuit. Equal input triad invariants do not constrain it.

## Repair

Each bracketing requires a native three-body process-phase calibration using an
independently phase-certified triple-coherence reference. The reference must be
routed through the same occupied paths and vacuum dilations as the science
carrier but prepared and sealed independently.

Use both coherence signs and both global phase quadratures. A route-local
three-body phase follows the circuit. A source associator follows the declared
bracketing transformation under physical circuit exchange.

No collection of lower-arity calibrations can replace this gate. That is a
theorem consequence, not an engineering preference.

## Disposition

The previous fourteen-gate preregistration was still incomplete. Native
three-body input calibration and native three-body process calibration are
different carriers and must both match.

## Verification

Run:

```text
python research/aspect/checkers/check_hidden_three_body_phase_falsifier.py
```
