# Testing twelve inputs, three outputs and retained fibers

## Conjecture and precise scope

The operator proposes that an assembled coherence complex has twelve inputs,
three outputs, one destination per input and no unused output. Model this as a
surjection f:I12→O3. This does not require a unique internal history. A balanced
four-input fiber at every output additionally requires symmetry of the outputs;
it does not follow from surjectivity alone.

This local test constructs the tetrahedral candidate, checks its cut-relabeling
squares, and compares it with the unchanged native proton forward transfer.
It does NOT construct the full P/N/E complex or all physical cuts. It does not
reopen the disposed physical grading/origin programme by claiming a new scalar
or group-label coincidence selects native particles.

Prospective contract: `contracts/twelve-three-routing-v1.json`.
Checker: `checkers/check_twelve_three_routing_v1.py`.
Receipt: `results/twelve-three-routing-v1.json`.
No SCC registration, conjecture-net mutation, native producer invocation, source
replacement or viewer change was performed.

## Positive result: a source-geometric 12→3 quotient

The twelve even permutations A4 act regularly on twelve rotation labels. Its
normal four-element subgroup V4 yields three four-element fibers. The ACTUAL
proton transport matrices in `research/voevodsky/results/proton_merkle_store.json`
are verified as precisely these twelve rotations, including their marked edge
images. Therefore this is not merely an abstract numerical identification.
The fibers in native directed-edge labels are:

| Geometric output class | Four input labels |
|---|---|
| 1 | AB, BA, CD, DC |
| 2 | AC, BD, CA, DB |
| 3 | AD, BC, CB, DA |

These are the three pairs of opposite edges, retaining both directions.
All5775 unlabeled balanced partitions of twelve labels into three fours were
examined. Exactly ONE is preserved by the regular A4 action: this partition.
All144 left/right group cut-relabeling squares commute. Within-fiber swaps and
whole-fiber swaps descend to output relabelings; a single exchange between two
fibers does not. Thus cut compatibility is not vacuous.

The output class alone forgets which of four inputs was used. Retaining both
(output class, within-fiber label) reconstructs all twelve inputs. This gives
three ports with four-way retained fibers, NOT an invertible compression of
twelve independent configurations into three scalar values.

## Negative source identification: native transfer is not that routing

The exact proton source is loaded from
`results/common-three-carrier-protocol/proton.json`. The original positive
metric and L/G/N operators are retained; commuting orthogonal-projection laws
and the full raw-reader forward square are checked again.

From the actual full image encoders K_L,K_G and decoder D_G, construct

    F = D_G G K_L : C12 → M3,
    K_G F = G K_L.

Every one of the twelve input channels has nonzero coefficients in ALL THREE
output channels. The exact matrix rank is1, equal to the native active return
rank. The receipt contains the complete3×12 exact matrix, source-derived channel
labels/pivots and a concrete input/output witness. Its mode coefficients are not
replaced with a convenient routing matrix.

This is a basis-independent obstruction at the stated full-channel scope:
a weighted deterministic surjection12→3 with one nonzero entry per column and
no unused row has three nonempty disjoint row supports, hence rank3. No invertible
change of either full channel basis changes the actual rank1 into3.

This does not prohibit the discrete port quotient. It rejects identifying that
quotient with the present native complex-linear transfer between three independent
one-dimensional output channels. Geometric destination classes, coherent mode
components and internal fiber data must remain distinct.

## Disposition and next decision

* Abstract balanced cut-compatible routing: constructed.
* Correspondence with actual twelve native rotation labels: verified.
* Equality with actual native proton forward transfer: rejected at full-channel
  scope, with explicit coefficient and rank witnesses.
* Full assembled-complex map, arbitrary geometric cuts, electron admissibility
  and occupancy: not constructed/tested here.

The next question is whether the proposed three outputs mean geometric classes
with retained internal fibers, rather than the present three native channel
coordinates. Such a fiber-aware complex needs its own explicit source-preserving
maps and readers. The quotient cannot silently replace the native transfer.

## Reproduction

    python research/strominger/checkers/check_twelve_three_routing_v1.py

Fresh execution passes19 verification groups. Receipt status `pass` means both
the scoped positive construction AND the native obstruction were verified; it
is NOT acceptance of the full physical conjecture. Input/helper hashes are
retained in the receipt. No physical charge, electron-number exclusion or clock
was derived.
