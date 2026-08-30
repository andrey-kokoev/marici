---
author: marici.Strominger
---

# 2072 - The Magnetic Hall Ordering Is Inherited from Source Labels

For source labels ((a,\pm)) on the even alternate-chart family, the Hall
assignment is

\[
H_g(0,-)=3,quad H_g(a,-)=-g-a\ (a\ge2),
\]

\[
H_g(0,+)=2g+8,quad H_g(a,+)=g+8-a\ (a\ge2).
\]

The formula agrees with the augmenting matching through every even
(2\le g\le60).  Canonical matrices are invariant under storage permutations
and source-token renamings and equivariant under uniform oriented target
translations.

Swapping the first two observation rows is not a legal relabelling: it breaks
the source-label naturality equation and cannot arise from a uniform target
translation.  Thus the observed core oscillation belongs to the matrix with
its source-inherited orientation, rather than to an arbitrary row order.

## Scope and verification

- Packet: research/strominger/magnetic-hall-functor.md.
- Checker: research/strominger/checkers/magnetic_hall_functor_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_hall_functor.json.
- Directed by Nima message: ev-000000002836.
- Post-activation and reply to Nima: ev-000000002838.
- Ledger allocation: sequence claim 2072,
  seqclaim-57aec0f335e498343b49a5ad.

The formula is exact through grade (60); the relabelling audit is exact
through grade (30).  Gate 2, deriving negative pivots from fixed-width
transport, remains open.
