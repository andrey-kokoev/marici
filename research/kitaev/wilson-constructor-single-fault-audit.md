# Wilson constructors: a single-fault propagation audit

Status: exact Pauli-propagation theorem for the declared fault locations and
loop lengths `2 <= L <= 8`.

## Frozen circuits and fault location

The coherent mobile protocol uses one pointer initialized in `|0>`, followed
by the ordered gates `CNOT(data_e -> pointer)` around the Wilson support and a
pointer `Z` measurement.  The fault set is one pointer Pauli inserted
immediately after a declared CNOT.

The refined parallel protocol uses one pointer per edge, one data--pointer
CNOT each, individual pointer measurement, and classical parity.  Only
post-coupling pointer faults are compared here.

## Mobile propagation

Forward CNOT propagation gives

\[
Z_a\longmapsto Z_eZ_a
\]

at every later data-control gate.  A pointer `Z` fault after gate `k`
therefore deposits `Z` on the remaining `L-k` edge suffix.  Every nonempty
proper suffix is an open chain with two star endpoints.  Across all checked
sizes the maximum correlated weight is `L-1`, strictly below code distance
`L`, so every nonzero propagated damage is detectable and not itself logical.
The fault after the final gate propagates no data damage.

A pointer `X` fault does not fan out through later CNOTs but flips the final
pointer `Z` record.  A `Y` fault combines the suffix damage and record flip.

## Parallel refined propagation

A post-coupling pointer fault has no later data gate through which to fan out.
An `X` fault flips one fine record and hence the reported parity; a `Z` fault
does neither at the frozen location.  This does not make the refined protocol
superior: even without faults its individual edge measurement kills star
coherence and is not the QND Wilson instrument.

Thus fault fanout and ideal backaction are independent comparison axes.  A
protocol cannot be ranked by maximum propagated weight while ignoring that
it implements a different instrument in the fault-free limit.

## Falsifiers and limits

The result fails if a mobile post-gate `Z` fault produces a logical cycle or
anything other than a two-endpoint proper suffix, or if a parallel
post-coupling fault fans into data without a later interaction.

Excluded locations include preparation faults, faults during a two-qubit
gate, measurement faults beyond Pauli record flips, multiple faults, and a
verified Shor/cat protocol.  Those require a larger circuit contract.
