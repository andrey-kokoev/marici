# The v3 faithful-joint-graph contract does not require the single-metric four-unit identity

## Question

Is Aspect's new `polarized-prime-cell-open-theorem.v1` a necessary constructor for the currently declared theta--RH interaction-net v3 interface?

## Claim boundary

Not under the literal v3 carrier and topology fields. Version 3 declares a faithful retained joint graph, multi-rung topology, no universal Riesz identification, and no undeclared quotient. Prior source constructs the first-Adams cell exactly as a joint graph of two typed realizations. Equality of their Green metrics is therefore an optional stronger single-metric refinement, not a prerequisite for existence of the v3 joint-graph edge.

## V3 declarations

The materialized contract

`research/aspect/contracts/theta-rh-interaction-net-state.v3.json`

declares:

- `analytic_carrier = faithful_retained_joint_graph_weighted_second_order_bilateral_relative_history`;
- source coordinate retained in the graph;
- a multi-rung projective/Hilbert/strong-dual topology;
- `universal_riesz_identification = false`;
- `undeclared_quotient = false`;
- contragredient transpose on each declared pairing.

These fields explicitly permit different typed output metrics and forbid silently collapsing them to one Hilbert target.

## Source first-Adams object

Prior construction gives

$$
\Gamma_{p,12}
=
\{(A_{p,12}x,C_{p,12}x):x\in E_{p,12}\},
$$

where the window/resolved and cut/Wronskian outputs remain distinct. The direct-sum form is

$$
\|A_{p,12}x\|_{\rm res,wall}^2
+
\|C_{p,12}x\|_{\rm cut,Wr}^2.
$$

This is precisely a faithful retained joint graph. It has zero radical locally, and global completion is complemented after retaining the labelled source coordinate.

## What the four-unit theorem asserts

The newer open-theorem contract asks for

$$
\mathfrak G_p^{\rm St}(e_j,e_k)
=
\mathfrak G_p^\theta
(Q_p^{\rm lin}e_j,Q_p^{\rm lin}e_k).
$$

This identifies the pullbacks of two independently typed metrics. It is necessary only if one demands that one realization replace the other isometrically in a single-metric output carrier.

It is not needed to form, close, polarize, or invert the joint graph, because both outputs and their common source already remain present.

## Nonimplication

From a closed joint graph one cannot infer the four-unit equality. Conversely, failure of one matrix-unit equality does not destroy the joint graph; it only proves that the two observers assign different energies to the same source direction.

Thus

$$
\text{joint-graph constructor}
\centernot\Rightarrow
\text{single-metric equality},
$$

and

$$
\neg(\text{single-metric equality})
\centernot\Rightarrow
\neg(\text{joint-graph constructor}).
$$

## Contract consistency options

Aspect can make the dependency graph consistent in either of two ways.

### Option A: faithful v3 semantics

Mark the first-Adams joint-graph edge constructed and classify the four-unit theorem as an optional `single_metric_descent` refinement. No quotient or metric identification occurs.

### Option B: single-metric successor

Amend the interface to declare that the Stieltjes output must descend isometrically into the theta Green target. Then the four-unit theorem is required, together with the quotient/descent map and its topology.

Option B is stronger than the current v3 descriptor and must be versioned rather than silently imposed.

## RH boundary

Neither option proves Evans membership or the prime-shell cancellation family. Joint-graph completion removes an interface-construction blocker; it does not annihilate

$$
B_\Sigma^\dagger\partial_z^ju(\cdot;z_0).
$$

## Disposition

Under the literal theta--RH v3 interface, the first-Adams faithful joint-graph edge is constructed and the four polarized matrix-unit identities are not required for that edge. They remain a meaningful optional test of single-metric descent. Treating them as mandatory requires a new contract field or successor version.