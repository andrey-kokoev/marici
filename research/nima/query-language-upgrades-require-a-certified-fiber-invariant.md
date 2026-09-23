# Query-language upgrades require a certified fiber invariant

## Result

The owning analytical interface can sometimes be upgraded to a richer query language **without new acquisition and without recovering discarded frame history**. The missing premise is precise:

> The retained possibilities must contain every source point compatible with their visible image, relative to the admitted source model.

This is a property of the admitted possibility set, not of a chosen representative lift. It holds for the existing observable-only evidence grammar. It can fail after a bin-level frame is accepted, and it can become true again when later visible evidence makes that frame redundant.

Nine exact upgrades and five downgrade tests pass independent verification. Two unsafe downgrades are rejected by the equality test below.

## 1. The recoverability invariant

Let P be the complete declared three-bin moment relaxation and let

    L(x)=(S,F).

For a current admitted carrier C, write Q=L(C). Call C fiber-saturated relative to P and L when

    C = P intersect L^-1(Q).

If initialization is P and every accepted frame is a halfspace in the old observables, this equality follows inductively. Indeed, the accumulated frames have the form L^-1(H), so their effect is completely determined by the observable point.

Consequently the current polygon Q and the immutable source model P recover C exactly. Earlier frame syntax, order and individual source witnesses are unnecessary for this reconstruction.

This does not hold merely because every polygon vertex has a feasible source lift. A lift proves that some source point realizes an observable value, not that all restrictions inside its fiber have been retained.

## 2. Constructive language upgrade

Add the observable x_1, giving

    M(x)=(S,F,x_1).

The owning lower kernel coefficients satisfy l_2 != l_3. Therefore M is invertible on the three moment coordinates:

    x_1 = h,
    x_2 = (F-l_1*h-l_3*(S-h))/(l_2-l_3),
    x_3 = (l_2*(S-h)-(F-l_1*h))/(l_2-l_3).

The constructor transforms the source inequalities by this inverse and conjoins the current polygon constraints on (S,F). It uses only P, L and Q, not the discarded frame chain or stored representative lifts.

For saturated C, the result is exactly M(C). Arbitrary later affine queries in the enlarged coordinates therefore have the same answers as queries on C itself. This is an upgrade of the possibility representation, not selection of an actual mass vector.

The tests cover the initial polygon, all five retained stages of the owning traces, a singleton observable fiber, the zero fiber and a constant-S segment. Polygon, segment, point and empty states are handled explicitly. An impossible observable singleton is rejected rather than upgraded as an admitted state.

An independent oracle retains the original observable frame conjunction only for verification. Its source vertices agree exactly with the constructor's upgraded relation in all nine cases.

## 3. Exact possibility does not imply an actual answer

The owning kernel collision gives two admitted mass vectors with identical S and F but x_1 on opposite sides of 1000.

Upgrading that singleton observable point recovers the whole source fiber. The response to x_1<=1000 is `MIXED`, not an invented answer obtained from one representative. The zero observable fiber, by contrast, forces all masses to zero and gives `ALWAYS_TRUE`.

An empty carrier is classified as `INCONSISTENT`; it supplies no vacuous factual certificate.

Thus a new source observation may still be necessary to determine the actual bin value, even when no new acquisition is needed to reconstruct all model-compatible possibilities. Physical acquisition and publication authority remain separate questions.

## 4. The same polygon and the same stored lift can hide different restrictions

At the observable point of (1000,1000,1000), consider the two carriers

    C_low  = P intersect fiber(S,F) intersect {x_1<=1000},
    C_high = P intersect fiber(S,F) intersect {x_1>=1000}.

They have the same singleton observable image. The center (1000,1000,1000) is a common feasible stored lift for both.

Choose a rational alpha strictly between the owning lower collision point's x_1 value and 1000. The new query x_1<=alpha is feasible in C_low and infeasible in C_high.

Therefore even the old polygon **together with that stored lift** cannot determine the enriched query answer. Without the saturation invariant or retained fiber constraints, the required disposition is `NEEDS_FIBER_INFORMATION`.

These hidden frames would not be admitted by the original observable-only grammar. The example does not refute its lawful upgrade. It shows why a later language change must update the retention contract rather than continue assuming the old invariant.

## 5. Certified downgrade after a richer update

Suppose an upgraded interface accepts a bin-level constraint. Before discarding that constraint and retaining only its old image, compute

    Q'=L(C'),
    R=P intersect L^-1(Q').

Always C' is contained in R. The downgrade is exact precisely when the reverse inclusion holds too. On the rational compact carrier, checking every vertex of R against C' gives a constructive equality test.

Both hidden-half examples fail it: reopening the old fiber introduces a point violating an accepted constraint. The test returns an explicit offending source point.

A redundant bin cap passes the test. More importantly, forgetting can become safe later:

1. Accept x_1<=1000.
2. Subsequently accept the old-observable frame S<=500.
3. Nonnegativity now implies x_1<=S<=500<=1000.

The hidden bin bound has become redundant. An exact nonnegative row combination proves that implication. The image can now be retained alone, and a later model-based upgrade recovers the correct remaining carrier.

So an extension need not force permanent retention of every newly introduced field. It requires retaining its residual constraint until elimination is justified.

## 6. What was verified

The producer operates with exact rational polyhedra. The independent verifier imports neither its constructor nor an optimization package. It uses determinant-based vertex enumeration and independently reconstructed supporting halfspaces.

Checks include:

- both affine inverse identities;
- nine exact upgraded carriers and 66 source lifts;
- equality with full retained-history refinement;
- five downgrade tests, including two explicit failures;
- the same-polygon/same-lift collision;
- safe elimination after visible evidence makes a hidden row redundant;
- rejection of an observable point with no source lift.

The frozen workload limits are 32 upgraded rows, 64 vertices and 8,192-bit retained rationals. Observed maxima are 17 rows, 16 vertices and 1,536 bits. These are not uniform bounds for arbitrary future evidence sequences.

The source model and its coefficients count as available retained information. The constructor does not recover discarded restrictions from a hash. The invariant depends on known initialization, the admitted frame grammar and faithful maintenance; it is not inferred from the polygon alone or authenticated by this experiment.

## Structural consequence

Language extension has three distinct outcomes:

- **Exact model-based upgrade:** complete source model plus certified fiber saturation suffices.
- **Conditional or unresolved actual answer:** the upgraded fiber still contains multiple possibilities.
- **Missing retained information:** an unrepresented fiber restriction prevents an exact upgrade.

The corresponding forgetting rule is not merely “the current observable image is unchanged.” It is:

> Forget a restriction only when reopening the retained source fiber cannot restore any possibility that the restriction excluded.

## Reproduction

    python research/grothendieck/checkers/verify_query_relative_tail_interface.py
    python research/nima/checkers/check_query_language_upgrade.py
    python research/nima/checkers/verify_query_language_upgrade.py

Artifacts:

- `research/nima/results/query-language-upgrade-contract.json`
- `research/nima/results/query-language-upgrade-packet.json.gz`
- `research/nima/results/query-language-upgrade.json`
- `research/nima/results/query-language-upgrade-verification.json`

Scope: the owning rational moment relaxation and its declared query languages, not exact prime realizability, actual source selection or physical action authorization.
