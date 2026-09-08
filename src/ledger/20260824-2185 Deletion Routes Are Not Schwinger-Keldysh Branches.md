---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2185 — Deletion Routes Are Not Schwinger–Keldysh Branches

## Two independent occurrence labels

The contact interference packet compares two graph-construction routes:

\[
R_{\rm del}
=
\{\text{grade-two spectator route},
\text{fully deleted contact route}\}.
\]

By contrast, a Schwinger–Keldysh source carries contour occurrences

\[
B_{\rm SK}=\{+,-\}.
\]

The frozen correlator formulas derive the first pair from edge deletion. A
contour-doubled source would add the second pair independently. Its labelled
occurrence set would therefore be

\[
\boxed{R_{\rm del}\times B_{\rm SK},}
\]

with four elements, not two.

## No canonical identification

Route exchange and branch exchange are independent commuting involutions on
this four-element set. Identifying the deletion routes with (+) and (-)
selects one diagonal subset and discards the other two legitimate labelled
occurrences.

No source map in Benincasa–Dian or in the three-site wavefunction source
authorizes that collapse. Therefore

\[
\boxed{
\text{the route-difference covector }(1,-1)
\text{ is not automatically a Keldysh quantum-source derivative.}
}
\]

## Consequence

Entry 2107 proves that a transverse Keldysh response can reveal information
lost on the equal-source diagonal. Entry 2185 shows that this fact alone
does not activate the contact interference packet: the hidden direction is
in deletion-route space, not branch space.

An admissible activation requires a mixed comparison that relates contour
branch history to deletion-route history. Such a map would be additional
coherence data, not a relabelling of existing occurrences.

## Scope

This is a typing theorem about source labels. It does not prove that no
future Schwinger–Keldysh construction can couple the two index systems. It
prohibits assuming that coupling without deriving it.

## Evidence

- Entries 2107–2110 and 2174–2183
- `research/benincasa/checkers/deletion_route_not_keldysh_branch.rs`
- allocator claim `seqclaim-8c51284b16052b0c3290111c`