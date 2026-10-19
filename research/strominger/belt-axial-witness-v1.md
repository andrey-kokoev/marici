# Source-axis preparation and an executable retained belt witness

## Construction

The actual real-complex arrow source determines a proper order-three affine action with zero translation. In its original `(r,a,b)` coordinates, let R be its linear part. Exact computation gives

    P=(I+R+R²)/3=diag(1,0,0).

P is an idempotent of rank one, RP=P, and R-I has rank two. Thus the rotation determines an axis line, without reading the desired opposite-branch signs.

Project the two retained source seeds, in their recorded order A,D. Their projections are `(7/20,0,0)` and `(-7/20,0,0)`, exactly the orbit means. Second minus first gives a nonzero fixed direction. In the original belt chart this is `(0,-7/10,0)`.

Apply the declared axial extension `beta_d(u,v)=-det(d,u,v)` to the six outward faces. The output is exactly `(-,-,-,+,+,+)`. The target branch store is loaded only after this construction. A positive-determinant shear of the coordinates, axis and faces preserves all signs and signed cell coefficients.

What is determined: the fixed axis line by the source rotation, its magnitude by the retained seeds, and its direction by their order. Swapping seed roles reverses all six signs and the entire signed chain. Neither the unpointed rotation nor the unordered seed pair selects one direction. Using the axial contraction rather than the previously tested radial contraction remains an explicit construction rule.

## Belt-specific WG instance

The generic Layer1 interface in `research/nima/agda/TypedGeneratorLayers.agda` is a state-to-output-and-witness interface; it is not restricted to the four-vertex Boolean fixture. The new Python constructor instantiates that mathematical pattern directly on a belt request.

The request retains point coordinates, face orders, axis and its projection/seed provenance. The constructor returns the induced face signs, signed tetrahedral chain and COMPLETE boundary, together with the retained request and an independently recomputable output relation. It rejects a purported witness whose output has lost the internal defects.

A second transition operates by the actual C3 vertex permutation. Its witness retains input, output, vertex map and operation occurrence. The verifier checks chain transport, boundary transport, boundary consistency and history extension. Three forward transitions return the geometric state while retaining a three-entry history. A backward transition restores the corresponding geometric state without erasing chronology; the retained input also remains recoverable from the witness.

This is a new executable finite specialization, not an Agda-compiled Layer1 term, a theorem about every WG, or an adapter from `SeedGeometricResponseState`'s different four-vertex carrier. Exact source-axis derivation is checked before admission of the request; the generic request relation itself does not authenticate caller provenance or source-select an axis.

Full request and before/after witness packets are saved in `results/belt-axial-witness/witnesses.json`. The constructor does not merely save a final sign list.

## Internal defect cannot be filled in isolation

Split the signed tetrahedral boundary into outer and internal parts:

    boundary(c)=outer+internal.

The six internal triangular coefficients have magnitude two, as in the previous audit. The new test computes

    boundary(internal) != 0,
    boundary(outer) = -boundary(internal).

There are six nonzero edges in this boundary. Therefore no ordinary three-chain b can satisfy `boundary(b)=-internal`: applying boundary again would contradict boundary-of-boundary zero. An isolated filler cancelling only those internal faces while keeping all outer data unchanged is impossible in this chain complex.

This does not refute retaining the full signed boundary as an interface record. Nor does it exclude a relative construction, altered outer/interface data, or a different coefficient system. None is silently installed here. The six orientation defects remain distinct from the 21 amplitude-comparison seams.

## Tests and scope

Prospective protocol: `inputs/belt-axial-witness-protocol-v1.json`.
Checker: `checkers/check_belt_axial_witness.py`.
Receipt: `results/belt-axial-witness/verification.json`.

Ten exact groups pass: fixed-axis derivation, ordered-seed direction, target signs, reversal, chart covariance, output witnesses, transition witnesses, retained history, hostile deletion/erasure controls, and the nonclosed internal residual. SCC targeted check passed. An export-only addition then saved full witness packets; fresh execution and frozen challenge pass at `2586d58319094ebb` (the earlier freeze is retained).

    python research/strominger/checkers/check_belt_axial_witness.py
    python research/aspect/scc/scc.py check belt-axial-witness
    python research/aspect/scc/scc.py challenge belt-axial-witness research/strominger/checkers/check_belt_axial_witness.py survives

The result supplies a source-grounded conditional axial preparation and retained execution, not selection of that coupling as physical law or a seam-free neutral assembly. Other-owner files remain unchanged and source hashes are checked. No Agda compilation, commit or push was performed.
