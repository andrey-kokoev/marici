# Entry 1897 — The Proposed Seven-Site Fourfold Incidence Fails the Frozen Source Gate

## Frozen candidate

Test the seven-cycle incidence

\[
g_{12}\mid g_{34}\mid g_{56}\mid g_7
\]

against the complete cosmological-polytope facet and source-term inventory.
No denominator or carrier cell may be added after the test.

## Slot-count correction

The singleton (g_7) is already part of the universal source prefactor

\[
G\prod_{i=1}^7g_i.
\]

It is a genuine active wall, but it does not consume one of the six
additional denominator slots of a seven-site term. Thus the three new pair
walls must be supplemented by three—not two—completion facets.

## Labelled occurrence orbit

The incidence has trivial stabilizer under (C_7). Its seven labelled
occurrences form the regular representation

\[
\mathbb Q[C_7],
\qquad
\chi=(7,0,0,0,0,0,0).
\]

Transport in source order preserves residue orientation strictly. Comparison
with lexical ordering gives the convention-dependent signs

\[
(+,-,+,+,-,-,+),
\]

which are recorded but have no invariant meaning by themselves.

## Exact source census

Every triple of frozen completion facets was tested against two independent
conditions:

1. the common zero-vertex set must have affine rank seven;
2. the distinct source denominator rows must have rank fourteen.

No completion triple satisfies both.

Exactly four triples attain affine rank seven. All four have denominator
rank thirteen:

\[
\begin{array}{c|c}
\text{completion triple}&\text{exact extra relation}\\
\hline
(g_{1234},g_{123456},g_{3456})
&g_{1234}-g_{123456}-g_{34}+g_{3456}=0\\
(g_{1234},g_{12347},g_{127})
&-g_{12}+g_{1234}-g_{12347}+g_{127}=0\\
(g_{12567},g_{127},g_{567})
&g_{12567}-g_{127}-g_{567}+g_7=0\\
(g_{3456},g_{34567},g_{567})
&g_{3456}-g_{34567}-g_{56}+g_{567}=0.
\end{array}
\]

These are occurrence-labelled inclusion--exclusion relations, not accidental
numeric degeneracies.

There are many rank-fourteen triples, but each has affine rank at most six.
Thus denominator independence and face compatibility never coincide.

## Terminal result

\[
\boxed{
g_{12}\mid g_{34}\mid g_{56}\mid g_7
\text{ occurs in no full-rank frozen seven-site source term.}
}
\]

The proposed incidence is therefore not an admitted seven-site Carrier
stratum. Constructing a Cayley--Menger family over it would transport the
six-site pattern as authority and would violate the frozen-source rule.

This is not a failure of H2. The Carrier has rejected the proposed
higher-arity continuation before coefficient geometry is formed. The
horizontal-plus-vertical architecture remains established at six sites but
is neither confirmed nor falsified at seven sites by this incidence.

## Consequence for the planned twelve-step attack

Steps 4–12 are inapplicable for this candidate. Their source object does not
exist. The correct next independent attack must first search the frozen
seven-site source inventory for an actually admitted maximal incidence; only
then may its coefficient geometry be constructed.

## Durable verification

- `research/benincasa/marici-gm/src/bin/seven_site_disjoint_pair_singleton_source_gate.rs`
- `research/benincasa/results/seven-site-disjoint-pair-singleton-source-gate.json`
- allocator claim: `seqclaim-e7d6af1caa4a31f9f36d27d4`
- epistemic event: `ev-000000002265-9656b91b-fbf8-4621-a0dd-9c79c2dbe532`
