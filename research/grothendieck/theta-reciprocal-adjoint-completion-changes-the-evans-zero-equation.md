# Theta reciprocal adjoint completion changes the Evans zero equation

## Bounded question

What is the finite labelled adjoint residual of the boundary-control Evans
system, and can reciprocal backreaction remove it without changing the scalar
zero condition?

## Forward incidence

At a finite source cutoff (X), let (f_X\in\mathcal H_X) be the completed
labelled source vector. The forward control map is

\[
B_{+,X}:\mathbb C\longrightarrow\mathcal H_X,
\qquad
B_{+,X}c=cf_X.
\]

Its Hilbert adjoint is

\[
B_{+,X}^*G=\langle f_X,G\rangle.
\]

The one-way system used in packet 230 has lower incidence (B_{-,X}=0).
Therefore its exact adjoint residual is

\[
R_{\mathrm{adj},X}
=B_{-,X}-B_{+,X}^*
=-B_{+,X}^*.
\]

In particular,

\[
\|R_{\mathrm{adj},X}\|=\|f_X\|.
\]

This is a bulk residual. Endpoint domains cannot remove it on compactly
supported test states.

## Source candidate for reciprocal backreaction

If Fourier--Tate sewing is unitary in the completed source metric and fixes the
real source vector, the native reciprocal candidate is exactly

\[
B_{-,X}=B_{+,X}^*.
\]

This would repair the off-diagonal symmetry defect before scalar aggregation.
But it adds a lower scalar equation to the system.

## Changed kernel equation

A symmetric block completion has the form

\[
\mathcal L_{z,X}
=
\begin{pmatrix}
A_{z,X}&B_{+,X}\\
B_{+,X}^*&C_{z,X}
\end{pmatrix}.
\]

For a tail solution (G=cG_{z,X}), the new lower equation becomes

\[
c\left(
\langle f_X,G_{z,X}\rangle+C_{z,X}
\right)=0.
\]

The packet-230 Evans condition was instead the endpoint equation

\[
G_{z,X}(0)=F_X(z)=0.
\]

These scalar equations are not identical. Choosing (C_{z,X}) after computing
the pairing would manufacture the desired determinant. A valid completion must
derive (C_{z,X}) independently from primitive, prime-square, seam, and
archimedean boundary data and then prove equality of the two zero conditions.

## Finite acceptance test

For every cutoff, compute

\[
S_X(z)
=C_{z,X}-B_{+,X}^*A_{z,X}^{-1}B_{+,X}.
\]

The reciprocal colligation is admissible only if:

1. (B_{-,X}=B_{+,X}^*) in the actual source metrics and domains;
2. (C_{z,X}) is derived before inspecting (F_X);
3. the Schur determinant agrees with (F_X(z)) up to an explicit nowhere-zero
   unit;
4. the agreement is compatible with cutoff inclusions and completion.

The first nonzero adjoint residual or first mismatch of zero divisors rejects
the proposed completion.

## Meaning

The one-way system solved the zero-to-state problem by using an endpoint
condition. Reciprocal symmetry solves the Green-form problem by adding the
adjoint return channel. These are complementary capabilities, but their naive
combination changes the spectral equation.

The remaining constructor is therefore not merely an adjoint block. It is a
source-derived reciprocal colligation whose Schur complement reproduces the
endpoint Evans determinant.

## Scope

This packet computes the finite labelled adjoint residual and proves that the
obvious symmetric completion changes the zero equation. It does not construct
the required scalar block, prove Schur--Evans agreement, or prove RH.
