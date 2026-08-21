# The zero-producing spectral shift localizes to two prime channels

On the critical line, the diagonal prime operator `P_s e_p=p^(-s)e_p` lies
in `S_3`. Its canonical third regularized determinant

```
D_3(s)=det_3(I-P_s)
```

is holomorphic and nonzero for `Re(s)>0`; its logarithm contains exactly the
prime repetitions `k>=3`. Thus `D_3` supplies a source-derived smooth boundary
phase on the critical line but no zero or phase jump there.

In the Euler half-plane the missing logarithm is forced to be

```
C_1(s)+C_2(s)
 = sum_p p^(-s) + (1/2)sum_p p^(-2s).                (1)
```

Combining this with the spectral-shift formulation gives a sharper target.
After the gamma reference and `D_3` background are removed, the residual
spectral shift is

```
xi_12(T)
 = -S(T) - (1/pi)arg D_3(1/2+iT)                    (2)
```

up to the global sign and normalization conventions. Every Riemann-zero jump
must occur in the determinant-line object realizing this two-channel
residual, because `D_3` is nonvanishing.

## Why two scalar counterterms cannot work

Independently regularized scalar functions `C_1,C_2` would contribute
`exp(C_1+C_2)`, which is nonzero wherever finite. They can change phase but
cannot supply the zeros. The required object must therefore remain coupled
before scalarization: a singular Schur complement, relative torsion, or
oriented coefficient--Betti determinant whose Euler-region logarithm reduces
to (1).

This reduces the unknown prime coupling from an unrestricted infinite
operator to one precise anomaly problem:

1. retain the canonical `k>=3` `S_3` background;
2. construct a coupled linear/quadratic prime complex with coefficients
   exactly `1` and `1/2`;
3. renormalize it jointly against gamma and endpoint channels;
4. prove its boundary determinant is a self-adjoint perturbation determinant
   with spectral shift (2).

No claim of RH follows. The gain is localization: all zero-producing
information is forced into a two-channel continuation anomaly rather than an
unspecified nonlocal potential.

