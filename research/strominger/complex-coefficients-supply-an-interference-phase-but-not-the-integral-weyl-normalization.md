# Complex coefficients supply an interference phase but not the integral Weyl normalization

## Source-side multiplicative port

The spin-memory source does contain a multiplicative observation in an
operational sense.  Equations (4.3)--(4.5) of *New Gravitational Memories*
define a real counter-orbiting-light delay \(\Delta u\), and the text states
that this delay shifts an interference pattern.  For a monochromatic probe of
angular frequency \(\omega\), the corresponding record is

\[
W_\omega(\Delta u)=\exp(i\omega\Delta u)\in U(1).
\]

This is stronger than merely replacing real coefficients by complex additive
coefficients.  It is a source-motivated multiplicative instrument.

## Why complexification alone still fails

The additive groups of both \(\mathbb R\) and \(\mathbb C\) are torsion-free.
Consequently every additive homomorphism

\[
\mathbb Z/7\longrightarrow\mathbb C
\]

is zero.  Seventh roots become available only after applying the exponential
and landing in \(U(1)\subset\mathbb C^\times\).

The exponential needs a dimensionless argument.  If candidate delays are

\[
\Delta u_t=\frac{2t}{7}\tau,
\]

then

\[
W_\omega(\Delta u_t)=
\exp\left(2\pi i\frac{2t}{7}\right)
\]

only when \(\omega\tau=2\pi\) modulo \(14\pi\).  Neither the puncture cycle
lattice nor complexification selects such a frequency-scale pairing.

## Gauge versus instrument periodicity

The phase port is periodic as an instrument:

\[
W_\omega(\Delta u+2\pi n/\omega)=W_\omega(\Delta u).
\]

That does not imply that the gravitational states with delays \(\Delta u\)
and \(\Delta u+2\pi n/\omega\) are gauge equivalent.  The real delay remains
available to another frequency or to direct timing.  Hence the phase port is
a nonfaithful observation of a real source state, not a compactification of
the source state space.

The family over all positive frequencies is faithful: if
\(e^{i\omega x}=e^{i\omega y}\) for every \(\omega>0\), then \(x=y\).
Thus no intrinsic finite quotient survives the complete interference
instrument family.

## Classification

Complex coefficients explain three quarters of the desired picture:

1. a physical multiplicative phase record exists;
2. its codomain contains the seventh roots of unity;
3. two real delays can be aliased by one chosen phase port.

They do not explain the remaining source theorem:

4. why the affine-discriminant step is locked to one seventh of the chosen
   optical period.

The smallest missing constructor is therefore no longer a generic
prequantization.  It is a source-authorized normalization correspondence

```text
DiscriminantInterferometerLock
  gravitational_delay_unit tau
  probe_frequency omega
  affine_discriminant_pairing lambda_F
  dimensionless_lock omega*tau = 2*pi
  authority_root
```

Without this lock, choosing \(\omega\) to manufacture the desired seventh
root is fitted instrumentation.  With it, the finite Weyl phase port is
source-derived.  The source material currently authorizes the interference
phase but not the lock.

## Verdict

Complex coefficients reveal a genuine physical phase-valued readout, so the
earlier statement that exponentiation is merely formal was too strong.  They
do not by themselves establish an integral Weyl lift.  The obstruction moves
from existence of a phase port to source authority for its normalization.
