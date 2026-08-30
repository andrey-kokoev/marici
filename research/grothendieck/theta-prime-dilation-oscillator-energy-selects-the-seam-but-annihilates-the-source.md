# Theta prime-dilation oscillator energy selects the seam but annihilates the source

## Bounded question

Does Nima's Gaussian vacuum--prime dilation square produce a source-derived
energy whose transport distinguishes the critical seam?

## Labelled oscillator form

For the labelled Gaussian atom

\[
\phi_n(x)=e^{-\pi n^2x^2},
\]

put

\[
a_n=\partial_x+2\pi n^2x,
\qquad
H_n=a_n^*a_n.
\]

Let raw dilation act by

\[
(R_p\psi)(x)=\psi(px).
\]

The exact covariance is

\[
a_{pn}R_p=pR_pa_n.
\]

Since \(R_p^*R_p=p^{-1}\) on \(L^2(\mathbb R,dx)\), it follows that

\[
R_p^*H_{pn}R_p=pH_n.
\]

Thus the quadratic oscillator energy obeys

\[
E_{pn}(R_p\psi)=pE_n(\psi),
\qquad
E_n(\psi)=\|a_n\psi\|^2.
\]

## Mellin transport selects the seam

Prime multiplication in the spectral character contributes the amplitude
\(p^{-s}\). Therefore

\[
E_{pn}(p^{-s}R_p\psi)
=p^{1-2\Re s}E_n(\psi).
\]

This is the first source-derived positive energy encountered in the programme
whose transport multiplier changes orientation exactly at the critical line:

- it contracts for \(\Re s>1/2\);
- it is isometric for \(\Re s=1/2\); and
- it expands for \(\Re s<1/2\).

The half-offset is forced by the competition between the prime dilation
Jacobian and the squared Mellin amplitude. It is not fitted from the zero set.

Iterating a prime orbit gives

\[
E_{p^kn}(p^{-ks}R_{p^k}\psi)
=p^{k(1-2\Re s)}E_n(\psi).
\]

Its logarithmic transport increment is \((1-2\Re s)\log p\), placing the
von Mangoldt coefficient and the seam displacement in one exact law.

## Faithfulness obstruction

Every labelled source atom is a vacuum:

\[
a_n\phi_n=0.
\]

Consequently

\[
E_n(\phi_n)=0
\]

for every label. On the labelled direct sum, the diagonal oscillator form
annihilates the entire source-vacuum module

\[
\bigoplus_n\mathbb C\phi_n.
\]

This includes every finite arithmetic coefficient packet before synthesis.
The energy therefore has perfect seam orientation but no faithfulness on the
physical source states whose scalar aggregation produces the zeta readout.

The obstruction is stronger than one null vector. Adding more diagonal
oscillator energies or iterating prime powers leaves the whole labelled vacuum
module in the kernel.

## Meaning

Two previously separate structures now meet exactly: Gaussian oscillator
scaling and prime Mellin transport.

Their relation explains why the half-line is the unit-energy seam. But an
energy can identify the correct seam while remaining blind to every admitted
source state. Seam selection and zero confinement are distinct capabilities.

## Revised live gate

A useful completion must add a source-derived off-diagonal or relative energy
that compares different labelled vacua. It must satisfy three conditions:

1. retain the multiplier \(p^{1-2\Re s}\) or an equivalent reciprocal law;
2. be nonzero on every admissible scalar-null source state; and
3. arise before scalar aggregation from prime dilation, Poisson sewing, or
   boundary incidence.

The cheapest candidate is a commutator or difference energy comparing the
prime-shifted vacuum with its transported predecessor, rather than applying
\(H_n\) separately to each atom. Its hostile test is whether the entire
labelled Gaussian orbit still lies in its kernel.

## Scope

This packet proves the exact prime-dilation energy scaling and derives the
critical seam as its isometric locus. It also proves that the diagonal
oscillator energy annihilates the complete labelled source-vacuum module. It
does not construct a faithful relative energy, bridge scalar zeros to excited
states, close the global current, or prove RH.
