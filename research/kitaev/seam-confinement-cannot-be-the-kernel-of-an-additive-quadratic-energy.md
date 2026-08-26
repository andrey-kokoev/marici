# Seam Confinement Cannot Be the Kernel of an Additive Quadratic Energy

The failure of zero-velocity cones suggests replacing them by an additive or
quadratic source law. That repair has a sharp limitation: the zero set of a
positive semidefinite quadratic form is a linear subspace, whereas seam
confinement is not closed under addition.

Let the seam be the imaginary axis and consider

\[
F_+(z)=(z-i)(z-2i)
=z^2-3iz-2,
\]

\[
F_-(z)=(z+i)(z+2i)
=z^2+3iz-2.
\]

Every zero of each polynomial lies on the seam. But

\[
F_+(z)+F_-(z)=2z^2-4=2(z^2-2),
\]

whose zeros are

\[
z=\pm\sqrt2.
\]

Both are off the seam. Thus the class

\[
\mathcal S
=\{F:\text{every zero of }F\text{ lies on the seam}\}
\]

is not a linear subspace.

## Quadratic-kernel obstruction

Let \(H\ge0\) be a Hermitian operator on a coefficient space and define

\[
E(F)=\langle F,HF\rangle.
\]

Then

\[
E(F)=0
\quad\Longleftrightarrow\quad
H^{1/2}F=0,
\]

so

\[
\ker E=\ker H
\]

is linear. Consequently, no positive semidefinite quadratic form on a linear
space containing \(F_+\) and \(F_-\) can have

\[
\ker E=\mathcal S.
\]

Indeed, if both seam-confined polynomials had zero energy, their sum would
also have zero energy, despite its off-seam zeros.

The same obstruction applies to any linear defect map \(L\): its kernel cannot
equal the full seam-confined class on this coefficient space.

## What additive energy can still do

An additive energy remains viable in three more carefully typed roles.

1. Its kernel can be a source-defined linear subspace contained in the
   seam-confined class. This requires an independent theorem that every state
   in that subspace is seam-confined; equality with all seam-confined states is
   neither needed nor generally possible.

2. It can measure a linear source defect whose vanishing implies a nonlinear
   spectral theorem. The implication is extra mathematics, not encoded by the
   kernel alone.

3. It can act on a nonlinear lift of the state, such as a typed Gram,
   Hermite--Biehler, divisor, or state-current packet. The lift must be derived
   before the quadratic form and must retain the information lost by scalar
   coefficients.

Thus the best surviving DPC cannot say that a quadratic kernel is exactly the
seam sector. It must identify a linear constructor defect \(L\), prove a
source inequality controlling \(L\), and separately prove

\[
L(F)=0
\quad\Longrightarrow\quad
F\text{ is seam-confined}
\]

on the frozen admissible source class.

## Deutschian consequence

The energy is not the explanation merely because it is positive. The
explanation must say why the source state carries a particular lifted defect
whose vanishing entails seam confinement. Otherwise the nonlinear conclusion
has been hidden in the choice of lift or admissible subspace.

## Falsifiers

- Claiming that the complete seam-confined class is a quadratic kernel.
- Assuming seam confinement is preserved by linear superposition.
- Defining a nonlinear lift using the desired divisor and calling the result
  source-derived.
- Proving positivity of an energy without proving what its linear kernel means
  spectrally.
- Restricting the admissible subspace after inspecting zeros.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to test whether the additive repair can directly encode the
desired spectral sector.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. It cannot: the kernel is linear and seam confinement is not. The missing
bridge is now explicitly a source-derived lift plus a separate spectral
implication.
