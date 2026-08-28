# Ward-Spectral Positive Functional Has a Scale Fiber

## Question

Can WP834's neutral kernel be repaired by adding a positive spectral term to
the Ward pairing?

## Combined positive functional

Consider

\[
F_\alpha(Q,D)
=\operatorname{Tr}Q^2+\alpha\operatorname{Tr}D^2,
\qquad \alpha>0.
\]

For the WP833 base and WP834 neutral completion,

\[
\begin{array}{c|cc}
&\operatorname{Tr}Q^2&\operatorname{Tr}D^2\\
\hline
\text{base}&14&9\\
\text{neutral completion}&14&22
\end{array}
\]

At one common spectral scale, the functional detects and penalizes the neutral
completion. This repairs the Ward kernel algebraically.

## Independent spectral-scale fiber

Operator irreducibility survives \(D\mapsto\lambda D\) for every
\(\lambda>0\). The neutral-completion score is

\[
F_4(\lambda)=14+22\alpha\lambda^2.
\]

It is strictly increasing, approaches 14 as \(\lambda\to0^+\), and has no
stationary point at positive scale. Its infimum is not an irreducible finite-
scale minimizer.

More sharply, the base at unit scale and the neutral completion at

\[
\lambda=\frac3{\sqrt{22}}
\]

have exactly the same score \(14+9\alpha\) for every \(\alpha>0\). Thus the
combined functional compares spectra only after their clocks have already
been parallelized.

The transformation

\[
D\mapsto cD,
\qquad
\alpha\mapsto\frac{\alpha}{c^2}
\]

also leaves the spectral contribution unchanged. The relative coefficient is
an inverse-square clock, not a dimensionless order supplied by positivity.

## Stabilizing the scale moves the freedom

Adding an inverse-spectral term gives

\[
G(\lambda)=14+22\alpha\lambda^2
+\frac{37\beta}{16\lambda^2}.
\]

Its stationary scale satisfies

\[
\lambda^4=\frac{37\beta}{352\alpha}.
\]

The scale is now selected only after the positive coefficient ratio
\(\beta/\alpha\) is supplied. Likewise, imposing a lower spectral gap makes
the monotone functional choose the imposed boundary. Neither operation derives
the clock.

## Instrument and selector classification

At fixed common scale and fixed \(\alpha\), the functional is faithful to the
displayed neutral completion. No admitted physical experiment measures the
Ward-current and finite-Dirac terms in one calibrated relative metric.

Therefore the candidate is a conditional comparison functional and spectral
rigidifier. It does not yet select a full source spectrum, portal magnitude,
RG basin, threshold descendant, or physical readout.

## Smallest exact falsifier

The base packet at scale one and neutral completion at scale
\(3/\sqrt{22}\) have identical \(F_\alpha\) for every positive \(\alpha\).
This isolates the missing constructor as a common source clock, not another
positive term.

## Disposition

Negative scale-selection result with a progressive conditional pairing. A
complete source must derive the charged-neutral relative metric and spectral
clock, prove a unique global minimizer over physical completions, and carry it
through RG, thresholds, and one common instrument.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp835_ward_spectral_positive_functional_scale_fiber.py
```
