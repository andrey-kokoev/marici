# 2824 — Equal Koszul Rank Does Not Determine Occurrence Support

## Hostile pair

Consider the two source-labelled three-section packets

\[
S_V=(q_{g1},q_{g2},q_{g3})
\]

and

\[
S_C=(q_{g23},q_{g31},q_{g12}).
\]

Both have:

- three marked generators;
- all-soft incidence rank two;
- incidence nullity one;
- primitive kernel coordinates \((-1,-1,1)\).

Abstract Koszul rank data therefore identifies them.

## Labelled affine support

For the vertex packet,

\[
q_{g3}-q_{g2}-q_{g1}=x+y+3z.
\]

For the complementary packet,

\[
q_{g12}-q_{g31}-q_{g23}=2(x+y).
\]

After primitive normalization, their concurrency supports are respectively

\[
x+y+3z=0
\]

and

\[
x+y=0.
\]

Thus equal abstract rank, nullity, and kernel coordinates do not determine where the relation is supported. The occurrence-labelled affine incidence packet does.

## Interpretation

This is the first explicit discriminator between the Carrier account and the bare rank-counting rival:

\[
\text{unlabelled Koszul data}
\longmapsto
\text{one abstract relation},
\]

whereas

\[
\text{occurrence-labelled affine data}
\longmapsto
\text{a relation with a definite support divisor}.
\]

The result does not yet establish different physical readouts. It establishes the prior typed distinction required for such a test: the two relation lines occupy different supported objects before integration.

## Next falsifier

Compute restriction/Gysin transport for these two equal-rank relation lines. If their distinct support divisors produce distinct naturality or costalk behavior, the Carrier explanation gains predictive content beyond rank. If all supported transport becomes canonically equivalent after the admissible comparison calculus, occurrence labels were redundant in this example.

## Durable artifacts

- `research/benincasa/check_equal_rank_occurrence_support_discriminator.py`
- `research/benincasa/equal-rank-occurrence-support-discriminator.json`
