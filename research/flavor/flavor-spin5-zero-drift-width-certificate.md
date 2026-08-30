# Spin(5) zero-drift width certificate (WP901)

## Question

What does the corrected WP900 experiment conclude if all four cells have
exactly zero observed six-bin drift?

## Exact finite certificate

Use six bins, four-cell simultaneous coverage \(1-\alpha=0.95\), and the
diagnostic tolerance \(\varepsilon=0.01\). With equal selected counts per
cell, the corrected radius is

\[
r(n)=\sqrt{\frac{\log(2^8/0.05)}{2n}}.
\]

At zero empirical drift, admission requires \(2r(n)\leq0.01\). The exact
minimum integer is \(n=170819\) selected events in each of the four cells. At
this value, \(2r=0.00999997641831\), leaving margin
\(2.35817\times10^{-8}\). The four-cell failure-probability bound is
0.04999798594, below 0.05. One fewer selected event per cell fails the frozen
one-percent inequality.

The complete zero-drift design therefore requires 683276 selected simulated
events. Projecting only from the existing 140 GeV pilot acceptance
\(389/14688\) gives a diagnostic capacity estimate of 6449845 generated
events per cell, or 25799380 total. This projection is not acceptance authority
for either actual pole; WP895 requires generated and rejected counts in each
new cell.

## Disposition

Zero observed drift would certify source-width stability of the frozen six-bin
response at the declared tolerance and coverage. It would not identify
\(q_u,q_v\), prove collision-data power, validate backgrounds, or select a
flavor point. No such four-cell event samples currently exist in the admitted
workspace, so WP901 is an exact prospective certificate rather than an
observed experimental result.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp901_spin5_zero_drift_width_certificate.py
~~~
