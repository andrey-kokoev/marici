# The inter-component current is not an ordinary delayed column

The branchwise \(q\to q+2\) lift has the exact defect

\[
K_{g,a,q}=-2J_{g,a}^{(-)}+2J_{g,a}^{(+)}.
\]

A possible sewing mechanism would express \(K_{g,a,q}\) as a linear
combination of ordinary columns in the target component \(q+2\). Then the
raising operation could be corrected internally, without adding a new output
port.

Exact rational span tests give the opposite bounded result.

- At the same cutoff, none of 1,400 defect packets belongs to the target
  column image.
- With the target cutoff expanded independently through \(K=12\), none of
  280 tested defect packets ever enters the image.
- The smallest failure is already \((g,k,q,a)=(2,2,1,0)\).

The second test matters: it rejects the interpretation that the missing
current is merely an upper-boundary truncation artifact that becomes an
ordinary column after more pole depths are admitted.

## Present strength

The finite-difference formula for the current is exact for arbitrary
parameters. Nonmembership in the ordinary target image is currently a bounded
exact census, not an unbounded cokernel theorem.

The emerging typed factorization is

\[
\text{branch-split source}
\xrightarrow{T_{q,q+2}}
\text{branch-split target plus current port}
\longrightarrow
\text{magnetic readout}.
\]

Forgetting the current port prevents the first square from commuting. Enlarging
the old pole-depth cutoff does not repair the tested failures.

The next theorem target is a symbolic left-cokernel functional
\(\lambda_{g,q}\) such that

\[
\lambda_{g,q}M_g=0
\]

on all ordinary target columns, while

\[
\lambda_{g,q}(K_{g,a,q})\ne0.
\]

Such a functional would upgrade the bounded result to an unbounded theorem and
identify the current port as a genuine new observation coordinate.

Replay with: python research/strominger/checkers/magnetic_current_port_sewing_checks.py
