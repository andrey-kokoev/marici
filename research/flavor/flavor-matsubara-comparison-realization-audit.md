# Matsubara Comparison and Realization Audit

## Question

Can Euclidean horizon regularity construct the primitive frequency-comparison
cell missing from WP813, rather than merely postulating
\(\Delta=n\kappa\)?

## Admitted Euclidean source

The horizon thermal circle has period

\[
\beta=\frac{2\pi}{\kappa}.
\]

Its bosonic and fermionic Fourier modes are

\[
\omega_n^{\rm B}=\frac{2\pi n}{\beta}=n\kappa,
\qquad
\omega_n^{\rm F}=\frac{(2n+1)\pi}{\beta}
=\left(n+\frac12\right)\kappa.
\]

Unlike WP813's free attachment coefficient, these relations follow from the
period and spin structure. The thermal circle therefore supplies a primitive
Euclidean frequency carrier and canonical endpoint attachments.

## What this repairs

At the Euclidean level the comparison germ is now source-defined:

```text
EuclideanHorizonFrequencyGerm
  horizon_identity
  metric_and_state_provenance
  thermal_period
  spin_structure
  Fourier_mode_label
  primitive_frequency_unit
  orientation_mark
```

The dimensionless products are \(2\pi n\) for bosons and
\((2n+1)\pi\) for fermions, so the surface-gravity scale cancels without a
hand-inserted coefficient. This passes WP813's primitive comparison gate for
Euclidean coefficients.

It does not select the mode. Bosonic \(n=0,1,2\) and fermionic
\(n=0,1\) give different biases while obeying the same periodicity and spin
structure. Representation or incidence data must identify which mode couples
to flavor.

## Realization is a separate germ

A Matsubara coefficient is not a physical detector energy gap. The target must
cross from Euclidean frequency to a Lorentzian transition and then to a
calibrated record. Aspect's native arity is therefore:

```text
Euclidean selector target
  horizon thermal germ
  flavor operator germ
  Euclidean frequency-comparison cell

Physical detector target
  all three objects above
  Lorentzian detector-realization germ
```

The first target is ternary. The second is quaternary. Algebraic equality of
the displayed frequencies does not construct the fourth argument.

## Exact raw-continuation hostile pair

Without an admitted growth and positivity class, discrete Matsubara samples
do not determine a real-frequency germ. The analytic function

\[
h_{m B}(z)=\sinh\!\left(\frac{\beta z}{2}\right)
\]

vanishes at every bosonic Matsubara point
\(z=2\pi i n/\beta\), but at the real horizon frequency
\(z=\kappa\) it equals \(\sinh\pi\). Likewise

\[
h_{m F}(z)=\cosh\!\left(\frac{\beta z}{2}\right)
\]

vanishes at every fermionic Matsubara point and equals \(\cosh\pi\) at
\(z=\kappa\).

These functions are exact witnesses for the raw analytic sampling domain.
They are not asserted to satisfy reflection positivity or the full
Osterwalder--Schrader axioms. That distinction is decisive: complete Euclidean
Green functions satisfying the OS axioms and their growth conditions can
reconstruct a Lorentzian theory. The current flavor packet has not supplied
such a source-derived Green-function family, reflection-positive state, or
detector coupling.

## Contextual partition and instrument

- Euclidean thermal circle plus spin structure: canonical Matsubara frequency
  attachment.
- Fixed periodicity without mode incidence: discrete \(n\)-fiber.
- Raw Matsubara samples: nonfaithful continuation quotient.
- Full OS-positive Euclidean theory: potential Lorentzian reconstruction, not
  presently admitted.
- Lorentzian transition detector: separate realization germ.
- `physical16` record: additionally requires weak-basis descent, portal
  normalization, detector gain, and uncertainties.

Even granting the unit bosonic mode, the record

\[
R=s g_0\tanh\pi
\]

retains the exact hostile pair \((g_0,s)=(1,2),(2,1)\).

## Classification and smallest falsifier

Euclidean regularity is a genuine comparison-cell constructor. It is neither
a mode selector nor a physical realization functor. The smallest structural
falsifier is the pair of analytic germs \(0\) and \(h_{m B}\): they agree on
the complete Matsubara tower but differ at a real detector frequency. The
smallest selection falsifier is \(n=1\) versus \(n=2\).

## Deutschian appraisal

The thermal circle explains the otherwise arbitrary coefficient one in
\(\omega_n=n\kappa\). This is hard-to-vary progress: periodicity and primitive
Fourier normalization jointly determine it. But a Euclidean label is not yet
the observed portal. The explanation must also derive why one mode couples,
why its OS reconstruction is physical, and how its Lorentzian operator acts on
the faithful flavor quotient and detector.

The next constructor must therefore be a reflection-positive chiral
flavor--horizon correlator whose spectral measure contains a uniquely selected
mode and whose same coupling defines an Unruh--DeWitt-type physical16
instrument. Only that complete four-object germ can be tested for sign,
magnitude, RG, and threshold survival.

## Assumptions and falsifiers

The positive result assumes a smooth Euclidean thermal circle and declared
bosonic or fermionic spin structure. The continuation no-go applies only to
the raw analytic sampling domain without OS positivity and growth conditions.
An admitted reflection-positive flavor correlator with unique spectral
reconstruction would close that kernel, but would still need mode selection
and detector calibration.

Primary sources: Osterwalder and Schrader, [Axioms for Euclidean Green's
Functions](https://doi.org/10.1007/BF01645738) and [Axioms for Euclidean
Green's Functions II](https://doi.org/10.1007/BF01608978).

## Disposition

Progressive at the comparison level, incomplete at realization. Euclidean
regularity supplies the primitive frequency attachment required by Aspect's
tester, but it does not select a flavor mode or construct a Lorentzian
physical16 instrument.
