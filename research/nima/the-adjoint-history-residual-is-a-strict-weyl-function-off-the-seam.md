# The adjoint-history residual is a strict Weyl function off the seam

## Skew history generator

Let \(A\) be the closed skew-adjoint translation generator on the retained
bilateral half-density history space.  For

\[
z=a+it,
\qquad a\ne0,
\]

the resolvent exists and the natural forced history is

\[
u_z=(A-z)^{-1}\Phi.
\]

Define the scalar adjoint residual

\[
m(z)=\langle\Phi,u_z\rangle
=
\left\langle
\Phi,(A-z)^{-1}\Phi
\right\rangle.
\]

This is the Weyl/resolvent matrix coefficient selected by the forcing vector.

## Exact real-part identity

The resolvent equation is

\[
(A-z)u_z=\Phi.
\]

Pairing with \(u_z\) and using skew-adjointness gives

\[
\operatorname{Re}
\langle u_z,Au_z\rangle=0.
\]

Therefore, with the declared inner-product convention,

\[
\operatorname{Re}m(z)
=-a\|u_z\|^2
\]

up to the fixed conjugation convention for which argument is linear.  The
sign reverses if the resolvent is written as \((z-A)^{-1}\); strictness does
not change.

Since \(\Phi\ne0\), the resolvent is injective on \(\Phi\), so \(u_z\ne0\).
Hence

\[
a\operatorname{Re}m(z)<0.
\]

In particular,

\[
m(z)\ne0
\qquad(a\ne0).
\]

## Spectral representation

If \(iA\) has spectral measure \(d\mu_\Phi(\lambda)\) in the forcing state,
then

\[
m(z)
=
\int_{\mathbb R}
\frac{d\mu_\Phi(\lambda)}{i\lambda-z}.
\]

Its real part is

\[
\operatorname{Re}m(a+it)
=
-a
\int_{\mathbb R}
\frac{d\mu_\Phi(\lambda)}
{a^2+(t-\lambda)^2}.
\]

The integral is strictly positive before multiplication by \(-a\).  Thus the
nonvanishing is a source spectral theorem, not a numerical observation.

## Consequence for paired completion

The lower equation of the minimal paired pencil is

\[
V^*u_z=m(z)=0.
\]

The strict Weyl identity shows that no natural forced resolvent history can
satisfy this equation off the seam.  The paired pencil is therefore
automatically off-seam kernel-free, independently of the Xi section.

This is the desired Green orientation for the paired operator, but it also
shows why Xi divisor compatibility is difficult: an off-seam Xi zero, if one
existed, could not map to this natural paired kernel.

## No determinant inference

The strict sign of \(m(z)\) does not prove that Xi has no off-seam zero.  It
proves only that the natural resolvent realization has no off-seam state
satisfying its adjoint source equation.

To infer RH, one still needs the source divisibility map

\[
K_\tau\longrightarrow C_{\rm FP}
\]

showing that every Xi residue is represented by that paired kernel.  The Weyl
sign cannot supply this map; assuming it would identify two independently
constructed divisors.

## Completion scope

The argument requires:

- the bilateral translation generator to be skew-adjoint on the retained
  history domain;
- \(\Phi\) to lie in the Hilbert forcing space;
- the resolvent history to use the same half-density metric as \(V^*\);
- endpoint restrictions not to change the bulk resolvent before sewing.

These conditions hold for the analytic history leg.  Arithmetic, seam, and
endpoint augmentation still require the separate divisor comparison.

## Disposition

The adjoint-history residual is now identified as a strict Weyl function and
is proved nonzero off the seam.  This closes off-seam invertibility for the
natural paired history block.  It does not identify its characteristic with
Xi, so G4 and RH remain open.
