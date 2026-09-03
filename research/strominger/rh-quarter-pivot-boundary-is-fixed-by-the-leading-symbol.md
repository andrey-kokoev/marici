# Quarter pivot boundary is fixed by the leading symbol

## Problem

The rate equation leaves a homogeneous constant \(C\) that direct degree-28 fits estimate with visible ratio-dependent bias.

## Bold conjecture

The fixed-degree leading symbol supplies the large-\(\kappa\) boundary and uniquely fixes \(C\).

## Named rivals

The rivals are direct finite-degree normalization, zero homogeneous constant, and a leading-symbol pattern that fails beyond the tested sizes.

## Risky consequences

If \(L_n\) is the leading coefficient of \(S_n(s+t)\), then the pivot-leading ratio must obey

\[
\frac{L_n}{L_{n-1}}=4^{n-1}(n-1)!,
\]

implying

\[
f(\kappa)\sim3\log\kappa+\log4-1.
\]

The homogeneous constant must then equal

\[
C=\int_0^\infty\frac{H(u)}{(u+2)^2}\,du.
\]

## Strongest falsification attempt

The leading-coefficient ratio is exact through \(n=8\) with zero residual. Endpoint-regularized quadrature gives \(C=0.46941664\). Direct finite-degree fits instead rise from \(0.43391\) to \(0.45459\) across the tested ratios, exposing a spread \(0.02068\) rather than a constant; that failed route was repaired as a finite-window-bias diagnostic. All leading-symbol gates passed.

## Disposition

Select \(C=0.46941664\) as the boundary-normalized value conditional on the crossover and rate ansatz. The next leaf is `quarter-pivot-rate-boundary-closed-form`: determine whether this integral reduces to logarithms of algebraic factors or a Barnes constant.

## Claim boundary

The leading-symbol identity is checked only through \(n=8\), and the integral value is numerical. Neither proves the uniform rate ansatz or the rational crossover.
