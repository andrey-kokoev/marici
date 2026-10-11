# Prepopulating the actual source with three receiver arrows

## Sources traced

1. `research/nima/checkers/check_twelve_packets_to_tetrahedron.py` defines the twelve endpoint-labelled packets and groups them into source records.
2. `research/nima/checkers/check_triangle_half_phase.py` constructs a cyclic action from composable directed triangle packets.
3. `research/nima/checkers/check_twelve_triangle_positive_geometry.py` supplies the proper-tetrahedral orbit geometry, cyclic mode, transport average and dense feedback.
4. `research/voevodsky/checkers/check_proton_merkle_reassembly.py` verifies the resulting typed support and closed-traversal retention certificate.

These are not one generic graph-to-coefficient compiler. The geometry/phase constructor fixes a particular tetrahedral orbit and protocol. The audit reads the actual packet literal and actual rotation-generator declarations, and freshly verifies the retained 1836-arrow packet.

## First actual break: the receiver record is never created

The original packet constructor groups only by **source address**. With twelve complete directed K4 packets, every target also happens to be a source, so all endpoint references resolve.

Prepopulate A→e, B→e, C→e before grouping. The source records now have outgoing counts

```text
A:4, B:4, C:4, D:3.
```

There is no e record, because e has no outgoing packet. The original target-resolution condition fails. Its additional assumptions of three packets per record and reciprocal arrows fail too.

Thus the first needed extension is more basic than a coefficient adjustment: **the source language must retain a target-only receiving record**.

The new construction artifact implements that explicit extension. It creates records for all endpoints, retains all fifteen packet occurrences exactly once in their outgoing groups, and gives e a terminal-receiver role with its three incoming references. It does not fabricate any e→A/B/C return packet.

## What follows already from the changed incidence

Forgetting arrow directions and applying the existing optional clique-completion convention yields nine edges, seven triangular faces and two tetrahedral cells, ABCD and ABCe. ABC is their common face. Seven counts the internal shared face too; the outer bipyramid boundary has six triangles.

This explains the face-sharing geometry from the prepopulated graph rather than supplying it independently. It does not generate cyclic dynamics on the receiver side: none of ABe, ACe, BCe contains a directed source cycle because e is a sink. The original triangle-cycle constructor rejects those noncomposable packets.

The original proton cycles remain unchanged. No new arrow enters any closed primitive traversal.

## The chosen face must remain marked

The actual proper tetrahedral symmetry group has twelve elements. The added three-leg star on ABC is preserved by only three of them: the face's cyclic rotations.

If the new legs were blindly extended through the constructor's full old rotation orbit while keeping e fixed, the orbit would also contain **D→e**. That fourth leg was not proposed.

Therefore the old full rotation construction can remain on the proton subsystem, but the combined source must retain the marked face. Applying an unmarked old orbit recipe to everything changes the input rather than compiling it faithfully.

## The remaining coefficient boundary

The original coefficient ports are `(stage, triangle, axis)`, with 36 coordinates at each of raw, local and aligned stages. The primitive labels A,B,C are not already three scalar ports of that protocol.

Our receiving maps on K-valued A/B/C channels have a verified cyclic-compatibility meaning. To compile them into the established coefficient network, the construction still needs an explicit channel bridge and a retention observable for their equal-image witness. Neither is supplied by the old closed-return-only protocol.

A sink extension cannot affect a return to an old port when it supplies no path back. Thus closed-cycle retention alone would discard its additional transfers. Retaining compatibility alongside the old return is a substantive extension of the observable, not a new proof of the old pruning criterion.

## Count status

- Input packets: **15**.
- Endpoint-complete records: **5**.
- Unchanged retained proton protocol: **1836** typed coefficient arrows.
- Combined retained coefficient support: **not yet defined by the source rules**.

The artifact stores the last value as `null`, rather than substituting 1839 or 15×153.

The required next constructor is a **face-marked open-channel compiler**: preserve the closed proton subsystem, expose specified scalar source channels to the three receiver legs, and retain their compatibility witness. A bridge or comparison implementation must be stated before counting its coefficient transfers.

## Verification and artifact

```text
python research/voevodsky/checkers/check_receiver_source_generation.py
```

Fifteen checks pass, including the actual source failure, endpoint-complete extension, clique geometry, failed directed receiver cycles, symmetry reduction, unwanted fourth-leg control, and fresh 1836-packet verification.

`results/receiver_source_generation_store.json` is the explicit prepopulated open source: all packets, endpoint records, terminal role, cyclic receiver contract and original proton root. `results/receiver_source_generation.json` records the audit and hashes. The historical constructors and source packets are unchanged.
