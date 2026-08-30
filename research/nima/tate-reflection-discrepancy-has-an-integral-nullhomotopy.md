# The Tate reflection discrepancy has an integral nullhomotopy

Date: 2026-08-23

## Problem stated without the octahedral answer

Take the six common labelled sector objects and the union of two independently
frozen legal incidence systems:

- the cross-sheet conductor edges;
- the same-sheet literal short-facet edges.

Let \(S_{\rm src}\) and \(S_{\rm lit}\) be the two frozen reflection chain
maps. Ask whether their discrepancy admits an integral chain homotopy

\[
S_{\rm lit}-S_{\rm src}=dH+Hd
\]

whose degree-zero components use only legal support edges and whose relative
top is primitive. No octahedron, face count, or pure/mixed split is assumed.

## Derived completion

The union graph has six vertices and twelve legal edges. Its clique
completion derives exactly eight triangular 2-cells. The resulting boundary
matrix has rank seven and a one-dimensional primitive integral kernel, which
derives one relative 3-cell.

Thus the chain ranks are

\[
\operatorname{rank}d_1=5,
\qquad
\operatorname{rank}d_2=7,
\qquad
\operatorname{rank}d_3=1.
\]

Exact rational elimination, followed by integral-denominator checks, solves
all chain-homotopy equations. The forced degree-zero homotopy uses six legal
edges. In the initial zero-parameter gauge, the higher maps have 20 and 2
nonzero entries. The degree-one solution has twelve affine parameters.

A subsequent joint solve, rather than sequential gauge fixing, shows that
an integral representative exists with the top homotopy (H_2) identically
zero. Thus the two nonzero (H_2) entries in the initial representative are
gauge artefacts. The primitive relative interior controls ambiguity of
representatives; it is not required by the reflection nullhomotopy itself.

## Meaning

The earlier octahedral architecture is now an output:

\[
\boxed{
\text{frozen discrepancy diagrams}
\Longrightarrow
8\text{ triangular comparison cells}
+1\text{ primitive relative interior}.
}
\]

This is a carrier-level nullhomotopy theorem. It does not establish that the
same homotopy lifts through occurrence lines, normal circles, conductor Tor,
Čech localization, or proper/extraordinary variance. That loaded lift is now
the genuine next falsifier rather than a predetermined architectural task.

Evidence:

- `research/nima/checkers/check_tate_reflection_discrepancy_homotopy.py`.
- Entries 251, 253, 255--258, and 324.
