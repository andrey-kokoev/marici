# First-order bulk leakage is a projected nonlocal force

## Perturbed constrained lift

Let

\[
W_\varepsilon=K+\varepsilon G
\]

and minimize

\[
u^TW_\varepsilon u
\]

subject to fixed boundary data

\[
Au=d.
\]

The minimizer is

\[
u_\varepsilon
=W_\varepsilon^{-1}A^T
(AW_\varepsilon^{-1}A^T)^{-1}d.
\]

## Derivative formula

Define the Green-metric constraint projection

\[
P
=K^{-1}A^T(AK^{-1}A^T)^{-1}A.
\]

Differentiating at \(\varepsilon=0\) gives

\[
\dot u
=-(I-P)K^{-1}Gu_0.
\]

Thus the nonlocal metric produces the raw force

\[
K^{-1}Gu_0,
\]

while \(I-P\) removes the component that would alter the prescribed boundary data.

## Boundary invisibility

Because

\[
A(I-P)=0,
\]

one has

\[
A\dot u=0.
\]

First-order bulk leakage lies entirely in the two-moment kernel. It changes the interior explanation while preserving the boundary anomaly exactly.

## Interpretation

```text
nonlocal coupling G
-> acts on boundary lift u_0
-> Green precision K^-1 converts it to a state force
-> constraint projection removes boundary-visible part
-> interior kernel receives the leakage
```

This identifies the tangent direction by which exact boundary localization fails.

## Diagnostic use

If \(K\), \(A\), and \(u_0\) are known, the measured first-order interior profile determines the projected action

\[
(I-P)K^{-1}Gu_0.
\]

Multiple independent boundary targets \(d\) probe different columns of the unknown nonlocal coupling. Bulk leakage can therefore serve as tomography of deviations from the Markov metric.

## Verification

```text
python research/coherence/check_first_order_nonlocal_leakage_formula.py
```

The exact-rational checker verifies \(A\dot u=0\). Difference quotients converge linearly to the derived formula from \(\varepsilon=10^{-1}\) through \(10^{-6}\).

Artifacts:

- `check_first_order_nonlocal_leakage_formula.py`
- `first-order-nonlocal-leakage-formula.v1.json`
