# Exact native baryon factorization into a 12-by-3 field

## Result

Both native 36-coordinate baryon operator pairs admit an exact grid
factorization. It is reconstructed from the actual nonzero-support blocks and
rank-one return, not fitted from their advertised channel counts.

The fine projector has 12 disjoint blocks of size 3. The coarse projector has
3 disjoint blocks of size 12. Each fine/coarse block pair intersects in exactly
one coordinate, defining a unique grid once block order is fixed.

P uses fine=L, coarse=G. N uses fine=G, coarse=L.

## Phase/amplitude gauge and metric

Let z be the actual nonzero first column of the native rank-one return
projector. All 36 entries are nonzero. Write the original state as

```
x_i = z_i y_i.
```

The induced metric on y is `w_i = m_i |z_i|^2`, retaining the original physical
inner product rather than replacing it by an identity metric. Under this
invertible diagonal coordinate change, the common surviving state is constant.

On the derived grid, the checker proves exactly

```
w_ij * total = rowWeight_i * columnWeight_j.
```

Thus the metric weights separate into a product. Every full operator
coefficient agrees with

```
Fine   = I_12 tensor A_3
Coarse = A_12 tensor I_3
Return = A_12 tensor A_3
```

A_3 and A_12 are the corresponding weighted-mean projectors. Both orders of
Fine/Coarse give the same return. This explains the ranks 12,3,1 using the
actual native phase/amplitude data and transported metric.

## Weights are part of the structure

For P, the twelve-way weights are uniform 1/12, while the three-way weights
are (1/15,7/15,7/15) in the source-derived grid order.

For N, the three-way weights are uniform 1/3; the twelve-way weights are
nonuniform and retained exactly in the receipt. The two species therefore
share the factorization pattern while exchanging fine/coarse roles. Their
source weights are not silently identified or discarded.

## What this gives T

A concrete field architecture now exists: one 12-by-3 array, two commuting
weighted projections along its two directions, and a shared constant mode in
the transformed coordinates. Source phases/amplitudes are encoded by z and the
metric. P/N are the opposite assignments of these two projection tasks.

The algebraic tensor directions have not yet been identified with geometric
M,C or R on the glued simplex. Nor does the factorization establish that every
row/column permutation is a permitted native physical symmetry; native marked
histories, metrics and operation dictionaries still constrain those actions.
The E field has not been included in this factorization.

## Verification

Exact arithmetic checks both native carriers, all 36-coordinate operator
entries, metric separability and both projection compositions. Source files,
production generator and viewer remain unchanged.

```sh
python research/strominger/checkers/check_baryon_tensor_grid.py
```

Evidence: `results/baryon-tensor-grid/verification.json`, containing the derived
grid, every source coordinate label, the complex gauge vector, induced metric,
normalized weights and hashes.
