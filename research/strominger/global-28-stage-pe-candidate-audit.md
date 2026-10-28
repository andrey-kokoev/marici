# First executable audit of the global 28-stage P/E conjecture

## Frozen question

Does an existing native reader/phase-advance operation supply the conjectured single global rotation law, without adding a 28-entry schedule? See [the conjecture](global-28-stage-pe-fibration-conjecture.md).

This audit tests candidate bindings to existing local constructors. It does not assume that local packet species already identify the conjecture's whole-object P/E presentations. Failure of a binding is not rejection of the broader conjecture.

## Actual source operations

`research/nima/generative-phase-assembly.mjs` supplies `GenerativeAssemblyRules`. Its outgoing menu includes PN, inverse-PN, NE, reader-phase-advance and NN-phase-advance where their geometric conditions hold. Every transfer validates actual reference marks, shared faces, occurrence phases and the complete five-slot coefficient permutation.

The P reader successor exchanges C0/C1 and M0/M1 while staying on its carrier. This is the double-pair swap pattern of a tetrahedral half-turn, not a newly supplied global rotation. Its coefficient permutation is [2,3,0,1,4]. The corresponding N phase permutation is [0,3,4,1,2]. Both coefficient maps square to identity; the retained realization origin nevertheless increases rather than resetting.

The phase-advance witness requires matching source and target species. Thus reader phase advances alone cannot change the P/N/E species tag. No axis/angle selector for the proposed whole complex is supplied by this local rule.

## Fresh replay

For all 24 ordered markings of the native P seed:

- Follow the unique available P reader successor through 28 transitions.
- Validate each native transfer.
- Preserve every stage's species, origin, chart, coefficient permutation and outgoing-operation menu.
- Compare this candidate with the existing PN then NE route.

Results:

| Stage | Reader-only species | Chart/coefficient behavior | Retained origin |
|---|---|---|---|
| 0 | P | Initial | 0 |
| 1 | P | Pair-swapped | 1 |
| 2 | P | Initial chart and coefficients restored | 2 |
| 28 | P | Initial chart and coefficients restored | 28 |

All 24 reader-only traces remain P. At every tested P stage the source offers **both PN and reader-phase-advance**. The available menu does not choose between them. Following only reader advance was an explicitly tested candidate policy, not a source-derived scheduler.

All 24 seeds also admit the locally validated word PN,NE: it reaches E in two transfers at origin zero. E has no outgoing operation in this grammar. These transfers are not identified as quarter/half turns of the whole retained assembly. Their local validation is not a proof of global assembly coherence.

## Disposition

1. **Reject the native reader-only candidate:** it does not perform the requested P/E exchange at stage 28.
2. **Reject identifying the existing PN,NE word with the proposed 28-stage rotation law:** it has two transfers, a different operation type, and a terminal E endpoint.
3. **Keep the conjecture open:** a whole-complex operator and its whole-object P/E readout have not been bound to this grammar. A global coherence condition might constrain local choices, but that selector has not been constructed here.

The retained origin is important: repeating the geometric/coefficient endpoint does not erase the history. But a growing origin alone neither selects stage 28 nor produces the endpoint exchange. Switching to NE when an invented counter reaches 28 would fit the target rather than derive it.

## Next missing construction

Define the candidate whole-state presentation and its reader action on shared interfaces, with an explicit whole-object P/E readout. Test whether those data select the next turn from the retained state. This must distinguish global re-presentation from local particle addition or a local species relabeling. Repeating a larger native path search without that binding would test the wrong object again.

## Reproduction and scope

`node research/strominger/checkers/check_global_28_stage_pe_candidates.mjs`

**121 assertions passed across 24 seed markings.** [Receipt](results/global-28-stage-pe-candidates.json) includes complete 29-state reader traces, native exit words and hashes of the listed source files. This is not an exhaustive dependency-closure certificate. The 24 markings are not a test of arbitrary continuous spatial orientations. No production source, viewer, other owner's contract, or global proof outcome was changed.
