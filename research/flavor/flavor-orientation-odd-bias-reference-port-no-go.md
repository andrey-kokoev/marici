# The lattice discriminator does not supply its own orientation selector: WP785

## Question

Can the norm sign that distinguishes the WP784 flux doublet be promoted to a
source-derived selector without adding a reference orientation?

## The discriminator already exists

In lightcone variables the two minimizing fluxes are

\[
(u,v)=(1,3),\qquad (u,v)=(-1,3).
\]

They have the same pairing \(b\mathbin{\cdot}f=3\), while

\[
q(f)=f^2=uv
\]

takes the values \(+3\) and \(-3\). Thus failure of selection is not failure
of algebraic separation.

The map

\[
R(u,v)=(-u,v)
\]

exchanges the two states. In the integral basis it is
\(R(x,y)=(-y,-x)\), and

\[
R^TJR=-J.
\]

It is therefore an orientation-reversing comparison, not an isometry inside
one fixed oriented lattice frame.

## A topological phase does not select the energy branch

The reference-free topological candidate changes the Euclidean weight to

\[
w(f)=\exp\!\left[-V(f)+i\theta q(f)\right].
\]

For \(q=\pm3\), the two weights have different phases but identical moduli.
Consequently this term supplies an interference readout only if an admitted
coherent comparison exists; it does not lift the WP784 energy degeneracy.

## The smallest real bias exposes the missing reference

A real candidate selector is

\[
V_{t,\mu}(u,v)
=\frac12\left(e^tu^2+e^{-t}v^2\right)+\mu uv.
\]

At \(t=\log3\), it splits the doublet by

\[
V_{+}-V_{-}=6\mu.
\]

The quadratic form is positive exactly when \(|\mu|<1\), since its Gram
determinant is \(1-\mu^2\). Thus the term is mathematically consistent and
can be tuned to choose either branch.

But with a fixed scalar \(\mu\), orientation reversal changes the term.
Descent is restored only under the combined transformation

\[
(u,\mu)\longmapsto(-u,-\mu).
\]

Hence \(\mu\) must be a pseudoscalar reference. Adding it changes the physical
groupoid to the stabilizer of a chosen reference orientation. This defines a
new relational experiment; it does not recover an absolute sign from the
original flux system.

## Dynamical symmetry breaking still does not predict an absolute sign

If the reference is dynamical with a symmetric potential such as

\[
U(\mu)=\lambda(\mu^2-\mu_0^2)^2,
\]

the combined configurations \((f_+,-\mu_0)\) and
\((f_-,+\mu_0)\) remain exactly degenerate. The interaction correlates the
flux with the reference vacuum but does not say which absolute orientation is
realized. A boundary condition, asymmetric source state, or cosmological
history must do that work.

## Green--Schwarz and instrument gates

A constant \(\mu\) is blind to the WP781 product-preserving tangent
\((\delta k,\delta c)=(k,-c)\). Making the bias transverse requires an
independently derived function \(\mu(k,c)\); anomaly cancellation fixes only
\(kc\) and supplies no such law.

No admitted instrument currently compares the two topological phases or
calibrates the pseudoscalar reference in detector units. The candidate
therefore neither fixes the Stückelberg threshold nor reaches the
physical16 readout.

## Classification

The norm is a physical discriminator but not a source selector. The
topological term is a phase probe without energetic selection. A real bias is
an effective selector only after a new pseudoscalar reference port is added,
and a symmetric dynamical port leaves a paired-vacuum ambiguity.

The next source principle must derive a symmetry-breaking reference state,
its sign and magnitude, its nonzero response along the Green--Schwarz kernel,
and its RG- and threshold-stable detector coupling in one common frame.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp785_orientation_odd_bias_reference_port_no_go.py

Generated result:
research/flavor/results/wp785_orientation_odd_bias_reference_port_no_go.json
