# Blind spectrum of the first Jacobi compression

Numerically diagonalizing the source-derived `4x4` Jacobi compression gives
compact-coordinate nodes

\[
 0.0000823101,quad0.0008835281,quad0.0021521788,quad0.0049987250.
\]

Without supplying any zero locations, the inverse map

\[
 \gamma=\sqrt{u^{-1}-1/4}
\]

predicts ordinates

\[
 14.13510,quad21.54984,quad33.63891,quad110.22215.
\]

Only after this blind construction, comparison with the standard first
ordinate `14.134725...` shows an error about `3.7e-4` (relative error about
`2.6e-5`). This is striking evidence that the low-order source moments already
lock onto the bottom of the spectral support. The second prediction is much
coarser and the remaining nodes are not consecutive-zero approximations; a
four-node Gaussian quadrature must also represent the unresolved tail.

The correct interpretation is therefore not “the first four zeros recovered.”
It is: the first source-derived Jacobi compression makes a sharp blind
first-edge prediction and visibly loses resolution deeper in the spectrum.
Tracking convergence of this extremal node with matrix order is now a concrete
long-horizon test of the operator program.

## Scope

Diagonalization here uses ordinary binary arithmetic, not eigenvalue interval
bounds. The moments and Jacobi coefficients are certified, but these displayed
nodes are numerical diagnostics. This does not prove RH.

## Durable verification

- Checker: `checkers/quarter_point_jacobi_blind_spectrum.py`
- Result: `results/quarter-point-jacobi-blind-spectrum.json`
