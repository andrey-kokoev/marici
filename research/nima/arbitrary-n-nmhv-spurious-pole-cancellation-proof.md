# Arbitrary-n NMHV spurious-pole cancellation

## Theorem

For every `n>=6`, every spurious codimension-one pole in the standard momentum-twistor NMHV BCFW representation

$$
\mathcal A_n^{\rm NMHV}
=
\sum_{2\le i\le n-2\atop i+2\le j\le n-1}
[n,i-1,i,j-1,j]
$$

occurs in exactly two five-brackets, and their residues cancel with opposite orientation. Hence the complete sum has no spurious codimension-one pole.

## Facet pairing

The arbitrary-n boundary involution partitions all internal facets into three families:

$$
F_1(i,j)=F_2(i+1,j)
\qquad (j\ge i+3),
$$

$$
F_1(i,i+2)=F_4(i+1,i+3),
$$

$$
F_3(i,j)=F_4(i,j+1)
\qquad (j\le n-2),
$$

with the previously stated endpoint exclusions. In each equality, the common four labels occur in the same displayed order. The simplicial boundary coefficients on the two sides are respectively

$$
(-1,+1),
\qquad
(-1,+1),
\qquad
(-1,+1).
$$

Thus every internal facet has incidence two and opposite induced orientation.

## Residue cancellation

The canonical form of an oriented simplex has residue equal to the canonical form of its oriented facet. A super five-bracket is precisely this canonical form in momentum-super-twistor coordinates. Therefore, if two cells induce opposite orientations on a common facet `P`, then

$$
\operatorname{Res}_{P=0}R_{C_1}
=-
\operatorname{Res}_{P=0}R_{C_2}.
$$

The facet involution proves that these are the only two BCFW summands singular at a generic point of `P`. Consequently

$$
\operatorname{Res}_{P=0}\mathcal A_n^{\rm NMHV}=0
$$

for every spurious facet.

No componentwise Grassmann expansion is required: cancellation holds for the complete super-residue because it is induced by the oriented facet identity.

## Count

The number of distinct cancelled spurious facets is

$$
N_{\rm spur}=(n-5)(n-3).
$$

Each has incidence two, so the total number of spurious facet incidences is

$$
2(n-5)(n-3).
$$

Together with the physical incidence-one facets, this exhausts the five facets of every BCFW cell.

## Relation to executable evidence

The exact spurious-residue checkers at six through nine points expand the super-residues and verify cancellation component by component. The oriented boundary checker verifies the facet involution through `n=50`. The theorem for arbitrary `n` follows from the three pairing formulas and canonical-form residue orientation.

## Claim boundary

This proves cancellation of generic codimension-one spurious poles in the standard NMHV BCFW representation. It does not prove equality of arbitrary triangulations, control higher-codimension intersections independently, or extend the pairing involution to general `N^kMHV` cells.
