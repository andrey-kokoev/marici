# Typed first-return actions and the exact effect-comparison boundary

## Source search

The existing `ActualSeedEndpointTable.agda` supplies the six labelled endpoint rows, not payload functions or invertible comparisons. `SeedSeamPathComparisonBoundary.agda` already retains the relevant parallel pairs:

- x0 = AB and x1 = AD DB, from A to B;
- y0 = BA and y1 = BC CA, from B to A.

It proves that the direct and indirect paths differ in the free history interpretation. `NativeTableRules.agda` requires an equivalence and marked-value path as comparison parameters; its higher rule likewise takes a supplied equality. These inspected constructors do not turn common endpoints into a seed effect comparison. This is a bounded source finding, not an impossibility claim about every WG interpretation. Earlier context: `seed-seam-native-witness-construction-audit.md` and `primitive-seed-arrow-role-audit.md`.

## New checked construction

`agda/SeedFirstReturnActions.agda` imports those existing declarations rather than creating another seed. It constructs endpoint-typed append and the canonical history action

    advance e : History(source e) -> History(target e),
    History(v) = Path A v.

Each action appends the actual occurrence to the retained history. This gives concrete outward AB/AD and inward BA/CA actions, with BC/DB acting inside the complement. Four computation laws identify their executions with

    r00 = x0 y0 = ABA
    r01 = x0 y1 = ABCA
    r10 = x1 y0 = ADBA
    r11 = x1 y1 = ADBCA.

All six pairwise inequalities between these returned histories are proved. In particular ABCA and ADBA have equal length but distinct first occurrences: traversal count alone would miss their difference.

The formalization adds no physical response law. An effect interpretation is an explicit parameter consisting of X(v) and a typed function act(e):X(source e)->X(target e) for every primitive occurrence. Its interpreter satisfies the path-composition law. Each returned package retains BOTH its path and its interpreted value. Equality of values does not imply equality of the retained packages.

## Exact next witnesses and a conditional mixed square

The two local effect-comparison types are

    alpha(a) : run(x0,a) = run(x1,a),   a : X(A)
    beta(b)  : run(y0,b) = run(y1,b),   b : X(B).

Neither is supplied for a physical seed interpretation. They are sufficient comparison obligations, not a proof that every physical response must make these effects equal. A response may instead retain a genuine discrepancy or require a different comparison relation.

If these pointwise witnesses are supplied, the module derives comparisons along all four sides of the return rectangle. It also constructs its mixed square directly:

    mixed(a,i,j) = beta(alpha(a,i),j).

All four boundary computation laws are checked. Thus this particular mixed coherence is not a further independent choice once the two full pointwise witnesses are present. This does not manufacture those witnesses, prove identity return, or identify the history channels.

A trivial Unit-valued interpretation provides an explicit control: its effects agree, while the corresponding retained histories remain distinct. It is deliberately not a physical model or a method for erasing the discrepancy.

## Disposition

We moved from a path inventory to executable typed history actions, four proved return computations, pairwise history separation, and an exact conditional effect-comparison square. The remaining source obligation is an independently justified effect interpretation and its actual comparison/response witnesses. Neither the old scalar gains nor G were inserted or derived. No claim that this recovers a previously absent physical constructor is made.

## Verification

Fresh headless check passed:

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedFirstReturnActions -Fresh

Receipt: `results/agda-SeedFirstReturnActions.json`; safe Cubical/guardedness options, ignored interfaces, stable inputs, exit code zero. Finished 2026-10-05T20:04:40.9155638Z. Source SHA-256: `fda07e49475b8cc42367cbd7b54bbb90c60f955c24566e9f955d54827a54d3ee`.

The first compile exposed a missing Sigma product import; after adding it, the complete fresh check passed. No postulates or unresolved holes were introduced. No ledger entry, commit or publication was performed for this step.
