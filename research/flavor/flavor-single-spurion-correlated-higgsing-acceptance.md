# Single-spurion correlated-Higgsing acceptance theorem: WP749

## Question

Can one source deformation generate both the heavy-vector mass and the soft
mass required by WP747, so that WP748's independent trajectory amplitude and
clock no longer control the dimensionless portal magnitude?

## Admitted construction

Assume one positive spurion scale \(v^2\), a fixed interacting gauge
normalization \(g_*^2\), and positive response coefficients \(a,b\) such that

\[
M_V^2=a g_*^2v^2,
\qquad
m_{\mathrm{soft}}^2=b g_*^2v^2.
\]

This is an acceptance hypothesis, not a microscopic source model. In
particular, WP749 does not assume that \(a:b\) has already been derived.

## Exact cancellation

The WP747 nondecoupling factor becomes

\[
\epsilon
=\frac{m_{\mathrm{soft}}^2}{M_V^2+m_{\mathrm{soft}}^2}
=\frac{b}{a+b}.
\]

Consequently the ordered WP746 portal contrast is

\[
\Delta
=\frac{g_*^2}{2}\frac{b}{a+b}>0.
\]

The common dimensionful clock \(v\) cancels. A source theory satisfying these
relations would therefore avoid the specific amplitude mismatch isolated by
WP748 and would preserve the required ordered sign.

## Residual coefficient fiber

Clock cancellation is not numerical selection. At the same \(g_*\) and \(v\),

\[
(a,b)=(1,1)
\quad\Longrightarrow\quad
\Delta=\frac{g_*^2}{4},
\]

while

\[
(a,b)=(1,3)
\quad\Longrightarrow\quad
\Delta=\frac{3g_*^2}{8}.
\]

The exact residual is \(g_*^2/8\). Thus saying that both masses come from one
spurion is insufficient. The source must fix the positive coefficient ray
\(a:b\), not merely permit it.

## Threshold and readout do not cancel

The low-energy support condition remains

\[
E^2<M_V^2=a g_*^2v^2.
\]

It retains the physical clock \(v\), the spectrum coefficient \(a\), and the
experimental energy \(E\). Cancellation in the dimensionless matching factor
therefore does not prove threshold survival. Nor does this algebra construct a
map from the source perturbation into calibrated `physical16` detector units.

## Deutschian disposition

The construction is not yet a hard-to-vary explanation. Its mechanism
survives arbitrary positive changes of \(a:b\), even though those changes alter
the numerical prediction. It is instead an exact acceptance theorem for a
future source theory:

1. one independently required source deformation generates both masses;
2. representation theory or dynamics uniquely fixes \(a:b\);
3. the same anomaly-free theory fixes the ordered embedding and \(g_*\) with
   an attractive basin;
4. its spectrum proves the threshold inequality over the admitted domain;
5. its source-defined probe descends to `physical16` and has a calibrated
   instrument.

Failure of any item prevents the construction from answering the active
source-principle question.

## Disposition

WP749 is a conditional magnitude selector and common-clock canceller. It is
not a source theorem, threshold-survival theorem, or physical readout. The
smallest exact falsifier to numerical uniqueness is the two coefficient
packets above.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp749_single_spurion_correlated_higgsing_acceptance.py`.

Generated result:
`results/wp749_single_spurion_correlated_higgsing_acceptance.json`.
