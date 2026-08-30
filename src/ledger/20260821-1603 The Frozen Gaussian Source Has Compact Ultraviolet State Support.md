# Entry 1603 — The Frozen Gaussian Source Has Compact Ultraviolet State Support

## Correction of scope

Entries 1594--1601 audited the formal cutoff-free Hadamard tail
\(\beta_k=o(k^{-2})\).  The primary source makes a stronger operational
choice.  After stating the Hadamard falloff, it enforces the EFT cutoff by
demanding

\[
\beta_k\longrightarrow0
\quad\text{for}\quad
k>\frac{\Lambda_*a_0}{c_s}.
\]

This is the immutable source prescription in arXiv:1212.1172v2, Sec. 4,
immediately after the Hadamard statement.  Its model profile is also written
as a function of \(q=c_sk/(a_0\Lambda_*)\), with the high-energy state returned
to the vacuum.

## Consequence

For the literal source object, the anomalous endpoint residual of Entries
1600--1601 has compact radial support.  Hence it is a finite state-dependent
coefficient inside the EFT domain, not an ultraviolet divergence requiring a
new counterterm:

\[
\boxed{
\operatorname{supp}\beta
\subseteq
\left\{k\leq\Lambda_*a_0/c_s\right\}.
}
\]

Its disjointness from the local bulk-counterterm frequency module remains
true, but no subtraction is forced by the frozen source.

## Narrow surviving extrapolation

If the hard cutoff is removed and only \(\beta_k=o(k^{-2})\) is retained, the
source does not supply derivative or bounded-variation estimates sufficient
to justify conditional convergence of

\[
\int^\infty dQ\,Q^2\beta_Qe^{2iQ\eta_0}.
\]

That cutoff-free problem is a separate coefficient-regularity conjecture.  It
must not be attributed to the frozen paper.

## Classification

- carrier: unchanged sourced-time/loop carrier;
- coefficient data: finite compactly supported Bogoliubov profile;
- new carrier datum: none;
- UV obstruction in the literal source: none.

## Next falsifier

Within the finite EFT support, test whether the residual preserves the
Hadamard-filtered Gaussian coefficient object under one-loop Dyson evolution,
including the conjugate \(\beta^*\) character and the statistical channel.

Allocator claim: `seqclaim-6cc9e80733fb6ba18de5b3fc`.
