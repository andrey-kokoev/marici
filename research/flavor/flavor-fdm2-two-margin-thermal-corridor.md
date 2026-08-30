# Two-margin thermal corridor for FDM-2 (WP106)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

## Independent source margins

Along a declared thermal/RG path parameterized by `s`, define

\[
\Delta(s)=\lambda_H-rac{(\lambda_x^-)^2+(\lambda_y^-)^2}{8}
\]

for global quartic coercivity, and

\[
\Sigma(s)=36/25-\tau(s)-\lambda_y(s)u(s)
\]

for local CP breaking in the WP94/WP102 normalization. The transverse
curvature is `-2 Sigma`, and the broken branch obeys `y^2=Sigma/4`.

The thermal source is admissible as a selector only in the intersection

\[
\Delta(s)>0\quad\text{and}\quad\Sigma(s)>0.
\]

Neither condition implies the other.

If `|dot Delta|<=B_Delta`, `|dot Sigma|<=B_Sigma` on path length `L`, then the
strict corridor certificate is

\[
\Delta_0>B_\Delta L,
\qquad
\Sigma_0>B_\Sigma L.
\]

The surviving margins are
`Delta_min=Delta0-B_Delta L` and
`Sigma_min=Sigma0-B_Sigma L`.

## Faithful CP-odd margin

For the exact WP90 Yukawa witness generalized to `S=x+i y` and finite
threshold factor `r`, the checker derives

\[
\det[H_u,H_d]=1920i\,r^3y(x^2+y^2).
\]

On either broken branch, `|x^2+y^2|>=y^2` and
`|y|>=\sqrt{\Sigma_{min}/4}`. If `r>=r_min>0`, the corridor therefore gives
the exact conservative physical16 bound

\[
|\det[H_u,H_d]|\ge240\,r_{min}^3\Sigma_{min}^{3/2}>0.
\]

This turns the qualitative selector into a nonzero invariant-margin
certificate, conditional on source-derived path bounds. It still does not
select the sign or numerical magnitude.

## Verdict

Classification: branchwise finite-threshold selector throughout a certified
two-margin corridor; not a rigidifier or coefficient selector. The smallest
exact falsifiers are `Delta_min=0` (global flat boundary) and `Sigma_min=0`
(CP branches merge). Remaining instrument gate: derive `tau(s),u(s)`, portal
running and thresholds, certify both derivative bounds and `r_min`, and join
this source margin to WP101's downstream error budget.

Verification: `uv run --with sympy python
research/flavor/checkers/wp106_fdm2_two_margin_corridor.py`.
