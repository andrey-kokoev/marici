# Existing intrinsic five-cell maps exist, but the local attachment does not select a global doublet

**Third batch, iteration 2 of 10.**

**Strength:** read-only exact reconstruction of prior conditional intertwiners and a local-readout ambiguity witness. Not a derived physical electron protocol or atlas rewrite.

[Source correspondence](ATLAS-SEED-CORRESPONDENCE.md) · [Checker](check_five_cell_attachment_bridge.py) · [Receipt](results/five-cell-attachment-bridge.v1.json)

## 1. Fresh source search corrects an overly broad missing-map interpretation

The current implementation guide, `docs/arrow-assembly.md`, points beyond the older fixed-cell obstruction to existing intrinsic spin transports and declared five-cell coefficient networks. Their owning packet is `research/strominger/diagonal-spin-networks.md`.

These constructions use geometric Pauli frames and exact reflection-word lifts, not just copied identity fibers. Therefore **absence of every mathematical five-cell map is not the remaining gate**. The old obstruction is narrower: the geometric five-cycle does not preserve one fixed attachment cell, and a geometric seed alone does not supply the physical coefficient/energy law.

This turn imports exact algebra helpers without calling owner producer entrypoints, verifies the owner packet and prerequisite hashes, and reconstructs the existing sparse maps. No shared stores or source notes are regenerated.

## 2. Explicit dimensions and maps

For each chirality the prior construction supplies:

- five two-component logical cell fibers: ten complex coordinates;
- twenty directed face ports with two components each: forty raw coordinates;
- an isometric encoding J from logical cell coordinates to face coordinates;
- two orthogonal rank-two projectors, constant C and complementary B;
- their rank-four sum Q=C+B.

The checker recovers these matrices coefficient-for-coefficient over Q(sqrt(2),sqrt(3),sqrt(5),i) and verifies J*J=I.

For either rank-two projector P, its attachment-based isometry is

    W_P = sqrt(5) * P[:, attachment columns],
    W_P* W_P=I_2, W_P W_P*=P.

All source-bound transports in the five existing cases, for both chiralities, preserve each projector. Their induced two-dimensional actions satisfy

    T W_P = W_P U_P, U_P* U_P=I.

Thus closed conditional coefficient carriers and exact transport intertwiners already exist. The chosen five-cycle lift has fifth power -I; this is a retained lift convention, not an inferred physical period or charge.

## 3. Correct source-label binding

Source pole A corresponds to geometric vertex E, index 4. Source attachment BCDE corresponds to geometric ABCD, facet cell 4. This convention is preserved explicitly; source A must not be identified with geometric A merely because their names match.

Let R restrict ten logical cell coordinates to the two coordinates of cell 4. Both global encodings satisfy

    R W_C = R W_B = I_2/sqrt(5).

Their forty-coordinate face encodings also restrict identically to the attachment cell's eight face coordinates. Multiplying that restriction by sqrt(5) gives an exact local rank-two isometry.

This intrinsic local encoding is not yet identified with the old native tetrahedral spinor fixture. That requires the next explicit face/Pauli frame adapter, not a particle-name equality.

## 4. An exact ambiguity witness

The two global doublets are orthogonal:

    W_C* W_B=0.

Yet their local readouts are identical. In particular,

    R(W_C-W_B)=0,
    (W_C-W_B)*(W_C-W_B)=2I.

The difference has rank two and is invisible at the attachment. Hence local spinor data alone cannot choose one of these global extensions. A chosen global projector remains substantive model data.

Both declared global protocols have supports 80+1520+1520=3120 and rank-two return. Exact sparse multiplication verifies N=J P J*, N^2=N and NL=N. Identical support totals do not identify the two different projectors or select a doublet.

The prior native single-cell protocol has 144 transfers. **3120 is not a replacement for 144**, a minimal-count theorem or a physical mass. Geometric transport steps are separate from the declared static L/G/N stages and require their own schedule if executed.

## 5. Updated correspondence boundary

The atlas's physical five-cell spinor/energy gate remains open, but its missing-map wording must not be read as denying the recovered conditional constructions. The refined obligations are:

1. Identify the intrinsic attachment encoding with the native tetrahedral spinor through explicit frame, metric and protocol maps.
2. Supply or justify the global doublet selection; attachment data and transfer count do not force it.
3. Retain lift signs, other carriers and any rejected records without calling them physical periods or emitted states.
4. Establish physical charge, energy and preparation separately from unitary conditional transport.

This local correction neither edits the atlas nor changes formal work-net outcomes. The scientific root remains null.

## 6. Next executable test

Construct the face-order and Pauli-frame adapter between the recovered intrinsic local attachment map and the native eight-coordinate tetrahedral spinor fixture. Verify its isometry and stage intertwining, then test how inverse five-cycle action acts on the transported logical doublet. Do not assume that inverse seed, coefficient conjugation and charge conjugation are the same operation.

## Reproduce

```sh
python research/scattering/seed-composition/check_five_cell_attachment_bridge.py
python research/scattering/seed-composition/check_five_cell_attachment_bridge.py --check
python research/scattering/seed-composition/check_atlas_seed_correspondence.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact reconstruction checks both chiralities and ten source-bound case/chirality combinations. Owner entrypoints are not called; shared artifacts remain read-only. Only this checker's local receipt is written, and `--check` compares read-only.
