# All four thimble columns remain compatible with the completed relative-boundary data

## Purpose

After closing the finite and four-endpoint sewing calculations, test whether those data actually select an integral ambient thimble/Gysin column.

## Four ambient lattices

For each

\[
(a,b)\in\{0,1\}^2,
\]

define

\[
L_{a,b}
=
\frac{
\mathbb Z\langle e_6,v_{\rm alg},m\rangle
}{
\langle2m-ae_6-bv_{\rm alg}\rangle
}.
\]

Every candidate has the same rational split extension and the same elliptic width-two quotient. The completed relative-boundary contribution

\[
2v_{\rm alg}
\]

is an even element of the algebraic kernel in every \(L_{a,b}\). The principal endpoint splitter is likewise available independently of \((a,b)\).

The closed physical infinity Leray functional annihilates \(e_6\) and \(v_{\rm alg}\), so it also cannot distinguish two lifts differing by either algebraic generator.

## Exact compatibility result

All four columns

\[
(0,0),\quad(1,0),\quad(0,1),\quad(1,1)
\]

satisfy simultaneously:

1. the source width-two elliptic monodromy;
2. the primitive free generic infinity-Gysin sequence;
3. the even wall-plus-endpoint contribution;
4. the integral principal endpoint divisor;
5. the physical Leray functional's vanishing on the algebraic kernel;
6. the local Legendre thimble relation.

Thus the newly recovered endpoint packets do not determine the ambient column.

## Consequence

The desired column cannot be inferred by further composition of existing scalar residue, endpoint, or Leray packets. It requires genuinely new chain-level data: an ambient lift and one integral intersection with each algebraic dual.

This is a constructive underdetermination certificate, not merely an absence search: four explicit integral presentations realize all four answers while reproducing every currently available invariant.

Verification:

- `research/voevodsky/checkers/check_four_thimble_column_models.py`
- `research/voevodsky/results/four_thimble_column_models.json`
