# The common entropy interface is projective-positive, not merely stochastic

## Candidate and obstruction

The scattering and flavor sectors both produce finite normalized probability
states, suggesting the category of finite stochastic maps. That category is
too narrow. A biased accepted-event effect acts first by a positive linear
map \(K\) on an unnormalized cone and then by

\[
[p]\longmapsto [Kp]
=\frac{Kp}{\mathbf 1^TKp}.
\]

Unless \(\mathbf 1^TKp\) is state independent, this normalized action is not
affine. Thus it is not a stochastic map on the normalized simplex.

## Refined interface

The common pre-normalized object is a finite positive cone with:

- a distinguished positive trace;
- nonzero positive rays as physical normalized states;
- positive linear maps as readout/support constructors;
- projectivization only after the accepted nonzero support is known.

For composable positive maps \(K,L\),

\[
\mathbb P(L)\mathbb P(K)[p]=\mathbb P(LK)[p].
\]

Normalization therefore preserves composition projectively even though it
does not preserve convex mixtures. Flavor permutations and bistochastic
overlap maps form a special trace-preserving subcategory. Bell support filters
occupy the larger projective-positive category.

## Entropy typing

Shannon entropy is a valuation on the normalized probability object produced
at the end; it is not a functor monotone under every positive constructor.
Its grouping law belongs to deterministic partitions with their conditional
fiber states. Data processing, postselection, and bistochastic mixing are
different morphism classes and must not be conflated.

Hence the cross-sector refinement is

\[
\boxed{
\text{sector coefficient object}
\to
\text{finite positive traced cone}
\xrightarrow{\text{support/constructor}}
\text{nonzero positive ray}
\xrightarrow{\text{normalization}}
\text{probability state}
\xrightarrow{H}
\mathbb R_{\ge0}.}
\]

This is a stronger and more falsifiable claim than saying that every sector
eventually supplies probabilities: it predicts a shared pre-normalization
calculus and explicitly locates normalization as a projective, generally
nonlinear boundary.
