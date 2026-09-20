# Higher-coherence topology iteration 41: analytic Köthe sheaves make the codiagonal faithful on open germs, but not after specialization to the Xi divisor

## Candidate topology

Over a spectral domain `U`, let

\[
\mathscr K(U)
=
\left\{(f_{p,k}) : f_{p,k}\in\mathcal O(U),\
\sup_{z\in K}q_\delta(f(z))<\infty
\text{ for all }K\Subset U,\delta>0\right\}.
\]

This is a sheaf of locally convex Köthe modules. It simultaneously retains
prime labels, holomorphic continuation, and exponential source control.

## Open-germ injectivity

For a labelled Dirichlet/Laplace synthesis

\[
C(f)(z)=\sum_{p,k}f_{p,k}(z)e^{-zL_{p,k}},
\]

normal convergence permits differentiation and restriction. If the
coefficients are spectrally fixed (or belong to a source class with a proved
uniqueness theorem), vanishing of `C(f)` on an open set can force every
coefficient to vanish.

Thus analytic continuation can make a codiagonal faithful on whole germs even
when one point evaluation is not faithful.

## Specialization is the problem

The bordered identity is

\[
C(R)(z)=\Delta_{\rm border}(z)=\tau(z)H(z),
\]

not `C(R)=0` on an open set. At a zero `z_0` of `tau`, it yields only

\[
C(R)(z_0)=0.
\]

Uniqueness of analytic Dirichlet series cannot recover all coordinates from
one scalar equation at one point.

Sheaf-theoretically, one specializes by tensoring with

\[
\mathcal O_{U,z_0}/(\tau).
\]

An injective map of analytic modules need not remain injective after this
quotient unless the inclusion is pure/flat relative to the divisor. Its kernel
after specialization is measured by a torsion or `Tor_1` term.

## Finite hostile

Even with two labels, choose analytic germs `u_1,u_2` so that

\[
u_1(z)e^{-zL_1}+u_2(z)e^{-zL_2}=\tau(z)H(z).
\]

At `z_0`, the two nonzero specialized coordinates can cancel. All germs are
holomorphic and finite support satisfies every Köthe bound. Hence neither
nuclearity nor analytic continuation alone removes divisor-fiber cancellation.

## Possible unlock: purity

A useful theorem would show that the source-generated labelled range is a
pure submodule of the common-history sheaf and that the bordered quotient has
no `tau`-torsion. Then codiagonal injectivity would survive base change to the
Xi divisor.

Concretely one needs

\[
C(R)\in\tau\,\operatorname{im}C
\quad\Longrightarrow\quad
R\in\tau\,\mathscr K.
\]

Coordinatewise divisibility would give `R(z_0)=0`, and positivity would force
confinement. This purity statement is stronger than ordinary injectivity and
is not currently proved.

## Higher-coherence interpretation

The infinite cone tower may be viewed as a locally free resolution of the
cokernel of `C`. If that resolution proves flatness along the Xi divisor, the
higher coherences would eliminate the specialization kernel noncircularly.
This identifies a precise role for additional systems: resolve divisor torsion,
not merely append nullhomotopies.

## Verdict for topology 41

Analytic Köthe sheaves strengthen scalar codiagonal faithfulness from pointwise
to germwise data. They still do not permit passage from a Xi-divisible scalar
defect to coordinatewise vanishing at a Xi zero. The missing property is
purity/flatness of the labelled incidence along the Xi divisor.

The next nonredundant topology to test is a derived-completed sheaf topology
using the Koszul complex of `tau`, where the relevant `Tor_1` specialization
obstruction can be computed explicitly.