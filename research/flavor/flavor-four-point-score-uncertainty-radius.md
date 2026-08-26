# Four-point score uncertainty radius

Work package: WP568  
Owner: marici.Figueiredo

## Purpose

WP567 supplied the missing deterministic interface:

\[
d=K\operatorname{diag}(p_0)s,
\]

where \(s\) is a frozen source score, \(K\) an independently calibrated
detector channel, and \(d\) the detector-probability tangent. A nonzero nominal
\(d\) is not yet an experimental result. Calibration and nuisance uncertainty
may contain a completion that erases it.

This packet derives the exact robust acceptance condition.

## Typed uncertainty set

Let \(W\) be a positive detector metric fixed independently of the desired
answer. For an ordinary multinomial score test, the local Fisher metric is
\(W=\operatorname{diag}(q_0)^{-1}\) on the probability-conserving tangent
space. Let the independently propagated calibration and nuisance uncertainty
in \(d\) be the ellipsoid

\[
\mathcal U_\rho=
\left\{\delta:
\delta^T W\delta\le\rho^2,
\quad
\mathbf 1^T\delta=0
\right\}.
\]

The radius \(\rho\) must be derived by transporting uncertainty in the
calibrated channel \(K\), source baseline \(p_0\), and nuisance completion. It
cannot be chosen from the desired significance.

## Exact robust Gram theorem

Write \(r=\sqrt{d^T Wd}\). Because \(d\) lies in the probability-conserving
tangent space, the reverse triangle inequality gives

\[
\sqrt{(d+\delta)^T W(d+\delta)}\ge r-\rho.
\]

The bound is attained by an uncertainty displacement antiparallel to \(d\).
Therefore

\[
\min_{\delta\in\mathcal U_\rho}
(d+\delta)^T W(d+\delta)
=\max(r-\rho,0)^2.
\]

The detector direction is robustly resolved exactly when

\[
\rho<\sqrt{d^T Wd}.
\]

Strict positivity of the nominal Gram is insufficient. The uncertainty radius
must be strictly smaller than the nominal metric norm.

## Exact hostile radii

Use WP567's noisy binary detector channel. Its nominal distribution and
tangent are

\[
q_0=(1/2,1/2)^T,
\qquad
d=(1/4,-1/4)^T,
\qquad
W=2I_2.
\]

Hence \(d^TWd=1/4\) and \(r=1/2\).

- At \(\rho=1/4\), the exact worst-case Gram is \(1/16>0\). The direction is
  uncertainty-stable.
- At \(\rho=1/2\), the uncertainty set contains \(\delta=-d\), and the exact
  worst-case Gram is zero. The same nominal instrument no longer has
  identification authority.

This is the smallest exact uncertainty falsifier for the score-channel
constructor. Nothing about the nominal channel changes; only the admitted
calibration support changes.

## Experimental acceptance contract

A portal-score experiment may claim a resolved four-point direction only if:

1. \(s\), \(K\), and \(W\) are frozen independently;
2. null and failed-selection records are included in \(K\);
3. channel and nuisance uncertainties are propagated into a declared set
   \(\mathcal U_\rho\) in the same detector frame;
4. support and probability normalization are preserved;
5. the exact or certified lower bound on the profiled Gram is positive;
6. the inequality remains strict under completion and finite-resolution
   uncertainty.

For multiple source directions, the scalar radius test is replaced by a lower
bound on the smallest singular value or smallest generalized Gram eigenvalue.
The same rule applies: authority requires the entire admitted uncertainty set
to remain outside the relevant kernel.

## Classification and present gate

The operation remains a separator constructor, not a selector. It can certify
that a source direction survives a calibrated detector channel; it does not
choose the source value. Its entrance and exit are physical probabilities on
an invariant `physical16` path, so full weak-basis descent passes. No reference
port is introduced.

WP568 closes the formal uncertainty grammar but not the physical-instrument
gate. No current HHH release supplies an independently calibrated portal-score
channel together with a transported uncertainty ellipsoid in the common
source/readout frame. Until such an object exists, the robust Gram cannot be
evaluated experimentally.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp568_four_point_score_uncertainty_radius.py

The generated result is
`research/flavor/results/wp568_four_point_score_uncertainty_radius.json`.
