# Exact thermal phase gate for FDM-2 (WP94)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Test the minimal CP-even thermal deformation

\[
V_\tau=V+\tau(x^2+y^2),\qquad \tau\ge0.
\]

This is a typed ansatz, not a derived finite-temperature effective action.
Its exact CP-odd stationarity equation factorizes as

\[
\partial_yV_\tau=2y(\tau+4y^2-36/25).
\]

Hence the CP-broken branches obey

\[
y_\pm(\tau)=\pm\sqrt{9/25-\tau/4}
\]

and meet the CP-even branch continuously at `tau_c=36/25`. The curvature of
the CP-even branch in the `y` direction is `2(tau-36/25)`, so cooling through
the critical value produces the required pitchfork within this ansatz.

This repairs the absence of an explicit quench path, but not its source
authority. A physical calculation must derive `tau(T)` and all other allowed
thermal terms from the declared singlet/mediator plasma. CP symmetry enforces
evenness in `y`, not this one-parameter thermal form or a nucleation/reset rate.

Classification: the ansatz supplies a selector dynamics, not a rigidifier.
Smallest falsifier of the ansatz-level transition is a derived thermal
effective potential whose `y=0` curvature never changes sign. Remaining
instrument gate: source-derived thermal coefficients, rates, domains, and
canonical Yukawa matching from WP93.

Verification: `uv run --with sympy python research/flavor/checkers/wp94_fdm2_thermal_phase.py`.
