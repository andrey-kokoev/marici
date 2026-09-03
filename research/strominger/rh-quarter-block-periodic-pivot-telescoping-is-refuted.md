# Quarter block-periodic pivot telescoping is refuted

## Problem

The renormalized pivot amplitude would be elementary if the quarter lattice made each residue class of

\[
\rho_j=rac{c_j}{1+2/j}
\]

a low-degree rational function of \(j\).

## Bold conjecture

For each residue \(r\) modulo four, \(\rho_j\) on \(j\equiv r\pmod4\) is a ratio of equal-degree polynomials of degree at most two.

## Named rivals

The rivals are a global Barnes constant with no termwise rational formula, a higher-degree residue-class formula, and a recurrence-defined factor sequence without finite rational closure.

## Risky consequences

For each residue and degree \(d=1,2\), the unique rational interpolant fitted to the first \(2d+1\) exact values must reproduce every later exact value in that residue class.

## Strongest falsification attempt

Exact determinant arithmetic produced \(\rho_j\) through \(j=25\). Eight interpolants were fitted, one for each residue and degree. Every holdout equality failed exactly. The residual is eight failed exact holdout tests out of eight; no floating comparison was used.

## Disposition

Reject the conjecture. Quarter-lattice block periodicity does not rescue degree-one or degree-two termwise telescoping. The global Barnes rival survives this test; the next executable leaf is `quarter-barnes-constant-shift-equation`.

## Claim boundary

The test does not exclude residue-wise rational formulas of degree at least three, unequal polynomial degrees, or non-rational block recurrences.
