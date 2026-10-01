# Minimality of the twelve-triangle collective-identity net

## Result

**Stagewise geometry qualification:** the [bare-operator audit](stagewise-geometric-positivity.md) did not certify geometric transitions. Subsequent [explicit atlas witnesses](stagewise-positive-atlas-witness.md) now attain the 73/72 bounds with stagewise positive geometry for the registered positive-homothetic family and a declared shared immutable atlas. These remain conditional coefficient-network minima, not general geometric-formation minima.

The 1836-arrow graph is **pruning-minimal with its weights held fixed**, but **not minimal among implementations of the same collective identity**.

With the same twelve-triangle geometry and the same full input/output projector N:

| Implementation | Directed arrows |
|---|---:|
| Original local/symmetry/dense-feedback graph | 1836 |
| Same local and symmetry stages, identity-wire feedback | 576 |
| Factored three-stage graph | 73 |
| Factored two-pass graph | 72 |

The 73- and 72-arrow bounds are attained minima in their respective linear, layered network classes with 36 fixed visible coefficient ports and arbitrary disjoint auxiliary interfaces. Every arrow in each factored graph lies on a positive-weight closed return traversal.

## Observable retained by the comparison

Let u be the 36-component assembled vector from `twelve-triangle-positive-geometry.md`. Its entries lie in Q(i*sqrt(3)), every entry is nonzero, and u^dagger u=80. The required return is

    N=u u^dagger/80.

Equality is required on EVERY input, including inputs outside the collective line. This excludes the trivial shortcut of replacing the projector by a full identity operator.

The original graph implements N G L=N, where L selects the local eigenlines and G averages the tetrahedral action. Its spatial surface and tetrahedral action are independent of how the linear map is factored.

## The original graph cannot be pruned at fixed weights

Each of its 1296 closed three-step cycles has positive real weight. These weights sum to trace(N)=1. All 1836 arrows occur in at least one such cycle.

Deleting any arrow removes a positive cycle contribution. Deleting additional arrows cannot restore that contribution or create new cycles. Hence every proper edge-deleted subgraph, with the remaining weights unchanged, has return trace strictly less than one and cannot implement N.

This proves inclusion/pruning minimality, including deletion of several arrows at once. It does not prohibit reweighting or refactoring the maps.

## Direct counterexample to implementation-size minimality

Replace dense feedback N by 36 identity wires. Then

    I G L = N.

The input/output map is unchanged and the graph uses 108+432+36=576 arrows. The three-stage clock and all 108 stage ports can be retained. This alone refutes unrestricted size-minimality of 1836.

## A smaller collective-mode factorization

Take one gathering map and one distribution map:

    B=u^dagger/80, A=u.

Then

    AB=N, BA=1.

The auxiliary port therefore represents exactly one collective mode. Gathering and returning preserves the full target projector, including its suppression of components orthogonal to u.

The primitive arrows are

    coefficient_i -> Omega    weight conjugate(u_i)/80,
    Omega -> coefficient_i    weight u_i,

for all 36 coefficient ports. There are 72 distinct directed endpoint pairs, with no self-loops.

If contractive individual stages are desired, rescale the auxiliary coordinate to use A'=u/sqrt(80) and B'=u^dagger/sqrt(80). Both have operator norm one, B'=A'^dagger, and their support and composition are unchanged. The checker uses the rational/quadratic-field factors to retain exact arithmetic.

Every pair of arrows through coefficient_i is a closed two-step walk. Its weight is |u_i|²/80>0. These 36 walks cover all 72 arrows and their weights sum to one.

## Proven two-pass lower bound: 72

Consider any factorization N=A B with a disjoint auxiliary interface of arbitrary dimension. Each nonzero matrix coefficient is one directed arrow.

1. N has 36 nonzero input columns. B must therefore have a nonzero entry in every input column: at least 36 gathering arrows.
2. N has 36 nonzero output rows. A must have a nonzero entry in every output row: at least 36 returning arrows.
3. The opposite-direction arrows between visible and auxiliary interfaces are distinct endpoint pairs.

Therefore every network in this class has at least 72 arrows. The one-mode factorization attains the bound.

## Preserve three stages: proven lower bound 73

Keep the original three-step return schedule by using two one-dimensional auxiliary interfaces:

    coefficient ports --B--> Omega_local --1--> Omega_aligned --A--> coefficient ports.

This uses 36+1+36=73 arrows, and the full composition is still N. Its 36 closed three-step walks cover every arrow and have positive weights summing to one.

For ANY three-stage, no-bypass linear factorization N=C B A with disjoint stages:

- the first stage needs at least 36 arrows, because all input columns of N are nonzero;
- the middle stage needs at least one arrow, because N is nonzero;
- the final stage needs at least 36 arrows, because all output rows of N are nonzero.

Thus 73 is an attained minimum when intermediate dimensions may be compressed. This preserves the number of stages and the exact collective identity, while replacing the original intermediate 36-coordinate presentations by sufficient one-dimensional interfaces.

These theorems do not cover architectures with bypasses, arbitrary recurrent timing, implicit free summation, or a different definition of primitive arrow. Additional requirements to preserve each intermediate map L, G and N separately would be a different optimization problem.

## Geometry and symmetry

The twelve triangle placements, supporting planes and enclosed volume 8/3 are unchanged. The assembled vector u is invariant under the combined tetrahedral action on triangle labels and spatial coordinates. Thus A intertwines the trivial one-dimensional collective representation with the original coefficient representation, and B intertwines in the opposite direction.

The auxiliary collective mode can be associated with the fixed tetrahedral centre. Its addition does not alter the boundary triangulation. No original visible coefficient port is discarded.

## Verification

    python research/nima/checkers/check_twelve_triangle_net_minimality.py

Exact checks verify the original positive-cycle pruning argument, all three input/output factorizations, every visible input basis vector, tetrahedral equivariance, unchanged geometry, closed-walk coverage, positive return weights and single-arrow deletion controls for the two-pass construction.

Artifacts:

- `results/twelve-triangle-net-minimality.json`
- `results/twelve-triangle-72-arrows.json`
- `results/twelve-triangle-73-arrows.json`
