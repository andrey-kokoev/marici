# Chiral Gauge Conjugation-Closure Audit

## Question

Can microscopic chiral gauge consistency evade WP809 by admitting one chiral
source while excluding its conjugate, thereby making the asymmetric flavor
portal unavoidable?

## Source grammar and faithful quotient

The admitted grammar contains four-dimensional chiral gauge representations,
gauge-invariant Yukawa hyperedges, anomaly cancellation, perturbative RG, and
mass thresholds. Its concrete hostile packet is one Standard Model generation
written entirely with left-handed Weyl fields:

\[
(Y_Q,Y_{u^c},Y_{d^c},Y_L,Y_{e^c})
=\left(\frac16,-\frac23,\frac13,-\frac12,1\right).
\]

The conjugation functor sends each representation to its complex conjugate,
each abelian charge \(Y\) to \(-Y\), and each complex coupling to its complex
conjugate. The faithful flavor orientation remains

\[
J=\operatorname{Im}\det[H_u,H_d].
\]

This is a full weak-basis invariant; it must not be replaced by a texture
phase. The physical source quotient must therefore include the action of
conjugation on the complete chiral theory, separately from literal matrices,
texture rephasings, chart permutations, and equality of any selected
observables.

## Exact Standard Model hostile pair

The mixed, gravitational, abelian cubic, and color cubic anomaly equations are

\[
\begin{aligned}
2Y_Q+Y_{u^c}+Y_{d^c}&=0,\\
3Y_Q+Y_L&=0,\\
6Y_Q+3Y_{u^c}+3Y_{d^c}+2Y_L+Y_{e^c}&=0,\\
6Y_Q^3+3Y_{u^c}^3+3Y_{d^c}^3+2Y_L^3+Y_{e^c}^3&=0,\\
2A(3)-A(\bar3)-A(\bar3)&=0.
\end{aligned}
\]

Every linear or cubic anomaly changes sign under full conjugation, so zero
maps to zero. Quadratic Dynkin data and squared abelian charges are unchanged.
The four weak doublets per generation remain even. Gauge consistency therefore
admits both the displayed source and its fully conjugated source.

Yukawa incidence does not break the pair. With Higgs orientations
\(Y_{H_u}=1/2\) and \(Y_{H_d}=-1/2\), the three charge sums

\[
Y_Q+Y_{H_u}+Y_{u^c},\qquad
Y_Q+Y_{H_d}+Y_{d^c},\qquad
Y_L+Y_{H_d}+Y_{e^c}
\]

all vanish, and their fully conjugated sums vanish as well.

## RG, threshold, and portal consequences

Perturbative beta functions constructed from real group invariants and
polynomials in couplings and their conjugates are equivariant under complex
conjugation. Thus a flow and its conjugate share fixed-point eigenvalues,
basin dimensions, and crossover scales. Conjugate mass matrices have identical
singular values and therefore identical mass thresholds.

A faithful CP-odd invariant reverses:

\[
J\longmapsto-J.
\]

Likewise a genuinely signed portal contrast obeys

\[
g_n-g_m\longmapsto-(g_n-g_m),
\]

while its magnitude, CP-even spectrum, and quadratic RG data are unchanged.
The chiral grammar consequently supplies two physically oriented constructors,
not a unique one.

## Contextual partition and instrument

- Gauge and anomaly probes put the two constructors in the same admissible
  consistency class.
- CP-even spectra and thresholds collapse them.
- A faithful signed CP probe separates them after an experimental orientation
  convention is fixed.
- Choosing only one conjugation sector restricts the source category to a
  stabilizer experiment; it is not a result of anomaly cancellation.
- No admitted operation calibrates the signed readout directly in `physical16`
  detector units or chooses its source member.

The source is therefore a chiral rigidifier and can support a signed physical
readout, but it is neither an absolute selector nor a complete instrument.

## Smallest exact falsifier

One Standard Model generation and its fully conjugated generation are the
smallest phenomenologically relevant hostile pair. Both satisfy every tested
anomaly and Yukawa-incidence equation. They share quadratic running data and
mass thresholds but carry opposite \(J\) and opposite signed portal contrast.

## Deutschian appraisal

Gauge consistency explains why charges within either chiral packet fit
together. It does not explain why the packet rather than its conjugate is
realized. The conjugation functor makes this failure structural and hard to
vary: adding further homogeneous anomaly equations, CP-even potentials, or
ordinary mass thresholds preserves the pair.

The next candidate must identify a source principle whose admitted category is
not closed under full conjugation. Merely deleting the conjugate theory by
definition is not explanatory. The required asymmetry must arise from an
independently physical structure—potentially an oriented non-equilibrium
preparation or a non-invertible boundary condition—and that same structure
must define the detector orientation and calibration. Otherwise it is another
reference port.

## Assumptions and falsifiers

The conclusion assumes the microscopic source grammar is closed under full
complex conjugation and that RG and thresholds use the ordinary real group
invariants. A source-derived, unitary chiral constructor with no conjugate
object in its admitted category would falsify the closure premise. To count as
the desired explanation it must also fix the portal magnitude, RG trajectory,
threshold state, and calibrated `physical16` instrument.

Primary background: Alvarez, Gracia-Bondia, and Martin,
[Anomaly Cancellation and Gauge Group of the Standard Model in
NCG](https://arxiv.org/abs/hep-th/9506115), and Shi and Shrock,
[Chiral Gauge Theories](https://arxiv.org/abs/1510.07663).

## Disposition

Negative but progressive. Anomaly-complete microscopic chirality is not by
itself a non-mirror-completable source. The remaining frontier must break
conjugation closure through a physically derived constructor that also carries
the portal and its instrument.
