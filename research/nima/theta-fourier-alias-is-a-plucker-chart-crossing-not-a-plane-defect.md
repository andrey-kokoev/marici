# A Fourier alias is a Plücker-chart crossing, not a plane defect

## Status

Exact finite-dimensional correction to the metaplectic-alias interpretation.
A zero of one two-label Fourier minor usually means that one Plücker coordinate
of the transported two-plane vanishes. The full exterior state can remain
nonzero and retain rank. The Maslov grade then records atlas transitions of the
plane, not zeros of the distinguished theta transmission channel.

This exposes a recursive form of the ordered-port problem: positivity of the
full exterior norm does not orient or protect one source-selected Plücker
coordinate.

## Three-label Fourier carrier

Choose three distinct logarithmic positions

\[
q_1<q_2<q_3
\]

and two frequencies \(\xi_1<\xi_2\). Form the matrix

\[
M=
\begin{pmatrix}
e^{-i\xi_1q_1}&e^{-i\xi_1q_2}&e^{-i\xi_1q_3}\\
e^{-i\xi_2q_1}&e^{-i\xi_2q_2}&e^{-i\xi_2q_3}
\end{pmatrix}.
\]

Its Plücker coordinates are the three column minors

\[
\Delta_{jk}
=
e^{-i(\xi_1q_j+\xi_2q_k)}
-
e^{-i(\xi_2q_j+\xi_1q_k)},
\qquad
1\leq j<k\leq3.
\]

Each satisfies

\[
|\Delta_{jk}|^2
=
4\sin^2\left(
\frac{(\xi_2-\xi_1)(q_k-q_j)}2
\right).
\]

## One coordinate can vanish without rank loss

Put

\[
\xi_2-\xi_1
=
\frac{2\pi}{q_2-q_1}.
\]

Then

\[
\Delta_{12}=0.
\]

But if

\[
\frac{q_3-q_1}{q_2-q_1}\notin\mathbb Z,
\]

then

\[
\Delta_{13}\neq0.
\]

Consequently

\[
\operatorname{rank}M=2
\]

even though the selected coordinate \(\Delta_{12}\) vanishes.

The aliasing wall is therefore a boundary of the \((1,2)\) Plücker chart, not
a degeneracy of the full transported plane.

## Exterior Gram energy

By Cauchy--Binet,

\[
\det(MM^*)
=
|\Delta_{12}|^2
+|\Delta_{13}|^2
+|\Delta_{23}|^2.
\]

This is the squared norm of the exterior state formed by the two rows of
\(M\). It is strictly positive whenever at least one Plücker coordinate is
nonzero.

Thus the full-plane energy can be faithful while a distinguished cross minor
is zero. Summing the squares repairs chart singularity by forgetting which
ordered label pair supplied the readout.

## What the metaplectic lift actually transports

The lifted sign of \(\Delta_{12}\) tells us how the oriented plane passes from
one side of the \((1,2)\)-chart wall to the other. Another nonzero coordinate,
such as \(\Delta_{13}\), provides a valid chart through the crossing.

The lift therefore belongs naturally to the determinant line of the full
two-plane and its Plücker atlas. It does not automatically belong to the
source-selected scalar coordinate.

This is the same distinction already encountered in control form:

- the full Weyl determinant can remain regular;
- the ordered endpoint/source cross-transfer can vanish.

The Grassmannian rotation has rediscovered the framed-port correction rather
than escaped it.

## Arithmetic specialization

For

\[
q_j=\log n_j,
\qquad
n_1<n_2<n_3,
\]

the nonintegrality condition becomes

\[
\frac{\log(n_3/n_1)}{\log(n_2/n_1)}\notin\mathbb Z.
\]

A minimal exact example is

\[
(n_1,n_2,n_3)=(1,2,3),
\qquad
\xi_2-\xi_1=\frac{2\pi}{\log2}.
\]

Then \(\Delta_{12}=0\), while \(\Delta_{13}\neq0\) because
\(\log3/\log2\) is not an integer.

The full Fourier plane remains rank two at an exact labelled alias of the
first pair.

## The actual missing structure

The theta problem cannot be solved by proving only that the full exterior
state never vanishes. It must explain why the particular ordered
endpoint/source coordinate selected by the arithmetic construction cannot
vanish off the seam.

That requires a source-derived flag in the Plücker bundle:

\[
\mathfrak f
=
(b_0,b_{\rm src}).
\]

The flag must survive Fourier transport, reciprocal sewing, current
renormalization, and completion. An unflagged determinant-line norm is too
coarse.

## Finite falsifier

Use the three-label matrix above with labels \((1,2,3)\) and frequency gap
\(2\pi/\log2\). It simultaneously satisfies

\[
\Delta_{12}=0
\]

and

\[
\det(MM^*)>0.
\]

This falsifies every proposed inference from faithful full-plane Gram energy,
nonzero exterior state, or coherent metaplectic transport to nonvanishing of a
chosen ordered Plücker coordinate.

## Decisive conclusion

The infinite alias walls are mostly chart crossings, not physical punctures.
The metaplectic lift coherently transports the full oriented plane across
them. RH-strength content remains in the much sharper claim that one
source-selected coordinate of that plane cannot vanish off the critical seam.

The next legitimate move is not to strengthen the unflagged exterior norm. It
is to construct the ordered arithmetic flag inside the Plücker bundle and test
whether source transport preserves a transverse cone around that flag. If no
such flagged cone is source-derived, the geometric-algebra rotation returns to
the original cross-transfer problem without adding zero confinement.
