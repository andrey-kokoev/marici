# Wavefunction-to-correlator phase-kernel audit

## Frozen primary source

P. Benincasa and G. Dian, *The Geometry of Cosmological Correlators*,
arXiv:2401.05207v1.

## Source-derived comparison

- Equation (1.1) defines observables by integrating `|Psi[Phi]|^2 f[Phi]`.
- Equation (2.6) defines the normalized probability distribution from
  `|Psi[Phi]|^2`.
- Equations (2.8)--(2.10) derive equal-time boundary observables and field
  correlators from that probability distribution.
- The abstract and Section 4 identify weighted cosmological polytopes as a
  first-principles correlator geometry whose triangulations include both the
  in-in representation and the wavefunction-coefficient representation.

Thus this paper supplies the upstream wavefunction-to-correlator comparison
missing from arXiv:2408.16386 alone.

## Phase kernel

For any source-dependent global state-line phase,

\[
\Psi[\Phi]\longmapsto e^{i\gamma}\Psi[\Phi],
\]

one has

\[
|e^{i\gamma}\Psi[\Phi]|^2=|\Psi[\Phi]|^2.
\]

Therefore every observable of the source-defined class

\[
\langle f[\Phi]\rangle
=N\int D\Phi\,|\Psi[\Phi]|^2f[\Phi]
\]

annihilates the state-line Berry holonomy. The weighted-correlator map is
well typed, but the phase line lies in its kernel.

This does not contradict the transverse Keldysh response of Entry 2107. That
response differentiates a protocol difference before restricting to the
equal-source diagonal. Ordinary equal-time field correlators are diagonal
readouts after the modulus-square gluing.

## Narrow consequence

The state-line phase is not activated by the standard three-site equal-time
correlator sector. A physical cosmological activation would require a
source-derived observable outside the diagonal `f[Phi]` class—for example a
protocol-response observable, an off-diagonal density-matrix probe, or a
coherent comparison of background histories.

