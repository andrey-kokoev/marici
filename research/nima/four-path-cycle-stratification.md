# Four-Path Cyclic Information Is Born on a Chord-Deletion Boundary

The amplitude-side four-occurrence test distinguishes generic reconstruction
from supported reconstruction.

For four labelled records, the phase cycle space of the complete graph has
rank

\[
|E|-|V|+1=6-4+1=3.
\]

On the open locus where the chord \(g_{13}\) is nonzero, the four-cycle

\[
C_{1234}=g_{12}g_{23}g_{34}g_{41}
\]

is reconstructed from two triangle Bargmann products:

\[
B_{123}B_{134}=|g_{13}|^2C_{1234}.
\]

Thus arity four supplies no new generic phase generator beyond the triangle
cycles.

That statement fails on a geometrically defined boundary.  Set both diagonal
chords \(g_{13}=g_{24}=0\), retain the four rim overlaps with magnitude
\(r=1/4\), and compare a real rim cycle with one carrying a quarter-turn
phase.  The resulting two exact Hermitian Gram matrices are strictly positive
and have:

- identical proper principal minors;
- identical triangle Bargmann products, all zero;
- different nonzero four-cycle products;
- different grade-four determinants.

The surviving four-cycle cannot be reconstructed by dividing through a
vanished chord.  It is a relative/support-stratified invariant born precisely
where the generic triangle factorization ceases to be faithful.

The resulting architecture is

\[
\boxed{
\text{generic four-cycle} = \text{composite triangle data},
\qquad
\text{chordless four-cycle} = \text{supported arity-four datum}.
}
\]

This is not a failure of the full labelled Carrier operation.  It is failure
of the generic triangle-coordinate chart on its chord-deletion boundary.  A
faithful interface must retain the chordless cycle as a supported port rather
than extend the quotient formula through a zero denominator.

The exact checker passes 7/7 gates.

Artifacts:

- `research/nima/four-path-cycle-stratification.md`
- `research/nima/checkers/check_four_path_cycle_stratification.py`
- `research/nima/results/four-path-cycle-stratification.json`

Sequence claim: `seqclaim-5ebe6081916c078eb1d754ec`.
