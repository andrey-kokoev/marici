---
author: marici.Figueiredo
---

# 1901 — The Oriented Loop-Holonomy Line Is a Möbius Bundle over the Exact Flavor Carrier Groupoid (WP11)

## Question

WP10 certified that all 61 nine-link presentations lie in one exact
codimension-one carrier groupoid (33-edge tree-face spanning
certificate) and that the fundamental-cycle kernel \(K_T\) does not
descend to physical flavor space.  The packet's sharp next calculation:
transport the one-loop phase line through the exact tree and test the
fundamental cycles created by the remaining exact tree-face arrows —
any nontrivial cocycle belongs to the lens/readout data, not to
disconnected carrier geometry.

## Method

Exact integer/permutation arithmetic only; no fitted values.  Each of
the 61 presentations carries a unique oriented support cycle (true
incidence-kernel vector, divergence-free), oriented so the fitted phase
edge has coefficient \(+1\).  Each exact tree-face arrow (two
presentations sharing a connected eight-link tree face, i.e. a common
chart boundary) transports the oriented cycle through the canonical
face labels.  The vertex-level carrier multigraph (61 vertices; 2331
exact arrows; 60-edge spanning tree) has \(2314\) fundamental cycles;
the monodromy of the oriented phase line is computed around every one
of them, with all \(S_3^3\) witness choices enumerated so each cycle is
typed *trivial* (\(+1\) always), *twist* (\(-1\) always), or
*ambiguous* (both signs achievable).  An independent coboundary test
(no spanning tree) cross-checks nontriviality: a global signing
\(o(v)=\pm1\) with \(o(v)=s\,o(u)\) on every sign-definite edge exists
iff the cocycle is trivial.  Checker:
`research/flavor/checkers/wp11_phase_line_transport.py`; results:
`research/flavor/results/wp11_phase_line_transport.json`.

Convention note: the WP10 kernel checker used labelled occurrence
vectors that are not cycle-space elements (path walked Q→column with
the normal pinned to \(+1\)); comparing cycles across different normals
requires true kernel vectors.  Part C of the WP11 checker re-audits the
WP10 kernel with corrected vectors.

## Findings

### 1. The phase line twists: the exact cocycle is nontrivial

Of the \(2314\) fundamental cycles, \(1345\) are trivial, \(454\) are
**definite twists** (monodromy \(-1\) under every witness choice), and
\(515\) are ambiguous.  The tree-independent coboundary check confirms
nontriviality: the sign-definite subgraph (\(2367\) edges, all 61
vertices) admits no global signing (\(717\) violated constraints):

\[
\boxed{\text{the oriented loop-holonomy line is a Möbius line over the
exact carrier groupoid.}}
\]

Only the *unoriented* phase line — \(\varphi\) modulo sign, the
CP-conjugate pair \(\{\varphi,-\varphi\}\) — is data of the exact
sparse carrier groupoid.  The orientation of the holonomy (chart versus
its CP mirror) is double-cover data, not carrier-groupoid data.

### 2. All ambiguity is internal stabilizer reversal

Occurrence-level transports are fully definite (\(0\) of \(268\)
tree-face occurrences admit both signs across witnesses): face
automorphisms never reverse the relative orientation.  The entire
ambiguity concentrates in \(7\) of \(43\) internal \(S_3^3\) component
pairs, whose support stabilizers contain orientation-reversing maps —
exactly the \(\pm1\) involutions of Nima's prime-3 falsifier (entry
1550, graph ev-1700), now located as the local source of the twisted
geometry.

### 3. Vertex-level connectivity

The exact carrier groupoid is connected at vertex level: \(60\) tree
edges suffice for all \(61\) presentations (the WP10 certificate was
component-level; this strengthens it by one level of resolution).

### 4. WP10 kernel survives the convention correction

Recomputing the fundamental-cycle kernel with true cycle-space vectors
reproduces the committed WP10 headline exactly: \(370\) compatible
component pairs, one connected component.  The WP10 §5 connectivity
conclusion is unaffected; no erratum is needed.  (The signed-overlap
histograms differ, as they must — the pairings are different bilinear
forms — but every WP10 statement cited existence/nonvanishing, which is
preserved.)

## Scope

Everything here is exact support/permutation-level structure of the
sparse presentation groupoid at the WP7 best-fit point.  The twist does
**not** descend to the physical quotient — WP10 already showed the
labelled cycle module itself does not descend — so the Möbius bundle is
a property of the *lens* (the sparse coefficient presentation system),
not of physical flavor space.  It answers the packet's question
affirmatively: a nontrivial cocycle exists and it lives in the
lens/readout data.  It does not change the 1077 admission verdict, and
it gives no new quotient-level meaning to the \(\pi/8\) clusters.

The result sharpens the flavor typing for H2LR: the flavor lens is not
just multi-charted (Gribov copies, WP10 §3) but *non-orientable* in its
phase coordinate: any cross-sector comparison must use
sign-insensitive (\(|\sin\varphi|\)-type) loop data.

## Verification

- `research/flavor/checkers/wp11_phase_line_transport.py` (stdlib-only,
  exact; reuses the WP10 atlas/incidence/certificate JSONs).
- `research/flavor/results/wp11_phase_line_transport.json`:
  \(61/61\) vertices with valid oriented cycles, zero pullback
  exceptions across \(268\) occurrences (this validates the cycle and
  witness machinery); monodromy summary
  \(\{1345\ {\rm trivial},\ 454\ {\rm twist},\ 515\ {\rm ambiguous}\}\);
  coboundary check \(717\) conflicts, `cocycle_nontrivial: true`;
  kernel re-audit \(370\) pairs, one component.
- Epistemic graph: admitted as `ev-000000002269` (16 operations):
  claims `marici:claim:flavor-wp11-mobius-cocycle-v1`,
  `marici:claim:flavor-wp11-unoriented-phase-line-v1`,
  `marici:claim:flavor-wp10-kernel-reproduced-true-vectors-v1`;
  test `marici:test:flavor-wp11-phase-line-transport-v1` with outcome
  `marici:test_outcome:flavor-wp11-phase-line-transport-v1` (pass);
  `marici:refines` relations to the WP10 claims.
