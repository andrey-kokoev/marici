# Finite character probes have constructive route collisions

## Question

Can the predicted failure of every fixed finite character-probe family be exhibited by explicit equal-readout Carrier routes rather than dimension counting alone?

## Claim boundary

Shell-count vectors are finitely supported sequences in the free vector space \(W\). The tested probe family evaluates the shell polynomial at settings \(1,2,\ldots,m\). This proves nonfaithfulness for that family and illustrates the general finite-rank obstruction; it does not prove that every possible nonlinear or noncharacter readout is nonfaithful.

## Probe

For \(a=1,\ldots,m\), define

\[
\chi_a(v)=\sum_{i\geq1}v_i a^{i-1}.
\]

On the first \(R\) shells the evaluation matrix is Vandermonde:

\[
M_{a,i}=a^{i-1}.
\]

For \(R>m\), its rank is \(m\), and the Hankel Gram matrix

\[
Q=M^{\mathsf T}M
\]

has radical dimension \(R-m\).

## Constructive collision

Let

\[
P_m(x)=\prod_{a=1}^{m}(x-a)=\sum_{i=0}^{m}c_i x^i.
\]

Split its coefficient vector into nonnegative vectors

\[
u_i=\max(c_i,0),
\qquad
v_i=\max(-c_i,0).
\]

Then \(u\neq v\), but

\[
\chi_a(u)=\chi_a(v)
\]

for every tested setting. Because 1 is among the settings,

\[
\sum_i u_i=
\sum_i v_i,
\]

so the collision preserves total route length. The two shell-count vectors also give distinct prime-ratio endpoints; after choosing a base divisible by all required source-prime powers, both become executable routes with different endpoints and identical finite-probe readout.

## Infinite separating family

A finitely supported shell vector defines a polynomial. If it vanishes at every positive integer, it has infinitely many roots and is zero. Hence the countable family \(\{\chi_a\}_{a\geq1}\) is jointly faithful on finitely supported shell vectors, although no finite subfamily is.

## Strongest falsification attempt

For \(m=1,\ldots,8\) and shell cutoffs through 20, compute exact ranks of \(M\) and \(Q\), verify the radical dimension, construct \(u,v\) from \(P_m\), check equal readouts and equal route lengths, realize both from a common integral base, and require distinct integral endpoints.

## Computed result

For every \(m=1,\ldots,8\) and every tested cutoff \(m<R\leq20\), both \(M\) and \(Q\) have rank exactly \(m\), while the radical of \(Q\) has dimension \(R-m\). The coefficient split of \(P_m\) produces two distinct nonnegative routes with equal total length and identical readouts at all \(m\) settings. After a common executable base is supplied, their integral endpoints are distinct.

The bounded exhaustive sample of nonzero coefficient vectors with entries in \(\{-1,0,1\}\) and support at most five is separated by the first six settings, consistent with joint faithfulness of the countable family.

## Disposition

The finite-character nonfaithfulness prediction survives constructively. Every finite family \(1,\ldots,m\) has explicit same-length, different-endpoint route collisions once shell \(m+1\) is admitted. Countably many settings separate all finitely supported shell vectors by the polynomial root theorem. This result does not constrain nonlinear readouts.
