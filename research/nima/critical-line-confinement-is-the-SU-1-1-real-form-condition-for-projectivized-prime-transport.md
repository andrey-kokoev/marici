# Critical-line confinement is the SU(1,1) real-form condition for projectivized prime transport

## Determinant-one transport

Projectivize the local valuation tilt

\[
T_{p,z}=\operatorname{diag}(1,p^{-z})
\]

by its determinant to obtain

\[
\widehat T_{p,z}
=p^{z/2}T_{p,z}
=
\operatorname{diag}(p^{z/2},p^{-z/2})
\in SL(2,\mathbb C).
\]

Let

\[
J=\operatorname{diag}(1,-1).
\]

A direct calculation gives

\[
\widehat T_{p,z}^{*}J\widehat T_{p,z}
=
\operatorname{diag}
\left(p^{\operatorname{Re}z},-p^{-\operatorname{Re}z}\right).
\]

Therefore

\[
\widehat T_{p,z}\in SU(1,1)
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

Thus the critical seam is exactly the intersection of the complex spectral
torus with the reciprocal unitary real form.

## Relation to the Krein trace

The failure of `SU(1,1)` membership is measured by

\[
\widehat T_{p,z}^{*}J\widehat T_{p,z}-J.
\]

After undoing determinant normalization and evaluating on the equal-energy
reciprocal Gram, its oriented diagonal contraction is

\[
(1-p^{-2\operatorname{Re}z})E_p(b_z),
\]

the rung-four residual. Hence the residual is the metric defect of the
projectivized prime holonomy.

## Positive-geometric route

The positive `A_(n,2,4)` construction is defined over real positive external
data. Its rank-two boundary transport lies projectively in a real form of
`PGL(2,C)`. The group `PSU(1,1)` is Cayley-conjugate to `PSL(2,R)`.

This yields a precise candidate filler:

1. construct the rank-two holonomy of the two-phase four-presentation packet;
2. prove from canonical-form residue sewing that it lies in the positive real
   form;
3. identify that real form, through the source-fixed reciprocal Cayley frame,
   with `PSU(1,1)`;
4. identify its prime-diagonal restriction with `[T_hat_(p,z)]`.

These four steps would imply `Re z=0` without fitting a scalar correction.

## Frame warning

`PSL(2,R)` has several conjugate realizations inside `PGL(2,C)`. Realness of a
matrix in an arbitrary frame does not imply reciprocal `J`-unitarity. The
Cayley frame must be fixed by the source sheet involution and preserved by all
lower sewing cells. Otherwise the argument merely chooses a real form adapted
to the desired conclusion.

## Current gate

The repository has local projective `2 by 2` transport and a positive-geometric
canonical-form construction, but no global category-valued connection proving
that the prime spectral holonomy is the same transport in the source-fixed
Cayley frame. That identification is the bounded real-form gate.