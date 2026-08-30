# Perfectly correlated preparations defeat flavor moment concentration: WP966

## Question

Does correct one-slot calibration suffice to make WP97's moment separator
executable over repeated preparations?

## Exact hostile preparation

Take the symmetric broken mixture

\[
(p_-,p_0,p_+)=\left(\frac12,0,\frac12\right),
\qquad m_1=0,\qquad m_2=1.
\]

For any positive integer N, draw one latent sign Z uniformly from {-1,+1} and
prepare every labelled sampling slot with X_k=Z. Each individual slot has the
correct marginal distribution. The joint preparation is exchangeable, but it
is not independent and supplies no reset.

The empirical moments are exactly

\[
\widehat m_1=Z,\qquad \widehat m_2=1
\]

for every N. Applying the WP97 inverse reports either a pure plus route or a
pure minus route. Its total-variation distance from the true symmetric broken
mixture is 1/2 with probability one. Increasing N does nothing.

By contrast, independent slots give

\[
\operatorname{Var}(\widehat m_1)=\frac1N.
\]

The hostile preserves every one-slot source and detector calibration while
destroying the concentration conclusion. Therefore independence/reset is a
separate physical preparation capability, not a consequence of the marginal
instrument or of contextual faithfulness.

## Classification

This is a non-selector instrument obstruction. WP97 remains algebraically
faithful and WP98 remains correct conditional on IID preparation. The first
nonfaithful arrow is the joint preparation map. The next legal instrument must
certify decorrelation or bound batch-common covariance in source-defined
sampling slots. Slot labels encode a joint experiment, not physical time or
causal order.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp966_domain_moment_perfect_correlation.py

Generated result:
research/flavor/results/wp966_domain_moment_perfect_correlation.json.
