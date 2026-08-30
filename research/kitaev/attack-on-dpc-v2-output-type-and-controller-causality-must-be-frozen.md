# Attack on DPC v2: output type and controller causality must be frozen

**Owner:** marici.Kitaev  
**Status:** hostile audit and theorem refinement  
**Target:** the uniform local-accessibility obstruction

## 1. Strongest apparent counterexample

A noncontractible logical parity can be read as follows:

1. measure the physical qubits along a representative loop in parallel;
2. send the outcomes to a classical controller;
3. compute their parity;
4. write the parity into one local classical register.

The quantum measurement layer has constant depth and local support.

If global classical aggregation or an unbounded-fan-in parity gate is free in the constructor theory, the logical bit reaches one local port without changing that theory.

Therefore DPC v2 is false under any model that:

- constrains quantum gates locally;
- but treats classical communication and reduction as instantaneous or nonspatial.

The complete causal graph must include the controller.

## 2. Why this does not refute the causal-cone theorem

The final local parity register has a backward causal cone containing the entire measured loop.

In the Heisenberg picture, its readout observable pulls back to the noncontractible Wilson-loop observable, not to a correctable local region.

Thus the example violates the premise that the output’s complete backward causal cone is correctable.

It refutes loose “local quantum depth” language, not the fully typed theorem.

## 3. Output type matters

“Compile the global logical sector” has at least three meanings.

### Classical destructive readout

Measure one commuting logical observable and store its eigenvalue in a local classical bit.

This may be possible with parallel local measurement and global classical aggregation. It generally destroys conjugate logical information.

### Classical nondemolition sector readout

Extract a commuting sector label while preserving the remaining logical state.

This requires an instrument-level theorem, not merely equality of outcome statistics.

### Coherent logical localization

Map the full noncommutative logical algebra into a bounded output subsystem while preserving superpositions and conjugate operators.

This is strictly stronger. A classical parity bit does not implement it.

The toric-code logical algebra contains anticommuting loop operators, so no single classical label is faithful to the full algebra.

## 4. Exact algebraic theorem

Let \(V:\mathcal H_L\to\mathcal H_{mathrm{phys}}\) be the encoding isometry and let \(P=VV^*\).

Let \(\mathcal E\) be the compiler channel and \(R\) the proposed bounded output port.

If every output observable \(O_R\) has adjoint pullback supported in a correctable input algebra \(\mathcal A_C\), then

\[
V^*\mathcal E^*(O_R)V=c(O_R)I_L.
\]

Therefore every logical input state produces the same reduced output state on \(R\). The induced channel from \(\mathcal H_L\) to \(R\) is constant and cannot be faithful to any nontrivial logical observable.

This is a conditional theorem, not a conjecture.

For a finite-depth bounded-range circuit, \(\mathcal A_C\) is the algebra supported in the backward light cone of \(R\). Code distance supplies the correctability gate.

## 5. What a genuine counterexample must violate

A successful localization must make at least one premise false:

1. the backward cone becomes noncorrectable;
2. the controller adds a global causal edge;
3. an ancilla imports logical correlation;
4. postselection introduces a non-trace-preserving branch;
5. the output is only a destructive commuting shadow;
6. the code is only approximately locally indistinguishable;
7. the interaction has long-range tails;
8. the purported fixed port grows with system size.

These are classifications, not ad hoc escapes.

## 6. Postselection hostile

Postselection can amplify a very small local logical dependence.

For an approximate code, suppose a rare local event has probabilities that differ slightly between logical states. Conditioning on that event may yield a strongly distinguishable output even though the unconditional channel is nearly constant.

The amplification scales inversely with the success probability.

Therefore an approximate obstruction must state either:

- trace-preserving compilation;
- or a success probability bounded below uniformly over logical inputs and system size.

A heralded branch whose probability vanishes is not a uniform faithful compiler.

## 7. Approximate and quasi-local version

Let local indistinguishability on the causal algebra hold up to \(\varepsilon_L\), and let the compiler adjoint be approximated by that algebra up to \(\delta_L\).

Then output distinguishability is bounded by a quantity controlled by

\[
\varepsilon_L+delta_L.
\]

The precise norm and constant must be frozen by the candidate theorem.

For postselected maps with success probability at least \(p_{min}\), the conditional bound can worsen by a factor of order \(1/p_{min}\).

Long-range interactions require a Lieb–Robinson-type tail estimate rather than strict support.

## 8. Revised DPC/theorem boundary

### Exact theorem

For exact locally indistinguishable codes and trace-preserving compilers whose complete quantum-and-classical backward cone is correctable, the bounded output port is logically constant.

### DPC extension

For approximate codes, quasi-local dynamics, adaptive instruments, and completion limits, a quantitative version holds when:

- causal tails vanish uniformly;
- local indistinguishability error vanishes;
- success probability is bounded below;
- controller communication is included;
- the output algebra and preservation requirement are frozen.

## 9. Decisive falsifier

A genuine falsifier must provide:

1. a growing-distance or vanishing-local-distinguishability family;
2. a fixed output algebra;
3. a complete quantum-and-classical causal graph;
4. a uniformly correctable backward cone;
5. a trace-preserving map, or uniformly nonvanishing heralding probability;
6. output states separated by a uniform positive amount;
7. preservation of the declared logical algebra or instrument type.

Without all seven, the example identifies a changed constructor or weakened output claim.

## 10. Present conclusion

DPC v2 survives only after becoming more precise.

The exact core should be promoted from conjecture to theorem:

> A port cannot reveal logical information absent from its complete backward causal algebra.

The genuinely conjectural frontier is quantitative stability under approximate locality, approximate correction, postselection, and completion.
