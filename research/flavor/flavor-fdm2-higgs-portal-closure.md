# Higgs-portal closure of the FDM-2 source (WP102)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

## Missing renormalizable source terms

WP90 declares a CP-even complex gauge singlet `S=x+i y` and the Standard Model
Higgs doublet `H`, but its scalar source is not the complete gauge- and
CP-invariant renormalizable potential. In addition to the singlet monomials
catalogued by WP91, the mixed scalar basis contains

\[
(H^\dagger H)x,\qquad (H^\dagger H)x^2,\qquad
(H^\dagger H)y^2.
\]

Their coefficients are respectively dimension one, dimensionless, and
dimensionless. CP forbids `(H^dagger H)y` and `(H^dagger H)xy`, but it does
not forbid any of the three displayed portals.

Consequently the WP94 one-parameter thermal ansatz is not closed under the
declared source symmetries. Setting all portals to zero is a renormalization
condition, not a consequence of CP or gauge invariance.

## Exact selector sensitivity

Write `h2=H^dagger H` and add the allowed portal

\[
\Delta V=\lambda_y h_2y^2.
\]

Along the CP-even branch, it shifts the exact transverse curvature by
`2 lambda_y h2`. For the WP90 scalar potential,

\[
\partial_y^2(V+\Delta V)|_{y=0}
=2(\lambda_y h_2-36/25).
\]

The broken stationary branch becomes

\[
y^2=9/25-\lambda_yh_2/4.
\]

Thus an allowed portal background with `lambda_y h2>36/25` removes the
CP-broken branch. Conversely a negative portal can enhance the instability,
subject to global boundedness of the complete quartic form. The portal is
therefore source data at the selector arrow, not downstream detector noise.

## Verdict

FDM-2 remains a **conditional branchwise selector**, not a rigidifier. The
smallest exact falsifier of selection by the incomplete WP90 source is the
single allowed term `lambda_y(H^dagger H)y^2` at
`lambda_y h2>36/25`. It descends under the full weak-basis groupoid because it
contains no generation-space presentation data.

The remaining physical-instrument gate is sharpened: declare and renormalize
the complete Higgs-singlet scalar potential, impose boundedness, derive the
temperature-dependent Higgs background and fluctuations, and only then test
the transverse-curvature crossing and rates used by WP101.

Verification: `uv run --with sympy python
research/flavor/checkers/wp102_fdm2_higgs_portal_closure.py`.
