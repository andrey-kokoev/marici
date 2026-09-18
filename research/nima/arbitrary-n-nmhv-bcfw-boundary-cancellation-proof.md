# Arbitrary-n NMHV BCFW boundary cancellation

## Theorem

For every integer `n>=6`, consider the oriented five-bracket cells

$$
C_{i,j}=[n,i-1,i,j-1,j],
\qquad
2\le i\le n-2,
\qquad
i+2\le j\le n-1.
$$

With the simplicial boundary convention

$$
\partial[v_0,v_1,v_2,v_3,v_4]
=\sum_{k=0}^4(-1)^k
[v_0,\ldots,\widehat v_k,\ldots,v_4],
$$

every internal facet occurs exactly twice with opposite orientation, while every external facet occurs exactly once. Consequently the oriented boundary of the NMHV BCFW sum contains only physical facets.

The numbers of cells, external facets, and internal unoriented facets are

$$
N_{\rm cell}=\frac{(n-3)(n-4)}2,
$$

$$
N_{\rm phys}=\frac{n(n-3)}2,
$$

$$
N_{\rm spur}=(n-5)(n-3),
$$

and they obey

$$
5N_{\rm cell}=N_{\rm phys}+2N_{\rm spur}.
$$

## Proof

Write `F_k(i,j)` for the facet obtained from `C_(i,j)` by deleting its `k`th displayed vertex, numbered from zero. Every internal facet belongs to exactly one of three disjoint pairing families.

### Horizontal pairing

If `j>=i+3`, then

$$
F_1(i,j)
=[n,i,j-1,j]
=F_2(i+1,j).
$$

The two boundary coefficients are `(-1)^1=-1` and `(-1)^2=+1`. The displayed vertex orders agree, so the oriented contributions cancel.

### Short-diagonal pairing

If `j=i+2` and `(i,j)!=(n-3,n-1)`, then

$$
F_1(i,i+2)
=[n,i,i+1,i+2]
=F_4(i+1,i+3).
$$

The coefficients are `-1` and `+1`, again in identical vertex order.

### Vertical pairing

If `j<=n-2`, then

$$
F_3(i,j)
=[n,i-1,i,j]
=F_4(i,j+1).
$$

The coefficients are `(-1)^3=-1` and `(-1)^4=+1`.

These pairings are exhaustive. Facets of types `F_1,F_3` have the listed successor whenever their index lies away from the indicated boundary. Facets of types `F_2,F_4` are the corresponding unique successors. The three formulas have distinct deleted-position pairs `(1,2)`, `(1,4)`, and `(3,4)`, so no facet is paired twice.

The unpaired facets are exactly:

1. every `F_0(i,j)`, contributing `N_cell` facets;
2. `F_1(n-3,n-1)`, contributing one;
3. every `F_2(2,j)`, for `4<=j<=n-1`, contributing `n-4`;
4. every `F_3(i,n-1)`, for `2<=i<=n-3`, contributing `n-4`;
5. `F_4(2,4)`, contributing one.

Each contains two disjoint cyclically adjacent label pairs and is therefore a physical NMHV boundary. Their total is

$$
N_{\rm cell}+2(n-4)+2
=\frac{n(n-3)}2.
$$

All remaining facets are paired internal boundaries. Hence

$$
N_{\rm spur}
=\frac{5N_{\rm cell}-N_{\rm phys}}2
=(n-5)(n-3).
$$

The opposite signs in each pairing family prove oriented cancellation for every `n>=6`.

## Relation to executable evidence

`check_nmhv_bcfw_oriented_boundary_cancellation.py` and `check_nmhv_bcfw_boundary_count_formula.py` verify the same involution and counts for `6<=n<=50`. Those computations are regression tests; the universal claim follows from the three explicit pairing formulas and boundary classification above.

## Claim boundary

This proves arbitrary-multiplicity cancellation of codimension-one internal boundaries in the standard NMHV BCFW five-bracket chain and gives the exact boundary counts. It does not prove normalized physical residues, equality of distinct triangulations beyond relations already established separately, or a general `N^kMHV` boundary theorem.
