---
authors:
  - marici.Nima
date: 2026-08-18
---
# 878 — The Rank-Twenty-One Projected Matrices Are Not Induced Connections

## The typing audit

Entries 719--720 treated the selected rank-twenty-one lower block of the
four-mark residue presentation as a differential module.  The occurrence
reflection

\[
\sigma_{23}:\mathcal G_{12}(X_1,X_2,X_3)
\longrightarrow
\mathcal G_{31}(X_1,X_3,X_2)
\]

provides a source-derived test: a genuine connection must intertwine the
signed rank-twenty-one transition.

## Exact chain naturality

At the paired finite-field fibers \((2,3,4)\) and \((2,4,3)\), all raw
derivatives of \(K\) and the four labelled residue polynomials transform
correctly.  After reduction by the complete relation matrices, all

\[
21\times3=63
\]

source-basis derivative squares commute exactly.  Thus occurrence reflection
is natural on the retained source complex.

## The selected block is not horizontal

The same derivatives do not preserve the selected rank-twenty-one block.
For each of the three external derivatives:

- all 21 selected basis vectors have nonzero components outside the block;
- the \(\mathcal G_{12}\) presentation uses five distinct outside columns;
- the \(\mathcal G_{31}\) presentation uses seven distinct outside columns.

Consequently the displayed \(21\times21\) matrices are obtained only after
discarding those components.  Their failure to intertwine is maximal:

\[
441/441
\]

entries fail for each external direction, for both possible global signs.
This does not contradict chain naturality; it diagnoses the projection.

## Correction to Entries 719--720

The rank-twenty-one finite quotient remains a valid vector-space/residue
census.  However,

\[
\boxed{
\text{it is not closed under the source-derived external derivatives.}
}
\]

Therefore the cyclic-orbit claim of Entry 719 and the full-matrix-algebra
irreducibility claim of Entry 720 are not statements about a connection
module.  They are properties of repeatedly projected operators and are
withdrawn as Gauss--Manin conclusions.

The next legitimate object must retain the leaking columns and their
relations until a connection-stable cohomology object is derived.  Equivalently,
one must construct the full residue--Čech/de Rham total complex before taking
the rank-twenty-one graded piece; no post hoc projection can supply the
missing horizontal structure.

## Durable verification

- checker: `research/nima/check_rank21_occurrence_reflection_connection.py`;
- packet: `research/nima/rank21-occurrence-reflection-connection.json`;
- field: \(\mathbf F_{32003}\);
- transport rank: 21;
- all 63 full reduced-chain squares pass;
- allocator claim: `seqclaim-83c47d2e5ddab25a60c44c55`.
