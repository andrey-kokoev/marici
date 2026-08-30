# Flavor Charge Origin and Orientation Need Different Observers

## Result

The affine ambiguity above the hierarchy matrix has two coordinates:

- a continuous or lattice-valued translation of the charge origin;
- a discrete reflection of the charge line.

These coordinates are naturally observed by different constraint types. A
generic linear sum constraint fixes an origin on each reflected sheet. A
translation-invariant signed difference fixes the sheet while leaving the
origin free.

## Affine family

Write every lift of the observed hierarchy as

\[
q(s,c)=s(3,2,0)+c(1,1,1),
\]

where

\[
s\in\{-1,1\}
\]

is orientation and \(c\) is the common shift.

## Origin observer

Consider the illustrative condition

\[
q_1+q_2+q_3=5.
\]

On the positive sheet it gives

\[
s=1,
\qquad
c=0.
\]

On the reflected sheet it gives

\[
s=-1,
\qquad
c=\frac{10}{3}.
\]

Thus the equation does not select orientation over rational charges. It fixes
one origin on each sheet.

The earlier integer census retained only the first solution because
\(10/3\) is not an integer. That uniqueness relied on an additional charge
lattice. Charge quantization must therefore remain explicitly typed; it cannot
be silently attributed to the affine sum equation.

## Orientation observer

Now consider

\[
q_1-q_2=1.
\]

Its coefficient sum is zero, so common translation cancels. It holds for every
shift on the positive sheet and changes sign on the reflected sheet.

This observer detects orientation but cannot determine the origin.

## Joint reconstruction

Combining the origin and orientation constraints gives

\[
s=1,
\qquad
c=0
\]

over rational charges, without using integrality as an accidental selector.

The two observers are therefore complementary:

- the origin observer has nonzero response to common translation;
- the orientation observer has zero translation response and odd reflection
  character.

## General constraint typing

For a linear observer

\[
L_a(q)=a_1q_1+a_2q_2+a_3q_3,
\]

the sum

\[
a_1+a_2+a_3
\]

determines its translation type.

If the sum is nonzero, the observer can constrain the origin. If the sum is
zero, it factors through charge differences and cannot see the origin. Its
reflection character then determines whether it can distinguish the two
sheets.

Actual anomaly equations may be nonlinear or involve charges from additional
representations, but the same audit applies: compute their response to common
translation and reflection before claiming that they select an affine lift.

## Staged architecture

The likely order is now:

1. hierarchy observer reconstructs the unsigned distance matrix;
2. representation or anomaly data constrain the charge origin;
3. a signed translation-invariant relation constrains orientation;
4. charge-lattice typing checks integrality or rational quantization;
5. terminal pullback retains only jointly compatible lifts;
6. later preparation dynamics address Wilson coefficients and CP.

The second and third stages may exchange order if their domains permit it, but
their outputs cannot substitute for each other.

## Finite falsifiers

A proposed anomaly-based charge derivation fails if:

- its equations are translation-sensitive but it claims to fix reflection
  without checking both sheets;
- its equations are translation-invariant but it claims to fix the absolute
  origin;
- integer uniqueness disappears when the charge-lattice assumption is removed;
- the lattice, representation, or anomaly data were selected after inspecting
  the target charge vector.

## Status

The source search can now be performed by constraint character rather than by
raw equation count. Figueiredo should classify each candidate anomaly and
representation condition by translation response, reflection response, and
charge-lattice domain before testing whether the full family has a unique
lift.
