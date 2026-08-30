# The RH-Bearing Equalizer Must Retain Boundary Grade

## Candidate square

Let \(A\) be the source packet object, \(F:A\to A\) the reciprocal
Fourier–Tate transport, and let

\[
b_+:A\to B,
\qquad
b_-:A\to B
\]

be the direct and reciprocal boundary maps into one adelic-height graded
boundary object \(B\). The candidate null-event object is the equalizer of

\[
b_+
\qquad
b_-F.
\]

It must additionally retain a nonzero leading boundary class. Without that
condition, equality of two zero images is automatic and carries no
confinement information.

## Why the scalar equalizer is circular

Let \(a:B\to\mathbb C\) forget grade and take the completed scalar readout.
The equalizer of \(ab_+\) and \(ab_-F\) is too large. Two boundary classes in
different grades can have the same scalar image, and at a scalar zero both
images may vanish identically.

Consequently, defining a null event after applying \(a\) merely repackages the
functional equation or scalar zero condition. Hostile symmetric multipliers
survive that construction.

## Grade-separation theorem

Write the boundary object as a direct sum of homogeneous components,

\[
B=\bigoplus_\lambda B_\lambda.
\]

For a zero germ at \(s\), the direct and reciprocal leading classes occupy
grades

\[
1-\operatorname{Re}s,
\qquad
\operatorname{Re}s.
\]

Distinct homogeneous components intersect only at zero. Therefore a strict
graded equality between two nonzero leading classes forces

\[
1-\operatorname{Re}s=\operatorname{Re}s.
\]

This selects the critical seam without imposing a bounded norm on the
Fourier transport itself.

## What remains unproved

The theorem is conditional on a source bridge:

> Every completed scalar zero determines a nonzero object in the strict
> graded equalizer of the two boundary maps before scalar augmentation.

This is stronger than reciprocity. Fourier–Tate transport may carry one grade
to its complementary grade without identifying them. The missing coherencer
must explain why a null event is one boundary object with two presentations,
rather than merely a transported pair.

## Finite falsifier

Take a boundary carrier with two one-dimensional grades. Put the direct class
in the first grade and the reciprocal class in the second. An augmentation
that sends both basis vectors to \(1\) makes their scalar readouts equal.
They are nevertheless unequal in the graded carrier.

If the augmentation instead kills both basis vectors, scalar equality becomes
even more automatic. Neither case supplies a strict equalizer object.

## Decisive next calculation

Construct \(b_+\) and \(b_-\) from the labelled Euler–Maclaurin or theta/Tate
boundary packet and compute the pullback

\[
A\times_{B\times B}\Delta_B.
\]

Then test whether the scalar zero locus maps into this pullback with nonzero
leading class. Failure closes the fixed-null route. Success forces the seam
by grade separation.

