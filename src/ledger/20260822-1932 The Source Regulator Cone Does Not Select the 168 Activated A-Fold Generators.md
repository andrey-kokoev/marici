# 1932 — The Source Regulator Cone Does Not Select the 168 Activated A-Fold Generators

## Primary-source correction

The Bunch--Davies prescription relevant to the C8 fold problem is not limited to the contour variables.  Primary-source Eq. (4.19) gives

\[
x_s\longmapsto x_s-i\epsilon_{x_s},
\qquad
y_e\longmapsto y_e-i\epsilon_{y_e},
\qquad
\epsilon_{x_s},\epsilon_{y_e}>0.
\]

Thus the physical source supplies a negative-imaginary tube.  The remaining question is whether its positive regulator cone maps into one fold-normal chamber.

## Family-A fold normal

At the exact generic family-A fold point used in Entry 1930,

\[
a=b=c=d=1,qquad z^2=\frac{32}{5},qquad k=1,qquad l=0,
\]

the companion divisor has edge-energy gradient

\[
(\partial_aH,\partial_bH,\partial_cH,\partial_dH,\partial_zH)
=
(-154,-70,0,0,56\sqrt{10}).
\]

Under Eq. (4.19), the first fold-normal variation is

\[
\delta H
=
i\left(154\epsilon_a+70\epsilon_b-56\sqrt{10}\epsilon_z\right).
\]

All regulator components remain strictly positive.  Nevertheless:

- \((\epsilon_a,\epsilon_b,\epsilon_c,\epsilon_d,\epsilon_z)=(1,1,1,1,1)\) gives positive imaginary normal;
- \((1,1,1,1,2)\) gives negative imaginary normal;
- \((1,1,1,1,4/\sqrt{10})\) is tangent to the fold.

Therefore the source-admissible positive cone meets two opposite fold-normal chambers and their separating tangent locus.

## Consequence for the C8 census

Entry 1931 identifies 168 activated family-A occurrences and eight activated occurrences in one exceptional B8 orbit.  For all 168 A occurrences, cyclic covariance transports the calculation above.  Hence

\[
\boxed{
\text{the primary Bunch--Davies regulator cone does not select an affine A-fold generator.}
}
\]

Their projective coefficient lines and OS-sewn algebraic pairings remain canonical, but the signed Betti generator depends on the positive regulator chamber.

The unique activated B8 orbit is different.  At the tested fold point its edge-regulator generators span a pointed complex quadrant and do not cross the normal origin.  Its eight labelled occurrences remain undecided until the source regulator Jacobian for the companion parameters \(k,l\) is reconstructed.

## Classification update

Of the 176 algebraically activated labelled occurrences:

\[
168\text{ are physically unselected by an explicit positive-cone chamber test},
\]

while

\[
8\text{ remain open pending the }(k,l)\text{ regulator map}.
\]

No new carrier datum is indicated.  The ambiguity lies in sector-specific Betti continuation data over already existing carrier support.

## Verification

- `research/benincasa/checkers/eight_site_rank4_source_regulator_fold_chambers.py`
- `research/benincasa/results/eight-site-rank4-source-regulator-fold-chambers.json`

Allocator claim: `seqclaim-1507e061059623922a0b098f`.

Epistemic graph event: `ev-000000002355-e58b207d-b37e-4f39-a02b-02f43979f43c`.

## Next falsifier

Recover the exact source change of variables from \((X_i,y_e)\) and their positive regulators to the B8 companion coordinates \((a,b,c,d,z,k,l)\).  Project the full positive cone to the B8 fold normal.  A crossing proves the last eight occurrences unselected; a pointed image contained in one homotopy chamber supplies the first source-selected C8 fold line.
