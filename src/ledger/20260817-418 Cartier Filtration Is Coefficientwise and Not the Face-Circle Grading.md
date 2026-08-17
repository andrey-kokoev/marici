---
id: 418
date: 2026-08-17
title: Cartier Filtration Is Coefficientwise and Not the Face-Circle Grading
---

# Cartier Filtration Is Coefficientwise and Not the Face-Circle Grading

Entry 417 constructed the four-term filtered module and proposed placing its
eight Cartier states over the fixed occurrence/Čech target. A literal
identification of Cartier exterior degree with Entry-105's normal-circle
number is impossible.

For a facewise generator \((S,H)\), normal-circle number is \(|H|\) and
chain degree is \(3-|S|+|H|\). After removing the two endpoint packets, the
bigraded ranks of \(F_K/F_V\), with rows indexed by chain degree and columns
by face-circle number, are
\[
\begin{array}{c|rrrr}
 &0&1&2&3\\ \hline
0&12&0&0&0\\
1&21&36&0&0\\
2&9&42&36&0\\
3&1&9&21&12
\end{array}
\]
and their row sums are \((12,57,87,43)\).

The Gysin-collapsed source has Cartier filtration profiles
\[
\begin{array}{c|rrrr}
 &0&1&2&3\\ \hline
0&1&3&3&1\\
1&3&9&9&3\\
2&3&9&9&3\\
3&1&3&3&1.
\end{array}
\]
The literal identification fails in bidegrees
\[
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3).
\]
In particular, degree-zero Tate states carry all four Cartier levels, while
a degree-zero facewise PC generator necessarily has \(H=\varnothing\).

This is not a new obstruction. It proves that the two gradings encode
different geometry:

- \(H\subseteq S\) records original/Borel--Moore normal circles already
  supported on a PC face;
- the Cartier exterior degree records independent multi-Rees conormal
  filtration transported by extraordinary purity.

They must not be identified.

## Correct target type

The realization target must be treated as
\[
\boxed{
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\widehat\otimes
\Lambda^\bullet N_{\rm Cart}^{\vee},
}
\]
where the exterior packet is coefficientwise and Gysin shifted, so it does
not alter cellular chain degree. On this object:

- the Entry-143 differential acts on the PC/Čech factor;
- the Cartier Bockstein acts on the external coefficient factor;
- the two operations commute formally before the geometric graph-Cartier
  comparison is imposed.

The coefficientwise target has enough capacity in every bidegree. This is
again only a typing and capacity theorem. The remaining nonformal step is to
identify the external Cartier action with the actual graph-Cartier can--var
operation using Entry 131's local purity maps and the three-connector Čech
assembly.

Thus the next gate is not a search for 64 target cells. It is one global
operator comparison:
\[
\kappa\,B_{\rm ext}\simeq B_{\rm graph}\,\kappa
\]
on the assembled connector, including the generic \(Q\) roof and endpoint
restrictions.

The executable audit is
\`research/voevodsky/check_cartier_face_circle_type_separation.py\`.
