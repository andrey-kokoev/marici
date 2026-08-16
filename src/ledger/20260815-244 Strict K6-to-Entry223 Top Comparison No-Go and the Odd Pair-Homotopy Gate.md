# Strict K6-to-Entry223 Top Comparison No-Go and the Odd Pair-Homotopy Gate

## Record

Date: 2026-08-15

Status: falsified for the strict integral support-preserving comparison from the
literal \(K_6\) top complex to the entry223 three-facet/three-pair SNC complex.
The unique \(D_3\)-equivariant rational comparison is half-integral. Its
integral obstruction is a primitive \(\mathbb Z/2\) class. This is not a
no-go for a derived log-excess correspondence with an additional
pair/corridor homotopy generator. No graph admission is claimed.

## Strict comparison problem

The literal source has cellular ranks
\[
(1,9,21,14)
\]
in top, facet, edge, and vertex degrees. The entry223 SNC target has ranks
\[
(1,3,3)
\]
in top, long-road facet, and pair-intersection degrees, with pair incidence
\[
B=\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix}.
\]

Fix the only strict top/facet comparison compatible with the named grades:
the source top maps with coefficient \(+1\), the three long facets map
identically with their cellular signs, and the six short facets map to zero.
Literal support permits an edge column only when that edge contains a unique
long diagonal, and then only in the two target pair rows incident to that
road. This leaves 24 integral variables.

## Integral calculation

The supported chain equations have rank 21 and affine rank 3. Adding strict
\(C_3\)-rotation covariance raises the rank to 23 and leaves affine rank 1.
Adding the physical reflection equations gives a full-rank 24-variable
system with a unique rational solution.

That solution has twelve nonzero coefficients, all equal to
\(\pm\tfrac12\). Hence it is not integral. Modulo two, the coefficient
matrix has rank 23 while the augmented matrix has rank 24. An explicitly
selected maximal minor has determinant \(+2\). Consequently the Smith
factors are
\[
\underbrace{1,\ldots,1}_{23},2,
\]
and the strict obstruction group is exactly \(\mathbb Z/2\).

This is the earliest exact falsifier for the proposed strict
support-preserving top comparison. It proves that the six short-facet
contractions cannot be derived as integral strict rows under the stated
literal support and \(D_3\) requirements.

## Minimal repair

A derived correspondence can evade the no-go only by adding at least one
reflection-odd pair/corridor homotopy generator whose boundary maps with an
independently derived odd coefficient into the mod-two defect row. A unit
coefficient is sufficient and minimal. Merely inserting halves, declaring
a pair-intersection state, or choosing an AW contraction would fit the
missing datum.

Geometrically, the required generator must come from an actual
multiplicity-sensitive log/excess overlap object
\(\Gamma_{ij}^{!,\log}\), with a support-typed map to the complementary
literal corridor \(C_\bullet(q_k)\subset F_B/F_V\). Its boundary must derive
the odd row while retaining occurrence ideals, normal-circle states, Tor
grades, Čech signs, both adjacent long-facet restrictions, endpoint
framing, reflection, and \(D_3\).

## Downstream status

The strict no-go does not instantiate the endpoint/\(Q\) mapping fiber.
Until the odd derived overlap generator and its literal entry143
corestrictions are constructed, \(p_{\partial,Q}\), its Bockstein, and the
\(D_8\)/Jordan coherence tests remain undefined.

## Executable evidence

Checker:
research/voevodsky/check_k6_entry223_strict_top_comparison_no_go.mjs

SHA-256:
8f0e30ef462755fe1ffbd88a7e14299ba145eb02d76ee35fa73eda87c4498fa7

The user-site structured-command MCP executed Node with exit code zero. The
checker asserts the complete census, rational ranks, mod-two rank jump,
half-integral unique solution, determinant-two maximal minor, and Smith
factors before emitting its JSON result. Delegation-worker validation was
attempted first at low cognition, but its admitted root is limited to the
Narada site and correctly refused the Marici repository cwd.

## Outcome contract

~~~json
{
  "claim": "No strict integral D3-equivariant support-preserving comparison exists from the literal K6 top complex to the entry223 three-facet/three-pair SNC complex.",
  "status": "falsified_scoped_strict_integral_K6_to_entry223_top_comparison",
  "scope": "strict literal support rows with fixed top and long-facet images; derived log-excess overlap generators excluded",
  "matrix": {
    "variables": 24,
    "supported_rank": 21,
    "supported_affine_rank": 3,
    "rotation_equivariant_rank": 23,
    "rotation_equivariant_affine_rank": 1,
    "D3_equivariant_rank": 24,
    "D3_equivariant_affine_rank": 0,
    "unique_solution_nonzero_coefficients": 12,
    "unique_solution_denominators": [2],
    "integral_solution": false,
    "mod2_coefficient_rank": 23,
    "mod2_augmented_rank": 24,
    "selected_maximal_minor_determinant": 2,
    "smith": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    "obstruction_group": "Z/2"
  },
  "general_derived_correspondence_no_go": false,
  "minimal_additional_datum": "one geometrically derived reflection-odd pair/corridor homotopy generator with unit boundary into the mod-two defect row",
  "unconstructed": [
    "Gamma_ij exceptional/log overlap object",
    "24 literal entry143 occurrence/normal/Tor/Cech corestriction rows",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_k6_entry223_strict_top_comparison_no_go.mjs",
  "checker_sha256": "8f0e30ef462755fe1ffbd88a7e14299ba145eb02d76ee35fa73eda87c4498fa7"
}
~~~
