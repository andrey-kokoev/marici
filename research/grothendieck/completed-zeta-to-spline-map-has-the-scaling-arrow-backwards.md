# The completed-zeta-to-spline map has the scaling arrow backwards

## Declared transform

The convention packet declares

`h(t)=integral f(2x)e^(itx) dx`.

Let

`g(x)=f(2x)`.

Then `h` is the Fourier transform of `g`, up to the declared sign and normalization. A standard explicit formula written for inverse-Fourier test `g` samples

`g(log n)=f(2 log n)`

on the prime side, not `f(log n)`.

Likewise the Laplace pairing is

`integral_0^infinity g(x)e^(-b x) dx`

`=integral_0^infinity f(2x)e^(-b x) dx`

`=(1/2) integral_0^infinity f(u)e^(-b u/2) du`.

It is not `integral f(x)e^(-b x)dx` without an additional redefinition.

## Comparison with the checker

The checker’s prime branch samples `profile(log n)`. Its archimedean branch integrates `profile(x/2)e^(-b x)`, equivalently `2 integral profile(u)e^(-2bu)du`.

Neither branch follows from the declared arrow `g(x)=f(2x)`:

- the declared prime sample would be `profile(2 log n)` if `f=profile`;
- the declared Laplace term would use `profile(2x)`, not `profile(x/2)`.

Thus the internal convention map did not merely fail to reconcile two checker branches. Its scaling implication was reversed when translating the Fourier test into prime and gamma samples.

## Required repair

Start from one published explicit formula in variables `(h,g)` with an explicit Fourier inversion pair. Only afterward introduce a spline profile by a named dilation operator. Derive prime samples and Laplace kernels functorially from that dilation; do not infer them from desired support or cutoff.

## Disposition

No current coordinate repair is source-authoritative. The earlier suggestion that the `1024` cutoff identifies the intended convention is implementation provenance only, not theorem authority. The spline branch is blocked until the transform map is rederived.
