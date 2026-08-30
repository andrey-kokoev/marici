# Physical16 Gramian pullback gate

Work package: WP557  
Owner: marici.Figueiredo

## Question

Does WP556's six-state positive pairing define a faithful geometry or selector
on the sixteen-dimensional physical flavor quotient?

## Domain mismatch

WP556 is defined on the minimal realization of one frozen aligned source
resolvent. The faithful flavor quotient is the generic nondegenerate
`physical16` domain. A descent would require a source-derived smooth map

\[
\phi:\mathrm{physical16}\longrightarrow\mathbb R^6
\]

and its Jacobian \(J_\phi\). No such map is currently admitted.

Even if it existed, pulling back the positive Gramian metric gives

\[
G_{16}=J_\phi^T G_6J_\phi.
\]

Since \(J_\phi\) has six rows,

\[
\operatorname{rank}G_{16}\leq6,
\qquad
\dim\ker G_{16}\geq10.
\]

Thus the six-state pairing cannot by itself separate generic `physical16`
points or define a faithful quotient metric.

## Complementarity with measured ten

Let \(P_{10}\) denote the measured-ten projection. A six-row source probe can
repair its missing directions only if

\[
\operatorname{rank}
\begin{pmatrix}P_{10}\\J_\phi\end{pmatrix}=16.
\]

The checker gives two exact hostiles:

- if \(J_\phi\) factors through measured ten, the stacked rank remains ten
  and its kernel has dimension six;
- if its six rows are exactly complementary, the stacked rank is sixteen.

Dimension counting therefore permits repair but does not authorize it.
Complementarity must be derived from the flavor source and measured with a
physical instrument.

## Hostile physical pair

WP52 already supplies two physically inequivalent `physical16` points with
identical measured ten coordinates. In the local normal form, a displacement
along any missing coordinate lies in \(\ker P_{10}\). The factor-through
six-state probe also annihilates it, whereas the complementary witness detects
it exactly.

## Selector test

A separating pullback would still be a readout. Neither full stacked rank nor
a positive metric removes a physical point from the admissible family. Source
selection requires an additional fixed-locus, image, or stationarity law that
is transverse to an admitted physical direction.

The smallest exact falsifier of present descent is the rank bound: every
six-row pullback metric has at least a ten-dimensional local kernel. The
smallest repair certificate is stacked rank sixteen with an independently
derived \(J_\phi\).

## Status

WP557 closes promotion of WP556 to a faithful `physical16` operation. The
Gramian is a source-side rigidifier on one internal realization. It is neither
a physical16 selector nor a standalone faithful probe.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp557_physical16_gramian_pullback_gate.py

The generated result is
research/flavor/results/wp557_physical16_gramian_pullback_gate.json.
