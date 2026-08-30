# 1928 — The C8 Rank-Four Center Is a Rank-Three Excess Specialization of a Transverse Seven-Torus

## Source-normal typing

For each labelled occurrence let

\[
q=N_XX+N_yy
\]

be its seven partial-energy forms. Exact calculation over all 288 occurrences gives

\[
\operatorname{rank}(N_X\mid N_y)=7,
\qquad
\operatorname{rank}N_y=4.
\]

Thus the seven divisors are transverse in the complete ((X,y)) normal space. Apparent rank-four nontransversality occurs only after the external directions are specialized.

The labelled relation space

\[
K=\ker N_y^T
\]

has rank three. For any basis matrix (C) of (K),

\[
CN_y=0,
\qquad
B:=CN_X,
\qquad
\operatorname{rank}B=3.
\]

The row space of (B) agrees exactly with every source-representative base ideal in the universal-Jacobian packet after matching labelled cyclic charts.

## Relative-current complex

Before specialization the source boundary value carries the canonical labelled Leray torus

\[
T^7:quad
d\log q_1\wedge\cdots\wedge d\log q_7.
\]

Pullback to the external base (B=0) is an excess intersection. Its canonical algebraic model is the Koszul complex

\[
0\to\Lambda^3K
\xrightarrow{\iota_B}\Lambda^2K
\xrightarrow{\iota_B}K
\xrightarrow{\iota_B}\mathbb Q
\to0,
\]

with chain ranks

\[
(1,3,3,1).
\]

On the associated base grade (B=0), the differential vanishes and the graded object is (Lambda^\bullet K), of total rank eight.

## Cyclic orientation

The source-normalized transverse minors have distribution

\[
144\times(+8),
\qquad
144\times(-8).
\]

These signs coincide with the two occurrence components of Entry 1922. One cyclic step exchanges the components; two steps preserve them.

## Consequence

The required nontransverse local object is not a chamber chosen in a rank-four arrangement. It is the derived specialization of a source-defined transverse seven-dimensional Leray object, retaining a rank-three excess complex.

This constructs the local complex over all 288 occurrences. It does not yet prove independence under all resolutions or compute its pairing with the companion fold.

Allocator claim: `seqclaim-d0d5e08e7dbe124689c1cd12`.

Artifact: `research/benincasa/results/eight-site-rank4-excess-leray-complex.json`.
