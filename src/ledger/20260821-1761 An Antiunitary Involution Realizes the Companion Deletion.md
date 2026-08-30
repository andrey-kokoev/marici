# 1761 — An Antiunitary Involution Realizes the Companion Deletion

## Symmetry candidate

Let \(K\) denote complex conjugation in the labelled rank-two measurement
frame and let

\[
Z=\operatorname{diag}(1,-1).
\]

The antiunitary involution

\[
\Theta=ZK
\]

acts on Hermitian Pauli directions by

\[
\boxed{
(I,X,Y,Z)\longmapsto(I,-X,Y,Z).
}
\]

Therefore

\[
\operatorname{Fix}(\Theta)=\langle I,Y,Z\rangle.
\]

## Effect on the tomographic packet

The real-superposition effect is proportional to

\[
E_x=I+X.
\]

Its invariant projection is

\[
E_x+\Theta(E_x)=2I,
\]

so its independent \(X\) direction disappears into the already retained
diagonal sector.

The imaginary-superposition effect

\[
E_y=I+Y
\]

is fixed:

\[
\Theta(E_y)=E_y.
\]

Thus the invariant packet retains:

- both diagonal directions \(I,Z\);
- the imaginary-superposition direction \(Y\);
- no independent real-superposition direction \(X\).

This is exactly the companion deletion assumed in Entry 1760.

## Narrow result

A legitimate involutive symmetry can produce Entry 1760's rank-one filtered
extension without an arbitrary label deletion. The symmetry is antiunitary,
not an ordinary permutation of scalar effects.

The physical scope remains conditional. We have constructed and verified
the symmetry on the abstract rank-two coefficient/readout system, but have
not derived \(\Theta=ZK\) from the frozen cosmological source.

Hence:

- symmetry realization of the deletion: established;
- induced rank-one extension: Entry 1760;
- cosmological source provenance of \(\Theta\): open;
- new carrier stratum: absent.

## Durable artifacts

- research/benincasa/checkers/antiunitary_companion_deletion.rs
- research/benincasa/results/antiunitary-companion-deletion.json
- research/benincasa/antiunitary-companion-deletion.md

## Next falsifier

Test whether the physical reality/Schwarz-reflection structure of a
source-defined cosmological coefficient block induces \(ZK\), plain \(K\),
or neither on its rank-two nearby-cycle/readout frame. Only the first case
activates the filtered extension of Entry 1760.
