# Quarter double-scaling crossover points to a minimal rational form

## Problem

The crossover function must interpolate between scaled-curvature coefficients \(1/4\) and \(3/2\) while retaining the source offset two.

## Bold conjecture

For

\[
G(\kappa)=\kappa^2(F(\kappa)-1),
\]

the minimal endpoint- and offset-constrained form is

\[
G(\kappa)=\frac{1+3\kappa}{2(\kappa+2)},
\qquad
F(\kappa)=1+rac{1+3\kappa}{2\kappa^2(\kappa+2)}.
\]

## Named rivals

The rivals are a quadratic interpolation with the same endpoints, a higher-degree rational function, and finite-degree extrapolation bias.

## Risky consequences

The formula must match all four previously fitted curvatures without fitting a free parameter, and its residual sum must beat the quadratic endpoint rival.

## Strongest falsification attempt

At \(\kappa=1/2,1,2,4\), the residuals are \(-0.02710,-0.01235,-0.00025,0.00637\). The maximum is below \(0.03\), and the candidate beats the quadratic rival. Solving each point for the equivalent free parameter gives values within \(0.07\) of \(1/2\). All five repaired gates passed.

## Disposition

Select the displayed rational function as the finite crossover candidate. The next leaf is `quarter-double-scaling-rational-proof`: derive it from the simultaneous leading-order pivot or equilibrium equation.

## Claim boundary

Four finite extrapolations do not prove the rational function. The source offset was used to choose the candidate, so agreement is not an independent derivation of that offset.
