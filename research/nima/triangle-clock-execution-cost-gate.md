# Execution/timing selection gate for the actual three-phase contrast

## Source policy found, and its limit

`docs/theory-page.md`, "Family formation is not execution", separates a
retained family from executing its components. Its "Paths retain traversal
resource" proposal requires additive positive traversal costs, including
attempts with zero state update. It does NOT assign primitive durations or
identify resource with elapsed time.

`native-triangle-route-to-seed-binding-audit.md` identifies an existing
ordered evaluator for a supplied coherent route. That evaluator's route
order is input; it neither schedules the entire growing six-arrow successor
family nor emits physical timestamps. Therefore it cannot silently fill
this gate.

## Test the strongest straightforward interpretation

Conditionally suppose every newly formed continuation word is one executed
primitive attempt, carrying the cost of its new final arrow. Retained prefix
history is not executed or charged again by this convention. Keep each of
the six primitive costs fixed and strictly positive, but otherwise arbitrary.

Counting ACTUAL words from the registered composition gives:

| Three-phase cycle | AB | BC | CA | BA | AD | DB | Unit-cost total |
|---|---:|---:|---:|---:|---:|---:|---:|
|1|6|6|4|6|6|4|32|
|2|26|26|16|26|26|16|136|
|3|110|110|68|110|110|68|576|

Thus, with primitive costs c_e,

    cost(cycle2)-cost(cycle1)
      =20(c_AB+c_BC+c_BA+c_AD)+12(c_CA+c_DB)>0.

This is a coefficientwise certificate for EVERY positive calibration, not
a sample using equal costs. Allowing nonnegative costs also suffices unless
all are zero. Fixed arrow-dependent durations therefore cannot make the
first two cycles equally timed under sequential execution of all new words.

## Why the workload keeps growing

The sum of the two channel endpoint profiles starts at (1,1,1,1). On its
invariant sector, the actual incidence law gives

    M(a,a,b,b)=(a+b,a+b,a,a).

Starting with a=b=1 yields unbounded Fibonacci growth. The contrast can
repeat while its containing families and execution workload grow.

If every branch really must execute, and the physical implementation has
a fixed finite work-per-time capacity, the unbounded cycle workload also
rules out a uniformly bounded period. This conclusion explicitly depends
on that capacity assumption. The source positive-resource proposal alone
is not a time or parallelism law.

## What this does NOT exclude

- Unlimited or growing parallel capacity: a different implementation policy.
- Executing only a selected branch: a different execution domain requiring
  its own justification and comparison with the family-count readout.
- Executing a compressed two-coordinate phase update: mathematically
  available, but not execution of every retained traversal.
- A new physical timing law: possible additional data, not already derived.

None is selected here. Assigning a duration simply to force a uniform clock
would insert the desired physical behavior rather than recover it.

## Result and stopping boundary

The all-n three-phase contrast proof stands. The obvious all-branch,
fixed-positive-cost execution interpretation does NOT give a uniform clock.
There is currently no source-selected execution/timing law connecting this
retained construction to physical duration. This gate needs additional
physical input or a source-derived event policy; another recurrence test
cannot supply it.

## Verification

    uv run --with sympy python research/nima/checkers/check_triangle_clock_execution_cost_gate.py

24 exact checks pass, rerunning the previous clock and reader chain.
Receipt: `results/triangle-clock-execution-cost-gate.json`.
