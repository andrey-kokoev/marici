# Dilation requires rescaling the spline preconditioner to preserve pole annihilation

## Laplace multiplier

Let the undilated profile be

`phi_a(x)=sum_m c_m k(x+m a)`.

Its bilateral Laplace transform factors as

`Phi_a(s)=K(s) P(exp(-a s))`

up to the fixed translation orientation. For the baseline coefficients,

`P(z)=(z+z^(-1)-5/2)^2`,

whose double zeros are at `z=2` and `z=1/2`.

With `a=2 log 2`, these correspond to centered pole characters `s=plus or minus 1/2`.

## Effect of dilation

For `D_c phi_a(x)=phi_a(c x)`,

`Laplace(D_c phi_a)(s)=c^(-1)Phi_a(s/c)`.

The shift multiplier is therefore

`P(exp(-a s/c))`.

Its double zeros occur at `s=plus or minus c/2`, not at the fixed completed-zeta pole characters `plus or minus 1/2`, unless `c=1`.

To preserve pole annihilation under dilation, the spline shift parameter must be rescaled simultaneously:

`a_c=c a`.

Then

`P(exp(-a_c s/c))=P(exp(-a s))`,

and the pole zeros remain fixed.

## Additional defect in the hybrid checker

The checker uses archimedean dilation `c=1/2` while retaining `a=2 log 2`, but omits pole terms using the undilated annihilator argument. Under the archimedean test actually implemented, the zeros move to `s=plus or minus 1/4`. Thus pole deletion is not justified for that branch.

This is independent of the previously found prime/archimedean coordinate mismatch.

## Repair contract

A scale-parameterized checker must choose one of:

1. rescale `a_c=c(2 log 2)` so pole annihilation is retained;
2. keep `a` fixed and explicitly restore the two pole evaluations.

It must not dilate the profile while reusing the undilated pole-deletion proof.

## Disposition

The frozen baseline theorem has a second normalization defect: omitted pole cells do not vanish for its implemented archimedean dilation. Full regeneration must include scale-covariant preconditioning or explicit poles.
