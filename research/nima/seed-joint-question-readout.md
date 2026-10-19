# A source-relative reader for the actual two-triangle question relation

## Structural advance

The retained-question branch already has more than an unfilled boundary. Existing modules supply:

- actual endpoint-typed path append and traversal actions (`SeedFirstReturnActions`);
- an arrival reader built from the original seed table's target fibers (`SeedArrivalEffects`);
- the two supplied triangles as an explicit JOINT relation, not a product of marginal choices (`SeedTriangleJointContext`).

Using those unchanged constructors, the new formal module proves that the arrival reader recovers the entire row of that two-triangle relation. No new numerical response, memory law, equality filler, or physical instrument is introduced.

## Freeze the correct source domain

The existing parallel alternatives are

    x0=AB, x1=AD DB : A->B,
    y0=BA, y1=BC CA : B->A.

The two-triangle joint table contains only

    ABC -> (direct, indirect),
    ADB -> (indirect, direct).

Both forward alternatives and both return alternatives occur. Nevertheless their Cartesian product has four rows, whereas this joint relation has two. The diagonal pairs are valid paths in the larger free-path language, but have no witness as rows of this frozen triangle table.

This is not a theorem that the six-arrow source forbids all other paths. It is the exact declared domain of the present row task. The intended rung domain must be checked rather than silently identified with either the two-row relation or its four-row enlargement.

## Existing execution and observation

The path action appends supplied occurrences, with no face equality or inverse assumption. The existing active arrival reader reports the last occurrence in the target fiber of the original seed table.

| Joint row | Retained execution | Final active arrival |
|---|---|---|
| ABC | AB BC CA | CA |
| ADB | AD DB BA | BA |

The result is independent of the initial arrival value. Define the source-relative decoder by testing the existing BA occurrence discriminator:

    CA -> ABC,
    BA -> ADB.

The actual function is total on Arrival(A); its claimed left-inverse law is proved on the image of this row execution. No surjectivity or unrestricted-path recovery is asserted.

## Formal positive results

`agda/SeedJointQuestionReadout.agda` proves, for every joint row t and initial arrival a,

    decode(arrived(t,a)) = t.

Consequences checked in the same module:

1. Recover both the forward and return choices, despite the arrival update inspecting only the return leg.
2. Recover the full selected execution word of this one-triangle row.
3. Distinguish the two rows even if their initial arrival values differ.
4. For EVERY question f on the joint row type,

       f(decode(arrived(t,a))) = f(t).

5. The same observation comparison holds after any of the existing marked label/source/target fiber embeddings. Grouped records keep their original row and membership witness; no averaging is substituted.

The source correlation is essential. On this relation, the return choice determines the outward choice. The earlier statement that the arrival reader "forgets the outward choice" was about the larger four-corner domain; applying it unchanged to this joint relation would be incorrect.

The decoder does not recover the initial arrival from the active value. The existing full trace retains that separately, together with the path and the unchanged six-row table.

## Exact limits, checked rather than assumed

### Enlarging to the four-corner product

The existing all-pairs constructor permits

    AB BA   -> BA,
    AD DB BA -> BA.

The histories are distinct. The module proves that no function of active arrival alone recovers every path in this product domain. This is the prior information-loss mechanism at its correct domain.

In particular, the formal mixed rectangle requires all four corners. The positive two-row reader theorem does not construct the two missing joint rows or license importing a rectangular mixed-response law onto a relation without those rows.

### Allowing repeated traversals

One ABC execution and two concatenated ABC executions both end at arrival CA. Their retained lengths are three and six. The module proves equal arrival readings and distinct histories.

Therefore the single-row decoder is not a decoder for arbitrary accumulated histories or a replacement for the full retained state. If history-sensitive questions are admitted, that larger interface needs its own observation contract. The subsequent `seed-arrival-continuation-quotient.md` proves that arrival alone IS continuation-closed for the arrival-only task under every typed finite path. Repetition by itself does not invalidate that predictive quotient; asking to recover the repeated history does.

## Consequence for the T9 search

There is now a concrete source-relative observation square on the unfilled question branch, not merely a generic assertion that histories survive. It uses an existing source relation, existing execution, and an existing reader.

But execution/arrival has NOT been declared the intended T9. In particular:

- the primitive traversal actions are history updates; arrival is a selected observation update, not a derived interaction;
- the two-triangle relation is a specified source domain, not the whole free path space or the137-slot fixture;
- marked regrouping is the existing vertical presentation mechanism, not proof that a particular horizontal constructor was selected;
- the recovered triangle label is not the original matrix J4, a physical amplitude, or a calibrated detector record.

The next exact binding question is now: **does the intended rung12 object retain this joint relation, the four-corner completion, or a continuation-closed history family?** Those choices have demonstrably different sufficient readers. A T9 proposal must state which it consumes and which rows it generates; one cannot decide its observation needs from marginal counts or from an enlarged-domain collision alone.

No new wrapper or arbitrary effect model is needed to ask that question. Existing path execution and arrival already give a checked positive branch, while the enlargement controls identify exactly where more retained information becomes necessary.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedJointQuestionReadout -Fresh

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs, including the actual seed table, free-path questions, first-return actions, arrival interpretation and joint-context dependencies. No postulates or holes were added; existing constructors were unchanged.

Receipt: `results/agda-SeedJointQuestionReadout.json`.

This is formal structural verification, not experimental evidence or completion of source-selected physical descent.
