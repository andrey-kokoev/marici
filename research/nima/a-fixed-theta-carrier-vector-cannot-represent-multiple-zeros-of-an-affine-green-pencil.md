# A fixed theta carrier vector cannot represent multiple zeros of an affine Green pencil

## Fixed-incidence proposal

Let the Green pencil be affine in the spectral parameter:

\[
C(s)=C_0-sI
\]

on a fixed domain.  Suppose a source frame of the theta carrier line is sent
to one fixed nonzero vector

\[
\psi\in H
\]

independent of \(s\).

A divisor-to-state square would require

\[
C(s_0)\psi=0
\]

at every Xi zero \(s_0\).

## Two-point obstruction

If \(s_1\ne s_2\) are two represented zeros, then

\[
(C_0-s_1I)\psi=0,
\]

\[
(C_0-s_2I)\psi=0.
\]

Subtracting gives

\[
(s_2-s_1)\psi=0.
\]

Hence \(\psi=0\), contradicting injectivity of the defect incidence.

Therefore a fixed carrier vector cannot represent more than one spectral
point of an affine pencil.

## Required parameter dependence

The defect incidence must be a holomorphic family

\[
i(s):\mathcal L_{\theta,s}\to H
\]

whose image line moves with \(s\).  At a zero \(s_0\), the image must coincide
with the corresponding eigenspace or generalized root line of \(C(s_0)\).

The natural resolvent history

\[
u_s=(A-z(s))^{-1}\Phi
\]

has the required parameter dependence, but it fails the paired adjoint source
equation unless the unresolved arithmetic compatibility holds.

## Nonlinear-pencil alternative

A fixed vector can occur at several parameters only if the pencil depends on
\(s\) through a scalar factor that vanishes at those points, for example

\[
C(s)\psi=f(s)w.
\]

Taking \(f=\xi\) by definition installs the desired divisor.  A valid
nonlinear pencil must derive that factor from source operations before scalar
Xi identification.

Thus nonlinear parameter dependence does not remove the provenance gate.

## Multiplicity constraint

At a zero of order \(m\), a holomorphic root-vector chain must satisfy the
Keldysh equations obtained by differentiating

\[
C(s)i(s)=w(s)\tau_s.
\]

Pointwise selection of one kernel vector does not determine those derivatives
and cannot preserve algebraic multiplicity.

## G4 consequence

The source defect projection cannot be a constant embedding of the theta line
into one fixed history direction.  It must carry nontrivial holomorphic
parameter transport and generalized-root data.  This rules out using a fixed
Gaussian, fixed tensor-unit vector, or fixed endpoint generator as the entire
Xi defect state.

No RH conclusion is authorized.
