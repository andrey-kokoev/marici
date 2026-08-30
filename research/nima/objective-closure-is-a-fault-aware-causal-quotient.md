# Objective closure is a fault-aware causal quotient

## Result

Redundant record formation is not sufficient for objective or irreversible
closure. A compiled objective record needs four separately sourced properties:

1. **Causal reach:** the record fragment lies inside the propagation region of
   the source distinction.
2. **Readability:** the fragment states are distinguishable above a declared
   threshold.
3. **Fault separation:** the records do not merely replicate one common-mode
   fault, and the admitted checks cover the declared fault model.
4. **Restricted reversibility:** the observer no longer controls the full
   inverse of the global record-forming interaction.

The resulting closure is relative to an accessible algebra. Global microscopic
dynamics may remain reversible even when the reduced observer channel converges
to an idempotent record projection.

## Exact fanout witness

A binary CNOT tree creates \(N\) record qubits in depth

\[
\left\lceil\log_2(N+1)\right\rceil.
\]

For \(N=7\), depth three is both necessary under disjoint two-body layers and
attained by the tree. The two pointer codewords are all zeros and all ones, so
every leaf carries the same classical bit.

This redundancy has two exact blind spots:

- an early common-mode bit flip can change every descendant consistently, so
  all agreement checks still pass;
- a conjugate phase flip changes the global GHZ phase while leaving every
  pointer-basis probability unchanged.

Thus agreement redundancy detects neither all correlated bit faults nor phase
faults.

## Reversibility boundary

The full CNOT network is unitary and has an inverse. An observer retaining
global control can erase the records coherently. The contractive reduced
channel arises only after restricting access to the environmental record
degrees of freedom.

Therefore an apparent arrow of closure requires a declared quotient or access
restriction. Record depth becomes physical time only through a source-derived
locality or clock law. Irreversibility becomes operative only relative to the
controls that have actually become inaccessible.

## Closure cone

A candidate objective record must lie in the intersection of four admissible
regions:

```text
causally reachable
readable
fault-separated
not reversibly erasable by admitted controls
```

Failure of any one condition blocks the objective-record claim while leaving
the others intact.

## Falsifiers

- A fragment outside the light cone falsifies causal reach.
- Pointer overlap above the readability threshold falsifies observation.
- A common-mode codeword flip passing every agreement check falsifies fault
  independence.
- An admitted global inverse falsifies irreversible closure.

