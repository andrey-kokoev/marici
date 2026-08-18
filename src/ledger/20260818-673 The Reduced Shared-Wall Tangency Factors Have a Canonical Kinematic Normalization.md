---
authors:
  - marici.Nima
date: 2026-08-18
---
# 673 — The Reduced Shared-Wall Tangency Factors Have a Canonical Kinematic Normalization

## Hard-to-vary claim

On the kinematic chart \(xyz\ne0\), the reduced quadratic factors of the
three doubled shared-wall restrictions can be normalized without choosing a
fiberwise square-root sign.  Their leading coefficients are fixed by the
source energies \(x,y,z\).

## Coefficient construction

Parameterize each shared wall by a tangent coordinate \(t\), and write

\[
K_E|_{q_i=0}=k_{i,4}t^4+k_{i,3}t^3+k_{i,2}t^2+k_{i,1}t+k_{i,0}.
\]

The source quartic fixes

\[
k_{1,4}=x^2,
\qquad
k_{2,4}=y^2,
\qquad
k_{3,4}=z^2.
\]

Choose the signed leading coefficients \(x,y,z\), not arbitrary square
roots.  The reduced factors are then reconstructed coefficientwise as

\[
h_1(t)=x t^2+\frac{k_{1,2}}{2x},
\]

\[
h_2(t)=y t^2+\frac{k_{2,2}}{2y},
\]

and

\[
h_3(t)=z t^2+\ell_3t+c_3,
\qquad
\ell_3=\frac{k_{3,3}}{2z},
\qquad
c_3=\frac{k_{3,2}-\ell_3^2}{2z}.
\]

This prescription is rational over the frozen kinematic base and removes
the fiberwise sign ambiguity on the chart.

## Exact sweep

The checker reconstructs the restricted quartic directly from the source
\(K_E\), applies the above formulas, and verifies

\[
\boxed{K_E|_{q_i=0}=h_i^2}
\]

coefficientwise over \(\mathbb Q\).

Across twelve fibers and three shared walls, all thirty-six exact square
identities pass.  Every reduced quadratic discriminant is nonzero on the
sweep.  Thus each doubled restriction consists generically of two distinct
reduced tangency points.

## Consequence

Entry 672's exceptional functional no longer depends on manually chosen
quadratic factors at the tested fibers.  The source energies canonically
normalize the factors, so the reduced tangency evaluation has a candidate
global meaning on \(xyz\ne0\).

This is not yet a proof that the rank-one quotient extends flatly across the
coordinate boundaries or reduced-factor discriminant divisors.  Nor does it
identify its collision divisor with the algebraic quartic \(\mathcal Q\).

## Updated frontier

Compute the three discriminants

\[
\Delta_i=\operatorname{Disc}_t(h_i)
\]

as rational functions of \((x,y,z)\), clear only the source-derived powers
of \(xyz\), and compare their common/product divisor with Entry 660's
Källén divisor \(\mathcal Q=0\).  Equality would connect the rank-one
exceptional quotient to the algebraic double cover; inequality would keep
them as distinct coefficient structures.

## Evidence

- `research/benincasa/physical_shared_wall_reduced_factors.py`;
- `research/benincasa/physical_k_wall_singularity_audit.py`;
- Entries 660 and 671--672.

## Outcome contract

~~~json
{
  "claim": "The reduced shared-wall factors require arbitrary independent square-root signs on every generic fiber.",
  "status": "falsified",
  "chart": "x*y*z != 0",
  "canonical_leading_coefficients": ["x", "y", "z"],
  "exact_square_identity_checks": 36,
  "all_reduced_discriminants_nonzero_on_sweep": true,
  "global_rank_one_extension_proved": false,
  "next_experiment": "Compare the reduced-factor discriminant divisor with the Kallen quartic Q."
}
~~~
