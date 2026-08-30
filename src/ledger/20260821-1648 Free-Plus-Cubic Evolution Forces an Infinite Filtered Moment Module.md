# 1648 — Free-Plus-Cubic Evolution Forces an Infinite Filtered Moment Module

## Closure test

Entry 1647 identifies the first missing mixed quadratic observable.  Test whether adjoining finitely many polynomial moments closes the process coefficient object under the full free-plus-cubic evolution.

## Exact derivation

For one canonical pair, use

\[
H=\frac{p^2}{2}+\frac{q^3}{3}.
\]

The associated-grade Heisenberg/Hamiltonian derivation is

\[
D f
=
\{f,H\}
=
p\,\partial_qf-q^2\,\partial_pf.
\]

The free term preserves polynomial degree; the cubic term can raise it by one.  Starting at (q), the exact iterates begin

\[
Dq=p,
\qquad
D^2q=-q^2,
\qquad
D^3q=-2qp.
\]

The sparse exact checker obtains the maximum-degree sequence

\[
1,1,2,2,3,3,\ldots,12,12,13
\]

through 24 iterations.  Degree rises every second step.

## Narrow result

\[
\boxed{
\text{No finite polynomial-degree moment space containing the canonical variables is invariant under free-plus-cubic evolution.}
}
\]

The isolated position-only cubic kick is misleadingly finite because its nested commutators can terminate.  Free propagation converts positions into momenta and repeatedly reactivates degree growth.

Therefore the supported process coefficient object is an infinite filtered moment module.  Finite moment systems remain useful associated grades or controlled truncations, but they are not globally closed coefficient objects.

This infinite rank is coefficient complexity over the existing labelled carrier.  It does not supply evidence for infinitely many new carrier strata.

## Durable artifacts

- `research/benincasa/checkers/free_cubic_moment_hierarchy.rs`
- `research/benincasa/results/free-cubic-moment-hierarchy.json`
- `research/benincasa/free-cubic-moment-hierarchy.md`

## Next falsifier

Determine whether the infinite filtration is finitely generated as a module over the evolution derivation and polynomial observable algebra.  A finite cyclic or holonomic presentation would retain computational control; failure would require a genuinely non-Noetherian coefficient architecture.
