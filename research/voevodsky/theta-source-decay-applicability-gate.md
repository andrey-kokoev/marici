# Theta source-decay applicability gate

## Question

Can fixed-parameter Gaussian theta decay supply the weighted source map required by the affine-filler completion theorem?

## Claim boundary

The audit tests transfer into \(B_\epsilon\). It does not alter the conditional filler theorem.

## Fixed slices versus uniform control

For a fixed geometric parameter \(x>0\), theta coefficients

\[
c_n(x)=e^{-\pi n^2x}
\]

belong to every polynomially weighted summability space. This is only parameterwise.

Set \(x=m^{-2}\). For every \(n\leq m\),

\[
c_n(m^{-2})\geq e^{-\pi}.
\]

Hence

\[
\sum_{n\geq1}c_n(m^{-2})n^\epsilon
\geq e^{-\pi}\sum_{n=1}^m n^\epsilon,
\]

which diverges as \(m\) increases for every \(\epsilon>0\). Theta decay is therefore not uniform toward this Mellin boundary.

For unsmoothed Euler coefficients \(c_n=1\), the weighted norm diverges directly:

\[
\sum_{n\geq1}n^\epsilon=\infty.
\]

The exact checker instantiates \(\epsilon=1\), verifies the growing theta lower bounds, and verifies growing dyadic Euler blocks.

## Disposition

No source-derived map from the actual theta/Euler object into \(B_\epsilon\) has been supplied. The acceptance test is an explicit coefficient-and-label map together with a positive weighted norm estimate uniform over an orbit wide enough to contain the modular endpoints. Parameterwise Gaussian decay cannot substitute for that estimate.

The conditional filler theorem remains valid on its declared domain. It currently yields no RH implication.

## Verification

- `research/voevodsky/theta-source-decay-applicability-gate-v1.json`
- `research/voevodsky/checkers/check_theta_source_decay_applicability_gate.py`
- `research/voevodsky/results/theta_source_decay_applicability_gate.json`
