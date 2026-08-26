# Cross-experiment quartic Gram

Work package: WP562  
Owner: marici.Figueiredo

## Independent detector complement

WP561 identifies the single-Higgs rate as the smallest source-derived
complement to the triple-Higgs quartic readout. CMS HIG-21-018 supplies a
detector-independent realization. It combines 138 inverse femtobarns of 13 TeV
CMS data and reports the inclusive Higgs yield

\[
\widehat r=1.014^{+0.055}_{-0.053}.
\]

The CMS release states that uncertainty contributions are symmetrized by the
average of upward and downward excursions. The admitted scalar uncertainty is

\[
\sigma_r={0.055+0.053\over2}=0.054.
\]

On the WP472 leading universal-mixing domain, with no exotic Higgs decay and no
new production amplitude, the trace-adjoint/Higgs mixing coordinate
\(z=\sin^2\theta\) gives \(r=1-z\).

CMS and the ATLAS HHH experiment use different detectors, so event and
detector-statistical overlap is absent. Their Standard Model normalization and
theory systematics need not be independent.

## Covariance grammar

Let \(q=\lambda_s z^2/\lambda_H\) be the source-induced quartic readout. Freeze
independent residual standard deviations \(\sigma_r>0\) and \(\sigma_q>0\),
and one shared theory nuisance with standard deviation \(\tau\geq0\) and
loadings \(a,b\). The smallest cross-experiment covariance is

\[
C=
\begin{pmatrix}
\sigma_r^2+a^2\tau^2&ab\tau^2\\
ab\tau^2&\sigma_q^2+b^2\tau^2
\end{pmatrix}.
\]

Its determinant is

\[
\det C=\sigma_r^2\sigma_q^2
+\tau^2(\sigma_r^2b^2+\sigma_q^2a^2)>0.
\]

Thus any calibrated positive independent residuals keep the combined
covariance nonsingular for every finite shared-theory loading. Zero assumed
cross-correlation is unnecessary.

## Source Gram

For source coordinates \((\lambda_s,z)\), the joint response Jacobian is

\[
J=
\begin{pmatrix}
0&-1\\
z^2/\lambda_H&2\lambda_s z/\lambda_H
\end{pmatrix}.
\]

With \(W=C^{-1}\), the source Gram obeys

\[
\det(J^TWJ)={z^4\over\lambda_H^2\det C}>0
\]

on \(z>0\), \(\lambda_H>0\). Hence shared theory covariance cannot recreate
the algebraic kernel once both independently realized detector channels are
present. It can still make the smallest eigenvalue operationally too small.

Both readouts descend under the full quark weak-basis groupoid. The mixing
angle, mass-eigenstate Higgs yield, and Higgs quartic modifier are invariant.
No texture coordinate or absolute-phase reference port enters.

## Remaining calibration gate

The CMS side is now physically calibrated at the inclusive-readout level. The
ATLAS HS3 release contains detector nuisances for each fixed signal template,
but it does not provide the portal-complete interpolation

\[
(\lambda_s,z)\longmapsto N_i(\lambda_s,z,\nu)
\]

across its analysis bins. Consequently \(\sigma_q\), the shared-theory loading
\(b\), and the source response curvature cannot yet be evaluated in the same
model. The exact Gram theorem is an acceptance test, not a numerical
identification claim.

The smallest source falsifier remains \(z=0\). The smallest instrument
falsifier is \(\sigma_q\) undefined because no portal-complete HHH template
family exists. The smallest uncertainty falsifier after completion is a
smallest source-Gram eigenvalue that does not clear the preregistered
resolution threshold.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp562_cross_experiment_quartic_gram.py

The generated result is
research/flavor/results/wp562_cross_experiment_quartic_gram.json.
