# CP-odd orientation vacuum (WP281)

## Minimal source field

Introduce a real CP-odd field \(a\) with the CP-even source potential

\[
V(a)=\frac{\lambda}{4}(a^2-v^2)^2,
\qquad \lambda>0,
\qquad v>0.
\]

Its stationary points are \(0\) and \(\pm v\). The origin has curvature
\(-\lambda v^2\), while both nonzero vacua have curvature
\(2\lambda v^2>0\) and equal energy zero.

Coupling the orientation drift as

\[
A(a)=a\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]

gives full dynamic tower determinants \(-v\) and \(+v\) on the two vacua. The
field therefore repairs WP280's self-reading problem at the architectural
level: orientation is supplied by a dynamical source variable rather than a
measured Jarlskog value.

## Branch kernel

The CP-even action selects the unordered vacuum pair, not one signed branch.
The two vacua have identical energy and local curvature but generate opposite
drift orientations. Reading the sign afterward distinguishes the realized
branch; it does not explain its preparation.

The smallest local branch-lifting operator is a CP-odd bias \(-ha\). On the
unperturbed vacua it produces energy split \(-2hv\), explicitly introducing a
new authority-bearing CP-odd datum. A cosmological history, boundary condition,
or superselection mechanism could instead select a branch, but would define a
larger source experiment.

## Classification

WP281 supplies a conditional source-generated orientation magnitude with two
CP-conjugate branches. It is neither a unique signed selector nor a complete
preparation instrument. Progress requires branch selection plus independently
derived \(v\), kinetic normalization, flavor coupling, wall history, noise, and
stabilization.

Run `uv run --with sympy python
research/flavor/checkers/wp281_cp_odd_orientation_vacuum.py` for the exact
stationary points, curvatures, degeneracy, drift ranks, and bias split.
