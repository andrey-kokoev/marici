# Laguerre coordinates expose two distinct skew-Jacobi completion channels

## Scope

This note continues the correction that the even and odd analytic completion sectors do not share one finite front matrix. It derives the source-metric operator in the normalized Laguerre coordinates. No claim about compactness, Fredholm determinants, zero identification, or RH is made here.

## Normalized sectors

Let (X=pi x^2). The source Gaussian grade metrics are diagonalized by

[
E_k^{(-1/2)}(X)=c_{k,-},e^{-X}L_k^{-1/2}(2X)
]

in the even sector and

[
E_k^{(1/2)}(x)=c_{k,+},x e^{-X}L_k^{1/2}(2X)
]

in the odd sector, with the constants chosen so each family is orthonormal in its own analytic source metric.

Write (A=xpartial_x=2Xpartial_X). In either sector define

[
B=A+rac12.
]

For the even sector take (alpha=-	frac12); for the odd sector take (alpha=	frac12), including the extra derivative contribution from the prefactor (x). The Laguerre recurrence gives the common-form action

[
B E_k^{(alpha)}
=
u_k^{(alpha)}E_{k+1}^{(alpha)}
-
u_{k-1}^{(alpha)}E_{k-1}^{(alpha)},
]

where

[
u_k^{(alpha)}
=
sqrt{(k+1)(k+alpha+1)},
qquad
u_{-1}^{(alpha)}=0.
]

Thus (B) is a skew-Jacobi operator on the finite-sequence core. The form is common, but its coefficients are not:

[
u_k^{mathrm{even}}
=
sqrt{(k+1)(k+	frac12)},
]

[
u_k^{mathrm{odd}}
=
sqrt{(k+1)(k+	frac32)}.
]

This is the analytic reason the parity sectors cannot share one numerical completion matrix.

## Completion operator

The direct analytic completion operator in both sectors is

[
P=A(A+1)=B^2-rac14.
]

Therefore

[
P E_k^{(alpha)}
=
u_k^{(alpha)}u_{k+1}^{(alpha)}E_{k+2}^{(alpha)}
-
left(
(u_k^{(alpha)})^2+
(u_{k-1}^{(alpha)})^2+
rac14
ight)E_k^{(alpha)}
+
u_{k-1}^{(alpha)}u_{k-2}^{(alpha)}E_{k-2}^{(alpha)}.
]

The completion is pentadiagonal only in the ambient indexing sense; it preserves index parity and is tridiagonal on each even-index or odd-index subchain.

The diagonal coefficient is

[
-left(
2k^2+2(alpha+1)k+alpha+rac54
ight).
]

Hence the even and odd diagonal sequences are respectively

[
-left(2k^2+k+rac34ight)
]

and

[
-left(2k^2+3k+rac74ight).
]

## Operator closure on the coefficient carrier

Because (u_k^{(alpha)}sim k),

[
sum_{kge0}rac1{u_k^{(alpha)}}=infty.
]

The Carleman criterion therefore gives essential self-adjointness of (iB) on the finite-sequence core. Equivalently, (B) has a canonical skew-adjoint closure. Consequently

[
P=B^2-rac14
]

has the canonical self-adjoint realization determined by that closure and satisfies the form inequality

[
Ple -rac14 I.
]

This is a closure statement internal to each normalized analytic sector. It does not imply compact resolvent or any determinant-class property.

## Derivative intertwiner remains typed

The odd channel is not obtained by assigning the shifted polynomial directly to the odd basis. The correct identity remains

[
A(A+1)D=D(A-1)A.
]

Thus ((A-1)A) acts on an even potential before differentiation, while (A(A+1)) acts directly on the resulting odd analytic state. In Laguerre coordinates this derivative map must intertwine the (alpha=-	frac12) and (alpha=	frac12) skew-Jacobi carriers; it does not identify their coefficient matrices.

## Result

The analytic Gaussian completion has two source-normalized Jacobi channels:

[
alpha=-rac12
quad	ext{and}quad
alpha=rac12.
]

They share the structural formula (P=(A+	frac12)^2-	frac14), but their recurrence weights differ. The next finite calculation is therefore the explicit Laguerre-coordinate matrix of the derivative intertwiner and its graph norm, not another attempt to impose a parity-common grade matrix.
