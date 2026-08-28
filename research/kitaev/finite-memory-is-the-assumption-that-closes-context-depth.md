# Finite memory is the assumption that closes context depth

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** When does a finite family of sequential contexts separate reusable constructors?

## 1. No finite-depth separator without a memory bound

Fix any proposed testing depth \(r\). Consider unary-input deterministic transducers.

Machine \(A_r\) outputs \(0\) forever.

Machine \(B_r\) moves through a chain of hidden states and outputs \(0\) for the first \(r\) uses, then outputs \(1\) on use \(r+1\).

Their contextual traces agree through depth \(r\) and differ at depth \(r+1\).

Therefore no fixed finite family of bounded-use contexts is separation-complete for arbitrary finite-memory constructors when the memory size is unbounded.

This is not failure of observation noise. It is an exact representation-class hostile.

## 2. Finite-state representation supplies a bound

Let \(A\) and \(B\) be deterministic finite-state transducers with state sets of sizes \(n_A\) and \(n_B\), sharing a finite input alphabet.

Run them synchronously on the product state space

\[
S_A\times S_B.
\]

If their outputs ever differ, choose a shortest distinguishing input word. Before its final distinguishing transition, no product state can repeat. If a product state repeated, the intervening loop could be removed, contradicting shortestness.

Hence an inequivalent pair has a distinguishing word whose length is at most the number of reachable product states, and in particular no greater than

\[
n_A n_B.
\]

Consequently, agreement on all words through that bound implies behavioral equivalence.

The exact off-by-one convention depends on whether outputs are attached to states or transitions. SCC should store the declared convention rather than hard-code one numerical form.

## 3. Bisimulation is the closure certificate

Define a relation \(R\subseteq S_A\times S_B\). It is a behavioral bisimulation when related states:

1. have equal current outputs;
2. move to related states under every admitted input.

The greatest such relation is a fixed point of the monotone predecessor operator.

The two initial states are behaviorally equivalent exactly when their pair lies in this greatest fixed point.

Thus finite-memory separation closes by the controlled-invariant mechanism:

- the product state space is finite;
- repeated pair states add no new behavioral information;
- the greatest fixed point stabilizes after finitely many eliminations;
- any inequivalence has a bounded shortest witness.

This is stronger than enumerating traces. It explains why longer traces cannot add a new distinction after fixed-point stabilization.

## 4. “First failed” becomes exact

For two represented machines, the first failed rung is the length of a shortest distinguishing word.

It is computed conceptually by breadth-first search in the product transition system until reaching an output-disagreeing pair.

This notion is well typed only after fixing:

- the input generator alphabet;
- the cost assigned to each generator;
- whether parallel, adaptive, reset, and ancillary contexts are admitted;
- the output timing convention;
- the initial-state convention.

Change the context grammar and “first” may change.

## 5. The representation theorem does the explanatory work

Finite-state closure depends on more than the observed traces. It depends on an upper bound on hidden state complexity.

The hard-to-vary explanation is:

1. every admitted reusable constructor has at most \(n\) internal states;
2. every authorized input acts through the declared transition table;
3. the output map is complete for the declared observations;
4. product-state reachability exhausts every sequential comparison;
5. the finite product cannot produce a genuinely new pair after repetition.

Without item 1, the delayed-divergence hostile survives at every depth.

## 6. Relation to the earlier closure mechanisms

This example unifies contextual separation and controlled-invariant closure.

Contextual separation asks whether some admitted word distinguishes inequivalent machines.

Controlled invariance proves that all such words reduce to a bounded search plus a greatest-fixed-point certificate.

So the fourth mechanism is not merely another output coordinate. It is what can terminate the otherwise unbounded tower of distinguishing contexts.

## 7. Quantum and higher-process boundary

The classical theorem is a template, not authority for quantum memory processes.

A quantum analogue must freeze:

- the internal memory dimension;
- the completely positive transition representation;
- allowed ancillas and entanglement;
- adaptive instruments;
- reset authority;
- the process equivalence relation.

One-shot Choi tomography separates memoryless channels. It does not by itself separate reusable devices with hidden memory.

A finite quantum-memory closure theorem would need a representation-specific bound or an operator-space fixed-point argument. It must not be inferred from the classical product-state count.

## 8. SCC certificate

A reusable-constructor termination claim should include:

```json
{
  "process_type": "deterministic_finite_state_transducer",
  "state_bound": {
    "left": "n_A",
    "right": "n_B"
  },
  "context_grammar": {
    "inputs": ["source-authorized generators"],
    "adaptive": false,
    "reset": "declared convention",
    "output_timing": "state | transition"
  },
  "separator_bound": "reachable_product_state_count",
  "closure_certificate": "greatest_bisimulation_fixed_point",
  "first_failure": "shortest_distinguishing_word | null",
  "unbounded_memory_hostile": true
}
```

A claim lacking a state or representation bound must remain open against delayed divergence.

## 9. Falsifiers

1. Two machines within the frozen state bounds agree through the certified depth but differ later.
2. An admitted input transition is absent from the product audit.
3. Reset or adaptivity creates contexts not represented by words in the frozen alphabet.
4. Scalar output equality hides a typed output distinction.
5. The state bound is inferred from observed traces rather than supplied by source theory.
6. Completion permits an unbounded-memory limit while retaining the finite-state certificate.
7. A quantum application imports the classical bound without a quantum representation theorem.

## 10. Present conclusion

A bounded universal separator for reusable constructors is not obtained by choosing a sufficiently large empirical depth.

It is obtained by proving a bound on the hidden realization and then showing that the induced behavioral fixed point stabilizes.

This gives a precise answer to the Deutschian question:

> Longer contexts cease to matter because every possible comparison state has already occurred, not because no longer experiment was attempted.
