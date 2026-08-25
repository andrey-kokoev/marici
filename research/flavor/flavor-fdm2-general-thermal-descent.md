# General thermal descent conditions for FDM-2 (WP95)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## What CP actually supplies

Let the source-derived finite-temperature effective potential be analytic and
CP even,

\[
V_{\rm eff}(x,y;T)=V_{\rm eff}(x,-y;T).
\]

Then `y=0` is stationary in the CP-odd direction, and every broken stationary
point `(x,y)` has a degenerate conjugate `(x,-y)`. These are pairing and
descent statements. They do not imply that a broken branch exists or that the
symmetric branch loses stability.

Define the minimized CP-even branch `x_0(T)` by
`partial_x V_eff(x,0;T)=0` and its transverse curvature

\[
\mu_y^2(T)=\partial_y^2V_{\rm eff}(x_0(T),0;T).
\]

A continuous quench selects a broken pair only if the source calculation
establishes a sign change of `mu_y^2`, plus positive stabilizing higher order
terms and dynamical access to the new basin. CP alone supplies none of these.

## Exact conditional theorem and hostile deformation

For WP94's restricted ansatz, `mu_y^2=2(tau-36/25)`, so a continuous `tau(T)`
with a high-temperature value above `36/25` and `tau(0)=0` must cross once or
more by the intermediate value theorem.

The smallest CP-preserving falsifier of automatic thermal selection is the
allowed deformation `+kappa*y^2` with constant `kappa>=36/25`. Its broken
stationarity condition is

\[
y^2=9/25-\kappa/4,
\]

which has no nonzero real solution for `kappa>36/25` and only merges at the
boundary for equality. Thus a mathematically CP-symmetric bath can erase the
selector rather than implement it.

## Classification

The source operation is a **conditional selector** only after the transverse
curvature crossing and dynamical basin-access conditions are derived. It is
not a texture rigidifier. The contextual partition is the CP-even branch and
the conjugate broken pair; CP pairs the latter but does not force occupation.

Remaining physical-instrument gate: compute the complete renormalized
`V_eff(x,y;T)` from the singlet, Higgs, mediator and plasma couplings; verify
curvature crossing, boundedness, transition rate, domain formation/reset and
WP93 canonical readout errors.

Verification: `uv run --with sympy python research/flavor/checkers/wp95_fdm2_general_thermal_descent.py`.
