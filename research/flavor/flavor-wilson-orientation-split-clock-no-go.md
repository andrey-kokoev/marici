# Wilson orientation cannot jointly select split and clock: WP1113

## Question

Can an orientation-odd Wilson/flux boundary datum jointly select the WP1111
Green–Schwarz split and the mass-clock orientation?

## Exact separation

The Wilson phase is orientation-odd:

\[
\phi=\frac13\pmod{\mathbb Z}
\quad\mapsto\quad
-\phi=\frac23\pmod{\mathbb Z}.
\]

But the clock orbit is even:

\[
\frac BA=6n^2,
\qquad 6(-n)^2=6n^2.
\]

The split equations contain \(t\), not the Wilson sign:

\[
k_4=-\frac14-t,\qquad k_2=-t.
\]

There are zero admitted equations coupling the Wilson phase or flux sign to
\(t\). The phase distinguishes \(1/3\) from \(2/3\), but selects neither the
split nor \(n,\sigma\).

## Classification

Negative gate. Wilson/flux orientation cannot serve as the joint
orientation-odd boundary datum.

Checker: `research/flavor/checkers/wp1113_wilson_orientation_split_clock_no_go.py`

Result: `results/wp1113_wilson_orientation_split_clock_no_go.json`
