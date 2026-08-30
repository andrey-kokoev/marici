# Oriented triangular frustration is a collective CP selector

Work package: WP604  
Owner: marici.Figueiredo

## Admitted source domain

Take three labelled unit-modulus source phases

\[
z_j=e^{i\theta_j},
\]

quotiented by common \(U(1)\) phase and by cyclic permutation \(C_3\). Bare
CP acts by complex conjugation. Radial stabilization is assumed upstream; the
claim is restricted to this phase domain.

The frustrated positive carrier is

\[
B=\lvert z_1+z_2+z_3\rvert^2.
\]

Its zero set consists exactly of equilateral phase triples. Modulo common
phase, the two chiral representatives are

\[
(1,\omega,\omega^2),
\qquad
(1,\omega^2,\omega),
\qquad
\omega=e^{2\pi i/3}.
\]

This fixes the relative phase geometrically, without inserting an observed
flavor number.

## The accidental-reflection hostile

The carrier \(B\) alone has full permutation symmetry \(S_3\). A transposition
composed with CP fixes either chiral representative. Ordinary triangular
frustration therefore does not establish physical spontaneous CP breaking.

Introduce the cyclic orientation carrier

\[
F=\sum_{\mathrm{cyc}}
\cos(\theta_1+2\theta_2-3\theta_3).
\]

Its exact permutation symmetry is \(C_3\), not \(S_3\). It is bare-CP even,
but a transposition changes it. For any

\[
\lvert\epsilon\rvert<1/3,
\]

the complete positive phase potential

\[
V=B(1+\epsilon F)
\]

has the same zero set as \(B\), since \(\lvert F\rvert\le3\). Thus the
orientation carrier removes the accidental reflection without moving the
selected phase relation.

After fixing the common phase, the two Hessian eigenvalues at the displayed
vacuum are

\[
1-{3\epsilon\over2},
\qquad
3-{9\epsilon\over2},
\]

which are positive throughout the declared domain. The result is stable under
continuous variation of \(\epsilon\) inside that interval.

## Generalized-CP audit

Within the admitted torus-preserving monomial transformations, the complete
pair graph in \(B\) forces every diagonal rephasing to be a common \(U(1)\).
The remaining internal permutation group is exactly \(C_3\). No cyclic
permutation composed with CP maps the conjugate Fourier mode back to the
selected mode, even after allowing that common phase. Hence neither chiral
vacuum has a generalized-CP stabilizer in the admitted group.

Restoring any transposition restores a stabilizer immediately. This is the
smallest exact falsifier and shows that the orientation carrier is
load-bearing.

## Explanatory status

WP604 is the first progressive collective source selector in this branch:

- its relative phase is fixed by a positive zero-set constraint;
- the result is coefficient-independent on an open parameter interval;
- bare CP is a source symmetry;
- the selected vacuum has no generalized-CP stabilizer;
- the reflection-restoration hostile is exact.

It is not yet an explanation of observed flavor. The oriented carrier is a
higher-degree interaction on the unit-phase domain. A microscopic field
theory must derive the cyclic tensor, radial completion and positivity rather
than declaring them because they produce CP breaking. The source orbit must
then descend through a weak-basis-invariant portal to `physical16`, and its
prediction must survive the complete fitted ensemble.

## Independent experimental criticism

The microscopic completion should contain the mediators generating the
oriented cyclic interaction. WP603 gives the minimum probe typing:

- resolve the mediator masses and partial widths;
- retain a common coherent final state;
- measure the sign-sensitive interference that distinguishes orientation
  reversal;
- verify the matching relation against the CP-odd `physical16` portal.

Reflection-symmetric mediator couplings, absence of the oriented interaction,
or a threshold interference sign inconsistent with the low-energy CP branch
would refute the architecture. This remains a prospective experiment until a
specific mediator and detector channel are supplied.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp604_oriented_triangle_collective_cp_selector.py

The generated result is
research/flavor/results/wp604_oriented_triangle_collective_cp_selector.json.
