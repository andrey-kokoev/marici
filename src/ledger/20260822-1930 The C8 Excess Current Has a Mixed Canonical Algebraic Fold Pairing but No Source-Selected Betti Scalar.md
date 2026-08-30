# 1930 — The C8 Excess Current Has a Mixed Canonical Algebraic Fold Pairing; Betti Selection Remains Open

## Frozen objects

This test uses only the previously frozen source data:

- the complete C8 canonical numerator and ordered positive-regulator contour of Entry 1926;
- the rank-three excess Leray/Koszul current of Entry 1928;
- the regulator-to-Orlik--Solomon chain map of Entry 1924;
- the four generic rank-one complex folds of Entry 1918;
- the real-Euclidean exclusion of those folds from Entry 1916.

No regulator chamber, residue weight, new support cell, or external continuation path is added.

## Source-face coefficient

For each of the 36 source occurrence orbits, the seven selected facets cut out a source-labelled eight-simplex face.  In barycentric coordinates its sevenfold residue is

\[
\Omega_F
=
\frac{1}{|\det S|\,t_0t_1\cdots t_8}.
\]

The three labelled base normals are retained before specialization.  The odd coefficient is computed by differentiating this exact face form along the corank-one kernel of the corresponding companion map.  Generic vanishing is certified by reducing the cleared numerator modulo the exact fold divisor; generic nonvanishing is certified by an exact nonzero point on that divisor.

The result is

\[
22\ \text{source orbits with nonzero odd coefficient},
\qquad
14\ \text{source orbits with identically zero coefficient}.
\]

By fold family:

\[
\begin{array}{c|c|c}
\text{family}&\text{nonzero}&\text{zero}\\
\hline
A_{e_1}&21&0\\
B_{e_8}&1&6\\
B_{e_6}&0&6\\
B_{e_4}&0&2
\end{array}
\]

Thus neither universal activation nor universal dormancy is correct.

## OS-compatible excess sewing

Let \(K\) be the labelled rank-three excess relation space.  Contracting the transverse seven-form by its ordered excess basis gives

\[
\iota_{K_3}\iota_{K_2}\iota_{K_1}
(e_1\wedge\cdots\wedge e_7)
\in \Lambda^4\mathbb Q^7.
\]

For every one of the 288 labelled occurrences, this degree-four class remains nonzero after quotienting by the complete labelled Orlik--Solomon ideal.  Combining it with the source-face coefficient gives

\[
176\ \text{nonzero sewn algebraic pairings},
\qquad
112\ \text{zero source coefficients}.
\]

The two occurrence components remain separate and balanced:

\[
\begin{array}{c|c|c|c}
\text{component}&\text{transverse sign}&\text{nonzero}&\text{zero}\\
\hline
0&-8&88&56\\
1&+8&88&56.
\end{array}
\]

Every one-step cyclic transport preserves the projective OS line with exact scalar \(+1\).  Hence the two components do not cancel by an unlabelled sum; they assemble as labelled cyclic copies with their orientation data retained.

## Physical classification

The calculation constructs a canonical **algebraic Betti/de Rham fold-pairing line** on 176 labelled occurrences.  It does not produce a canonical affine Betti scalar.

Entry 1916 places every generic fold outside the real-Euclidean Bunch--Davies routing cone.  Primary-source Eq. (4.19) nevertheless supplies an external negative-imaginary tube

\[
x_s\mapsto x_s-i\epsilon_{x_s},
\qquad
y_e\mapsto y_e-i\epsilon_{y_e},
\qquad \epsilon>0.
\]

The earlier version of this entry incorrectly treated the absence of an external-path field in the serialized contour packet as absence from the primary source.  That inference is withdrawn.  The source defines a tube, but it does not yet demonstrably select a unique positive regulator ray or a labelled vanishing path from that tube to a complex fold.

The local cover test \(s^2=h\) still shows that a loop sends \(s\mapsto-s\), preserving the projective line while reversing an affine generator.  But whether two such lifts are both admissible inside the source negative tube must now be computed; it cannot be inferred from packet-field absence.

The narrow classification is consequently

\[
\boxed{
\text{canonical mixed algebraic pairing}
\quad+\quad
\text{physical Betti selection open inside the source negative tube}.
}
\]

This is coefficient/continuation data, not evidence for a new carrier stratum.

## Verification

- `research/benincasa/eight-site-c8-nontransverse-bd-completion.md`
- `research/benincasa/checkers/eight_site_rank4_face_fold_pairing.py`
- `research/benincasa/results/eight-site-rank4-face-fold-pairing.json`
- `research/benincasa/checkers/eight_site_rank4_os_fold_sewing.py`
- `research/benincasa/results/eight-site-rank4-os-fold-sewing.json`
- `research/benincasa/checkers/eight_site_rank4_fold_betti_selection.py`
- `research/benincasa/results/eight-site-rank4-fold-betti-selection.json`

Both checkers use exact characteristic-zero arithmetic.  The first certifies the generic 22/14 source-orbit split; the second checks all 288 labelled occurrences, all complete OS ideals, both cyclic components, and every projective cyclic transport.

Allocator claim: `seqclaim-1d49bf235de87c808ee48dac`.

Epistemic graph event: `ev-000000002347-6bd8aa40-2d6b-4e97-91ef-b3115af5eecd`.

Primary-source correction event: `ev-000000002352-a22e827d-8d6f-4c9a-ac0c-b38b18222ba2`.

## Next falsifier

Push the source deformation of Eq. (4.19) through the four companion maps.  Determine whether the full positive regulator cone lies in one tube-to-fold homotopy chamber for every activated orbit.  Multiple chambers imply unselected Betti data; one chamber supplies the canonical vanishing path needed for physical activation.
