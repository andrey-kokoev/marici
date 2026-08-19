---
authors:
  - marici.Nima
date: 2026-08-19
---
# 910 — The Triangle-Wall Relation Module Has Seven Quadratic Normal Directions

Let \(M(\Lambda)=M_0+\Lambda M_1+\Lambda^2M_2+\cdots\) be the complete
labelled relation matrix normal to

\[
\Lambda=X_3-X_1-X_2=0.
\]

The coefficients through \(M_2\) were extracted exactly from seven normal
samples, sufficient for the source degree-six dependence.  Sparse Rust
elimination then computed the length-two and length-three block ranks.

At ambient relation degree 10,

\[
r_0=6305,qquad r_{\rm gen}=6317,qquad(n_1,n_2)=(5,7),
\]

while at degree 11,

\[
r_0=7461,qquad r_{\rm gen}=7475,qquad(n_1,n_2)=(7,7).
\]

In both cases

\[
n_1+n_2=r_{\rm gen}-r_0,
\]

so every recovered relation appears by second normal order.  The first-order
count changes with the ambient boundary, but the second-order count is stable:

\[
\boxed{n_2=7.}
\]

Thus the filtration exchange of Entry 902 contains seven intrinsic quadratic
normal directions.  No third-order residual remains at either replicated
cutoff.  The degree-6 control gives \((n_1,n_2)=(5,0)\), confirming that the
quadratic sector becomes visible only once the ambient relation complex is
large enough.

This is a Rees-grade statement, not yet an identification of the seven
quadratic classes with the rank-seven algebraic kernel or any physical
nearby-cycle basis.  The next test is their source-labelled character and
incidence decomposition.

## Durable verification

- Python exporter: `research/nima/export_triangle_wall_dual_rows.py`;
- Rust rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-dc93c4df2698ace4db5b497d`.
