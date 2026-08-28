# Theta overdrive cannot be repaired by appending an input port

## Result

The earlier positive-colligation phase diagram correctly detects an overdriven region, but its proposed positive repair needs tightening. If the original source column is frozen, merely appending an independent lossless input channel cannot repair \(\rho>1\).

Let a positive continuous-time lossless realization obey

\[
C^*C=Q,\qquad B=-C^*D,\qquad D^*D=I.
\]

Keep the theta source as the first input column

\[
b=-f(1,0)^T.
\]

Writing \(d\) for the corresponding first column of \(D\), the balance law requires

\[
C^*d=-b,\qquad \lVert d\rVert=1.
\]

For every output enlargement satisfying \(C^*C=Q\), the least possible squared norm of a solution is

\[
\lVert d\rVert_{\min}^2=b^*Q^{-1}b
=\frac{|f|^2}{1-4r^2}
=\rho.
\]

Therefore \(\rho>1\) is already a contradiction on the original input column. Extra columns in \(D\) do not change that column's norm. The obstruction is columnwise and survives every finite positive output or input enlargement that preserves the original source normalization and the same state balance.

## Corrected phase interpretation

- For \(\rho<1\), output slack completes the forced column.
- For \(\rho=1\), no slack is needed.
- For \(\rho>1\), passive port appending is impossible.

The admissible repairs are stronger operations:

1. renormalize or coherently split the original source excitation before declaring its physical input unit;
2. couple an active reservoir that changes the state balance \(Q\), hence changes the generator rather than just adding a column;
3. change the positive state metric;
4. pass to an indefinite supply metric.

This separates a spectator reservoir from a dynamical reservoir. A spectator adds channels to an unchanged colligation. A dynamical reservoir changes the balance law. Only the latter can cross the overdrive boundary.

## Transfer to relative connections

Strominger's invariant relative field \(B=A-A_C\) has exactly the required type distinction. A response-derived composite connection changes presentation but not capability. A genuinely independent relative field can alter the active connection and its curvature, thereby changing the balance itself. Its quantized zero-defect law supplies an experimental discriminator: a proposed active reservoir must change the measured balance while retaining the required puncture holonomy. If it only adds a dark unused port, it cannot repair theta overdrive.

## Falsifier

Operate at \(r=0\) and \(y=\log 2/(2\pi)\), where \(f=\sqrt2\) and \(\rho=2\). Any claimed positive lossless realization retaining the normalized theta source must exhibit one of the four balance-changing operations above. A design claiming repair solely by an appended unit input port is algebraically impossible.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_theta_extra_input_no_go.py
```
