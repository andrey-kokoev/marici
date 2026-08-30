# 1843 — Correction: The Physical Gram Current Supplies the Polar Deck Sign

## Notation corrected

Entries 1841--1842 blurred the invariant Gram equation with its oriented root.
The correct objects from Entry 1216 are

\[
D=\det H,
\qquad
z=\det Q_{\rm ext},
\qquad
z^2=D.
\]

The deck involution is \(z\mapsto-z\).

## Frozen physical current

Entry 1216 already derives

\[
\boxed{
d^3\ell
=
\frac{du_1\wedge du_2\wedge du_3}{z}.
}
\]

Under the orientation-reversing deck transformation,

\[
z^{-1}\longmapsto-z^{-1},
\qquad
du_1\wedge du_2\wedge du_3
\longmapsto
-du_1\wedge du_2\wedge du_3.
\]

Therefore the complete physical current is invariant:

\[
(-1)\cdot(-1)=+1.
\]

## Correction to Entry 1842

The bare trace statement

\[
\operatorname{Tr}_{\mu_2}(z^{-1})=0
\]

remains correct.  But the bare coefficient is not the complete physical
object.  The numerator orientation line supplies the independently derived
anti-invariant factor that Entry 1842 treated as absent.

Thus no additional Betti sign is required for **local current descent**.  The
invariant object is the paired current

\[
\frac{du_1\wedge du_2\wedge du_3}{z},
\]

not \(z^{-1}\) alone.

## Polar coefficient identification

Entry 1840's polar \(D^{-1/2}\) Kummer character is exactly the external-Gram
Kummer density already frozen in Entry 1216.  It is neither a new coefficient
primitive nor a new carrier datum.

The corrected local architecture is

\[
\boxed{
\text{existing Gram carrier}
+
\text{existing physical-current Kummer/orientation pair}.
}
\]

## Remaining physical boundary

This correction establishes canonical local current descent.  It still does
not construct the global Bunch--Davies relative chain or its intersection
number with the polar vanishing cycle.  Global activation therefore remains
undefined, while the local deck-sign obstruction is closed.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_physical_gram_descent_correction.py`
- `research/benincasa/results/five-site-region-pair-physical-gram-descent-correction.json`
- Entry 1216 and Entries 1840--1842
- allocator claim: `seqclaim-1e5f3a58b2e31081b29d6272`
