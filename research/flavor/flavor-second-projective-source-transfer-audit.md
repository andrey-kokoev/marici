# Existing source projectors do not yet transfer into the WP957 flavor slot: WP958

## Question

Does an already admitted Marici source constructor supply WP957's missing
second projective flavor tensor without importing readout-chosen coordinates?

## Nearest source-authorized constructors

The bounded filesystem search found two serious candidates.

First, WP877's sequential `SO(5)` breaking derives two ordered real
rank-one projectors from a stable source potential.  They act on the real
five-vector carrier and label the two singlets of a `3+1+1` decomposition.
No admitted arrow maps either singlet projector to a complex generation-space
ray.  Moreover, every operator formed with real coefficients from real
projectors is real symmetric.  Two such Grams have a real antisymmetric
three-dimensional commutator, whose determinant and cubic trace vanish.
Therefore this constructor cannot supply CP capability unless an additional
complex structure and a named carrier interface are sourced.

Second, WP859's Kirchhoff junction derives a complex rank-one projector and a
lossless complementary port.  Its carrier is a two-path relational experiment.
Embedding that two-dimensional algebra into three generations preserves a
common line; its commutators have rank at most two and zero cubic trace.  The
return phase belongs to the changed relational experiment and cannot be
reinterpreted as an absolute flavor phase.

## Exact hostile witnesses

For arbitrary real symmetric three-by-three matrices `A` and `D`, the
commutator `K=[A,D]` is real antisymmetric.  Exact symbolic calculation gives

\[
\det K=0,
\qquad
\operatorname{Tr}K^3=0.
\]

For the Kirchhoff bright projector at `z=i`, embedded as a two-by-two block,
and any second embedded two-path Hermitian operator, the third basis vector is
a common invariant line.  The exact commutator has rank at most two and zero
cubic trace.

## Classification

The programme already contains source-generated projectors, but not the
required arrow into the WP957 family module.  WP877 is source-authorized and
real but CP-blind; WP859 is complex and instrumented at source level but is a
two-path reference experiment.  Coordinate compatibility would not create a
legal transfer.

The missing constructor is now typed more narrowly:

\[
P_{\rm family}:\mathcal S_{\rm source}
\longrightarrow \operatorname{Proj}_1(\mathbb C^3),
\]

with a declared source carrier, complex structure, weak-basis covariance,
relational independence from the up tensor, completion stability, and a
calibrated flavor instrument.  No arrow is assigned physical time or
causality.

## Smallest falsifier

A proposed transfer fails if its image is confined to a real family form or a
common two-dimensional block: in either case the CP cubic is identically zero.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp958_second_projective_source_transfer_audit.py

Generated result: `research/flavor/results/wp958_second_projective_source_transfer_audit.json`.
