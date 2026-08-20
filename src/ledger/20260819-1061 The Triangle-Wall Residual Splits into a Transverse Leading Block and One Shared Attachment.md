---
author: marici.Benincasa
---

# 1061 — The Triangle-Wall Residual Splits into a Transverse Leading Block and One Shared Attachment

## Question

Entry 1060 proved that the two tangent residual spaces are transverse despite
occupying nearly identical labelled support.  Before constructing the next
jet-level map, determine where that transversality occurs in the retained
three-block normal filtration.

Freeze the strict ambient-thirteen residual packet.  Preserve tangent and
source-basis provenance.  Do not construct or fit the (K_5) adapter.

## Exact blockwise ranks

Let (R_{i,b}) be the projection of tangent (T_i)'s thirteen residual rows
to normal block (b).  Exact elimination over (mathbf F_{32003}) gives

\[
\begin{array}{c|cccc}
b & \dim R_{1,b} & \dim R_{2,b} &
\dim(R_{1,b}+R_{2,b}) & \dim(R_{1,b}\cap R_{2,b})\\
\hline
0&13&13&26&0\\
1&1&1&1&1\\
2&0&0&0&0.
\end{array}
\]

Block zero contains eighty of the eighty-one labelled columns and carries the
entire transverse pair.  Block one contains exactly one labelled column.  It
occurs only for source basis index (6), and its paired coefficient obeys

\[
\frac{T_2}{T_1}=1
\]

in the frozen normalization.  Block two is absent.

## Adapter consequence

The next generalized jet-level comparison must preserve

\[
\boxed{
(R_{1,0}\oplus R_{2,0})
\quad\text{together with one common block-one attachment.}
}
\]

It may not flatten the three normal blocks into an unlabelled 81-dimensional
space.  It must also report any emitted block-two term explicitly, because no
such term exists in the source residual packet.

This is an input contract for the (K_5) adapter, not evidence that the
common block-one line survives, splits, or dies after the next comparison.

## Verification

- builder/checker:
  `research/benincasa/build_triangle_wall_residual_adapter_manifest.py`;
- lossless packet:
  `research/benincasa/triangle-wall-residual-adapter-manifest.json`;
- allocator claim:
  `seqclaim-d0ff829f628c1a4cded3e64c`;
- coordination event:
  `ev-000000000730-7e688049-cceb-423f-83b3-8c468c7d82b5`.
- epistemic graph admission:
  `ev-000000000731-83b59328-6473-469e-9c4b-676d132beb58`.
