# Actual reader contexts and the PN coefficient-image gate

## Task

Extend the separable eight-sector PN comparison test to Strominger's four actual native N reader contexts, their native NN maps, and both saved five-coefficient bindings. Keep the full-field obstruction diagnostic separate from assertions about admitted coefficient states. Source-owner files remain read-only.

## Construction

`reader_chart_transport.py` stores all eight chart rows of 36 internal components with the complete root/reader charts, absolute origins, operations and witness provenance. It stores no hidden original N fields. The inverse chart reconstructs the four source reader fields and checks the vanishing of the native chart's four detail rows. Source contexts are validated against the expected full context, not merely their self-reported digest.

The four reader slots are rechecked geometrically: each actual native component contains exactly the two source octahedral face sectors assigned to its native-diagonal coarse slot. Origins are 0,1,2,3; slot order is 0,1,3,2.

Both noncanonical saved bindings are decoded from their exact algebraic coefficients. Fresh checks establish their metric isometry and `E_(r+1) Pi_N = E_r` for the actual saved NN factors. All twenty independent coefficient basis directions are transported through all four charts and decoded. Independent records are a comparison task, not a claim that those twenty directions are one reachable history. A separate coherent native chain is checked and has vanishing difference rows.

The three NN partial channel maps are conjugated by the chart transitions. Their squares are tested on all five coefficient basis directions for both bindings and every chart. Support is compared with the source receipt, including the cases touching four coarse pairs. These partial maps are not unitary evolution on the whole direct sum. Their identity co-moving action is justified on the coefficient image only, not silently extended as a native operation on all 36 components.

## PN diagnostic and decisive promotion gate

Place each complete native PN route field, in turn, in each actual reader-labelled summand, with the other summands zero. This is explicitly a full-field diagnostic, not a five-coefficient state assignment. Decode the chart, rebuild the ORIGINAL anchored PN oracle and compare every block and its amplitude anchor. The original PN contact is not identified with these different reader cells.

For every reader slot and chart, compute the two-column workspace residual Gram and require exactly `3 I2`. Separately project the residual onto each phase-aware five-coefficient image with `E_r E_r^sharp`. Record both the projected and discarded Grams; require their sum to recover the original Gram by metric orthogonality.

This distinguishes faithful full-field transport from a proposed coefficient-level promotion. A nonzero discarded Gram is an explicit failure of that promotion: the tested coefficient bindings cannot simply be used to represent the complete PN discrepancy. No alternate binding or native source law is manufactured to make this test pass.

## Controls and boundary

Reject origin folding, reader-slot drift, a detail mode outside the native coarse image, changed NN factors and missing source contexts. Dropping target differences must either violate the image contract or change the recovered fields compared with the oracle. No authenticity or noise-detection claim is made for arbitrary field corruption that remains inside the allowed image.

Source receipts pass direct-hash freshness gates and all imported files are checked unchanged. The experiment derives no new occupied assembly, E exit, geometric PN intertwiner or physical quantum-field coupling.

## Measured result

The exact checker passes 160 coefficient-basis recoveries, eight coherent-chain recoveries, 120 NN chart squares, 64 complete PN oracle reconstructions, 16 workspace residual Grams equal to `3 I2`, and 64 composition triangles. Six negative controls are rejected or distinguished by the recovery oracle as specified.

The coefficient-image gate fails for all eight tested binding/origin pairs. Both the retained projection and the discarded complement have rank two: this projection does **not** erase the entire obstruction, but it does lose part of the actual witness. The projected Gram eigenvalues are `270/299` and `405/299`; the discarded Gram eigenvalues are `492/299` and `627/299`. Thus neither coefficient-only storage nor a claim of full witness retention is justified by these bindings. This rules out the tested promotion, not every possible alternative binding.

## Reproduce

```sh
python research/nima/checkers/check_contextual_reader_pn_transport.py
```

Receipt: `results/contextual-reader-PN-transport/verification.json`.
