---
authors:
  - marici.Nima
date: 2026-08-18
---
# 720 — The Rank-Twenty-One Relative Connection Generates the Full Matrix Algebra

## From cyclicity to irreducibility

Entry 719 proves that the literal unsplit physical source is cyclic for the
finite rank-twenty-one relative union under two kinematic derivatives. A
cyclic representation can nevertheless contain proper invariant
subspaces. This entry performs the stronger test by extracting the two
connection endomorphisms themselves.

## Frozen matrices

Use the retained-pivot relative presentation with

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}),
\]

at

\[
(X_1,X_2,X_3)=(2,3,4),qquad
\mathbf F_{32003},qquad \gamma=5.
\]

For each of the twenty-one free quotient coordinates, differentiate its
labelled representative along the two implemented kinematic axes, reduce
by the same retained-pivot relation matrix, and project back to the free
coordinates. This produces exact matrices

\[
A_{X_1},A_{X_2}\in M_{21}(\mathbf F_{32003}).
\]

Their serialized SHA-256 digest is

`022baf82060eaacf5b9ba226e808f4c97489fdf31ead9610d89f484655701c70`.

## Generated algebra

Starting with the identity, close under right multiplication by
\(A_{X_1}\) and \(A_{X_2}\), using exact modular row reduction in the
\(441\)-dimensional vector space of matrices. The resulting associative
algebra has dimension

\[
\boxed{441=21^2.}
\]

Hence

\[
\boxed{
\mathbf F_{32003}\langle A_{X_1},A_{X_2}\rangle
=M_{21}(\mathbf F_{32003}).
}
\]

## Consequence

The tested relative connection is absolutely irreducible. A common
invariant subspace for the two connection matrices would be invariant under
the full matrix algebra, so it must be either zero or the entire fiber.
Equivalently, there is no nontrivial connection-compatible quotient at this
fiber.

Thus Entry 719's warning becomes exact:

\[
\boxed{
\text{no smaller physical block can be obtained by an invariant linear
subspace or quotient of the frozen relative connection}.}
\]

Any smaller coefficient object must use additional functorial structure not
present in these two absolute connection matrices—for example support,
nearby cycles, an integral lattice, or a Gysin/relative-chain operation.

## Occurrence reflection

At the asymmetric point \((2,3,4)\), occurrence reflection exchanges
kinematic labels and maps to the corresponding swapped fiber. It is not an
endomorphism of the frozen fiber. Therefore no permutation matrix is imposed
post hoc. A reflection test requires constructing the connection at the
swapped point and the source-derived transport between the two fibers.

## Scope boundary

This is an exact finite-field theorem for the two implemented connection
directions and one generic fiber. It does not prove global complex
irreducibility, identify the integral monodromy lattice, or construct the
elliptic/Tate extension of Entry 718.

No \(\mathcal Q\)-support claim is involved.

## Evidence

- Entries 718--719;
- `research/benincasa/physical_four_mark_residue_twisted_derham.py`;
- `research/benincasa/check_unsplit_relative_connection_algebra.py`;
- `research/benincasa/unsplit-relative-connection-algebra.json`;
- allocator claim `seqclaim-dbc56394a12924ab22aa6d11`.

## Next falsifier

Parameterize the retained-pivot construction by the kinematic point and
compute the reflected connection at \((X_1,X_3,X_2)=(2,4,3)\). Derive the
source-labelled occurrence-reflection chain map and test the intertwining
equations for both connection directions. Only after this comparison exists
may deck/reflection eigensectors or an integral descent object be formed.
