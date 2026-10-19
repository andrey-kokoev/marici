# Four discrete states do not retain the frozen PN task discrepancy

## Frozen test

Retain the PN task's input amplitudes, phase conventions and full native-metric
route discrepancy. Candidate: a deterministic extraction into exactly four
values, with a decoder that recovers that discrepancy on all admissible inputs.
The decoder may depend on the already fixed task/implementation, but may not
receive an additional continuous amplitude, original state or hidden context
encoding the answer. Four labelled vector spaces with continuous fibers are
not a four-value carrier and are outside this no-go claim.

Use the known invariant Q=G_P-N_P and its universal aligned-input identity
E^sharp E=3Q. Freshly replay the explicit PN task. Choose orthonormal unit
vectors u in im(N_P), v in im(Q), using normalized source-projector columns.
For t=0,1/4,1/2,3/4,1 form

    x_t = sqrt(1-t) u + sqrt(t) v.

All have unit norm and lie in im(G_P). The predicted squared discrepancy is3t.
Independently evaluate both routes using the actual PN candidate and fixed
geometric rotations, not just the expected scalar formula. Five distinct
exact outputs imply by pigeonhole that no four-value extraction plus decoder
can recover the task discrepancy on this subfamily, hence not on the full
input domain. Enumerate all4^5 assignments as a bounded negative control.

Also retain the distinction between:

- sector support: the three interior inputs have the same two occupied sectors,
  yet different discrepancies;
- four continuous sector weights: Q-weight recovers this particular scalar,
  but these weights are not four discrete states or full field recovery;
- binary pass/fail: on this restricted diagnostic family, Q-weight zero versus
  nonzero suffices for zero versus nonzero discrepancy, but discards its value;
- full field: x_t and the state with opposite relative sign have identical
  sector weights and discrepancy norms but different route residual vectors
  at an interior t, with the same phase reference.

## Scope and consequence

This excludes a four-value sufficient statistic for the frozen exact metric
readout, not all four-object categories, four-sector decompositions, four
operations or physical models. It does not require changing the source task
to achieve a chosen cardinality. The general four-state extraction conjecture
must be rejected for this selected interpretation; a continuously decorated
carrier is a separate candidate with a different retained type.

No field-wide readout-completeness theorem follows: Q-weight sufficiency here
concerns only the aligned-input discrepancy diagnostic. It does not reconstruct
relative phase, arbitrary transformations or the full36-component field.

Replay: `python research/strominger/checkers/check_four_state_task_sufficiency.py`.
Receipt: `results/four-state-task-sufficiency/verification.json`.
