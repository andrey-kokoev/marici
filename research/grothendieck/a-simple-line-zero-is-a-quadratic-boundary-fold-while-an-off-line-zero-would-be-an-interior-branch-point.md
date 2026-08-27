# A Simple Line Zero Is a Quadratic Boundary Fold While an Off-Line Zero Would Be an Interior Branch Point

## Local map at a zero

For the source potential

\[
Y'(z)=\frac12X(z),
\]

let `z_0` be a simple zero of `X`. Then

\[
Y'(z_0)=0,
\qquad
Y''(z_0)=\frac12X'(z_0)\ne0.
\]

Taylor expansion gives

\[
Y(z)-Y(z_0)
=
\frac14X'(z_0)(z-z_0)^2
+O((z-z_0)^3).
\]

Thus every simple Riemann zero is a quadratic branch point of the potential
map. The gradient field has index one there, while the potential map has local
degree two.

## Boundary fold on the critical line

Suppose

\[
z_0=i\gamma.
\]

Reality and evenness imply that `Y(it)` is purely imaginary and `X'(i gamma)`
is purely imaginary. Write

\[
\frac14X'(i\gamma)=i\kappa,
\qquad
\kappa\ne0.
\]

For the local coordinate

\[
z-z_0=a+i\tau,
\]

the quadratic term is

\[
i\kappa(a+i\tau)^2
=
-2\kappa a\tau
+i\kappa(a^2-\tau^2).
\]

Therefore the leading real potential is

\[
U(a,\gamma+\tau)-U(0,\gamma)
=-2\kappa a\tau+O(|a+i\tau|^3).
\]

Its zero-level set has two local branches:

\[
a=0,
\qquad
\tau=0,
\]

meeting at right angles. One branch is the critical seam; the other is its
normal continuation. The simple zero is therefore a two-fold boundary fold,
not an unexplained point sitting on a preferred line.

The local squaring map doubles angles. Conversely, lifting a smooth image ray
through the branch point produces two preimage rays separated by ninety
degrees. This is the exact geometric content of the proposed right-angle
unfolding intuition.

## Off-line meaning

If the same critical point occurs with nonzero real coordinate, there is no
boundary on which one branch can reside. The quadratic fold then lies entirely
inside an open reciprocal sector. It is an interior branch point of the
source-normalized comparison map.

RH can therefore be stated as:

> Every branch point of the completed theta potential is a boundary fold on
> the reciprocal seam; none is an interior branch point of either sector.

This statement concerns local meaning, not merely plotted zero locations.

## Relation to visible ovals

Level curves of `U` and `V` can appear as distorted ovals in the original
spectral chart. Near a simple zero, the canonical coordinate supplied by the
potential is quadratic. In that coordinate the local foliation is the
ordinary orthogonal grid of real and imaginary level lines. The apparent oval
or fold is therefore a projection of a regular two-sheet geometry through the
squaring map.

This does not imply that every globally visible oval is a literal circle, nor
does it prove RH. It identifies the exact local object of which the right-angle
geometry is a coordinate shadow.

## Next theorem

The minimal global theorem is now a branch-localization statement. Construct
the foliation of the right half-plane by the level sets of `U` and `V`, with
the weighted infinity port retained, and prove that its branch divisor is
supported on the boundary seam.

A hostile source with an off-line zero produces an interior quadratic branch
point while preserving generic positivity and symmetry. The missing theta law
must reject that branch through labelled modular transport before scalar
aggregation.

## Result

Simple critical-line zeros are source-potential boundary folds with an exact
right-angle local split. Off-line zeros would be interior branch points of the
same map. RH is the confinement of the potential's branch divisor to its
constant-potential boundary.
