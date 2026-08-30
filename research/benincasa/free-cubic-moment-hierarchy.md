# Free-plus-cubic evolution generates an unbounded moment hierarchy

For one canonical pair, take

\[
H=\frac{p^2}{2}+\frac{q^3}{3}.
\]

The classical Hamiltonian derivation, equivalently the associated-grade Heisenberg derivation, is

\[
D f=\{f,H\}=p\,\partial_qf-q^2\,\partial_pf.
\]

The quadratic/free part preserves polynomial degree.  The cubic part can raise it by one.  Starting from (q), repeated application gives

\[
Dq=p,
\qquad
D^2q=-q^2,
\qquad
D^3q=-2qp,
\]

and subsequent alternation between free propagation and cubic interaction continues to produce higher degrees.

The exact sparse-polynomial checker iterates (D) without numerical fitting.  The maximum degree rises every second iteration and reaches degree thirteen within 24 iterations.  Hence no finite polynomial-degree observable space containing the canonical variables is invariant under the full free-plus-cubic generator.

This distinguishes the isolated cubic kick, whose position-only commutators can terminate, from actual time evolution including the free Hamiltonian.  The minimal process coefficient object is therefore a filtered infinite moment module.  Finite degree truncations are associated grades or approximations, not closed global dynamics.
