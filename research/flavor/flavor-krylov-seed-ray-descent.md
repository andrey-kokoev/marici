# The Krylov orientation sign does not descend in flavor

Work package: WP612  
Owner: marici.Figueiredo

## Candidate and physical domain

Nima's conditional constructor starts from an evolution (A) and seed (x):

\[
\Omega_A(x)=\det[x,Ax,A^2x].
\]

Over a real oriented frame this determinant is an alternating controllability
carrier. Flavor, however, has a common-left (U(3)) weak-basis group, and a
physical one-dimensional seed is a ray ([x]), represented by the projector
(xx^\dagger). Both quotients must be imposed before granting physical
orientation authority.

## Exact seed-ray hostile

Take

\[
A=\operatorname{diag}(1,2,3),
\qquad
x={1\over\sqrt3}(1,1,1)^T.
\]

Then

\[
\Omega_A(x)={2\over3\sqrt3}.
\]

Let (zeta=e^{i\pi/3}). The seeds (x) and (zeta x) define exactly the
same physical projector, but

\[
\Omega_A(\zeta x)=\zeta^3\Omega_A(x)=-\Omega_A(x).
\]

The same operation is the central weak-basis transformation (S=\zeta I).
It leaves (A) fixed and multiplies the determinant by
(det S=-1). More generally a central (U(1)) rotates the determinant
continuously. Its sign or phase is therefore not a function on the physical
flavor quotient.

## What does descend

In an eigenbasis of a nondegenerate Hermitian (A), with eigenvalues (a_i)
and seed components (x_i), exact factorization gives

\[
\Omega_A(x)=
\prod_{i<j}(a_j-a_i)\,x_1x_2x_3.
\]

Consequently

\[
|\Omega_A(x)|^2=
\Delta_A^2\prod_i p_i,
\qquad
p_i=\operatorname{Tr}(P_i^A P_x),
\]

for a normalized seed projector (P_x). This positive quantity descends. It
vanishes exactly when the spectrum degenerates or the seed ray misses an
eigendirection. Its normalized seed-support factor obeys

\[
\prod_i p_i\le {1\over27},
\]

with equality for democratic support.

If (A=H_u) and the seed ray is one ordered down-type eigenstate, then

\[
p_i=|V_{ij}|^2
\]

for one charged-current column. The descended Krylov magnitude is therefore a
positive function of already physical spectral and mixing data. It measures
cyclicity; it does not furnish an alternating orientation sign.

## Reference disposition

A fixed complex volume form or seed phase would make the determinant phase
relationally meaningful. That additional object reduces the weak-basis
groupoid to its stabilizer. It defines a new reference experiment and must be
derived and instrumented explicitly; it cannot be described as recovery of an
absolute flavor orientation.

## Selector and instrument status

The three-port Cayley--Hamilton closure and the two cyclicity falsifiers remain
valid. Their status is now separated:

- (|\Omega|^2) is a positive cyclicity carrier and physical readout;
- its spectral weights have a charged-current instrument;
- the phase or sign of (Omega) has no instrument on the unreferenced flavor
  quotient;
- neither object selects the observed small nonzero (J) magnitude.

Thus a microscopic (A,x) pair could still be useful, but it must either act
through the positive descended magnitude or supply a physical volume/phase
reference as part of a new relational source architecture.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp612_krylov_seed_ray_descent.py

The generated result is
research/flavor/results/wp612_krylov_seed_ray_descent.json.
