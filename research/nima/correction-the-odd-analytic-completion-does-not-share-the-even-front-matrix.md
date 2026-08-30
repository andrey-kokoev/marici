# Correction: the odd analytic completion does not share the even front matrix

## Error

The earlier coefficient audit incorrectly assigned
\[
(A-1)A
\]
directly to the odd analytic basis
\[
o_k=xX^ke^{-X}.
\]

That shifted polynomial acts on the even potential before differentiation in the intertwining identity
\[
A(A+1)D
=
D(A-1)A.
\]

The completion operator acting on the odd function \(D f\) itself remains
\[
A(A+1).
\]

Therefore the claimed common matrix \(J_3\) across even and odd analytic packets is withdrawn.

## Correct even packet

For
\[
e_k=X^ke^{-X},
\qquad
Ae_k=2k\,e_k-2e_{k+1},
\]
the direct even completion is
\[
P_{\mathrm{even}}=A(A+1).
\]

Hence
\[
P_{\mathrm{even}}e_k
=
2k(2k+1)e_k
-
(8k+6)e_{k+1}
+
4e_{k+2}.
\]

Its three-grade front matrix is
\[
J_{\mathrm{even},3}
=
\begin{pmatrix}
0&0&0\\
-6&6&0\\
4&-14&20
\end{pmatrix}.
\]

## Correct odd packet

For
\[
o_k=xX^ke^{-X},
\qquad
Ao_k=(2k+1)o_k-2o_{k+1},
\]
the direct analytic completion is still
\[
P_{\mathrm{odd}}=A(A+1).
\]

Therefore
\[
P_{\mathrm{odd}}o_k
=
(2k+1)(2k+2)o_k
-
(8k+10)o_{k+1}
+
4o_{k+2}.
\]

Its three-grade front matrix is
\[
J_{\mathrm{odd},3}
=
\begin{pmatrix}
2&0&0\\
-10&12&0\\
4&-18&30
\end{pmatrix}.
\]

The even and odd front matrices are different.

## Correct shifted-potential identity

If the odd incidence is written as
\[
g=Df
\]
with even potential \(f\), then
\[
P_{\mathrm{odd}}g
=
A(A+1)Df
=
D(A-1)Af.
\]

On the even potential grades,
\[
(A-1)Ae_k
=
2k(2k-1)e_k
-
(8k+2)e_{k+1}
+
4e_{k+2}.
\]

For the base Gaussian,
\[
(A-1)Ae_0
=
-2e_1+4e_2,
\]
and differentiating this reproduces
\[
A(A+1)o_0
=
2o_0-10o_1+4o_2.
\]

This is the correct commuting square.

## Consequence

There are three distinct matrices:

1. direct even completion \(A(A+1)\);
2. direct odd completion \(A(A+1)\) represented in the degree-shifted odd basis;
3. shifted potential completion \((A-1)A\) before applying \(D\).

They are intertwined by differentiation but are not equal coefficient matrices.

Thus a common grade transport cannot be asserted merely from parity shifting. The source Adams comparison must preserve the derivative intertwiner explicitly.

## Laguerre coordinates remain valid

The Gamma-Gram repair by generalized Laguerre bases is unaffected. It supplies the correct analytic metric for both parity sectors.

The next matrix calculation should conjugate the direct analytic operators into their respective Laguerre bases and verify the derivative comparison between them.

## Disposition

The common-\(J_3\) claim from event 10393 and the common abstract band operator built from it are superseded as analytic parity claims. Their even-sector formulas remain valid; their extension to the odd sector does not.

No downstream coercivity or completion conclusion may use the withdrawn common-matrix identification.
