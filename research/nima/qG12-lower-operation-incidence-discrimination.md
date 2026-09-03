# `q_G12` lower-operation incidence discrimination

## Question

Which candidate operation—deletion face, graph contraction, or cut/product—is supported by the source incidence of the three sewn shared-wall residues?

## Exact wall incidence

Taking a residue on one shared wall removes exactly that wall factor and retains the other two shared walls together with both occurrence divisors in their unsplit source combination.

| wall | orientation | retained occurrence numerator | occurrence product | other shared-wall product |
|---|---:|---|---|---|
| `q_g1` | `-da` | `a+z-x` | `(y+z-x)(a-y)` | `(a-x-z)(a+y+2z)` |
| `q_g2` | `+db` | `b+z-y` | `(b-x)(x+z-y)` | `(b-y-z)(x+b+2z)` |
| `q_g3` | `+db` | `-x-y-z` | `(b-x)(-b-z-y)` | `(b-y-z)(-b-x-2z)` |

The occurrence numerator is the sum of the two occurrence denominators after restriction. It must remain unsplit: separate occurrence periods depend on regulator hierarchy and endpoint trivialization, while the sewn sum is source-canonical.

## Candidate discrimination

### Deletion/localization face

This operation is supported. It removes the selected shared-wall denominator, pulls back every remaining source divisor, and inherits the Poincaré-residue orientation. It reproduces all retained factors in the table and preserves the occurrence-unsplit numerator. Its output is the already-typed relative wall class `rho_i`.

### Graph contraction

No source-labelled contraction map is present. A contraction candidate would need to show how vertices, edges, site energies, occurrence labels, and the Cayley–Menger measure map to a smaller graph. The wall equations alone do not determine this combinatorial operation. Therefore contraction is untyped rather than disproved.

### Cut/product factorization

The naive cut/product candidate is rejected at source-incidence level if it resolves the two occurrence terms into separate factors or periods: their individual physical boundary values are noncanonical. A product can remain admissible only if an independently constructed cut object retains the unsplit occurrence pair and reproduces the inherited orientation and conductor branch. No such object is frozen.

## Result

Incidence selects a unique currently typed operation: localization to the deletion face. It does not select an independently normalized lower graph. Graph contraction remains undefined, and a naive product decomposition conflicts with source sewing.

Thus the strongest established factorization-like statement is

\[
\operatorname{Res}_{q_{gi}}\operatorname{Res}_{q_{G12}}\Omega_{\rm phys}=\rho_i
\]

inside the relative wall calculus. Replacing `rho_i` by a lower-graph amplitude or product requires new source data.

## Strongest falsification attempt

Split the occurrence numerator into its two fractions and assign one to each cut factor. Two allowed regulator hierarchies give different individual boundary currents, while their unsplit sum cancels the spurious ambiguity. This falsifies occurrence-resolved cut factorization at a generic nonsoft point.

## Acceptance test for a stronger lower object

1. declare a contraction or cut graph independently;
2. retain both occurrence labels through its constructor;
3. reproduce the table’s denominator pullbacks and orientations;
4. prove its source period is invariant under regulator hierarchy and endpoint trivialization;
5. compare its conductor-normalized class with `rho_i`;
6. deliberately split the occurrence pair and verify failure.

## Disposition

Deletion-face localization survives exactly. Contraction is untyped. Naive cut/product factorization is falsified by occurrence-level noncanonicity; only a future source-sewn cut constructor could reopen it.

## Evidence

- `research/benincasa/physical_g12_shared_wall_residues.py`
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
- `research/nima/checkers/check_three_site_q_cyclic_completion.py`
