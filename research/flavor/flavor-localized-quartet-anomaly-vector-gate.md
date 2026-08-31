# Localized-quartet anomaly-vector gate: WP1067

## Question

What complete globally vanishing anomaly vector does the one-quartet
localization require?

## Channels and normalization

Use

\[
A(4)=1,
\qquad
T(\Box)=\frac12.
\]

The admitted channels are the five perturbative channels whose full
\(15+2\overline6\) anomaly vanishes:

\[
SU(4)^3,\qquad
SU(4)^2U(1),\qquad
SU(2)^2U(1),\qquad
U(1)^3,\qquad
U(1)\,{\rm grav}.
\]

The gauge-gravity \(SU(4)\) and \(SU(2)\) channels are not admitted here:
their full subgroup indices are both \(3\), so an external Green–Schwarz or UV
completion is required before local inflow can be tested.

## Exact inflow vectors

For a boundary packet at endpoint \(0\), local cancellation in each channel
uses

\[
A_0=b+\frac B2+k,
\qquad
A_\pi=\frac B2-k.
\]

In the displayed channel order, the exact vectors are:

\[
\begin{array}{l|r}
\text{localization} & k_{\rm CS}\\
\hline
\text{one quartet} &
\left(\frac12,\frac14,0,2,2\right)\\[2mm]
\text{one quartet, reflected} &
\left(-\frac12,-\frac14,0,-2,-2\right)\\[2mm]
2_a+2_b,\; C=23,k=0 &
(0,0,-1,-16,-4)\\[2mm]
8,\; C=19 &
\left(-1,\frac12,1,4,4\right)\\[2mm]
1,\; C=26 &
(0,0,0,32,2)
\end{array}
\]

Thus the one-quartet cell needs a multicomponent shifted quantization law.
The port-destroying \(C=23\) doublet-pair cell is integral on all admitted
channels.

## Boundary

The next source must derive the shifted Chern–Simons vector and complete the
nonzero \(SU(4)\)-gravity and \(SU(2)\)-gravity channels from the UV theory.
This packet neither proves nor excludes such a shifted lattice.

## Classification

Complete vanishing-channel anomaly-vector gate. It upgrades WP1066's single
half-integral cubic requirement to the exact vector
\((1/2,1/4,0,2,2)\).

Checker: `research/flavor/checkers/wp1067_localized_quartet_anomaly_vector_gate.py`

Result: `results/wp1067_localized_quartet_anomaly_vector_gate.json`
