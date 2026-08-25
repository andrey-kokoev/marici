# Sharp adversarial margin for minimum `D(S3)` scalar probes

Owner: `marici.Kitaev`

## Bounded question

How much deterministic readout error can the four minimum scalar probe
families tolerate before anyon labels cease to be uniquely recoverable?

Equip each complex probe coordinate with its usual modulus and a signature
vector with the `L_infinity` product metric.  This treats a complex twist or
Hopf-link amplitude as the one probe declared in the predecessor theorem.

## Exact result

Every one of the four minimum families

\[
(\theta,S_C,S_D),\ (\theta,S_C,S_E),\
(\theta,S_D,S_F),\ (\theta,S_E,S_F)
\]

has minimum pairwise signature distance exactly

\[
\delta=1/3.
\]

Consequently, if every measured coordinate differs from its ideal value by
strictly less than

\[
\delta/2=1/6,
\]

nearest-signature classification is unique.  This is a deterministic coding
radius, not a probability of success.

## Sharp boundary witness

For the selected family `(theta,S_D,S_F)`, sectors `A` and `D` are a
closest pair:

\[
A=(1,1/2,1/3),\qquad D=(1,1/2,0).
\]

Their midpoint

\[
(1,1/2,1/6)
\]

lies at distance exactly `1/6` from each.  Closed adversarial error balls
therefore meet at the boundary, proving the strict radius is sharp.  The
other three minimum families have the same distance, with closest pair
`A,D` or `B,D` according to reference choice.

## Exact complex metric

Twists are represented in `Q(omega)` with

\[
|a+b\omega|^2=a^2-ab+b^2.
\]

The checker therefore compares actual complex moduli, not formal symbol
inequality.  In this finite instance the closest pairs differ in a rational
Hopf-link coordinate, but all twist distances are still audited in the same
metric.

## Verification

`python -u research/kitaev/checkers/check_s3_scalar_probe_noise_margin.py`
passes six aggregate gates.  It evaluates all 28 label pairs for each of the
four minimum families, records every closest pair, and verifies the exact
boundary midpoint.  Fresh stdout matches the saved JSON after newline
normalization.

## Claim boundary

No stochastic noise distribution, sample complexity, confidence interval,
apparatus calibration, correlated-error model, or physical decoder is
derived.  Different coordinate weights, splitting complex amplitudes into
two experimental quadratures, or allowing adaptive/full-operator readout
changes the metric and its radius.  The result certifies only deterministic
robustness of the frozen ideal scalar codebook.

## Falsifiers

Any pair at distance below `1/3`, a minimum family with a different margin,
failure of unique nearest decoding below `1/6`, or nonintersection of the
displayed closed balls at `1/6` falsifies the packet.
