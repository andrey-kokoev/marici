# The order-four Hausdorff corner is strictly positive

Degree-nine interval composition gives

\[
 A_8\approx1.95119101128753\,10^{-21},\qquad
 A_9\approx9.74950465781042\,10^{-24}.
\]

It includes eta and gamma data through order ten, the Bernoulli cancellation
`-L^10/47900160`, `(2s-1)^(-1)`, and Catalan inversion through `h^9`.

The certified `5x5` determinant intervals are

\[
\begin{aligned}
\det H^{(4)}&\in[1.92200864461860,1.92200864461957]10^{-67},\\
\det H_u^{(4)}&\in[7.6781851909456,7.6781967188311]10^{-83},\\
\det H_{4-u}^{(4)}&\in[1.96361847175934,1.96361847176124]10^{-64}.
\end{aligned}
\]

The lower determinant remains smallest. Its relative interval width is about
`1.5e-6`, improved by the tighter eta tail. Adaptive analytic precision thus
controls the earlier conditioning pressure.

## Scope

Four finite corners pass without zero locations. This does not establish the
infinite hierarchy, limiting measure, or RH.

## Durable verification

- Checker: `checkers/quarter_point_order_four_interval.py`
- Result: `results/quarter-point-order-four-interval.json`
- Eta input: `results/eta-order-ten-decimal-interval.json`
