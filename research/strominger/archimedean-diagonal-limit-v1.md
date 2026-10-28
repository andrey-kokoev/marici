# The common diagonal and a controlled centered packet limit

## Result

The diagonal of the [physical archimedean packet matrix](archimedean-cutoff-entry-v1.md) now has an explicit convergent finite-part formula and an error bound. Together with the off-diagonal estimates, this controls the entire centered5x5 packet matrix in the declared even archimedean sector.

This is an analytic integral representation, not a numerical quadrature value or a positivity result. The rational checker certifies the constants and rate bookkeeping; the continuum argument is given below.

## Correct counterterm

Let

    c(s) = integral p_0(u) p_0(u-s) du,
    d = c(0) = integral p_0(u)^2 du.

The autocorrelation is even, smooth and supported on `[-log2,log2]`. Translation of p_0 multiplies its Mellin transform by a unitary phase, so all five operators `A_j A_j*` coincide. Thus every diagonal entry is the same T_00(Lambda).

The reference/volume matrix is

    2 log(Lambda) d I5.

It is **not** `2 log(Lambda) d T* T`, where T is the encoder's endpoint/flux observation matrix. Those are different norms. In particular T* T has nonzero off-diagonal entries, while the actual source volume matrix is diagonal because packet supports are disjoint.

## Isolating the singular part

Put

    a = 2 pi Lambda^2,
    x = exp(s)-1,
    eta = 1/2,
    f(x) = c(log(1+x))/sqrt(1+x),
    h(x) = f(x) - d 1_{|x|<=eta}.

The x-support is `[-1/2,1]`, and f(0)=d. The physical kernel from the preceding construction gives

    T_00 = (1/pi) integral_{-1/2}^1 f(x) Si(a x)/x dx
         + (1/pi) integral_{-log2}^{log2}
             c(s) exp(s/2)/(1+exp(s)) Si(a(1+exp(s))) ds.

Only the first integral is singular in the limit. Splitting off the constant d gives its scalar part

    (2d/pi) I(a eta),
    I(X) = integral_0^X Si(t)/t dt.

The standard Mellin identity

    integral_0^infinity t^(z-1) sin(t) dt = Gamma(z) sin(pi z/2)

and its derivative at z=0 give `integral log(t) sin(t)/t dt = -pi EulerGamma/2`. Integration by parts then yields

    I(X) = (pi/2)(log X + EulerGamma) + E(X),
    |E(X)| <= 2/X.

The error follows by integrating `|Si(t)-pi/2|/t <= 2/t^2` from X to infinity. This fixes the subtraction constant; it is not fitted from finite cutoffs.

## Explicit finite part

Since eta=1/2, subtracting `2d log(Lambda)` leaves

    F = d(log pi + EulerGamma)
      + (1/2) integral_{-1/2}^1 h(x)/|x| dx
      + (1/4) integral_{-log2}^{log2} c(s)/cosh(s/2) ds.

All these integrals converge ordinarily. Near zero, h(x)=O(|x|), so no principal-value ambiguity remains. The jump of the chosen subtraction indicator at |x|=eta is away from the singular point and harmless. Choosing another admissible subtraction radius changes the scalar and integral pieces compensatingly, not the physical limit.

## Explicit error bound

The compact bump profile gives usable coarse constants without quadrature:

- `1/3 < epsilon < 1/2`;
- on `|u|<=epsilon/2`, `phi(u)>=exp(-1/3)>2/3`, hence `A>2/9`;
- `100/121 <= d <= 9/2`;
- `|phi'|<=8/epsilon`, hence `sup|c'|<=108`;
- on `|x|<=1/2`,

      |f'(x)| <= 2 sqrt2 (sup|c'|+d/2) <= M=1323/4.

The derivative bound for phi follows by writing `y=1/(1-(u/epsilon)^2)`: `y^2 exp(1-y)<=4/e<4`. The lower bound on d is Cauchy–Schwarz together with `integral p_0>=10/11` and support length log2<1.

Split the subtracted singular integral at |x|=1/a. Use

    |Si(y)-sign(y)pi/2| <= min(pi/2, 2/|y|).

The near-zero part costs at most M/a; the middle part costs at most `4M log(a/2)/(pi a)`; the outer positive interval contributes at most `2d/(pi a)`. The scalar correction costs `8d/(pi a)`. The smooth cosine term contributes at most `4/(9a)`, using `integral c <=1`.

Therefore

    |T_00 - 2d log(Lambda) - F|
      <= [M(1+(4/3)log(a/2)) +139/9]/a.

For `Lambda=2^k`, k>=1, pi in(3,4) and log2<1 give the fully rational bound

    E_k = [ (1323/4)(1+8(k+1)/3) +139/9 ] / (6*4^k).

The checker records bounds through Lambda1024, where E_k is below1/100. The estimates are deliberately coarse; no claim of optimal convergence rate is made.

## Whole packet matrix

Subtract `2d log(Lambda) I5` from the physical ordered matrix. Its common diagonal converges to F. Every off-diagonal entry converges to the prior absolutely convergent integral, and the opposite ordered entries have the same limit.

If C is the largest certified off-diagonal error constant, then in the standard coefficient2-norm

    ||centered_matrix(Lambda) - limit_matrix|| <= E_k + 4C/Lambda^2.

This follows from row/column sum bounds and does not assume the finite-cutoff matrix is Hermitian. The limiting matrix is real symmetric. No sign of its spectrum is inferred from convergence.

The code also gives a deliberately broad finite-part enclosure from `0<=EulerGamma<=1`, `1<log pi<2` and the integral bounds. It spans both signs and is not a substitute for numerical evaluation.

## Remaining gate

This controls a particular finite packet in one physical sector. Next compare its limiting form with the retained analytical witness data and its native-field pullback. Computing a limit does not identify those higher witnesses, prove positivity, or extend the construction to all semilocal sectors or the114-record channel.

```sh
python research/strominger/checkers/check_archimedean_diagonal_limit.py
```

- [Frozen subtraction and rate contract](contracts/archimedean-diagonal-limit.v1.json).
- [Finite-part expression and cutoff bounds](results/archimedean-diagonal-limit.json).
- [Verification receipt](results/archimedean-diagonal-limit-verification.json).
