# The ring geometry does not lock continuous spin memory to the sevenfold discriminant

## Candidate endogenous lock

The strongest available normalization mechanism uses the same circular
apparatus that defines spin memory.  A ring of radius \(L\) has orbit scale
\(L\), while the source formula contains

\[
\Delta^+u=
\frac{1}{2\pi L}
\int du\oint_C
\left(D^zC_{zz}\,dz+D^{\bar z}C_{\bar z\bar z}\,d\bar z\right).
\]

One might hope that a ring mode supplies \(\omega_n=n/L\), making
\(\omega_n\Delta^+u\) an endogenous dimensionless phase.

## First failure: the source apparatus does not select one optical mode

The grounded source specifies counter-orbiting light pulses, mirrors or fiber
optics, and an interference-fringe shift.  It does not identify the optical
carrier frequency with the inverse ring radius.  Even an ideal ring resonator
has a family of longitudinal modes, not one preferred mode.  Hence the ring
geometry supplies a scale family rather than the required unique lock.

## Decisive failure: continuous amplitude survives any ring-mode choice

More importantly, the radiative source space is a real vector space.  If a
magnetic shear \(C\) is admissible, then \(sC\) is admissible in the linearized
source theory for real \(s\), and

\[
\Delta^+u[sC]=s\Delta^+u[C].
\]

For any fixed nonzero ring frequency, therefore,

\[
s\longmapsto
\exp\left(i\omega_n\Delta^+u[sC]\right)
\]

has continuous image in \(U(1)\).  It is not confined to \(\mu_7\).  The
seventh roots can be sampled by choosing seven amplitudes, but that selection
is not closed under the source's scalar constructors and is not source
generated.

Equivalently, a continuous map from the connected source line
\(\mathbb R C\) into the discrete subgroup \(\mu_7\) must be constant.  A
nonconstant sevenfold character requires the admissible amplitude line itself
to be replaced by or reduced along an integral lattice.

## Why the determinant seven does not supply amplitude quantization

The determinant

\[
\det F=-7
\]

classifies an index-seven defect in the integral affine presentation lattice.
It does not assert that physical shear amplitudes occur in seventh-integer
units.  Mapping the discriminant generator to a specially normalized shear
is an additional comparison morphism.  Choosing that morphism so that one
generator produces phase \(e^{2\pi i/7}\) fits precisely the desired answer.

Thus the two appearances of seven remain correctly typed but unconnected:

- presentation side: the finite cokernel \(D_F\cong\mathbb Z/7\);
- instrument side: an arbitrarily selectable seven-point subset of a
  continuous interference circle.

## Minimal theorem now required

The required source theorem is stronger than frequency locking:

```text
QuantizedSpinMemoryComparison
  integral affine discriminant D_F
  admissible magnetic source lattice Lambda_mag
  comparison D_F -> Lambda_mag^dual / Lambda_mag
  normalized interference character
  compatibility with source scalar constructors
  authority_root
```

It must either quantize normalized magnetic amplitudes or provide a compact
gauge quotient that makes the seven selected phases intrinsic.  Ring geometry
and complex coefficients do neither.

## Falsifier outcome

The proposed endogenous geometric lock is rejected.  Even after imposing the
most favorable ring-mode relation, continuous source rescaling moves the
phase away from \(\mu_7\).  The obstruction is therefore not the absence of a
dimensionless phase.  It is the absence of a source-authorized discrete
magnetic amplitude lattice and its comparison with the affine discriminant.
