# Complementary lift-channel rank

> Superseded physical interpretation: WP989 shows that the four labelled
> coefficient coordinates have a two-dimensional kinetic field-normalization
> redundancy. The rank-four result below remains correct on the labelled
> coefficient packet, but it is not a rank statement on the faithful physical
> quotient. The three proposed coordinate rows do not descend individually.

## Question

WP986 asks for the smallest complementary response family that can remove the
WP985 constructor kernel locally on the labelled coefficient packet.

Use logarithmic source coordinates

\[
x=(x_\Gamma,x_A,x_B,x_C)
=(\log\Gamma,\log A,\log B,\log C).
\]

The normalized determinant response supplies one row:

\[
y_0=2x_\Gamma+4x_A-x_B-5x_C.
\]

Its Jacobian is

\[
r_0=(2,4,-1,-5),
\]

with a three-dimensional kernel.

## Minimal rank theorem

Any family containing \(y_0\) and at most two additional scalar channels has
rank at most three on the four-dimensional source tangent space. At least
three independent complementary channels are therefore necessary.

The formal family

\[
y_\Gamma=x_\Gamma,qquad
y_B=x_B,qquad
y_C=x_C
\]

is sufficient. Its joint Jacobian is

\[
J=
\begin{pmatrix}
2&4&-1&-5\\
1&0&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\qquad
\det J=-4.
\]

For the independently calibrated identity metric, the positive Gram
determinant is

\[
\det(J^TJ)=16.
\]

The source coordinates reconstruct as

\[
x_\Gamma=y_\Gamma,quad
x_B=y_B,quad
x_C=y_C,quad
x_A=\frac{y_0-2y_\Gamma+y_B+5y_C}{4}.
\]

## Physical typing

The rows suggest, but do not yet establish, a physical family:

- a calibrated determinant/commutator competition response for \(y_0\);
- an independently normalized quartic-vertex response for \(y_\Gamma\);
- scalar and adjoint pole-mass responses for \(y_B,y_C\).

These are algebraically source-labelled because they refer to distinct
Lagrangian vertices and poles. They are not yet a physical instrument:
finite widths, mixing, decoupling, detector resolution, common-frame
calibration, and full weak-basis descent remain unproved.

This family separates UV source tangents. It does not select a preferred
source point or prove the WP983 magnitude.

The smallest falsifier is either a physical realization whose calibrated
Jacobian loses rank, or a source symmetry that identifies one of these
supposedly independent channels.

## Reproduction

Run:

    python research/flavor/checkers/wp986_complementary_lift_channel_rank.py

The generated result is
research/flavor/results/wp986_complementary_lift_channel_rank.json.
