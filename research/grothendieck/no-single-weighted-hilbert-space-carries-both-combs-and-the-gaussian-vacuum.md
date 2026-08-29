# No Single Weighted Hilbert Space Carries Both Combs and the Gaussian Vacuum

## Two logarithmic combs

In the logarithmic carrier coordinate \(q\), the direct comb trace is

\[
B_+\psi
=
\sum_{n\geq1}
n^{-1/2}\psi(\log n).
\]

Reciprocal reflection produces the opposite trace

\[
B_-\psi
=
\sum_{n\geq1}
n^{-1/2}\psi(-\log n).
\]

Consider a weighted Sobolev realization whose local packet norm near \(q=R\)
scales like

\[
w(R)^{1/2}.
\]

## Weight forced by trace continuity

A fixed compact packet translated to \(R\) has direct comb trace of size

\[
e^{R/2}.
\]

Continuity of \(B_+\) therefore forces

\[
w(R)\gtrsim e^R
\qquad
(R\longrightarrow+\infty).
\]

Applying the same argument to \(B_-\) forces

\[
w(R)\gtrsim e^{-R}
\qquad
(R\longrightarrow-\infty).
\]

Thus any single symmetric weighted Hilbert realization controlling both traces
must grow at least like

\[
w(q)\gtrsim e^{|q|}.
\]

## Gaussian vacuum lies at the excluded threshold

The logarithmically unitarized Gaussian vacuum is

\[
\psi_+(q)
=
e^{q/2}e^{-\pi e^{2q}}.
\]

As \(q\) tends to negative infinity,

\[
|\psi_+(q)|^2\sim e^q.
\]

Against a weight satisfying \(w(q)\gtrsim e^{-q}\), the weighted density obeys

\[
w(q)|\psi_+(q)|^2\gtrsim1.
\]

Its integral diverges at the negative end. Hence \(\psi_+\) is excluded from
every such Hilbert space.

The reflected vacuum

\[
\psi_-(q)=\psi_+(-q)
\]

is excluded at the positive end by the same argument.

## Structural no-go

No single ordinary weighted Hilbert space can simultaneously:

- contain both source vacua as finite-norm states;
- make both logarithmic comb traces continuous;
- retain the natural two-sided carrier coordinate.

This is not a poor choice of weight. The source decay exponent and the comb
density meet exactly at the nonintegrable threshold.

## Required architecture

The faithful object must remain sector-split:

- a direct rigging containing \(\psi_+\) and its direct trace;
- a reciprocal rigging containing \(\psi_-\) and its reciprocal trace;
- an interface or relative pairing that sews them without demanding that all
  data inhabit one Hilbert norm.

The Gaussian vacuum must appear as a boundary or distributional state at the
opposite end of each sector. This gives an analytic reason for retaining the
primitive boundary current rather than completing it away.

## Scope boundary

The no-go selects the category in which an arithmetic extension must live. It
does not construct the relative determinant or prove zero confinement.

## Falsifier

A counterexample would be one weight \(w\) for which both comb traces are
continuous and both \(\psi_+\) and \(\psi_-\) have finite weighted norm. The
translation lower bounds and endpoint asymptotics exclude such a weight in
the stated local weighted-Sobolev class.
