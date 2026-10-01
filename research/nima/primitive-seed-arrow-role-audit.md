# Primitive seed arrows are rows, not automatically comparison equivalences

## Source distinction

The actual `TwoPacket`/seed tuple declarations retain a label, source and target. The existing formal kernel `TableFibrationCycle.Table L S T` has precisely this shape: a row type with label/from/to projections. This is a labelled span, not a collection of automatically interpreted functions between endpoint payload types.

`BoundaryGeneratedQuestions.Filler`, by contrast, is the explicitly witness-bearing comparison constructor between COMPLETE packages. The theory page's section "Retain witnesses rather than impose flatness" discusses that comparison constructor; it does not identify each primitive seed row with such a filler.

Therefore the missing pointed-filler fields found in `actual-seed-pointed-binding-field-audit.md` are not missing fields of the primitive row definition. They are extra obligations introduced by interpreting those rows as invertible package comparisons. That interpretation remains optional and unestablished, not a prerequisite for using the seed's actual table semantics.

## Concrete formal instance, without new payload assumptions

`agda/ActualSeedEndpointTable.agda` instantiates the EXISTING table constructor with four vertex constructors and the exact six occurrence constructors AB,BC,CA,AD,DB,BA. Its projections are the given endpoint assignments; labels are occurrence identities.

The module reuses `unpack-correct` and `four-correct` to prove field-preserving recovery under source grouping/unpacking and the existing four-step grouping/reversal cycle. It also supplies the six endpoint equality witnesses sewing the two directed triangles.

These proofs are about rows and their incidence. They do not create an equivalence A->B between interpreted physical value types. The equivalence in a table recovery theorem relates presentations of the ENTIRE retained row family; it is not a per-row inverse law.

Transposing the table presents the AB occurrence with source B and target A, while retaining label AB. The separately supplied BA occurrence remains a different constructor. Thus a reversed presentation is not silently a newly executed inverse or an identification of the two supplied records.

## Corrected structural boundary

The seed already has a concrete formal home without any invented Boolean filler:

    supplied occurrences -> labelled endpoint table
        -> existing grouping/recovery operations.

An occurrence can participate in endpoint-matched path composition using the already tested path-word adapter. A primitive occurrence need not be an invertible value map merely because presentation regrouping is reversible.

The remaining physical question is downstream: which source-justified interpretation/promotion turns these retained records into the desired response and rung4 observation? If that operation uses pointed comparisons, its actual witnesses and admission policy will be required THERE. The flat and general pointed binding contracts remain conditional interfaces for that interpretation, not mandatory repairs to the primitive seed.

No physical execution or calibrated readout follows from table recovery, and this four-step presentation return is not the six-step slot successor or the confirmed rung schedule by itself.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ActualSeedEndpointTable -Fresh

Fresh safe/cubical/guardedness closure passes. Receipt: `results/agda-ActualSeedEndpointTable.json`. This specializes an existing kernel to the actual seed; no payload maps, filler choices, admission policy or inverse-arrow law were added.
