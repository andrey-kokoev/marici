# Canonical path complexity is asymptotic to e times factorial

## Question

How rapidly does canonical route multiplicity grow while every canonical relative attachment remains contractible?

## Claim boundary

The count concerns typed maximal directed paths inside the distinct-shell canonical attachment package. It is not a count of homology classes, physical records, or globally distinct trajectories after coherence quotienting.

## Exact count

Let

\[
A_n(x)=(1+x)^{n-2}(1+x+x^2)
\]

be the canonical attachment polynomial. Each \(r\)-cell contributes \(r!\) maximal direction orderings, so

\[
R_n=\sum_{r=1}^{n}r!\,[x^r]A_n(x).
\]

Writing \(N=n-2\) and changing variables from cell degree to complementary subset size gives

\[
\frac{R_n}{N!}
=
\sum_{j=0}^{N-1}\frac1{j!}
+
\sum_{j=0}^{N}\frac{N-j+1}{j!}
+
\sum_{j=0}^{N}\frac{(N-j+2)(N-j+1)}{j!}.
\]

Replacing the truncated exponential sums by their limits yields

\[
R_n\sim eN!(N^2+2N+2).
\]

Since

\[
\frac{N^2+2N+2}{n(n-1)}
=
\frac{n^2-2n+2}{n(n-1)}
\longrightarrow1,
\]

we obtain

\[
R_n\sim e\,n!.
\]

## Interpretation

The number of typed routes grows factorially, while the direction-one Morse matching contracts the entire relative package. Computational route multiplicity and homotopical complexity therefore diverge sharply: factorially many presentations can encode no persistent obstruction.

## Strongest falsification attempt

For dimensions 3 through 50, compute \(R_n\) independently from polynomial coefficients and from the complementary-index closed sum. Require exact integer agreement. Compare \(R_n/n!\) with \(e\) at increasing dimensions and require the error to decrease over the final tested range. Retain exact values for dimensions 3 through 15.

## Computed result

The coefficient sum and complementary-index formula agree exactly for every dimension from 3 through 50. The sequence begins

\[
12,53,276,1695,12068,97857,890508,8987291.
\]

The normalized ratio \(R_n/n!\) rises from approximately 2.47666 at \(n=10\) to 2.66503 at \(n=50\), while its absolute error from \(e\) falls from approximately 0.24163 to 0.05326 over that range.

## Disposition

The factorial-growth prediction survives, and the exact derivation proves \(R_n\sim e n!\). Combined with the integral Morse contraction, this establishes an unbounded separation between route-presentation complexity and relative homological complexity: the former is asymptotically factorial while the latter remains zero.
