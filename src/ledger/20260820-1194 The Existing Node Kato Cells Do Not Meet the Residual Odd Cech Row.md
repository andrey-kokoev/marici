---
title: "The Existing Node Kato Cells Do Not Meet the Residual Odd Cech Row"
date: 2026-08-20
entry: 1194
status: active-negative-falsifier
sector: cosmology
---

# 1194 — The Existing Node Kato Cells Do Not Meet the Residual Odd Čech Row

Sequence claim: `seqclaim-f3863487e1281579e443758f`.

## Tested conjecture

Entry 1192's eight deck-odd classes occur only in terms that also contain a
fourfold concurrence at a branch node. The nearest predeclared mechanism is
the local (A_1) Kato/vanishing-cycle cell of Entries 1178--1181.

The finite test is whether its oriented fourfold boundary defines a nonzero
row on the deck-odd triple basis and kills the residual (H^2_-).

## Exact nonincidence

For every source branch quadruple, all four of its triple faces are themselves
ramification triples. A ramification point has no deck-odd (H^0) generator.
Consequently the only variance-compatible Kato row is identically zero:

\[
\boxed{d_{\rm Kato}:C^2_-\longrightarrow V_{A_1}=0.}
\]

Appending every typed branch-node row therefore leaves

\[
\boxed{\dim H^2_-=8.}
\]

The augmented matrices still satisfy (d_2d_1=0) termwise.

## Meaning

Entry 1181's node-local cone remains acyclic in its own occurrence-resolved
support category. It cannot be used to kill Entry 1192's classes: that would
transport a node vanishing object across a missing deck-odd restriction map.

This negative result preserves H2. The eight classes remain sector-specific
coefficient candidates on the existing carrier; they are not evidence for a
new carrier stratum.

## Next falsifier

The next admissible mechanism is horizontal rather than node-local: derive
the Gauss--Manin connection on the two (\mathbf Q[C_4]) residual modules,
including their extension with the smooth elliptic-pair row. Test whether
the rank-eight subquotient is horizontal. If it is not, compute its minimal
flat closure; if it is, factor its intrinsic singular support before any
physical-chain interpretation.

## Artifact

- `research/benincasa/checkers/four_site_qg_node_kato_completion.py`
- `research/benincasa/results/four-site-qg-node-kato-completion.json`
