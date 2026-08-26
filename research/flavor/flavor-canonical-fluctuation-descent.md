# Canonical fluctuation descent (WP359)

## Bounded question

Can WP358's jump-plus-curvature probe be stated invariantly when the effective
field has an unfixed kinetic coefficient, and what source quotient does the
physical instrument actually identify?

Take

\[
\mathcal L=\frac Z2(\partial t)^2-V(t),
\qquad Z>0,
\]

with the WP357 sextic potential. Under the field-coordinate change
\(t'=a t\), \(a>0\), the packet transforms as

\[
(Z,r,u,w,q,\kappa)\mapsto
\left(\frac Z{a^2},\frac r{a^2},\frac u{a^4},
\frac w{a^6},a^2q,\frac\kappa{a^2}\right).
\]

The raw jump and Hessian do not descend separately. The canonically normalized
readouts do:

\[
Q=Zq,
\qquad
M^2=\frac{\kappa}{Z}.
\]

Here \(Q\) is the squared canonical vacuum displacement and \(M^2\) is the
tree-level pole-curvature scale.

## Faithful source quotient

The invariant coefficient coordinates are

\[
R=\frac rZ,
\qquad
U=\frac u{Z^2},
\qquad
W=\frac w{Z^3}.
\]

On coexistence they are reconstructed by

\[
U=-\frac{M^2}{Q},
\qquad
W=\frac{3M^2}{4Q^2},
\qquad
R=\frac{M^2}{4}.
\]

Thus \((Q,M^2)\) is faithful on the field-rescaling quotient of the classical
coexistence family. It is not faithful on literal coefficient packets, nor
should it be: packets related by a field-coordinate change are the same
effective source presentation.

## Hostile representatives and boundary

The representatives

\[
(Z,r,u,w)=(1,1,-4,3)
\]

and

\[
(Z,r,u,w)=\left(\frac14,\frac14,-\frac14,\frac3{64}\right)
\]

are related by \(a=2\). Their raw \((q,\kappa)\) values are respectively
\((1,4)\) and \((4,1)\), while both give \((Q,M^2)=(1,4)\).

This is an effective-field reparameterization result, not proof of descent
under the full flavor weak-basis groupoid. Nor does reconstruction imply
selection: all positive \((Q,M^2)\) remain admissible. A physical instrument
must measure a renormalized pole and a canonically normalized coupling or
vacuum response in a declared scheme; a coordinate Hessian alone is illegal.

Run `uv run --with sympy python
research/flavor/checkers/wp359_canonical_fluctuation_descent.py` to regenerate
the exact result.
