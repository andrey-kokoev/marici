# Scaled exchange normalization obstruction (WP363)

## Bounded hostile test

WP362 used the unit swap between \(x=J^2\) and \(y=Q/M^2\). Test the most
general positive scaled involution

\[
P_s=
\begin{pmatrix}
0&s\\
s^{-1}&0
\end{pmatrix},
\qquad s>0.
\]

It obeys \(P_s^2=I\) for every \(s\), so involutivity alone does not calibrate
the relative port normalization.

For the WP362 portal matrix

\[
K_\alpha=
\begin{pmatrix}
1&-\alpha\\
-\alpha&\alpha^2
\end{pmatrix},
\]

the exact Ward residual is

\[
P_s^T K_\alpha P_s-K_\alpha
=
\begin{pmatrix}
\alpha^2/s^2-1&0\\
0&s^2-\alpha^2
\end{pmatrix}.
\]

On the positive domain, Ward invariance gives \(\alpha=s\), not
\(\alpha=1\). The unit result in WP362 is therefore conditional on a unit
relative port calibration.

## Missing positive pairing

A source-defined Euclidean pairing on the two-port doublet would additionally
require

\[
P_s^T P_s=I.
\]

Positivity then forces \(s=1\), and only with that extra pairing does the Ward
identity fix \(\alpha=1\). The pairing is new source structure: it cannot be
inferred from the desired equality of the two readouts.

If \(s\) is obtained by detector calibration, the experiment can identify
\(\alpha=s\), but it has measured the relative normalization rather than
predicted it. If a microscopic common multiplet derives the pairing before
flavor readout, unit normalization becomes a genuine conditional source
prediction.

## Disposition

WP363 qualifies WP362. A cross-sector involution by itself is not sufficient
to remove matching authority. The operation remains a relational experiment
over a changed stabilizer groupoid, now indexed by the calibration \(s\).
Only a source-defined positive pairing collapses that family to the unit swap.

The smallest exact falsifier is that \(P_2^2=I\) while it selects
\(\alpha=2\), not 1. The remaining physical-instrument gate is a common
source-derived positive Gram metric on the two ports, or an explicit admission
that detector calibration supplies \(s\) and therefore no numerical selector
claim is made.

Run `uv run --with sympy python
research/flavor/checkers/wp363_scaled_exchange_normalization_obstruction.py`
to regenerate the exact result.
