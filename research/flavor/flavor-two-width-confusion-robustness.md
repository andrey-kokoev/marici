# Two-width confusion robustness: WP653

## Detector response

Model symmetric misclassification between WP652's two labelled channels by

\[
C(e)=
\begin{pmatrix}
1-e&e\\
e&1-e
\end{pmatrix}.
\]

The normalized log-width response becomes \(J_{\mathrm{det}}=2C(e)\). Its exact
determinants are

\[
\det J_{\mathrm{det}}=4(1-2e),
\qquad
\det(J_{\mathrm{det}}^\top J_{\mathrm{det}})=16(1-2e)^2.
\]

Thus detector confusion preserves magnitude identification exactly when
\(e\ne1/2\). At \(e=1/2\), both reconstructed ports are identical and the rank
collapses to one.

## Uncertainty-stable gate

For a calibration interval \(e\in[e_0-\delta_e,e_0+\delta_e]\), a sufficient
and exact separation condition is

\[
|1-2e_0|>2\delta_e.
\]

The smallest singular value is then bounded below by

\[
2(|1-2e_0|-2\delta_e)>0.
\]

At the exact illustrative benchmark \(e_0=1/10\), \(\delta_e=1/20\), this lower
bound is \(7/5\).

## Disposition

This is a conditional detector-robust identification theorem, not an admitted
experimental calibration. No detector-derived value of \(e\) or uncertainty
set is currently attached. Finite-width overlap, backgrounds, efficiencies,
and mass resolution remain to be incorporated.

The smallest exact falsifier is \(e=1/2\).

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp653_two_width_confusion_robustness.py
```

Generated result: `results/wp653_two_width_confusion_robustness.json`.
