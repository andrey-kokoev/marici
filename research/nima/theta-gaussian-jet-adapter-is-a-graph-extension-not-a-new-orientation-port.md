# Theta Gaussian jet adapter is a graph extension, not a new orientation port

## Status

Exact factorization no-go. On the source-generated scaled Gaussian comb module,
derivative samples are canonically determined by value samples. The resulting
even current, however, has a half-Mellin transform that is an affine function
of the already retained half-amplitude and seam value.

Adjoining this current therefore produces a graph extension of the existing
state, not a new independent port. Reciprocal sewing of the graph cannot remove
states from the scalar readout kernel unless an additional source relation is
derived.

## Canonical restricted jet adapter

For the scaled Gaussian

\[
f_u(x)=e^{-\pi e^{2u}x^2},
\]

integer samples satisfy

\[
f_u'(n)=-2\pi e^{2u}n f_u(n).
\]

Thus on the labelled Gaussian module the derivative adapter is diagonal and
source-derived:

\[
D_u(v_n)_n
=(-2\pi e^{2u}nv_n)_n.
\]

It is continuous in the natural rapidly decreasing sequence topology. This is
the legitimate restricted-source exception to the ambient Schwartz no-go.

## Current factorization

Let (A(u)\) denote the sampled Gaussian-comb amplitude and let (E(u)\) be the
even current obtained after the odd labelled current cancels under
(n\leftrightarrow-n\). Grothendieck's exact identity is

\[
E=\frac12A-A'.
\]

Let

\[
H(z)=\int_0^\infty A(u)e^{izu}\,du
\]

be the half-Mellin amplitude. Integration by parts gives

\[
\mathcal M_+E(z)
=\left(\frac12+iz\right)H(z)+A(0).
\]

The entire distributed current has collapsed to two old channels:

- the half-amplitude (H(z));
- the seam evaluation (A(0)).

No independent bulk coordinate remains.

## Graph-extension theorem

Write the old half-state as

\[
x=(H,A_0),
\qquad
A_0=A(0),
\]

and the current as

\[
J=\alpha(z)H+A_0,
\qquad
\alpha(z)=\frac12+iz.
\]

The enlarged state is

\[
\Gamma_z(x)=(H,A_0,J).
\]

Its image is the graph of the affine linear current map. Projection onto the
first two coordinates satisfies

\[
\pi\Gamma_z=I.
\]

Hence \(\Gamma_z\) is injective and its image is canonically isomorphic to the
old state space. Adjoining (J\) does not restrict the admissible state set; it
only records a derived coordinate.

Any scalar-zero state in the old representation has a unique lifted
scalar-zero state on this graph.

## Reciprocal double

Retain the two half-amplitudes

\[
H_+(z)=H(z),
\qquad
H_-(z)=H(-z),
\]

and the common seam value (A_0\). Their derived currents have the form

\[
J_+(z)=\left(\frac12+iz\right)H_+(z)+A_0,
\]

\[
J_-(z)=\left(\frac12-iz\right)H_-(z)+A_0.
\]

Reciprocal reflection exchanges the two graph coordinates coherently. The
scalar transform remains

\[
X(z)=H_+(z)+H_-(z).
\]

The condition (X(z)=0\) is compatible with nonzero (J_+\), (J_-\), and
(A_0\). Merely sewing the two derived currents therefore does not exclude the
readout kernel.

## Why an extra equality would need authority

One could impose a new relation between (J_+\) and (J_-\), such as equality,
opposition, or positivity of a combination. None follows from their affine
definitions alone.

If a proposed relation is derived only after substituting

\[
H_-=-H_+
\]

at a scalar zero, it is fitted to the divisor. A valid relation must arise from
the labelled reciprocal source before scalar aggregation and must survive the
completion domain audit.

## Rank statement

At fixed (z\), the current row lies in the span of the half-amplitude row and
the seam row. Therefore adjoining it does not increase observation rank. In a
finite matrix compiler, the rank increment is exactly zero.

This is the smallest falsifier for claims that the Gaussian derivative adapter
adds a new observable.

## Relation to hostile carriers

The Gaussian annihilation law rejects nonconstant Fourier-fixed Hermite
perturbations, so those hostiles do not belong to this restricted adapter
module. That establishes source selection.

But after the source is selected, the adapter still factors through the old
amplitude and seam channels. Excluding hostiles and adding an independent
orientation law are different achievements.

## Consequence

The derivative-comb branch has reached a clean boundary:

- on ambient Schwartz space, the derivative port is fully independent and
  unoriented;
- on the Gaussian module, it descends canonically but factors through old
  channels;
- reciprocal sewing of this graph extension adds no new constraint.

Any surviving RH-bearing boundary current must either retain information lost
before the identity (E=A/2-A'\), introduce a genuinely independent marked or
infinite-completion port, or derive a new reciprocal relation not contained in
the functional equation.
