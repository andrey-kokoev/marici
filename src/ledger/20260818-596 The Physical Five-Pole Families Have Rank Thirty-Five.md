# 596 — The Physical Five-Pole Families Have Rank Thirty-Five

## Hard-to-vary claim

The complete homogeneous source families

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{23}}\},
\qquad
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{31}}\}
\]

have deletion-closed rank determined by the literal \(q_{G_{12}}\) residue geometry, not by the truncated rank-twenty-one subpacket.

## Deletion--restriction

For a generic nonresonant twisted complement, adjoining \(q_{G_{12}}\) gives

\[
\operatorname{rank}M_5
=
\operatorname{rank}M_4
+
\operatorname{rank}M_{4|G_{12}}.
\]

The primary source gives the homogeneous four-pole lower rank

\[
\operatorname{rank}M_4=15
\]

and the unmarked \(q_{G_{12}}\)-residue rank

\[
\operatorname{rank}M_{\varnothing|G_{12}}=9.
\]

The required restricted object is not that unmarked rank-nine module: all four lower pole lines remain marked on the residue surface.

## Exact residue incidence census

Set \(c=-E\). For the \(q_{g_{23}}\) summand the four lines are

\[
b=y+z,qquad
a=x+z,qquad
a+b=-z,qquad
b=x.
\]

The first three are forced-square Cayley--Menger boundary lines. Their restrictions have two distinct branch punctures. The final occurrence line is ordinary and has four distinct branch punctures.

Adjoin the lines in source order. The numbers of branch punctures and new finite intersections give:

\[
\begin{array}{c|c|c|c}
\text{line}&\text{branch}&\text{new finite}&\text{rank increment}\\
\hline
q_{g_1}&2&0&1\\
q_{g_2}&2&1&2\\
q_{g_3}&2&2&3\\
q_{g_{23}}&4&2&5
\end{array}
\]

because a line punctured at \(n\) distinct points contributes \(n-1\).

Therefore

\[
\boxed{
\operatorname{rank}M_{123,23}
=9+1+2+3+5=20.
}
\]

The occurrence-reflected \(q_{g_{31}}\) family has the identical census and rank.

The calculation reproduces at

\[
(x,y,z)=(2,3,4),\qquad(3,5,6)
\]

over \(\mathbb F_{32003}\).

## Five-pole rank

Deletion--restriction now gives

\[
\boxed{
\operatorname{rank}M_{123,G_{12},23}
=15+20=35,
}
\]

and likewise

\[
\boxed{
\operatorname{rank}M_{123,G_{12},31}=35.
}
\]

## Meaning

The complete source summand is neither the rank-twenty-one three-pole packet nor the generic six-scale rank-thirty-four lower family. Its homogeneous five-pole rank is thirty-five.

This result complements Entry 594:

- the residue target is a rank-twenty relative four-mark object;
- its shared-wall conductor boundary is generically nonzero;
- it does not descend canonically to the absolute rank-nine \(q_{G_{12}}\)-only module;
- ordinary infinity-Gysin projection is therefore not directly admissible.

No new carrier divisor is required. The additional fifteen directions are relative marked-line coefficient data over the frozen residue surface.

## Scope

This is an Euler-characteristic/deletion--restriction rank theorem at generic homogeneous kinematics. It does not construct a master basis, connection matrix, or the localization-triangle morphism to the elliptic infinity boundary.

## Next falsifier

Construct the rank-twenty residue localization complex explicitly:

\[
H^2(S_E\setminus W)
\longrightarrow
\bigoplus_i H^1(W_i^\nu\setminus C_i)
\longrightarrow
\bigoplus_{i<j}H^0(W_i\cap W_j),
\]

including the conductor residues of Entry 594. Then test whether a morphism of localization triangles to the infinity elliptic complex exists and determine the rank of its elliptic image.

## Artifacts

- research/benincasa/marici-gm/src/bin/five_pole_residue_euler_rank.rs;
- research/benincasa/five-pole-residue-euler-rank.json;
- frozen source applications.tex, lines 300--420;
- Entries 545, 590, and 594.
