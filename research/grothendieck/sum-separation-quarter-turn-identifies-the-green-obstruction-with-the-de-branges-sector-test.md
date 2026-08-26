# Sum--separation quarter-turn identifies the Green obstruction with the de Branges sector test

## Question

The doubled Green identity uses ordered source separation, while the original
theta attack used a two-variable quadrant kernel.  Are these independent RH
routes, or two coordinate projections of one pair-source geometry?

## One-sided spectral factor

Let

\[
A(z)
=
\int_0^\infty f(q)e^{zq}\,dq
\]

for the positive completed theta kernel.  The even completed readout is

\[
X(z)=A(z)+A(-z).
\]

Real source structure gives

\[
\overline{A(-\bar z)}=A(-z).
\]

Hence a zero of (X) satisfies

\[
|A(z)|=|A(-\bar z)|.
\]

## Sector modulus defect

Define

\[
\mathcal D(z)
=
|A(z)|^2-|A(-\bar z)|^2.
\]

For (z=\sigma+it), direct expansion gives

\[
\mathcal D(\sigma+it)
=
2
\int_0^\infty\int_0^\infty
f(q)f(v)
\sinh\!\left(\sigma(q+v)\right)
\cos\!\left(t(q-v)\right)
\,dq\,dv.
\]

Thus a strict sector law

\[
\sigma\,\mathcal D(\sigma+it)>0
\qquad
(\sigma\ne0)
\]

would exclude every off-seam zero, since any zero forces
\(\mathcal D(z)=0\).

This is the Hermite--Biehler or de Branges modulus inequality in the native
half-tail frame.

## The quarter-turn in pair coordinates

Introduce pair coordinates

\[
S=q+v,
\qquad
D=v-q.
\]

The sector modulus defect is controlled by

\[
\sinh(\sigma S)\cos(tD).
\]

The Green forcing found in the preceding packet is controlled by

\[
\sinh(\sigma D)\cos(tD)
\]

after ordering (v\ge q) and integrating the common coordinate.

The two routes therefore differ by which pair coordinate carries the
hyperbolic displacement:

- sector comparison puts growth on the sum coordinate (S);
- causal tail transport puts growth on the ordered separation (D).

This is the mathematical quarter-turn.  It exchanges global sector weight
with causal propagation distance while preserving the same source-pair
measure.

## Why the Green identity returns to de Branges

At a zero, the antidiagonal seam condition makes the two spectral factors have
equal modulus.  The Green identity then expresses the attempted equality as a
bulk norm balanced by the ordered-separation forcing.

Consequently:

- the de Branges defect is the global, pre-zero sector test;
- the Green forcing is its causal, zero-conditioned flux test;
- the curvature hierarchy is the even separation-moment expansion of the
  same pair source.

These are not three independent arguments.  They are three functorial
readouts of one two-copy theta object.

## Explanatory gain

The earlier quadrant kernel was not an accidental successful reduction.  It
appears because a zero equates the norms of the two reciprocal spectral
factors.  To forbid that equality off the seam, the source must orient the
sum-coordinate hyperbolic weight against the difference-coordinate
oscillation.

The hard theorem can therefore be stated without auxiliary operators:

\[
\sigma
\int_0^\infty\int_0^\infty
f(q)f(v)
\sinh\!\left(\sigma(q+v)\right)
\cos\!\left(t(q-v)\right)
\,dq\,dv
>0.
\]

The theta-specific modular mechanism must prove this orientation.  Generic
positive kernels do not.

## Falsifiers

The global sector route is falsified by any ((\sigma,t)), with
\(\sigma\ne0\), for which

\[
\sigma\mathcal D(\sigma+it)\le0.
\]

Such a failure does not produce a zeta zero, but it closes the proposed global
Hermite--Biehler proof.

The claimed unification is falsified if the completed theta readout cannot be
written as (A(z)+A(-z)) with the same positive half-source used in the tail
system.

## Result

The doubled Green obstruction, the de Branges modulus defect, and the
curvature hierarchy are coordinate shadows of the same positive two-copy
theta source.  The decisive RH theorem is the original sum--difference
orientation inequality, now derived from the faithful antidiagonal zero-state
geometry rather than guessed from the desired conclusion.
