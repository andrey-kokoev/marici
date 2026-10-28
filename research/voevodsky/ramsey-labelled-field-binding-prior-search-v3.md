# Prior research for the labelled T-seam / joint-field binding

Target: revision29's open `T-seam-joint-field-readout-binding`. This search follows the actual geometric and coefficient inputs of the44-channel candidate, rather than counting its already recorded sewing result again.

## 1. A marked P-field attachment to T already exists

`research/strominger/tetrahedral-field-attachment-v1.md` reconstructs every native P local/alignment/return coefficient from12 tetrahedral patches with three spatial components each. It supplies the explicit marking A->a, B->b, C->u, D->v onto T's P facet; scaling coordinates by1/2 matches all24 saved facet metrics without changing the projectors.

This is a real geometric starting point, not an arbitrary identification of36 slots. However, the marking and cyclic character remain explicit choices. Native N cannot be obtained from P merely by relabelling and diagonal phase/amplitude gauge: the return-projector diagonal multisets differ. A T-seam field map cannot be justified as a monomial gauge on that ground alone.

## 2. The actual N-reader attachment is already implemented

`research/strominger/neutron-reader-field-interface-v1.md` and `checkers/check_neutron_reader_field_interface.py` construct three marked belt charts onto the reader faces buv/cuv. They implement

    A(y)_i = (y_i+y_(i+12)+y_(i+24))/3,
    J(x) = (x,x,x),
    AJ=I12, JA=G, A*=J,
    AL=P_reader A, LJ=J P_reader, N=J P_reader A.

Here J denotes this source's replication map, NOT the occurrence-reflection J_r of the T-seam.

The12-coordinate reader metric is three times the sector metric. The24-dimensional kernel is retained in the original field, not reconstructed from A. The charts disagree on six shared-vertex occurrences as maps into one fixed marked tetrahedron. None of the eight tested overlap-permutation completions has identity loop monodromy; the all-even choice has order-two monodromy (b u)(c v). None of the24 marked N-facet metrics is similar to the selected belt-pair metric.

Thus this interface supplies actual labelled local data but not one fixed globally metric vertex assignment. Its internal co-moving axes must not be silently read as target Euclidean tangent axes. The finite chart obstruction does not prohibit contextual field sewing with retained transition data.

## 3. The five-to-field binding has a precise geometric seed

Inspected `research/strominger/checkers/check_full_five_channel_candidate.py` directly, with `geometric-context-and-extended-coherence-v1.md`.

Its N embedding is constructed as follows:

- columns1,2,3 populate the three native sector-local modes;
- column0 uses the unique centroid-edge patch on buv incident to uv;
- column4 uses the corresponding patch on cuv;
- each context uses the line orthogonal to its native cyclic mode, replicated over all three sectors.

The resulting five columns are isometric, C3-equivariant and reduce the N projectors. On this chosen five-space, L retains the active triple, G averages that triple while retaining both contexts, and the return averages the triple while rejecting contexts.

The P embedding is then defined by PN pullback; it is NOT independently selected from the marked P attachment in item1. The E binding uses the contrast exchange and retains the complementary baryon information. This locates the exact unresolved source-selection step: the active-window/sector assignment, context-face assignment and inherited phases are inputs to the candidate, not consequences of the native five-slot grammar.

A useful algebraic observation for the next test (not a new recorded prior theorem): Q=[4,3,2,1,0] swaps the two context columns and reverses the active triple. Consequently the displayed reduced N projector actions commute with Q. That removes a simple reduced-projector obstruction but supplies neither a marked geometric field map nor the required C0/M2 readout provenance.

## 4. Prior binding work already rejects two tempting shortcuts

`research/strominger/five-coefficient-field-binding-v1.md` and its checker establish:

- With ordered-corner N field transport U=I, a fixed B obeying B=B Pi_N has rank at most3. It cannot retain all five coefficients.
- Phase-dependent B_(r+1)=B_r Pi_N retains all five; two different isometric seeds demonstrate that norm/transport do not uniquely select the coupling.
- Outward-positive-character NN transport is antiunitary. It cannot intertwine a complex-linear native coefficient permutation through nonzero complex-linear bindings on all complex inputs. An alternating semilinear convention would be extra structure.

`reader-field-transport-v1.md` derives the distinction between ordered-corner linear transport with an orientation record and outward-oriented conjugating transport. Do not assign one of these to occurrence reversal without a separate derivation: the tested NN spatial reflection is not automatically the T-seam map.

## 5. Preserve full complements rather than demand face-only transport

`global-PN-NE-extension-v1.md` reports exact face-return fractions1/4 versus1/6. A return-preserving metric-unitary PN map cannot preserve those selected six-component face subspaces as a closed block. A return-intertwining36-to8 N/E map also has rank at most7.

`T-projector-field-v1.md` distinguishes common projector protocol from common geometric realization: native P/N return rank1 versus E rank2 blocks the simplest single-baryon reducing-subspace identification. The joint44 candidate avoids that particular hypothesis by exchanging N contrast modes with E return modes, not by identifying their return projectors.

These are constraints on particular maps, not a no-go for the labelled T-seam or the enlarged retained carrier.

## 6. Exact seam implementation remains a different interface

Read `checkers/check_T_seam_transition.mjs`. It derives Q from incoming/outgoing occurrence lists, checks reflected phase frames and verifies Q NE^-1 Q=PN and Q PN^-1 Q=NE. It does not load the field embeddings, neutron reader charts or a target field-readout constructor.

Conversely, the inspected full-five construction loads the N-reader chart receipt but does not consume the T-seam occurrence/basis record. Their geometric ingredients are closer than the previous search showed, but the actual labelled interface between these implementations was not found.

## Next discriminating source-backed test

Use the existing N chart/patch maps and the five-column seed, not a freshly arbitrary isometry. Track how occurrence reversal acts on the two selected faces, common edge, ordered axes, active sectors, context lines and phases. Then compare the resulting full-field map and its target readout with Q, retaining both C0/M2 occurrences and the entire complement. Propagate a successful local interface through the existing PN pullback and joint NE exchange only afterward.

A formula defining B_dual from Q would still be a transported construction unless this labelled readout comparison is supplied. Flat coefficient frames or arbitrary geometric port connections do not provide it automatically.

## Evidence status

This is source/report inspection, not a scientific suite rerun. Fresh checks of the recorded direct `sourceHashes` found no mismatches:

| Receipt under research/strominger/results/ | Direct pins |
|---|---:|
| tetrahedral-field-attachment/verification.json |6|
| neutron-reader-field-interface/verification.json |7|
| five-coefficient-field-binding/verification.json |4|
| full-five-channel-candidate/verification.json |10|
| global-PN-NE-extension/verification.json |7|
| T-projector-field/verification.json |3|

Direct-pin freshness is not transitive verification closure. No owner implementation, saved scientific receipt or conjecture-net status was changed. The typed binding remains open.
