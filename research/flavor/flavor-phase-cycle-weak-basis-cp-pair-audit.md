# Phase-Cycle Weak-Basis Descent and CP-Pair Audit

## Question

What is the smallest interaction structure that carries a physical portal
orientation, and can a CP-symmetric source select its sign?

## Rephasing cycle is not enough

Four Yukawa entries (y_{ij}) with two left and two right species have the
plaquette product

\[
P=y_{11}y_{22}y_{12}^*y_{21}^*.
\]

Its phase survives every diagonal field rephasing. The four-by-five phase
charge matrix has rank three, and the left-kernel generator is
((1,-1,-1,1)).

This still does not define a physical flavor orientation. For

\[
Y=\begin{pmatrix}1&1\\1&i\end{pmatrix},
\qquad
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]

the weak-basis transformation (Y\mapsto UY) preserves (Y^\dagger Y) but
changes (P) from (i) to zero. The plaquette descends through the diagonal
rephasing groupoid and fails descent through the full weak-basis groupoid. It
is another presentation-chart phase, not a faithful physical16 coordinate.

## First physical orientation

A weak-basis-invariant CP orientation requires two noncommuting Hermitian
flavor operators with three nondegenerate generations. For

\[
H_u=\operatorname{diag}(1,2,3),
\qquad
H_d=V\operatorname{diag}(4,5,7)V^\dagger,
\]

with the unitary three-point Fourier matrix (V), the exact invariant

\[
J_{\rm phys}=\operatorname{Im}\det[H_u,H_d]
=\frac{4\sqrt3}{3}
\]

is unchanged by simultaneous weak-basis conjugation. Complex conjugation
reverses its sign. This is the correct type of orientation coordinate for the
faithful quotient.

## CP-pair obstruction

A source with real CP-even coefficients can depend on a physical phase through
even combinations. The exact example

\[
V(\Phi)=-\cos\Phi+\cos2\Phi
\]

has nontrivial minima satisfying (cos\Phi=1/4), with curvature (15/4).
It selects the phase magnitude but leaves two exactly degenerate minima
(Phi=\pm\arccos(1/4)). CP-symmetric RG preserves the paired basins.

Adding (-\kappa\sin\Phi) lifts the pair, but (kappa) is a new CP-odd source
coordinate. Unless its sign and normalization arise from the same admitted
source, this merely moves the portal-sign tuning upstream. A reference port
would instead define a relational experiment over the stabilizer groupoid.

## Threshold and instrument gates

Even a selected nonzero (J_{\rm phys}) fixes neither relevant scalar masses
nor the symmetry-breaking vacuum. It also does not construct a physical16
instrument. A Jarlskog-type invariant is a mathematically faithful
distinguishing functional; its experimental readout still requires a declared
family of CP-odd amplitudes and calibrated detector asymmetries.

## Classification

- Yukawa plaquette: texture-preserving phase rigidifier only.
- Jarlskog-type invariant: faithful physical orientation coordinate.
- CP-even potential: magnitude selector and presentation-independent sign
  pairer.
- CP-odd term: possible sign selector only after its own source authority.
- Threshold and physical readout: unselected.

## Smallest exact falsifiers

- Descent: (P(Y)=i) while (P(UY)=0), with (Y^\dagger Y) unchanged.
- Sign: the two minima (pm\arccos(1/4)) have identical CP-even energy and
  opposite physical orientation.
- Instrument: the invariant is unchanged while mass and detector-calibration
  coordinates vary independently.

## Disposition

The required source principle must be spontaneous or explicit CP-orientation
selection on a faithful weak-basis invariant, not selection of a texture loop
phase. Spontaneous CP breaking alone leaves a mirror pair. A complete source
must make one orientation dynamically unavoidable through a source-derived
CP-odd datum whose own sign is fixed, then place that invariant in a controlled
irrelevant RG direction and co-select the massive vacuum and detector
instrument.

Verification:

- checker: research/flavor/checkers/wp806_phase_cycle_weak_basis_cp_pair_audit.py
- generated result: research/flavor/results/wp806_phase_cycle_weak_basis_cp_pair_audit.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp806_phase_cycle_weak_basis_cp_pair_audit.py
