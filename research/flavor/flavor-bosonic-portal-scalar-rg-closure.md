# Bosonic-portal scalar RG closure: WP713

## Frozen scalar extension

Extend the WP662 two-triplet potential by one real (Z_2)-even portal boson
(chi), with quartic support

\[
V_4=lambda_na^2+lambda_mb^2+lambda_xab+lambda_cc^2
+lambda_\chi\chi^4+g_na\chi^2+g_mb\chi^2,
\]

where (a=|n|^2), (b=|m|^2), and (c=n\mathbin\cdot m).

Applying the same (operatorname{Tr}(\operatorname{Hess}V_4)^2) convention as
WP662 closes on exactly these seven operators. The first four beta polynomials
are the WP662 expressions plus

\[
\Delta\beta_n=4g_n^2,
\qquad
\Delta\beta_m=4g_m^2,
\qquad
\Delta\beta_x=8g_ng_m,
\qquad
\Delta\beta_c=0.
\]

The new equations are

\[
\beta_\chi=12g_n^2+12g_m^2+144\lambda_\chi^2,
\]

\[
\beta_{g_n}=8g_m\lambda_c+24g_m\lambda_x+32g_n^2
+80g_n\lambda_n+48g_n\lambda_\chi,
\]

\[
\beta_{g_m}=32g_m^2+80g_m\lambda_m+48g_m\lambda_\chi
+8g_n\lambda_c+24g_n\lambda_x.
\]

## Signed consequence

The source calculation fixes the WP712 bosonic normalization to
(kappa=4). Its WP709 contrast is

\[
N+M-X=4(g_n-g_m)^2.
\]

With WP711 Dirac strengths included, first-order radial opening requires

\[
(g_n-g_m)^2>2(F_n+F_m).
\]

## Disposition

WP713 repairs the RG-closure debt of WP712 within the scalar subsector. It is
a source grammar and exact transport field, not yet a selector. The portal
couplings and boson self-coupling remain free boundary data, and the full
seven-dimensional projective rays and transverse basin have not yet been
classified. Gauge, Yukawa, fermion-running, thresholds, and detector response
also remain outside this scalar packet.

The smallest exact falsifier is any one-loop scalar counterterm outside the
seven displayed operators or disagreement with the seven coefficient
polynomials.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp713_bosonic_portal_scalar_rg_closure.py

Generated result: results/wp713_bosonic_portal_scalar_rg_closure.json.
