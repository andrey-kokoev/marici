# Quarter seven-halves log correction comes from Stirling and shift degree

## Problem

Exact pivot fits selected a ratio-independent coefficient \(-7/2\) for \((\log n)/n\), but its source was unidentified.

## Bold conjecture

The coefficient is forced by the exact leading pivot symbol

\[
d_n(t)\sim4^{n-1}(n-1)!\,t^{3(n-1)}
\]

in the large-shift boundary.

## Named rivals

The rivals are a fitted artifact, a ratio-dependent coefficient, and a contribution coming only from the factorial or only from the shift power.

## Risky consequences

At \(t=\kappa n\), Stirling expansion must split the logarithmic coefficient into

\[
-rac12-3=-rac72,
\]

independently of \(\kappa\).

## Strongest falsification attempt

The factorial contributes \(-\tfrac12\log n\), while \(t^{3(n-1)}\) contributes \(-3\log n\). Numerical Stirling residuals decrease by a factor of two under each degree doubling and are below \(1.05\times10^{-4}\) at degree eight hundred for four ratios. Omitting the factorial half fails exactly. All five gates passed.

## Disposition

Prove the coefficient \(-7/2\) at the large-shift boundary. Its constancy at finite \(\kappa\) is supported by exact-pivot fits but still needs next-order transport. The next leaf is `quarter-pivot-log-correction-transport`: derive whether the next-order pivot balance forces the coefficient to be constant in \(\kappa\).

## Claim boundary

The derivation uses the leading-symbol boundary. It does not by itself prove uniform transport of \(-7/2\) across finite simultaneous-scaling ratios.
