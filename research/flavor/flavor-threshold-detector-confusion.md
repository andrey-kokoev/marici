# Threshold detector confusion (WP370)

## Bounded detector model

Pass WP369's dispersive and absorptive threshold vector \(u\) through a
calibrated symmetric two-channel confusion matrix

\[
C_\beta=
\begin{pmatrix}
1-\beta&\beta\\
\beta&1-\beta
\end{pmatrix},
\qquad 0\leq\beta\leq\frac12.
\]

The detector record is \(d=C_\beta u+b\), where \(b\) is an independently
calibrated fixed background. The detector eigenchannels have gains

\[
1,
\qquad
\gamma=1-2\beta.
\]

Thus the complementary difference channel survives exactly when
\(\gamma>0\).

## Composed faithfulness

WP369's source-to-threshold Jacobian has determinant

\[
\det J_{\mathrm{thr}}
=-\frac{\mu^4}{4(L^2+\Omega^2)^2}.
\]

The composed detector Jacobian satisfies

\[
\det(C_\beta J_{\mathrm{thr}})
=(1-2\beta)\det J_{\mathrm{thr}}.
\]

For calibrated \(\beta<1/2\), subtracting \(b\) and applying
\(C_\beta^{-1}\) recovers both threshold channels exactly. At
\(\beta=1/2\), the two source packets \((1,0)^T\) and \((0,1)^T\) both produce
the record \((1/2,1/2)^T\). Detector resolution then destroys the
complementary repair.

## Background gate

A fixed known background does not alter the response Jacobian. An unknown
differential background does: in the difference channel the record depends on
\(\gamma a+\delta\), where \(a\) is the physical channel amplitude and
\(\delta\) is background asymmetry. The packets \((a,\delta)=(1,0)\) and
\((0,\gamma)\) collide exactly. Background calibration is therefore part of
the faithfulness theorem, not an optional correction.

## Disposition

Finite detector confusion preserves WP369's local pole identification only on
the calibrated positive-contrast domain. It does not create selector
authority or a second source control. Its exact robustness margin is
\(\gamma=1-2\beta\); inversion amplifies the difference channel by
\(1/\gamma\).

The smallest exact falsifier is complete confusion \(\beta=1/2\). The
remaining instrument gate is an independently calibrated lower bound on
\(\gamma\), background asymmetry, and finite-sample noise over the support of
the threshold scan.

Run `uv run --with sympy python
research/flavor/checkers/wp370_threshold_detector_confusion.py` to regenerate
the exact result.
