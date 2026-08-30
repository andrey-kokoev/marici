# The readout layer is a capability-indexed instrument surface

## Correction

“Readout” is too passive. A physical interaction can both emit a classical
record and change the state available to later interactions. The appropriate
finite object is an instrument

\[
\mathcal I_i:\rho\longmapsto\mathcal I_i(\rho),
\]

with

\[
p_i=\operatorname{Tr}\mathcal I_i(\rho),
\qquad
\rho_i'=\frac{\mathcal I_i(\rho)}{p_i}.
\]

Different physical systems possess different capabilities: preparations,
effects, channels, accepted supports, and access to diagnostic refinements.

## Formal cross-sector completion

For both scattering analyzer projectors and flavor mass projectors, the exact
checker constructs the repeatable Lüders instrument

\[
\mathcal I_i(\rho)=E_i\rho E_i.
\]

The outcome probabilities normalize, every nonzero conditional state has
unit trace, and repeating the selected effect preserves that state. This is a
mathematical completion of the established effect algebras, not yet a
source-derived physical instrument.

## Public read versus diagnostic access

Let \(E=E_0+E_1\). Two interactions can expose the same public coarse
probability:

\[
\operatorname{Tr}(E\rho E)
=
\operatorname{Tr}(E_0\rho E_0+E_1\rho E_1),
\]

while producing different post-interaction states. The direct coarse
instrument preserves coherence inside the coarse block; measuring the fine
diagnostic alternatives and forgetting the result destroys it.

Therefore:

\[
\boxed{
\text{same visible read record}
\not\Rightarrow
\text{same physical interaction contract}.}
\]

This types the browser-console analogy. A diagnostic or side-channel
capability may reveal implementation detail, but exercising it can itself
change the implementation state. It is not merely a larger passive query.

## Architectural model

\[
\boxed{
\text{capability-indexed interaction surface}
=
\text{preparations}
+\text{effects}
+\text{state-transforming instruments}
+\text{public records}
+\text{diagnostic/side-channel refinements}.}
\]

The public semantic surface consists of operations stable under declared
internal equivalences. Observable implementation details may remain available
through stronger capabilities without becoming part of that public contract.

## Provenance obstruction

The physical sources do not currently select these updates:

- Entry 1576 states that detector effects, phase-space support, and accepted
  conditionalization are not supplied by the scattering amplitude trace;
- Entry 1586 derives the fixed-kinematics probability packet but leaves the
  accepted-event pushforward open;
- the flavor source supplies weak-basis invariants and CKM transition data,
  not a state-update rule for a flavor-measurement apparatus.

Therefore the strongest presently supported statement is:

\[
\boxed{
\text{shared physical effect-algebra interface}
+\text{available formal instrument completions}
\neq
\text{shared source-derived physical instrument surface}.}
\]

## Scope

The exact test establishes that the existing scattering and flavor
Hilbert-space realizations admit instrument structures and that probabilities
alone underdetermine backaction. It does not establish which completion is
physical. The Carrier-level capability lattice remains conjectural.
