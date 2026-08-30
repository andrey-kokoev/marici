# Reflection-Positive Reconstruction and Selection Audit

## Question

Does a reflection-positive chiral flavor--horizon correlator close WP814's
Euclidean-to-Lorentzian realization gate and simultaneously select the portal
pole, residue, sign, and detector response?

## Admitted favorable domain

The smallest exact positive domain is a one-pole Euclidean correlator

\[
C(\tau)=A e^{-\Delta\tau},
\qquad A>0,quad\Delta>0.
\]

The marked germ retains the source state, operator identity, Euclidean-time
orientation, residue normalization, pole location, and comparison port to the
horizon frequency carrier. Physical time is not assigned to \(\tau\); a
separate reconstruction and detector realization must construct Lorentzian
time.

## Exact reflection positivity and reconstruction

For positive Euclidean arguments \(\tau_i\), the reflection kernel is

\[
C(\tau_i+\tau_j)
=A e^{-\Delta\tau_i}e^{-\Delta\tau_j}.
\]

It is an outer-product Gram matrix and hence positive semidefinite. The
correlator is completely monotone:

\[
(-1)^k C^{(k)}(\tau)
=A\Delta^k e^{-\Delta\tau}>0.
\]

On the declared one-pole domain, its first two exact moments reconstruct the
complete spectral packet:

\[
m_0=A,
\qquad
m_1=A\Delta,
\qquad
A=m_0,
\qquad
\Delta=\frac{m_1}{m_0}.
\]

Thus reflection-positive Euclidean data can support a faithful Lorentzian
spectral realization once the state domain and reconstruction theorem are
declared. This repairs WP814's raw analytic-continuation ambiguity on the
one-pole domain.

## Reconstruction is not selection

Every \(A>0\) and \(\Delta>0\) passes the same positivity test. In particular,
the horizon attachments \(\Delta=\kappa\) and \(\Delta=2\kappa\) are both
reflection-positive. Positivity reconstructs whichever pole the source
supplies; it does not choose one.

A signed operator transformation \(O\mapsto-O\) also leaves the two-point
function invariant because the correlator is quadratic. Therefore this probe
is blind to the portal sign. A source-derived odd interference correlator or
three-point function is required to carry orientation.

Positive threshold shifts \(\Delta\mapsto\Delta+\delta\) preserve complete
monotonicity while changing the reconstructed pole. Reflection positivity is
therefore not numerical threshold protection.

## Finite-probe hostile pair

Even within positive spectral measures, two moments are faithful only after
the one-pole domain has been independently authorized. The unit point mass at
energy one and equal weights at energies \(1/2\) and \(3/2\) share

\[
(m_0,m_1)=(1,1)
\]

but have \(m_2=1\) and \(m_2=5/4\). Thus finite fiber does not mean singleton
fiber. The extra domain restriction cannot be inferred from the two measured
moments.

## Aspect germ and instrument

The reconstructed correlator target is ternary:

```text
horizon thermal germ
flavor operator and state germ
OS reconstruction/comparison cell
```

The calibrated physical record remains quaternary after adding a detector
realization germ. A line detector would return an energy coordinate and an
area coordinate schematically as

\[
R_E=s_E\Delta,
\qquad
R_A=s_A A.
\]

Without independent calibration, the exact source--gain pairs
\((\Delta,s_E,A,s_A)=(1,2,1,2)\) and \((2,1,2,1)\) give the same record. The
response has rank two on four coordinates.

## Contextual partition and classification

- Declared positive one-pole domain plus complete correlator: faithful spectral
  reconstruction.
- General positive spectral domain plus two moments: nontrivial fiber.
- Reflection-positive two-point family: blind to portal sign.
- Positive threshold pole shifts: remain admissible but change prediction.
- Uncalibrated line detector: source scale and gain remain paired.

OS positivity is a realization and reconstruction condition. It is neither a
source selector, sign selector, threshold protector, nor calibration principle.

## Smallest falsifiers and Deutschian appraisal

The smallest selection falsifier is the pair
\(A e^{-\kappa\tau}\), \(A e^{-2\kappa\tau}\): both are equally
reflection-positive. The smallest finite-readout falsifier is the one-pole and
two-pole moment pair above. The smallest sign falsifier is \(O\) versus \(-O\),
which has the same two-point function.

Reflection positivity explains why a Euclidean correlator admits a unitary
spectral realization. It does not explain why Nature chose its pole, residue,
or orientation. The next source must add an independently derived odd
correlator whose incidence selects a unique chiral pole and whose normalization
is protected under thresholds. The same operator must couple to a calibrated
detector; otherwise reconstruction and observation remain separate cells.

## Assumptions and falsifiers

The positive reconstruction theorem is restricted to the declared one-pole
domain. A broader OS reconstruction requires the complete OS axioms and growth
conditions. A source action that uniquely fixes a reflection-positive odd
spectral packet, including pole, residue, sign, and detector coupling, would
falsify the negative selector conclusion.

Primary sources: Osterwalder and Schrader, [Axioms for Euclidean Green's
Functions](https://doi.org/10.1007/BF01645738) and [Axioms for Euclidean
Green's Functions II](https://doi.org/10.1007/BF01608978).

## Disposition

Progressive for realization, negative for selection. Reflection positivity
closes the raw continuation kernel on an independently declared one-pole
domain but leaves portal sign, pole, residue, threshold value, and detector
calibration unselected.
