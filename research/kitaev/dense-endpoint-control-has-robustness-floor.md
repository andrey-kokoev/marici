# Dense endpoint control has a robustness floor

Owner: `marici.Kitaev`

## Question

When an executable one-parameter control is dense in a higher-dimensional
endpoint torus, does density supply a robust compiler after sufficiently long
control time?

## Claim boundary

Not under a fixed nonzero calibration uncertainty.

Consider

\[
U_\alpha(t)
=
\operatorname{diag}(e^{it},e^{i\alpha t}),
\qquad
\alpha\notin\mathbb Q.
\]

Let `\tau(\varepsilon)` be the least time such that the orbit segment
`|t|\le\tau` is `\varepsilon`-dense in the two-torus of target phases.
The orbit segment is a curve of length proportional to `\tau`. Its
`\varepsilon`-tube has area at most a metric constant times
`\varepsilon\tau`. Covering a torus of fixed positive area therefore
requires

\[
\tau(\varepsilon)\ge \frac{c}{\varepsilon}
\]

for some metric-dependent `c>0`. Arithmetic properties of `\alpha` can
make particular hitting times worse, but cannot beat this dimensional lower
bound uniformly over targets.

Now let the realized frequency be `\alpha+\eta`, with unknown
`|\eta|\le\delta`. A pulse of duration `t` accumulates an additional
relative phase `\eta t`. Before phase wrapping, worst-case calibration
deviation is proportional to `\delta|t|`.

Hence any compiler that covers every target to nominal accuracy
`\varepsilon` must employ, for some target, time of order at least
`1/\varepsilon`. On that target the adversarial phase uncertainty is of
order at least `\delta/\varepsilon`, up to the nominal error and metric
constants. A robust error target `\varepsilon` consequently requires

\[
\delta\,\tau(\varepsilon)
\lesssim
\varepsilon,
\]

which combined with the covering bound gives a floor of order

\[
\varepsilon\gtrsim\sqrt\delta.
\]

The scaling statement is the theorem; constants depend on the chosen torus
metric and error convention. It assumes uncompensated static frequency
uncertainty and a single open-loop dense orbit. Feedback, echo symmetry, or
additional independently calibrated controls change the constructor theory
and may evade the bound.

Thus topological density gives approximate distinguishability but not
arbitrarily accurate robust execution. Increasing compilation time eventually
amplifies the coefficient uncertainty faster than it improves the global
cover.

## Disposition

A closure-based control claim must carry two functions:

1. a covering-time modulus `\tau(\varepsilon)`;
2. a sensitivity modulus for admitted control faults over that time.

The physical compiler is valid at accuracy `\varepsilon` only where their
composition remains below the error budget. Report the best attainable robust
accuracy, not merely density of the ideal orbit.

For D(S3), any proposal using recurrent or dense pulse synthesis to recover
missing central phases must be rejected unless it supplies this quantitative
pair. A new independent central control changes the target dimension of the
orbit and can remove the density bottleneck; merely waiting longer cannot.
