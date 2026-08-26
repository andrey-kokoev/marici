# Theta zero is an antidiagonal seam state, not two Dirichlet tails

## Question

The source-tail programme treated a transform zero as a two-endpoint boundary
state.  Does a zero make each half-tail vanish at the seam, or only their
completed sum?

## Doubled half-tail representation

Let (f) be the real, rapidly decreasing completed theta kernel on the
positive half-line, and write the even bilateral transform as

\[
X(z)
=
\int_0^\infty
f(v)
\left(
e^{zv}+e^{-zv}
\right)
\,dv.
\]

Define the two raw tails

\[
R_+(q,z)
=
\int_q^\infty f(v)e^{zv}\,dv,
\qquad
R_-(q,z)
=
\int_q^\infty f(v)e^{-zv}\,dv,
\]

and their transported versions

\[
H_+(q,z)=e^{-zq}R_+(q,z),
\qquad
H_-(q,z)=e^{zq}R_-(q,z).
\]

They obey the source-derived first-order system

\[
H_+'=-zH_+-f,
\qquad
H_-'=zH_--f.
\]

Rapid theta decay gives

\[
H_+(\infty,z)=H_-(\infty,z)=0
\]

throughout every bounded spectral strip.

## Correct zero boundary condition

At the seam endpoint (q=0),

\[
X(z)=H_+(0,z)+H_-(0,z).
\]

Therefore

\[
X(z)=0
\]

is equivalent to the antidiagonal boundary condition

\[
H_-(0,z)=-H_+(0,z).
\]

It does not imply

\[
H_+(0,z)=H_-(0,z)=0.
\]

The two half-tail states may both be nonzero and cancel only after completed
seam aggregation.  This is the faithful two-sector zero-to-state bridge.

## Exact Green identity

Write

\[
\sigma=\Re z
\]

and define

\[
N=|H_+|^2+|H_-|^2,
\qquad
J=|H_+|^2-|H_-|^2.
\]

Differentiating with the tail equations gives

\[
J'
=
-2\sigma N
-2f\,\Re(H_+-H_-).
\]

Equivalently,

\[
2\sigma N
=
-J'
-2f\,\Re(H_+-H_-).
\]

For a zero-state, the antidiagonal seam condition implies

\[
J(0)=0.
\]

Decay gives (J(\infty)=0).  Hence integration produces the exact identity

\[
2\sigma
\int_0^\infty N\,dq
=
-2
\int_0^\infty
f\,\Re(H_+-H_-)
\,dq.
\]

The completed zero condition therefore kills the flux boundary term without
killing either sheet.

## The remaining obstruction is explicit

If the state is nonzero, then

\[
\int_0^\infty N\,dq>0.
\]

Thus zero confinement would follow from a source identity forcing

\[
\int_0^\infty
f\,\Re(H_+-H_-)
\,dq=0.
\]

More generally, it is enough to show that this forcing integral is an exact
modular boundary current whose endpoint contribution vanishes on the complete
adelic state.

This is the same obstruction previously denoted by the doubled forcing term,
but its boundary typing is now correct.  No separate Dirichlet condition may
be imposed on either half-tail.

## Geometric meaning

The two open sectors meet at an interface carrying the antidiagonal subspace

\[
\Lambda_-
=
\{(a,-a):a\in\mathbb C\}.
\]

The flux form (J) vanishes on this subspace because its two components have
equal norm.  A zero is therefore a nontrivial interface state with zero net
sector flux, not disappearance of the full relationship.

This realizes the operator intuition that scalar cancellation can coexist
with a nonzero full comparison state.

## Falsifiers

The conservation route fails if:

- the actual completed theta representation does not admit the stated
  doubled half-tail decomposition;
- the tails fail to decay after transport in the required strip;
- the modular source does not convert the forcing integral into a boundary
  current;
- or completion admits a nonzero state with zero (N)-norm.

## Result

A completed theta zero is an antidiagonal seam state.  This condition makes
the doubled Green flux vanish at both endpoints while retaining a strictly
positive bulk norm for every nonzero state.  The whole RH-bearing burden is
the single forcing integral in the exact identity above.
