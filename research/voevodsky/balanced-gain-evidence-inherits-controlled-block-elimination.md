# Balanced-gain evidence inherits controlled block elimination

## Wider relation class

Consider rational source constraints

    x_v <= g_uv x_u + b_uv, g_uv>0,

together with the owning atom-cap bounds. Suppose positive rational scales s_v exist with

    s_v=g_uv s_u

for every gain row. Set z_v=x_v/s_v. Each row becomes

    z_v-z_u<=b_uv/s_v.

The source caps become 0<=z_v<=cap_v/s_v. Thus the entire state, not just separate rows or sampled witnesses, is exactly a difference-constraint system in one shared coordinate chart. Raw audit values are recovered by x_v=s_v z_v; their semantics are not silently replaced by scaled thresholds.

## Admission criterion for the chart

Treat every specified gain equation as an undirected edge with reciprocal gain on reversal. A positive scale assignment exists iff the product of gains around every closed walk is one. Propagating scales from a root tests this rationally; encountering conflicting assignments rejects the chart. Each connected component has one free positive overall scale.

A tree with one gain assignment per edge always passes; repeated rows between the same variables must agree on their gains. Merely checking directed cycles is insufficient because inconsistencies can occur in undirected cycles of an acyclic orientation.

This rejects only the proposed difference-coordinate representation. It does not prove the original inequalities inconsistent, noncompact or hard to solve. Unbalanced systems may still admit perfectly valid general LP presentations.

## Certified interfaces and composition

After normalization, shortest-path bounds D(a,b) give exact interface rows z_b-z_a<=D(a,b). In raw public coordinates these are

    x_b/s_b-x_a/s_a<=D(a,b).

A b-node interface, including the zero anchor, still needs at most b(b-1) rows. Given an admitted interface assignment, reconstruct hidden z by the minimum-distance extension, then multiply by s. This yields a source-admitted raw witness satisfying all original gain rows.

Blocks must use compatible scales on shared interfaces. They may inherit a single global chart; independently chosen component scalings must first be reconciled. Under this condition exact block projection and composition inherit the difference-constraint proof. Small graph width alone is not the argument: closure of this balanced relation class is what controls the representation.

## Owning controls

Use the original tail atom caps with raw-atom public observations (not the U,V moment pair), scales cycling through 1,2,3, neighboring gain rows and a closing chord. Exact normalization is checked row by row. Three cases m=4,8,16 pass independent path-closure verification and six source-lift checks. Doubling the chord gain violates the chart condition in all three cases; the verifier checks its mismatch against the chain product.

There are 395 exact distance/path checks. Producer and verifier are separate; the verifier reconstructs the expected rows and chart instead of importing the normalization or shortest-path producer. The diagonal and path checks concern consistent controls; no negative-cycle inconsistency branch is implemented.

## Scope and accuracy

This extends the positive block-elimination class beyond equal-coefficient differences while preserving original raw audit semantics. It does not cover arbitrary linear moment constraints or general two-variable polyhedra. A moment row couples many atoms and typically leaves this class.

The chart is a semantic transformation, not permission to compare conditioning under rescaled norms. Large rational scales and path bounds can have substantial encoding and accuracy costs. Neither bounded interface row count nor successful normalization implies bounded proof bits or total storage savings. The earlier continuation restriction also remains: a compact public summary is not enough to restore discarded fine evidence upon arbitrary audit re-exposure.

## Reproduction

    python research/voevodsky/checkers/check_balanced_gain_elimination.py
    python research/voevodsky/checkers/verify_balanced_gain_elimination.py

Artifacts:

- `results/balanced-gain-elimination.json`
- `results/balanced-gain-elimination-verification.json`

This is a structural subclass and exact implementation control, not a new general elimination algorithm, an owning API change or a fresh upstream analytical-admission proof.
