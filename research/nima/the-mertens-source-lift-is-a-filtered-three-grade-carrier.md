# The Mertens source lift is a filtered three-grade carrier

## Question

What is the minimum state-valued source object that can precede the scalar
Mertens/BSY readout and still retain the completion distinctions already proved
necessary?

## Three incompatible grades

The Euler logarithm has the established filtration:

- primitive raw carrier: third-Schatten but not Hilbert--Schmidt globally;
- square grade: Hilbert--Schmidt but not trace class;
- connected grades \(k\geq3\): trace class.

The observed primitive density is a separate second-Schatten-level object; it
must not be identified with a literal trace of the raw carrier. These grades
cannot be flattened into one ordinary trace-class carrier before
renormalization. Doing so either deletes the primitive and square currents or
silently assigns them a completion they do not possess.

The minimum source carrier is therefore a filtered object

\[
0\subset F_3\subset F_2\subset F_1,
\]

with associated grades

\[
F_1/F_2=G_1,
\qquad
F_2/F_3=G_2,
\qquad
F_3=G_{\geq3}.
\]

The scalar Mertens functional is a later map

\[
q:G_1\oplus G_2\oplus G_{\geq3}\longrightarrow\mathbb R.
\]

Its calibrated value is the declared combination of the primitive constant,
half the prime-square constant, and the connected remainder.

## Scalar lift obstruction

Even in the smallest finite model, the scalar map

\[
q(x_1,x_2,x_3)=x_1+x_2+x_3
\]

has a two-dimensional kernel. A scalar value has an affine plane of lifts.
For example,

\[
(1,0,0),\quad(0,1,0),\quad(0,0,1)
\]

all produce the same scalar while representing different grades and different
completion laws.

There is no canonical inverse to \(q\). Choosing equal thirds, putting the
whole value in one grade, or fitting a preferred lift from the completed
answer erases source typing. A lawful lift must be constructed grade by grade
from labelled Euler incidence.

## Why direct sum is still insufficient

The notation \(G_1\oplus G_2\oplus G_{\geq3}\) records the associated graded
object only. The actual filtered carrier also contains extension data:

- how primitive subtraction changes the square domain;
- how the det3 counterterms attach to the connected determinant;
- how endpoint and archimedean currents act across the filtration;
- how reciprocal sewing reverses or preserves each grade;
- how cutoff refinement transports the boundary residues.

Thus the required state object is a filtered relative-determinant carrier, not
three unrelated registers.

## Acceptance contract

A proposed Mertens source lift must provide:

1. labelled incidence into each of the three grades;
2. the filtration and its extension maps;
3. cutoff bonding maps preserving the filtration;
4. endpoint, gamma, and reciprocal actions before scalar projection;
5. a boundary-corona topology on the full filtered object;
6. the scalar Mertens functional as a continuous final readout;
7. a proof that the completed residual vanishes in the carrier, not merely
   after applying the scalar.

## Finite falsifier

Use the three grade vectors

\[
v_1=(1,0,0),\qquad v_2=(0,1,0),\qquad v_3=(0,0,1).
\]

All have scalar readout one. Their grade-deletion responses are distinct, and
no scalar-only procedure can reconstruct which state was present. Any proposed
comparison cell defined only after applying \(q\) is therefore not faithful on
the minimum source carrier.

## Verdict

The state-valued predecessor of the Mertens/BSY scalar is a filtered
three-grade relative-determinant carrier. Its scalar quotient has a
two-dimensional kernel before any infinite completion effect is considered.
The next construction must lift finite Euler and theta--Tate routes into this
same filtered boundary carrier and compare them there.
