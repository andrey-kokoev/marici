# Radiative-memory scalarization retains nonabelian orbit information

The direction-resolved memory readout of the preceding audit carries the
standard rank-two representation of \(D_3\).  Write a memory difference as

\[
(x,y,z)=(a,-a+b,-b),
\qquad x+y+z=0.
\]

The permutation invariants restrict to

\[
q_2=a^2-ab+b^2,
\qquad
q_3=ab(a-b).
\]

Because \(D_3\simeq S_3\) is the reflection group of type \(A_2\), its
invariant algebra on the standard plane is

\[
\boxed{
\mathbb Q[a,b]^{D_3}=\mathbb Q[q_2,q_3].
}
\]

The exact checker verifies both generators under all six matrices on 625
integer points and confirms that \((q_2,q_3)\) separates every group orbit on
that bounded control grid.

## Conceptual correction

Invariant scalarization is not group abelianization.  The covariant memory
multiplet detects the commutator subgroup, while its scalar invariant algebra
still records the resulting nonabelian orbits through degree-two and
degree-three data.

Thus the refined sequence is

\[
\text{nonabelian covariant multiplet}
\longrightarrow
\operatorname{Spec}\mathbb Q[q_2,q_3]
\longrightarrow
\text{commutative scalar records}.
\]

The output algebra is commutative because scalar observables multiply
commutatively—not because the underlying symmetry action has been replaced by
its abelianization.

For the constructor-principle hypothesis, the readout constructor may
therefore compute an **orbit invariant** of a nonabelian task.  Arithmetic
structure should be sought in the algebra of stable invariant records, while
the transformation groupoid remains nonabelian.

Evidence: Ledger Entry 1056 and
`research/nima/radiative-memory-d3-commutator.md`.
