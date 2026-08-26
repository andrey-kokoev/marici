# The prime-cutoff adjoint-anomaly cocycle is exact and universal

## Bounded question

Does the extensive off-seam adjoint anomaly define a nontrivial conserved
charge under Euler-cutoff enlargement?

## Cutoff category

Let \(S\) be a finite set of primes and put

\[
x=\operatorname{Re}\left(s-\frac12\right).
\]

The logarithmic modulus anomaly of the native two-sheet comparison is

\[
A_x(S)=2x\sum_{p\in S}\log p.
\]

Adding a new prime \(q\notin S\) gives the increment

\[
A_x(S\cup\{q\})-A_x(S)=2x\log q.
\]

The increment is independent of \(S\). It is therefore a closed additive
one-cocycle on the Boolean cutoff category.

## Exactness

The cocycle is the coboundary of the explicit zero-cochain \(A_x\) itself.
Equivalently, the path-independent countercurrent

\[
B_x(S)=-2x\sum_{p\in S}\log p+C(x)
\]

satisfies

\[
B_x(S\cup\{q\})-B_x(S)=-2x\log q.
\]

Hence

\[
A_x(S)+B_x(S)=C(x)
\]

is conserved under every cutoff enlargement.

Conversely, any path-independent scalar countercurrent with the required
single-prime increments has this form. Its only freedom is the cutoff-independent
constant \(C(x)\).

## Why this conservation law has no RH force

The construction uses only the local coefficient mismatch and the labelled
prime set. It does not use:

- the theta source;
- a scalar zero-state;
- primitive or square endpoint conditions;
- the archimedean Gaussian;
- reciprocal star compatibility.

Therefore the conserved quantity exists for every spectral displacement and
for every hostile system with the same local prime coefficients. Choosing
\(C(x)=0\) makes the total charge vanish identically for all \(x\), including
off seam.

The conservation law is bookkeeping of an exact cutoff cocycle. It cannot
force \(x=0\).

## Prime powers do not change the result

On the finite set of prime-power labels, replace the potential by

\[
A_x^{\rm pp}(X)=2x\sum_{p^k\leq X}\log p.
\]

Each newly admitted incidence again contributes an exact increment
\(2x\log p\). The primitive, square, and higher filtration types the pieces of
the potential but does not create cutoff holonomy.

## Result

The first candidate conserved charge demanded by the Deutsch audit exists,
but it is exact, universal, and zero-insensitive. It explains how to
renormalize the native adjoint anomaly, not why an off-seam zero is impossible.

This closes any RH argument based only on telescoping the scalar local modulus
defects over Euler cutoffs.

## Remaining explanatory target

A nontrivial charge must involve a second operation whose square fails to
commute with cutoff addition by a source-typed residual. In categorical terms,
the programme now needs a mixed coherence cell, not a one-dimensional cutoff
cocycle. The natural candidate is the square formed by prime addition and
Fourier--Tate or archimedean transport. Its residual must vanish for the theta
source, fail for hostile sources, and couple to the scalar zero-state boundary
condition.
