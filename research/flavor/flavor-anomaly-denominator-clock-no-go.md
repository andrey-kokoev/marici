# Anomaly-denominator clock no-go: WP1101

## Question

Can WP1070's denominator-four anomaly coset select the mass clock?

## Exact comparison

The shifted Chern–Simons residue has common denominator \(4\). The mass clock
has the orbit

\[
\frac BA=6n^2.
\]

For \(n=-2,-1,0,1,2\),

\[
6n^2=24,6,0,6,24.
\]

The denominator \(4\) is not one of these values and no map from the quarter
residues to \(n\) is supplied. The same WP1070 coset remains compatible with
all five displayed integer lifts.

## Orientation gate

Since

\[
6(-n)^2=6n^2,
\]

the clock formula does not select \(\sigma\).

## Classification

Negative gate. Anomaly denominator four is neither the clock coefficient six
nor a lift selector. The remaining gate is a source-derived map from boundary
data to integer \(n\), sign \(\sigma\), and the unit orbit.

Checker: `research/flavor/checkers/wp1101_anomaly_denominator_clock_no_go.py`

Result: `results/wp1101_anomaly_denominator_clock_no_go.json`
