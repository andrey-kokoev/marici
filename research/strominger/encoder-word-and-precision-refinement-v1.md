# Joint word and evaluator refinement survives the requested 0.01 falsifier

## Question and disposition

The operator requested falsification of a WG refinement process that changes both
control words and certification precision. Its proposed finite discriminator was
a new accepted word below 0.01, beyond the old word's proved error lower bound.

The test survives, with a stronger result: a new exact word is accepted at 1e-6,
with certified encoding error at most 2.3444675120472308e-7. This is a finite
refinement witness, not a proof that the heuristic search terminates at every
tolerance or a compiled formal WG term.

## Word refinement

The original 312-gate word is retained unchanged. Its exact error remains bounded
below by 0.03796922410420683, so no precision-only improvement can meet 0.01.
The numerical scout was extended only with a separate output-file argument; the
same objective, exact-dyadic phase conversion and independent acceptance checker
remain in force.

A deterministic 12-layer search with a 2500-iteration cap stops after 609
iterations. It proposes 468 conjugated bank gates with 36-bit dyadic phase
parameters. Its numerical Frobenius error is about 2.24944e-7, but that score
plays no role in acceptance. Replayed source conjugations expand to 3276
primitive operations counting inverse rotation as one macro.

This uses 50 percent more gates than the old word, not fewer. The result is an
accuracy improvement with increased gate resources, not a shorter-word claim.

## Precision refinement, separated from candidate failure

The new word first passes the requested 0.01 threshold using the existing
degree-268 evaluator. Its certified bound is 1.2095407556911325e-6.

At a tighter request of 1e-6, that SAME word with that SAME evaluator is
`unresolved_by_bounds`, not refuted. The evaluator tail dominates the upper
budget; the lower bound does not exclude the target. This is the precise case
where the process should refine evidence rather than discard a candidate.

Regenerate the exact evaluator with tolerance 1e-8. Its degree becomes 343 and
its rational tail bound is approximately 9.502336109924694e-9. With no change
to the new word, independent exact acceptance now gives

    9.047255526789342e-8 <= ||A-J||op <= 2.3444675120472308e-7.

Therefore it is accepted at 1e-6. Its nonzero lower bound also prevents treating
this second finite word as a solution at every possible accuracy.

The resulting source-bound free-storage and contact theorem supplies uniformly
in the storage parameter:

- encoding and free-storage state error at most 2.345e-7;
- decoded recovery and co-transported contact-amplitude error at most 4.689e-7.

These rounded decimals are outward displays; the receipts retain exact rational
bounds. The contacts follow the exact word, not the rounded certification arrays.

## Explicit refinement decisions

| State | Request | Evidence | Decision |
| --- | --- | --- | --- |
| Old word | 0.01 | Exact lower bound exceeds request | Change the word |
| New word, degree 268 | 0.01 | Upper bound below request | Accept |
| New word, degree 268 | 1e-6 | Neither acceptance nor refutation bound | Refine evaluator |
| Same new word, degree 343 | 1e-6 | Upper bound below request | Accept |

These are actual retained transitions in the research workflow. The orchestration
was performed explicitly through checker calls; an autonomous all-tolerance WG
refinement engine and formal composition proof are not claimed.

## Fresh execution

    OPENBLAS_NUM_THREADS=1 uv run --offline --with numpy --with scipy python research/strominger/checkers/scout_encoder_control_word.py --layers 12 --iterations 2500 --output encoder-control-word-scout-refined.json
    python research/strominger/checkers/check_encoder_certified_polar_evaluator.py --epsilon 1/100000000 --output encoder-certified-polar-evaluator-1e-8.json
    python research/strominger/checkers/check_encoder_control_word_acceptance.py --epsilon 1/1000000 --scout encoder-control-word-scout-refined.json --evaluator encoder-certified-polar-evaluator-1e-8.json --output encoder-control-word-refined-accepted-1e-6.json

The evaluator and acceptance tools now accept separate named result inputs/outputs
so distinct candidates and precisions are not silently overwritten. The previous
degree-268 evaluator, original accepted-word certificate and original 1e-8
refutation were replayed after these interface changes. The original exact word
was not edited.

Additional receipts retain the new word at coarse precision:
- `results/encoder-control-word-refined-at-1e-2.json`
- `results/encoder-control-word-refined-coarse-evaluator.json`

The final refined witness is in:
- `results/encoder-control-word-scout-refined.json`
- `results/encoder-certified-polar-evaluator-1e-8.json`
- `results/encoder-control-word-refined-accepted-1e-6.json`

## Remaining conjecture

The discriminating finite test passes. The unresolved claim is total refinement:
a fair implementation must generate candidate words and increase certification
precision without starving either process, eventually accepting every positive
rational request under the conditional software reachability contract. Numerical
optimization is a useful candidate producer, not its completeness proof.

No global optimization result, physical switching authority, formal-kernel WG
proof, graph publication, commit or push is asserted.
