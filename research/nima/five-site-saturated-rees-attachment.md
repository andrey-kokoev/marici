# The Deck-Saturated First-Rees Attachment Is Generically Exact but Character-Mixing

The 45-dimensional saturation-collapse kernel requires a different normal map
from the unsaturated comparison of Entry 1204.

For a connected complementary pair on a fixed boundary-sign sheet, write

\[
q_A=q,
\qquad
q_{A^c}=T-q,
\qquad
T=E_T.
\]

At \(T=0\), the two defining equations differ by a unit \(-1\), so their
logarithmic divisor classes coincide. The first normal difference is

\[
\boxed{
\left.\partial_T\bigl(\log(T-q)-\log(-q)\bigr)\right|_{T=0}
=-\frac1q.
}
\]

For an edge block,

\[
q_+=T+2y_i,
\qquad
q_-=T-2y_i,
\]

and the corresponding normal coefficient is \(-1/y_i\).

These reciprocal coefficients are nonzero away from the already declared
marked divisors. In the sheet basis, the saturated attachment decomposes into

- five rank-one edge blocks;
- ten rank-four connected-boundary blocks.

Therefore its generic rank is

\[
\boxed{5+10\cdot4=45,}
\]

and its generic kernel is zero.

## Character behavior

For a boundary pair with sheet values

\[
q_{s,t}=x+sy_i+ty_j,
\qquad s,t=\pm1,
\]

the four coefficients \(-1/q_{s,t}\) generically have nonzero transforms in
all four characters

\[
1,\quad\chi_i,\quad\chi_j,\quad\chi_i\chi_j.
\]

Thus the attachment is equivariant in the transported sheet basis but mixes
the declared character columns after Fourier transformation. It produces no
new characters and no generic homology.

The only rank-loss support is \(q_{s,t}=0\), already one of the 45 marked
hyperplanes on the total-energy saturated complement.

This refines Entries 1204--1205 rather than contradicting their unsaturated
Koszul exactness. The polynomial symbol \(2X_A\) controls the fixed-sheet
label comparison; the reciprocal symbol \(-1/q\) controls projective
coalescence in the deck-saturated divisor complex.

Artifacts:

- `research/nima/check_five_site_saturated_rees_attachment.py`
- `research/nima/results/five-site-saturated-rees-attachment.json`
