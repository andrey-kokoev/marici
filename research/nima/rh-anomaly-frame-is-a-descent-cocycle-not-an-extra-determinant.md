# The anomaly frame is a descent cocycle, not an extra determinant

## Local frames

At every finite cutoff, the order-three determinant separates the logarithm
into degrees one, two, and at least three. The third-degree tail has its own
regularized determinant. The first two degrees instead specify a local frame
for the relative determinant line.

On an overlap of two cutoff or presentation charts, two admissible frames may
differ by

\[
g_{ij}(K)=
\exp\!\left(
a_{ij}\operatorname{Tr}K+
\frac{b_{ij}}2\operatorname{Tr}K^2
\right).
\]

The coefficients retain their source degrees. Mixing them would erase the
primitive-versus-square typing.

## Descent criterion

Triple-overlap compatibility requires

\[
g_{ij}g_{jk}g_{ki}=1.
\]

Taking the degree-resolved logarithm gives two additive cocycle conditions:

\[
a_{ij}+a_{jk}+a_{ki}=0,
\qquad
b_{ij}+b_{jk}+b_{ki}=0.
\]

A canonical global scalar frame exists only when both cocycles are
coboundaries. There must be chart potentials \(a_i,b_i\) satisfying

\[
a_{ij}=a_j-a_i,
\qquad
b_{ij}=b_j-b_i.
\]

The completed determinant problem is therefore descent in a product of two
typed anomaly-line torsors. It is not the construction of a fourth
regularized determinant.

## What reciprocal sewing does

Reciprocal dagger sewing relates transition data on paired charts. It can
force parity relations between their degree-one and degree-two components.
Those relations do not by themselves imply that the cocycles are
coboundaries. A reciprocal pair can carry equal and opposite local
transitions while a cycle through the completion chart retains nonzero
holonomy.

Consequently, functional-equation symmetry supplies an equivariant descent
datum, not a global trivialization. The endpoint, seam, and archimedean Green
law must provide the missing coboundary potentials or an equivalent canonical
null-homotopy.

## Finite falsifier

Use three charts arranged in a cycle. Assign degree-one transition increments

\[
a_{01}=1,
\qquad
a_{12}=1,
\qquad
a_{20}=-1.
\]

Every edge has a valid invertible transition, but the cycle sum is \(1\), so
no chart potentials can generate the transitions. The same construction works
independently in degree two. This is the smallest obstruction to a proposed
global anomaly frame.

The decisive source calculation is now finite in form: compute the typed
transition increments supplied by the primitive, square, endpoint, seam, and
archimedean boundary maps, then test every generating cycle. One nonzero
degree-resolved cycle sum falsifies scalar descent. Vanishing cycle sums yield
a global frame only after the resulting potentials are shown compatible with
cutoff completion.

## DPC verdict

The order-three determinant supplies the local three-stratum totalization.
The remaining constructor is a source-derived descent contraction for two
separate anomaly cocycles. Symmetry, invertibility, and cutoffwise scalar
agreement are insufficient substitutes.

## Verification

`check_rh_anomaly_frame_descent.py` checks exact cocycle and coboundary
conditions, source-degree separation, a valid trivializable fixture, and the
three-chart hostile cycle above.
