# The theta transvectant is bilinear, not Hilbert-positive

## Bounded question

Why does positivity of the source separation operator fail to make the
generalized Laguerre hierarchy automatically positive, and why has a
self-adjoint RH operator not emerged from the source construction?

## Two-copy operators

Let

\[
 \mathcal H=L^2(\mathbb R,du),
 \qquad \Omega(u)=\sqrt{\Phi(u)},
\]

and let `Q` be multiplication by `u`.  On `H tensor H`, define the commuting
self-adjoint operators

\[
 \Delta=Q\otimes I-I\otimes Q,
 \qquad
 \Sigma=Q\otimes I+I\otimes Q.
\]

Packet 121 gives the exact matrix coefficient

\[
 \boxed{
 (2n)!\mathcal L_n[X](x)
 =\langle\Omega^{\otimes2},
 \Delta^{2n}e^{ix\Sigma}\Omega^{\otimes2}\rangle.}
\]

Here `Delta^(2n)` is positive and commutes with the unitary
`exp(ix Sigma)`.  Their product is generally not positive.  Source positivity
therefore proves the nonoscillatory value at `x=0`, but not its orientation on
the real spectral axis.

## Bilinear versus sesquilinear pairing

Equivalently, let

\[
 \Psi_x=e^{ix\Sigma/2}\Omega^{\otimes2}.
\]

With the complex **bilinear** pairing

\[
 [f,g]_0=\int f(u,v)g(u,v)\,du\,dv,
\]

one has

\[
 (2n)!\mathcal L_n[X](x)
 =[\Psi_x,\Delta^{2n}\Psi_x]_0.
\]

But replacing this with the Hilbert sesquilinear pairing conjugates the first
phase and removes `x`:

\[
 \langle\Psi_x,\Delta^{2n}\Psi_x\rangle
 =\langle\Omega^{\otimes2},\Delta^{2n}\Omega^{\otimes2}\rangle>0.
\]

Thus the desired scalar is precisely the non-Hilbert polarization.  Treating
it as an ordinary norm silently deletes the oscillatory information whose sign
is equivalent to the problem.

## Why self-adjointness is not automatic

The source supplies self-adjoint `Delta` and `Sigma`, but the RH-bearing
readout inserts a unitary character inside the positive moment.  No theorem of
self-adjoint spectral positivity controls

\[
 \langle\Omega,Pe^{ix\Sigma}\Omega\rangle
\]

from `P>=0` alone.

This answers the earlier load-bearing question:

\[
 \boxed{
 \text{the source-derived boundary operator need not be self-adjoint in the
 pairing that produces }X.}
\]

A Hilbert--Polya construction would require an additional source-derived
polarization turning the bilinear transvectant into a Hermitian positive form
without erasing `e^(ix Sigma)`.  That polarization is exactly what remains
unknown.

## Krein/real-structure formulation

Complex conjugation `C` converts the bilinear form into

\[
 [f,g]_0=\langle Cf,g\rangle.
\]

So the Laguerre hierarchy is positivity relative to an antiunitary real
structure, not ordinary Hilbert positivity.  Reciprocal reflection supplies
another involution, and their composition fixes the critical seam.  The
natural target is therefore a compatible real/Krein polarization in which the
transported symmetric-power forms acquire a definite sector.

## Falsifier and next gate

The next conjecture must specify such a polarization independently of zero
locations.  It must intertwine modular reflection, the integral winding
transport, and every even symmetric power.  A valid construction would give

\[
 [\Psi_x,\Delta^{2n}\Psi_x]_0
 =\|T_{n,x}\Psi_x\|^2
\]

or a positive Schur complement for all real `x`.

The falsifier is immediate: if the proposed polarization also works for a
hostile self-Fourier carrier with off-critical zeros, it supplies no RH force;
if it fails to be positive or bounded on the theta analytic core, the operator
construction is ill-typed.
