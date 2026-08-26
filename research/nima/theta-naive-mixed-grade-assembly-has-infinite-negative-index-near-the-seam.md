# Naive mixed-grade assembly has infinite negative index near the seam

## Primewise condition

For one prime, the \(k=1,2\) unilateral self-commutator is positive
semidefinite only if

\[
\frac{2}{\sqrt p}
\cosh(r_p)\cosh(2r_p)
\ge1,
\qquad
r_p=x\log p,
\]

where \(x=\Re z>0\).

For large \(p\),

\[
\cosh(x\log p)\cosh(2x\log p)
\sim
\frac14p^{3x}.
\]

Hence the left side has asymptotic behavior

\[
\frac12p^{3x-1/2}.
\]

## Infinite family of negative blocks

If

\[
0<x<\frac16,
\]

then

\[
3x-\frac12<0.
\]

The positivity expression tends to zero as \(p\) tends to infinity. Therefore
all sufficiently large primes have a strictly negative \(2\times2\) boundary
minor.

The direct sum of naively mixed \(k=1,2\) currents consequently has an
infinite-dimensional negative spectral subspace throughout the open window

\[
0<\Re z<\frac16.
\]

By reciprocal reflection, the opposite half-window has the reversed infinite
defect.

The threshold \(1/6\) is the same window in which the \(k\ge3\) connected
operator tail is absolutely summable. The collision is structural: exactly
where the tail becomes harmless, untyped primitive-square mixing has infinite
negative index.

## Finite-rank repair is impossible

Let \(C\) be the self-adjoint direct sum of the primewise mixed
self-commutators. Let \(N_-\) be the span of one negative vector from every
failing prime block. Then

\[
\dim N_-=\infty.
\]

Let \(F\) be any finite-rank self-adjoint correction arising from a
finite-dimensional endpoint or gamma port. The kernel of \(F\) has finite
codimension, so

\[
N_-\cap\ker F
\]

contains a nonzero vector \(v\). For that vector,

\[
\langle(C+F)v,v\rangle
=
\langle Cv,v\rangle
<0.
\]

Therefore no finite-rank correction can make the naively assembled current
hyponormal in the near-seam window.

## Required size of a genuine sewing law

Any successful correction must act on infinitely many primewise negative
directions. It must therefore be one of the following:

- an infinite-rank operator on the primitive-square boundary carrier;
- an unbounded but closable rigged boundary relation;
- a change of assembly functor that keeps the grades orthogonal;
- an exact cancellation derived before the direct sum is formed.

A fitted finite matrix cannot work. A scalar gamma factor cannot work after
the prime directions have been erased.

This explains why the primitive and square currents must remain as
reconstructive boundary data. Their full labelled carrier is the minimum
space large enough to host a possible repair.

## Relation to completion escape

The negative eigenvalues shrink with \(p\), so finite cutoffs can make the
problem look increasingly mild while the negative index grows without bound.
Scalar determinant or trace-norm tests may miss this because they aggregate
the directions.

The correct completion audit must track both:

\[
\text{magnitude of the negative part}
\]

and

\[
\text{dimension of its support}.
\]

Vanishing operator norm without stabilization of support does not yield a
finite-dimensional orientation law.

## Finite falsifier sequence

Fix any \(x\) with \(0<x<1/6\). For increasing prime cutoff \(P\):

1. build the direct sum of exact \(k=1,2\) boundary blocks;
2. count negative eigenvalues;
3. verify that the count diverges with \(P\);
4. add the proposed endpoint or gamma correction;
5. compare its rank with the negative index;
6. exhibit a negative vector orthogonal to its range.

Any claimed finite-port repair fails once the negative count exceeds the
correction rank.

## Disposition

The single-edge signed index remains a valid source-local orientation law.
Naive arithmetic assembly destroys it in infinitely many independent
directions near the critical seam.

The surviving programme is sharply constrained: primitive and square grades
must stay separately typed, and any constructor that later couples them must
operate on their full rigged labelled carrier. The source of RH-strength
orientation, if it exists here, must be that infinite-rank sewing law.
