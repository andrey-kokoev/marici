# Invariant Positivity Exists Only After Label Completion

## Two projections

Let

\[
\mathsf E=\frac{1+\mathsf R}{2},
\qquad
\mathsf A=\frac{1-\mathsf R}{2},
\qquad
(\mathsf Rf)(u)=f(-u).
\]

For the source split

\[
\Phi=\phi_1+\tau,
\]

completed reflection symmetry gives

\[
\mathsf A\phi_1+\mathsf A\tau=0
\]

and

\[
\Phi=\mathsf E\phi_1+\mathsf E\tau.
\]

## Failure of labelwise invariant positivity

The primitive invariant projection is

\[
\mathsf E\phi_1(u)
=
\frac{\phi_1(u)+\phi_1(-u)}2.
\]

It is negative for every sufficiently large positive \(u\). Therefore the
reflection-invariant projection is not positivity-preserving on the primitive
theta label.

Since the full completed source is positive,

\[
\mathsf E\tau(u)
=
\Phi(u)-\mathsf E\phi_1(u)
>
\Phi(u)
\]

whenever \(\mathsf E\phi_1(u)<0\).

The tail's invariant component must therefore overshoot the final completed
source by exactly the primitive invariant deficit.

## Noncommuting proof architecture

Algebraically, summation and projection commute:

\[
\mathsf E(\phi_1+\tau)
=
\mathsf E\phi_1+\mathsf E\tau.
\]

But positivity does not commute with this decomposition. The individual
projected summands are signed even though their completed sum is positive.

Thus the admissible proof order is:

1. retain the positive labelled source packet;
2. assemble all labels;
3. use the exact anti-invariant incidence to sew the chambers;
4. only then regard the result as a positive invariant source.

Projecting each label first destroys the positive-source interpretation.

## Consequence for the RH lane

No labelwise positive Fourier or Mellin argument can be obtained by applying
the invariant projector separately to primitive labels. The relevant positive
object is the completed invariant packet, while the labels remain necessary
as provenance and incidence data.

This isolates the next hard question:

Does the completed labelled incidence orient the oscillatory transform of the
positive invariant sum, even though neither projected component is positive?

## Falsifier

Labelwise invariant positivity would require

\[
\mathsf E\phi_n(u)\geq0
\]

for every label and every positive \(u\). The primitive label already violates
this condition.
