# Spectral infinity forbids a cross-minor to full-Weyl unit

## Bounded question

Can the theta cross transfer equal the determinant of the unbordered two-port
Weyl matrix up to a nowhere-zero rational unit?

## Pure resolvent Weyl matrix

At a finite source-authorized compression, let

\[
A=A^*,
\qquad
B=\begin{pmatrix}b_f&b_0\end{pmatrix},
\]

and use the pure resolvent Weyl contribution

\[
W(z)=-B^*(A-zI)^{-1}B.
\]

At spectral infinity,

\[
(A-zI)^{-1}
=
-\frac1zI-\frac1{z^2}A+O(z^{-3}),
\]

so

\[
W(z)
=
\frac1zG_0+\frac1{z^2}G_1+O(z^{-3}),
\qquad
G_0=B^*B.
\]

## Cross and determinant orders

The theta cross entry satisfies

\[
W_{f0}(z)
=
\frac{\langle b_f,b_0\rangle}{z}
+O(z^{-2}).
\]

If the ports are linearly independent, their Gram determinant is positive:

\[
\det G_0>0.
\]

Consequently,

\[
\det W(z)
=
\frac{\det G_0}{z^2}
+O(z^{-3}).
\]

When the source-endpoint incidence is nonzero,

\[
\langle b_f,b_0\rangle\ne0,
\]

the quotient has the asymptotic form

\[
\frac{W_{f0}(z)}{\det W(z)}
=
z\frac{\langle b_f,b_0\rangle}{\det G_0}
+O(1).
\]

Thus the cross minor and full determinant have different orders at spectral
infinity.

## Unit obstruction

Both finite-cutoff quantities are rational functions of \(z\). If

\[
W_{f0}(z)=u(z)\det W(z)
\]

with a nowhere-zero rational unit on the finite spectral plane, then \(u\)
must have the linear growth displayed above. A rational function without
finite zeros or poles is constant. A nonconstant polynomial has a complex
zero. Therefore no such unit exists.

This is a divisor-independent obstruction: it uses only port independence,
nonzero incidence, and resolvent asymptotics.

## Degenerate port alternative

If the two ports are linearly dependent, then \(B\) has rank one and

\[
\det W(z)\equiv0.
\]

That does not recover a nonzero cross transfer. It collapses the full exterior
coordinate entirely.

If the ports are independent but orthogonal, the leading cross coefficient
vanishes and a separate higher-moment audit is required. The native theta
endpoint-source incidence is nonzero, so this exceptional branch is not the
current source type.

## The minimal additional reference

One scalar reference coordinate does make the cross minor determinantal:

\[
L(z)=
\begin{pmatrix}
0&b_f^*\\
b_0&A-zI
\end{pmatrix},
\qquad
\det L(z)=-\det(A-zI)W_{f0}(z).
\]

This border is minimal and exact. It also exposes why the operation cannot be
performed inside the original full \(2\times2\) determinant: it adds a
reference incidence rather than asserting an identity among existing minors.

The price remains that different source and endpoint ports make \(L\)
non-self-adjoint. The reference solves faithfulness of the scalar readout, not
self-adjoint spectral typing.

## Result

For independent theta ports with nonzero incidence, spectral-infinity degree
forbids any nowhere-zero rational unit relating the cross transfer to the full
two-port Weyl determinant. The only canonical minimal determinant promotion is
the one-coordinate border already derived, and it is non-self-adjoint.

Therefore the Cayley-positive full determinant cannot be transferred to the
theta cross divisor by a normalization unit. A successful route needs a
genuinely larger source correspondence whose positivity acts on the bordered
section itself.

## Sharp falsifier

At each finite cutoff verify:

\[
\det(B_X^*B_X)>0,
\qquad
\langle b_{f,X},b_{0,X}\rangle\ne0.
\]

These two coefficients already force the \(z^{-1}\) versus \(z^{-2}\)
mismatch. Any proposed unit relation must either violate these source
coefficients, introduce a finite zero or pole, or use the bordered determinant
rather than the full Weyl determinant.
