---
id: 419
date: 2026-08-17
title: Local Cartier Purity Descends to the Global Connector Operator
---

# Local Cartier Purity Descends to the Global Connector Operator

Entry 418 reduced the remaining finite realization gate to the operator
comparison
\[
\kappa B_{\rm ext}\simeq B_{\rm graph}\kappa
\]
on the assembled three-road connector. Entry 131 proves this comparison on
each marked road chart. The question is whether the three local comparisons
descend with a residual overlap choice.

They do. The overlap nerve used in Entry 398 is the full augmented
two-simplex
\[
\mathbb Z\longrightarrow\mathbb Z^3
\longrightarrow\mathbb Z^3\longrightarrow\mathbb Z
\]
with ranks \((1,2,1)\). In oriented bases,
\[
d_2=(1,-1,1)^T,\qquad
d_1=
\begin{pmatrix}
-1&-1&0\\
1&0&-1\\
0&1&1
\end{pmatrix},
\qquad
\epsilon=(1,1,1).
\]
All nonzero Smith factors are one.

More strongly, coning the simplex to the first chart gives an explicit
integral contraction. Therefore tensoring the nerve with the finite
operator lattice, and then with the flat Čech localization summands, remains
exact. Pairwise differences of local Cartier homotopies have a unique
integral filler, and the triple-overlap compatibility has no residual class.
Consequently
\[
\boxed{\kappa B_{\rm ext}=B_{\rm graph}\kappa}
\]
in the assembled finite filtered PC/Čech model.

## Nonvacuity

The descended equality is not obtained from the zero map. Its boundary
values were fixed independently:

- Entries 396--397 give the primitive generic roof
  \([\mathrm{top},D]\) with coefficient \(+1\);
- Entry 378 gives its nonzero generic Rees coefficient \(x_D\);
- Entries 131 and 391 give closed Cartier residue \(+1\);
- Entry 400 gives the unimodular endpoint comparison
  \[
  \begin{pmatrix}0&1\\1&0\end{pmatrix}
  \]
  of determinant \(-1\);
- Entry 398 supplies the full pairwise and triple Čech assembly.

Thus the generic \(Q\) leg, the closed Cartier face, and both endpoints are
restrictions of the same descended operator comparison.

## Consequence

Tensoring the assembled connector of Entries 397--400 with the external
Cartier packet of Entries 417--418 now produces a filtered chain map in the
finite PC/Čech category. Its carrier differential is
\(N/(1-r)/\epsilon\), and its coefficient operator is the actual
graph-Cartier Bockstein.

This closes the finite operator-realization gate. It does not yet construct
the complete geometric primal trace from the raw normalization-sheet
six-functor object, nor a smooth representative. The next audit should
compare the resulting filtered connector with the full Entry-143 target
filtration generator by generator after forgetting the external Cartier
filtration, ensuring that its cone contracts to the already proved
ordinary carrier map and introduces no extra homology.

The executable audit is
\`research/voevodsky/check_global_cartier_operator_descent.py\`.
