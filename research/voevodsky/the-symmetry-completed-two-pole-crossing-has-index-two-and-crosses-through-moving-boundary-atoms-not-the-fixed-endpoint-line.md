# The symmetry-completed two-pole crossing has index two and crosses through moving boundary atoms, not the fixed endpoint line

## Prior-research boundary

The repository contains the general statement that contour pole crossings contribute spectral-shift jumps, but no symmetry-completed elementary crossing family was found. The construction below is therefore a local analytic fixture, not a model of the complete zeta multiplier.

## Symmetry-completed family

Fix

\[
\gamma>0
\]

and define, for real \(a\),

\[
\Theta_{a,\gamma}(z)
=
\prod_{\epsilon=\pm1}
\frac{
z-
epsilon\gamma+ia
}
{
z-
epsilon\gamma-ia
}.
\]

For real \(t\),

\[
|\Theta_{a,\gamma}(t)|=1.
\]

The family also satisfies the centered real/reciprocal symmetry

\[
\Theta_{a,\gamma}(-\bar z)
=
\overline{
\Theta_{a,\gamma}(z)
}.
\]

Thus the two centers \(\gamma\) and \(-\gamma\) are exchanged by the completed reflection.

## Positive side

If

\[
a<0,
\]

put \(b=-a>0\). Then

\[
\Theta_{a,\gamma}(z)
=
B_{b,\gamma}(z),
\]

where

\[
B_{b,\gamma}(z)
=
\prod_{\epsilon=\pm1}
\frac{
z-
\epsilon\gamma-ib
}
{
z-
\epsilon\gamma+ib
}
\]

is a degree-two Blaschke product in the upper half-plane.

Therefore its de Branges--Rovnyak kernel is positive and has rank two:

\[
k_{a,\gamma}
\succeq0,
\qquad
\operatorname{rank}k_{a,\gamma}=2.
\]

## Hostile side

If

\[
a>0,
\]

then

\[
\Theta_{a,\gamma}
=
B_{a,\gamma}^{-1}.
\]

The kernel identity gives

\[
k_{a,\gamma}(z,w)
=
-
rac{
k_{B_{a,\gamma}}(z,w)
}
{
B_{a,\gamma}(z)
\overline{B_{a,\gamma}(w)}
}.
\]

Hence

\[
k_{a,\gamma}
\preceq0,
\]

and

\[
\operatorname{ind}_-(k_{a,\gamma})=2.
\]

This is the symmetry-completed counterpart of the rank-one half-orbit fixture.

## Crossing value

At

\[
a=0,
\]

one has

\[
\Theta_{0,\gamma}=1
\]

and the open-domain kernel is zero:

\[
k_{0,\gamma}=0.
\]

This statement concerns fixed interior observations. It does not describe the boundary-current limit.

## Boundary phase current

On the real boundary,

\[
\frac1i
\partial_t
\log
\Theta_{a,\gamma}(t)
=
-
\frac{2a}
{(t-
\gamma)^2+a^2}
-
\frac{2a}
{(t+
\gamma)^2+a^2}.
\]

Therefore, distributionally,

\[
\lim_{a\downarrow0}
\frac1i
\partial_t
\log
\Theta_{a,\gamma}(t)
=
-2\pi
(
\delta_{\gamma}
+
\delta_{-\gamma}
),
\]

whereas

\[
\lim_{a\uparrow0}
\frac1i
\partial_t
\log
\Theta_{a,\gamma}(t)
=
+2\pi
(
\delta_{\gamma}
+
\delta_{-\gamma}
).
\]

The crossing carries two boundary spectral-flow atoms, matching the index-two jump.

## Fixed-packet behavior

For every finite interior packet separated from \(\pm\gamma\), the Gram matrix tends to zero as \(a\to0\). Its two nonzero eigenvalues are of order \(|a|\).

Thus a fixed interior discretization sees two margins collapse to zero and then reappear with opposite sign.

