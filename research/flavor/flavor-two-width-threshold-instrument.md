# Two-width threshold instrument: WP652

## Source-derived ports

The two vertices in each WP651 messenger chain generate distinct labelled
decay channels when both are kinematically open. After independent
phase-space calibration,

\[
\Gamma_L=A_LM|x|^2,
\qquad
\Gamma_R=A_RM|y|^2.
\]

For \(u=\log|x|\) and \(v=\log|y|\), the normalized log-width response is

\[
(u,v)\longmapsto(2u,2v).
\]

Its Jacobian has rank two. With any independently calibrated positive metric
\(W=\operatorname{diag}(w_L,w_R)\),

\[
\det(J^\top WJ)=16w_Lw_R>0.
\]

Each width alone has rank one, so two labelled ports are necessary and
sufficient for the two magnitude directions. WP651's hostile constructors
give normalized width pairs ((1,1)) and ((4,1/4)), and are therefore
distinguished.

## Quotient and phase typing

The low-energy coefficient already measures the product phase
(\arg(xy)). The reciprocal phase transformation is a rephasing of the
vectorlike messenger field, not an additional physical source direction.
Thus the combined low-energy and two-width experiment is faithful on the
physical vertex-magnitude quotient under the stated channel assumptions.

## Experimental boundary

This is an ideal, source-derived threshold instrument, not yet a calibrated
detector realization. Admission requires both channels to be open and
distinguishable after finite widths, mixing, backgrounds, branching
reconstruction, mass resolution, efficiencies, and uncertainties. The
smallest singular value must remain positive after those effects.

It repairs source identification on the magnitude fiber; it does not select
the numerical coefficient values.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp652_two_width_threshold_instrument.py
```

Generated result: `results/wp652_two_width_threshold_instrument.json`.
