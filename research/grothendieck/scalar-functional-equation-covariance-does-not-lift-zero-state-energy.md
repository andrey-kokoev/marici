# Scalar functional-equation covariance does not lift zero-state energy

## The tempting implication

The doubled valuation colligation gives a strict local seam detector. One
might hope that reciprocal functional-equation symmetry and a scalar zero
automatically equate the direct and dual chain energies.

That inference is false at the level currently constructed.

## Smallest typed countermodel

Let

\[
H_+=H_-=\mathbb R^2
\]

and let the reciprocal comparison be the unitary swap

\[
F(x_1,x_2)=(x_2,x_1).
\]

Define covariant scalar readouts

\[
L_+(x_1,x_2)=x_2,
\qquad
L_-(y_1,y_2)=y_1.
\]

Then

\[
L_-(Fx)=L_+(x)
\]

for every (x). This is an exact scalar functional equation.

Choose distinguished states

\[
v_+=(1,0),
\qquad
v_-=(0,2).
\]

Both scalar readouts vanish:

\[
L_+(v_+)=L_-(v_-)=0,
\]

but

\[
\lVert v_+\rVert^2=1,
\qquad
\lVert v_-\rVert^2=4.
\]

The readout covariance does not imply that the selected states satisfy

\[
v_-=Fv_+.
\]

## Consequence for the theta/Tate programme

The scalar functional equation

\[
\Xi(s)=\Xi(1-s)
\]

relates completed readouts. Even combined with

\[
\Xi(s)=\Xi(1-s)=0,
\]

it does not by itself identify the underlying direct and reciprocal
zero-states or equate their energies.

The next rung of the fourth tower must therefore be a state-lift theorem:

\[
\Psi_-(1-\overline s)
=
\mathcal F_{\mathrm{Tate}}\Psi_+(s)
\]

on the source-derived zero-state domain, not merely after scalar readout.

## A second required intertwiner

Even a full-state unitary lift is insufficient unless the oriented local
valuation energies are functorial shadows of that state comparison. The local
states

\[
x_{p^{-s},N},
\qquad
x_{p^{s-1},N}
\]

are not presently proved to be the images of the completed zero-state under a
common norm-compatible projection.

Thus we need maps

\[
\pi_{p,N}^{\pm}:H_{\mathrm{completed}}^{\pm}
\longrightarrow H_{p,N}^{\pm}
\]

and a commuting square

\[
\pi_{p,N}^-\mathcal F_{\mathrm{Tate}}
=
F_{p,N}\pi_{p,N}^+.
\]

The energy comparison is RH-relevant only if the boundary conditions of a
zero-state force equality of the projected direct and reciprocal norms.

## Fourth-tower retyping

Two distinct rungs were previously conflated:

1. scalar readout covariance;
2. state-level reciprocal equivalence;
3. valuation-projection naturality.

The doubled local seam detector belongs after rung 3. It cannot be pulled back
through rung 1 alone.

## Falsifiers

The route fails if:

- reciprocal sewing is defined only on scalar sections;
- the canonical direct and dual zero-states are not related by the lifted
  Fourier--Tate map;
- the valuation projections do not commute with sewing;
- they commute but do not preserve the Green energy required by the seam
  detector;
- equality of projected norms is imposed as a domain definition rather than
  derived from source boundary conditions.

## Current obstacle

Construct the state-valued functional equation before using the local energy
orientation. The next exact object is the commuting square between completed
theta zero-states and bordered valuation-chain states. Without it, the seam
detector is mathematically correct but disconnected from zeros.

