# 2135 — Deleted Correlator Sectors Have Connected-Component Energy Poles

## Correction

Entries 2130--2134 assigned a single global translated total-energy pole to disconnected deletion graphs. The frozen correlator source instead factorizes each disconnected graph into connected components, with one energy denominator per component.

The grade-two global threshold and the grade-three Fermat quartic are therefore retracted as cosmological claims.

## Source rule

For deletion subset `S`, let

\[
G\setminus S=\bigsqcup_\alpha G_\alpha
\]

be its connected-component decomposition. The dashed term is a product of wavefunction/contact factors for the `G_\alpha`. Its singular energy normals are

\[
\boxed{
q_\alpha
=
\sum_{i\in V(G_\alpha)}X_i
+
\sum_{e\in S,\ e\text{ incident to }V(G_\alpha)}y_e,
}
\]

with each deleted edge occurrence contributing to the component containing its endpoint.

The sum over all component normals equals the translated global coordinate

\[
\sum_\alpha q_\alpha
=E_T+2\sum_{e\in S}y_e,
\]

but that sum is generally **not a denominator**.

## Grade-two sector

For `S={12,23}`, the retained edge `31` gives components

\[
G_{13}\sqcup G_2.
\]

Their poles are

\[
q_{13}=X_1+X_3+y_{12}+y_{23},
\qquad
q_2=X_2+y_{12}+y_{23}.
\]

The correct relative Landau calculations therefore constrain the sum of two loop distances to `-(X_1+X_3)` or `-X_2` separately. They do not constrain it to `-E_T/2`.

## Grade-three sector

With all edges deleted, the graph is the product of three isolated contacts. Its poles are

\[
\begin{aligned}
q_1&=X_1+y_{12}+y_{31},\\
q_2&=X_2+y_{12}+y_{23},\\
q_3&=X_3+y_{23}+y_{31}.
\end{aligned}
\]

There is no source pole

\[
E_T+2(y_{12}+y_{23}+y_{31})=0.
\]

Hence the Fermat sum-of-three-distances discriminant is not part of the correlator's Landau system.

## Surviving scope

Entries 2115--2118 remain valid. Entry 2119 remains valid as a kinematic translation packet after the pole/coordinate distinction above. Entry 2123 remains correctly typed because deleting one edge from the triangle leaves a connected path graph.

## Narrow lesson

\[
\boxed{
\text{translated global coordinate}
\not\Rightarrow
\text{global pole after graph disconnection}.
}
\]

The Carrier's connected-component typing prevents an attractive but false successor quartic.

## Correct next falsifier

Run the relative Landau calculation for the two grade-two component poles `q_2` and `q_{13}`. Then run the three grade-three contact poles `q_1,q_2,q_3` separately. Classify their thresholds and test whether any factor exceeds existing signed-energy, soft, and triangle support.

