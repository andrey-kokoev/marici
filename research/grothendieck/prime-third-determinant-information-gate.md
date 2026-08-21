# The third regularized prime determinant reaches the critical line but carries no zeta zeros there

For `P_s e_p=p^(-s)e_p`, the Schatten condition is

```
P_s in S_q  iff  sum_p p^(-q Re(s))<infinity.          (1)
```

On the critical line `Re(s)=1/2`, this holds for every `q>2`; in particular
`P_s` belongs to `S_3`. The third regularized determinant is therefore
well-defined:

```
det_3(I-P_s)
 =product_p (1-p^(-s))
   exp[p^(-s)+p^(-2s)/2].                              (2)
```

Its logarithm retains only repetitions `k>=3`:

```
-log det_3(I-P_s)
 =sum_p sum_(k>=3) p^(-ks)/k.                          (3)
```

The removed `k=1` and `k=2` channels are precisely the terms that prevent
the ordinary Fredholm determinant from reaching the critical line.

## Zero-information obstruction

For `Re(s)>0`, every eigenvalue obeys `|p^(-s)|<1`; hence no factor
`1-p^(-s)` vanishes. The exponential factors never vanish. Therefore

```
det_3(I-P_s) != 0       for Re(s)>0.                   (4)
```

In particular, the third regularized determinant has no Riemann zeros on
the critical line. Any completed factorization must write schematically

```
zeta(s)
 =det_3(I-P_s)^(-1) exp[C_1(s)+C_2(s)],                (5)
```

where the analytically regularized low-order prime channels `C_1,C_2` carry
all zero-producing information. Merely observing that `det_3` exists does
not construct zeta spectrally; it moves the hard problem into the
counterterm.

## Domain gain

The map `s -> P_s` is `S_3`-valued in `Re(s)>1/3`, so (2) gives a genuine
holomorphic nonvanishing determinant across the critical line. This is still
useful as a canonical high-repetition factor. It isolates a finite set of
renormalization channels rather than leaving an undifferentiated divergent
Euler product.

## Research target

Construct `C_1` and `C_2` jointly with the oscillator gamma determinant and
endpoint factors as a relative determinant or anomaly. The construction
must:

1. be canonical and reflection compatible;
2. reproduce analytic continuation of the completed logarithmic derivative;
3. explain, rather than assume, its zero set; and
4. preserve the odd-source/skew-adjoint mechanism.

## Falsifier

A proposal fails if it identifies `det_3(I-P_s)` alone with zeta or claims
that its existence on the critical line explains zeta zeros. Equation (4)
shows it is nonvanishing there.

