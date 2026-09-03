# Checkpointed provenance replay

Problem: avoid simultaneously expanding every source-combination vector while
retaining replayable provenance.

Bold conjecture: an acyclic elimination log plus pivot checkpoints reproduces
certificates and exposes corruption.

Rivals: expanded vectors; rank-only checkpoints; and operation logs without
replay digests.

Risky consequences: every pivot and null row must replay, checkpoint digests
must be stable, and changing one recorded reduction coefficient must leave a
nonzero residual.

Strongest falsification attempt: a ten-row triangular presentation over the
prime 101 produced eight pivots, two null rows, ten DAG nodes, thirteen
reduction edges, and two checkpoint digests. All certificates replayed. A
single corrupted edge left a residual with eight nonzero entries.

Disposition: retained for the bounded DAG prototype. Expanded provenance need
not be retained simultaneously. Storage scales with reduction operations, which
this test does not bound at full scale, and no integral generator was
constructed. The next test asks whether stable DAG certificates at two good
primes reconstruct one labelled integral candidate and rejects an incompatible
certificate.
