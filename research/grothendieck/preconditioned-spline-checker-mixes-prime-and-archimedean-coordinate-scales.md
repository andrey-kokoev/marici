# The preconditioned spline checker mixes prime and archimedean coordinate scales

## Defect

The checker defines `shifted_k(u,a)` as the five-shift septic profile in variable `u`.

Its prime term evaluates

`shifted_k(log(q),a)`.

Its archimedean integration, zero-jet scaling, and comments instead use

`f(x)=shifted_k(x/2,a)`.

The factor is visible in `integral_shift`: the change of variables supplies an outer factor two and exponent parameter `c=2b`, exactly corresponding to integrating `shifted_k(x/2,a) exp(-b x)`. The zero jets likewise multiply the `r`th profile derivative by `2^(-r)`.

Therefore the same checker does not apply one test function to both sides:

- prime side uses `u=log(q)`;
- archimedean side uses `u=x/2`, hence would require prime evaluation `shifted_k(log(q)/2,a)` if `x=log(q)`;
- alternatively, retaining prime evaluation at `log(q)` requires archimedean integration of `shifted_k(x,a)` with no factor-two coordinate change.

## Independent symptom

A direct quadrature using the archimedean test `shifted_k(x/2,a)` but applying that same function at `log(q)` produced a prime value far from the checker’s cancellation. The mismatch is not a small quadrature residual; it is the explicit factor-two coordinate split above.

## Consequence

The baseline positive interval and the two-translate negative determinant are values of a hybrid functional assembled from two differently scaled test functions. They are not Gram values of one autocorrelation packet and cannot be mapped to a Weil criterion.

All criterion-level spline claims, including the negative alarm, are retracted pending repair. The interval arithmetic may remain correct for its hybrid executable definition, but that definition is not the declared common test-function form.

## Acceptance test

Choose one coordinate convention and regenerate both baseline and cross results:

1. assert symbolically that the prime evaluation argument and Laplace-integral profile are the same function;
2. run direct quadrature of the archimedean kernel;
3. preserve pole annihilation in the repaired coordinate;
4. retain deliberate prime-sign and factor-two failures;
5. recompute the two-translate determinant only after baseline regression.

## Disposition

The apparent negative Weil packet is explained as a normalization defect. Repair ownership belongs to Nima’s checker locus. No RH interpretation survives.
