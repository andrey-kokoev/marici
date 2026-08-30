# Stable Carrier data is a record-control formal concept

## Result

The commutant Galois connection identifies a precise sense in which stable
Carrier data is closure-like. A closed interface object is not merely a stored
record algebra \(R\). It is a pair \((R,M)\) satisfying

\[
R=M',
\qquad
M=R'.
\]

Such a pair is a formal concept of the record/control polarity. The record side
contains exactly the sharp information compatible with the control side; the
control side contains exactly the operations compatible with the record side.

The induced closure operators are

\[
R\longmapsto R'',
\qquad
M\longmapsto M''.
\]

They are extensive, monotone, and idempotent on the admitted operator-algebra
carrier. Fixed points are stable record/control interface types.

## Exact two-dimensional concept chain

For the scalar, diagonal, and full subalgebras of \(M_2\), the closed pairs are:

```text
scalar records   ↔ full controls
diagonal records ↔ diagonal controls
full records     ↔ scalar controls
```

Increasing record sharpness reverses the inclusion order on controls. The
middle object is self-dual. Each pair is recovered after two commutant steps.

## Meaning for Carrier

This supports a constrained version of the conjecture that Carrier data is a
closure:

> Authority-bearing operational data should be represented by a source-rooted
> fixed point of an admitted record/control polarity, together with its proof
> DAG and operational profile.

It does not imply that every byte string is mathematically a double commutant.
The statement applies where a shared operator-algebra carrier and a declared
nondisturbance relation have been constructed.

The data object therefore includes both what has been fixed and which future
transformations remain legal. Two equal byte strings can represent different
formal concepts when their compatible control algebras or authority roots
differ.

## Cross-sector reading

- In quantum control, the commutant is literal.
- In classical identification, the analogue may be an observable/indistinguishability
  polarity rather than a noncommutative commutant.
- In completion problems, a finite closed pair may still fail the separate
  completion-stability gate.

## Falsifier

A claimed closed Carrier object is rejected if its declared record algebra and
control algebra are not mutual commutants, or if the pair is compatible but its
source-rooted proof DAG is missing. Compatibility remains distinct from
authority.

