# Canonical diagonal death has a prime-stable exact witness DAG

For source candidate 0 of `(10,3)->(12,4)`, exact elimination provenance was
retained as a replayable directed acyclic graph. Over both primes the witness
has:

- 571 closure nodes;
- 161 IBP, 79 K-multiplication, and 331 marked-q relation leaves/nodes;
- 118 target-reduction steps;
- identical relation-index support and dependency topology.

The coefficient digests differ by prime, while the structural skeleton digest
is stable. Replay regenerates the ordered target relations and evaluates each
node as its normalized source relation minus its dependency nodes.

This supplies exact provenance omitted by the earlier zero-residual receipt.
The witness remains dense and pivot-order-dependent; it is not yet a uniform
ambient-degree homotopy.
