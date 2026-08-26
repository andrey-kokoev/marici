# Inward Divisor Transport Is Not Closed under Positive Superposition

The repaired DPC proposes a source-defined admissible cone carrying inward
divisor transport. The word “cone” is substantive: an ordinary convex cone is
closed under positive scaling and addition. The divisor-velocity law is not.

For a state-current pair

\[
F_t=F+tG,
\]

a simple zero \(z\) of \(F\) has instantaneous velocity

\[
z'=-\frac{G(z)}{F'(z)}.
\]

Consider two exact affine pairs:

\[
(F_1,G_1)=(z-10,1),
\]

\[
(F_2,G_2)=(z+9,-100).
\]

The first zero is \(z_1=10\), with

\[
z_1'=-1,
\qquad
z_1z_1'=-10<0.
\]

The second zero is \(z_2=-9\), with

\[
z_2'=100,
\qquad
z_2z_2'=-900<0.
\]

Both move strictly toward the seam \(\operatorname{Re}z=0\).

Their positive sum is

\[
(F_1+F_2,G_1+G_2)=(2z-1,-99).
\]

Its zero is \(z=1/2\), but

\[
z'=\frac{99}{2},
\qquad
zz'=\frac{99}{4}>0.
\]

The superposed zero moves outward.

## Exact obstruction

Let \(\mathcal R\) denote the set of state-current pairs satisfying strict
inward transport at every simple off-seam zero. Then

\[
(F_1,G_1),(F_2,G_2)\in\mathcal R
\]

does not imply

\[
(F_1+F_2,G_1+G_2)\in\mathcal R.
\]

Thus \(\mathcal R\) is not a convex cone and not a linear submodule.

This is not repaired by saying that both currents arise from one linear
generator. On the two-dimensional span of \(F_1,F_2\), a linear operator can
be defined by

\[
AF_1=G_1,
\qquad
AF_2=G_2.
\]

Linearity then forces

\[
A(F_1+F_2)=G_1+G_2,
\]

which is precisely the outward fixture.

## Consequence for the repaired DPC

The source cannot obtain the desired class merely by intersecting a linear
state space with an atomwise inward condition. It needs additional correlated
structure that forbids independent positive superposition of admissible
trajectories.

There are only three honest repairs:

1. Replace the cone by a nonlinear, nonconvex constructor orbit.
2. Retain a convex cone but prove that the source admits only specially coupled
   state-current pairs, excluding at least one member of every hostile sum.
3. Replace zero-by-zero velocity with an additive operator or energy law from
   which divisor confinement follows globally.

The third is the most explanatory candidate. Additive source algebra naturally
controls quadratic forms, currents, and positive kernels. Individual zero
velocities are ratios and therefore compose badly.

## Authority boundary

The affine fixture is an abstract compiler counterexample, not a theta/Tate
state. It does not prove that the source admits either trajectory. It proves
that linearity, cone invariance, and atomwise inward motion are not mutually
automatic. The source must exhibit the nontrivial correlation law rather than
calling the successful set a cone.

## Falsifiers for the surviving DPC

- Two independently admitted source trajectories whose sum is admitted but
  moves a zero outward.
- A claimed convex cone whose state-current relation is not closed under
  addition.
- A linear generator whose invariant state cone does not preserve the phase
  inequality.
- Excluding hostile sums only after their zeros are inspected.
- Replacing an additive source law by a nonadditive zero-velocity ratio without
  a constructor derivation.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to test compatibility between the revised conjecture and
linear superposition.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Inward divisor transport is exactly nonconvex; the conjecture must use a
correlated nonlinear orbit or return to an additive energy theorem.
