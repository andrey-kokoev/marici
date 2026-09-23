# The eight-point positive fibre is curved: the seven-point polygon method does not scale

The fixed-target seven-point section method is genuinely special to `n=7`. At **eight** points, even a target with a strictly positive source can have a nonpolyhedral positive `CZ` fibre.

Take rank-two source matrices with eight columns and strictly positive moment-curve external data

    Z_j=(1,j,j²,j³,j⁴,j⁵),  j=1,...,8.

The left kernel of `Z` has dimension two. Two independent vectors are

    k0=(1,-6,15,-20,15,-6,1,0),
    k1=(0,1,-6,15,-20,15,-6,1).

Start with source rows

    x=(1,1,1,1,1,1,1,1),
    y=(1,1,2,3,4,5,6,7).

The only vanishing ordered minor is 12; every other ordered minor is strictly positive. Fix the target `Y=CZ` and examine the two-dimensional AFFINE slice of its source fibre

    C(a,b)=C+[a*k0; b*k1].

Every matrix in this slice has exactly the same `CZ`. But its first ordered minor is

    Delta12(C(a,b))=7a+b+ab.

Near `(0,0)` all other ordered minors remain strictly positive. Thus the boundary of the positive fibre in this slice is locally the **curved** graph

    b=-7a/(1+a),

whose second derivative is `14/(1+a)^3`, not zero. Two independently checked positive boundary points are `(1/10000,-7/10001)` and `(1/5000,-7/5001)`; the minimum of their other 27 ordered minors is respectively `24637341/25002500` and `6068591/6251250`. Their midpoint has `Delta12=7/400120008`, not zero. The target is not merely a boundary target: `C(0,1/10000)` has ALL 28 ordered minors strictly positive and the same `CZ`.

An affine slice of a polyhedron must itself be polyhedral. A genuine curved smooth boundary segment cannot be a union of finitely many straight facets. Hence this admitted eight-point positive fibre is **not polyhedral**. The obstruction is the mixed `ab` coefficient resulting from independent kernel vectors entering the two source rows. At seven points there is only one kernel vector, and the analogous quadratic term cancels identically in every minor.

This changes the research frontier. The exact seven-point halfspace/Farkas/active-set procedure cannot be promoted verbatim to an arbitrary-`n` positive-cell compiler, let alone to an analytic `n^-2` completion law. At eight points a replacement must handle polynomial or semialgebraic fibre constraints, find a different affine carrier, or avoid fibre-section optimization. This result does **not** falsify the eight-point history/form matches already recorded elsewhere, nor rule out arbitrary-`n` positive-cell constructions by other means.

Run `python research/nima/checkers/check_eight_point_fibre_curvature.py`; packet `research/nima/results/eight-point-fibre-curvature.json`.
