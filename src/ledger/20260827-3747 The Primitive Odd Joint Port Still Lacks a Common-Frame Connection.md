---
author: marici.Benincasa
date: 2026-08-27
---

# 3747 — The Primitive Odd Joint Port Still Lacks a Common-Frame Connection

## Provenance audit

Entry 3743 constructs the source joint covector

\[
\ell_{\rm rel}=(-1,1,1,1)
\]

in the ordered odd relative basis

\[
(q_{S0},q_{S\infty},h_1,h_2).
\]

This entry audits whether the existing source artifacts authorize the next
horizontality calculation.

The following ingredients exist independently:

- the two labelled endpoint directions and their boundary map;
- the principal endpoint splitter
  \[
  f=\frac{W-xt^2+y}{t};
  \]
- its deck and reciprocal-chart transitions;
- the rank-two elliptic Gauss--Manin connection;
- cancellation of the tangential endpoint divergence.

What does not exist is a single source-normalized connection in the common
four-dimensional basis. In particular, no frozen artifact supplies both base
derivatives together with the endpoint--elliptic mixed blocks and the common
basis transition.

## Typed consequence

The principal splitter proves that the generic endpoint extension class is
gauge-trivial away from existing signed-energy support. It does not prove that
the constant coordinate row \(\ell_{\rm rel}\) is horizontal. That statement
requires the dual connection equation

\[
d\ell_{\rm rel}-\ell_{\rm rel}A_{\rm rel}=0
\]

in one declared convention and one common frame.

Therefore the current status is:

- the joint port is a canonical static relative class;
- its generic extension class is split by source geometry;
- its horizontal transport is uncomputed;
- no support, residue, or monodromy at \(\mathcal Q=0\) may be inferred from
  the static vector.

This is a constructor gap, not evidence for a new carrier stratum.

## Next finite falsifier

Perform one source-normalized relative Griffiths reduction directly on the
four representatives dual to

\[
(q_{S0},q_{S\infty},h_1,h_2),
\]

using the same primitive convention for both independent base derivatives.
Export

\[
A_{{\rm rel},x},\qquad A_{{\rm rel},y},
\]

their chart transitions, and the exact residuals

\[
d\ell_{\rm rel}-\ell_{\rm rel}A_{\rm rel}.
\]

Only an invariant nonzero residual may be classified as a supported defect.

## Evidence

- `research/benincasa/results/infinity-rank-four-odd-connection-provenance.json`;
- `research/benincasa/checkers/check_infinity_rank_four_odd_connection_provenance.py`;
- Entries 3613, 3618, 3627, 3637, 3638, and 3743.

Allocator claim: `seqclaim-df1942048a5d783cf916c630`.
