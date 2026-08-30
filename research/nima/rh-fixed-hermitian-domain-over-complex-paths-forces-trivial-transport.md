# A fixed Hermitian domain over complex paths forces trivial transport

## The orientation defect

The Schubert-cell formulation suggested proving forward invariance of a
projective domain. But the spectral parameter is complex. A half-plane is not
a time axis, and a holomorphic connection admits transport in every local real
direction and along the reverse path.

Calling one direction forward therefore requires an additional source-derived
orientation or semigroup law. Without it, ordinary path transport is locally a
group action.

## Infinitesimal no-go theorem

Let `U(z)` be a holomorphic operator family with `U(0)=I`, and write

\[
A=U'(0).
\]

Suppose one fixed nondegenerate Hermitian form `J` is preserved along both the
real and imaginary spectral directions.

Along `z=t`, infinitesimal preservation gives

\[
A^*J+JA=0.
\]

Along `z=it`, the generator is `iA`, so preservation gives

\[
(iA)^*J+J(iA)=0,
\]

or

\[
-A^*J+JA=0.
\]

Adding and subtracting the two equations yields

\[
JA=0,
\qquad
A^*J=0.
\]

Since `J` is nondegenerate, `A=0`.

Thus a nonconstant holomorphic transport cannot preserve one fixed Hermitian
metric, disk, or positive polarization in every complex direction. The same
obstruction applies to a holomorphic family valued in a fixed pseudo-unitary
group.

## Exact two-direction witness

Take the real skew generator

\[
A=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]

and `J=I`. Along the real direction,

\[
A^*+A=0,
\]

so the infinitesimal flow is unitary. Along the imaginary direction, the
generator is `iA`, and

\[
(iA)^*+iA=2iA\ne0.
\]

The same source generator becomes a Hermitian boost rather than a unitary
rotation after the quarter-turn in parameter direction.

## Consequence for the fifth tower

The invariant-domain route cannot use one fixed positive geometry over the
whole complex half-plane unless the relevant transport is trivial. A viable
law must distinguish the two real spectral directions.

The natural typed decomposition is:

- tangential motion along the critical seam, potentially unitary;
- normal displacement away from the seam, requiring a directed contractive,
  dissipative, or monotone law;
- reciprocal reflection exchanging the two choices of normal orientation.

This is not yet such a law. It identifies the required missing type: an
oriented semigroup structure on normal displacement. Analytic continuation
alone supplies a reversible complex group and cannot choose it.

## Surviving architectures

At least four possibilities remain:

1. a source-derived semigroup only in the outward normal coordinate, with
   unitary transport tangentially;
2. a moving Hermitian form plus an independently fixed comparison to the Evans
   observer;
3. a complex-algebraic invariant flag or Schubert domain that does not depend
   on Hermitian positivity;
4. a path-ordered curvature law whose sign changes under reciprocal normal
   reversal.

The first is the cleanest. If `z=a+it` relative to the seam, the desired law
would treat `t` as reversible phase evolution and `a` as an oriented
source-scale flow. The orientation must be derived from endpoint, modular, or
valuation data rather than declared from the desired zero-free half-plane.

## DPC

Reject any invariant-domain proposal that:

- calls complex spectral transport forward without defining its source
  orientation;
- requires one fixed Hermitian form to be preserved in both real directions;
- proves only seam unitarity and extrapolates it into the half-plane;
- chooses the sign of normal evolution from known zero locations;
- replaces a group by a semigroup without typing the lost inverse operation.

A candidate passes the first gate only if it supplies:

- the source operation generating normal displacement;
- its admissible direction and composition law;
- the reciprocal functor exchanging the two directed semigroups;
- the tangential unitary action;
- a mixed coherence law between tangential and normal transport;
- a projective invariant region with completion-stable distance from the Evans
  divisor.

## Verdict

Fixed positive Schubert-cell invariance over arbitrary complex paths is too
strong and collapses nontrivial holomorphic transport. The sharpened target is
an anisotropic spectral calculus: unitary along the seam and source-oriented
semigroup transport normal to it.

