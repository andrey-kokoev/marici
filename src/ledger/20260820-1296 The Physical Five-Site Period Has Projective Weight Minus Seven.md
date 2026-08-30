---
title: "The Physical Five-Site Period Has Projective Weight Minus Seven"
date: 2026-08-20
entry: 1296
status: active-narrow-result
author: marici.Benincasa
---

# 1296 — The Physical Five-Site Period Has Projective Weight Minus Seven

Sequence claim: `seqclaim-201e24c68d1f152998f91435`.

## Frozen period

Use Entry 1233's source-defined physical period, Entry 1257's asymmetric
momentum-conserving shape, and the homogenized scale (ho):

[
Pi(t,ho)
=
int_{Gamma_3(ho P)}
d^3ell,
Omega_{C_5}(X_i=t,y_i(ell;ho P)).
]

On the frozen Gram chart the external-Gram density is constant and nonzero.
The Cayley--Menger/Gram inequalities defining (Gamma_3) are homogeneous,
so

[
Gamma_3(lambdaho P)=lambda,Gamma_3(ho P).
]

## Exact scaling

Entry 1293 proves

[
degOmega_{C_5}=-10.
]

The physical loop current has scaling degree three:

[
d^3(lambdaell)=lambda^3d^3ell.
]

Changing variables (ell=lambdaell') therefore gives

[
oxed{
Pi(lambda t,lambdaho)
=
lambda^{-7}Pi(t,ho).
}
]

Equivalently,

[
oxed{
(tpartial_t+hopartial_ho+7)Pi=0
}
]

and

[
oxed{
Pi(t,ho)=ho^{-7}Pi(t/ho,1).
}
]

This is a source-level change-of-variables identity, not a fitted
Picard--Fuchs equation.

## Consequence

The restored scale does not add a second period modulus. It exposes the
projective weight and shows that Entry 1257's (ho=1) family retains the
entire nontrivial one-variable dependence.

The identity fixes one Euler operator in the cyclic differential module
(mathcal DcdotPi), but it does not determine the remaining scalar
annihilator in the ratio (z=t/ho), its order, or its singular points.

## Scope

The conclusion uses the ordinary source integral where the homogeneous
change of variables is valid. It does not authorize a claim about anomalous
regularized boundary terms on a different contour or about a finite master
basis absent from the primary source.

## Next falsifier

Work directly in

[
z=t/ho.
]

Derive a scalar differential relation for the source integrand modulo exact
three-forms, with order and polynomial degree bounded before reconstruction.
Any candidate must be certified by exact integrand reduction; numerical
period fitting remains discovery evidence only.
