# The cross-prime Magnus channel is not absolutely summable

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact completion obstruction

## Pairwise channel

For the normalized seam exchanges of ledger 3061,

\[
[X_p(t),X_q(t)]
=2i\sin\left(t\log\frac qp\right)\sigma_3.
\]

For the unnormalized exchanges, the corresponding magnitude is

\[
\frac{2}{\sqrt{pq}}
\left|\sin\left(t\log\frac qp\right)\right|.
\]

This is the second-order cross-prime term in any ordered-product or Magnus
expansion of the doubled reciprocal connection.

## Absolute divergence

Fix \(t\ne0\). Choose \(r>1\) such that

\[
\left|\sin(t\log r)\right|=1.
\]

By continuity, there are proportional intervals

\[
p\in[X,(1+\varepsilon)X],
\qquad
q\in[r_0X,r_1X]
\]

with \(1<r_0<r_1\), such that every ratio \(q/p\) in the resulting rectangle
satisfies

\[
\left|\sin\left(t\log\frac qp\right)\right|\ge c_t>0.
\]

The prime number theorem gives asymptotically a constant multiple of
\(X/\log X\) primes in each interval. Every pair in the rectangle contributes
at least a constant multiple of \(1/X\). Therefore the rectangle contributes
at least

\[
C_t\frac{X}{(\log X)^2}.
\]

This tends to infinity. Taking disjoint growing rectangles proves

\[
\sum_{p<q}
\frac{\left|\sin(t\log(q/p))\right|}{\sqrt{pq}}
=\infty
\]

for every fixed \(t\ne0\).

At \(t=0\), every commutator vanishes. The discontinuity in completion type is
therefore tied to spectral height, not to a finite exceptional prime set.

## Consequence

The nonabelian prime connection cannot be completed by applying only the
local primitive and prime-square counterterms already attached to individual
Euler factors. Noncommutativity creates a genuinely new pair-labelled
boundary current.

A surviving construction must do one of the following:

1. derive an exact cross-prime cancellation before taking norms;
2. supply a source-authorized pair-current counterterm;
3. replace ordered multiplication by a different global composition whose
   coherence kills the commutator sector; or
4. show that the relevant determinant functor is insensitive to this channel
   while retaining enough noncommutative information to avoid the scalar
   gauge no-go.

The fourth option is delicate: determinant and trace erase commutators, so it
may simply return to the nonexplanatory scalar Euler product.

## Falsifier and boundary

The theorem proves failure of absolute summability, not failure of every
conditional or renormalized ordering. A claimed completion survives only if
it specifies its ordering, pair-current subtraction, cutoff covariance, and
independence from arbitrary regrouping.

## Scope

The pairwise formula and absolute-divergence theorem use only the exact
commutator and the prime number theorem. No claim is made that all conditional
ordered products diverge. No completed operator, determinant bridge, zero
confinement, or RH theorem is constructed.

