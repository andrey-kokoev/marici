# Bisimplicial certificate-nerve naturality

## Question

What compatibility is still missing when every certificate fiber has local arrows and horn fillers, but the certificate state is strengthened?

## Claim boundary

This packet identifies mixed naturality squares between certificate base change and sector-overlap maps. It does not assert that certificate strengthening itself supplies evidence or that every fiber inclusion is identity on chosen realizations.

## Two independent simplicial directions

The overlay has two nerves:

- the nerve \(N(B_D)\) of the certificate-state poset, whose simplices are chains of certificate strengthening;
- the overlap nerve \(N(\mathcal U)\) of local sector representations.

Their product is bisimplicial. A bidegree \((p,q)\) cell records compatibility across a \(p\)-simplex of certificate strengthening and a \(q\)-simplex of sector overlap.

The prior horn analysis treated mostly bidegree \((0,q)\): coherence inside one certificate state. A global certificate-fibred representation also requires mixed cells with \(p>0\).

## The first mixed square

For \(b\le b'\), suppose a sector comparison is realized in both fibers:

\[
f_b:x_b\to y_b,
\qquad
f_{b'}:x_{b'}\to y_{b'}.
\]

Let \(i_x:x_b\to x_{b'}\) and \(i_y:y_b\to y_{b'}\) be base-change arrows. Naturality requires a typed comparison

\[
i_y\circ f_b
\Rightarrow
f_{b'}\circ i_x.
\]

The existence of all four boundary arrows does not imply this cell. This is a bidegree \((1,1)\) horn-filling problem.

If certificate strengthening merely reveals the same immutable map, the comparison may be identity. If strengthening changes normalization, quotient representative, completion, or source interface, a nontrivial transport certificate is required.

## Higher mixed coherence

For a chain \(b_0\le b_1\le b_2\), the two composites of mixed naturality cells must agree, producing a bidegree \((2,1)\) condition. Associator fillers transported across one certificate edge require bidegree \((1,2)\) conditions. The general local-to-global audit is therefore not a single horn tower but a bisimplicial family of horns.

## Countermodel

Take identical two-dimensional source and target spaces at two certificate states, with identity base-change maps. Let the weaker fiber realize \(f_b=I\) and the stronger fiber realize \(f_{b'}=\operatorname{diag}(1,-1)\). Both fibers contain a typed arrow, and base change exists, but the mixed square does not commute. A separate comparison cell or a rejection of one realization is required.

This countermodel blocks the inference:

`generator present in both fibers` implies `monotone realization of one generator`.

Registry identity and immutable map provenance are needed to establish that the two fiber arrows are the same realization.

## Schema consequence

Every fiber-persistent generator should record:

- `logical_generator_id`;
- `certificate_state_source`;
- `certificate_state_target`;
- `source_base_change`;
- `target_base_change`;
- `fiber_realization_source`;
- `fiber_realization_target`;
- `mixed_comparison_cell`;
- `mixed_residual`;
- `higher_mixed_dependencies`.

A missing mixed cell is a coherence blocker, not a failed scientific map inside either fiber.

## Markov and R-zeta placement

The Markov analytic fragment uses immutable path-product formulas under certificate strengthening, so its checked inclusions can carry identity mixed cells where interfaces are unchanged. The current \(R_\zeta\) proposal has no realized fiber arrow, so its mixed naturality questions are deferred rather than passed.

## Disposition

The pyramid overlay is bisimplicial: sector coherence and certificate naturality are independent. Global gluing requires horn fillers in both pure directions and all mixed bidegrees. This adds a missing gate between a family of fiberwise representations and one certificate-natural global representation.

## Verification

- `research/voevodsky/checkers/check_bisimplicial_certificate_naturality.py`
- `research/voevodsky/results/bisimplicial_certificate_naturality.json`
