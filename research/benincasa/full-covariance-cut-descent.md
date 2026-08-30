# Full covariance makes correlated Gaussian Cut descent tree-independent

For a block (A) of labelled internal occurrences define the extensive
covariance

\[
S_A=\sum_{i,j\in A}\Sigma_{ij}
\]

and, for disjoint blocks, the cross covariance

\[
K_{AB}=\sum_{i\in A,j\in B}\Sigma_{ij}.
\]

The normalized collective variance is \(\nu_A=S_A/|A|\). Merging two blocks
uses

\[
S_{A\cup B}=S_A+S_B+2K_{AB}.
\]

For a third block,

\[
K_{A\cup B,C}=K_{AC}+K_{BC}.
\]

These identities make every nested merge equal to the direct quadratic form

\[
\nu_N=\frac1N\mathbf1^T\Sigma\mathbf1.
\]

The exact checker verifies 33 rational symmetric covariance matrices, 71,142
ordered binary bracketings through eleven occurrences, and 495 labelled
cross-covariance transport identities.

Therefore correlated Gaussian Wick defects are natural when the full labelled
covariance is retained. A variance-only projection is insufficient, as already
seen in Entry 1652.

