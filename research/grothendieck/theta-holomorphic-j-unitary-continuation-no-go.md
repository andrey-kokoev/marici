# Nonconstant holomorphic \(J\)-unitary continuation is impossible

## 1. Proposed continuation

The unitary defect determinant theorem suggests extending real character
transport to a holomorphic family \(F(z)\) preserving a fixed nondegenerate
Hermitian form \(J\):

\[
  F(z)^*JF(z)=J.
\]

If this held on an open complex domain, one might hope to transport the
real-axis kernel interpretation off-axis.

That proposal is impossible for a nonconstant holomorphic family.

## 2. Exact no-go

Assume \(F(z)\) is holomorphic, bounded-operator-valued, invertible, and
satisfies

\[
  F(z)^*JF(z)=J
\]

on a connected open set. Differentiate with respect to \(z\) in the
Wirtinger sense. Since \(F(z)^*\) is antiholomorphic,

\[
  \partial_zF(z)^*=0.
\]

Therefore

\[
  F(z)^*JF'(z)=0.
\]

Invertibility of \(F(z)^*J\) gives

\[
  F'(z)=0.
\]

Hence:

\[
\boxed{
\text{every holomorphic fixed-}J\text{-unitary family on an open domain is
constant}.}
\]

The argument applies equally to finite matrices and suitably regular bounded
operator families.

## 3. Bilinear versus Hermitian sewing

Reciprocal analytic doubling can preserve a complex bilinear form:

\[
  \mathcal U_z
  =
  \begin{pmatrix}
    e^{izQ}&0\\
    0&e^{-izQ}
  \end{pmatrix},
\]

with

\[
  \mathcal U_z^{T}
  \begin{pmatrix}0&I\\I&0\end{pmatrix}
  \mathcal U_z
  =
  \begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]

This identity is holomorphic because it uses transpose, not adjoint. It
supplies reciprocal symmetry and divisor pairing, but no positive norm.

Hermitian unitarity uses conjugation and can hold nontrivially only on a real
boundary locus. This is exactly why the critical axis supports the positive
defect determinant while the complex continuation does not.

## 4. Correct replacement

The viable analytic object is a half-plane transfer function that is
contractive in the interior and unitary on the boundary:

\[
  F(z)^*JF(z)\le J
  \qquad(\operatorname{Im}z>0),
\]

with boundary values satisfying equality almost everywhere. Depending on
the metric, this is a Schur, \(J\)-Schur, or characteristic-function
condition.

Such a function can be nonconstant and holomorphic. Its defect kernel

\[
  \mathcal K_F(z,w)
  =
  \frac{J-F(w)^*JF(z)}
       {-i(z-\bar w)}
\]

is positive precisely when the contractive law holds with the stated
orientation.

This returns the programme to a sharply typed de Branges/Pick target, but now
with a derivation requirement: \(F\) must be the full labelled modular
crossing, not a scalar function manufactured from \(X\).

## 5. RH-bearing formulation

The strongest surviving conjecture is:

> Completed adelic sewing produces a source-derived operator-valued
> \(J\)-Schur transfer function whose unitary boundary defect determinant is
> \(|X(x)/X(0)|^2\), and whose vacuum transition section is \(X(z)\) up to a
> nowhere-zero unit.

Interior contractivity would then supply an actual orientation law absent
from a generic positive source. But proving this property after defining
\(F\) from \(X\) would merely restate the Pick/de Branges criterion.

## 6. Hostile test

A hostile Fourier-stable source shares:

1. real-axis unitary character transport;
2. the universal vacuum defect determinant;
3. reciprocal bilinear doubling; and
4. positive Laplace Fisher geometry.

It must fail the operator-valued half-plane contractivity or the labelled
modular realization before its zeros are inspected. Otherwise the proposed
transfer function contains no RH-specific force.

## 7. Scope

The holomorphic \(J\)-unitary no-go and the bilinear/Hermitian distinction are
exact. The \(J\)-Schur kernel is the correct replacement target. No
source-derived contractive transfer function, determinant comparison,
off-axis exclusion, or RH theorem is established.
