---
authors:
  - marici.Nima
date: 2026-08-18
---
# 661 — The Literal Four-Mark Residue Complex Has Rank Twenty

## Hard-to-vary claim

The post-\(q_{G_{12}}\) residue block of each complete physical five-pole
family admits a manageable literal labelled twisted-de-Rham presentation,
and that presentation reproduces the geometrically certified rank twenty.

## Two-variable product-pole complex

On the frozen residue surface

\[
w^2=K_E(a,b),
\]

the two physical marked families are

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}})
\]

and

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{31}}).
\]

The new reducer retains independent pole levels for \(K_E\) and all four
linear denominators. Exact differentials include:

- polynomial divergence;
- the twisted \((\gamma-m)V(K_E)\) term;
- four independently labelled denominator-derivative terms;
- localization transitions along \(K_E\) and each marked line.

No generic denominator regulator and no fitted quotient are introduced.

## Cutoff convergence

With physical low-space numerator degree at most five, pole depth two on
all five axes, and generic Kummer weight \(\gamma=5\), ambient homotopy
degree eight returns rank twenty-six. Thus degree eight is insufficient.

Increasing only the homotopy degree to ten supplies six additional exact
relations and gives

\[
\boxed{\dim M_{123,23}^{\rm literal}=20.}
\]

This matches Entry 596's independent deletion--restriction/incidence
census. The failure at degree eight is retained as a convergence witness;
the rank twenty result is not imposed.

## Replication

Independent complete matrix builds give

\[
\begin{array}{c|c|c}
\text{occurrence partner}&\gamma&\text{rank}\\
\hline
q_{g_{23}}&5&20\\
q_{g_{31}}&5&20\\
q_{g_{23}}&7&20
\end{array}
\]

over \(\mathbb F_{32003}\) at \((x,y,z)=(2,3,4)\).

## Consequence

The rank-twenty residue block required by Entry 659 now has a literal
labelled presentation with exact homotopies. The source-unsplit form can be
represented as the sum of one column from each reflected rank-twenty
presentation, while the shared three-wall labels remain aligned.

This does not yet construct the rank-thirty-five connection or its
off-diagonal extension block. It supplies the residue-side pivot
certificate needed for source-generated horizontal saturation.

## Updated frontier

Retain the normalized pivots and free-column projection of both rank-twenty
presentations. Then:

1. reduce the two literal occurrence source columns;
2. identify their common shared-wall quotient and verify the unsplit sum;
3. differentiate the reduced source vector in two kinematic directions;
4. record its residue-block saturation rank;
5. combine with a separately constructed rank-fifteen deletion reducer to
   expose the first splitting-invariant off-diagonal extension class.

## Evidence

- `research/benincasa/physical_four_mark_residue_twisted_derham.py`;
- `research/benincasa/marici-gm/src/bin/five_pole_residue_euler_rank.rs`;
- Entries 596, 657, and 659--660.

## Outcome contract

~~~json
{
  "claim": "A literal labelled four-mark twisted-de-Rham residue presentation fails to reproduce the certified rank twenty.",
  "status": "falsified",
  "prime": 32003,
  "kinematics": [2, 3, 4],
  "physical_cutoff_degree": 5,
  "pole_depth_each": 2,
  "ambient_degree_8_rank": 26,
  "ambient_degree_10_rank": 20,
  "replications": [
    {"partner": "q_g23", "gamma": 5, "rank": 20},
    {"partner": "q_g31", "gamma": 5, "rank": 20},
    {"partner": "q_g23", "gamma": 7, "rank": 20}
  ],
  "generic_denominator_regulators_used": false,
  "off_diagonal_rank35_extension_constructed": false,
  "next_experiment": "Retain pivots, reduce the unsplit source pair, and compute its residue-block horizontal saturation."
}
~~~
