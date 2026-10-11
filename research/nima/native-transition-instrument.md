# Native query recording exists; its back-action is not selected

## Construct the operation, rather than merely name a query

`agda/NativeTransitionInstrument.agda` imports the source-attached transition
query. Supply a Boolean memory register. For answer a(x), define

    R(x,b)=(x,b XOR a(x)).

The module proves R is an involution, hence an equivalence, and constructs
an ACTUAL native comparison Filler between the complete packages prepared(s)
and prepared(R(s)). On a blank register, its memory output is exactly the
native query answer. The source vertex is unchanged.

This closes a mathematical query-to-record operation. The memory carrier,
blank preparation and XOR policy are explicit construction inputs. Native
admissibility does not establish physical implementation, energy cost,
record amplitude, or an autonomous production mechanism.

## A source-supported rival, not arbitrary numeric noise

Fix the actual ABC transport and query target B. Its answer is true exactly
at source A. The source-cycle composition ADB after ABC fixes A and cycles
B->C->D->B. Call it h. The module proves h is precisely that composition,
not a new unrelated source permutation, and that it preserves this query.

Now define

    R'(x,b)=(h(x),b XOR a(x)).

R' is also an equivalence and has its own actual typed Filler attachment.
It writes exactly the same memory value as R for every input. It also
preserves the query value of the resulting source, so repeating the same
question does not distinguish their source changes.

Yet on (B,false):

    R  returns (B,false),
    R' returns (C,false).

The Agda module proves the outputs unequal through another retained vertex
observable. Therefore native admissibility, reversibility, correct recording
and query repeatability do NOT uniquely select the back-action on the whole
source. This is a bounded counterexample, not a no-go under every stronger
physical instrument contract.

If one explicitly requires the entire source to stay unchanged, that excludes
this rival and picks the nondisturbing recorder within this comparison. That
is an additional requirement, and still does not derive exchange dynamics.

## Preparation and history boundary

On the true query, a blank bit changes from false to true. This is Boolean
record production from a supplied state and memory, not mechanical excitation
from vacuum or a prepared oscillator displacement.

Using R twice on the SAME bit returns it to its original value. Reversibility
is not accumulated history retention: recording a growing history requires
fresh memory or a separately retained execution log. No free reset, elapsed
time or intrinsic clock is supplied by these bit operations.

## Consequence for the interaction programme

There is now a native-typed instrument construction, not just a conditional
numerical observer. But neither it nor its source-derived rival selects the
carrier/record exchange, a signed-charge force law, a mass readout or duration.
The remaining physical requirement must specify which source observables an
instrument preserves, which it may change, and how its memory/controller is
coupled. Counting retained witnesses cannot substitute for that requirement.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeTransitionInstrument -Fresh
    python research/nima/checkers/check_native_transition_instrument.py

Fresh safe Cubical headless closure passes with ignored interfaces and stable
inputs. 34 finite controls pass, including the source-cycle word for h,
bijectivity, answer preservation, distinct back-action and memory-reuse control.
Receipts: `results/agda-NativeTransitionInstrument.json` and
`results/native-transition-instrument.json`.
