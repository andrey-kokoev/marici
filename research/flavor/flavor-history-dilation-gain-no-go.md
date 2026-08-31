# History-dilation gain no-go: WP1093

## Question

Does conditional history dilation supply event reweighting or the gain law?

## Isometry gate

WP1087's conditional history dilation maps one cyclic ray into three history
slots. After normalization the slot weights are

\[
\left(\frac13,\frac13,\frac13\right),
\]

with total norm \(1\). The dilation is an isometry, so its gain is \(1\), not
the target \(3/2\).

## Production gate

The six localized soft branches retain dimensions

\[
(6,8,1,4,2,2)
\]

and distribution

\[
q=\frac1{23}(6,8,1,4,2,2),
\]

not the six event weights \((1/4)^6\).

The internal history dilation supplies zero history-to-soft reweighting rows
and zero branch-to-physical16 coupling rows. Three history slots cannot be
promoted to six event weights, and isometry cannot produce gain \(3/2\).

## Classification

Negative gate. Conditional history dilation can preserve cyclic history, but
it is norm-preserving and internal. It has no admitted production or descent
matrix.

The remaining gate is a source-derived production kernel with branch
reweighting, physical16 coupling rows, and gain \(3/2\).

Checker: `research/flavor/checkers/wp1093_history_dilation_gain_no_go.py`

Result: `results/wp1093_history_dilation_gain_no_go.json`
