# 1789 — The Five-Site (g_5) Pinch Survives the Complete Source Sum

## Question

Entry 1788 proves that one free (C_5)-orbit satisfies the geometric real
pinch conditions. Can its double residue cancel after summing all terms of the
frozen 180-term five-cycle canonical function?

## Frozen residue packet

The wall (g_5) belongs to the common prefactor. Exactly 26 source terms
contain the labelled wall (G^-_{e12}). For each term:

1. remove (g_5) and (G^-_{e12});
2. retain every remaining common and term-specific denominator;
3. evaluate on the unique source-labelled (g_5) assignment from Entry 1788;
4. include the source double-Leray Jacobian (1/2);
5. sum all 26 contributions before testing nonvanishing.

No term is removed by magnitude or sign.

## Two real loop sheets

The three labelled distances determine two loop points, related by reflection
across the plane of the three routing foci. Their remaining internal energies
are reconstructed from the frozen regular-cone routing.

Numerically, the complete residue sums are

\[
R_-\approx-0.10007764942068838,
\qquad
R_+\approx-0.08226159469974444.
\]

The nearest unused source denominator has absolute value approximately

\[
0.0932\quad\text{and}\quad0.1847
\]

on the two sheets, respectively.

## Exact interval certificate

The proof does not rely on those decimals. Isolate the (g_5) Landau root by
an exact rational Sturm interval, propagate rational interval bounds through:

- the rational-univariate function (p(x));
- the nested square roots for (y_i,y_j,y_e);
- the exact regular-pentagon routing coordinates;
- both reflected loop points;
- all five internal edge energies;
- every remaining denominator in all 26 terms;
- the complete rational residue sum.

Every division interval excludes zero. On each sheet, the final exact rational
interval is strictly negative.

Therefore

\[
\boxed{
R_-\neq0,
\qquad
R_+\neq0.
}
\]

## Result

\[
\boxed{
\text{The complete frozen source canonical function does not cancel the
surviving }g_5\text{ pinch.}
}
\]

By (C_5)-naturality, the same noncancellation statement holds for all five
labelled occurrences in its free orbit.

## Remaining qualification

This establishes a nonzero source coefficient at an interior, nondegenerate,
same-sign Landau pinch. The final physical statement still requires the
oriented Picard–Lefschetz intersection number of Entry 1783's canonical
double-Leray germ with the local Morse thimble. In particular, the relative
orientation of the two reflected loop points must not be inferred from the
common sign of their scalar residues.

## Evidence

- `research/benincasa/checkers/five_site_g5_source_residue.py`
- `research/benincasa/results/five-site-g5-source-residue.json`
- allocator claim: `seqclaim-bb9a22403e36282adc948d2c`
