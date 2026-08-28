# Kato Kernel–Detector Parallel Transport

## Question

Can a canonical connection transport the actual portal kernel and its detector
evaluation through the gapped threshold family that defeated the equivariant
index in WP868?

## Claim boundary

For the WP868 family

\[
D_t=(\sin t,\cos t),
\qquad
k_t=(\cos t,-\sin t)^T,
\qquad
P_t=k_tk_t^*,
\]

the Kato generator is

\[
A_t=[\dot P_t,P_t]
=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

The initial-value problem

\[
\dot U_t=A_tU_t,
\qquad U_0=I,
\]

has the exact unitary solution

\[
U_t=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

It transports the complete marked complex:

\[
P_t=U_tP_0U_t^*,
\qquad
D_tU_t=D_0.
\]

Therefore Kato transport retains information discarded by the equivariant
index. If the detector row is co-transported by

\[
e_t=e_0U_t^*,
\]

then

\[
e_tk_t=1
\]

for the whole threshold path. The orthogonal row is transported by the same
unitary, so the complete bright/dark two-port instrument remains lossless.

## Fixed versus co-moving experiments

For a fixed laboratory row \(e_0=(1,0)\), the response is

\[
|e_0k_t|^2=\cos^2t.
\]

At \(\cos t=3/4\), it is \(9/16\), exactly the WP868 attenuation. Kato
transport repairs this only by changing the detector row to \(e_t\). That is
a new relational experiment over the stabilizer of the transported frame
unless the microscopic source independently makes the detector coupling obey
the same Kato equation.

The distinction is essential:

- the projector path canonically determines a mathematical parallelization;
- algebraic availability of \(U_t\) does not make detector control executable;
- a fixed detector does not inherit the co-moving response;
- if the source co-generates \(D_t\) and \(e_t\), the common-frame Gram is
  protected exactly.

For a general complex family, Kato transport may also carry holonomy. A
phase-sensitive readout must retain its reference around the path; only the
intensity Gram is insensitive to a terminal line phase.

## Gate classification

- Portal ray: transported exactly as an embedded kernel, not merely as an
  index class.
- Relative sign: transported relative to the initial marked frame; no absolute
  sign is created.
- Magnitude: the normalized detector Gram is exactly preserved under
  co-transport.
- Basin: WP866's conditional expectation transports covariantly with \(P_t\).
- Threshold: repaired for the entire two-port object conditional on the Kato
  path being the admitted physical matching operation.
- Instrument: mathematically specified but physically unrealized; executable
  detector co-control and 'physical16' calibration remain absent.

## Smallest exact falsifier

At \(\cos t=3/4\), the fixed row has response \(9/16\), while the Kato row has
response \(1\). Both use the same source kernel. This proves that projector
transport alone does not authorize detector transport.

## Disposition

Progressive interface theorem. Kato transport is the first canonical
constructor in this chain that carries the actual kernel projector and full
two-port readout through a gapped threshold. It completes the mathematical
parallelization missing in WP868. It is not yet the physical source principle:
the microscopic flavor model must derive the threshold path, make the detector
coupling follow the same connection, normalize the RG coordinate, and
calibrate the final record in 'physical16' units.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp869_kato_kernel_detector_parallel_transport.py
~~~
