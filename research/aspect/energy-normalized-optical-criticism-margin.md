# Energy-normalized optical criticism margin

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact finite metric-authority hostile

## Physical experiment

Prepare two coherent optical displacement modes. Source energy supplies the
actuation metric

\[
G_S=I.
\]

After shot-noise whitening, the calibrated quadrature readout has gains

\[
L=\begin{pmatrix}1&0\\0&1/5\end{pmatrix}.
\]

The second-mode loss may represent overlap, attenuation, or detector coupling,
but its physical origin and calibration must be declared. The energy-normalized
criticism margin is \(1/5\).

## Coordinate hostile

Rescale the second source coordinate by \(1/5\). The displayed readout matrix
becomes identity. If the source metric is silently reset to Euclidean, the
reported margin becomes one—an apparent fivefold improvement with no change
to the apparatus.

Transporting the energy metric correctly gives

\[
G'_S=\operatorname{diag}(1,25),
\]

and the generalized actuation-to-observation margin remains \(1/5\).
Coordinate normalization can improve presentation but cannot improve physical
criticizability.

## Genuine repair

Add an independently source-authorized reference row that observes the second
physical mode at unit gain. The enlarged experiment has a margin at least one
in the original energy metric. Unlike coordinate rescaling, this repair
changes the context, apparatus, noise budget, and cost.

The report must therefore distinguish:

- invariant margin under a transported source metric;
- algebraic availability of the extra row;
- executable cost and uncertainty of its physical implementation.

## Deutsch boundary

The fixture makes a source-significant unit-energy difference predict a
bounded detector consequence. It is still an instrument theorem, not an
explanation of why a particular source law holds. Its explanatory use is to
prevent a coordinate-dependent singular value from masquerading as improved
criticism.

## Reproduction

Run:

    python research/aspect/checkers/energy_normalized_optical_criticism_margin.py

