# Opposite attachment order equals the transported route in the current marked model

## Question

Distinguish relabeling a finished nested object from performing the two attachments in the opposite order. Compare full typed routes, not just their final active values. Active obligation: attachment transport and path-level comparison before adding another geometric or physical object.

## Construction and checks

`agda/NestedAttachmentOrder.agda` gives the existing `NestedWitnessTransport.Term` syntax an explicit step type. The sole generator is append(parent,e), with its source and target retained in the type. A dependent path retains each intermediate object and append witness.

Construct the two routes independently:

    core -> attach(core,e1) -> attach(attach(core,e1),e2)
    core -> attach(core,e2) -> attach(attach(core,e2),e1).

Global label exchange acts on every object and every step witness. The transported first route is definitionally equal to the second route, including the intermediate object. This is stronger than the previous endpoint-only comparison, but follows from the same uniform attachment constructor; it is not an independent physical interchange law.

At fixed labels the first intermediate objects differ. The final objects differ, and the complete route packages are unequal. The checker proves all three facts. Thus the result does not assert that the two append operations commute at fixed marks or that their records can be erased.

## Disposition

Within the current free marked construction there is no additional discrepancy between reversed execution order and global relabeling. The available transport supplies their full path comparison; no new volume or physical correction is forced by this test. This narrows the earlier suggestion that changing order might produce an independent effect: that possibility is not realized by the actual attachment operation currently supplied.

The model's operation attaches a labelled record uniformly. It does not update an active orbital, evaluate an interaction or feed a retained parent's physical response into the next attachment. Those would be distinct source operations, not consequences of the current path syntax. The result neither proves that every physical attachment is order-independent nor selects a new state-dependent law. No additional physical branch is opened merely because this comparison closes.

Verification command:

`pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NestedAttachmentOrder -Fresh`

Fresh safe verification passed via `structured_command_execution:e_32876_1791227635774245900_47`, after resolving two imported/local constructor name clashes. Formal source: `agda/NestedAttachmentOrder.agda`; receipt: `results/agda-NestedAttachmentOrder.json`. No commit or publication is claimed.
