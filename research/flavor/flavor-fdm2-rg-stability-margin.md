# RG transport of the FDM-2 stability margin (WP105)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Define the strict portal-stability margin at logarithmic scale `t=log(mu/mu0)`:

\[
\Delta(t)=\lambda_H(t)-rac{(\lambda_x^-(t))^2+(\lambda_y^-(t))^2}{8}.
\]

The complete scalar source is quartically coercive only while `Delta(t)>0`.
Within a fixed portal-sign chamber its exact beta function is

\[
\dot\Delta=\beta_H-rac{1}{4}
\left({\bf1}_{\lambda_x<0}\lambda_x\beta_x+
{\bf1}_{\lambda_y<0}\lambda_y\beta_y\right).
\]

If a source calculation certifies `|dot Delta|<=B` on an interval
`|t|<=L`, then

\[
\Delta(t)\ge\Delta(0)-BL.
\]

Consequently `Delta(0)>BL` is a sufficient strict stability certificate for
the whole interval. This is a transport condition, not a selector for the
initial coefficient values.

Sign-chamber crossings are not singular in `Delta`: the squared negative-part
function is continuously differentiable at zero. They do, however, require
updating the active beta-function term. Threshold matching can also jump the
couplings, so every threshold needs its own post-match positive margin.

The exact hostile flow `Delta(t)=Delta0-Bt` reaches the flat boundary at
`t=Delta0/B` and becomes unstable afterward. It proves that pointwise
stability at `mu0` cannot authorize a wider scale or thermal domain.

Classification: RG supplies stability transport inside a declared source
domain; it is neither selector nor rigidifier. Smallest exact falsifier of a
claimed interval certificate is `Delta0=BL`, which reaches the unsafe flat
boundary at the endpoint. Remaining gate: derive the actual coupled beta
functions and threshold jumps for the portal-complete singlet, Higgs,
vectorlike mediator, and Yukawa system, then certify `B,L` without fitting the
desired result.

Verification: `uv run --with sympy python
research/flavor/checkers/wp105_fdm2_rg_stability_margin.py`.
