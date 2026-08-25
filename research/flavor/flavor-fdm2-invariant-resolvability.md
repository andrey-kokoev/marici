# Physical16 invariant resolvability for FDM-2 (WP107)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

WP106 supplies the conditional branchwise lower bound

\[
C_{min}=240r_{min}^3\Sigma_{min}^{3/2}
\]

for `C=|det[H_u,H_d]|`, while a symmetric source has `C=0`. Let the complete
canonical matching and single-branch measurement error obey
`|C_hat-C|<=epsilon_C`.

The symmetric readout interval is `[0,epsilon_C]`. The broken interval starts
at `C_min-epsilon_C`. A deterministic threshold separating them exists iff

\[
C_{min}>2\epsilon_C.
\]

When this strict gap holds, the exact midpoint threshold `T=C_min/2` satisfies
`epsilon_C<T<C_min-epsilon_C`. Thus the source attribute is not merely
mathematically distinguishing: it has a conditional finite-resolution
decision rule.

At equality the two certified intervals touch, and below equality they
overlap. No amount of downstream moment inversion can repair that first
canonical-readout collapse. Repetition can reduce a statistical contribution
to `epsilon_C`, but systematic canonical-matching bias must be bounded
independently.

After branch classification, WP101's route-weight certificate remains

\[
\epsilon_{route}\le
(\epsilon_s+\epsilon_d)/\gamma+\epsilon_c+\epsilon_r,
\]

with `gamma>0`. Therefore a fully separated contextual partition requires
both the invariant gap `C_min>2epsilon_C` and the detector margin `gamma>0`.

Classification: conditionally instrumented branchwise selector; neither
rigidifier nor numerical/sign selector. The smallest exact falsifier is
`C_min=2epsilon_C`, where the certified intervals meet. Remaining physical
gate: derive numerical `r_min,Sigma_min`, canonical matching/systematic error,
and detector margins on one common source and scale domain.

Verification: `uv run --with sympy python
research/flavor/checkers/wp107_fdm2_invariant_resolvability.py`.
