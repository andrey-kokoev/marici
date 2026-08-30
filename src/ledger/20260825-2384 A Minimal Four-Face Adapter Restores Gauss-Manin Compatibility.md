---
author: marici.Benincasa
date: 2026-08-25
---

# 2384 — A Minimal Four-Face Adapter Restores the (z)-Directional Gauss--Manin Comparison

## Scope correction

The original heading omitted that the certified comparison used only
\(\partial_z+A_z\). A subsequent axis-resolved audit found residual cone ranks
\(101\) and \(104\) for \(\partial_x+A_x\) and \(\partial_y+A_y\), respectively,
in the same target. Therefore this entry establishes the minimal adapter only
for the tested \(z\)-direction. It does **not** establish full Gauss--Manin
compatibility. The broader wording is withdrawn.

## Question

Which source-derived finite-presentation faces must be enlarged so that the
ambient-eight exact relation complex maps horizontally in the tested
\(z\)-direction into a larger labelled complex?

Sequence claim: seqclaim-2a0ceb337b67525b045e5fe7.

## Occurrence-resolved adapter cube

The target presentation was generalized from one uniform marked-pole depth to
the labelled vector

\[
(d_{g_1},d_{g_2},d_{g_3},d_{g_{23}},d_{g_{31}}).
\]

Every vertex is derived by literal label inclusion. The complete target exact
image is regenerated at that vertex, and every source relation is acted on by
the true target operator (\partial_z+A_z). No quotient is selected from the
observed residual.

With polynomial ambient fourteen, the one-face ranks are

\[
\begin{array}{c|rrrrrr}
\text{enlarged face}&\varnothing&K&g_1&g_2&g_3&g_{23}&g_{31}\\
\hline
\operatorname{rank}\operatorname{Cone}_{\nabla}
&2349&1724&1854&2693&2718&2378&2379.
\end{array}
\]

The nonmonotonic values show that these are interacting Čech faces, not
independent summands.

## Joint closure

Increasing the three global marked poles together gives rank (412). Increasing
the (K)-depth together with all three global marked poles gives

\[
\boxed{
\operatorname{rank}\operatorname{Cone}_{\nabla}=0.
}
\]

The closing target is

\[
\boxed{
\begin{aligned}
D&\longmapsto D+4,\\
d_K&\longmapsto d_K+1,\\
(d_{g_1},d_{g_2},d_{g_3})
&\longmapsto(d_{g_1}+1,d_{g_2}+1,d_{g_3}+1),\\
(d_{g_{23}},d_{g_{31}})&\longmapsto(d_{g_{23}},d_{g_{31}}).
\end{aligned}}
\]

The polynomial shift by four is source-derived from the quartic fiber degree
of (K).

## Minimality in the declared cube

Every codimension-one deletion fails:

\[
\begin{array}{c|c}
\text{deleted requirement}&\text{remaining cone rank}\\
\hline
K&412\\
g_1&925\\
g_2&732\\
g_3&667\\
D+4\text{ replaced by }D+2&3032.
\end{array}
\]

The zero persists at polynomial shifts (D+4) and (D+6), and replicates after
simultaneously changing the prime and kinematic point. Thus the four-face
adapter is necessary and sufficient within the frozen occurrence-resolved
face cube.

## Narrow result

\[
\boxed{
\text{the missing }z\text{-directional Gauss--Manin coherence is supplied by the joint}
\text{ quartic-}K\text{/three-global-mark adapter.}
}
\]

The pair marks (g_{23},g_{31}) are not required for this exact-sector
comparison. Extending them alone or together increases rather than removes the
cone, confirming that they belong to a different relative layer.

## Architectural meaning

The corrected finite object is not a single cutoff quotient. It is a port
adapter

\[
C_{D,d_K,\mathbf d_q}
\longrightarrow
C_{D+4,d_K+1,\mathbf d_q+(1,1,1,0,0)}
\]

whose exact image is strictly compatible with \(z\)-directional transport. This is
the first source-derived repair of the rank-growth problem; no cells were
added after inspecting a target cohomology class.

## Classification

- Carrier incidence: unchanged;
- required boundary ports: quartic polynomial face, (K)-face, and the three
  global marked-pole occurrences;
- pair-mark faces: not part of this adapter;
- \(z\)-directional commutator cone: zero;
- \(x\)- and \(y\)-directional cone ranks in this target: \(101\) and \(104\);
- physical observer rank: still uncomputed in the adapted complex;
- new Carrier support: unsupported.

## Durable verification

- research/benincasa/check_cutoff_inclusion_gauss_manin_adapter.py;
- research/benincasa/check_minimal_four_face_gauss_manin_adapter.py;
- research/benincasa/minimal-four-face-gauss-manin-adapter.json.

## Next falsifier

Recompute the true covariant source-jet Hilbert function in the four-face
adapted target and test whether it stabilizes. Then transport the frozen score,
polarization, marked-wall, and relative-cycle ports through the same adapter.
Any rank loss must be classified before aggregation as route loss or as a
nonzero labelled packet in the physical summation kernel.
