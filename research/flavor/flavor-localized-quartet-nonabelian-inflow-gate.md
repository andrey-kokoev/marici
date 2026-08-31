# Localized-quartet non-Abelian inflow gate: WP1066

## Question

Does the non-Abelian \(SU(4)\) cubic anomaly constrain WP1056's one-quartet
localization?

## Cubic anomaly packet

Normalize

\[
A(4)=1,
\qquad
A(\overline4)=-1.
\]

For the \(SU(4)\times SU(2)\) branches,

\[
A(6)=0,
\qquad
A(4,2)=2,
\qquad
A(1)=0,
\]

and \(SU(2)\) has no perturbative cubic anomaly. The full WP1056 family is
consistent:

\[
A(15)+2A(\overline6)=2+2(-1)=0.
\]

## One-quartet inflow

Localizing one \(\overline4\) branch gives boundary anomaly \(-1\) and bulk
anomaly \(B=1\). The fixed-point equations are

\[
A_0=-1+\frac12+k_{\rm CS},
\qquad
A_\pi=\frac12-k_{\rm CS}.
\]

Hence

\[
k_{\rm CS}=\frac12.
\]

At the reflected endpoint, the required level is \(-1/2\).

An integral \(SU(4)\) Chern–Simons lattice therefore rejects the one-quartet
cell. A shifted or half-integral class can admit it.

## Exact hostiles

The port-destroying \(C=23\) cell obtained by localizing both doublets has

\[
A_{\partial}=0,
\qquad
B=0,
\qquad
k_{\rm CS}=0,
\]

so it is compatible with an integral lattice but retains no ports.

Localizing the bifundamental \(8\) instead gives

\[
A_{\partial}=2,
\qquad
B=-2,
\qquad
k_{\rm CS}=-1,
\]

but has \(C=19\), failing the WP1036 capacity point.

## Boundary

This packet computes the \(SU(4)\) cubic channel only. WP1057's linear
\(U(1)\) result remains separate. The next source must derive a shifted or
half-integral \(SU(4)\) Chern–Simons class and endpoint orientation, and then
compute the complete mixed and gravitational anomaly lattice.

## Classification

Non-Abelian inflow gate. It sharpens the localization blocker from an unfixed
integer cofiber to a concrete shifted-quantization requirement.

Checker: `research/flavor/checkers/wp1066_localized_quartet_nonabelian_inflow_gate.py`

Result: `results/wp1066_localized_quartet_nonabelian_inflow_gate.json`
