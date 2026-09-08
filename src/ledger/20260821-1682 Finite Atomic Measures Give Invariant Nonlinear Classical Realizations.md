# 1682 — Finite Atomic Measures Give Invariant Nonlinear Classical Realizations

## Finite-family falsifier

Entry 1681 proves that scalar-cubic evolution is not autonomous on the
quadratic moment cone. Test whether this forces every exact positive process
realization to be infinite-dimensional.

For

\[
\dot q=p,
\qquad
\dot p=-q^2,
\]

take an (N)-atomic positive measure

\[
\mu=\sum_{s=1}^Nw_s\delta_{(q_s,p_s)},
\qquad
w_s>0,
\qquad
\sum_sw_s=1.
\]

Hamiltonian pushforward transports each atom independently:

\[
\dot q_s=p_s,
\qquad
\dot p_s=-q_s^2,
\qquad
\dot w_s=0.
\]

Therefore the family remains (N)-atomic and positive. Its moments

\[
m_{ab}=\sum_sw_sq_s^ap_s^b
\]

satisfy exactly

\[
\boxed{
\dot m_{ab}
=a,m_{a-1,b+1}-b,m_{a+2,b-1}.
}
\]

The exact checker verifies twenty three-atom families, 1,320 moment-hierarchy
identities through degree ten, and 800 positive polynomial-square evaluations.

For fixed (N), the parameter space has dimension

\[
2N+(N-1)=3N-1.
\]

In particular, the tested three-atom realization is eight-dimensional.

## Narrow result

\[
\boxed{
\text{the classical scalar-cubic process has finite-dimensional invariant positive families.}
}
\]

This does not contradict Entries 1648 and 1681. The moment hierarchy is an
infinite linear coefficient representation; an (N)-atomic family is a finite
nonlinear subvariety whose infinitely many moments satisfy algebraic rank
relations.

This result is classical. Delta measures on phase space do not automatically
define positive quantum states and generally violate quantum uncertainty.

## Durable artifacts

- `research/benincasa/checkers/finite_atomic_classical_realization.rs`
- `research/benincasa/results/finite-atomic-classical-realization.json`
- `research/benincasa/finite-atomic-classical-realization.md`

## Next falsifier

Test whether the finite atomic realization is compatible with
cardinality-weighted Cut merge. Determine how atom counts multiply under
independent product and how coincident pushed-forward atoms reduce the count.
Classify whether the resulting finite-state category is closed under Cut,
dynamics, and convex mixture simultaneously.