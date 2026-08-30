# Entry 1615 — The Corrected Endpoint Location Complex Has a Positive Labelled Cut Pairing

## Claim

At the level of labelled vertex locations, the corrected source multiplicities
\((1,2,1)\) assemble canonically into a positive Cut pairing.

## Labelled construction

Let \(A_B\) and \(A_S\) denote the source-normalized bulk and initial-surface
production amplitudes.  Before identifying the mixed occurrences, the Cut
expansion is

\[
A_B\overline{A_B},
\quad
A_B\overline{A_S},
\quad
A_S\overline{A_B},
\quad
A_S\overline{A_S}.
\]

Cut conjugation exchanges the two middle terms.  Their pushforward gives the
location multiplicities

\[
(1,2,1).
\]

The complete labelled sum is

\[
\boxed{
|A_B+A_S|^2\ge0.
}
\]

The contour orientation and endpoint signs belong inside the complex number
\(A_S\); they do not alter the positive multiplicity census.

## Result

The first source-level combinatorial gate for Entry 1608 passes.  The
source-derived endpoint location complex—not the defective printed Eq. (19)
weights—has exactly the symmetric-square structure required by a Cut norm.

## Remaining gates

This does not yet prove the physical cosmological identity.  Still required:

1. source-normalized formulas for \(A_B,A_S\);
2. the physical two-particle phase-space measure;
3. the \(q/k\) occurrence trace;
4. equality with the second phase-space jet of the Dyson covariance.

## Artifacts

- `research/benincasa/marici-gm/src/bin/labelled_endpoint_cut_pairing.rs`
- `research/benincasa/results/labelled-endpoint-cut-pairing.json`

Allocator claim: `seqclaim-ddecc8773404ce0b37d67f44`.
