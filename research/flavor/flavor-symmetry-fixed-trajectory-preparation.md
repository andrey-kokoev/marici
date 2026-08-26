# Symmetry-fixed trajectory preparation (WP272)

## Candidate preparation law

Could a source symmetry force WP271's measure-zero fixed trajectory? Consider
the smallest equivariant flow

\[
\frac{dz}{dt}=-z
\]

with the symmetry \(z\mapsto-z\). Its trajectories are

\[
z_A(t)=Ae^{-t}.
\]

The reflected trajectory is also a solution, and every amplitude reaches the
same UV fixed point.

## Quotient does not kill the amplitude

The faithful symmetry quotient is represented by

\[
q(t)=z_A(t)^2=A^2e^{-2t}.
\]

It identifies \(A\) with \(-A\), but not amplitudes of different magnitude.
At the finite matching scale, \(A=1\) and \(A=2\) give quotient records one and
four. The symmetry quotient removes sign redundancy while leaving a continuous
trajectory coordinate; this is not texture-presentation rigidification.

Group averaging does not prepare the fixed state. Averaging the pair
\(z_A,-z_A\) gives zero mean, but its second moment remains
\(A^2e^{-2t}\), whereas the delta state on the fixed trajectory has zero second
moment. A symmetric ensemble is not the same object as a symmetry-fixed state.

## Classification

Source-law equivariance alone does not select the fixed trajectory and is not
a flavor texture rigidifier. The first
nonfaithful arrow is from symmetry of the dynamics to preparation of an
invariant state. Progress requires a unique unbroken symmetric vacuum,
dissipative preparation channel, boundary condition, or superselection rule
that removes \(|A|\), not merely its sign.

Run `uv run --with sympy python
research/flavor/checkers/wp272_symmetry_fixed_trajectory_preparation.py` for
the exact flow, quotient, hostile amplitudes, and orbit-average moment test.
