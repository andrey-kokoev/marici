# The unweighted conjugation graph has no Fredholm determinant limit

Write a free conjugation correspondence as an orthogonal sum of two-point
swap blocks

```
J_j = [0 1; 1 0].                                      (1)
```

At a cutoff containing `m` conjugate pairs, the graph operator

```
J_(m)=direct_sum_(j=1)^m J_j                            (2)
```

has `2m` singular values equal to one. Hence

```
||J_(m)||_1=2m,              ||J_(m)||_2=sqrt(2m).      (3)
```

The infinite unweighted graph operator is unitary, not compact. It is neither
trace class nor Hilbert--Schmidt. Consequently no ordinary Fredholm
determinant `det(I+zJ)` or Carleman--Fredholm determinant `det_2(I+zJ)` is
defined by the standard Schatten theory for nonzero constant `z`.

The finite determinants expose the same failure. Each pair contributes

```
det(I-z J_j)=1-z^2,                                    (4)
```

so

```
det(I-z J_(m))=(1-z^2)^m.                              (5)
```

For fixed generic `z`, this does not stabilize to a nonzero entire cutoff
limit. A regularization cannot be omitted or hidden in the word
"determinant."

## Exact weighted threshold

For weighted blocks `w_j J_j`, the singular value `|w_j|` occurs twice.
Therefore

```
W is trace class       iff sum_j |w_j| < infinity,
W is Hilbert--Schmidt  iff sum_j |w_j|^2 < infinity.   (6)
```

In the trace-class case the ordinary Fredholm determinant is available. In
the Hilbert--Schmidt-only case the canonical candidate is the regularized
determinant

```
det_2(I+W)=det((I+W)exp(-W)),                           (7)
```

whose zeros, with algebraic multiplicity, still occur exactly when `-1` is
an eigenvalue of `W`. The subtracted linear trace is part of the
regularization data and must be restored independently if the target
normalization requires it.

For block weights, finite `det_2` factors are explicitly obtained from
`det(I+w_j J_j)=1-w_j^2`; since each block has trace zero, the first-order
exponential correction is trivial blockwise. Convergence is controlled by
the square sum of the weights.

## Consequence for the two-channel correspondence

The operator-valued two-channel square cannot use the bare graph projector as
its determinant-class perturbation. It needs source-derived decay weights or
a relative determinant in which the unweighted graph cancels against a
reference operator. The alternatives are sharply separated:

1. absolute Fredholm determinant: prove trace-class decay;
2. regularized `det_2`: prove Hilbert--Schmidt decay and account for the
   removed trace term;
3. relative determinant/torsion: exhibit a reference and prove their
   difference is determinant class.

The previously defined Xi reflection-defect operator is Hilbert--Schmidt, so
it demonstrates that the second analytic type is consistent after using the
zero divisor. It is not a source construction because its weights already
come from the zeros.

## Falsifier and next target

A proposal fails if it takes a Fredholm determinant of the unweighted
infinite copy or conjugation operator, or if it asserts cutoff convergence
without a summability estimate. The next source-side target is an arithmetic
weighting of the growing incidence square with a proved Schatten bound,
followed by an independently normalized `det`, `det_2`, or relative torsion.

This is a determinant-class obstruction theorem. It neither constructs the
weights nor proves RH.
