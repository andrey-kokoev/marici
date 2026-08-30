# Pure noncompact convolution cannot have the discrete Xi spectrum

Let `G` be a noncompact locally compact abelian source group and suppose a
translation-invariant operator Fourier-diagonalizes as multiplication by a
measurable function `m` on a nonatomic part of `G_hat`:

```
F T F^-1 = M_m.                                        (1)
```

For a resolvent point `z`,

```
(M_m-z)^(-1)=M_(1/(m-z)).                              (2)
```

A nonzero multiplication operator on a nonatomic `L2` space is not compact.
Indeed, on some positive-measure set its modulus is bounded below by an
`epsilon>0`; splitting that set into infinitely many disjoint positive-
measure pieces gives an orthonormal sequence whose images remain separated.

Therefore a pure translation-invariant convolution operator on the
noncompact logarithmic line cannot have compact resolvent. It cannot by
itself possess a discrete spectrum escaping to infinity like the Xi zero
ordinates.

## Compatibility with the odd-source theorem

Oddness still forces skew-adjointness, but it does not force discreteness:

```
odd real convolution  =>  skew-adjoint continuous multiplier,
not                     =>  Xi spectral operator.      (3)
```

This separates two jobs that a successful source construction must perform:

1. source-leg antisymmetry must force the critical-line/skew-adjoint
   condition;
2. an archimedean or geometric mechanism must provide confinement and
   compact resolvent.

## Admissible escape routes

A viable model must do at least one of the following:

1. add a confining term that breaks translation invariance while preserving
   the adjoint symmetry;
2. pass to a finite-volume quotient with a nontrivial coefficient bundle;
3. use a noncommutative crossed-product/transfer operator whose resolvent can
   be compact; or
4. realize Xi zeros as resonances rather than ordinary eigenvalues, with a
   separately proved reality mechanism.

The completed gamma factor is the natural candidate to supply confinement,
but no operator identity doing so has been derived.

## Finite-window falsifier

For the skew multiplier `m(x)=ix` on `[-1,1]`, the resolvent at `z=1` has

```
|(ix-1)^(-1)|^2=1/(1+x^2)>=1/2.                       (4)
```

Every refinement of the window therefore produces more orthogonal modes
whose resolvent norms stay at least `1/sqrt(2)`, the finite-dimensional
shadow of noncompactness.

