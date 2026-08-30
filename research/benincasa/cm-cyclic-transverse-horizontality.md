# Quotient horizontality of the cyclic transverse-curvature port

## Correction from Entry 2602

The calculation below proves pointwise closure after adjoining the three
first-normal classes. It does not prove that their span is preserved by the
connection. The reconstructed scalar has nonzero curvature, so the quotient
connection and the phrase “quotient horizontality” are retracted. See
`cm-cyclic-pointwise-closure-curvature.md`.

## Connection convention

For a rational coefficient \(A\) multiplying the physical twist
\(K^{-1/2}\),

\[
\nabla_D(AK^{-1/2})
=
\left(
D A-\frac12A\frac{D K}{K}
\right)K^{-1/2}.
\]

Apply this to the cyclic transverse curvature of Entry 2591 in the three
base directions

\[
\partial_{P_1^2},\qquad
\partial_{P_2^2},\qquad
\partial_{P_3^2}.
\]

## Exact result

At A, B, HOMA, and SOFT1, with an independent-prime replication at A,

\[
\boxed{
\operatorname{rank}
\langle
\nu_1,\nu_2,\nu_3,
\mathsf A_{\rm cyc}^{(2)},
\nabla_1\mathsf A_{\rm cyc}^{(2)},
\nabla_2\mathsf A_{\rm cyc}^{(2)},
\nabla_3\mathsf A_{\rm cyc}^{(2)}
\rangle
=4.
}
\]

Therefore

\[
\nabla\mathsf A_{\rm cyc}^{(2)}
\subset
\langle\nu_1,\nu_2,\nu_3,\mathsf A_{\rm cyc}^{(2)}\rangle.
\]

After quotienting by the three first-normal classes, the cyclic quadratic
line is horizontal.

## Typing boundary

The result is quotient horizontality. A chosen lift of the line inside the
full seven-dimensional CM cohomology can mix with first-normal classes. No
canonical affine splitting, marked-relative subconnection, or physical
activation follows.

## Next falsifier

Compute the induced rank-one connection scalar symbolically and factor its
intrinsic pole divisor. Test support only modulo changes of quotient
generator. In particular, a denominator in one finite-field frame is not
intrinsic support.
