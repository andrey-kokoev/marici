# Retained direct sum closes structural, not incidence, coherence

Date: 2026-09-08

## Structural theorem

The selected G1 carrier is an ordered prime/grade-labelled direct sum.  Fix the
canonical normal bracketing by flattening every expression to its ordered
source coordinates.  Every associator and unitor is then only a coordinate
rebracketing.  In the frozen direct-sum metric its matrix is an identity or
permutation unitary.

Therefore, for every word length and every pair of bracketings,

\[
\|U_{\tau\to\tau'}\|
=\|U_{\tau\to\tau'}^{-1}\|=1,
\qquad
\kappa(U_{\tau\to\tau'})=1.
\]

This is independent of prime cutoff, grade cutoff, and assembly depth.  It
preserves the bounded-energy completion exactly.  Triangle and pentagon
coherence reduce to equality of ordered coordinate flattenings.

A finite hostile audit sampled 20 random bracketings at each atom count from 1
to 64.  All 1,280 transports had condition number one; together with flattening
checks, 2,560 assertions passed.  The general conclusion follows from the
coordinate-rebracketing description, not from sampling.

## G2 reduction

This closes the generic depth-conditioning concern for structural assembly on
the retained labelled architecture.  It does not close G2.

The remaining G2 content is nonstructural: admit the arithmetic-to-analytic
incidence, moving-seam transport, endpoint extraction, and Adams weighting as
typed rewrite rules and prove their critical pairs preserve the complete
external interface.  In particular, scalar Mellin equality cannot replace the
join between incidence-then-transport and transport-then-incidence.

Thus G2 now separates cleanly into:

- direct-sum associator/unitor coherence and completion stability: closed;
- source incidence rewrite and seam/endpoint critical joins: open.

No braid, dagger, or analytic normalization cell is declared unitary by this
argument unless it is literally one of the retained coordinate transports.

## Evidence

- `check_marici_rh_retained_direct_sum_coherence_20260908.py`
- `marici_rh_retained_direct_sum_coherence_certificate_20260908.json`