After normalization, the two witness vectors concentrate at the boundary points \(\pm\gamma\). Uniform source control fails unless the topology retains these moving boundary traces.

## Crucial distinction from the completed endpoint pair

The crossing atoms occur at

\[
t=\pm\gamma
\]

on the continuous spectral boundary.

They are not the fixed completed endpoint evaluations

\[
z=
\pm i/2
\]

associated with \(s=0,1\).

Therefore the moving divisor crossing and the odd completed-endpoint line are not literally the same feature channel.

A finite-dimensional endpoint bundle cannot record crossings at arbitrary \(\gamma\). The correct boundary completion for moving interior divisors would require a boundary spectral measure or a full trace distribution along the real boundary.

This corrects the tempting interpretation that every interior defect transfers through the single odd endpoint line.

## Relation between the two negative mechanisms

The augmented inequality may contain both

\[
A_B^*A_B
\]

and

\[
b^*b,
\]

but they have different geometric origins:

1. \(A_B\) records moving forbidden divisor directions along the spectral boundary;
2. \(b\) records the fixed global endpoint residue at \(s=0,1\).

They combine in one Schur inequality because both subtract from the same positive bulk, not because they are generally one mode.

Only a crossing occurring at the distinguished endpoint coordinate could directly transfer between these two channels.

## Full symmetry orbit

In the centered spectral coordinate, the upper-half-plane poles are

\[
\gamma+ia,
\qquad
-
\gamma+ia.
\]

Their lower-half-plane reflected partners are supplied automatically by the denominator/numerator symmetry. Translating back to the \(s\)-coordinate gives the expected functional-equation/conjugation quartet.

Thus the family has the correct local orbit cardinality for an off-axis completed divisor.

## Krein--Langer channel

The index table is

| Regime | Numerator/denominator form | Positive rank | Negative index |
|---|---|---:|---:|
| \(a<0\) | degree-two Schur Blaschke numerator | 2 | 0 |
| \(a=0\) | constant multiplier | 0 | 0 in the open-domain kernel |
| \(a>0\) | degree-two Blaschke denominator | 0 | 2 |

The two boundary atoms at the crossing are the spectral-flow record of this rank transfer.

## Douglas channel

On the hostile side, the Schur feature is zero in the pure reciprocal fixture while the defect feature has dimension two:

\[
A_S=0,
\qquad
\dim
\overline{
\operatorname{ran}A_B
}=2.
\]

No Douglas map exists. Translated Gaussian observers detect both directions on a suitable finite packet.

On the positive side, the same two-dimensional model space appears with positive sign.

## Tetrahedral channel

The signed tetrahedron remains coherent across the family because the degree-two defect face is retained. The positive-lift fiber changes as follows:

| Regime | Positive-lift fiber |
|---|---|
| \(a<0\) | inhabited for the rank-two positive kernel |
| \(a=0\) | interior fiber degenerates; boundary-current limits remain nonzero |
| \(a>0\) | empty on a source-faithful carrier |

The discontinuity is analytical and metric, not combinatorial.

## Topological lesson

There are three relevant topologies:

1. compact-open interior observation, in which the kernel tends to zero;
2. fixed finite Gram topology, in which margins tend to zero;
3. boundary-current topology, in which nonzero delta atoms survive.

A completion using only the first two loses the index crossing. The source graph must state explicitly whether it retains the third.

## Regression requirements

Any proposed positive construction should satisfy:

1. positive rank two for \(a<0\);
2. two collapsing margins as \(a\uparrow0\);
3. boundary atoms at \(\pm\gamma\);
4. negative index two for \(a>0\);
5. failure of the Douglas map on the hostile side;
6. invariance of the signed tetrahedral identity;
7. no false absorption by the fixed rank-one endpoint line.

## Disposition

The symmetry-completed hostile family confirms the index-flow picture but separates two channels that had been conflated.

A moving off-axis divisor crosses through continuous boundary spectral-flow atoms. The fixed odd endpoint line is a different negative mechanism. They share one augmented Schur inequality but are not generally one geometric mode.
