# Analytical cut interfaces compose when shared factors survive elimination

## Result

A frozen exact elimination procedure now constructs and composes residual relations on the owning Chebyshev-derived three-bin moment carrier. It was not supplied the remaining-budget formula or a globally minimized observer.

The checks pass for 167 projection plans, including alternative elimination orders, fixed-prefix commitments and early-versus-late suffix evidence. The known pairwise assembly remains a negative control.

The important distinction is:

> Join the constraints sharing a variable before forgetting that variable. Independently forgetting its witnesses and then joining the resulting summaries can change the admitted relation.

The positive construction is not arbitrary composition of locally minimized marginals. Every elimination receives all factors incident on its variable, including the ternary budget and the objective relation.

## 1. Owning analytical input

The input is Grothendieck's hash-bound three-bin moment carrier, with nonnegative masses, atom caps and cumulative budgets. The owning verifier is freshly replayed, including outward capacity bounds, exact primal/dual certificates and the certified kernel-box obstruction.

Introduce an objective coordinate

    z = l_1*x_1 + l_2*x_2 + l_3*x_3,

where the l_i are the owning rational lower kernel coefficients. Keeping z with the surviving mass coordinates preserves their joint possibilities, rather than separately preserving a mass range and an optimized scalar.

The task is exact existential projection of this declared moment relation. It is not exact prime realizability or the exact microscopic signed-kernel pairing. When a prefix is known, its equality constraints are inserted before elimination; the compiler must not replace a committed prefix by an arbitrary new witness.

## 2. Frozen construction rule

Use rational Fourier-Motzkin elimination. For an eliminated coordinate, combine every positive-coefficient row with every negative-coefficient row so that the coordinate cancels. Keep all rows that do not read it. Each output inequality carries its nonnegative combination of the original rows.

Normalize by positive scaling and keep the strongest parallel inequality. No global continuation minimization is used to choose the interface. Redundant objective bounds derived from the original atom caps make boundedness explicit.

For a retained assignment, the eliminated coordinate has a finite interval of possible values. The generated pair inequalities assert that every lower endpoint is below every upper endpoint. This supplies a constructive lift. Reversing the elimination steps reconstructs one admitted completion without claiming it is the actual historical source.

This is why the method preserves complete residual relations rather than just necessary inequalities. The interval argument and exact elimination identities apply over the real polytope, not only at the points enumerated by the checker.

## 3. Test workload

The frozen workload includes:

- every proper subset of mass coordinates, always retaining z;
- every elimination order for each such cut;
- four prefix commitments: zero, the owning full optimizer, the owning pairwise candidate's prefix, and half of that candidate prefix;
- objective upper and lower refinements at the block threshold;
- upper and lower refinements of the third mass;
- an inconsistent third-mass interval;
- a coupled constraint involving both the third mass and z.

For each permitted refinement E on retained coordinates, compare

    projection(A intersect E)

with

    projection(A) intersect E.

There are 72 early/late comparison pairs. All agree. The logical identity holds because E does not read an eliminated variable; the certificate replay verifies its implementation on the actual inputs.

A late read of x_1 after eliminating it is rejected as `ELIMINATED_COORDINATE_READ`. Reintroducing a fresh variable with that name would not recover the old witness and is not an allowed refinement.

## 4. Direct versus staged verification

The independent checker does not import the producer or an optimization package. It uses a different arithmetic construction for elimination pairs and determinant-based vertex enumeration rather than the producer's linear solver.

For every plan it checks:

1. The source and frame rows are the frozen input, not an invented residual carrier.
2. Every emitted row is a nonnegative combination of those rows.
3. Every elimination stage contains the complete generated relation, after the declared normalization.
4. Every original vertex projects into the residual relation.
5. Every residual vertex has an explicit lift satisfying the original conjunction.
6. Each retained coordinate is bounded.

Complete vertex enumeration of these bounded rational polytopes, together with the lifts and row certificates, establishes equality of the whole projected polytopes. This is not finite grid sampling.

The independent replay checks:

- 167 projection plans;
- 313 elimination stages;
- 8,189 nonnegative row certificates;
- 464 constructive vertex lifts;
- 64 exact Farkas inconsistency certificates;
- 11 elimination-order comparison groups;
- 72 refinement-commutation pairs.

The original scalar minimum is reproduced exactly. No objective discrepancy is introduced by staged elimination.

## 5. Mandatory unsafe-composition control

Independently project the mass carrier onto each coordinate pair and join those pair relations. Each pair projection is exact and has a checked full-carrier lift.

Nevertheless the owning pairwise candidate passes all three projected relations while its total mass exceeds the ternary budget. The full residual relation, retaining the objective coordinate, rejects its proposed mass/objective completion. The source-bound block-threshold separation remains intact.

Thus the successful elimination result does not rescue arbitrary pairwise assembly. The globally shared budget must enter the factors before its variables are eliminated. There is no way to infer that missing relation merely from the already projected pair images.

## 6. Representation and resource limits

The representation class is an exact rational polyhedron with row certificates, not a claimed minimal scalar or piecewise interface.

Before running, the workload bounds were frozen at:

- 128 retained rows per stage;
- 512 generated candidate rows per stage;
- 8,192 bits per retained numerator or denominator.

Observed maxima were 13 retained rows, 19 generated rows and 811 bits.

These are bounds for the frozen workload, not a uniform promise for arbitrary subsequent evidence. In particular, unrestricted affine refinements in multiple retained dimensions can require additional facets. Exact commutation does not imply uniformly bounded representation size.

The exported audit packet retains original rows and intermediate proofs for independent replay. It is not a claim that all this audit material is the minimal runtime interface. Nor does the experiment establish that discarded historical coordinates remain recoverable for new queries.

## 7. What this establishes for synthesis

The construction supports a concrete compositional rule on an owning analytical family:

    complete joint source constraints
      -> join all factors sharing an eliminated coordinate
      -> exact residual relation with objective attached
      -> admissible later refinement on retained coordinates.

Different legal cut orders give equivalent residual relations. Forgetting shared witnesses before joining can instead admit false completions.

This is a checked application of standard exact elimination, not a new general elimination theorem. Its contribution to the lane is to bind that rule to the owning signed-bound obstruction, independently verify composition and refinement, and expose the representation cost rather than assume a small interface.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/verify_ternary_tail_budget_dpc.py
    python research/nima/checkers/check_analytical_cut_composition.py
    python research/nima/checkers/verify_analytical_cut_composition.py

During development, independent stage replay caught a mutable-list alias: appending late evidence also changed an exported earlier elimination stage. Copying the residual row list before appending fixed the audit record. The corrected packet passes all checks.

Artifacts:

- `research/nima/results/analytical-cut-composition-contract.json`
- `research/nima/results/analytical-cut-composition-packet.json.gz`
- `research/nima/results/analytical-cut-composition.json`
- `research/nima/results/analytical-cut-composition-verification.json`
