# A fixed rank-two selector has an optimal three-formula approximation

## Result

The previously specified six-formula rank-two section now has a whole-domain, fine-admissible approximation using THREE distinct affine formulas. Its exact uniform error is

    epsilon_* = 129/1000

in the ORIGINAL three-atom infinity norm at the same public point.

This threshold is optimal among ALL finite piecewise-affine admissible sections using at most three distinct affine source formulas, not merely among candidates found by the constructor. Every admissible selector needs at least three formulas. Exact reproduction of the specified reference needs at least six.

The construction retains six triangular cells. Formula reduction is not cell reduction. Intermediate four-/five-formula tradeoffs below epsilon_* are not determined here.

## Fixed reference and owning source

The reference is the alternative section already admitted in `rank-two-provider-substitution-preserves-admissibility-not-selected-witnesses.md`, not a reference selected after seeing the approximation.

The owning `one-sided-audit-evidence` migration has public coordinates

    U=t0+t1+t2,
    V=t0+t1/128+t2/16384,

and exact fine source box

    0<=t0<=10, 0<=t1<=102, 0<=t2<=104.

Its public domain is the certified hexagon. In cyclic order, the boundary vertices have source lifts

    v0=(0,0,0), v1=(0,0,104), v2=(0,102,104),
    v3=(10,102,104), v4=(10,102,0), v5=(10,0,0).

The reference uses six triangles joining the public center to successive boundary vertices. At the public center, (108,22125/4096), it assigns

    t_ref=(5,51,52)+(1,-129,128)/1000.

All six source formulas are distinct. The reference digest, owning expected plan, public scope and requested error budgets are frozen before candidate selection. The old provider report supplies a proposal; fresh owning migration and full-section checks supply admission authority for this workload.

## Construction: restore central symmetry

Keep the entire mesh and every boundary lift. Replace only the center lift by

    t_sym=(5,51,52)=(v0+v3)/2.

This point remains fine-admissible and projects to exactly the same public center. Full-domain source admission and continuity follow from the independently checked triangular section certificate.

Opposite boundary edges are centrally symmetric about t_sym, in both source and public coordinates. Their two center-based triangles consequently have the SAME affine source map. The six triangles therefore use only three distinct formulas, with opposite cells referring to a shared formula-table entry.

The constructor compiles these formulas by rational Gaussian elimination. The verifier separately reconstructs each cell's affine extension from its admitted vertex lifts and checks the formula table and every cell-to-formula index.

## Exact whole-domain error

On any one of the six triangles let lambda be the barycentric weight of the center. Boundary values are unchanged, so

    S_ref(y)-S_sym(y)=lambda*(1,-129,128)/1000,
    0<=lambda<=1.

Therefore the original-atom infinity error is at most 129/1000 everywhere, and equality occurs at the center.

The executable checker does not rely on this special mesh identity. It constructs pairwise intersections of reference and candidate triangles and evaluates the source-map difference at every intersection vertex. Each coordinate difference is affine on an overlap, so checking both signs at its vertices bounds that coordinate throughout the overlap. The reported maximum is attained, giving an exact supremum rather than a sample estimate.

Both candidate and reference independently pass full-domain coverage, fine-source admission and continuity. A small displacement is never used as a substitute for fine admissibility.

## Why any admissible selector needs at least three formulas

First, the fine lift is UNIQUE along each of the six public boundary edges.

For each public edge the checker reconstructs its supporting normal and pulls it back to the source atoms. Exactly one source coefficient is zero. Saturation of the support inequality fixes the other two atoms at their appropriate box bounds, and U fixes the remaining atom. Thus every admissible section must trace the same six source edges, regardless of its approximation budget.

The endpoints of ANY three of those source edges have affine rank three. All twenty triples are checked with exact rational arithmetic. But the image of an affine map from the two-dimensional public plane lies in an affine subspace of dimension at most two. One affine source formula cannot contain three of the forced source edges.

For a finite-formula section, every boundary edge must be matched along its entire affine line by at least one formula: a different affine formula can match the prescribed edge map only at at most one point, and finitely many isolated points cannot cover an edge.

Hence six forced source edges require at least three affine formulas. This argument does not assume a particular triangulation or connected formula-support regions.

## Matching lower bound for the three-formula error

If only three formulas are used, each must contain exactly two of the forced boundary edges. The checker enumerates all fifteen edge pairs:

- six pairs have affine rank three and are impossible for one formula;
- nine pairs span affine planes and determine a unique affine source map.

For every admissible pair, three noncollinear public endpoints determine its map exactly. The checker verifies all remaining endpoint values. Thus any three-formula admissible selector can return at the public center only one of these nine affine-map values.

The smallest original-atom infinity distance between those nine values and t_ref is exactly 129/1000. Some of the nine values are themselves inadmissible at the center; keeping them in the minimization only makes the lower bound more conservative.

It follows that every admissible selector with at most three formulas has uniform error at least 129/1000. The symmetric construction attains that bound on the entire domain. This proves the optimal threshold, rather than inferring optimality from a finite search over proposed selectors.

## Exact reproduction and the unresolved middle regime

The reference has six nonempty open triangular regions with six distinct affine source maps. If another finite-formula section agrees exactly with it, each reference map must occur among that section's formulas: finitely many proper affine equality sets cannot cover an open triangle. Therefore six formulas are necessary at epsilon=0.

For 0<epsilon<129/1000, the boundary argument rules out three formulas, while the reference supplies a six-formula upper bound. This implementation does not decide whether four or five formulas improve that interval. Its fallback to the reference is not an optimality claim there.

## Artifacts and costs

Five frozen budgets are checked: 0, 1/1000, 1/10, 129/1000 and 1/5. Below the proved three-formula threshold the constructor returns the reference; at and above it, it returns the symmetric three-formula program.

For this encoding:

| Representation | Distinct formulas | Triangular cells | Program bytes |
|---|---:|---:|---:|
| Fixed reference | 6 | 6 | 1,207 |
| Symmetric approximation | 3 | 6 | 671 |

Program bytes include mesh coordinates, triangles, formula-table entries and cell assignments. Section-admission certificate bytes are reported separately. The lower-bound certificate, reference archive, source context and verification code are additional retained data; these figures are not a total-storage compression theorem.

Six mutation controls reject an insufficient error budget, a first-atom-only understatement of the norm, corrupted coefficients, false formula sharing, an inadmissible source lift and a changed reference binding.

The separate verifier imports no selector constructor or provider router. It shares the established exact geometry and owning-source kernels. Finite certificate checks establish the algebraic premises above; the stated universal lower bounds follow from the boundary, affine-rank and finite-cover arguments, not sampling.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_selector_approximation.py
    uv run --with sympy python research/nima/checkers/verify_selector_approximation.py

Artifacts: `research/nima/results/selector-approximation*`.

No provider replacement is performed by this experiment. It constructs and verifies programs relative to a fixed source selector and error budget; live resource and authority admission remain separate obligations.
