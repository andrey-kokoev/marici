# Boundary obligations generalize formula bounds but can leave free selectors

## Result

The hexagon argument now has a reusable exact certificate format for two-dimensional polyhedral images. It separates:

1. certified forced boundary lifts;
2. compatibility of boundary obligations with one affine source formula;
3. a formula-count lower bound from covering those obligations;
4. a conditional finite-formula approximation-error bound.

A nonsymmetric owning example shows why the fourth step needs an additional premise. Its boundary still forces at least three formulas, but a minimum cover can leave one formula underdetermined. Discarding that free family would produce a false positive error lower bound.

Both workloads and nine corruption controls pass. The earlier optimal three-formula approximation verifier also passes unchanged.

## General source and coverage certificate

Let the independently expected source be

    P={x: A*x<=b},

with a rational two-coordinate observer y=O*x. The proposed public domain is a nondegenerate convex polygon D.

For each polygon edge with supporting inequality n*y<=beta, the packet supplies nonnegative multipliers lambda such that

    lambda^T*A=n*O,
    lambda^T*b=beta.

This proves O(P) is contained in every declared polygon halfspace. Admitted source lifts at all polygon vertices prove the reverse inclusion by convexity. Hence O(P)=D; the polygon is not accepted merely because a candidate claims coverage.

Source rows and observer coordinates come from the expected model. They are never replaced by a candidate's advertised source constraints.

## A sufficient gate for forced boundary lifts

At a point of the supported edge, the weighted source inequality is saturated. Every source row with positive multiplier must therefore be an equality.

Stack those active row normals with the observer rows. If the stacked matrix has full source-column rank, those equalities and the public point determine a unique source vector. Admitted endpoint lifts interpolate to a source lift over the whole edge, so this determines the complete forced affine edge map.

Rank deficiency of one certificate does NOT prove nonuniqueness. The negative branch instead requires two distinct admitted source vectors at the same interior point of the edge. The checker verifies both against the expected source rows and observer.

This is a sufficient certificate interface, not a claimed complete procedure for finding all possible forcing proofs.

## Affine compatibility and the cover lower bound

For each nonempty subset of certified forced edges, solve the simultaneous interpolation equations

    F(y_endpoint)=x_endpoint

for an affine source map F on the public plane.

An inconsistent system rules out one formula serving that group. A consistent system is recorded as:

- **pinned**, when the public endpoint equations determine the entire affine map;
- **free**, when coefficients remain undetermined.

The verifier reconstructs EVERY subset classification. A producer cannot increase the lower bound by silently omitting a compatible group.

Let L be the minimum number of compatible groups covering all forced edges. Then every finite-formula admissible selector requires at least L affine formulas.

Reason: on a forced edge, an affine formula either agrees with its entire affine lift or matches it at at most one point. Finitely many isolated coincidences cannot cover the edge. Thus some formula must serve each whole forced edge, and each formula's assigned edges form a compatible group.

The implementation enumerates minimum partitions rather than overlapping covers. This is equivalent for the lower bound because compatibility is hereditary: a cover can assign each edge to one covering group and discard empty groups.

Boundary compatibility is only a necessary condition for a complete selector. The resulting count is a lower bound, not a claim that every compatible cover extends to a continuous, globally admissible section.

## When a finite error bound follows

Suppose a selector is allowed at most L formulas, and EVERY group in EVERY minimum partition is pinned. Every formula must participate in covering the boundary; otherwise fewer than L formulas would cover it. Its affine map therefore belongs to the finite pinned list.

At a specified public probe y, the selector must return one of those maps evaluated at y. Against an independently fixed reference value S0(y),

    min_F ||F(y)-S0(y)||_infinity

is a lower bound on uniform approximation error. Including pinned maps that fail other admissibility conditions only weakens this bound, so the argument remains sound.

The implementation deliberately refuses this finite-list error argument if a minimum partition contains a free group. This condition is sufficient, not necessary for every conceivable error proof; further analysis of free coefficients could establish other bounds.

