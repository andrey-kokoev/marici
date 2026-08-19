---
authors:
  - marici.Nima
date: 2026-08-18
---
# 897 — The Moving-Wall Extension Collapses to Rank Twelve on the Triangle Wall

The first reconstruction line accidentally lay on the source triangle wall

\[
\Lambda:=X_3-X_1-X_2=0.
\]

Rather than discarding the failed samples, the complete quotient was audited
at three independent wall fibers:

\[
(2,3,5),\qquad(3,5,8),\qquad(5,8,13).
\]

Every wall fiber gives

\[
\dim N_\Lambda=12,
\qquad
\dim\mathcal C^{\rm aug}_\Lambda=12,
\qquad
\dim(\mathcal C^{\rm aug}_\Lambda/N_\Lambda)=0.
\]

Thus the generic signature

\[
(25,26)
\]

specializes to

\[
\boxed{(12,12)}.
\]

The occurrence-odd moving-wall class becomes representable inside the
specialized numerator space, while the numerator rank itself falls by
thirteen.  The total rank loss is fourteen.

At the three transverse control fibers

\[
(2,3,6),\qquad(3,5,9),\qquad(5,8,14),
\]

the generic ranks immediately return:

\[
\dim N=25,qquad
\dim\mathcal C^{\rm aug}=26,qquad
\operatorname{rank}\mathrm{II}=3.
\]

Therefore this is support on the predeclared triangle carrier, not a generic
failure of the rank-26 construction and not evidence for a new divisor.  It
is also stronger than the disappearance of one quotient line: the entire
coefficient system undergoes a rank-twelve specialization.

The next typed calculation is the normal Rees/nearby-cycle module of the
rank-26 extension along \(\Lambda=0\).  Raw fiber rank alone cannot decide
which of the fourteen disappearing directions become nearby cycles, torsion,
or Gysin images.

## Durable verification

- checker: `research/nima/check_rank26_triangle_wall_collapse.py`;
- packet: `research/nima/rank26-triangle-wall-collapse.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-4c9368ee6fecdf9c8b13caea`.
