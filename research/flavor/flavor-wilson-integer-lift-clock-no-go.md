# Wilson integer-lift clock no-go: WP1095

## Question

Can a conditional Wilson phase select the integer clock lift \(n\) or the sign
convention \(\sigma\)?

## Modulo-one gate

A Wilson phase measures an exponent modulo \(1\). The lifts

\[
\theta=\frac13,\qquad \theta+1=\frac43,\qquad \theta+2=\frac73
\]

all give the same phase class \(1/3\).

The corresponding clock values differ:

\[
\frac BA=6n^2:\qquad n=0,1,2\mapsto 0,6,24.
\]

Thus the phase class does not select the integral representative \(n\).

## Sign gate

The quadratic clock also gives

\[
6(-n)^2=6n^2,
\]

so \(B/A\) alone does not select \(\sigma\).

## Classification

Negative gate. A conditional Wilson constructor may fix a phase class, but not
its integral lift or clock orientation. The remaining gate is a source packet
selecting the integer flux lift \(n\), the unit orbit \(B/A=6n^2\), and the
sign convention \(\sigma\).

Checker: `research/flavor/checkers/wp1095_wilson_integer_lift_clock_no_go.py`

Result: `results/wp1095_wilson_integer_lift_clock_no_go.json`
