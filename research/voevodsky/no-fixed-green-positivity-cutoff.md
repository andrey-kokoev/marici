# No fixed local cutoff certifies finite Green positivity

## Question

Can any fixed bound on subsystem size certify positivity of arbitrary finite Green amalgamations?

## Bold conjecture under test

There exists an integer \(k\) such that positivity of every principal Green block of size at most \(k\) implies positivity of the full finite Green form.

## Falsifier family

For each \(k\ge2\), take \(k+1\) normalized one-dimensional sectors with constant off-diagonal pairing

\[
r_k=-\frac{2k-1}{2k(k-1)}.
\]

This lies strictly between the two thresholds

\[
-\frac1{k-1}<r_k<-\frac1k.
\]

An \(m\times m\) equicorrelation block has eigenvalues

\[
1-r_k
\]

with multiplicity \(m-1\), and

\[
1+(m-1)r_k
\]

on the collective direction. For every \(m\le k\), both are positive. At \(m=k+1\), the collective eigenvalue is negative.

Hence every principal subsystem admitted by the proposed cutoff passes, while the next-size joint form fails.

## Exact residual

The obstruction is a collective mode supported on all \(k+1\) sectors. Every proper subsystem of size at most \(k\) misses enough negative correlation to remain positive.

## Strongest test

The exact-rational checker verifies the construction for cutoffs \(2\) through \(12\), including positive cutoff-size determinants and negative next-size determinants. The displayed inequalities prove the family for every \(k\ge2\).

## Disposition

The fixed-cutoff conjecture is rejected. Finite Green positivity requires one of:

- the full joint Gram certificate at the actual sector count;
- a source-derived structural theorem implying positivity uniformly, such as a valid Cholesky, Markov, diagonal-dominance, or completely positive kernel construction.

Local tests remain useful falsifiers but cannot be promoted to a universal certificate without such a theorem.

## Verification

- `research/voevodsky/checkers/check_no_fixed_green_positivity_cutoff.py`
- `research/voevodsky/results/no_fixed_green_positivity_cutoff.json`
- `research/voevodsky/falsify-two-truncated-green-descent.md`
