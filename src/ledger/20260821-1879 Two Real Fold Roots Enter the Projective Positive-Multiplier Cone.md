# 1879 — Two Real Fold Roots Enter the Projective Positive-Multiplier Cone

## Frozen question

Entries 1876--1878 identify four real source-sheet roots of the two
region-only quartic norms and prove that each is an ordinary \(A_1\) fold.
A real fold is not yet a Landau pinch.  The next necessary test is whether
the three source wall multipliers can be chosen with one common nonzero
sign, modulo their irrelevant common projective rescaling.

## Exact sign audit

The real-root isolator now evaluates the three quadratic-field wall
multipliers on rational isolating intervals.  No floating-point root or
sampled sign is used.

For

\[
D_3:\quad g_{123}\mid g_4\mid g_5,
\]

the two \(+\sqrt5\) source-sheet roots have projective sign vectors

\[
(-,+,+),\qquad (+,+,+).
\]

For

\[
D_4:\quad g_{12}\mid g_{34}\mid g_5,
\]

they have

\[
(-,-,-),\qquad (+,+,-).
\]

Hence exactly one root of each topology belongs to the common-sign
projective cone.  The other root of each topology cannot be an ordinary
positive-multiplier pinch.

## Narrow result

\[
\boxed{
4\ \text{real source-sheet }A_1\text{ folds}
\;\longrightarrow\;
2\ \text{projectively positive-multiplier candidates}.
}
\]

This is a necessary Landau condition, not a physical singularity theorem.
It does not determine the oriented intersection of the continued
Bunch--Davies chain with either rank-one vanishing cycle, and it does not
fix the source \(i\epsilon\) sheet.

## Consequence for H2

No new carrier component is indicated.  The two surviving candidates are
ordinary fold coefficient data supported on the already frozen three-wall
incidences.  Their possible physical visibility has been reduced to a
source-contour pairing problem.

## Next falsifier

For the surviving \(D_3\) and \(D_4\) roots, transport the source-defined
relative contour with its original \(i\epsilon\) prescription and compute
the oriented intersection with the local \(A_1\) thimble.  A zero pairing
closes that candidate physically; a nonzero source-normalized integer
activates a coefficient singularity without adding a carrier stratum.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_real_roots.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-real-roots.json`
- allocator claim: `seqclaim-5eff936c2416cf0f67e06ad4`
- epistemic event: `ev-000000002236-5a794a11-4981-46fc-a9b3-3322f55f89ab`
