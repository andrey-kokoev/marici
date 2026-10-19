# Actual carrier columns bound to retained endpoint readouts

## Fresh construction

Adapted the EXISTING arrow->state endpoint-readout law from the mass path-port research to the marked137-slot domain. The domain is unchanged:

    E'=all12 nonidentity four-state arrows except(0,1),
   121 arrow-pair slots plus16 state-pair slots.

For an arrow pair(e_i,e_j), its source and target endpoint observations are respectively

    (source(e_i),source(e_j)),
    (target(e_i),target(e_j)).

All these16 state-pair labels are already present in this domain. The actual fixture row source/target columns match these observations, with their arrow/state branch tags retained. This concretely binds those columns to CARRIER-index observations, not to the common A,B assembly endpoints.

The prior mass construction had a different153-slot inner view and excluded reference states. This adapter uses the current137 view, where all16 state pairs remain; its counts are recomputed, not transferred.

## Directed observations, not inverse connectors

There are242 arrow->state endpoint-readout events: two for each of121 arrow-pair records. Every event retains parent label and which endpoint was observed.

The plain target-state readout is noninjective. The checker records two actual distinct parents with the same observed endpoint pair. A standalone state record therefore supplies neither its parent nor an inverse operation.

Adding the prior active-arrow continuation law, restricted to the counted E' view, gives:

- one strongly connected121-slot arrow sector;
-16 sink state slots;
- every arrow slot reaches all137 slots;
- each state reaches only itself;
-16593 directed reachable slot pairs, leaving2176 unavailable.

This is SLOT transition/readout reachability. It is not the earlier14657 supported record comparison pairs, which were computed from a DIFFERENT graph and operation.

No reverse state->arrow event is added by discarding the readout direction. Continuation represents an appended edge with retained history; its last-arrow projection is not full execution recovery.

## Reversible retained observation lift

A declared classical register implementation keeps the parent and writes the endpoint into a two-coordinate four-state register:

    (parent,q) -> (parent,q XOR endpoint(parent)).

For each source/target convention, this map is bijective and involutive on137*16=2192 basis states. A blank register yields exactly the desired endpoint observation. Its inverse needs the parent AND register; it does not create an inverse from an isolated state slot to a selected parent.

This is a lossless mathematical observation encoding, not selection of a physical gate, reset law, energy cost or native filler. The earlier retained Boolean relation recording supplies the analogous principle; the present finite lift is explicit and separately checked.

## A sharper task distinction for T9

Preserving the tagged target key is stronger than preserving the endpoint STATE-PAIR observation alone.

Each of16 state pairs is observed at both:

- an arrow target fibre;
- the corresponding state fibre.

Thus a successor preserving only the untagged endpoint observation may merge those two fibres. The coarsest such successor has16 final families and1219 supported comparison pairs, versus32 families and977 pairs for exact tagged-target retention.

The checker constructs that16-family candidate using the unchanged first incoming families and a declared successor key equal to the observed state pair. It verifies original leaf retention, unchanged J4, and constancy of the state-pair observation within each final family.

There are2^16=65536 compatible kernel partitions in this candidate class: each observed pair's two first fibres may be kept separate or merged independently. This algebraic count follows from the exactly-two-fibres-per-observation audit; those65536 candidates were not all executed.

Consequently "preserve endpoint observation" alone does NOT select inherited-key T9. It must also say whether the arrow/state branch tag is a protected part of that task. The16-family candidate is a counterexample, not an authorized cross-sector connector.

## Endpoint-role conclusion

The original runnable rung fixture uses carrier-index column values. The shared-leg path assembly simultaneously has common A,B morphism endpoints. Their relationship is now explicit:

- carrier columns feed these source/target label observations;
- assembly endpoints type the response paths;
- native outer presentations type the feedback construction.

No one of these can replace another without a declared adapter and operation/observation contract.

A source-authorized readout must also say whether the branch tag is semantic information, retained provenance only, or intentionally forgotten at the next boundary. This is the next exact selection question—not whether an average matrix can be matched.

The state-matrix values are not claimed to be endpoint readouts of arrow-matrix values. This construction reads labels and retains history, while the matrix observation remains its separately declared response task.

## Verification

    uv run research/nima/checkers/check_137_retained_endpoint_readout.py

4923 exact checks pass. They include actual column equalities, all242 directed event destinations, reachability, a lossy-readout witness, retained event identity, both full-register involutions/bijections and the endpoint-only16-family counterexample. Dependencies freshly rerun the assembly/carrier endpoint audit and the existing typed numerical record chain.

No new Agda theorem, physical task selection or intended-T9 completion claim is made.

Artifacts:

- `checkers/check_137_retained_endpoint_readout.py`
- `results/137-retained-endpoint-readout.json`
