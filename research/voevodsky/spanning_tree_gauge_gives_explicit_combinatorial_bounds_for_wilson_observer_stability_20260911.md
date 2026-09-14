# Spanning-tree gauge gives explicit combinatorial bounds for Wilson-observer stability

## Question

Can the graph-dependent bi-Lipschitz constant for the basis-independent all-cycle Wilson observer be bounded explicitly from the finite graph and its edge weights?

## Claim boundary

The packet gives explicit lower and upper bounds for a finite connected graph with positive edge weights and at least one cycle. The observer contains real and imaginary quadratures for every oriented simple cycle, with the ordinary Euclidean target metric. A spanning tree is used only to prove and optimize the bound; the quotient metric and all-cycle observer remain basis independent. No sharpness or graph-uniform lower bound is asserted.

## Setup

Let \(\Gamma=(V,E)\) be finite and connected. Give each unoriented edge a weight

\[
\lambda_e>0.
\]

On the edge torus \(\mathbb T^E\), use

\[
d_E(z,z')^2
=
\sum_{e\in E}\lambda_e|z_e-z'_e|^2.
\]

The vertex-gauge quotient metric is

\[
d_\Gamma([z],[z'])
=
\inf_g d_E(z,g\cdot z').
\]

Let \(\mathscr C(\Gamma)\) contain all oriented simple cycles and define

\[
\Psi_\Gamma([z])
=
\bigl(
\operatorname{Re}\operatorname{Hol}_c(z),
\operatorname{Im}\operatorname{Hol}_c(z)
\bigr)_{c\in\mathscr C(\Gamma)}.
\]

Since a real/imaginary pair has Euclidean distance equal to complex chord distance,

\[
\|\Psi_\Gamma([z])-\Psi_\Gamma([z'])\|^2
=
\sum_{c\in\mathscr C(\Gamma)}
|\operatorname{Hol}_c(z)-\operatorname{Hol}_c(z')|^2.
\]

## Explicit lower bound from a spanning tree

Fix a spanning tree \(T\subset E\). Every gauge orbit has a representative with

\[
z_e=1
\quad(e\in T).
\]

For each chord \(e\in E\setminus T\), let \(c_e\) be the fundamental simple cycle formed by \(e\) and the unique tree path joining its endpoints. In tree gauge, the chord coordinate equals its fundamental holonomy up to inversion:

\[
z_e=\operatorname{Hol}_{c_e}(z)^{\pm1}.
\]

Take tree-gauge representatives \(\widehat z\) and \(\widehat z'\) of two moduli points. Since quotient distance is an infimum,

\[
\begin{aligned}
d_\Gamma([z],[z'])^2
&\le d_E(\widehat z,\widehat z')^2\\
&=
\sum_{e\notin T}\lambda_e
|\operatorname{Hol}_{c_e}(z)-
\operatorname{Hol}_{c_e}(z')|^2\\
&\le
\Lambda_T
\sum_{e\notin T}
|\operatorname{Hol}_{c_e}(z)-
\operatorname{Hol}_{c_e}(z')|^2,
\end{aligned}
\]

where

\[
\Lambda_T=
\max_{e\notin T}\lambda_e.
\]

Every fundamental cycle occurs among the all-cycle coordinates, hence

\[
\|\Psi_\Gamma([z])-\Psi_\Gamma([z'])\|
\ge
\frac{1}{\sqrt{\Lambda_T}}
 d_\Gamma([z],[z']).
\]

Thus one explicit lower constant is

\[
\alpha_{\Gamma,T}=
\Lambda_T^{-1/2}.
\]

## Basis-independent optimized lower bound

Define the cotree bottleneck

\[
\Lambda_{\mathrm{cot}}(\Gamma,\lambda)
=
\min_{T\text{ spanning tree}}
\max_{e\notin T}\lambda_e.
\]

The set of spanning trees is finite. Choosing a minimizing tree in the proof gives the basis-independent numerical bound

\[
\alpha_\Gamma
\ge
\Lambda_{\mathrm{cot}}(\Gamma,\lambda)^{-1/2}.
\]

The definition uses no selected tree. A minimizing tree is a certificate for the bound, not part of the moduli coordinates.

For equal edge weights \(\lambda_e=1\),

\[
\alpha_\Gamma\ge1.
\]

This does not claim that the optimal lower constant equals one; redundant cycle coordinates can make it larger.

## Explicit upper bound

For a simple cycle \(c\), telescoping products of unit phases give

\[
|\operatorname{Hol}_c(z)-
\operatorname{Hol}_c(z')|
\le
\sum_{e\in c}|z_e-z'_e|.
\]

Weighted Cauchy--Schwarz yields

\[
|\operatorname{Hol}_c(z)-
\operatorname{Hol}_c(z')|^2
\le
\left(
\sum_{e\in c}\lambda_e^{-1}
\right)
 d_E(z,z')^2.
\]

Because holonomy is gauge invariant, this estimate holds after replacing \(z'\) by any gauge translate. Taking the gauge infimum and summing cycles gives

\[
\|\Psi_\Gamma([z])-\Psi_\Gamma([z'])\|
\le
L_\Gamma d_\Gamma([z],[z']),
\]

with

\[
L_\Gamma^2
=
\sum_{c\in\mathscr C(\Gamma)}
\sum_{e\in c}\lambda_e^{-1}.
\]

If both orientations of each geometric cycle are included, this sum counts both. Removing reverse duplicates and retaining both quadratures gives a smaller target and correspondingly smaller upper bound without changing orbit separation.

## Coarser combinatorial bounds

Let

\[
\lambda_{\min}=
\min_{e\in E}\lambda_e,
\qquad
\lambda_{\max}=
\max_{e\in E}\lambda_e.
\]

Then

\[
\alpha_\Gamma
\ge
\lambda_{\max}^{-1/2}.
\]

Also,

\[
L_\Gamma^2
\le
\lambda_{\min}^{-1}
\sum_{c\in\mathscr C(\Gamma)}|c|.
\]

These bounds require only extremal edge weights and the total simple-cycle length. They can be much weaker than the spanning-tree and cycle-weight formulas.

## Product-observer constant

If the bulk/source observer has lower constant \(\delta_X\), then the basis-independent product observer satisfies

\[
\delta_{\mathrm{product}}
\ge
\min\left(
\delta_X,
\Lambda_{\mathrm{cot}}^{-1/2}
\right).
\]

This is an explicit graph-combinatorial replacement for the previous existential constant \(\min(\delta_X,\alpha_\Gamma)\).

The bound remains relative to the declared edge weights and the unweighted Euclidean norm on all-cycle quadratures. Rescaling either metric changes the numerical constant as expected.

## Example: square with one diagonal

Take the graph with four vertices, four perimeter edges, and one diagonal. Its first Betti number is two. With unit edge weights, every spanning tree has two chords and

\[
\Lambda_T=1.
\]

Therefore

\[
\alpha_\Gamma\ge1.
\]

A fundamental cycle family consists of one triangle and the perimeter square, or the two triangles. The all-cycle observer contains either family, so its lower estimate does not depend on choosing between them.

The existing \(\mathbb Z/4\) shadow checker exhaustively finds 16 gauge orbits and verifies that the redundant all-cycle signatures separate them. That finite result tests separation, not the continuous numerical bound proved here.

## Algorithmic certificate

For a fixed weighted graph:

1. enumerate spanning trees;
2. compute \(\max_{e\notin T}\lambda_e\) for each;
3. choose the minimum as \(\Lambda_{\mathrm{cot}}\);
4. enumerate unoriented simple cycles;
5. compute \(L_\Gamma^2\) from reciprocal edge weights;
6. report the metric conventions with both bounds.

For the lower bound alone, full cycle enumeration is unnecessary. The cotree bottleneck can be found by a weighted spanning-tree optimization.

## Constructor-role consequences

- the edge weights define the quotient metric;
- a spanning tree supplies a proof certificate;
- fundamental holonomies supply a lower-bound subobserver;
- the all-cycle family supplies basis-independent presentation;
- the cotree bottleneck supplies a basis-independent numerical bound;
- none of these creates bulk coercivity.

## Deliberate failures

1. A bound from one tree is valid but not optimized; it must not be called canonical without minimizing or retaining the tree label.
2. Omitting a fundamental chord cycle destroys the displayed lower-bound proof and may destroy separation.
3. Counting reverse cycles twice changes the upper constant but not the moduli dimension.
4. The unit-weight bound does not survive arbitrary rescaling of edge weights.
5. A graph-dependent lower bound is not uniform over graphs with unbounded edge weights.
6. The finite \(\mathbb Z/4\) orbit test does not prove the continuous chord inequality.

## Disposition

The formerly existential lower constant now has an explicit combinatorial bound. Tree gauge identifies chord coordinates with fundamental holonomies, giving \(\alpha_\Gamma\ge\Lambda_{\mathrm{cot}}^{-1/2}\). Weighted telescoping gives an explicit all-cycle upper bound. The construction remains basis independent because the metric and observer do not select a tree; spanning trees appear only as finite optimization certificates.
