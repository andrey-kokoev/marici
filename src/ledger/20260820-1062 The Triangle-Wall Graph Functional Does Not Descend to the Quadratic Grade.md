---
author: marici.Benincasa
---

# 1062 — The Triangle-Wall Graph Functional Does Not Descend to the Quadratic Grade

## Question

Entry 1061 retyped the sole block-one residual coordinate as the graph of a
linear functional on the transverse block-zero module.  Determine whether
this functional is already determined by Entry 1060's eighteen-dimensional
quadratic-coordinate image.

Freeze the twenty-six labelled source rows and their block-one values.  Do
not construct the pending \(K_5\) target map.

## Exact augmentation test

Let

\[
C:R_{1,0}\oplus R_{2,0}\longrightarrow C_{\rm quad}
\]

be the frozen quadratic-coordinate map, and let

\[
\lambda:R_{1,0}\oplus R_{2,0}\longrightarrow\mathbf F_{32003}
\]

be the block-one graph functional.  Exact sparse elimination gives

\[
\operatorname{rank}C=18,
\]

while adjoining \(\lambda\) gives

\[
\boxed{
\operatorname{rank}(C,\lambda)=19.
}
\]

Therefore no functional \(\bar\lambda\) on the quadratic image satisfies

\[
\lambda=\bar\lambda\circ C.
\]

Equivalently, the tangentwise functionals disagree on the
eight-dimensional overlap of the two quadratic-coordinate subspaces.

The checker also exports a normalized thirteen-probe relation \(r\), mixing
both tangents, for which

\[
C(r)=0,
\qquad
\lambda(r)=1.
\]

This supplies a concrete regression vector for the generalized adapter,
rather than only a rank discrepancy.

## Narrow conclusion

\[
\boxed{
\text{the graph functional is residual-module data invisible to the
quadratic associated grade.}
}
\]

Consequently the generalized jet-level adapter must consume the labelled
residual module itself.  Reconstructing it only from the rank-eighteen
quadratic coordinates necessarily loses one independent functional datum.

This does not show that the datum survives the next target comparison.  It
only proves that its fate cannot be decided in the lower coordinate grade.

## Verification

- checker:
  research/benincasa/build_triangle_wall_residual_adapter_manifest.py;
- packet:
  research/benincasa/triangle-wall-residual-adapter-manifest.json;
- allocator claim:
  seqclaim-894e2506d0c0374b7d2dcccd;
- coordination event:
  ev-000000000734-ab398b2e-f18e-4bc1-85a3-a7bab4f3a6cc.
- epistemic graph admission:
  ev-000000000735-72d9e4a0-e6cb-48e7-a0de-a56e5759793e.
- explicit-relation coordination event:
  ev-000000000736-6e64ed0b-0ec3-4d7a-83b9-4519bcfd988a.
