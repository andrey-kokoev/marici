# Reference objectivity is groupoid descent plus fault-qualified readout

## Question

When does a relational signal measured against transported references define an
objective readout rather than a gauge choice, a noisy convention, or an
undetected reference fault?

## DPC

### Source data

Let a finite gauge group (G) act on a set of admissible frame assignments
(T). Let a reference graph carry edge transitions in (G), let (S) be the
set of source-authorized selectors, and let (r:T\to Y) be a proposed
readout. A noise channel may alter reference transitions before readout.

The proposed explanation is:

> Objective relational readout is obtained by synchronizing the reference
> graph, retaining the resulting action groupoid when no natural gauge exists,
> and descending a source-authorized readout that is both orbit-invariant and
> faithful on the intended physical quotient.

### Predictions

The proposal predicts all of the following before sector-specific fitting:

1. Every closed reference cycle has identity product in the fault-free model.
2. Frame assignments reconstructed from a connected graph form one global
   (G)-torsor.
3. A canonical representative exists exactly when the authorized presentation
   action has a fixed admissible assignment and that choice has source
   authority.
4. Without such a fixed point, the canonical result is the action groupoid,
   not an orbit representative.
5. A scalar readout descends exactly when it is constant on every authorized
   orbit. Descent does not imply faithfulness between distinct orbits.
6. Binary tag noise attenuates the signed channel by (1-2\omega), so an
   unbiased random tag destroys orientation information.
7. A cycle syndrome may detect a bad edge without locating it. Fault
   correction therefore requires enough independent cycle checks to separate
   the admitted fault hypotheses.
8. Gain inside the same signal-reference loop cannot improve their relative
   signal-to-reference-error ratio when both acquire the same pole. Only an
   independently rooted reference cycle or downstream-noise suppression adds
   information.

### Finite falsifiers

- A nonidentity product around a declared fault-free cycle rejects coherent
  synchronization.
- The two-point torsor exchanged by a presentation swap rejects strict natural
  gauge selection while preserving the action groupoid.
- A gauge-dependent scalar rejects readout descent.
- A constant orbit-invariant scalar proves that descent alone is not physical
  faithfulness.
- One bad edge in a triangle gives a nontrivial syndrome but three equally
  admissible single-edge repairs, rejecting fault localization.
- At \(\omega=1/2\), the signed response vanishes.
- Common-loop gain multiplies signal and loop-reference perturbation by the
  same factor and therefore cannot repair their synchronization.

## Exact resolution

The finite problem is resolved as a typed decision procedure.

1. Reject if the transition data do not close on cycles.
2. Construct the action groupoid of admissible synchronized frames.
3. Strictify only if a source-authorized presentation-fixed selector exists.
4. Otherwise retain the groupoid without choosing a representative.
5. Admit a readout only after proving orbit invariance.
6. Call it physically distinguishing only after proving faithfulness on the
   declared physical orbit set.
7. Qualify the result by the reference fault model. Detection without unique
   syndrome decoding is not correction.

Thus canonical objectivity does not require a canonical gauge. It requires a
canonical relational groupoid and a lawful readout from it. Gauge descent,
physical faithfulness, and fault correction are three independent properties.

The checker resolves all finite logical gates. It deliberately does not infer
the physical reference carrier, presentation action, noise model, or readout
authority for a particular sector. Those remain source-incidence obligations.

## Claim boundary

This is a finite theorem and compiler contract. It does not prove that any
specific optical, flavor, arithmetic, or civic apparatus supplies the required
reference graph or source-authorized readout. It does not turn graph admission
into truth certification.

## Disposition

The abstract DPC passes. The naive claim that objectivity requires a preferred
frame is false. The corrected claim is exact: objectivity is invariant,
fault-qualified readout from a canonical action groupoid; strict gauge choice
is an optional additional structure.

