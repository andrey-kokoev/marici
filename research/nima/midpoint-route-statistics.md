# Midpoint ancestry routes: multiplicity, cost and variance

## Question

The operator conjectured that the recursively averaged assembly walk might contain statistical thermodynamics and requested a test. This is a non-evidential search direction, tested here on the existing regular tetrahedron, not a premise identifying geometry with physical energy.

SCC obligation: readout descent. Does a declared geometric route cost factor through its terminal stage? The source is the equal-weight midpoint operation on the four barycenters of each vertex-insertion order. All 24 orders are tested. There is no physical-time map.

## Claim boundary

Unfold the midpoint computation into a binary ancestry tree. Starting at its root, choose either input at each of three levels with probability 1/2. The eight route records retain their bit strings, nodes, edge costs and terminal stages. Stage k has multiplicity binomial(3,k); equal weighting returns the original recursively averaged state.

Two costs were declared for testing, not derived as a unique WG energy:

1. Assembly cost: sum of squared displacements along the four original barycenters.
2. Ancestry-route cost: sum of squared displacements along a root-to-leaf route through the midpoint computation.

These are different path spaces. All assembly orders have cost 3, so this cost cannot distinguish their common-endpoint constructions. In contrast, midpoint ancestry cost does not descend to its terminal stage.

### Counterexample and exact spectrum

For order ABCD, routes 001 and 010 both start at (5/8,1/4,0) and end at the edge barycenter (1,0,0). Their costs are respectively 143/192 and 79/192. The eight route costs are

    43/192, 59/192, 79/192, 143/192,

with multiplicity two each. This table is unchanged by all 24 vertex orders. Conditional cost variances at terminal stages 1 and 2 are 361/10368 and 61/10368. Thus replacing every route by a single cost attached to its stage erases information. Replacing costs by their conditional mean also fails to reproduce the exponential weights at second order in the weighting parameter.

### Mean preservation and variance

The midpoint rule itself, without an energy interpretation, implies that the expected next ancestry node conditional on the current route prefix is the current node. This is a vector martingale indexed by ancestry depth. Its increments have zero cross-correlation in expectation; no claim of pathwise orthogonality is needed. Consequently

\[
\mathbb E\!\left[\sum_j\|X_{j+1}-X_j\|^2\right]
=\mathbb E\|X_3-X_0\|^2
=\frac{27}{64}.
\]

The checker verifies every conditional-mean identity and this exact variance equality. The variance of route cost itself is 361/9216, distinct from the variance of terminal state.

### Entropy and optional Gibbs weighting

Under fair ancestry choices, the route entropy in nats is 3 ln(2). Stage probabilities are (1,3,3,1)/8, giving

\[
H(K)=3\ln2-\frac34\ln3,
\qquad H(\text{route}\mid K)=\frac34\ln3.
\]

For the declared squared-displacement cost E, one may additionally choose Gibbs weights, with

\[
Z(\beta)=2\left(e^{-43\beta/192}+e^{-59\beta/192}
+e^{-79\beta/192}+e^{-143\beta/192}\right).
\]

Then -d ln(Z)/d beta is the weighted mean cost and d² ln(Z)/d beta² its variance. These follow by differentiating the displayed finite sum; the checker records exact derivatives of Z at zero. The original midpoint average corresponds to beta=0. Nonzero beta is an additional reweighting rule, not the original averaging operation and not a derived inverse physical temperature. It generally changes the expected terminal state.

## Falsification and disposition

- Conjecture tested: geometric cost can distinguish routes with the same endpoint.
- Rival: every candidate cost is endpoint-only. Refuted for squared ancestry cost by the explicit pair above, but the assembly-order test has equal costs.
- Rival: route dependence is unavoidable. Refuted by a potential-difference cost: summing squared-norm differences telescopes to an endpoint-only value on the same routes.
- Scale control: doubling all coordinates multiplies squared costs by four. Geometry supplies no absolute energy unit.
- Surviving scope: an exact eight-route statistical model, mean-preserving ancestry and a cost-dependent failure of endpoint descent. Native WG cost selection, physical energy and temperature, equilibration and a thermodynamic limit remain unprovided; none are inferred from finite partition-function notation.

Verification: `python research/aspect/scc/scc.py check nima-midpoint-route-statistics` passed, execution `structured_command_execution:e_32876_1791222492146597900_21`. Checker: `checkers/check_midpoint_route_statistics.py`; results: `results/midpoint-route-statistics.json`; owner-local manifest: `scc-models/midpoint-route-statistics.json`. SCC reports checker exit-code evidence, not physical certification. No commit or publication is claimed.
