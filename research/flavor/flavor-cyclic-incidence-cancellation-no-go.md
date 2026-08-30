# Fully cyclic portal incidence still permits exact CP cancellation: WP1022

## Question

Do fixed portal norms and nonzero incidence on every generation edge force a
nonzero physical CP-transmission invariant?

## Admitted source packet

Retain the WP90 singlet and portal vectors,

\[
z=4/5+3i/5,qquad a=(1,2,3)^T,qquad b=(2,1,1),
\]

so that (|a|^2=14) and (|b|^2=6) are fixed. Deform only one real
background entry:

\[
Y_0=\operatorname{diag}(1,2,4)-\frac{10}{381}E_{12}.
\]

## Exact cyclic hostile case

For (c=Y_0b^T), every component of the oriented bivector cycle is nonzero:

\[
(q_{12},q_{23},q_{31})
=\left(-\frac{742}{381},2,\frac{244}{127}\right).
\]

Every Gram-cycle edge
((H_d)_{12},(H_d)_{23},(H_d)_{31}) is also nonzero. The up and down spectra
are nondegenerate and (Y_d) has full rank.

Nevertheless, the exact cubic terms cancel:

\[
T=\operatorname{Im}((H_d)_{12}(H_d)_{23}(H_d)_{31})=0.
\]

Thus the commutator has rank two and zero determinant. Restoring the single
background entry to zero gives the WP90 value (1152i), so this is a genuine
cancellation inside the same cyclic portal architecture.

## Consequence

Three-generation support, fixed norms, and nonzero oriented bivector
components are still presentation constraints. They remove disconnected and
scale-free failures but do not select the physical sign or magnitude of (T).

The signed Jarlskog/CKM instrument detects the cancellation. It does not
forbid it. All 1,210 fitted sheets have nonzero (J), so the exact hostile
portal remains outside the fitted class.

## Smallest exact falsifier

The single rational deformation (Y_{0,12}=-10/381) is sufficient. It changes
no field, charge, portal rank, fixed vector norm, or cycle support, yet moves
the physical readout from (det[H_u,H_d]=1152i) to zero.

## Claim boundary

This closes fixed norms plus nonzero cyclic incidence. It does not exclude a
source law that directly fixes a weak-basis-invariant oriented volume or
positive (T)-margin. Such a law would be additional dynamics or geometry,
not a consequence of incidence alone. No implicit time or causal meaning is
used.

## Disposition

Do not promote cyclic support to selector authority. The next candidate must
derive the oriented-volume equation itself, prove it descends without a
reference port, remain closed under allowed source perturbations, and survive
the full fitted ensemble with a calibrated instrument.

Verification: uv run --with sympy python
research/flavor/checkers/wp1022_cyclic_incidence_cancellation_no_go.py.
