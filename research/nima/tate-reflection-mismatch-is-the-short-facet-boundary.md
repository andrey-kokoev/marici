# The Tate reflection mismatch is the short-facet boundary

Date: 2026-08-23

The source and literal sector reflections differ:

\[
s_{\rm src}(i)=1-i,
\qquad
s_{\rm lit}(i)=5-i
\pmod 6.
\]

For every sector, join these two images by the oriented edge

\[
s_{\rm src}(i)\longrightarrow s_{\rm lit}(i).
\]

Exact enumeration gives the six distinct edges

\[
\{0,2\},\{2,4\},\{4,0\}
\sqcup
\{1,3\},\{3,5\},\{5,1\}.
\]

These are exactly Entry 253's six same-sheet literal short-facet edges. With
their induced orientations they form two closed triangles:

\[
0\to4\to2\to0,
\qquad
1\to5\to3\to1.
\]

They are precisely the boundaries of the two pure-sheet faces in Entry 255's
octahedral conductor carrier. Therefore the failure of strict reflection is
not an unexplained support defect. It is the boundary of a canonical
carrier-level homotopy supplied by those two faces.

The interpretation is now:

- the two pure-sheet octahedral faces provide the reflection comparison;
- the six mixed faces compare it with the cross-sheet dP6/Rees transport;
- the full eight-face fundamental boundary is the candidate global
  Beck--Chevalley coherence;
- Entry 257's interior class supplies its primitive odd top normalization.

What remains unproved is loaded realization: the eight carrier faces must be
sent to occurrence-, normal-, Tor-, and Čech-resolved transformations in one
mixed-variance six-functor kernel.

Evidence:

- `research/nima/checkers/check_tate_reflection_mismatch_short_facet_boundary.py`.
- Entries 251, 253, 255, 257, and 324.
