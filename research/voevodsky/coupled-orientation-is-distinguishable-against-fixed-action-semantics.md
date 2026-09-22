# Coupled orientation is distinguishable against fixed action semantics

## Frozen test

Compare each of the 638 actual coupled states with the same vertex in the logical opposite graph. Reverse every transition edge while retaining its action label and each vertex's operational output: typed source corner, received value and issued value.

The present output is identical by construction. Ask whether some continuation word produces different sets of terminal outputs, including an empty set for rejection. The opposite graph may be nondeterministic, so the test uses successor sets rather than choosing an arbitrary predecessor.

This freezes an orientation reference: source-event labels, acquisition/delivery meanings, and the interpretation of source masks remain fixed. It is a logical comparison, not a claim that the opposite graph is an admitted physical protocol.

## Result

All 638 states admit a separating continuation. Every shortest witness has length one. Each witness is independently replayed after search. No state has equal forward/opposite continuation behavior under this contract.

For example, at state 0 the source mask is 3. Event source(3,0) is admitted forward, reaching mask 11; the same label has no incoming predecessor edge at that vertex and hence is rejected in the opposite graph.

The source workflow itself carries the asymmetry: adding an unused event advances the fixed mask ordering. Reversing the graph while holding that interpretation fixed exposes the orientation immediately. This confirms the fixed-reference claim but does not supply evidence for an intrinsic orientation independent of observer transport.

## Structural boundary

There are two different questions:

1. With the observer's labels and source interpretation held fixed, does reversal alter continuation behavior? This finite test answers yes at every state.
2. After source, observer, labels and outputs are transported together, can an internal observation distinguish the orientations? This test does not answer that question. The algebraic pullback equality preserves individual readings; extending that equality to the full coupled protocol requires an independently specified transport of acquisition and evidence constructors.

Thus the current direction reference lies in the retained composition/admission rules, not in an instantaneous scalar reading. The stronger relational-duality question remains open.

## Reproduction

    python research/voevodsky/checkers/check_coupled_orientation_distinguishability.py

Artifacts:

- `results/coupled-orientation-contract.json`
- `results/coupled-orientation-distinguishability.json`
