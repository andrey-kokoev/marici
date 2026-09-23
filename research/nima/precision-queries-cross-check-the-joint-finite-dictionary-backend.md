# Precision queries cross-check the joint finite-dictionary backend

## Update

The subsequent [verified source Farkas fallback](verified-source-farkas-fallback-closes-the-joint-precision-workload.md) closes all four unanswered requests. Current artifacts contain 88 native joint certificates and four explicit fallbacks. The native-only results below describe the initial run; its solver failures remain recorded, not relabeled as native successes.

## Initial result

The existing precision workload now runs through the joint-audit lazy backend. Independent verification accepts 88 joint certificates and completes all 44 feasible-state comparisons. Both objectives on each of the two inconsistent states fail during proposal: four operational failures, not four mathematical answers.

All 46 specialized certificates are independently replayed. Eleven altered-history, precision, schema, objective, proof, cut and stale-snapshot controls are rejected.

This is a verified partial backend substitution, not a claim that the joint implementation answered every requested query.

## Translation with two residual free atoms

Expose exactly the supplied pinned indices A. The two free atoms i<j are not added as separate audit coordinates. Write

    r=128^-i, s=128^-j, d=r-s,
    u=U-sum_(k in A) h_k,
    v=V-sum_(k in A) 128^-k h_k.

Then the free coordinates are the exact linear functions

    x=(v-s*u)/d,
    y=(r*u-v)/d.

The joint query objectives are these expressions for -x and x. Every free-coordinate halfspace is translated by substitution. Full-moment measurement rows retain their original coefficients and normalization. Supplied pins become paired equality rows; every evidence event remains in order.

Unlike the earlier full-audit-schema bridge, this representation leaves a two-dimensional residual zonotope. It therefore exercises residual facet cuts, rather than reducing the source image to audit-box caps and displayed affine equalities alone.

## Denotational obligation

Pulling the two inverse expressions back to source coordinates gives exactly the coordinate vectors e_i and e_j. The independent checker verifies those coefficient identities.

Pin equalities, moment boxes and translated halfspaces therefore pull back to the original source constraints. Conversely, every admitted joint point has a source lift under the joint-image contract; its pinned and free coordinates satisfy those same original constraints. Both presentations denote the same admitted source set, including empty sets and lower-dimensional intersections.

The query x<=h retains its weak-inequality semantics. Certified extrema determine the same four-valued answer as the specialized backend. No representative is promoted to actual-source evidence.

## Independent joint verification

The new verifier imports neither the joint engine nor its optimizer. From the independently expected precision state it reconstructs:

- the ordered audit schema, pin equalities and every retained frame;
- both translated objectives;
- source supports by direct pullback to atom coordinates;
- the fixed audit-cap, residual-edge and residual-mass dictionary.

It checks each rejected candidate against all prior rows, strict violation of its cut, unique dictionary identities and exact final row order. It then checks the source lift and nonnegative dual combination, or a Farkas combination when supplied. The nonnegative joint-coordinate convention justifies componentwise dual domination of the objective.

Each successful objective must match its independently certified planar extremum. When both objectives succeed, that establishes the full audit answer. Identical source witnesses are neither expected nor required.

## Workload and failures

The bridge reuses all existing precision requests with m<=8: 46 states/queries and 92 requested objective certificates. These include best/worst audit placements, threshold equality, joint cap clipping, simultaneous errors, exact observations, retained precision histories and line/singleton carriers.

The joint backend returns 88 certificates, all independently verified. The `inconsistent` and `zero-row-inconsistent` cases raise `AssertionError` in proposal for both objective signs. These are recorded as PROPOSAL_FAILED. The specialized backend already supplies independently checked Farkas proofs for both states, and the earlier source-space bridge transports those proofs successfully; no ambiguity about their mathematical emptiness is inferred from the joint solver failure.

This run does not diagnose or repair the underlying LP proposal routine. The finite-dictionary theorem assumes a total exact LP backend; four proposal failures are an implementation boundary, not a counterexample to the theorem.

Observed maxima among verified joint packets:

| Account | Maximum |
| --- | ---: |
| Discovered cuts | 2 |
| Query-local rows | 32 |
| Displayed dimension | 8 |
| Rational numerator/denominator bits | 55 |

These are finite-workload measurements, not uniform performance guarantees. Pins, retained histories and dense joint rows still cost storage.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_precision_joint_bridge.py
    python research/nima/checkers/verify_precision_joint_bridge.py

Artifacts: `research/nima/results/precision-joint-bridge*`.

The bridge does not modify the owning joint backend or the public precision API. Expected statements remain external to the returned answer; hashes do not authenticate observations. No new upstream analytical-admission proof, noisy-pin semantics, storage reclamation or witness interchange is claimed.
