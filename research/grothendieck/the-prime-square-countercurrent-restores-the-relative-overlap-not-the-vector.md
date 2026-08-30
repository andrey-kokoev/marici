# The Prime-Square Countercurrent Restores the Relative Overlap, Not the Vector

## Vanishing finite overlap

For squarefree \(Q\), the overlap between the normalized additive vacuum and
the multiplicative half-density is

\[
a_Q
=
\sqrt{\frac{\varphi(Q)}{Q}}
=
\prod_{p\mid Q}\sqrt{1-p^{-1}}.
\]

It tends to zero along primorial cutoffs.

## Canonical square renormalization

Define the relative overlap

\[
\widetilde a_Q
=
a_Q
\exp\left(
\frac12\sum_{p\mid Q}p^{-1}
\right).
\]

Its logarithm is

\[
\log\widetilde a_Q
=
\frac12\sum_{p\mid Q}
\left(
\log(1-p^{-1})+p^{-1}
\right).
\]

Expanding the logarithm gives

\[
\log\widetilde a_Q
=
-\frac12
\sum_{p\mid Q}
\sum_{k\ge2}\frac{p^{-k}}{k}.
\]

The double series converges absolutely over all primes. Therefore

\[
\widetilde a_Q
\longrightarrow
\widetilde a_\infty
=
\exp\left(
-\frac12
\sum_p\sum_{k\ge2}\frac{p^{-k}}{k}
\right),
\]

and

\[
0<\widetilde a_\infty<1.
\]

The limit is independent of prime exhaustion.

## Grade interpretation

At the critical half-density, the local primitive amplitude is
\(p^{-1/2}\). The divergent term \(p^{-1}\) is its square. Thus the
counterfactor

\[
\exp\left(
\frac12\sum_{p\mid Q}p^{-1}
\right)
\]

is exactly the prime-square boundary current required to renormalize the
half-density overlap. The remaining \(k\ge2\) terms in powers of \(p^{-1}\)
form an absolutely convergent tail.

This derives the relative determinant-line scalar directly from the
additive--multiplicative Hellinger comparison.

## What is and is not repaired

The result repairs the scalar overlap:

\[
a_Q\to0,
\qquad
\widetilde a_Q\to\widetilde a_\infty\ne0.
\]

It does not repair the half-density vectors \(h_Q\). Those vectors still
have norm one and converge weakly to zero against every finite-conductor
observer.

Multiplying \(h_Q\) by the divergent counterfactor would make their norms
diverge. The renormalization is therefore line-valued: it belongs to the
relative determinant of the correspondence, not to either Hilbert-space
state.

## Consequence

The additive--multiplicative bridge has two independent outputs:

1. a renormalized nonzero determinant-line overlap;
2. a representation-changing correspondence whose state vectors remain
   disjoint.

The first is now constructed canonically. It cannot substitute for the
second, and by itself it has no RH zero-selection force. A nonzero relative
determinant scalar does not imply that the connected prime current lands in
the tempered archimedean boundary space.

## Revised frontier

The remaining theorem must combine:

- the multiplicative Haar sector;
- the additive theta sector;
- the nonzero square-renormalized overlap line;
- the conductor-corona state;
- and the archimedean half-density current.

The desired temperedness must be proved for the full correspondence. No
further scalar renormalization of the vacuum overlap is missing.

## Falsifier

A proposed construction fails if it:

- subtracts any term other than the source-derived \(p^{-1}/2\) divergence;
- produces an exhaustion-dependent limit;
- claims the renormalized scalar creates a strong vector limit;
- or uses the nonzero determinant overlap as evidence of RH orientation.

