# WP163 — tangent-actuator accessibility audit

## Bounded question

Does WP162's algebraically faithful tangent complement remain faithful after
the holonomy deformation is typed through a finite-energy actuator?

## Frozen instrument grammar

Use an on-shell actuator for the continuous protector gauge mode. A tangent
response is executable only when

\[
M_a<E_{\max},
\qquad E_{\max}=1.
\]

If the mode is accessible, retain WP162's three responses
\((D,nD,n^2D)\). If it is inaccessible, all three operational responses are
zero. The exact return tower is retained in both cases.

This is a typed conditional instrument, not a claim that every below-threshold
virtual susceptibility vanishes. Such a susceptibility would be a different
declared experiment with its own resolution and matching law.

## Exact rank phases

### Uniformly accessible packet

Set all four continuous-mode masses to

\[
M_a=\frac12.
\]

All tangent ports execute and the combined response has

\[
\operatorname{rank}R=7,
\qquad \dim\ker R=0.
\]

### Partial packet

Set the continuous masses to

\[
\left(\frac12,\frac34,\frac54,2\right).
\]

Exactly two tangent modes are accessible. The rank is six and the source
kernel has dimension one.

### Common dilation

Multiply the uniformly accessible masses by four:

\[
\frac12\longmapsto2.
\]

The low-energy selector and every return-order record are unchanged, but all
tangent actuators become inaccessible. The rank collapses to

\[
\operatorname{rank}R=4,
\qquad \dim\ker R=3.
\]

This is the exact accessibility analogue of WP131's threshold-scale
obstruction.

## Typing

- **Admitted state domain:** WP161's seven sources plus continuous gauge-mode
  masses.
- **Faithful flavor quotient:** `physical16`; the common mass dilation does not
  change the selected flavor packet.
- **Source-authorized probe family:** return records and conditionally
  executable on-shell tangent responses.
- **Contextual partition:** resolution depends on which continuous modes lie
  below reach; full separation is restricted to the uniformly accessible
  domain.
- **Separation:** rank seven, six, or four in the full, partial, and inaccessible
  packets respectively.
- **Selection:** none.
- **Rigidification:** none.
- **Descent:** mass and reach are physical relational data; all flavor records
  still descend under the full weak-basis groupoid.
- **Reference port:** the actuator and defect define a new relational
  experiment.
- **Physical instrument:** typed as an on-shell actuator, not implemented or
  calibrated.

## Smallest exact falsifier

The pair of source packets with common masses \(1/2\) and \(2\) have identical
ordinary flavor and return records, but their operational ranks are seven and
four. Finite reach therefore prevents uniform source identification.

## Remaining gates

An implemented experiment must derive the continuous symmetry-breaking scale,
gauge coupling, defect tension, mode width, actuator efficiency, and detector
resolution. A subthreshold virtual-response proposal must be frozen
independently and tested against decoupling and noise; it cannot inherit the
on-shell rank by algebraic continuation.

## Verification

```text
python research/flavor/checkers/wp163_tangent_actuator_accessibility.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The likely scale dilation made this a sharp operational test. The
confound was the deliberate on-shell instrument restriction.

Frozen optionality snapshot: one fully accessible mass packet, one partial
packet, one common dilation, ranks seven/six/four, 12 checks, and one typed but
unimplemented actuator.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. Algebraic joint faithfulness survived only on the fully accessible
domain. One partial kernel and the full three-dimensional inaccessible kernel
were restored exactly. The actuator is now typed, but no source-selected mass
scale, detector calibration, or subthreshold instrument was constructed.

