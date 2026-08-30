# 1742 — The Wilson Character Detects Noncommutativity but Forgets Based Ordering

## Frame-free readout

For Entry 1741's two-loop holonomy representation \(\rho\), define the Wilson
character

\[
W(w)=\operatorname{Tr}\rho(w)
\]

on loop words \(w\).

It is invariant under every simultaneous fiber-frame change

\[
\rho(w)\longmapsto G\rho(w)G^{-1}
\]

and under cyclic rotation of a word.

## What survives

The two generators satisfy \(A^2=B^2=1\).  Their group commutator is

\[
[A,B]=ABA^{-1}B^{-1}=(AB)^2=-I,
\]

so

\[
\boxed{W([A,B])=-2.}
\]

Thus the Wilson packet detects that the transport is noncommutative.

## What is forgotten

Cyclicity forces

\[
W(AB)=W(BA)=0.
\]

Hence scalar Wilson traces cannot distinguish the two based orderings or
recover the fiber matrices.  In the tested representation all word traces lie
in

\[
\{-2,0,2\}.
\]

The complete character retains conjugacy-class information about the
semisimple representation, not a labelled trivialization of its fibers.

## Narrow result

Without a fiber reference, the canonical physical candidate is a Wilson
character packet.  It sees nonabelianity but loses based matrix order.  Full
ordered transport requires a source-labelled matrix interference reference.

This is a coefficient/readout distinction over the existing loop carrier; no
new carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/two_loop_wilson_character.rs`
- `research/benincasa/results/two-loop-wilson-character.json`
- `research/benincasa/two-loop-wilson-character.md`

## Next falsifier

Add a source-labelled fiber reference and derive matrix interference entries.
Test whether their gauge-covariant packet recovers \(AB\) versus \(BA\) while
remaining independent of arbitrary simultaneous frame changes.
