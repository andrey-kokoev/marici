# 2766 — Relation-Cokernel Vanishing Does Not Yet Define an Euler Nullhomotopy

## Correction to Entry 2764

Entry 2764 established two facts:

1. the mixed Euler-coherence commutators are nonzero in the finite quotient;
2. their classes vanish after quotienting by the image of the complete moving marked-pole relation map.

The entry called this “homotopy-flatness.” That wording is too strong. A chain homotopy requires a typed source-labelled preimage, not only membership in an unlabelled row span.

## Finite ambiguity audit

At each frozen point, the aligned ambient-14 containment witness processes 9280 relation generators and has derived span rank 2524. Therefore its kernel has dimension at least

\[
9280-2524=6756.
\]

Consequently every displayed commutator preimage belongs to an affine family with at least 6756 homogeneous directions. Gaussian elimination can choose a representative, but that solver section is not source authority.

The stable repetition of the number 6756 across three points does not remove this ambiguity and does not define a canonical subspace splitting.

## Correct narrow statement

The established theorem is

\[
[\Theta_{jk}]=0
\quad\text{in the cokernel of the moving-relation map.}
\]

The following remain unproved:

- existence of a source-labelled nullhomotopy constructor;
- independence from relation presentation;
- compatibility with the three-chart transition packet;
- fourth-order coherence among the three nullhomotopies.

No new carrier or coefficient object is indicated. The missing datum is a higher map in the relation resolution.

## Artifacts

- `research/benincasa/check_rank26_nullhomotopy_typing.py`
- `research/benincasa/rank26-nullhomotopy-typing.json`

## Next falsifier

Derive the first syzygy differential of the complete labelled marked-pole relation map from the source multiplication identities. Test whether the three Euler commutators lie in its functorial image. Do not choose a row-space section.
