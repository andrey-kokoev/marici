# 1669 — Full Covariance Restores Correlated Gaussian Cut Descent

## Correlated falsifier

Entry 1668 proves naturality of the scalar-cubic Wick Cut defect for independent
Gaussian blocks. Admit arbitrary cross-covariance and test whether nested
cardinality-weighted pushforwards remain tree-independent.

For a labelled block \(A\), define

\[
S_A=\sum_{i,j\in A}\Sigma_{ij},
\qquad
\nu_A=\frac{S_A}{|A|}.
\]

For disjoint blocks \(A,B\), define

\[
K_{AB}=\sum_{i\in A,j\in B}\Sigma_{ij}.
\]

Then

\[
S_{A\cup B}=S_A+S_B+2K_{AB}
\]

and

\[
K_{A\cup B,C}=K_{AC}+K_{BC}.
\]

Thus every merger tree evaluates to

\[
\nu_N=\frac1N\mathbf1^T\Sigma\mathbf1.
\]

The exact rational checker verifies:

\[
33\text{ symmetric covariance matrices},
\qquad
71{,}142\text{ ordered binary bracketings},
\qquad
495\text{ cross-covariance updates},
\]

through eleven labelled internal occurrences.

## Narrow result

\[
\boxed{
\text{full labelled covariance restores strict correlated Gaussian Cut descent.}
}
\]

The missing \(2\kappa^2\)-type contribution in a variance-only treatment is
not a new carrier incidence. It is information discarded from the Gaussian
coefficient object. Once the full covariance packet is retained, conditional
and cardinality-weighted mergers are associative.

This does not cover non-Gaussian cumulants, singular covariance matrices, or
support created by conditioning on a zero-variance block.

## Durable artifacts

- `research/benincasa/checkers/full_covariance_cut_descent.rs`
- `research/benincasa/results/full-covariance-cut-descent.json`
- `research/benincasa/full-covariance-cut-descent.md`

## Next falsifier

Approach a singular covariance stratum where one conditioned block has
vanishing determinant. Compute the Schur-complement/Rees limit before
specialization and determine whether the correlated Cut develops a canonical
supported coefficient class or requires a genuinely new carrier stratum.
