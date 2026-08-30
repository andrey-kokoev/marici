# A quadratic history graph gives a sharp strict loading margin, conditionally

## Scope

The first-order history metric (I+mathsf D^*mathsf D) repairs the infrared defect but has zero strict contraction margin. This note identifies the minimal functional-calculus strengthening that would close both ends. It is a conditional analytic target, not yet a source-authority theorem.

Let

[
T=mathsf D^*mathsf Dge0.
]

## Quadratic graph metric

Consider

[
G_2=I+T+T^2.
]

The normalized first-order incidence is

[
K_2=mathsf D G_2^{-1/2}.
]

Functional calculus gives

[
K_2^*K_2
=
T(I+T+T^2)^{-1}.
]

For

[
r(lambda)=rac{lambda}{1+lambda+lambda^2},
qquad lambdage0,
]

one has

[
r'(lambda)
=
rac{1-lambda^2}{(1+lambda+lambda^2)^2}.
]

The unique maximum occurs at (lambda=1), where

[
r(1)=rac13.
]

Therefore

[
|K_2|=rac1{sqrt3},
]

provided the spectrum reaches or approximates (lambda=1); in all cases,

[
|K_2|lerac1{sqrt3}.
]

The resulting normalized strict margin is at least

[
delta_2=1-rac1{sqrt3}.
]

## Both endpoint failures are removed

At low frequency,

[
r(lambda)simlambda,
]

so the identity term prevents infrared inversion failure.

At high frequency,

[
r(lambda)simlambda^{-1},
]

so the quadratic term prevents ultraviolet saturation.

The first-order incidence is now compact relative to spectral escape at both ends, although this pointwise decay alone does not imply that the operator is compact when the underlying spectral measure is continuous.

## General coefficient

For

[
G_c=I+T+cT^2,
qquad c>0,
]

the maximum occurs at

[
lambda=c^{-1/2}
]

and equals

[
sup_{lambdage0}
rac{lambda}{1+lambda+clambda^2}
=
rac1{1+2sqrt c}.
]

Hence

[
|mathsf D G_c^{-1/2}|
le
rac1{sqrt{1+2sqrt c}}<1.
]

Any positive source-authorized quadratic coefficient therefore gives a strict margin. If (cdownarrow0) through the cutoff family, the completion margin again collapses.

## Authority gate

The theta completion already contains a second-order dilation polynomial,

[
A(A+1).
]

That fact does not automatically authorize (T^2=(mathsf D^*mathsf D)^2), because dilation energy and translation-derivative energy are different operators. The required source theorem must compare the actual completion/history form (G_{mathrm{src}}) to the quadratic graph:

[
G_{mathrm{src}}
ge
c_0(I+T+cT^2)
]

on the incidence range, with (c_0,c>0) uniform in the relevant prime, cutoff, and compact off-seam parameters.

A weaker relative estimate sufficient for loading is

[
mathsf D^*mathsf D
le
q^2G_{mathrm{src}},
qquad q<1.
]

But (q<1) must be derived from the source form rather than inferred from formal differential order.

## Result

The smallest scalar functional-calculus model that repairs both defects is

[
I+T+cT^2.
]

It yields the explicit strict bound

[
|mathsf D(I+T+cT^2)^{-1/2}|
le
(1+2sqrt c)^{-1/2}.
]

The next source calculation is now quantitative: determine whether the completed theta history dominates a positive quadratic function of the actual derivative incidence on its typed range. Until that comparison exists, the strict margin remains conditional.
