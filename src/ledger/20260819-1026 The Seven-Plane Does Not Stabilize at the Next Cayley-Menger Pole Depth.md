# The Seven-Plane Does Not Stabilize at the Next Cayley--Menger Pole Depth

## First honest pole-depth extension

Entry 1020 isolates the remaining gate for the canonically connected
exact-valuation object: stabilization under increasing pole depth.

The depth-two triangle-wall presentation was extended only in the
Cayley--Menger pole direction,

\[
k_{\max}:2\longrightarrow3,
\]

while retaining marked-divisor pole depth two, ambient relation degree ten,
and the same seven exact normal samples.  This is an honest nested source
window: the old ambient columns and every old labelled relation occur inside
the new presentation.

The extension has

\[
15360\ \text{columns},
\qquad
20684\ \text{raw relations}.
\]

## Exact rank result

The complete sparse ranks over \(\mathbf F_{32003}\) are

\[
R_0=8448,
\qquad
R_1=16903,
\qquad
R_2=25371.
\]

They give

\[
n_1=7,
\qquad
\boxed{n_2=13}.
\]

At depth two the corresponding ranks were

\[
n_1=5,
\qquad
n_2=7.
\]

Therefore

\[
\boxed{
\dim E_2(C^{k\le2})=7,
\qquad
\dim E_2(C^{k\le3})=13.
}
\]

The exact-valuation-two sector gains six dimensions at the first
Cayley--Menger pole-depth extension.

## Family typing

The depth-three cumulative family filtration is

\[
R_0=(396,3014,5526,6958,7766,8218,8448),
\]

\[
n_1=(0,12,12,12,12,12,7),
\]

\[
n_2=(0,0,0,0,0,0,13).
\]

As at depth two, the quadratic exact-valuation grade appears only when the
complete five-mark packet is present.  The new six dimensions are therefore
not attributable to an isolated new carrier or one marked divisor; they are
additional collective marked-incidence coefficient data exposed by the
larger principal-pole window.

## Consequence and boundary

The depth-two seven-plane is not a stabilized representative of the
connection-stable direct-limit object:

\[
\boxed{
7\not\simeq13.
}
\]

This falsifies the simplest proposed identification of the depth-two
seven-plane with the generic rank-seven algebraic kernel.

It does not yet determine the dimension of the eventual colimit.  Although
the source presentations are nested, exact valuation is a subquotient; the
induced map

\[
E_2(C^{k\le2})\longrightarrow E_2(C^{k\le3})
\]

may have nontrivial kernel, and later stages may introduce further classes
or relations.  The next calculation must compute this map itself—its rank,
kernel, and cokernel—rather than compare dimensions alone.

## Durable verification

- generalized source presentation:
  `research/benincasa/g12_g31_residue_chart_transition.py`;
- exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- sparse rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- result packet:
  `research/nima/triangle-wall-kdepth3-rank.json`;
- allocator claim: `seqclaim-70cf6ffba5723b3f09ba3bee`.
