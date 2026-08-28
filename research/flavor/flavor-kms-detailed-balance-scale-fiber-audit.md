# KMS Detailed-Balance Scale-Fiber Audit

## Question

Can a thermal KMS law derive WP811's reservoir asymmetry and thereby turn the
effective dissipative selector into a complete source explanation?

## Admitted source and physical time

The source is a two-sector system with energy splitting \(\Delta\), weakly
coupled to a reservoir at inverse temperature \(\beta\). The semigroup
parameter is admitted physical time through the weak-coupling reservoir
construction. Downward and upward transition rates obey

\[
\frac{\gamma_\uparrow}{\gamma_\downarrow}
=e^{-\beta\Delta}=q.
\]

Writing \(\gamma_\downarrow=\gamma\), the population generator is

\[
L_{\rm KMS}=
\begin{pmatrix}
-\gamma&\gamma q\\
\gamma&-\gamma q
\end{pmatrix}.
\]

The signed flavor observable is a weak-basis-invariant `physical16`
coordinate \(G=\operatorname{diag}(-g_0,+g_0)\), not a texture phase.

## Exact Gibbs selector

For positive rates the stationary state is unique:

\[
p_*=\frac1{1+q}
\begin{pmatrix}q\\1\end{pmatrix}.
\]

The dissipative gap is \(\gamma(1+q)\), and the stationary orientation is

\[
p_+-p_-
=\frac{1-q}{1+q}
=\tanh\!\left(\frac{\beta\Delta}{2}\right).
\]

Thus detailed balance supplies a genuine global attractor. At infinite
temperature its signed bias vanishes. At zero temperature it selects the
lower-energy sector.

## Where the source choice moves

KMS balance fixes a rate ratio conditional on the Hamiltonian and bath state.
It does not fix the sign of \(\Delta\). Replacing \(\Delta\) by \(-\Delta\)
reverses the stationary orientation while preserving the same detailed-balance
law. The mirror reservoir of WP811 has become a mirror Hamiltonian.

Nor does KMS fix the absolute relaxation scale \(\gamma\). Multiplying both
rates by a positive constant preserves the stationary state and changes the
physical clock. Consequently detailed balance supplies a relation, not a
complete dynamical normalization.

## Magnitude and threshold fibers

The bias depends only on the product \(\beta\Delta\). The exact hostile pair

\[
(\beta,\Delta)=(1,2),\qquad(2,1)
\]

has the same stationary state. Transition-count ratios can identify this
product, while the total count rate can identify \(\gamma(1+q)\); neither
separates temperature from the source splitting without an independent
thermometer or spectrometer.

A threshold correction \(\Delta\mapsto2\Delta\) changes the stationary bias.
The sign survives if the correction does not cross zero, but the predicted
magnitude does not. Threshold survival of a basin is therefore not numerical
survival of the portal.

With detector gain \(s\), the steady record is

\[
R=s g_0\tanh\!\left(\frac{\beta\Delta}{2}\right).
\]

It is rank one on the four coordinates \((\beta,\Delta,g_0,s)\). The portal
normalization and detector gain remain exactly confounded even if the thermal
product has been inferred.

## Contextual partition and classification

- Fixed \((\beta,\Delta,\gamma)\): unique Gibbs attractor and executable
  transition-count instrument.
- Fixed thermal product \(\beta\Delta\): a continuous temperature--splitting
  equivalence class.
- Full Hamiltonian grammar: mirror pair \(\Delta\leftrightarrow-\Delta\).
- Positive threshold corrections: retain the basin but generally change the
  bias magnitude and clock.
- Single calibrated record: three-dimensional local kernel across temperature,
  splitting, portal scale, and gain.

KMS detailed balance is a selector conditional on a signed Hamiltonian. It is
also a relational thermal rigidifier and an executable probe family. It is not
an absolute sign selector, magnitude selector, or complete `physical16`
instrument.

## Smallest exact falsifiers

The mirror Hamiltonians \(\Delta\) and \(-\Delta\) satisfy the same KMS law and
select opposite orientations. The scale pair \((1,2)\) and \((2,1)\) gives the
same thermal state. These independently falsify absolute sign and scale
identification.

## Deutschian appraisal

Detailed balance explains why transition rates, stationary bias, and thermal
response fit together. It improves WP811 by deriving the rate ratio from a
thermal contract. But the answer can still be reversed by changing the signed
Hamiltonian and rescaled by changing \(\beta\Delta\), without violating the
principle. It is therefore not yet the hard-to-vary explanation of the portal.

The next progressive source must derive the signed splitting and the physical
temperature from the same geometry. A horizon or other geometric KMS source
is a concrete candidate because it can normalize temperature. It must still
prove that its orientation is not a black-hole/white-hole or positive-/negative-
frequency reference pair, and must link the geometric scale to \(g_0\) and the
detector response.

## Assumptions and falsifiers

The result assumes a weak-coupling Davies/KMS description with a two-level
nondegenerate Hamiltonian. A geometry that fixes \(\beta\), the sign and value
of \(\Delta\), \(g_0\), and detector gain in one admitted source packet would
falsify the remaining fiber. Merely measuring those quantities independently
would reconstruct the state but would not make them source-selected.

Primary sources: Temme, [Lower Bounds to the Spectral Gap of Davies
Generators](https://arxiv.org/abs/1305.5591), and Guo et al., [Designing Open
Quantum Systems with Known Steady States](https://doi.org/10.22331/q-2025-01-28-1612).

## Disposition

Mixed but negative for the complete objective. Thermal detailed balance derives
the rate ratio and unique Gibbs basin, yet transfers sign authority to the
Hamiltonian and leaves temperature, clock, portal magnitude, and calibration
fibers.
