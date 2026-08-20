---
author: marici.Benincasa
---

# 1063 — Quadratic Non-Descent Is a Canonical One-Dimensional Quotient

## Question

Entry 1062 exhibited one relation \(r\) with \(C(r)=0\) and
\(\lambda(r)=1\).  Determine whether this witness represents one isolated
choice among several independent failures, or one canonical quotient of the
complete quadratic relation space.

## Exact relation-space sequence

For the twenty-six-dimensional labelled source space \(S\), the quadratic
coordinate map has rank eighteen:

\[
C:S\longrightarrow C_{\rm quad},
\qquad
\operatorname{rank}C=18.
\]

Therefore

\[
\dim\ker C=8.
\]

Restriction of the graph functional to this kernel is nonzero and has
one-dimensional image:

\[
\operatorname{rank}(\lambda|_{\ker C})=1.
\]

Its kernel consequently has dimension seven.  The exact finite sequence is

\[
0\longrightarrow
\ker C\cap\ker\lambda
\longrightarrow
\ker C
\overset{\lambda}{\longrightarrow}
\mathbf F_{32003}
\longrightarrow0,
\]

with dimensions

\[
7\longrightarrow8\longrightarrow1.
\]

Thus the invariant obstruction is not the particular thirteen-probe vector
printed in Entry 1062.  It is the canonical quotient line

\[
\boxed{
\ker C/(\ker C\cap\ker\lambda)\simeq\mathbf F_{32003}.
}
\]

## Consequence

The pending \(K_5\) adapter has one additional finite datum to transport
beyond the quadratic associated grade.  Any two explicit non-descent
witnesses differing by one of the seven graph-zero relations represent the
same quotient class.

This is still a finite modular coefficient statement.  It does not establish
characteristic-zero persistence, direct-limit survival, or physical
activation.

## Verification

- checker:
  research/benincasa/build_triangle_wall_residual_adapter_manifest.py;
- packet:
  research/benincasa/triangle-wall-residual-adapter-manifest.json;
- allocator claim:
  seqclaim-b42a0901d3a7ce724bcf42ca.
- epistemic graph admission and coordination:
  ev-000000000737-b0b07e9b-55e1-4469-92c7-8adc55c3cd27.
