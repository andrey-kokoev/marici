# Residue Resolution Is Not Canonically LIFO

Consider two legal paths meeting in one coherence cell:

\[
\text{restrict}\to\text{Gysin}\to\alpha,
\qquad
\text{transport}\to\text{specialize}\to\alpha.
\]

The coherence \(\alpha\) depends on both branches. The dependency graph has six
valid linear extensions. Reversing any one gives a valid LIFO repair order,
but no extension is canonical.

Therefore:

- nested residues may unwind as a stack;
- a chosen scheduler may linearize any acyclic residue graph;
- the invariant structure is the dependency partial order;
- coherence cells record joins between branches.

In programmer terms, \(R\) is closer to a structured-concurrency task graph
with compensations than to one exception stack.

Sequence claim: seqclaim-e7b359f6e33a09a704776c81.
