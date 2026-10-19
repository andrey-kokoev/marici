# WG rung schedule comparison v1: recovered table data is not a selected phase

## Net disposition

This settles the bounded `rung-schedule-prior-comparison` subtask, not the whole `rung-operation-schedule` node. The historical recurrence and later diagram agree after explicit field-preserving recovery but are different marked constructions. The horizontal constructor/table interpretation remains open.

## Fixed source and types

Use X={0,1,2,3}, E={(i,j):i!=j}, and twelve rows e_ij with label ('arrow',i,j), source ('vertex',i), target ('vertex',j), and retained one-edge word ((i,j),). These are the twelve arrows of the existing indexed-path fixture. This is one concrete retained table for comparison; we do not prove that it is the operator's full WG(s) or the native filled-comparison carrier.

For a selected field p:E->K, reuse the existing kernel

    F_p(E)(k) = Sigma(e:E) (p(e)=k)
    T_p(E) = Sigma(k:K) F_p(E)(k).

Recovery u_p(k,e,w)=e and section j_p(e)=(p(e),e,refl) are the maps of `TableFibrationCycle.unpack-fibers`. Later fields are pulled back through u_p. A finite membership check models w in the executable example; it is not a replacement for higher identity witnesses.

A complete presentation package also records the field selector and construction history. The row equivalence does not erase that history. The owning Agda source explicitly makes this distinction after `table-path`.

## First two successors on the SAME input

Write ell, s, t for label, source and target.

| Role | Historical label-first convention | Later diagram convention |
|---|---|---|
| 12 | E | E |
| 11 | T_ell(E) | T_s(E) |
| 10 | T_(s composed u_ell)(T_ell(E)) | T_(t composed u_s)(T_s(E)) |
| Selected history at10 | label, source | source, target |

The later original checker uses source/target indexed families, recovering the base table between views. The nested total on the right is a history-retaining lift of that convention, not a claim that its serialized rows are identical to those flat families. Recover the previous row and reindex to compare them; the checker verifies membership in the actual target family.

For e_01 the construction shapes are:

    historical11 = (label01, e01)
    historical10 = (source0, (label01, e01))
    diagram11    = (source0, e01)
    diagram10    = (target1, (source0, e01)).

Membership witnesses and field tags are retained. All four recover e01. They are not the same selected-column construction.

The label family has twelve singleton fibers. Source and target families each have four fibers of size three. All dependent totals have twelve rows. Source and target families have equal fiber counts but different membership: e01 lies over source0 and target1. Counts alone cannot detect the wrong phase.

## Explicit comparison, not silent phase equality

Compose historical recovery to E with the section into the later total. Its inverse is the opposite recovery/section composite. This preserves the original label, source, target and payload. At depth two, compose both recoveries/sections. The finite checker constructs the bijections by unique retained base labels and checks all original fields.

Keep both derivations in the comparison package. A theorem about equivalence of the underlying tables is not a theorem identifying separately retained phase histories.

The four negative tests reject:

1. label-first output used where source-first provenance is required;
2. label/source output used where source/target is required;
3. equal base recovery used to erase a differing selector history;
4. an eight-transition trace reported as six transitions.

These are finite provenance-contract failures, not fresh Agda negative compilations or claims that no differently typed adapter exists.

## All nine historical labels

| Label | Incoming selector | Retained depth | Row count |
|---|---|---:|---:|
| 12 | initial | 0 | 12 |
| 11 | label | 1 | 12 |
| 10 | source | 2 | 12 |
| 9 | target | 3 | 12 |
| 8 | label | 4 | 12 |
| 7 | source | 5 | 12 |
| 6 | target | 6 | 12 |
| 5 | label | 7 | 12 |
| 4 | source | 8 | 12 |

Thus this recurrence cannot justify a row-count decrease12->4. If its input is called WG(s), these eight further operations require a phase-carrying generator state; the first operation producing WG(s) is not specified here.

## Typed later diagram: all roles, horizontal operation still a parameter

For retained source and target tables A,B and an actual whole-package operation P:A->B, let S_A and T_A denote source and target presentation totals, with recoveries U_sA,U_tA and sections J_sA,J_tA. Similarly for B.

| Presentation | Source package | Transport package | Result package |
|---|---|---|---|
| labelled | 12: A | 9: P | 6: B |
| source-indexed | 11: S_A | 8: J_sB P U_sA | 5: S_B |
| target-indexed | 10: T_A | 7: J_tB P U_tA | 4: T_B |

Source-side vertical maps are J_sA and J_tA U_sA; target-side maps are J_sB and J_tB U_sB. These are maps on presentations; the whole comparison packages retain operands, recovery witnesses and construction traces. The expressions in the middle column abbreviate these witnessed packages, not bare unrecorded functions.

The middle arrows9->8->7 are presentation transport of P itself. Starting from P8, the lower presentation is obtained as

    (J_tB U_sB) P8 (J_sA U_tA),

and the recovery laws compare this to J_tB P U_tA. No inverse of P is used. This supplies the PARAMETRIC comparison law, not a selected source-specific P.

The outer squares and all three routes12->4 compare via the recovery witnesses. The owning finite diagram checker already tests instantiated candidates. Its two different target-row policies both pass, so those square laws alone do not select P. The current comparison reruns that checker; it does not identify its137-row fixture with E or the native promoted type.

## Why the remaining gate is real

Inspected `NativePromotionConstructorTrace.agda` directly. It defines

    input : Before.Compared
    output : After.Compared = F.run input

and proves inherited-question transport, outer route lengths, an inherited distinction, and preservation through a second promotion. It explicitly withholds a theorem identifying F.run with T9.

The source note records a further obstruction: the unchanged free seed does not supply the face witnesses of the admitted filled fixture. A generic table reindexing cannot create them. Choosing A=Before.Compared and B=After.Compared still requires actual table row/label/source/target maps and an interpretation of the intended input. Universe ascent is not numerical rung descent.

## Verification

Executed:

    python research/strominger/checkers/check_wg_rung_schedule_comparison.py

The first attempt exposed the owner's sibling-import requirement; adding its checker directory to the runner's import path repaired execution without changing owner files.

Final run passes13 checks and four wrong-phase/count controls. It reruns the existing label/from/to suite (147 tables,1176 transitions), indexed-path suite (lengths1,2,4), and clarified rung-diagram suite with its shared-leg dependency. These source fixtures remain separate typed instances.

Receipt: `research/strominger/results/wg-rung-schedule-comparison.json`.

No fresh Agda compilation, new T9 selection, conserved uncertainty law, physical interpretation or whole-net root closure is claimed.
