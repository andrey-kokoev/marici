# 2728 — Moving Marked-Pole Relations Supply the Missing Rank-Twenty-Six Coherence

## Frozen question

Entry 2713 localized the differentiated Euler defect to a global failure of the parameter-dependent presentation. Differentiate the three pre-existing relation families separately:

1. integration-by-parts relations;
2. (K_{m CM})-multiplication relations;
3. the five labelled marked-pole multiplication relations.

For every raw generator, include its coefficient derivative and Gauss--Manin image before quotient reduction. Do not add a new relation after inspecting the defect.

## Generator inventory

At the reference point and ambient degree (14), the frozen relation inventory contains

\[
264\quad\text{IBP generators},
\]

\[
1792\quad K_{\rm CM}\text{-multiplication generators},
\]

and

\[
13200\quad\text{labelled marked-pole multiplication generators}.
\]

## Result

The differentiated IBP span does not contain the Euler defect. Its residual support is (39).

The differentiated (K_{m CM})-multiplication span also does not contain the defect. Its residual support is (30).

The differentiated marked-pole multiplication span does contain the complete defect. Exact containment occurs after processing 891 predeclared generators, whose derived span has rank 823. The residual support is zero.

Thus

\[
\operatorname{Def}_{E,j}
\in
\operatorname{span}
\left(
\nabla_j R_{q,\alpha}
\right),
\]

where the (R_{q,\alpha}) are the original labelled marked-pole multiplication relations.

## Interpretation

The second-jet failure of Entry 2708 is not a failure of source homogeneity and does not require a fitted correction cell. It arises because the finite adapter transported quotient classes while omitting the coherence of the moving marked-pole relation presentation.

This is a source-derived port-adapter phenomenon: parameter transport and quotient formation commute only after retaining the derivative of the labelled relation map.

The result is currently proved for the (x)-direction at the reference point. Cyclic transport and independent-point replication remain required before globalizing it.

## Artifact

- `research/benincasa/check_rank26_moving_relation_coherence.py`
- `research/benincasa/rank26-moving-relation-coherence.json`

## Next falsifier

Split the marked-pole coherence span by the five occurrence labels. Determine the minimal labelled subset that absorbs the defect, then test the corresponding subsets in the (y) and (z) directions and at one independent control point. A non-covariant subset would reveal a chart artifact; a cyclically transported subset would establish the missing adapter cell.
