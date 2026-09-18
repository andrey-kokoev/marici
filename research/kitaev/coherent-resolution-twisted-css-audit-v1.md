# Boundary-completed Coherent Resolution as a twisted CSS object

## Result

At A3 the exact positive mutation transport is a rank-one rational local system with every face holonomy equal to one. Because the associahedron is contractible, it is globally gauge trivial. For diagonal basis gauges `G_k`, the weighted boundaries have the form

\[
d_k^\rho=G_{k-1}d_kG_k^{-1}.
\]

Hence

\[
d_{k-1}^\rho d_k^\rho=G_{k-2}d_{k-1}d_kG_k^{-1}=0,
\]

and ranks and homology equal the untwisted values. At A3 the ranks remain `(13,8,1)` and `H_1=0`. Over `Q` this is a genuine twisted chain complex but only a trivial gauge twist of the zero-logical-dimension CSS shadow.

## Mod-two gate

The supplied rational gauge does not canonically reduce to an invertible mod-two local system. At least one exact negative-simple coordinate has positive 2-adic valuation, so its reduction is zero rather than a unit. The untwisted incidence CSS code exists mod two, but the rational canonical-weight conjugacy cannot be called a mod-two twisted code without an integral lattice/unit model.

## Exchange defect

The negative exchange defect is nonzero while every measured face curvature `holonomy-1` is zero. Assigning the same defect naively as face curvature contradicts the exact flat transport and is falsified. It is not a syndrome because no physical-error-to-chain map is typed; not a stabilizer deformation because no commuting deformed check matrices are supplied; not a subsystem gauge generator because there is no gauge-check module; and not logical because `H_1=0`. Its present disposition is an untyped coefficient obstruction separate from the flat line.

## Arbitrary finite rank

For every finite `A_m`, conditional on all cluster weights being nonzero and mutation transport being the vertex coboundary `W(C')/W(C)`, the same diagonal conjugacy trivializes the local system and preserves the homology of `CR_m`. Since `CR_m` is contractible, no logical sector appears. This quantifier does not cover zeros on special kinematic loci and implies no uniform locality, LDPC bound, distance, colimit, or completed protection.

## Minimal operational map

Canonical-weight perturbations require a typed map

\[
E_{\rm phys}\to C_1(CR_m;R)
\]

from a declared physical error alphabet to edge chains, followed by a declared syndrome map such as `d_1^rho`. Correctability additionally requires an error composition law, support/locality relation, code projector or stabilizer/gauge module, and equivalence of errors modulo boundaries. The naive scalar-to-all-faces assignment fails because it creates nonzero curvature where exact holonomy is one.

## Evidence

- `research/kitaev/checkers/check_coherent_resolution_twisted_css.py`
- `research/kitaev/results/coherent_resolution_twisted_css.json`
- execution `structured_command_execution:e_21144_1789761957654580500_2`

## Disposition

- rational flat transport: `trivial_gauge_twist`;
- mod-two weighted transport: `undefined_without_integral_unit_model`;
- canonical untwisted CSS shadow: `code_with_zero_logical_dimension`;
- negative exchange defect: `untyped_obstruction_not_face_curvature`.