## Recovery of the original hexagon result

For the owning three-atom box with t0<=10, t1<=102 and t2<=104, all six public edges have forced lifts.

There are fifteen nonempty compatible groups: six singletons and nine pairs. No compatible group contains three edges. The minimum formula bound is three, with six minimum partitions. Every minimum partition consists of pinned pairs; singletons cannot participate at this minimum count.

For the previously fixed six-formula reference and its center probe, the generic checker recovers the lower bound 129/1000 in original atom infinity norm. This reproduces the earlier specialized argument without hard-coding its pair-count conclusion into the general gate.

## Nonsymmetric owning control

Append the public frame

    U<=162

to the SAME verified retirement. This clips the original hexagon into another hexagon that is not centrally symmetric. Its three opposite-vertex sums differ, providing an exact check of that fact.

Five old boundary edges survive, possibly shortened, and their source lifts remain forced. The new U=162 edge is different: its defining source normal is the U observer itself. Its support certificate supplies no additional independent source equation.

At the midpoint of this new edge, the source vectors

    (5,80,77)
    (5,80,77)+(1,-129,128)/1000

are distinct, obey all original fine constraints and U<=162, and have identical public observations. Thus the new edge is genuinely nonunique, not merely unsupported by a chosen proof.

The five forced edges still require three formulas. But every minimum partition now leaves a singleton obligation alongside two pairs. A singleton fixes a formula only on an edge, leaving a free affine family in the interior.

## A concrete failure of the naive finite-list inference

Choose as the reference on the clipped domain the lower-fiber section. In the source box its three affine pieces lie on the faces

    t0=0,  t1=102,  t2=0.

The producer triangulates their projected faces and clips them by U<=162. The resulting reference has three distinct affine formulas and eight triangles. Full source admission, polygon coverage and continuity are verified.

The original center remains in the clipped domain. At that probe, considering only the pinned formulas occurring in minimum boundary covers gives a distance of 45/32 from the reference value.

But the reference itself is a valid THREE-formula selector, with uniform error zero to itself. The formula on t1=102 belongs to a free singleton family rather than the finite pinned list. Ignoring that family would therefore assert a false positive error lower bound.

The checker returns UNPINNED_FORMULA_FAMILIES and no finite-list error bound. It does not report inconsistency, nor claim that all approximation bounds are impossible. Here zero error is achievable and the formula count three is optimal.

This distinguishes formula-count control from interior approximation control. Unique vertex lifts alone also do not repair the issue: the new boundary edge's endpoints are individually determined, while its interior fiber is not.

## Certificate replay and resource scope

The two instances replay 63 and 31 nonempty edge subsets, with 15 and 11 compatible groups respectively. Their encoded packets are 3,309 and 2,971 bytes. These packets include source-support weights, reference sections and compatibility data; expected source context and code are additional retained information.

Subset enumeration and minimum-partition enumeration are exponential. No polynomial verification, general selector synthesis, byte-optimal representation or arbitrary-dimensional public-domain algorithm is claimed.

The checker supports the conditional polyhedral argument with rational source rows and a two-dimensional observer. The producer exercises it on two domains from one owning retirement, not on arbitrary new source models. The new three-face reference is an explicit construction, not a general synthesis algorithm.

Nine refusals cover negative support weights, false uniqueness, identical nonuniqueness witnesses, omitted compatible groups, an invented count lower bound, a free group relabeled pinned, the false positive error bound, a changed source binding and a changed probe.

The verifier imports no candidate constructor. It shares established exact geometric and owning-source kernels and independently reconstructs the expected source, support consequences, reference validity, all compatibility systems and minimum partitions. The universal conclusions follow from the arguments above, not finite sampling.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_boundary_obligations.py
    uv run --with sympy python research/nima/checkers/verify_boundary_obligations.py

Artifacts: `research/nima/results/boundary-obligations*`.

Predecessor: `research/nima/a-fixed-rank-two-selector-has-an-optimal-three-formula-approximation.md`.
