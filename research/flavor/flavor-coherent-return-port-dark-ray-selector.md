# Coherent Return-Port Dark-Ray Selector

## Question

Can the terminated return edge of WP854 derive WP857's odd reservoir target,
rather than placing the desired parity directly into the jump operators?

## Retained return-port phase

Let (A,B) denote the two boundary path amplitudes. The removed unitary return
edge carries a unit phase (z). Retaining that edge as a monitored reference
port defines the normalized common-port row

\[
M_z=\frac1{\sqrt2}(1,z),
\qquad |z|=1.
\]

The unique normalized dark ray is

\[
d_z=\frac1{\sqrt2}(-z,1)^T,
\qquad M_zd_z=0.
\]

Thus equal magnitude and destructive relative phase follow from the kernel of
one rank-one coherent termination. They are not fitted scalar coefficients.

The equivalent boundary-link Hamiltonian is

\[
K_z=
\begin{pmatrix}
0&z\\
\overline z&0
\end{pmatrix}.
\]

Its eigenvalues are (-1,+1), and (d_z) is its nondegenerate negative
eigenray. A zero-temperature relaxation derived from this spectral ordering
has precisely the odd target used in WP857.

## Gauge covariance and changed groupoid

Under independent port rephasings, both (z) and (d_z) transform. The ray
is therefore covariant, not an absolute phase choice. Once the return port is
retained as a coherent reference, the physical groupoid is reduced to the
stabilizer of its phase. WP855's sign becomes relative to this same port.

If the terminated edge is discarded rather than monitored coherently, only
the diagonal endpoint projections survive. Their algebra cannot define
(M_z), (K_z), or an off-diagonal dark ray. The reference port is therefore
part of the new experiment, not recovery of an absolute phase from the open
path alone.

## Source-authority boundary

WP854 by itself specifies a removed directed edge but not a rank-one common
junction coupling both path amplitudes to that edge. The coherent termination
is an additional physical constructor. A phase-shifted row

\[
M_{-z}=\frac1{\sqrt2}(1,-z)
\]

selects the orthogonal bright-parity ray while satisfying the same rank and
normalization properties. The actual junction phase must therefore be derived
from the microscopic cycle, not chosen after the portal target is known.

Likewise, converting (K_z) into a relaxation generator requires an ordering
or bath condition. Replacing (K_z) by (-K_z) exchanges the ground and
excited rays. The return-edge phase alone does not fix this Hamiltonian-sign
interface.

## Finite-temperature hostile

At finite inverse temperature 
(\beta), the Gibbs state of (K_z) has both parity sectors. On the exact
slice (e^\beta=2), their weights are

\[
p_-=\frac45,
\qquad
p_+=\frac15.
\]

Its purity is (17/25), and the magnitude of its port coherence is (3/10),
not the pure-ray value (1/2). Exact magnitude and coherent sign therefore
require a vacuum or otherwise pure dark-state reservoir, not generic detailed
balance.

## Classification

Progressive relational parity and magnitude selector conditional on a coherent
common return-port junction and a pure ground-state reservoir. It derives the
WP857 odd ray as a kernel/eigenray and can reuse the same port as WP855's phase
reference. It still requires microscopic authority for the junction phase,
Hamiltonian ordering, RG interpretation, isometric threshold transport, and
detector calibration.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp858_coherent_return_port_dark_ray_selector.py
```
