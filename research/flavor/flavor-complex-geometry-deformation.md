# Complex-geometry deformation (WP353)

## Continuous projector family

Replace the third projector ray by the normalized vector proportional to

\[
(1,it,1)^T.
\]

Keeping the WP350 sector-character directions fixed gives the exact normalized
CP invariant

\[
J^2(t)=
\frac{t^2}
{(t^2+2)(8t^6+60t^4+96t^2+17)}.
\]

The real geometry (t=0) conserves CP, while (t=1) recovers the falsified
WP351 value (1/543). Near the real locus,

\[
J^2(t)=\frac{t^2}{34}+O(t^4).
\]

The derivative at (t=1) is nonzero, so (t) carries physical normalized-CP
authority rather than a chart choice.

## Ensemble-scale implication

The fitted (J^2) scale can be reached on a small-(t) capability branch, with
leading estimate below (10^{-3}). This is not a prediction. Choosing that
branch from the observed value fits the complex projector geometry.

Moreover (t) and (-t) are conjugate geometries with the same (J^2), and the
rational response may admit additional magnitude branches. Readout equality
does not imply a unique source geometry.

## Successor gate

A progressive successor must derive a discrete or stationary (t) from a
source action before reading flavor data. Its prediction must then survive the
complete ensemble without retuning the projector ray.

Run `uv run --with sympy python
research/flavor/checkers/wp353_complex_geometry_deformation.py` to regenerate
the exact deformation audit.
