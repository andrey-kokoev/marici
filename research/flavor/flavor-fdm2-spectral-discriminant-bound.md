# Source spectral-discriminant bound for FDM-2 (WP110)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

## Sharp three-level discriminant bound

For ordered nonnegative eigenvalues `0<=a<=b<=c<=U`, write the adjacent gaps
`p=b-a`, `q=c-b`. Then

\[
|(a-b)(a-c)(b-c)|=pq(p+q)
\le{(p+q)^3\over4}\le {U^3\over4}.
\]

The bound is sharp at `(a,b,c)=(0,U/2,U)`. Therefore Gram operator-norm
bounds `||H_u||<=U_u`, `||H_d||<=U_d` imply

\[
|\Delta_u\Delta_d|\le {U_u^3U_d^3\over16}.
\]

## Bound from the mediator source

For the WP90 family

\[
Y_d=Y_0+r z ab,
\]

the exact source norms are `||Y0||=4`, `||a||=sqrt(14)`,
`||b||=sqrt(6)`. If the same corridor supplies
`r<=r_max` and `|z|<=Z_max`, then

\[
U_d\le(4+\sqrt{84}\,r_{max}Z_{max})^2,
\qquad U_u=9.
\]

Combining WP106 and WP109 gives the source-normalized lower bound

\[
|J|\ge
{1920\,r_{min}^3\Sigma_{min}^{3/2}\over
729(4+\sqrt{84}\,r_{max}Z_{max})^6}.
\]

This is independent of the observed 1,210-sheet minimum. It is conservative,
not a numerical prediction until the four corridor bounds are source-derived.

Classification: source-typed normalized margin transport, not a new selector
or rigidifier. The smallest falsifier of a positive normalized bound is the
absence of finite `r_max` or `Z_max`: the spectral upper bound becomes
unbounded and the inferred `|J|` lower bound collapses to zero. Degenerate
spectra do not invalidate the raw CP-odd determinant but do invalidate the
normalized Jarlskog coordinate.

Remaining instrument gate: derive finite `r_min,r_max,Z_max,Sigma_min` and
canonical `|J|` error on one RG/thermal domain, then compare the resulting
source bound—without fitting—to the external ensemble margin.

Verification: `uv run --with sympy python
research/flavor/checkers/wp110_fdm2_spectral_discriminant_bound.py`.
