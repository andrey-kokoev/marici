# 1884 — The Six-Site Disjoint-Pair Triple Passes the Source-Incidence Gate

## Frozen analogue

Entry 1883 asks whether the activated five-site occurrence family extends
beyond arity five.  Before any Landau elimination, freeze the natural
six-cycle disjoint-pair triple

\[
g_{12}\mid g_{34}\mid g_{56}.
\]

The source packet is derived directly from the 18 cosmological-polytope
vertices and all genuine six-cycle facets.  No six-site denominator is added
after testing compatibility.

## Occurrence geometry

Unlike the free five-site orbit, this matching is stabilized by rotation by
two sites.  Its labelled \(C_6\) orbit therefore has size two:

\[
\{g_{12},g_{34},g_{56}\},
\qquad
\{g_{23},g_{45},g_{16}\}.
\]

This is a Carrier-predicted stabilizer effect, not a collapse of occurrence
labels.

## Exact source gate

A six-cycle OFPT term has the common prefactor \(G\prod_i g_i\) and five
additional compatible denominators.  Holding the three active walls fixed,
the exact facet-incidence and full-rank tests leave nine completions:

\[
\begin{aligned}
&(G-e_{23},g_{1256}),\ (G-e_{23},g_{3456}),\\
&(G-e_{45},g_{1234}),\ (G-e_{45},g_{1256}),\\
&(G-e_{61},g_{1234}),\ (G-e_{61},g_{3456}),\\
&(g_{1234},g_{1256}),\ (g_{1234},g_{3456}),
\ (g_{1256},g_{3456}).
\end{aligned}
\]

Hence

\[
\boxed{
g_{12}\mid g_{34}\mid g_{56}
\text{ occurs in exactly nine frozen six-site source terms.}
}
\]

The first all-arity gate therefore passes: the five-site phenomenon has a
source-admitted six-site analogue.  The changed orbit size and term count
show that the extension is structural rather than literal repetition.

## Scope and next falsifier

This is only source incidence.  It does not assert a nonsoft Landau solution,
a discriminant, multiplier saturation, or physical activation.

The next finite test is to solve the three active wall equations, retain all
three free loop coordinates, and determine whether the six-site
Cayley--Menger critical equations produce a generically nonsoft saturated
divisor.  Failure there makes the five-site activation arity-specific despite
the admitted source incidence.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_source_gate.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-source-gate.json`
- allocator claim: `seqclaim-4653e7dbbf28ecb2c04fffd1`
- epistemic event: `ev-000000002243-45ef8ff4-4210-446f-b9cd-75072145305c`
