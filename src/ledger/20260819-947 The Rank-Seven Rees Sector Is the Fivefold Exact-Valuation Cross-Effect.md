---
authors:
  - marici.Nima
date: 2026-08-19
---
# 947 — The Rank-Seven Rees Sector Is the Fivefold Exact-Valuation Cross-Effect

Entry 942 proved vanishing on the five codimension-one deletion faces.  The
complete marked-subset cube has now been evaluated.

Let

\[
I=\{g_1,g_2,g_3,g_{23},g_{31}\},
\]

and let \(C_S\) be the Rees cokernel retaining the common de Rham and
principal relations together with precisely the marked families in
\(S\subseteq I\).  Apply the functorial exact-valuation object of Entry 938:

\[
E_2(C_S)=
\frac{\ker\Lambda\cap\Lambda C_S}
     {\ker\Lambda\cap\Lambda^2C_S}.
\]

All 32 subsets were computed.  At ambient degrees 10 and 11 independently,

\[
\boxed{
E_2(C_S)=0\quad\text{for every }S\subsetneq I,
\qquad
E_2(C_I)\cong\mathbf F^7.
}
\]

Therefore the \(E_2\)-valued five-cube has a single nonzero vertex.  Its top
cross-effect is

\[
\boxed{
\operatorname{cr}_5(E_2\circ C)
\cong\mathbf F^7.
}
\]

## Order-of-operations obstruction

The raw presentation cube itself has zero total homotopy cofiber.  Indeed, its
target module is constant, its common source relations form a constant cube,
and each marked source summand is constant in four of the five cubical
directions.  Every summand is therefore killed by an iterated cofiber.

Consequently

\[
\boxed{
E_2\!\left(\operatorname{TotCofib} C_\bullet\right)=0,
\qquad
\operatorname{TotCofib}\!\left(E_2(C_\bullet)\right)
\cong\mathbf F^7.
}
\]

The rank-seven sector is not a new linear carrier cell hiding in the marked
presentation.  It is created by the nonlinear exact-valuation operation after
all five marked relations interact.

This sharpens the coefficient interpretation: the seven is a fifth
cross-effect of the degeneration functor.  It remains algebraic and
occurrence-covariant, but no physical period or identification with the
generic algebraic kernel has yet been derived.

## Durable verification

- packet filter:
  `research/nima/filter_triangle_wall_rees_packet.py`;
- tagged exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- exact Rees engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- census packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-8791c0021aff9ebd23c8102c`.
