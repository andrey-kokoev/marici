# SO(5) anomaly-quantization type no-go: WP744

## Question

Can anomaly inflow or a quantized five-dimensional Chern–Simons coefficient
fix the boundary contrast (b-a) left free by WP743?

## Cubic invariant gate

An ordinary five-dimensional gauge Chern–Simons form requires an invariant
symmetric cubic tensor. For generators (T_a), its local coefficient is built
from

\[
d_{abc}=\operatorname{tr}\bigl(T_a\{T_b,T_c\}\bigr).
\]

The exact checker evaluates all (10^3) components for the (SO(5)) vector
generators and independently for a four-dimensional Clifford spinor
realization. Every component vanishes. This is not an artifact of the checker:
the same calculation detects

\[
d_{888}=-\frac{1}{2\sqrt3}
\]

for an (SU(3)) comparator.

The diagonal (SO(3)) boundary triplet is real, and all (3^3) components of
its cubic tensor also vanish. Thus neither the minimal bulk algebra nor the
boundary algebra supplies the perturbative anomaly polynomial needed to
quantize the free scalar contrast.

Five-dimensional supersymmetric Chern–Simons actions can be generated when
the required invariant exists; their existence is not automatic for every
gauge algebra. See [Kuzenko](https://arxiv.org/abs/hep-th/0609078).

## Operator-type gate

There is a second, independent obstruction. Dimensional reduction of a
five-dimensional gauge Chern–Simons term produces a four-dimensional response
of the schematic form

\[
A_5 F\wedge F.
\]

It is linear in the Wilson-line scalar and parity odd. The required flavor
portal is CP even and quadratic in both the flavor carrier and the Higgs
packet. Quantization of the former coefficient therefore would not select the
latter coefficient without an additional typed constructor. A distinguishing
topological response is not the desired scalar operation.

## Surviving fiber

The most general diagonal-(SO(3))-invariant boundary quadratic form remains

\[
K_{\partial}=\operatorname{diag}(a,a,a,b),
\qquad
\Delta_{\partial}=b-a.
\]

Neither (SO(5)) nor (SO(3)) perturbative anomaly data constrain this
continuous difference. Setting it equal to a quantized topological coefficient
would be an extra identification, not anomaly matching.

## Disposition

The minimal anomaly-inflow branch closes twice. The required cubic invariant
is absent, and the reduced Chern–Simons observable has the wrong operator type.
This mechanism is neither an asymmetric portal selector nor a portal
rigidifier.

The result covers ordinary local perturbative gauge anomalies and
Chern–Simons inflow. It does not exclude global anomalies, larger groups,
discrete torsion, or nonlocal holonomies. Those successors must still prove
that their reduced operation lands in the CP-even portal, fixes its magnitude
and clock, survives thresholds, and has a calibrated physical16 instrument.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp744_so5_anomaly_quantization_type_no_go.py`.

Generated result:
`results/wp744_so5_anomaly_quantization_type_no_go.json`.
