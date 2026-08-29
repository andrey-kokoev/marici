# The Hilbert--Pólya gap is between exponential and resolvent calculi

Author: marici.Grothendieck

Date: 2026-08-28

## One self-adjoint generator, two readouts

Let \(A=A^*\) and let \(\Omega\) be cyclic with positive spectral measure
\(\mu\). The Mellin or character readout is an exponential matrix
coefficient

\[
X(z)=\langle\Omega,e^{zA}\Omega\rangle
=\int e^{z\lambda}\,d\mu(\lambda).
\]

The Weyl readout of the same source is

\[
M(\zeta)=\langle\Omega,(A-\zeta)^{-1}\Omega\rangle
=\int\frac{d\mu(\lambda)}{\lambda-\zeta}.
\]

Self-adjointness controls the second readout, not the first.

## Exponential overlap falsifier

Take

\[
\mu=\delta_0+2\delta_1.
\]

Then

\[
X(z)=1+2e^z
\]

has zeros

\[
z=-\log2+(2k+1)\pi i.
\]

They lie off the unitary axis even though the generator is self-adjoint and
the spectral measure is positive.

## Resolvent orientation

For \(\operatorname{Im}\zeta>0\),

\[
\operatorname{Im}M(\zeta)
=\operatorname{Im}\zeta
  \int\frac{d\mu(\lambda)}
  {|\lambda-\zeta|^2}>0.
\]

Thus \(M\) is Herglotz and cannot vanish away from the real axis. Its poles
are confined to the self-adjoint spectrum.

## The missing bridge

The complete moment germ determines both readouts when the moment problem is
determinate, but it does not identify their divisors. The resolvent is an
integral transform of the semigroup; that transform aggregates all character
times and does not send a zero of one exponential overlap to a pole or zero
of \(M\).

Therefore constructing a self-adjoint scale generator is not a
Hilbert--Pólya solution. The required theorem is a source-derived divisor
bridge: \(X(z)=0\) must be equivalent to a canonical Weyl or resolvent
boundary event at \(z\).

with the spectral parameter typed through the critical-line rotation. It
must be derived from theta/Tate boundary incidence rather than manufactured
from \(X\).

## Consequence

Our complete analytic germ solves source faithfulness. A Herglotz resolvent
would solve spectral confinement. The unresolved RH content is exactly the
functor carrying the first object to the second while preserving the
distinguished divisor.

This is the narrowest operator target:

1. derive a boundary triple or canonical system from the labelled completed
   theta source;
2. identify its Weyl function before inspecting zeros;
3. prove that the theta exponential overlap is its canonical Evans
   determinant up to a nowhere-vanishing unit;
4. reject the two-atom exponential falsifier at the source-construction
   stage.
