# Iteration15: explicit relation evaluation in the actual shared-leg algebra

## Fresh obligation and generator assignments

The49-node net requests a non-erasing source/action binding, not another common-count argument. This iteration supplies an explicit free marked-path evaluation into the ACTUAL shared-leg quiver and checks its local right action and balanced products.

For the four-event case take left events(0,1), right events(2,3). Map a source bitmask to A until the left pair is complete, then to U until the right pair is complete, then to B. For the five-event case use left(0,1), right(3,4); event2 does not change the target object.

Generator assignments are declared, not inferred:

- edges whose objects collapse to the same target object map to its identity path;
- a left-pair completion A->U maps to ax0 or ax1 according to the last left event;
- a right-pair completion U->B maps to ay0 or ay1 according to the last right event;
- an A->B jump maps to the independent d;
- unmarked edges have coefficient1; marked edges have coefficient1/2.

The factor1/2 is an explicit evaluation policy normalizing the two singly marked summands, not a physical calibration or a uniquely forced choice. The map is extended linearly and by path concatenation. It is unital and typed. Identity images of collapsed edges are essential.

## Actual nonzero relation image

For the exhibited singly retained a and forgotten b:

    Phi(a) = ax1-ax0 = delta(ah1)
    Phi(b) = ay1-ay0 = delta(ak1)
    Phi(ab) = ax1 ay1 - ax1 ay0 - ax0 ay1 + ax0 ay0.

Paths are written chronologically; matrices evaluate right factor on the left. The product is exactly the boundary of the owner's existing(1,1) DG rectangle, with roots(0,0), not a fitted matrix. Under the actual leg assignment its matrix is

    [[0,0],[0,1/15]] = (1/15) K H,

so its detector is nonzero. It cannot factor through the old terminal recorder, which annihilates this relation product.

On the typed local basis(a,b,ab), evaluation intertwines the actual right-b action with target path multiplication, including zero extension on incompatible summands. Thus the cross-layer a->ab action is retained rather than replaced by the disconnected graded action.

## Balanced factors and retained graph packets

All eight existing five-event cases have equal NONZERO target products under their two cuts. The middle event maps to a scalar identity (1 or1/2). Each EvaluatedAnswer retains the ORIGINAL source Answer with both raw cuts and balanced seam certificate, as well as the two evaluated products. Product/graph packets are checked by recomputing evaluation; substituting an unrelated or zero target fails.

This is a graph of a specified source evaluation, not an unrelated certificate tuple. However, the source evaluation is not globally injective, and target data alone do not reconstruct every source path or mark. Recovery relies on the retained source.

## A strict candidate is rejected

In the actual target degree-zero quiver all positive-length paths have length at most2. Its positive-path ideal J satisfies J^3=0. Hence any proposed evaluation sending EVERY source edge into J kills every four-edge path and therefore ab. Such a strict positive-path map cannot meet the nonzero-detector requirement.

The constructed collapse map escapes precisely that hypothesis by sending some edges to vertex identities. The obstruction is attached only to the strict candidate, not to all possible adapters.

## Verification

Executed `python research/strominger/checkers/check_relation_shared_leg_evaluation.py`.

Twelve checks pass, including832 typed adjacent-generator composition cases across the two cubes, the actual DG rectangle equality, all eight balanced product cases, the local action square and the zero-attachment hostile. The generator prescription and multiplicative extension explain the path-algebra map; the finite checks are not an all-source kernel proof. Receipt: `research/strominger/results/relation-shared-leg-evaluation-v1.json`.

No new Agda closure is claimed. Existing source implementations are reused unchanged.

## Remaining root compatibility gate

The map is into the free shared-leg path algebra, BEFORE terminal observation. It has not been shown to induce a map of the recorder-balanced seam complexes; the source seam witnesses are retained, not renamed as target seam witnesses.

More importantly, source/root continuation policies include the shared-leg gains and drift. This turn proves compatibility with right-b multiplication but does NOT establish that the evaluated source image is stable under those additional target actions. The four selected target legs need not remain within their span after a family-gain operation.

Next: test image stability and an intertwining/lift for those already declared target gain/drift actions. If the fixed image is not stable, give an explicit source extension or parameterized evaluation with a stated context-update law; do not silently alter generator assignments. Keep formal path detection distinct from numerical matrix detection, which may vanish at particular assignments. `relation-assembly-source-binding` and the root remain open until that compatibility is resolved.
