# 978 — The Chamber-Hexagon Cochain Transport Is Not Yet Typed

## Proposed global test

Entry 977 constructs one rational cochain

\[
\lambda\in C^0_{\rm target}\otimes
\mathbb Q(A_2,A_3,B_{24},B_{34},Z)
\]

on the frozen six-row loaded comparison. Its next test proposed transporting
\(\lambda\) around the chamber hexagon and computing \(\delta\lambda\).

That test requires, for every oriented chamber edge, a rational pullback map
on the target cochain and its pivot coordinates. If the boundary closes only
up to homotopy, it also requires the corresponding two-cell map with the same
variance.

## Frozen-data audit

The current packets contain:

1. one (6\times6) loaded comparison matrix;
2. one six-component cochain \(\lambda\);
3. six chamber adjacencies, each carrying an edge label, half-monodromy
   label, boundary factor, and branch-activity flag;
4. three (2\times2) occurrence permutations for the separate cyclic orbit
   of the rank-one mixed-corner source and target blocks.

They do not contain:

- a rational map on the six target cochain coordinates for any chamber edge;
- the induced transition on
  (A_2,A_3,B_{24},B_{34},Z) after the corner normalization;
- a two-cell homotopy acting on these target cochains.

The Entry 909 cyclic packet cannot fill this gap. It has three steps, acts on
two-dimensional source and target blocks, and proves a line-level orientation
character. The chamber test has six edges and a six-dimensional rational
cochain. These are different variances.

## Narrow conclusion

\[
\boxed{\delta\lambda\text{ is currently untyped.}}
\]

It is therefore neither zero nor nonzero on present evidence. Transporting
the Entry 909 sign around its (C_3) orbit would prove only the already known
rank-one occurrence covariance, not chamber-hexagon descent.

This is a missing comparison map, not evidence for a new carrier cell. The
six chamber edges and the two loaded circuit paths already exist.

## Next construction

Derive the target-chamber pullbacks directly from the same loaded Pochhammer
paths used in Entries 895–896 and 966. For every edge export:

1. its action on the six labelled target rows;
2. its rational action on pivot and pair coordinates before specialization;
3. its action on the two circuit homotopies;
4. its overlap composition.

Only then compute \(\delta\lambda\) and compare its six-edge return with
the native chamber two-cell.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_chamber_cochain_type_gate.rs;
- packet:
  research/benincasa/string-six-point-chamber-cochain-type-gate.json;
- verified command:
  cargo run --quiet --bin string_six_point_chamber_cochain_type_gate;
- allocator claim:
  seqclaim-bcd1deef0576cc09e81a3961.
- epistemic event:
  ev-000000000595-21981989-940a-471a-8ec7-0d9d48f23ecb.
