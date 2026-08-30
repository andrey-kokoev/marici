# Thinned count-tower calibration (WP337)

## Detector deletion sectors

Let each physical domain be detected independently with efficiency (eta). If
(m_j) is the source factorial-count moment and (widetilde m_j) the detected
moment, binomial thinning gives

\[
\widetilde m_j=\eta^j m_j.
\]

Composed with the WP336 binomial zeta transform, the seven-dimensional response
has determinant

\[
\eta^{0+1+\cdots+6}=\eta^{21}.
\]

Thus a calibrated nonzero efficiency preserves exact faithfulness of the full
count tower. At zero efficiency only the normalization channel remains.

## Uncalibrated hostile pair

An independent source Bernoulli probability (1/2) observed at efficiency
(1/2) gives the same detected Bernoulli probability as source probability
(1/4) observed at unit efficiency. Consequently the two packets have the
same complete detected count law through every order despite different source
laws and detector models.

Raw detected moments therefore contain background deletion sectors. The source
count law must first be typed through an independently derived efficiency-normal
channel; efficiency cannot be fitted from the desired reconstructed law.

## Instrument gate

Physical admission requires source-traceable efficiency calibration,
uncertainty and drift bounds, and tests excluding occupancy-dependent or
correlated missed detections.

Run `uv run --with sympy python
research/flavor/checkers/wp337_thinned_count_tower_calibration.py` to regenerate
the exact thinning audit.
