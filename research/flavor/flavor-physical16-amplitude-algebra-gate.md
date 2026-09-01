# Physical16 amplitude algebra gate: WP1119

## Question

What minimal stochastic amplitude algebra maps the six branch weights to the
six physical16 events?

## Exact equation

Let

\[
q=\frac1{23}(6,8,1,4,2,2),\qquad p=\Bigl(\frac14\Bigr)^6,\qquad G=\frac32.
\]

If \(K\) is a column-stochastic event map and \(p=G\,Kq\), then

\[
Kq=\Bigl(\frac16\Bigr)^6.
\]

The complete-mixing matrix \(K=J_6/6\), all of whose entries are \(1/6\), is
the minimal exact solution: it is column-stochastic, rank one, and satisfies

\[
Kq=\Bigl(\frac16\Bigr)^6,\qquad \frac32Kq=\Bigl(\frac14\Bigr)^6.
\]

## Source gate

This algebra erases branch information: all six rows are identical. It has
zero source-derived coupling entries and is therefore a target-compatible
hostile, not a production law. The remaining route is a physical
complete-mixing process or a nonuniform source matrix satisfying the same
equation.

## Classification

Conditional gate. WP1119 derives the required amplitude algebra but does not
construct source dynamics.

Checker: `research/flavor/checkers/wp1119_physical16_amplitude_algebra_gate.py`

Result: `results/wp1119_physical16_amplitude_algebra_gate.json`
