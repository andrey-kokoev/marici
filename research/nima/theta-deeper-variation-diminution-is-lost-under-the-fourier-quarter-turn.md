# Deeper theta mechanism: variation diminution is lost under the Fourier quarter-turn

## Status

Exact kernel-minor comparison and source-law DPC. Ordered Krein signature would
forbid the off-seam two-moment collision. A standard mechanism for preserving
such order is variation diminution under a totally positive or sign-regular
kernel. The bare theta atom kernel has this property in radial/Laplace
coordinates after one order reversal. The Fourier transformation used to make
logarithmic translation selfadjoint destroys fixed-sign minors.

The desired source law therefore lives naturally in one polarization, while
the selfadjoint spectral carrier lives in its conjugate polarization. A valid
RH mechanism must transport variation diminution through that quarter-turn or
retain both polarizations in a single framed object.

## Why variation diminution is the right pre-resolvent law

Suppose the source signature has one ordered transition. If the incidence map
from source labels to carrier spectral coordinates is variation diminishing,
the transported signature cannot acquire the alternating pattern

\[
+,-,+.
\]

The ordered-signature theorem then forbids the mass-and-barycenter collision
required by a nonreal transmission zero.

At finite level, total positivity of order two begins with the minors

\[
\Delta_{12}
=
K(x_1,y_1)K(x_2,y_2)
-
K(x_1,y_2)K(x_2,y_1).
\]

A fixed sign for every ordered pair is the smallest checkable source
certificate.

## Radial theta atom is sign-regular

The bare theta atoms use the exponential kernel

\[
K_{\rm L}(x,y)=e^{-xy},
\qquad
x>0,
\qquad
y>0,
\]

with arithmetic scale \(x\) and radial scale \(y\).

For

\[
x_1<x_2,
\qquad
y_1<y_2,
\]

the second minor is

\[
\Delta_{\rm L}
=
e^{-x_1y_1-x_2y_2}
-
e^{-x_1y_2-x_2y_1}.
\]

Since

\[
(x_1y_1+x_2y_2)
-
(x_1y_2+x_2y_1)
=
(x_2-x_1)(y_2-y_1)
>0,
\]

we have

\[
\Delta_{\rm L}<0.
\]

Reversing one coordinate order makes every such minor positive. The kernel is
strictly sign-regular at order two, and in fact belongs to the classical
strictly totally positive exponential family after the order convention is
fixed.

This is the natural home of a variation-diminishing source theorem.

## Fourier carrier loses fixed-sign minors

The logarithmic translation carrier is diagonalized by the Fourier kernel

\[
K_{\rm F}(q,\xi)=e^{-i\xi q}.
\]

For

\[
q_1<q_2,
\qquad
\xi_1<\xi_2,
\]

the second minor is

\[
\Delta_{\rm F}
=
e^{-i(\xi_1q_1+\xi_2q_2)}
-
e^{-i(\xi_2q_1+\xi_1q_2)}.
\]

Factoring out a unit phase leaves a sine of

\[
\frac{(\xi_2-\xi_1)(q_2-q_1)}{2}.
\]

Its sign and phase oscillate as the rectangle changes size. There is no global
order convention making all Fourier minors positive or even real with one
sign.

Therefore ordinary total positivity does not survive the Fourier quarter-turn.

## Exact polarization conflict

The two useful structures currently occupy different presentations:

- radial/Laplace presentation: sign regularity and variation diminution;
- Fourier/translation presentation: selfadjoint carrier and spectral energy.

Projecting entirely into the first loses the fixed selfadjoint spectral
geometry. Projecting entirely into the second loses the order structure that
could prevent alternating Krein signatures.

The missing object must retain the comparison between them before either
projection becomes authoritative.

## Relation to the two-sector Ubersector

This is another reason the complete theta object cannot be one scalar Hilbert
space. It needs at least:

\[
\left(
\mathcal X_{\rm L},
\mathcal X_{\rm F},
\mathcal T,
\mathfrak f,
\omega
\right),
\]

where \(\mathcal X_{\rm L}\) carries source order, \(\mathcal X_{\rm F}\)
carries the selfadjoint carrier, \(\mathcal T\) is the source-derived transform,
\(\mathfrak f\) is the ordered endpoint/source flag, and \(\omega\) is the
coherence law relating their quadratic and determinant data.

The transform \(\mathcal T\) cannot be treated as authority to transport total
positivity. Its oscillatory minors prove that such transport is not automatic.

## Possible surviving laws

Ordinary total positivity fails after Fourier rotation, but stronger structured
alternatives remain testable:

1. a complex sign-regularity law with a source-fixed phase for every minor;
2. a symplectic or Hermitian orientation of paired Fourier minors;
3. a two-sector sum in which conjugate oscillatory minors combine into a
   positive real determinant;
4. a de Branges-type phase monotonicity derived from the radial order;
5. a variation-diminishing theorem only on the framed zero-dynamics incidence
   class rather than on all Fourier data.

Each requires a named comparison cell. None follows from unitarity of the
Fourier transform.

## Finite source audit

The smallest useful calculation uses two arithmetic labels and two carrier
spectral samples:

1. form the complete labelled radial incidence matrix;
2. verify its order-two sign-regular minor;
3. apply the actual modular/Fourier sewing map;
4. retain the conjugate sector and ordered ports;
5. compute the resulting paired minor;
6. test whether its phase is source-fixed or whether it changes under hostile
   signed prime perturbations.

If the paired minor has no fixed orientation, the variation-diminishing route
closes before higher determinants are considered.

## Completion warning

Even a finite paired-minor orientation must survive:

- dense spectral sampling;
- primitive and square boundary currents;
- seam augmentation;
- the rigged Fourier trace;
- and restricted-product completion.

Cutoffwise sign regularity with a phase that oscillates increasingly rapidly
does not yield a completed order law.

## Decisive conclusion

The ordered-signature mechanism has a plausible source origin in the
sign-regular Laplace kernel of theta atoms. But the Fourier quarter-turn needed
for the selfadjoint carrier destroys ordinary variation diminution. The next
advance must be a source-derived two-polarization coherence theorem, not a
claim that total positivity is unitarily invariant.
