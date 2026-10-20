# Bidirectional assembly search: meeting convention works, shallow search does not match

## Construction

The operator proposed growing assembly from both sides, meeting in the middle,
and otherwise adding a layer on each side. The bounded prototype does exactly
that in the declared reversible software-control model.

Let E0 be ready-memory inclusion on the actual bright domain and J the ideal
polar embedding. A forward word F and backward word R meet when

    ||F E0 - R J|| < epsilon.

Metric unitarity gives

    ||R^-1 F E0 - J|| = ||F E0 - R J||.

The chronological joined list is the forward list followed by the REVERSED
backward list with each phase inverted. The search compares all five bright
columns in the inherited metric, implemented by whitening both domain and
codomain; it does not identify equal scalar readouts or discard records.

The target used for nearest-neighbor scouting is numerical. Any selected joined
word is submitted separately to the exact source-bound acceptance checker. The
geometric-tail polar evaluator, not the numerical target, determines acceptance.

## First control: split the existing certified word

Split the existing 468-gate word into two halves of 234 gates. Grow the backward
half by applying the inverse suffix to J in the correct chronological order.
Numerical middle and complete-word discrepancies both equal approximately
2.24943868e-7, differing by less than 1e-10. Omitting inverse-order reversal
instead gives meeting error approximately 2.27469873 and is rejected.

The existing exact full-word certificate bounds this same meeting error by
2.3444675120472308e-7 through the unitary identity above. This validates the join
convention but is not a newly discovered word or an efficiency improvement.

## Fresh bounded search

Freeze a finite vocabulary of 78 gates: all 39 source-derived conjugated bank
directions, each with exact stereographic parameter t=+1 or -1. These are inverse
cube-root phases. Consecutive gates on the same direction can always shorten
(cancel or combine into the inverse), so those candidate extensions are pruned.
No already executed history is erased; the selected candidate's actual word is
retained. This pruning uses the declared matrix-composition model, not an
arbitrary physical scheduling policy.

Both sides retain cumulative frontiers, so odd joined lengths are included.
Each round adds one operation per side, raising maximum joined length by two.

| Maximum depth per side | Boundaries on each side | Maximum joined length | Best numerical meeting Frobenius error |
| --- | --- | --- | --- |
| 0 | 1 | 0 | 2.82842712 |
| 1 | 79 | 2 | 2.78222596 |
| 2 | 6007 | 4 | 2.71616774 |

The requested tolerance is 0.01. No numerical meeting was found in this bounded
run. The best selected pair has two gates on each side. Exact certification of
its joined four-gate word gives

    1.2071856522845175 <= ||A-J||op <= 2.716167748523666.

Its scientific disposition is therefore `refuted` at 0.01, not merely
`unresolved`. The upper bound is Hilbert-Schmidt based and need not be sharp.

The source remains ready-memory bright input, the native/storage Hamiltonians
are unchanged, and candidate contacts would follow the SAME joined word. No
new record reset or scalar-only join is introduced.

## What the depth limit means

The nearest-neighbor search exhausts these numerical cumulative frontiers, but
only its selected best pair was independently certified. The run is not a
certified global depth obstruction, not a search over all exact phase parameters,
and not a no-go for deeper bidirectional synthesis. The present tool refuses
depth above two rather than silently allocating unbounded exhaustive frontiers.

Adding two search layers means one layer on each side. It is not a claim of two
new geometric dimensions or a newly proved separation invariant. No equality of
different retained histories is inferred from meeting boundary states.

The prototype stores 12014 cumulative boundary states rather than every
four-gate forward word. It makes no measured runtime-speedup claim: matching
in the full high-dimensional boundary space and frontier memory remain costs.
A deeper successor needs an explicit budget, beam/pruning policy, or adaptive
phase vocabulary. A beam would change exhaustive search into heuristic search
and must be labelled accordingly.

## Fresh execution and artifacts

    OPENBLAS_NUM_THREADS=1 uv run --offline --with numpy --with scipy python research/strominger/checkers/scout_encoder_bidirectional_meeting.py --max-depth 2 --epsilon 1/100
    python research/strominger/checkers/check_encoder_control_word_acceptance.py --epsilon 1/100 --scout encoder-bidirectional-meeting-scout.json --evaluator encoder-certified-polar-evaluator-1e-8.json --output encoder-bidirectional-meeting-verification.json

Both executions exit 0. The first reports scout-only misses; the second reports
a completed verification with `word_disposition: refuted`.

- `checkers/scout_encoder_bidirectional_meeting.py`
- `results/encoder-bidirectional-meeting-scout.json`
- `results/encoder-bidirectional-meeting-verification.json`

The scout retains forward and backward words separately, their exact joined
phase descriptors, layer counts, source hashes and the wrong-order control.
No new accepted encoder, all-tolerance baseline, formal WG proof, hardware
admission, graph publication, commit or push is claimed.
