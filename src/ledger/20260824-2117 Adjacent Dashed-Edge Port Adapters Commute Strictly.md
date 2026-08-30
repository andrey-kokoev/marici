# 2117 — Adjacent Dashed-Edge Port Adapters Commute Strictly

## Hard-to-vary claim

The source-defined Kummer port adapters for two distinct deleted edges commute strictly, including when the edges share a site.

For the adjacent triangle edges `12` and `23`,

\[
T_{12}T_{23}=T_{23}T_{12}.
\]

## Calculation

For a function `f(x_1,x_2,x_3)`, both orders give

\[
\frac{1}{y_{12}y_{23}}
f(
x_1+y_{12},
x_2+y_{12}+y_{23},
x_3+y_{23}
).
\]

The endpoint translations commute because they are additive, and the rank-one Kummer factors commute because they are scalar and carry distinct occurrence labels.

The same argument applies to disjoint edges and to every face of the three-edge Boolean deletion cube.

## Test

`research/benincasa/checkers/dashed_edge_pair_commutator.rs` verifies the cleared identity exactly over integers for a mixed polynomial at three signed sample loci. The general identity follows directly from commutativity of translations and scalar multiplication.

## Consequence

The edge-deletion rule supplies no nontrivial square coherence:

\[
[T_e,T_f]=0.
\]

Therefore the missing coefficient extension of Entry 2113 is not hidden in the ordering of the source dash operations. The full three-edge adapter is the tensor product of three commuting labelled Kummer ports.

This further narrows the possible home of integrated cosmological complexity:

\[
\boxed{
\text{not the deletion carrier}
\quad|\quad
\text{not a dash-order commutator}
\quad|\quad
\text{possibly integration/relative-cycle or period-extension data}.
}
\]

## Next falsifier

Apply one dashed-edge adapter to an actual marked relative Gauss--Manin sector and test whether the source integration chain is carried functorially under endpoint translation and Kummer twisting.

The first possible obstruction is no longer algebraic order dependence. It is failure of the **relative chain or marked divisor** to transport with the coefficient object.

