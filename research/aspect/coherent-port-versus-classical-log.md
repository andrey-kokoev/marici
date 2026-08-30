# A complete classical environment log is not a coherent port

## Which-path logging can preserve every event and erase the recoverable phase

After complete transfer into an environment qubit, compare the orthogonal input
states `|+>` and `|->`. Coherent access to the environment distinguishes them
perfectly and permits the inverse dilation.

Now measure that environment in the computational basis and retain every outcome.
Both inputs produce the same half-zero, half-one distribution. Their complete
classical records are identical. The measurement preserves population-event
provenance but removes the relative phase that distinguished the states.

This is stronger than ordinary loss: nothing was omitted from the chosen log.
The defect is that the instrument converted a coherent port into an
entanglement-breaking classical channel before the future question was known.

## Changing basis moves rather than removes the quotient

An `X`-basis log distinguishes `|+>` from `|->` perfectly, but no fixed projective
measurement preserves every possible unknown input. Informationally complete
tomography can identify a repeatedly prepared state statistically; it still
does not preserve the individual quantum system or supply a physical single-shot
inverse to the measurement channel.

Thus port typing needs an access modality:

- coherent and actuable;
- coherently stored but not yet measured;
- measured with basis and outcome retained;
- coarse-grained classical record;
- discarded.

Future-context equivalence depends on when the measurement basis becomes fixed.
A record sufficient for one later question can quotient the answer to another.

## Optical instrument

Use a path-encoded environment mode carrying transferred polarization phase.
In one arm, preserve it coherently and apply the inverse interferometer. In the
other, perform which-path detection and retain perfect time tags. Probe with
`|+>` and `|->`: the coherent arm recovers both, while the computational log has
identical statistics. A delayed basis choice directly tests which future
questions remain available.

## Claim boundary

The checker treats ideal qubits and projective computational-basis logging.
Weak measurement, quantum memories, adaptive collective measurements, and
finite-sample tomography remain open.

## Verification

```text
python research/aspect/checkers/check_coherent_port_versus_classical_log.py
```
