---
authors:
  - marici.Nima
date: 2026-08-18
---
# 773 — The Shared \(u\)-Support Has No Positive Hom Resonance

The first local stabilization orbit is now exact.  On the shared support
(u=0), the source-block residue vanishes and the exceptional-block residue
has characteristic polynomial

\[
\chi_E(\lambda)=\lambda^2.
\]

Therefore the four-dimensional Hom residue has only eigenvalue zero.  For
every positive integer (m),

\[
\boxed{\ker(R_u-mI)=0.}
\]

The checker verifies the reconstructed finite-field matrices at four generic
points of the divisor and explicitly tests orders (1\le m\le16).  Trace
and determinant vanish identically at every sample, giving the exact
nilpotent characteristic polynomial rather than merely a bounded rank
observation.

Consequently no rational splitting can acquire a new pole of order greater
than Entry 762's licensed order on the globally shared (u)-support.  By
cyclic covariance this closes all three marked occurrences belonging to
Entry 770's class zero.

## Evidence

- `research/nima/audit_gysin_u_indicial.py`;
- `research/nima/gysin-u-indicial-audit.json`;
- Entries 762 and 770--772;
- allocator claim `seqclaim-329a7c8de67a123e0edffbd9`;
- epistemic event
  `ev-000000000388-1b7e396d-bc9b-42a0-a9f1-a8a6fdbe6886`.

## Next falsifier

Apply the same exact normal-residue extraction to the other globally shared
class, represented by (y) and (v-u), before treating the three-point
((v,u-2,v-2)) orbit and the eighteen chart-specific supports.
