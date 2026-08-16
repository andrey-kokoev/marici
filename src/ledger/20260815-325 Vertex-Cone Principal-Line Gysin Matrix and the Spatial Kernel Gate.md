# Vertex-Cone Principal-Line Gysin Matrix and the Spatial Kernel Gate

## Record

Date: 2026-08-15

Status: proved in the finite labelled line-valued vertex-cone model. All
72 literal occurrence rows are evaluated primitively and naturally, with
no cross-line identification or localization. The spatial proper/log-BM
kernel realizing these evaluations remains unconstructed. No graph
admission is claimed.

## Line-valued cone

For each ordered pair, let the three cone axes be
\[
(\tau,n_0,n_1)
\]
and let their literal occurrence lines be
\[
(J_\tau,J_{n_0},J_{n_1}).
\]
A source cone state indexed by \(H\subset\{\tau,n_0,n_1\}\) carries
\[
\bigotimes_{a\in H}J_a^\vee.
\]

The literal radial map along axis \(a\) contributes the labelled section
of \(J_a\). The boundary map pairs only matching lines:
\[
J_a^\vee\otimes J_a\longrightarrow R,
\qquad X_a^\vee(X_a)=1.
\]
After evaluation, the remaining line is exactly
\[
\bigotimes_{b\in H\setminus\{a\}}J_b^\vee.
\]
Thus every occurrence coefficient is derived from a principal-line
evaluation. Distinct occurrence lines are never identified, and no
\(X_a^{-1}\) is introduced.

## Matrix and naturality

Across six ordered pairs, the checker verifies:

- 72 line-valued boundary rows;
- 48 chart rows and 24 wall rows;
- 72 primitive evaluations;
- 72 two-axis middle naturality squares;
- evaluated boundary rank 42;
- all 42 nonzero Smith factors equal to one.

The middle squares commute because evaluation and contraction in distinct
labelled factors commute. Generator rescaling is harmless: a principal
generator and its dual transform inversely.

## Symmetry

Rotation and physical reflection permute the six literal vertices and
their three principal lines. Since the dual line follows the inverse
character, each evaluation remains one. The construction therefore
respects \(D_3\) and physical reflection at the finite line-valued level.

## Remaining spatial gate

This removes the last coefficient divisibility obstruction in the
vertex-cone boundary. It does not prove that a proper product-Rees/log-BM
correspondence has these literal entry143 extraordinary restrictions.

The missing object is a constructible or coherent-constructible kernel on
the product-Rees correspondence whose relative dualizing complex contains
the three labelled dual factors and whose proper pushforward realizes the
72 evaluations above. Its Beck--Chevalley maps must agree with the actual
entry143 support inclusions and normal-Čech corestrictions, not merely with
their basis labels.

Only after that spatial theorem can the established endpoint odd counits
and the entry223 \(q_\Sigma\) top be attached to one global trace.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_vertex_cone_principal_line_gysin.rs`

SHA-256:
`98e44c2fd7c6cb3d5838c9938c5dcc1946cb2ec6b48c72f484b1860e14d0a4dc`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON field checks passed. Native PowerShell was used for
Rust verification because no repository-scoped structured-command MCP
capable of invoking `rustc` is exposed.

## Outcome contract

~~~json
{
  "claim": "Decorating each Rees-Cech/Tor vertex-cone axis by its own principal occurrence dual makes all 72 literal radial rows primitive through matching-line evaluation. The resulting matrix is saturated and D3/reflection compatible, with no cross-line identification or base inversion.",
  "status": "proved_scoped_finite_vertex_cone_principal_line_gysin",
  "scope": "finite labelled line-valued vertex-cone and literal entry143 radial/Boolean matrices; spatial proper/log-BM kernel excluded",
  "matrix": {
    "ordered_pairs": 6,
    "boundary_rows": 72,
    "chart_rows": 48,
    "wall_rows": 24,
    "primitive_evaluations": 72,
    "middle_naturality_squares": 72,
    "rank": 42,
    "all_nonzero_smith_factors": 1
  },
  "line_data": {
    "principal_dual_exponent": -1,
    "radial_section_exponent": 1,
    "evaluated_exponent": 0,
    "cross_line_identifications": 0,
    "base_inversions": false,
    "rescaling_invariant": true
  },
  "symmetry": {
    "D3_line_relabeling": true,
    "physical_reflection_line_relabeling": true
  },
  "unconstructed": [
    "proper log-BM six-functor kernel",
    "literal support/costalk Beck-Chevalley realization",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_vertex_cone_principal_line_gysin.rs",
  "checker_sha256": "98e44c2fd7c6cb3d5838c9938c5dcc1946cb2ec6b48c72f484b1860e14d0a4dc"
}
~~~

