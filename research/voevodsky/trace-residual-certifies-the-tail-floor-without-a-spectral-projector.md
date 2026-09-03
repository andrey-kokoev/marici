# Trace residual certifies the tail floor without a spectral projector

## Question

Must the selected 25-dimensional polynomial space be interval-identified with the exact concentration spectral projection before applying the tail coercivity bound?

## Claim boundary

No. Any exactly orthonormal 25-dimensional polynomial space whose captured concentration trace leaves residual below \(1/130\) has the required concentration bound on its own orthogonal complement. Spectral identification, a Davis--Kahan angle, and enclosure of individual Ritz vectors are unnecessary for this step. The finite Gram and captured-trace enclosures remain to be computed.

## Compression theorem

Let \(T\geq0\) be the trace-class concentration operator, let \(P\) be any finite-rank orthogonal projection, and write \(Q=I-P\). Positivity gives

\[
QTQ\geq0.
\]

For every positive trace-class operator, its norm is bounded by its trace. Therefore

\[
\|QTQ\|
\leq
\operatorname{Tr}(QTQ).
\]

Cyclicity and \(P+Q=I\) give

\[
\operatorname{Tr}(QTQ)
=
\operatorname{Tr}(T)-\operatorname{Tr}(PTP).
\]

Consequently,

\[
\operatorname{Tr}(T)-\operatorname{Tr}(PTP)<\frac1{130}
\quad\Longrightarrow\quad
QTQ<\frac1{130}Q.
\]

No invariance of \(P\) under \(T\) is used.

## Numerical margin

For the degree-79 polynomial space selected by the scout,

\[
\operatorname{Tr}(T)=\frac{70}{\pi},
\qquad
\operatorname{Tr}(PTP)\approx22.2754980198366.
\]

Thus

\[
\operatorname{Tr}(T)-\operatorname{Tr}(PTP)
\approx0.00619401302874
<
\frac1{130},
\]

with margin about \(0.00149829466\).

## Consequence for the gamma tail

The bad-frequency localization argument supplies the operator inequality

\[
A\geq\frac1{40}I-\frac{130}{40}T.
\]

On \(Q\), the trace residual bound implies

\[
QAQ
\geq
\frac1{40}Q-\frac{130}{40}QTQ
>
0.
\]

If a quantitative floor is required, an enclosed trace residual \(\rho<1/130\) yields

\[
QAQ\geq\frac{1-130\rho}{40}Q.
\]

This last expression shows that \(1/40\) is not itself the coercivity floor after subtracting the concentration penalty. Any use of \(C^{-1}\leq40Q\) requires a separate proof that \(C\geq1/40\,Q\); the trace argument alone gives only \((1-130\rho)/40\).

## Falsification and correction

The current Schur residual calculations use the factor \(40\), equivalent to assuming \(C^{-1}\leq40Q\). The displayed localization inequality combined with \(\rho\approx0.006194\) instead gives the much weaker inverse factor

\[
\frac{40}{1-130\rho}
\approx205.3.
\]

Unless an independent tail-floor theorem establishes \(C\geq1/40\,Q\), the factor-40 a posteriori lower forms are not continuum-valid. The next scout must replace \(40\) by the trace-derived inverse factor and test whether positivity survives.

## Disposition

The projector-angle gate is removed, but a hidden coercivity-strength assumption is exposed. The finite trace enclosure can certify the correct complement floor directly. Existing factor-40 Schur margins remain diagnostics pending the stronger correction test. No continuum positivity or RH implication is asserted.
