# The Port Ratio Is Gauge-Dependent but the Safety Margin Is Invariant

For the conditional residual

\[
R(x)=\beta J(x)-\alpha xK(x),
\]

the previous compiler used the projective coordinate \(r=\beta/\alpha\). That
number is not intrinsic until the normalizations of the two port rays are
frozen.

Rescale the typed repair and drift features by positive units

\[
J'=uJ,
\qquad
K'=vK,
\qquad
u,v>0.
\]

To preserve the same residual, the coefficients transform contragrediently:

\[
\beta'=\frac\beta u,
\qquad
\alpha'=\frac\alpha v.
\]

Then

\[
\beta'J'-\alpha'xK'
=\beta J-\alpha xK,
\]

but

\[
r'=\frac{\beta'}{\alpha'}
=\frac vu r.
\]

Thus no numerical lower bound on \(\beta/\alpha\) is gauge-invariant by
itself.

## Pointwise invariant margin

The pointwise threshold transforms in exactly the same way:

\[
\rho_{\mathrm{pt}}
=\sup_{x\in I}\frac{xK(x)}{J(x)},
\]

\[
\rho'_{\mathrm{pt}}
=\frac vu\rho_{\mathrm{pt}}.
\]

Therefore the dimensionless safety factor

\[
M_{\mathrm{pt}}
=\frac{r}{\rho_{\mathrm{pt}}}
\]

is invariant. Pointwise positivity is simply

\[
M_{\mathrm{pt}}>1.
\]

Equivalently, the local invariant is the directly evaluated ratio

\[
m(x)
=\frac{\beta J(x)}{\alpha xK(x)}.
\]

## Integrated invariant margin

With source weight \(w\), define

\[
M_{\mathrm{int}}
=
\frac{
\beta\int_IwJ
}{
\alpha\int_IwxK
}.
\]

Both numerator and denominator are invariant under the paired feature and
coefficient rescalings. Hence

\[
M'_{\mathrm{int}}=M_{\mathrm{int}}.
\]

Integrated positivity is exactly

\[
M_{\mathrm{int}}>1.
\]

The completion-ready statement is therefore not

\[
\frac{\beta_X}{\alpha_X}\ge r_*,
\]

unless the port units have been fixed. It is

\[
M_{\mathrm{int},X}\ge1+\delta
\]

or the corresponding pointwise margin, with cutoff-independent
\(\delta>0\).

## Polarization versus normalization

Positive diagonal rescaling preserves the distinction between the repair ray
and the drift ray. A general linear mixing of \((J,K)\) does not. Under such a
mixing, the decomposition into positive repair and negative drift is itself
changed.

Therefore the source must supply two different pieces of structure:

1. a polarization selecting the repair and drift rays;
2. either a normalization of those rays or a statement written entirely in
   invariant margins.

The first is structural and cannot be removed by projectivization. The second
is a choice of units and should not carry theorem content.

## Exact hostile normalization

Take \(u=2\) and \(v=1\). Then

\[
r'=\frac r2,
\qquad
\rho'=\frac\rho2.
\]

A raw claim that the ratio exceeds a fixed numerical threshold can change
truth value under this harmless change of units, while

\[
\frac{r'}{\rho'}=\frac r\rho
\]

and the residual remain unchanged.

## Falsifiers

- Reporting a cutoff-uniform bound on \(\beta/\alpha\) without frozen port
  units.
- Comparing ratios computed in different normalizations.
- Allowing constructor transport to mix the repair and drift rays silently.
- A claimed invariant margin that changes under positive diagonal rescaling.
- A completion margin whose denominator vanishes or loses continuity.
- Treating the choice of units as the source mechanism enforcing positivity.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The aim was to test whether the newly isolated compiler coordinate was
actually intrinsic.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The raw ratio is gauge-dependent; the invariant theorem lives in a
dimensionless safety margin plus a source-fixed port polarization.
