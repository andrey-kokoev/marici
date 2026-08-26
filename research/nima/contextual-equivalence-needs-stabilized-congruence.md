# Contextual equivalence needs stabilized congruence

## Problem

A context-indexed capability coalgebra can make two source-task presentations observationally identical now and distinguish them after a later authorized continuation. When is quotienting them legitimate?

## Exact criterion

Let the authorized context generators act as transitions on a finite presentation space, with observable capability as the output. Start from the partition induced by current outputs. Repeatedly refine it by the output and the successor classes under every authorized generator.

The stable partition is the greatest behavioral equivalence compatible with both readout and continuation. A quotient is lawful exactly when its kernel lies inside this stable equivalence. Equivalently, the proposed quotient must be a congruence for the entire authorized context action.

## Finite-horizon hostile

For every tested horizon (k), construct two source presentations whose outputs agree on all words of length at most (k). One additional application of the same authorized generator reaches outputs 0 and 1. Thus no fixed finite observation horizon establishes full contextual equivalence.

The checker constructs these machines for horizons zero through six. In every case:

- the bounded suite identifies the two sources;
- the word of length (k+1) separates them;
- partition refinement over the full transition graph separates their initial states.

The hostile is not an argument against finite verification. It identifies what finite verification must prove: stabilization on a closed finite state presentation, not merely agreement on an enumerated prefix of future experiments.

## Consequence

Source and task are not necessarily irreducible object fields. Nor are they disposable presentation labels. They may be quotiented only to the resolution preserved by the complete authorized context law.

For finite systems, stabilized partition refinement supplies a complete certificate. For infinite systems, an independent closure theorem, coinductive bisimulation, or finite generating presentation is required. Without one of those, claims of source reconstruction or source erasure remain horizon-relative.

## Relation to ordered forgetting

The same principle governs forgetting ports. Commuting continuation maps license cubical quotients. Noncommuting maps retain order. In both cases, equality of present scalar readouts is weaker than congruence of future behavior.
