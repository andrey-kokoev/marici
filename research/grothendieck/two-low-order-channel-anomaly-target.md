# The third prime determinant isolates exactly two anomalous channels

Let `P_s e_p=p^(-s)e_p`. On the critical line `P_s` lies in every Schatten
class `S_q` with `q>2`, hence in `S_3`, while it is not Hilbert--Schmidt. The
third regularized determinant is

```
det_3(I-P_s)
 = product_p (1-p^(-s)) exp[p^(-s)+p^(-2s)/2].         (1)
```

Its logarithm retains precisely the prime repetitions `k>=3`. In the honest
Euler half-plane,

```
zeta(s)^(-1)
 = det_3(I-P_s) exp[-C_1(s)-C_2(s)],                   (2)

C_1(s)=sum_p p^(-s),
C_2(s)=(1/2)sum_p p^(-2s).                             (3)
```

Thus the Schatten threshold does not leave an arbitrary counterterm. It
isolates exactly two low-order channels. This matches the smallest
two-channel correspondence architecture structurally:

- channel one is the linear prime source;
- channel two is the quadratic Hermitian/norm source;
- `det_3` is the convergent higher-repetition background.

## Why the match is not yet a solution

On the critical line, `C_1` lacks absolute convergence and `C_2` contains the
harmonic-prime divergence. Analytically continuing these scalar sums by
declaring (2) to hold imports zeta and is circular.

Moreover, exponentials of finite analytic scalar counterterms never vanish.
If `C_1` and `C_2` are independently regularized as ordinary analytic
functions, they cannot create the Riemann zeros omitted by the nonvanishing
`det_3`. The zero-producing information must therefore appear as a failure
of independent scalar exponentiation: a coupled determinant-line anomaly,
singular Schur complement, or relative torsion involving gamma and endpoint
channels before scalarization.

This clarifies the role of the two-channel four-cycle. It should not merely
place `C_1` and `C_2` on a diagonal. Its crossed route must encode their joint
renormalization against the archimedean and polar terms. Only the coupled
object may be scalarized.

## Exact finite-cutoff bookkeeping

At a finite prime cutoff every expression is elementary. For each local
variable `x=p^(-s)`,

```
log(1-x) = -x-x^2/2-sum_(k>=3)x^k/k.                  (4)
```

The third determinant removes exactly the first two terms, no more and no
less. This identity fixes the channel multiplicities and coefficients before
continuation. Any proposed two-channel lift must reduce to these coefficients
in the Euler region.

## Falsifiers

A proposal fails if:

1. it identifies the nonvanishing `det_3` background with zeta;
2. it defines `C_1,C_2` by analytic continuation of zeta rather than source
   renormalization;
3. it exponentiates two independently entire scalar counterterms and still
   claims they create zeros;
4. it changes the forced coefficients `1` and `1/2` of the low repetitions;
5. it couples the prime channels only after scalarization.

## Next target

Construct a two-channel relative complex whose finite-cutoff logarithmic
torsion equals `C_1+C_2` in the Euler half-plane, whose crossed
prime--gamma--endpoint renormalization is source-defined, and whose product
with `det_3(I-P_s)` extends to completed Xi. This is now the narrowest
zero-producing determinant anomaly compatible with the known Schatten
facts. No such complex is presently constructed.
