# One Schur operator forces the two anomalous prime coefficients

For a finite or trace-class Schur self-energy `X`,

```
log det(I-X) = -sum_(n>=1) Tr(X^n)/n.                (1)
```

The first two terms are therefore

```
-Tr X - (1/2)Tr X^2.                                 (2)
```

If the Euler-region eigenvalues of `X` are `p^(-s)`, these are exactly

```
-sum_p p^(-s) - (1/2)sum_p p^(-2s).                 (3)
```

Thus the coefficients `1` and `1/2` are not separate normalization choices.
They are forced by the logarithm of a single determinant. The two anomalous
channels are the linear and quadratic shadows of one operator-valued Schur
correspondence.

## Critical-line regularization

At `Re(s)=1/2`, the model prime operator belongs to `S_3` but not `S_2`, so
the terms in (2) are precisely the two undefined ordinary traces removed by
`det_3`. A coefficient--Betti mapping cone must make their **relative
supertraces** meaningful:

```
Str X_rel,       Str X_rel^2.                         (4)
```

The higher powers are already trace class. This is the operator form of the
two-channel continuation anomaly.

The cancellation cannot be performed by two independent scalar
renormalizations. Both terms must come from the same `X_rel`; otherwise the
determinant logarithm, multiplicative compatibility, and finite Euler
cutoff are lost. Nor may an exactly identical acyclic pair cancel every
supertrace: that would give torsion one and erase the desired interaction.
The physical coupling must leave a nontrivial relative Schur class while the
auxiliary bulk remains index zero.

## Refined construction target

Construct one reflection-compatible operator family `X_rel(s)` from the
physical Jacobi block, the paired smoothing tail, and the coefficient--Betti
coupling such that:

1. in `Re(s)>1`, its determinant reduces to the finite Euler Schur
   determinant and (3);
2. on the critical line, its first two relative supertraces exist jointly;
3. its `n>=3` trace series agrees with the canonical `det_3` background;
4. its determinant phase gives the residual spectral shift;
5. its Hermitian boundary realization comes from the reflection adjoint, not
   from replacing complex local Euler factors one by one with positive ones.

This target is narrower than “find two counterterms”: find one relative
Schur operator whose determinant automatically generates both.

