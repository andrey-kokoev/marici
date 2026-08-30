# Universal rank-one determinant bridge is nonexplanatory

## Question

Reciprocal graph observability does not control a scalar overlap zero.  The
next requested bridge is a source-derived operator whose determinant section
is the completed theta scalar.  Is the mere existence of such an operator
already meaningful?

## Exact rank-one realization

Write

\[
\Xi(z)
=
\frac12
\left(
1+a(z)K(z)
\right),
\qquad
a(z)=z^2-\frac14.
\]

Let \(\mathcal H\) be any Hilbert realization of the source overlap

\[
K(z)=\langle\Omega,u_z\rangle.
\]

Define the rank-one Fredholm family

\[
T_z
=
I+a(z)|u_z\rangle\langle\Omega|.
\]

The rank-one determinant lemma gives

\[
\det T_z
=
1+a(z)\langle\Omega,u_z\rangle
=
2\Xi(z).
\]

Thus

\[
\Xi(z)=0
\quad\Longleftrightarrow\quad
\ker T_z\ne0.
\]

The desired zero-to-kernel bridge can therefore be manufactured immediately.

## Why this does not explain anything

The construction uses only the already aggregated scalar overlap \(K(z)\).
It does not retain:

- theta labels;
- primal--dual transport;
- primitive or prime-square boundary currents;
- modular sewing incidence;
- any independent conservation law.

The equivalence between zero and kernel is the matrix determinant lemma read
backward.  Proving \(T_z\) invertible off the seam is exactly the original
scalar nonvanishing problem.

The inverse makes the circularity visible:

\[
T_z^{-1}
=
I-
\frac{a(z)}{1+a(z)K(z)}
|u_z\rangle\langle\Omega|.
\]

Its only obstruction is the scalar denominator \(2\Xi(z)\).

## Hostile lift

Every hostile tail \(K_H\) from the normalized reciprocal-even multiplier
construction has the same rank-one realization

\[
T_{H,z}
=
I+a(z)|u_{H,z}\rangle\langle\Omega_H|,
\]

with

\[
\det T_{H,z}=2\Xi_H(z).
\]

Therefore determinant typing alone does not reject inserted off-seam
quartets.  The hostile divisor simply becomes a hostile rank-one kernel.

## Strengthened determinant requirement

A meaningful theta determinant bridge must satisfy all of the following:

1. The operator is constructed on the labelled source module before scalar
   aggregation.
2. Its local blocks and domains are forced by theta/Tate transport.
3. Modular and boundary currents appear as operator incidences, not as fitted
   determinant coefficients.
4. The determinant identity is a consequence of eliminating the labelled
   system.
5. An independent Green, index, or exactness law constrains its kernel.
6. A normalized reciprocal-even hostile multiplier has no lift preserving
   those operator relations.

The determinant must be a shadow of a prior executable system.  It cannot be
the definition of that system.

## Relation to the source graph

Kitaev's reciprocal graph remains the correct observability layer once the
operator is legitimate.  The order is now strict:

1. derive the labelled comparison operator;
2. prove its determinant compresses to \(\Xi\);
3. pair it with its reciprocal adjoint graph;
4. establish kernel-core and reduced-minimum-modulus stability;
5. use the boundary polarization law to exclude off-seam kernels.

Skipping the first step reduces the entire programme to the universal
rank-one trick.

## Immediate target

The source-local operator cannot be inferred from \(K\).  It must be derived
from the translate family

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n)
\]

and its primal--dual completion.  The smallest credible construction should
have at least one nontrivial label-transport block whose elimination produces
the scalar cosh tail.

The finite falsifier is a proposed block system whose Schur complement equals
\(2\Xi\) only because a matrix entry was set equal to \(K\) or \(\Xi\).  Such
a system is rank-one repackaging, not a source derivation.

## Result

Every scalar overlap admits an exact rank-one Fredholm determinant bridge.
Consequently, a zero-to-kernel equivalence is not by itself progress toward
RH.  The missing theorem is a labelled, source-local operator construction
whose determinant and kernel law are both derived consequences.
