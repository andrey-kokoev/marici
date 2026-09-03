# Falsification of two-truncated Green descent

## Problem

Test whether every obstruction relevant to finite Green amalgamation is detected by pairwise and triple-overlap data, equivalently by a two-truncated Čech-style audit.

## Bold conjecture

If every pair and every triple of normalized Green sectors has a positive compatible Gram restriction, then the full finite Green amalgamation is positive.

## Named rivals

- positivity may first fail on a four-sector principal block;
- local positive completions may not admit a common global completion;
- the required Čech depth may grow with the number of sectors.

## Strongest falsification attempt

Take four normalized one-dimensional sectors with constant off-diagonal pairing

\[
r=-\frac25.
\]

Every pair has Gram determinant

\[
1-r^2=\frac{21}{25}>0.
\]

Every triple has equicorrelation Gram determinant

\[
(1-r)^2(1+2r)=\frac{49}{125}>0.
\]

Thus all restrictions involving at most three sectors are positive and mutually compatible: they are restrictions of the same declared pairings.

The full four-sector Gram determinant is

\[
(1-r)^3(1+3r)=-\frac{343}{625}<0.
\]

Equivalently, the all-ones direction has eigenvalue \(1+3r=-1/5\). The global form is indefinite despite every two-truncated restriction passing.

## Exact residual

The first failed object is the four-sector principal block. No pair or triple witnesses the negative collective mode.

## Disposition

The two-truncated detection conjecture is rejected for finite Green amalgamations. A fixed low Čech cutoff cannot certify arbitrary joint positivity. For \(n\) sectors, the operating certificate must include the full joint Gram operator or a source-derived structural theorem, such as a valid factorization, that implies its positivity at all sizes.

This does not imply that all simplicial levels must be enumerated when a theorem supplies a bounded criterion. It rejects an unsupported universal cutoff at degree two.

## Verification

- `research/voevodsky/checkers/check_two_truncated_green_descent.py`
- `research/voevodsky/results/two_truncated_green_descent.json`
- `research/voevodsky/certified-green-amalgamation-composition-audit.md`
