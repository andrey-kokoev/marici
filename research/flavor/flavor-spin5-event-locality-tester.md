# Spin(5) event-locality tester (WP912)

## Question

Can the event-locality premise in WP910 and WP911 be challenged by an
executable test before committing to a full paired CMS run?

## Naturality requirement

For a frozen run stratum, let (F) map an event-keyed input packet to an
output record keyed by pair identifier. Event locality requires the reindexed
record to commute with:

- every event permutation;
- partition into independently scheduled batches;
- restart and reassembly at declared batch boundaries;
- retention of selection-failure nulls.

In compact form, for every tested scheduling map (pi),

\[
F(\pi E)=\pi F(E).
\]

The comparison is performed after joining by pair identifier, never by output
row position.

## Executed probe family

The checker executes 64 event keys under four orderings and four batch sizes.
Its event-local reference derives each output only from the frozen stratum and
the event key. All reordered and restarted records agree exactly.

The hostile transform also carries a mutable cross-event counter. It is fully
deterministic and replayable in one fixed schedule, but reversing two or more
events changes the pair-ID-indexed record. Resetting the counter at batch
boundaries also changes results. Thus replay in one schedule is not an
event-locality certificate.

The smallest exact falsifier is two event keys whose output records change
after their processing order is swapped.

## Instrument contract

A production adapter must record:

- frozen run-stratum identifier and software/configuration hashes;
- immutable pair identifier and event key;
- schedule, stream, batch, retry, and restart metadata;
- all seven null-completed outputs;
- pair-ID joins between both width arms;
- exact comparisons across preregistered permutation and batching challenges.

Any mismatch fails closed. Passing the finite challenge excludes the tested
stateful defects but does not prove locality for all schedules or establish
independent key acquisition. Static claims by modules are not substitutes for
the challenge record.

WP912 is an executable detector-instrument tester. It neither selects a flavor
point nor rigidifies a presentation.

Run:

~~~text
uv run python research/flavor/checkers/wp912_spin5_event_locality_tester.py
~~~
