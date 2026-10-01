# Dynamic membership and scoped return edits

## Explicit policy

The prototype assigns stable, nonrecycled IDs to leaf records. Each record
contains source, target and value. Source/target indexes store member IDs;
family IDs are persistent for each (index direction, group key), even if the
group becomes empty. Empty families have no mean and reject mean edits.

Each leaf event stores (ID, old record, new record). Old/new absence denotes
insertion/deletion. Applying it checks the expected old state, updates both
indexes and retains the event. The inverse event reconstructs the prior live
record state using the retained old data. Identity allocation and history are
append-only in this policy: reversing events does not erase their provenance.

A mean-edit request contains the explicit member-ID snapshot it addresses.
If the live family membership differs, reject the request before mutation.
The fixture is single-threaded; transaction/concurrent compare-and-swap semantics
and full value-version validation for batches require a separate implementation.

## Dependent edit types

An insertion supplies a new ID and complete record. A deletion supplies an
existing ID and retains its old record. A move supplies the old/new endpoint
fields. A mean edit supplies a nonempty member snapshot and requested shift.
Thus admissibility depends on the current state; an unqualified scalar delta
is insufficient to specify a changing family's edit.

At each membership state the induced mean edit cost is n*delta^2. An insertion
changes n, the mean, and all residual coordinates. For inserted value v:

    mean_next=(n*mean+v)/(n+1),
    old_residual_next_i=old_residual_i+(mean-v)/(n+1),
    new_residual=n*(v-mean)/(n+1).

The retained member values determine that transport. Reusing the old mean or
metric unchanged after insertion would represent a different operation.
Deletion and endpoint movement likewise require recomputation in affected
families. These formulas describe the scalar linear readout; raw retained
records remain the reconstruction source.

## Coherence that survives

After every admitted event, incrementally maintained source/target indexes
reconstruct the same live ID-bearing record table as a complete rebuild.
Means plus residuals reconstruct all member values; residuals sum to zero.
The induced return cost uses current member counts.

## Coherence that requires edit scope

Start with one value2. Editing its family mean by+1 and then inserting value7
produces values(3,7). Inserting first and then editing the current family gives
(3,8). Both executions follow their current-membership semantics. They are
different interventions, not an inconsistency between indexed presentations.

A request explicitly scoped to the original singleton can be rejected after
the insertion, or a different policy could apply it only to its original member.
This prototype chooses rejection. Arbitrary operations cannot be commuted by
reindexing when they address different state-dependent domains.

## Verification and scope

    python research/nima/checkers/check_dynamic_record_fibration.py

A deterministic250-operation sequence produces301 leaf events including insert,
delete, endpoint move and mean edit. After every event, exact rational checks
compare incremental indexes with rebuilt views, verify reconstruction and
induced costs, and then reverse the event history. Negative controls distinguish
insertion/edit order and reject a stale membership snapshot without mutation.

This implements one-level dynamic indexes and stable family identity policy.
It does not yet implement recursively promoted endpoint records, concurrent
transactions, distributed merge, or a general dependent-type proof. It gives
an executable contract for those extensions.
