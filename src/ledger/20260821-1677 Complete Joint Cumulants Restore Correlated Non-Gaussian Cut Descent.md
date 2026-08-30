# 1677 — Complete Joint Cumulants Restore Correlated Non-Gaussian Cut Descent

## Correlated non-Gaussian falsifier

Entry 1676 proves normalized cumulant-species descent for independent blocks.
Admit correlations and test whether partition incidence creates a new
coherence class.

At order (r), the complete joint cumulant tensor has one labelled component
for every ordered occurrence tuple. Splitting occurrences into blocks (A,B)
partitions these components into the (2^r) slot patterns

\[
\epsilon\in\{A,B\}^r.
\]

Their cardinalities obey

\[
\boxed{
(|A|+|B|)^r
=
\sum_{\epsilon\in\{A,B\}^r}
|A|^{\#A(\epsilon)}|B|^{\#B(\epsilon)}.
}
\]

This is a disjoint labelled partition of the full tensor. Nested merger trees
only regroup the same ordered tuples, so they cannot alter the final joint
cumulant.

By contrast, retaining only the two pure sectors gives

\[
|A|^r+|B|^r<( |A|+|B|)^r
\]

for nonempty blocks and (r>1). Mixed cumulants are necessary coefficient
data.

The exact checker verifies:

\[
23{,}713\text{ ordered binary trees},
\]

\[
1{,}590{,}673\text{ internal node/order audits},
\]

and

\[
115{,}437{,}412\text{ labelled mixed-slot sectors}
\]

through eleven occurrences and cumulant order eight.

## Narrow result

\[
\boxed{
\text{the complete labelled joint cumulant tensor restores correlated non-Gaussian Cut descent.}
}

Partition incidence is already supplied by labelled occurrence tuples and set
decomposition. No new carrier cell or higher associator is required. The
failure of pure block cumulants is information loss in the coefficient object.

This result is algebraic. It does not establish positivity of an arbitrary
truncated cumulant packet or convergence of the infinite moment problem.

## Durable artifacts

- `research/benincasa/checkers/joint_cumulant_nested_merge.rs`
- `research/benincasa/results/joint-cumulant-nested-merge.json`
- `research/benincasa/joint-cumulant-nested-merge.md`

## Next falsifier

Test positivity/realizability. Determine whether finite truncations of the
joint cumulant species define positive moment functionals after
cardinality-weighted Cut descent, or whether positivity necessarily lives on
the complete infinite moment object of Entry 1648.
