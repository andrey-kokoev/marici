# A lossless 36-component field decoration of the 137-slot generator

## Construction and boundary

This is a concrete **candidate field-preserving comparison/refibration map**. It uses the existing two-block independent-family generator, not a replacement count formula. It supplies field-dependent payloads on its 137 slots and checks reconstruction and proper tetrahedral covariance.

It does **not** derive the numerical shared-leg/DG assignment, direct reference d, physical state preparation, or a differential-geometric foliation. In particular it is not yet a complete adapter to the pinned numerical T9 contract. The extra choices below remain visible rather than being inferred from the desired number 137.

## Input

The input is a field on all twelve directed tetrahedral arrows:

```
x[a,b] in C^3,   a != b.
```

There are 36 complex components. A directed reference arrow r is supplied. The old schedule already supplies such a mark; this construction does not select it from x.

The twelve triples retain their endpoint labels. Source or target indexing reorganizes them without dropping any triple. Native geometric rotations must also rotate each spatial vector; relabelling patch names alone is insufficient.

## Four state fibers, without four newly supplied amplitude vectors

For each source vertex a, define the ordered, endpoint-labelled fiber

```
F[a] = ((a,b), x[a,b]) for all b != a.
```

Each fiber contains three triples: nine components. Together the four fibers are exactly the original field under a source-indexed presentation. They are **not four scalars or four additional independent modes**. Choosing outgoing rather than incoming fibers is a declared policy; calling them physical state roots would need a further identification.

## The generated slots

Invoke the existing `advance` constructor with the same two typed support blocks:

- Arrow branch: eleven arrows e != r.
- State branch: the four source-vertex keys.

Decorate each generated ordered-parent record:

1. Arrow pair (e,f): retain both labelled triples `(e,x[e])` and `(f,x[f])`.
2. State pair (a,b): retain the full labelled fibers F[a] and F[b].

This produces **121 arrow-comparison slots + 16 state-comparison slots = 137 slots**. Their endpoints and ordered parent identities match the existing generator exactly. Self-pairs are retained. Cross-branch pairs are excluded by the same-kind policy; including them would be a different domain, not the same construction.

A slot is a structured pair, not an assumed inner product or matrix entry. Arrow and state slots have different payload sizes. No scalar contraction, Pauli embedding, fitted coefficients, or physical comparison metric is inserted.

## Reconstruction and redundancy

All repeated occurrences of a labelled triple must agree. Collect them, recover the twelve triples, regenerate the expected slot structure, and require exact equality of parents, endpoints, reference and payloads.

This reconstructs all 36 input components **from the slots themselves**, without storing a hidden original field alongside them. The reference arrow is absent from the arrow-pair branch but remains present in its source-state fiber. Deleting a slot, changing one repeated value, changing the mark alone, or corrupting a family key is rejected.

At a fixed reference and policy, the numerical payload encoding is linear duplication with a left inverse. Its image therefore carries the original 36 complex degrees of freedom, subject to repeated-value constraints—not 137 independent field modes. The 36 basis-vector checks confirm recovery; the explicit inverse explains the general result.

## Symmetry transport

Two separate tests are performed:

- All **24 vertex relabellings** commute with the slot generator when the reference and endpoint labels move too. This is label covariance, not a claim that every relabelling is a proper spatial rotation.
- All **12 independently constructed native proper tetrahedral actions** rotate the triples and permute their patches. Acting directly on each slot occurrence agrees with rotating the original field and then generating the slots. The independently supplied 36-by-36 action matrices are checked against that component-level action.

For all eleven nonidentity proper rotations on the test field, merely relabelling patches while omitting vector rotation fails. This preserves the existing geometric-action distinction rather than hiding it behind decode/re-encode conjugation.

For a fixed reference arrow, only its stabilizer acts within that marked slot domain. Full covariance transports between differently marked domains. The internal projector reflections have not been independently realized as local operations on these pair-valued slots in this experiment.

## Placement relative to the rung diagram

This map fills part of the previously missing *decoration* step:

```
12 arrow supports carrying 36 components
  -> 11 selected arrow roles + four derived source fibers
  -> existing same-kind ordered comparison generator
  -> 137 field-dependent pair-valued leaves
  -> raw/source-/target-indexed views of those same leaves.
```

These views retain all leaves and reconstruct the field. They are **before** the old numerical/DG binding and its two retained incoming-family promotions. The old right-rung family rows and this raw pair-valued slot view are different types. Their equal leaf support does not authorize silently substituting one for the other.

A complete field-bearing G9/G8/G7 still needs the operation-preserving adapter into the selected right-hand record contract. The old generator's fixed matrix assignment and d are not determined merely by this lossless pairing construction.

## What is now established, and what is next

Established at the stated candidate scope:

- An explicit field-dependent 36-to-137 structured encoding using the owning support generator.
- Recovery of every component, including the marked arrow.
- Exact ordered-parent and endpoint agreement.
- Native proper-rotation covariance and retained presentation reconstruction.

Still needed:

1. Justify or derive the reference and same-kind comparison policies.
2. Identify source fibers with the intended state branch, or supply the appropriate replacement without inventing extra field data.
3. Specify a numerical comparison/readout map from these structured pairs to the actual typed legs and witnesses, including d, while retaining enough information for the intended task.
4. Check the full horizontal diagrams with those payloads, not only the common support and retained leaf presentations.

Neither 137 comparison slots nor 36 components is identified with an energy, coupling constant, or spacetime dimension.

## Reproduction

```
python research/strominger/checkers/check_field_36_to_137_refibration.py
```

The checker replays the existing generating schedule and geometric rotation square, tests all 36 basis fields, all twelve reference choices, all 24 label permutations, all twelve proper rotations, raw/source/target reconstruction, and hostile mutations. It writes the ignored runtime receipt `research/strominger/results/field-36-to-137-refibration/verification.json` with direct source hashes and prerequisite logs. No viewer, website or production model is changed.
