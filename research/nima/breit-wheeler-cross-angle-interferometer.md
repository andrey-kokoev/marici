# Minimal experimental repair of the Breit-Wheeler phase obstruction

Independent angular bins measure only diagonal kernels. To recover the
cross-angle quantity

\[
K(\theta,\theta')=A(\theta)A(\theta')^*,
\]

one must coherently recombine the corresponding outgoing pair-momentum modes
before detection. For a controlled phase \(\phi\), measure

\[
P_\phi=\left|A(\theta)+e^{i\phi}A(\theta')\right|^2.
\]

Four settings give the exact reconstruction

\[
\operatorname{Re}K=\frac{P_0-P_\pi}{4},
\qquad
\operatorname{Im}K=\frac{P_{\pi/2}-P_{3\pi/2}}{4}.
\]

Applied entrywise after incoming-polarization and outgoing-spin selection,
this supplies the kernel missing from a nonforward unitarity relation.

The result establishes algebraic sufficiency, not practical feasibility. Its
physical demand is severe: a unitary charged-particle optical system must
preserve coherence between distinct MeV electron-positron momentum modes and
provide a calibrated phase shift. Ordinary tracking detectors destroy rather
than recombine those modes.

The conceptual conclusion is nevertheless clean: the missing Marici datum is
not “more angular resolution.” It is a coherent comparison morphism between
angular fibers.

Reproduce with
`research/nima/check_breit_wheeler_cross_angle_interferometer.py`.
