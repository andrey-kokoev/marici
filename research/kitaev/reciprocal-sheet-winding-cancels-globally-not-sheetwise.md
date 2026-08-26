# Reciprocal-Sheet Winding Cancels Globally, Not Sheetwise

Let \(u_+,u_-\) be normalization units on an annulus, attached to reciprocal
sheets, with

\[
\nu(u_-)=-\nu(u_+).
\]

Then their combined normalization has zero winding:

\[
\nu(u_+u_-)=0.
\]

Hence the product admits a global logarithm and a global square root. This is
pairwise normalization closure.

It does not imply sheetwise closure. Each sheet admits a global square root
only when

\[
\nu(u_+)\equiv\nu(u_-)\equiv0\pmod2.
\]

For odd reciprocal winding, both sheets carry the same nontrivial \(C_2\)
class because \(-1\equiv1\pmod2\), while their sum vanishes:

\[
\chi(u_+)+\chi(u_-)=0\quad\text{in }C_2.
\]

Thus the two-sheet Ubersector can be globally normalized even though neither
sheet possesses an individual square-root frame.

## Smallest exact hostile

The reciprocal pairs

\[
(u_+,u_-)=(z,z^{-1})
\]

and

\[
(u_+,u_-)=(z^2,z^{-2})
\]

both have combined product one and both take the vacuum value one at \(z=1\).
The first pair has odd winding and no sheetwise square roots. The second pair
has even winding and admits roots \((z,z^{-1})\). Therefore the completed
scalar product and vacuum normalization are jointly blind to the sheetwise
obstruction.

## Constructor hierarchy

Three constructions must not be interchanged:

1. **Combined scalar closure:** trivialize \(u_+u_-\).
2. **Sheetwise frame existence:** trivialize each parity class.
3. **Sheetwise frame selection:** after existence, use the source vacuum to
   choose the signs.

The first is invariant under reciprocal winding transfer

\[
(\nu_+,\nu_-)
\longmapsto
(\nu_++k,\nu_--k).
\]

Hence the combined scalar lives on a quotient that erases an integer torsor,
and in particular its parity. Recovering the sheetwise frame requires a
source-resolved winding port; a single scalar product cannot do so.

## Theta/Tate consequence

A reciprocal Fourier–Tate completion may have a perfectly well-defined total
determinant or energy while its individual sheet normalizations remain
topologically obstructed. This is a concrete mechanism for

\[
\text{global scalar closure}
\ne
\text{sheet-resolved constructor closure}.
\]

Grothendieck should therefore compute the winding of each source sheet before
using the reciprocal product to infer a canonical split. Pairwise cancellation
is evidence for the Ubersector only, not for either constituent sheet.

## Falsifiers

- Zero total winding is used to infer zero winding on each sheet.
- A square root of the product is factored into sheetwise square roots without
  an evenness theorem.
- Vacuum normalization of the product is used to choose individual frames.
- Reciprocal transport erases the integer displacement before its parity is
  recorded.
- Global scalar closure is reported as an operator-valued sheet lift.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The target was to decide whether reciprocal-sheet completion removes
the winding obstruction or merely hides it.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Reciprocal winding cancels in the total scalar while surviving on both
sheets as the same parity class; the exact quotient and missing port are now
explicit.
