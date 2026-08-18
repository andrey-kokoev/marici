---
authors:
  - marici.Nima
date: 2026-08-18
---
# 691 — Normalization Character Does Not Select a Line in the Gysin Kernel

## Proposed selector

Entry 689 identifies the oriented physical conductor costalk as
anti-invariant under the surface-normalization involution. A possible next
step was to decompose the rank-seven infinity-Gysin kernel and ask whether
it contains a unique compatible anti-invariant line.

It does not.

## Source master characters

The residue surface is

\[
w^2=K(a,b).
\]

Every frozen master is represented in one of the forms

\[
\frac{N(a,b)}{K^{1/2}}
\qquad\text{or}\qquad
\frac{D(a,b)}{K^{3/2}}.
\]

Under the normalization involution

\[
\iota:w\longmapsto-w,
\]

both (K^{-1/2}=w^{-1}) and (K^{-3/2}=w^{-3}) change sign. Therefore

\[
\iota(e_i)=-e_i
\qquad(1\le i\le9).
\]

The entire nine-master module is in the minus character:

\[
\dim(\mathcal M_9^-)=9,
\qquad
\dim(\mathcal M_9^+)=0.
\]

## Restriction to the Gysin kernel

The infinity-Gysin quotient has rank two and its kernel

\[
\mathcal T_7=\ker(\mathcal M_9\to\mathbb V_{\rm ell}(-1))
\]

has rank seven. Since the involution is scalar (-1) on the ambient module,
its restriction is also scalar (-1):

\[
\boxed{
\dim\mathcal T_7^-=7,
\qquad
\dim\mathcal T_7^+=0.
}
\]

Thus the physical costalk character is compatible with every direction in
the algebraic Gysin kernel. It selects no distinguished target line.

## Consequence

The uniqueness branch proposed in Entry 689 is falsified. Normalization
character is necessary typing data, but it has zero resolving power inside
the already anti-invariant master sector. Choosing (e_6),
(v_{\rm alg}), or the exceptional functional from character alone would
be arbitrary.

The next selector must come from a finer commuting structure already
present in the source—most naturally the occurrence/wall character,
relative-support filtration, or the explicit localization boundary map.
No scalar projection may be fitted afterward.

## Quartic consequence

This calculation neither introduces nor removes quartic support. It shows
that \(\mathcal Q\) cannot be localized by the coarse normalization
character. Any quartic extension class must first be typed by a finer
source-derived target decomposition.

## Evidence

- `research/benincasa/check_t7_normalization_character.py`;
- `research/benincasa/t7-normalization-character.json`;
- `research/benincasa/derive_nine_master_residue_connection.py`;
- Entries 150, 689–690;
- allocator claim `seqclaim-fed98a0af4724eb3c8a22788`.

## Next falsifier

Restrict the explicit occurrence/wall involutions to \(\mathcal T_7\) and
intersect their character eigenspaces with the normalization-minus sector.
Test whether the physical (g_3) costalk character tuple leaves a unique
line.
