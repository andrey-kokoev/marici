# The preconditioned septic spline has an explicit compact cubic spectral square root

## Question

Does Fourier nonnegativity of the certified degree-seven spline correspond to an authorized compact autocorrelation packet, so that translated explicit-formula evaluations are genuine Gram entries?

## Cardinal-spline factorization

Let `k_3` and `k_7` be the centered cardinal splines of degrees three and seven in the same normalization. Cardinal splines satisfy

`k_7=k_3*k_3_tilde`.

Both are even, so the reflection may be omitted.

Define the three-shift cubic packet in spline coordinate `u` by

`r_a(u)=(5/2)k_3(u)-k_3(u+a)-k_3(u-a)`.

Its autocorrelation has shift coefficients obtained by convolving

`(-1,5/2,-1)`

with its reversal. In shifts `2a,a,0,-a,-2a`, the result is

`(1,-5,33/4,-5,1)`.

Therefore

`r_a*r_a_tilde`

`=k_7(u+2a)-5k_7(u+a)+(33/4)k_7(u)-5k_7(u-a)+k_7(u-2a)`.

This is exactly the preconditioned septic profile used by the checker.

## Physical log-coordinate normalization

The checker profile is the right-hand side evaluated at `u=x/2`. Set

`g_a(x)=2^(-1/2) r_a(x/2)`.

Changing variables in convolution gives

`g_a*g_a_tilde=f`.

Thus the checked even function is not merely positive definite abstractly; it is the autocorrelation of an explicit compactly supported piecewise-cubic packet.

## Translate Gram identity

For `g_b(x)=g_a(x-b)`, the cross-correlation is

`g_b*g_c_tilde = tau_(b-c) f`

with the sign determined by the declared translation convention. Hence the Hermitian Gram entry of two translated cubic packets is the explicit-formula functional applied to a translate of the checked septic autocorrelation.

For real coefficients, the symmetric cross term is represented by

`(tau_delta f+tau_-delta f)/2`.

At `delta=4 log 2`, this is exactly the seven-shift coefficient vector derived in `first-two-translate-spline-hostile-has-an-explicit-seven-shift-vector.md`.

## Consequence

The two-translate determinant is now source-typed within the declared spline convention. No noncompact spectral square root or arbitrary choice of Fourier phase is involved. If the determinant is negative, the corresponding negative vector is an explicit linear combination of two compact cubic packets.

## Claim boundary

This factorization is an exact spline identity. It does not certify the cross energy, external explicit-formula authority, or global positivity. The physical scaling and translation sign must be regression-tested in the generalized checker.

## Disposition

The analytic prerequisite for the two-translate hostile is closed. The remaining executable step is solely the owned seven-shift interval evaluation and determinant enclosure.
